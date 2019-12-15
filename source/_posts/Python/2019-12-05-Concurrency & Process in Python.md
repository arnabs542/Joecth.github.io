---
layout: post
categories: Python
tag: [] 



---



### Concurrency in Script

```python
import subprocess
import sys
import threading
import os

err = 0
suc = 0

def run():
    global err
    global suc
    ret = os.system("./tts_name \'使用。\' out.wav 1.2 3.2")
    if ret == 0:
        suc += 1
    else:
        err += 1

t = []
for i in range(0, int(sys.argv[1])):
    tt = threading.Thread(target=run)
    tt.start()
    t.append(tt)

for i in t:
    i.join()
```

------



### SubProcess & OS

#### subprocess.Popen

```python
tts_name = './aliyuntts'
outfile = 'out.wav'
speed = 1.0
pause = 1.0
role = "aixia"

pipes = subprocess.Popen("{0} {1} {2} {3} {4} {5}".format(tts_name, content, outfile, 1, 0, role), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
std_o, std_err = pipes.communicate()
print('std_o: {}\n std_e: {}'.format(std_o.decode('utf-8'), std_err.decode('utf-8')))
```



#### os.system

```python
print(tts_name)
ret = os.system("{0} {1} {2} {3} {4} {5}".format(tts_name, "早安", outfile, 1, 0, 'sicheng'))
```

------



