---

layout: post
categories: SystemDesign
tag: []
date: 2019-03-18

---



- ### Web Server

- ### DB

- ### File System

- ### Cache



# 知識補充

## Merge K Sorted Lists

- 三種方式

  1. Heap, NxLg(K)

  2. 可說是 2A, NxK

     ![image-20200725184659925](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3ess84kjj30fu09edh7.jpg)

  3. 可說是 2B, NxLg(K)

     ![image-20200725184735971](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3eteo2k7j30k60bojts.jpg)

     ![image-20200725184803623](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3etvcsy4j30ho0b277b.jpg)

  4. ★★ D&C
     ![image-20200725185221462](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3eycvecfj30ue0getbh.jpg)

     猜到NxLog(K) 意謂著可知道每層、及stack的高度
     ![image-20200725185411349](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3f0a0t6lj30uk0eejvq.jpg)

     ![image-20200725185456319](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3f115lfij30nu0ds0uw.jpg)

​					

​					![image-20200725185540406](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3f1t38vkj30qu07k416.jpg)



-  Compare to M-Sort

![image-20200725185531135](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3f1mt8x4j30ny086mzm.jpg)



## 名詞們

- Web Server, 比較好企業級的 1K/sec，自己搭的10/sec就不錯了
- DB based on File System
- File System 接口單一，非結構化適合直接就放在FS, 而不是DB
- Cache



> ##### [单选题]【系统设计2020】下面哪个"不是"常见的用做消息队列（Message Queue）的软件
>
> A.RabbitMQ3.23% 选择
>
> B.Redis19.35% 选择
>
> C.Memcached64.52% 选择
>
> D.Amazon SQS12.90% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是D
>
> **正确答案:**C
>
> **解析:**
>
> Memcached 是一款缓存（Cache）软件，是单纯的 key value 结构，不支持队列结构。

# Design Twitter

```python
'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
from collections import defaultdict
import heapq
class MiniTwitter:
    
    def __init__(self):
        # do intialization if necessary
        self.users = defaultdict(list)  # self's tweets
        self.following = defaultdict(list)  # as an Adjacent list 
        self.article_id = 0
    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        tweet = Tweet.create(user_id, tweet_text)

        self.article_id += 1    # necessary for time info
        self.users[user_id].append([self.article_id, tweet])   # TODO: WRONG, requires time info for
        
        return tweet
        
    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here
        rt = []
        if user_id in self.users:
            rt = self.users[user_id][-10:]

        if user_id in self.following:
            for friend in self.following[user_id]:
                if friend in self.users:
                    rt.extend(self.users[friend][-10:])

        rt.sort(key=lambda x: x[0])
        return [tweet[1] for tweet in rt[-10:][::-1]]
        
        
    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed_mywrong(self, user_id):
        # write your code here
        # return []
        # if user_id not in self.users:
            # return [] # 給沒建帳號也可以呼叫follow函數…
        res = []
        if user_id in self.users:
            res = [mypost[1] for mypost in self.users[user_id][-10:][::-1]]
        
        # print('aaaaa', res)
        if user_id in self.following:
            for i in self.following[user_id]:   
                # res.append(self.users[guy_id])
                # res.append(self.users[i][-10:])
                if i not in self.users:
                    continue
            
                this_user = []
                this_user.append(like[1] for like in self.users[i][-10:][::-1])
                res.extend(this_user)
        print(res)
        return res
        
    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        if user_id not in self.users:
            return []
            

        return [like[1] for like in self.users[user_id][-10:][::-1]]

        
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        # if from_user_id not in self.following[from_user_id]:
        self.following[from_user_id].append(to_user_id)
        
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        friends = self.following[from_user_id]
        try:
            idx = friends.index(to_user_id)
            self.following[from_user_id] = friends[:idx] + friends[idx+1:]
        except Exception as e:
            print('This guy has no this friend!')
```



## 反應

- 當收到題目時，該如何？
  - 互動! 你想過沒有：或許現在只有2個用戶呢？
  - 所以：
    1. 可行解
    2. 特定問題
    3. 分析能力
    4. 權衡
    5. 知識儲備
  - 4S
  - ↓↓



## General

1. 注意事項：
   - 這個問題要考慮的用戶規模有多大？
   - 有哪些功能需要我設計的？
2. Key words: 
   - Load Balancer, Memcache, NodeJS, MongoDB, MySQL, Sharding, Consistent Sharding, Master Slave, HDFS, Hadoop...
     - How if only 2 users?...  No need all above... So, **ASK** for clarification first!
3. 側重：
   - Work solution
   - Special Case
   - Analysis
   - Tradeoff, PlanA vs PlanB
   - Knowledge Base, e.g. DB, FS, Memory, Info Queue



4. 4S analyzation
   - Scenario
     需要設計哪些功能？功能要到多厲害？
     Ask: Features, QPS, DAU, Interfaces
   - Service
     將大系統拆分為小服務
     Split Application, Module
   - Storage
     數據如何存儲與訪問
     Schema: Data, SQL, NoSQL, File System
   - Scale
     怎麼解決缺陷，處理可能遇到的問題
     Sharding, Optimize, Special Case



## Scenario 場景

1. Ask; 2. Analysis

- **需要設計哪些功能？**
- **需要承受多大的訪問量？**
  - DAU
  - **Twitter: MAU 330M, DAU ~170M+** == > 一萬台機器搞定?1

有些公司會用註冊用戶，但這不準。一般要看MAU。

> ##### [单选题]下面说法中，"不"正确的是
>
> A.MAU 会影响到 DAU，DAU 会影响到并发请求的用户数，从而影响到系统的承载力5.37% 选择
>
> B.一个用户一个月登陆了3次，会累加 3次 MAU77.78% 选择
>
> C.一个用户一天登陆了10次也只算一次 DAU9.55% 选择
>
> D.MAU 和 DAU 的比例通常是 2:1 左右7.30% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> B是错的，一个用户一个月登陆 100 次也只算作 1 次 MAU



### 需要設計哪些功能

Step1. Enumerate - 把 Twitter 的功能一個個羅列出來

- Register/ Login
- User Profile Display / Edit
- Upload Image / Video * 
- Search *
- Post /Share a tweet
- Timeline News Feed
- Follow Unfollow a User

Step2. Sort - 選出核心功能, 因为不可能這麼短時間什麼都設計

- **Post a Tweet !**
- Timeline
- News Feed
- Follow / Unfollow a user
- Register / Login

 

- 看估計：60代表每個用戶一天點60次

![image-20200725195638005](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3gt8wd00j30ro0de43l.jpg)

![image-20200725200005606](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3gwuuj71j30x40f2k0r.jpg)

> - 感觉老师对于服务器qps不太对啊，我查了一下资料，一天4核8G的腾讯云主机TPS就能达到15k呢，qps就更多了，可以达到30w.这个是链接。https://www.youtube.com/watch?v=CX6wS5j7FWw&t=237s。数据规模1千万。如果只是按照1k来估算的，最后结果会相差很大的。
>   - 如果只是返回简单的静态文件，你说的这个配置都能达到千万级别的qps，但是如果每个请求需要处理的逻辑复杂的话qps就会很低的。
> - QPS 的 query 是指访问一次某个接口，还是访问一次数据库？
>   - 根据场景不定，衡量并发的性能就是说每秒能承受多少用户访问，衡量数据库读的性能就是说每秒能承受多少次读取数据。
> - 在设计推特的时候，一个用户浏览新鲜事的qps和她浏览自己timeline的qps需要分开估计吗？
>   - 需要分开估计的，用户浏览新鲜事的qps 肯定 比 浏览自己timeline的qps 高一两个数量级的。



> - Read QPS: 是对数据库的操作频率
>
> - TPS = Transactions Per second
>   QPS = Queries Per second
>   一个 Transaction 里可能会有多个 Db Query。
>   一般来说我做这么细的区分，统一都用 QPS 就可以了。
>
> - mongodb, dynamodb 的QPS大概多少:
>
>   - 根据机器配置不同，是不一样的。大概在 1w~10w 这个级别。
>
>   <img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd6gby3ys1j30x40ewac9.jpg" alt="image-20200325203515823" style="zoom:50%;" />
>
> - SQL vs NoSQL 大概有几个原则：
>
>   1. 大部分的情况，用SQL也好，用NoSQL也好，都是可以的
>   2. 需要支持 Transaction 的话不能选 NoSQL
>   3. 你想不想偷懒很大程度决定了选什么数据库，SQL更成熟帮你做了很多事儿，NoSQL很多事儿都要亲力亲为(Serialization, Secondary Index)
>   4. 如果想省点服务器获得更高的性能，NoSQL就更好硬盘型的NoSQL比SQL一般都要快10倍以上
>
>   这个NoSQ跟SQL的选择没有一套万能的方法去告诉你应该怎么选，需要了解各种数据库的优缺点，根据场景需求灵活选择。
>
> -  NoSQL 的数据结构比较简单，支持的查询操作也比较简单。结构简单的话，处理效率就高。SQL 为了支持一些很复杂的查询，所以处理效率较低。
>
> - Database 里index query是啥呀
>   - 就是说查询的时候，database 通过 index 进行查询，会比一个一个数据查过去的方式更快
>   - select * from xxx table where yyy=1, 如果 yyy 有 index，就是一个 index query，否则就是一个 sequential query
>   
> - join应该是变慢，index query是加快，为什么都会让qps变小呢？
>   
> - index query 这里指的是相对于按照 primary key(id) 去 query。因为 index query 要先query index 的内部表，再去具体的表单里取数据，相比直接通过 id 去取数据要慢的。
>   
> - 为啥NOSQL承受量这么多， 跟SQL比起来
>
>   - 因为 NoSQL 的数据结构比较简单，支持的查询操作也比较简单。结构简单的话，处理效率就高。SQL 为了支持一些很复杂的查询，所以处理效率较低。
>
> - join应该是变慢，index query是加快，为什么都会让qps变小呢？
>
>   index query多所以查询速度快，所以每秒可处理的query更多，所以qps的值不是应该更大么？课件上说join和index query多的话，qps会小。。 ?
>
>   - index query 这里指的是相对于按照 primary key(id) 去 query。因为 index query 要先query index 的内部表，再去具体的表单里取数据，相比直接通过 id 去取数据要慢的。
>
>     



## Service

將大系統拆分為小服務, 如 **SOA, Service Oriented Architecture**

合併需要設計的功能，相似的功能整合為一個Service - 邏輯處理的整合

1. Replay 重放需求
2. Merge 歸併需求

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd6gnly99kj30oc0bead6.jpg" alt="image-20200325204630511" style="zoom:50%;" />



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3h5eovytj30bm06imyu.jpg" alt="image-20200725200820199" style="zoom: 67%;" />



## Storage

![image-20200725200946414](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3h6wynfqj31160h046y.jpg)

- **我們會想根據一個人的電話或email或地址去查他，所以關聯型**

- tweet 的查詢一般就是找id，所以nosql中比較合適，且天然自帶sharding



- 现在 id 一般要用 Bigint （64位）才不会担心溢出。
- 細化數據表單
- 畫圖展示數據存、讀過程
- 為每個Service選合適的儲存



> ##### [单选题][系统设计2020]关于文件系统和数据库系统之间的关系，下列说法“不正确”的是？
>
> A.数据库系统是建立在文件系统之上的，也就是说数据库系统中存储的数据最终都是要存在文件系统上的23.96% 选择
>
> B.文件系统中可以支持丰富的数据查询接口，如在记录用户信息的文件中快速挑选出所有身高在 175 到 185 之间的男性53.13% 选择
>
> C.我们一般将结构化的数据（Structured Data）放在数据库系统中，把非结构化的数据放在文件系统中15.63% 选择
>
> D.文件系统和数据库系统都是可持久化的存储系统7.29% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 数据库系统是文件系统的一层“包装”，将数据结构化的存储起来，从而可以支持更丰富的数据查询方法。如筛选某个属性在某个范围内的所有数据。而文件系统一般就是支持最简单的查询方法：取出某个文件从第x个字节开始的长度为y的所有数据。

![image-20200725201756110](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3hfje89fj310c0cqqf0.jpg)

![image-20200725201830146](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3hg34ifxj310y0h6wo6.jpg)



NoSQL 有index吗？

有的，MongoDB就支持索引http://www.runoob.com/mongodb/mongodb-indexing.html。
索引就是帮助快速定位数据的一组附加信息，可以用在NoSQL上。

> ##### [单选题]为什么 User Table 里不用 username / email 作为 Primary key
>
> A.因为两个用户可能使用同一个 Username23.95% 选择
>
> B.因为数据库只支持整数作为 primary key6.02% 选择
>
> C.因为 email 要区分大小写，查询相对较慢4.06% 选择
>
> D.因为很多网站支持用户修改 email 和 username65.97% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是A
>
> **正确答案:**D
>
> **相关知识点:**主键和外键 Primary Key & Foreign Key
>
> **解析:**
>
> 如果用 username / email 作为 primary key，会因被其他 table 引用而存储在其他的 table 中，如果被修改，会引起一连串的修改，效率很低。另外一个重要的原因是，通常 primary key 会作为 url 中的一个部分被分享出去，如果 primary key 被修改，则可能导致原本被分享出去的 url 失效。



### Design Schema

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd5ektr01cj30v60do430.jpg" alt="image-20200324224901600" style="zoom:50%;" />

- usernane, email是可以給修改，所以不會是primary key, 要是整數的話一般就是sql不是nosql，nosql一般生出來的是個字處串的uuid hash。
- **如果username當 user table的主鍵的話，那friendship table因為用了它當外鍵就都要全改!! 所以不好**
- varchar 是数据库里的 string。
- 用来作foreign key 的不希望它經常變化
- Tweet table的 id如果是存在nosql裡的話就是個字串當id了
- Tweet可以放在SQL也可以放在NoSQL。这里的Schema只是为了确定每条Tweet需要有哪些字段，这些字段可以存在SQL数据库中也可以存在NoSQL中。如果用SQL存的话，那么就是一行是一个tweet，如果是key-value型的NoSQL，那可能就是id => {user_id, content, created_at}这样的结构。
- media service 就不需要有任何結構啦



### 

### News Feed 如何存取？

==> Tradeoff!

- 登入後看到的info的整合
- 典型例子
  - FB, Twitter, 朋友圈，RSS Reader(關啦! 死了! 因為tweeter出現了)
- 新鮮事系統的核心因素？
  - 關注＆被關注
  - 每個人看到的新鮮都是不同的

#### Pull

![image-20200725202536234](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3hndbagej30ye09saf9.jpg)

主動要，拉自己關注的10個好友的前100 tweets，再合成一個給自己看的前100條 ==> 

* Merge K Sorted Lists
* 複雜度：
  * 如果關注了N個人，那麼就N次DB REA時間 + N路merge時間(這個可忽略)
  * disk 慢 memory 1000倍; 所以k路歸併可以忽略，主要是在讀N次disk的時間
  * Post a tweet => 1 次 DB Write 的時間

> ##### [单选题]关于为什么多路归并的时间可以被忽略，下列说法不正确的是
>
> A.因为 DB Reads 的时间是瓶颈15.43% 选择
>
> B.因为多路归并的操作都是在内存和CPU中进行的，相对于在DB中读取数据是很快的43.05% 选择
>
> C.因为多路归并的时间复杂度相对磁盘读取更低41.53% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是C
>
> **正确答案:**C
>
> **解析:**
>
> 假设一共 N 个关注的好友，每个好友100条信息。多路归并的时间复杂度是 O(100NlogN)，这里使用了一个大小为 N 的堆。初始化这个堆需要 O(N) 的时间，归并出 100N 条信息，每一条需要 O(logN) 的时间。值得注意的是，读 DB 的时间是获取了 O(100N) 条数据，这个从时间复杂度上来说要更低，但是因为 DB 的操作事实上是在对文件进行操作，而文件的访问比内存访问慢几百上千倍。

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd5f4d7ckaj31ii0pawgp.jpg" alt="image-20200324230746737" style="zoom:67%;" />

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd6g3t4bkvj30v20c8teh.jpg" alt="image-20200325202727234" style="zoom:50%;" />

##### 缺點：

- 現算，就是慢，算好才能展示，卡住，用戶可感知的慢

##### 偽代碼

![image-20200725202756299](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3hpsswu0j30w40dg7bo.jpg)



####  Push

寫擴散模型

![image-20200725202857797](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3hqvcvdnj31140h4171.jpg)

N次的DB write，它不需要知道有沒有fanout成功，不用去等這個過程結束，我可以丟給async做，在MQ裡處理，我發出去後就沒我事了。



##### Fanout

別人在發帖時，就把他的推到了我的News Feed List裡 -- ***Fanout***

需要一個**News Feed Table**。



##### Denormalize

**這邊的 created_at 其實對於這個table來講是個冗餘訊息，就是denormalized，這邊也可以把tweet的更多info都存過來方便用，這樣在這個table找跟我有關時，就可以不用再去另外拿內容，不用再多一次數據庫的查詢，把所有的tweet放到cache去查詢就是快**

- 用戶需要查看News Feed時，只要從該News Feed Lists中讀取最新的100條就可

| New Feed Table |             |
| -------------- | ----------- |
| id             | integer     |
| owner_id       | Foreign Key |
| tweet_id       | Foreign Key |
| created_at     | timestamp   |

> Denormalized 叫去标准化。通俗的解释是，通过在不同的 Table 中存储同一份数据的（也就是说至少一份是冗余数据）的形式，来加速数据的查询。因为当数据只存储在一个固定的 Table A 的时候，其他 Table B访问时如果需要同时取得关联的 Table A 的数据，则需要进行 join 操作之类的，会比较慢。一个例子就是在，统计有多少人点赞了一个帖子，可以通过 `select count(*) from like_table where post_id=` 的方式来获取，但是也可以在 post table 中新增一个 like_count，每次点赞就 +1。这里 like_count 就是一个 denormalized field，因为是可以通过 `select count(*)` 在 like table 中获得的。



- 複雜度分析
  - News Feed => 1次 DB Read
  - Post a tweet => N 個粉絲，需要N次的DB Write, 
    - 可以用異步在後台執行，不需要用戶等待

##### 例子

![image-20200725203809234](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3i0k1a4hj311e0gwnec.jpg)

- **如果想讓這次的query很快的話，數據庫的index 該怎麼建？**

  ==> **根據owner_id 以及 created_at 建複合索引 (composite index)**

> ##### [单选题]NewsFeedTable的索引（index）该怎么建？
>
> A.为 owner_id 建索引即可17.32% 选择
>
> B.为 created_at 建倒序索引即可4.96% 选择
>
> C.为 owner_id + created_at 建立联合索引（Composite Index）62.15% 选择
>
> D.为 owner_id 和 created_at 分别建索引15.57% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是D
>
> **正确答案:**C
>
> **相关知识点:**数据库索引 Index
>
> **解析:**
>
> 解析见视频



- 單獨給兩個feature作排序沒用，應該是要建一個**複合索引 (composite index)**，

- 新增好友，会创建一个异步任务，去把这个好友发的帖子查询到，然后插入到当前用户的 news feed 里。删除好友的时候也是类似的。看起来似乎很土，但是确实实际工程里就是这么做的。系统设计很多东西都不是大家想象的那种需要什么牛逼的技巧的，只要能用不费力就可以了。这个方法看着土，但是用异步任务可以很好的解决，也不是特别慢。十分行之有效。



##### Push 流程圖

web server要創建任務放在async task MQ裡，然後去做 **fanouts**

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd6fm9su6zj30xu0fa0ub.jpg" alt="image-20200325201034815" style="zoom:50%;" />

##### 缺陷

一般自己關注不會關注太多人，就是PULL模型；但，關注自己的粉絲會有**明星問題**，如要建1億條record

> ##### [多选题]Push 模型有什么主要的缺陷？
>
> A.数据库中创建太多记录，浪费磁盘20.49% 选择
>
> B.粉丝数目可能很大，导致 Fanout 过程很长，从而导致用户刷到新鲜事有延迟26.92% 选择
>
> C.浪费系统资源去为很多僵尸粉创建新鲜事记录25.38% 选择
>
> D.明星发帖会在短时间内为系统带来很大的处理压力27.21% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是ABCD
>
> **正确答案:**BCD
>
> **解析:**
>
> 记住一句话 "Disk is cheap"，不要怕浪费数据库存储，为了加速查询，多存一些东西是没关系的。

Pull - 自己關注的人不會很多一般來講，但明星的粉絲很多！一億之類，要為所有粉絲都建紀錄，超大。



- Code:  下面的async 任務自己慢慢執行

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd6fsjx9npj30qw0eogn0.jpg" alt="image-20200325201633121" style="zoom:50%;" />

#### 現有社交software的模型分析

![image-20200725214622556](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3jzgsth7j311a0egaix.jpg)

- FB - Pull; Ins - Push + Pull; Twitter - Pull; Friends Circle - 最多就是有廣告，沒排序或找你沒看過的，Pull

  總是要作Tradeoff的。勇擇一個

  廣告是pull模型，會編輯，要是看到廣告太多次，就不看了，所以不能在廣告商投放時放，所以比較好是pull
  
  > ##### [单选题]广告的插入是 Push 还是 Pull 模型？
  >
  > A.Push54.32% 选择
  >
  > B.Pull43.45% 选择
  >
  > C.猜不出来2.23% 选择
  >
  > ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
  >
  > **正确答案:**B
  >
  > **解析:**
  >
  > 广告的投放人群很多，Push 模式很费时间，无法实时生效。且广告主可以筛选和改变投放人群，因此 Push 模型并不能很好的支持这种动态的改动。



- 可以在 push 的时候筛选没错，但是消息一旦push 出去以后，你再想要改动就很难了。广告主的需求很可能是 push 出去之后发现钱烧得太快要缩小投放访问，这个时候 push 模式就不太方便了。

![image-20200725214817750](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3k1fm8o8j30x80fiti7.jpg)



### 數據庫的索引

查字典時，先找頭、找到全身、去翻頁碼，要有序啦

相當於一張專門存index的表

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd6j1mdm73j30xy0ewgu3.jpg" alt="image-20200325212010964" style="zoom:67%;" />

- 這個暫存表告訴我們直接去原表的4、9 row找
- 可加速 where時、還有range時的查詢
- 原理就 B+ Tree, 關聯型主要都是它，通過多分叉減小樹的高度，以減小磁盤 seek 次數
  - 1000 =>lg1000為10了，還是多會有磁頭移動的物理過程，不像內存裡動很快。所以仍希望二分->三分->四分，就是二叉的樹高還是太高，所以才有B+樹叉開

怎麼建index. & 常用的幾類 index

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd6ia4xbojj30sa0c0wfy.jpg" alt="image-20200325214230561" style="zoom:67%;" />

- 唯一索引：如在email, phone_number, user_name
- 聯合索引：涉及多個col需求，就是建聯合索引
- ***條件索引***：如要去filter已經付費的用戶中，的聯合索引；我們不去care沒付錢的



## Scale

Optimize!

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3k2mm3ioj30oa0dqq8y.jpg" alt="image-20200725214926676" style="zoom:50%;" />

如何擴展 - 如何優化？

> - Newsfeed 是朋友圈（你和你朋友发的帖子的汇总），timeline是你发的帖子的汇总。有的网站也把这两个概念反过来。我们课上用的是我刚才说的方式。
> - 那这个cache什么时候更新呢？是在N个用户任意一个发了新推特时候既更新DB又更新cache吗 （异步任务）？
>   - 用户发新的 post 的时候，只更新这个用户发过了哪些帖子的 cache，不会去更新关注他的人的 cache。关注他的人要获得这个新的帖子，需要 pull 一下然后拿到新的 post 然后再更新自己的 news feed cache。
> - pull优化中每个人的cache如何更新呢？如果每发一个新的tweet都更新一次cache，本质上和push就一样了吧
>   - pull的时候才更新cache，但是只更新上一次pull之后发的tweet。比如说你一分钟前pull过，pull的结果放在了cache里面，然后你现在再pull，就只会去db或者每个人的timeline cache里面取最近一分钟的tweets，从而优化了pull的速度。
> - 刚才有个人问了这个问题：”请问pull优化中每个人的cache如何更新呢？如果每发一个新的tweet都更新一次cache，本质上和push就一样了吧“。 我想说就算是从某个时间戳之后去DB拉去 Follower的数据，从IO次数上讲没有本质的变化啊。
>   - 是有区别的。如果我需要拿这个人所有的 posts 和我拿这个人最近5分钟的 posts，前者数据多，取出来慢，后者很多时候都是没有数据，速度很快。时间效率不仅仅跟 query 次数有关，跟数据的传输量也有关系。你想一下如果一个 hash map 里，key1 里存了 1个数，key2 里存了 1m 个数，你是取1个数快呢，还是取 1m 个数快呢？找到 1个数和 1m 个数的内存首地址是一样的。但是这里因为是访问 cache，cache和访问者未必在同一台机器，所以虽然 key1和 Key2都很快找到数据了，但是 key2 传输 1m 个数据到 cache 的使用者，这个过程是要比传输1个数据要慢的。

1. 優化


### 解決設計缺陷如 Pull vs Push

- PULL - 登入時才去組織內容，他要是關注了1000個用戶，就要有這麼多次的SQL query，效率就是還低。

  ![image-20200725215327168](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3k6sj0xdj30rg0dg0zi.jpg)

  - **所以可以在DB訪問前加入 Cache**
  - **Cache每個用戶的 Timeline**
    - N次DB請求 =》 N次Cache read請求 ，差了100、1000倍!
    - ***Tradeoff***: Cache幾條？最近的1000條？其實也就100、200就差不多啦，畢竟內存不是disk，沒那麼便宜啦
  - **Cache 每個用戶的 News Feed** -- 可能30秒我就刷一下，刷跟刷之間我所關注的人沒有更新，每次都做歸併merge太浪費計算時間啦，所以直接把它的cache下來
    - 沒有 Cache News Feeds 的用戶: Merge N用戶的最近100條 Tweets，然後取出前100條，除非這個是第一次。
    - 有Cache News Feeds的用戶：歸併merge N 用戶在某個**時間戳**之後的所有 Tweets
  - **對比 MySQL vs Memcached 的 QPS**
    - **約 1000 ~100**

- PUSH - 浪費了更多的 Disk

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3k9bseplj30nw0bmq9h.jpg" alt="image-20200725215553093" style="zoom: 50%;" />

  - PULL 是存在Mem中，相較起來disk上便宜啦!
  - 讓常登入的優先收到，但機器人也是問題。。。

  - **Fanout** 的時過程要幾個小時啊！資源該多為大多數人服務，但都為lady gaga服務了
    - 嘗試在現有的模型作最小改動優化之，多加幾台用於作Push任務的機器, Problem solved! 
    - 對長期的增長進行估計，並評估是否值得轉換整個模型成PULL或混合的，PULL還可以方便插入廣告、內容排序、幹掉zombie粉不給他發帖了

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3kcm6rdgj311a0eak7f.jpg" alt="image-20200725215902414" style="zoom:67%;" />

10 M還可以push，1B就不可能push啦! pull還是方便，什麼插內容廣告、僵屍粉、都解決

### **PUSH + PULL** 

- 
  - **普通用戶一樣是PUSH**

  - **明星就標上去，不PUSH到用戶的News Feed中**

  - 當用戶需要的時候，來明星用戶的Timeline拿，然後合併到News Feed裡

  - 怎麼定義明星？

    - > ##### [单选题]直接用粉丝数目判断是否是明星会不会有问题
      >
      > A.有问题80.95% 选择
      >
      > B.没有问题12.72% 选择
      >
      > C.猜不出6.33% 选择
      >
      > ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A
      >
      > **正确答案:**A
      >
      > **解析:**
      >
      > 明星可能会掉粉，会从 >=1m 掉粉掉到 <1m，导致一些用户丢失掉一些明星发的帖子

  如果大明星掉了粉好幾10萬，

  最初因為他是大明星，所以系統不push他的文章，當他掉了一堆粉，我刷新News Feed, 因為這時大明星不是明星了，所以系統就不去Pull他的文章，我就丟失了他的動態啦。。

  

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3kfvm6tqj31080gwwnc.jpg" alt="image-20200725220211743" style="zoom:67%;" />

  - 所以不要動態計算他是不是明星，要離線計算，可以在User Table加一個字段 : is_superstar。

    ![image-20200725220243478](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3kgg4ssmj30l00e4jv7.jpg)

- 為什麼大家都用PULL, 幹嘛還要學PUSH?

  - 設計本就不是找唯一方案，而是最合適

  - **流量小時，Push是最經濟跟省力方式**

    | PUSH 使用時機                       | PULL 使用時機           |
    | ----------------------------------- | ----------------------- |
    | 資源少                              | 資源多、內存高          |
    | 想偷懶、想少寫code                  |                         |
    | **實時性不高**                      | **實時性要求高**        |
    | 用戶發帖比較少 如 ins               | 用戶帖多 如twitter      |
    | 雙向好友關係，沒有明☆問題，如朋友圈 | 單向好友關係，有明☆問題 |

    twitter就發得多，隨便噴；ins就比較慢

    FB PULL，又作群組又排序又插廣告就PULL

- 更多功能

  - Like，Follow & Unfollow, Ads
- 特殊情況時，如僵屍粉、大新聞搞掛了服務

  - 數據庫掛了怎辦？
  - 用戶逐漸
  - 服務器頂不住壓力怎辦？
  - 數據庫頂不住怎辦？
  - ![image-20200725220559196](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3kk5cg34j30l407i787.jpg)



1. Maintenance

   - 魯棒性，要是掛了怎辦
   - 擴展性，要是流量暴增怎辦

## Summary

* 4S 在心裡的思想
* Ask before Design -- 先問清楚再設計

- no more no less -- 要設計剛剛好夠用的就好

* Work solution first -- 先設計一個基本能工作的，再逐本優化
* Analysis is important than solution -- 沒有標準答案，分析過程展示知識儲備；權衡各種設計方式的利弊



# Extension

## 數據持久化與常見的數據庫

- MySQL, PostgreSQL
- Memcached
  - k-v緩存系統
  - value 不支持 set / list
  - 無法持久化
- Redis
  - value 支持 set / list，O(1) add, append，
  - 數據可持久化同步上disk，數據都load進memory，
  - 後來可多台機器的內存
  - 可用作 Cache/ Message Queu/ Database，重開機還在
- Cassandra, HBase
  - Column Family Base NoSQL 數據庫
  - key分為 row-key, column-key
  - 適合放查詢請求簡單不複雜的data
- MongoDB
  - 適合寫多讀少的數據，寫快讀慢
- Rocksdb
  - kv, value 不支持 set / list
  - 用於大公司的kv storage底層, 如FB、抖音



> - 选择memcached 和cache 的区别？
>   - cache单机的，单机的内存有限制，并且只能本机访问，memcache是一个cache db，可以由多台机器组成，并且可以多个server同时访问





> 异步任务中适合放那些不着急响应结果给用户或者执行起来比较慢的任务。所以 LintCode 评测和发邮件都适合放在异步任务中执行。C和D中的两个操作只是简单的在数据库中创建一条记录，是很快的，不需要通过异步任务执行，且 D 选项必须马上反馈给用户是否注册成功，更加不能放在异步任务中。



## 消息隊列

- IPC 進程間通信或同一進程的不同線程間的通信方式

- 時機：生產者、消費者

- 處理跟產生的速率不一致

  - 不可能一下單就有人來敲門到貨

    <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh5z1y30rqj30q20i6451.jpg" alt="image-20200727235851008" style="zoom: 33%;" />

- Lintcode 評測機

- 註冊後發email，一般是第三方發 mail的系統

  - e.g. mailgun 幫發mail
    - 第三方的api會慢一點
    - 只要跟用戶說「我有發了」就好，而不需要讓用戶等著
  - 1 慢；2 需要重試機制; 3 訂閱用戶，慢慢出現沒差，重要的是「已訂閱」了
    - 關注一個最主要是把好友關係存下來

- RabbitMQ, Redis(Cache比不過Memcached, MQ比不上RabbitMQ, DB比不上SQL及NoSQL，但快…)

  Amazon Simple Queue Service (SQS)

- 一消息只被處理一次，金融級別會有更高的要求，萬億級別的如螞蟻

- 鏡像Queues ，一個掛了另一個馬上頂上

- 12360 一個一個把訂票的要求執行了



# Appendix

### 1 果取關

- Push model 下的討論
  ![image-20200725225321376](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3lx48mupj30oy0cwacj.jpg)

就是取關了後還是看得到他的訊息，要再刷一次才不見，就是典型的還在計算



### 2 如何存 Likes

Denormalize: 原本可以在別的表單裡計算下的東西，我直接存在這個表單裡

直接把點讚的數目一股腦存下去

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd7r1stfcrj30ta0g475i.jpg" alt="image-20200326233130851" style="zoom:67%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3m1s1qinj30xa0e0tft.jpg" alt="image-20200725225749071" style="zoom:67%;" />

---



### 3 驚群現象 Thundering Herd

大家都在這時間都去關注這八卦

![image-20200725225925974](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3m3fvrv1j30km0bkn0y.jpg)



> ##### [单选题]【系统设计2020】数据库的分片机制是否对同一个数据的大量访问有用？
>
> 数据库分片，英文叫做 Sharding 或者 Partition
>
> A.有用26.53% 选择
>
> B.没用73.47% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是A
>
> **正确答案:**B
>
> **解析:**
>
> 因为访问的是同一个数据，sharding 机制无论如何都会 sharding 到同一个机器上。此时 sharding 不能做到分摊流量的作用。



- sharding 不會管用



![image-20200725230057674](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3m516nyzj30x00dswoi.jpg)

- https://engineering.fb.com/networking-traffic/under-the-hood-broadcasting-live-video-to-millions/
- 



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3m7c3zs6j30v40jwaie.jpg" alt="image-20200725230310804" style="zoom:50%;" />



- 解決方式

  - Memcache lease Get: 讓memcached 等一會，好多個人找同個key，讓大家排個隊，只放第一個lease get回去後面的就等著一會，取了後回填；只讓第一個拿不到，去通知，然後去跟老闆說，然後回填

    <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3mdyyq3vj30nc0ggdjl.jpg" alt="image-20200725230932282" style="zoom: 33%;" />

  - FB 也有寫了個博文，有視頻，待看!
  - Redis 防雪崩架構設計



# 四種姿勢

- 白紙 + 攝像頭
- 白板 + cam ==> 不清楚
- 錄屏、畫圖軟件、鼠標好
- 錄屏+手寫: iPad + apple pencil + airServer



##### Tradeoff

##### SOA

##### Pull vs Push Model

##### DB Systems

##### Async & Message Queue

##### Persistent

##### Denormalize

##### Thundering Herd

##### News Feed Design?!