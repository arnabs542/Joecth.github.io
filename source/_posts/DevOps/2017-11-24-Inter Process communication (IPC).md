---
layout: post
categories: DevOps
date: 2017-11-24
tag: [] 



---

### IPC

#### Pipe

This can be only one directional.

##### Anonymous Pipe

```bash
netstat -tulnp | grep 8080
```

##### Named Pipe

```bash
mkfifo pp
echo "Pipe testing" > test // Writing data
cat < pp // Read from pipe
```

In the example above, Line2 will be blocking until Line3 is executed in other shell.

1. **Pros: Makin sure data is really taken away by the other process.**

2. **Cons: One direction 2. Low efficiency.**

   

#### Advanced Pipe

Popen; when a process is executed as a whole new process within current process, it's a sub-process of current process. Also, we called it `Advanced Pipe`.

```python
        pipes = subprocess.Popen(['cp', '-rf', src, dest], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        std_o, std_err = pipes.communicate()
        if pipes.returncode != 0:
            raise Exception("Copy SC directory Failed.. {}".format(std_err.decode('utf-8')))
```



#### Info Queue

Information queue can be used to solve the `waiting problem` mentioned in `Pipe`, i.e. not being blocked for the one which sends data, which is  similiar to buffer mechanism.

1. **Pros: not being blocked.**
2. **Cons: time wasting for huge data. (Copy takes great amount of time to access memory)**



#### Shared Memory

Shared mm can be used to solve time-wasting problem when the data copied is huge mentioned in`Info Queue`.

When a system loads a process, the memory it allocates is the `virtual memory` rather than the `physical memory`. Therefore, the virtual addresses fromt the two different processes can be mapped to the same part of physical memory to achieve `shared memory`  mechanism, even though the twos have disparate virtual memory spaces.

1. **Pros: No need to wait for so long when the data copied is too large.**

2. **Cons: Competitive problem**

   

### Semophore

Competitive problem is the most serious one happened in `shared memory`. And semaphore physically acting as a counter can be adopted to solve this problem.

It's just like a traffic light to tell a process whether the other one is occupiing this resource.

1. **Pros: Have the different process accesses the resource in turn and thus solve the competitve problem.**

2. **Cons: LIMITATION, concisely; On one machine**

   

### Socket

The 4 mechanisms mentioned above are merely `IPC` mechanism on one machine. How if we want to make available communication btw tw machines far apart from each other?

Yeah, `Socket` can be used to solve this problem. 

E.g. When we sent a http request via browser, the server returns back the corresponding data. This is what `socket` is applied in `IPC`.



