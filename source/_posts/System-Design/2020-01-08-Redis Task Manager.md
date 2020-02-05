---
layout: post
categories: SystemDesign
ag: []
date: 2019-01-08

---



### taskwork.py

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
import Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print 'Connect to server %s...' % server_addr
m = QueueManager(address=(server_addr, 5000), authkey='abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(5):
    try:
        n = task.get(timeout=10)
        print "run task %d * %d" % (n, n)
        r = "%d * %d = %d" % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print "task queue is empty!"

print "worker exit!"

```

---



### taskmanager.py

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
如果我们已经有一个通过Quene通信的多进程程序在同一台机器上运行，现在，由于处理
任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么
用分布式进程实现？
'''

import random
import time
import Queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = Queue.Queue()
# 接收结果的队列:
result_queue = Queue.Queue()


class QueueManager(BaseManager):
    '''
    从BaseManager继承的QueneManager
    '''
    pass


# 把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000,设置验证码'abc'
manager = QueueManager(address=('', 5000), authkey='abc')
# 启动Queue
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# producer
for i in range(10):
    n = random.randint(0, 10000)
    print "Put task %d..." % n
    task.put(n)

print "Try get results..."
# worker
for i in range(10):
    r = result.get(timeout=20)
    print "Result: %s" % r

manager.shutdown()

```

