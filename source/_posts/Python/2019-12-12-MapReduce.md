---
layout: post
categories: BigData
tag: [] 



---



Ref: [https://zhuanlan.zhihu.com/p/62135686](https://zhuanlan.zhihu.com/p/62135686)

# Ref1

## 一、MapReduce是什么

1. MapReduce是一种分布式计算框架 ，以一种可靠的，具有容错能力的方式并行地处理上TB级别的海量数据集。主要用于搜索领域，解决海量数据的计算问题。
2. MR有两个阶段组成：Map和Reduce，用户只需实现map()和reduce()两个函数，即可实现分布式计算。

## 二、MapReduce做什么

1. MapReduce框架由Map和Reduce组成。
2. Map()负责把一个大的block块进行切片并计算。
3. Reduce() 负责把Map()切片的数据进行汇总、计算。

## 三、MapReduce怎么做

![img](https://pic1.zhimg.com/80/v2-956054759aea4352a795452e31754ef0_hd.jpg)

1. 第一步对输入的数据进行切片，每个切片分配一个map()任务，map()对其中的数据进行计算，对每个数据用键值对的形式记录，然后输出到环形缓冲区（图中sort的位置）。
2. map（）中输出的数据在环形缓冲区内进行快排，每个环形缓冲区默认大小100M，当数据达到80M时（默认），把数据输出到磁盘上。形成很多个内部有序整体无序的小文件。
3. 框架把磁盘中的小文件传到Reduce()中来，然后进行归并排序，最终输出。

## 四、要点是什么

1. MapReduce将输入的数据进行逻辑切片，一片对应一个Map任务
2. Map以并行的方式处理切片
3. 框架对Map输出进行排序，然后发给Reduce
4. MapReduce的输入输出数据处于同一个文件系统（HDFS）
5. 框架负责任务调度、任务监控、失败任务的重新执行
6. 框架会对键和值进行序列化，因此键和值需要实现writable接口，框架会对键排序，因此必须实现writableComparable接口。

## 五、MapReduce原语

MapReduce原语：“相同”key的键值对为一组调用一次Reduce方法，方法内迭代这组数据进行计算。



# Ref2

[https://www.jianshu.com/p/6b6a42a0740c](https://www.jianshu.com/p/6b6a42a0740c)

##### 1. mapreduce 简介

mapreduce源自google的一篇文章，将海量数据处理的过程拆分为map和reduce。mapreduce 成为了最早的分布式计算框架，这样即使不懂的分布式计算框架的内部运行机制的用户，也可以利用分布式的计算框架实现分布式的计算，并在hadoop上面运行。

##### 1. 设计思想

hadoop 文件系统 ，提供了一个分布式的文件系统，但是hadoop文件系统读写的操作都涉及到大量的网络的操作，并不能很好的完成实时性比较强的任务。

但是hadoop可以给上面的应用提供一个很好的支持。比如hadoop文件系统上面可以运行mapreduce。mapreduce是一个计算的框架，mapreduce是一个分布式的计算框架，这样mapreduce利用分布式的文件系统，将不同的机器上完成不同的计算，然后就计算结果返回。这样很好的利用了分布式的文件系统。

数据分布式的存储，然后计算的时候，分布式的计算，然后将结果返回。这样的好处就是不会涉及到大量的网络传输数据。

不知道在哪里看见一句话，觉得很好，记了下来。大数据设计的一个基本的思想是**将计算的任务推送到数据所在的地方，而不是反过来。**

##### 2. Mapreduce 的架构

mrappmaster（管理节点）
 Maptask（多个）
 reducetask（多个）

mapreduce 的计算过程，举一个例子 wordcount （单词计数的例子）比如说有一个文件 ，文件内容：



```csharp
good better best never it rest 
till good is better and better is best 
```

那么第一步 先map，map的流程是，将单词以空格来切分，然后建立一个key-value的map。

得到的结果是：



```csharp
good    1
better  1
best    1
never   1
it      1
rest    1
till    1
good    1
is      1
better  1
and     1
better  1
is      1
best    1
```

上面这个map的结果，相当于给每一个每一个单词都建立一个字典，key就是单词本身，value是个数。

第二步是reduce：
 reduce是将一致的单词，发送个同一个reduce节点。在同一个reduce节点上面，这个reduce节点，负责将相同的key合并再一起。

这样就完成的单词的计数。



![img](https:////upload-images.jianshu.io/upload_images/4717565-0afa417b7248b948.png?imageMogr2/auto-orient/strip|imageView2/2/w/767/format/webp)

image.png

###### 这里存在几个问题：

**Q1:** reduce的方式是将一个类型的key，送给同一个节点。比如说，把good都送给第一个节点。till送给第二个节点。那么如果做到这一点呢？

答：使用hash表的方式，一个key，放在hash表里面，就会产生一个为一个code（java 里面的数据结构是 hashcode），然后再给它取余数。比如机器有四个节点，做reduce，那么就取余4，这样计算的任务就分给四台机器。这个就是shuffl机制。（shuffl就是洗牌的意思）（这个算法其实就是**哈希取模**的算法）

**Q2:** map 执行完成之后，中间结果保存在哪里？
 map函数输出的中间结果key/value数据在内存中进行缓存，然后周期性的写入磁盘。每个map函数在写入磁盘之前，通过哈希函数，将自己的key/value对分割成R份。（R是reduce的个数 哈希函数一般是 用key对r进行哈希取模，这样将map函数的中间数据分割成r份，每一份分给一个reduce）。**当某个reduce任务的worker接收到master的通知，其通过rpc远程调用 将map任务产生的m份属于自己的文件远程拉取到本地。**

**mapreduce的计算特点以及不足：**
 mapreduce的计算框架的优点是，极强的扩展能力，可以在数千台机器上并发的执行。其次，有很好的容错性，另外，就是向上的接口简洁。用户只需要写map和reduce函数，即可完成大规模数据的并行处理。

**mapreduce的缺点：**
 mapreduce并不适合对实时性要求比较高的场景，比如交互式查询或者是流式计算。另外，也不适合迭代类的计算（比如机器学习类的应用）。

原因：
 mapreduce的启动时间比较长，对于批处理的任务，这个问题并不算大。但是对于实时性比较高的任务，其启动时间长的缺点就很不合适了。

mapreduce一次执行的过程里面，往往涉及到多出磁盘读写，以及网络的传输。对于迭代的任务，这样很好的开销需要很多次，明显降低了效率。

而Storm和Spark，一个是流式计算的框架，一个是机器学习的框架。他们更适合解决这类型的任务。

Demo：
 一个利用mapreduce思想单词计数的实例：[http://www.jianshu.com/p/59ebf5a36ee5](https://www.jianshu.com/p/59ebf5a36ee5)

参考：

1. google的mapreduce 论文
2. 《hadoop权威指南》
3. 《hadoop 海量数据处理》



作者：zhaozhengcoder
链接：https://www.jianshu.com/p/6b6a42a0740c
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



