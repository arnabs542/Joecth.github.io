---
layout: post
categories: SystemDesign
tag: []
date: 2019-04-23
---





# General

- 打擂台算法 - 就topk

  ```python
  def secondMax(self, nums):
  	first = None
    second = None
    for num in nums:
      if first is None or first < num:
        second = first
        first = num
      elif second is None or second < num:
        second = num
      return second
  ```

  

- DB Engines, kv strorage persistence  -- , as Hash on Disk

  - Redis 常駐內存
  - DynamoDB
  - MemcacheD -- 斷電就沒了
  - RocksDB
  - Cassandra - Sharding(row) & Range Query(col)

- MapReduce

  - Word Count

    - 不是所有都可以進內存

    - 單進程單機性能問題

    - 單詞算哈希然後模機器數，同個單詞一定在同一台機器上。

    - ```python
      class WordCount:
        def mapper(self, _, line):
          for word in line.split():
            yield word, 1
      
        def reducer(self, key, values):
          yield key, sum(values)
      ```

- intersection of 2 arrays, too easy

  ```python
  from collections import Counter 
  
  class Solution:
      """
      @param nums1: an integer array
      @param nums2: an integer array
      @return: an integer array
      """
  
      def intersection(self, nums1, nums2):
          s1 = Counter(nums1)
          s2 = Counter(nums2)
  
          ans = []
          for k in s1.keys():
              # n = min(s1[k], s2.get(k, 0))
              # for _ in range(n):
              if k in s2.keys():        
                  ans.append(k)
          return ans
  ```

  

- WordBreak

  ```python
  class Solution:
      def wordBreak(self, s: str, wordDict: List[str]) -> bool:
          if not s:
              return True
            
          if not wordDict:
              return False
            
          ws = set(wordDict) # wordSet
          dp = [False] * len(s)   # means states
          # abcde
          dp[0] = s[0] in ws
  
          for i in range(1, len(dp)):
              # print(i)
              
              if s[:i+1] in ws:
                  dp[i] = True
                  continue 
              # print(dp)            
              start = i
              
              """
              dp[1] =     s[1:1+1] in ws and dp[0]    # s[1] in ws and dp[0]  
                          or 
                          s[0:1+1] in ws                     
              
  
              dp[2] =     s[2:2+1] in ws and dp[1]    ## s[2]
                          or 
                          s[1:2+1] in ws and dp[0] 
                          or 
                          s[0:2+1] in ws
              """
              while start >= 0:
                  # if s[start:i+1] in ws and dp[start-1]:
                  if dp[start-1] and s[start:i+1] in ws:
                      dp[i] = True
                      break
                  start -= 1
                  
          return dp[-1]
  ```

  

# Web Crawler

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ge8kxuh73nj30qu0b2jtu.jpg" alt="image-20200427200540662" style="zoom:50%;" />

> - 除了中文分词，英文搜索是不是也要分词？
>   - 英文搜索不用分词。你不会跟人说：hellonicetomeetyou 的。

> - 为了对网页进行分析，解析出链接信息，标题信息等，我们是需要保存整张网页的，而不只是纯文本内容。
> - 搜索引擎的相关技术每一个都是一个深坑，慎入！在系统设计的面试中考得最多的当然还是 Web Crawler。另外关于倒排索引（Inverted Index）和 分词（Word Segmentation）的技术最好也是要知道的。



## Inverted Index

- 從 word 指向 doc id list 的索引 (index)
- 反過來就是 forward index (doc id -> list of words)

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ge8l2imdk0j30z80b8gwi.jpg" alt="image-20200427201034185" style="zoom:67%;" />

> - 当用户搜索 Hello World 的时候，搜索引擎会去倒排索引中检索 Hello 和 World 共同出现的文档有哪些，并且求出交集。



## Chinese Word Segmentation

中文分詞字字間沒有區分 e.g.化妝和服妝

- Viterbi Algorithm
- Word-break
- 早期 G廠在中國沒做所以有一陣子時被B超過





# Design Crawler

## Scenario

- 全抓下並建 inverted index

- 網頁間存在指向的anchor關係
- 節點 & 有向邊
- Google 立身之本- ”page rank” 看各網頁被引用的高低
  - 被更多其他網頁指向的網頁，具有更高的價值

### 開始爬的網頁

- as seed urls
- 新聞網站作起點很好、Alexa(Amazon下的做的看流量排名)也可以



### Producer/Consumer

- BFS爬，在有向圖上爬

> ##### [单选题]Web Crawler 一般可以使用哪种算法？
>
> A.深度优先搜索 DFS20.53% 选择
>
> B.宽度优先搜索 BFS79.47% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 互联网上的网页所构成的图巨大无比，如果使用 DFS 的话，深度太深也不易加入并行化的处理。使用 BFS 比较直观和方便。

- DFS會讓我在抓時一個網站都還沒抓多少就跳走了。
- 解析快；抓慢



### 多進程抓

> ##### [单选题]单进程(single process)模型的爬虫的瓶颈是什么？
>
> A.解析网页的速度太慢18.17% 选择
>
> B.网络请求慢，单进程大部分时候处于闲置(idle)状态81.83% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B

> ##### [单选题]开 2000 个进程是否可以做到每秒钟下载 1000 个网页？
>
> A.可以10.21% 选择
>
> B.不可以89.79% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 下载效率还受限于 CPU 个数和带宽。2000 个进程会导致大量的进程上下文切换（Context Switch），从而导致代码运行效率下降。

所以10個核的話啟100個process

> - nonblocking IO呢？
>   - non-blocking IO可以在一定程度上解决这个问题，不过单机的并发数始终还是有瓶颈的，当并发的IO数目达到一定数量时还是需要向distributed的方案转变。
> - 请问多process和threading的区别是？
>   - 多process不共享同一片内存，多 thread 共享同一片内存。



## Storage

### 網頁存儲 

> ##### [单选题]爬虫抓取下来的网页存在哪儿？
>
> A.爬虫这台机器上8.22% 选择
>
> B.分布式文件系统中（Distributed File System）91.78% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B

這個文件系統還需要給indexer作inverted index，所以不放給爬蟲，

這樣一人作兩角會破壞爬蟲自己的是stateless的思想。

爬蟲要不怕掛，就重啟，跟數據庫不一樣；愈多stateless的系統愈穩定。

> ##### [多选题]下列哪些东西是 Stateless 的？
>
> A.Web Server34.37% 选择
>
> B.NoSQL Database9.55% 选择
>
> C.SQL Database5.26% 选择
>
> D.Memcached18.27% 选择
>
> E.Async task worker (message queue consumer)32.55% 选择
>
> **正确答案:**AE
>
> **解析:**
>
> 任何存储数据的服务器都是 stateful 的。只执行代码不存储数据的一般是 stateless 的如 Web Server, Async task worker



### BFS中的Queue以及HashSet怎麼存的？

#### Queue

- linkedlist in java

- hash for visited

> ##### [单选题]BFS算法中使用到的 Queue 存在什么地方？
>
> A.在内存里直接开一个 Queue5.85% 选择
>
> B.使用消息队列（Message Queue）74.03% 选择
>
> C.使用 Memcached20.12% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B

放內存就要擔心斷電的問題。

#### 

#### HashSet

> ##### [单选题]BFS 中的 HashSet 在系统设计中适合使用什么来存储？
>
> A.内存中开一个哈希表3.14% 选择
>
> B.Memcached21.68% 选择
>
> C.SQL Database4.26% 选择
>
> D.NoSQL Database (Key-value Storage)70.92% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是D
>
> **正确答案:**D



> - message queue是不是stateful的？
>   - 是的
> - 为啥这里不用sql数据库存hashset，如果是多线程并发，要先查set中是否已经存在，然后不存在的话，写入，这是一个事务操作
>   - 从这业务分析，我们可以知道是对每一个domain（域名）中的所有url进行耙取的，而url与其domain的关系1：n的关系，所以，我们在选择NoSQL的数据中，其存储结构是key-value的简单关系结构(key是domain-name，value是List[url])，而且NoSQL系统，其所对应的是Map的结构，而不是Set的结构。如果是多线程。我们要有一个类似信号量的控制访问数据库的锁（如Java.util.concurrent.ReentryLock的使用），即可，不需要事务，事务花销更大，而且大多数NoSQL不支持事务。



## 可行解

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ge9sne1pgkj30wy0h2wng.jpg" alt="image-20200428211834537" style="zoom:67%;" />

- 注意第７行不是用recursive的，而是讓它去排隊，避免stack overflow



### Robot 協解

爬蟲協議。

> - 请问robot协议算是CORS的一种吗
>   - robot协议是针对爬虫的，告知爬虫对本网站数据的爬取规则。
>     CORS(Cross-Origin Resource Sharing)跨域资源共享是访问跨域资源时，浏览器与服务器应该如何沟通。是为了解决浏览器的[同源禁止访问策略](https://en.wikipedia.org/wiki/Same-origin_policy)。
>     CORS背后的基本思想就是使用自定义的HTTP头部让浏览器与服务器进行沟通，从而决定请求或响应是应该成功还是失败。

> 这是知乎的 robots 协议：https://www.zhihu.com/robots.txt
> 更多的关于 robots 协议的规则感兴趣的话可以看看 https://baike.baidu.com/item/robots/5243374?fr=aladdin



### 限制爬蟲的頻率

Queue 裡可能對同一個站同時抓太多次。

***让 Crawler 只做 Consumer，不负责产生新的抓取任务 新增一个 Scheduler (Producer) 负责调度和生产抓取任务 在 Database 中记录每个网站下一次可以友好抓取的时间***

> - 实际应用中是不是爬虫都有这个scheduler，并不是consumer和producer都爬虫自己做
>   - 是的，一般实用的爬虫框架都会有单独的scheduler，如果对实际的爬虫框架感兴趣的话可以看一下这两个开源的python爬虫框架：pyspider, scrapy



## 更可靠的解

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ge9v4lect4j310e0gytgt.jpg" alt="image-20200428221447375" style="zoom:67%;" />



### 表單內容和偽代碼

> - 课程里说这个UrlInf value里的status代表有没有抓过，有什么用吗？感觉结合后面反复抓取的情况，可能存的是抓取是不是成功的信息，这样可以计算下次抓取的时间（backoff)。不知这样理解对不对？
>   - 一般数据库里我们 status 是最常用的一个 field，用来表示一个事情的进展。 URL 在抓取的过程中，有很多的中间状态的 status，比如抓取成功，抓取失败，正在抓取，还没有抓取过。没有被抓取过的意义是，你可以知道现在有多少网页正在抓取，多少发现了还没抓取，多少已经抓下来了，多少可能是坏链接。这对于监控爬虫的正常工作情况有重大意义。
> - 为什么候选的UrlList要单独放张表，不可以作为DomainInfo的value 的一个Field吗？
>   - 你可以尝试使用一下 MySQL 之类的数据库，你会发现并不能找到一个 List 类型的 field。原因是 List 类型作为普通 MysQL 数据库的的 Field 的话，插入和删除都是 O(N) 的。因此为了更好的支持这种 key to list 的增删查改，要么在 SQL 数据库里用一个张单独的表单，以二元组的形式存储，如 `<domain1, url1>` `<domain1, url2>`，要么放在 redis 这种 value 支持 list 的数据库里。总之无论如何，都无法直接和 DomainInfo 放在一起，且数据的含义上，UrlList 也不属于一个 Domain 的 info。info 一般指一些 metadata 之类的信息。

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ge9v4yins0j30uo0kgnbr.jpg" alt="image-20200428224429124" style="zoom:67%;" />



### 分地區的爬蟲



### 處理更新抓取與失效

BFS裡會有HashSet看抓過沒。但會有更新，怎辦？

可 Exponential Backoff去試，搭配邊界。

> - 怎么处理不存在的老的链接呢？
>   - 总是抓取失败的话，就在 UrlInfo 里标记抓取失败，且下次要抓取的时间通过 Exponential Backoff 会慢慢变得很长，比如30天抓一次这种。

- 可md5 16字節看是否一樣，放在url表單裡。

> - 如果一个网页变化了，有URL链接的变化怎么处理？是不是把原来存的DomainInfo和UrlInfo都更新（删掉老的数据）？
>   - 比如 www.jiuzhang.com 对应的网页变化了，只需要更新这个 URL 下的网页内容。DomainInfo 和 URLInfo 做一些相应的更新，比如 webpage md5之类的。这个跟这个网页里的 Url 链接是否发生变化没有什么关系。网页里如果发现了新的 URL 就再加到数据库和待抓取列表里即可。

> 指数补偿(Exponential Backoff)指的是，在执行事件时，通过反馈，逐渐降低某个过程的速率，从而最终找到一个合适的速率（来处理事件）。
>
> 指数补偿通常用于网络和传输协议，比如在进行网络连接时，如果第一次请求失败，那么可以等待 *t1* 秒之后重试，如果再次请求还是失败，那么等待 *t2* 秒之后重试。重试可以一直继续下去，直到等待次数或等待时间超过特定值为止。
>
> 等待的时间 *ti* 是可以自由指定的，常用 1, 2, 4, 8 这样的指数序列，因此叫指数补偿。
>
> 类似的用到了指数补偿思想的场景还有动态数组（C++ 里的vector，Java 里的 ArrayList，Python 里的 list），动态数组之所以支持你不断的往里加入新元素，就是因为当一个数组满了以后，会再创建一个新的两倍元原来大小的数组来替换掉旧数组。



> 这个文章的作者用 20 台 AWS 的机器在 40 小时内抓取了 2.5亿篇网页，只花了 580$。
>
> http://www.michaelnielsen.org/ddi/how-to-crawl-a-quarter-billion-webpages-in-40-hours/
>
> 这篇文章中很多的内容是值得参考的比如如何拆分爬取任务的部分，作者的目的是单纯的抓取网页，和我们今天所设计的爬虫相比自然是我们课上讲的架构会更加适合一个真正的爬虫系统。







# Design TypeAhead v.s. Google Suggestion

兩種不同類型的

1. Typeahead.js 
2. Google Suggestion

- Trie - Re**trie**val

### Front End

### Back End

- QPS issue



## Scenario

- 返回被其他人蒐得多的 Top10 queries

- 個性化算法的架構

- 推算QPS ==> 要練心算速推

> ##### [单选题]Google Suggestion API 主要是读还是写？
>
> A.读96.80% 选择
>
> B.写3.20% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A

- 當讀多寫少時，就是用Cache進行優化



## Service

提供Top10Query 查詢

- QueryService
- CollectionService (敲了Enter後)

> ##### [多选题]为什么我们不让 QueryService 直接请求 CollectionService 获得结果？
>
> A.因为用户很难感知数据是否是最实时的，有一点延迟没有关系36.79% 选择
>
> B.因为 QueryService 请求 CollectionService 实时计算的话，会比较慢43.16% 选择
>
> C.QueryService 请求 CollectionService 的服务器间通信比较慢20.05% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是AB
>
> **正确答案:**AB
>
> **解析:**
>
> 服务器间通信是很快的。慢的是计算。

> - 这里CollectionService提供给QueryService信息是用的push模式吗？
>   - Yes



## Storage

### for Query Service

> ##### [单选题]是否有支持 Trie 的数据库？
>
> A.没有63.90% 选择
>
> B.有36.10% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A
>
> **正确答案:**A

- 沒有現成的數據庫，也不大可能自己去寫一套。

  替代品就是kv storage，如RocksDB, Redis

  kv在空間大一些，但就是系數上的大而已



當Collection Service拿到 apple, 

就要新增 a, ap, app ... 等的 key，讓他們都append 一次apple，然後打擂台映射到top10的list 



> - Trie的工程上应用意思是什么呢？实际工作中用吗？
>   - Trie在工程上用得很多，Trie的优势是O(字符串长度)的查找时间和良好的空间性能，相同的前缀只会存一份，因此适合在需要对大量字符串进行存储和查询（尤其是前缀查询）的场景。实际工作中有很多使用Trie及其变形的例子，像这里讲的search suggestion，还有IDE的auto complete, 浏览器的url历史补全，编辑器的spell checkers都可能会用到trie.
> - ”如果某个prefix已经存在了被搜索次数更多的其他10个 queries，就无需再加入了“。两个问题，1）怎么知道是被搜索次数更多的？加入的条件不是一样的吗，比如这里的1b 2) 更新一下是不是更好，因为是更新的结果。
>   - query 的搜索次数是会被 collection service 记录下来的。比较的时候是带着次数一起比较的。prefix -> top 10 的记录格式是 `[{"ap": {"query": "app", "count": 100}...}]`
>   - 更新 Top 10。



### for Collection Service

蒐集每個Query 被蒐的次數

###  

```python
class Node:
    def __init__(self, is_end=False):
        # self.val = val
        # self.next = None
        self.children = {}
        self.is_end = False

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        # self.children = {}
        self.head = Node('$')
        
    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        node = self.head
        for ch in word:
            # print(ch)
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.is_end = True
        
        
    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        node = self.head
        for ch in word:
            # if ch not in self.children:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
        
    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        node = self.head
        # print(self.children)
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```



## Scale 

### 優化 (prefix => Top10的構建) with Probability　

不是每條過來的query都有機會成為 top10

萬分之一去命中再把計數加一

> ```python
> class QueryService():
>     @classmethod
>     def should_log():
>         return random.randint(0, 9999) == 0
> 
>     @classmethod
>     def log_query(cls, query):
>         if cls.should_log():
>             database.query_count_plus_one(query)
> 
> ```



prefix => Top10的構建

### 打擂台太慢，可以改MapReduce



### 用戶打字太快怎辦？

跳過去！前端等待延時後再發請求。QPS一下可降3~5倍



### 後端 Backend Cache 優化

100M+ QPS的優化：

-  Backend Cache, 每次更新prefix to top10 去主動更新，PUSH 的方法。
- 不要懶惰加載



### 前端 Frontend Cache 優化

- 用戶可能常敲一敲再回刪
- 前端本地直接拿肯定更快
- 可再加設有效期 (小時、天為單位)



### 預加載

兩層次的預測加載，如ap的時候，就把app的top10也拉出來了 (因為對於ap而言，app比第二名的高)，就也是一種偷跑。

系統內的通信比用戶的前端跟後端的通信

> refetch 之前的 http response 可能是这样的：
>
> ```
> {
>   "prefix": "ap",
>   "top10": [
>     "app store",
>     "apple",
>     ...
>   ]
> }
> ```
>
> 有了 prefetch 以后，http response 可能就是这样的：
>
> ```json
> [{
>   "prefix": "ap",
>   "top10": [
>     "app store",
>     "apple",
>     "amazon",
>     ...
>   ],
> }, {
>   "prefix": "app",
>   "top10": [
>     "app store",
>     "apple",
>     "apple id",
>     ...
>   ],
> }, ...
> ]
> ```





## 實時熱門的 Top10 

Prefix=>top10要是每天一次的更新，趕不上突發事件。

怎麼把熱門的也加進去？這過程是比較慢的，因為量大

＝＞處理最近兩小時的Query Logs ，數據量小甚至不用map reduce, 直接for就ok

也不打機率打折扣

跟過去一年或更久的作權重分配合併。





# QA

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ge8kucucubj30ke0to40t.jpg" alt="image-20200427200250304" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ge8kyowkhij30kg0o40uz.jpg" alt="image-20200427200706721" style="zoom:50%;" />