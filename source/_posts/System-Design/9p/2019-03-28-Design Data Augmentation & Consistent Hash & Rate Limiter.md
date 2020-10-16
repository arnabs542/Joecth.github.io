---
layout: post
categories: SystemDesign
tag: []
date: 2019-03-28
---



# Design Data Aug. & Consistent Hash

## Outline

- Hash
- Consistent Hash
- Load Balancer
- Rate Limiter
- Web Logger



```python
class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        def helper_LTE(key, HASH_SIZE):
            res = 0
            for i in range(len(key)):
                # print(pow(33, len(key)-i))
                res += ord(key[i]) * pow(33,len(key)-1-i)
            # print(res)
            return res%HASH_SIZE
            
        def helper(key, HASH_SIZE):
            
            res = 0
            for i in range(len(key)):
                # 同余定理：
                # (a * b ) % MOD = ((a % MOD) * (b % MOD)) % MOD
                res = (res*33 + ord(key[i]))%HASH_SIZE
            
            # return res%HASH_SIZE  STILL LTE
            return res
        
        # return helper_LTE(key, HASH_SIZE)
        return helper(key, HASH_SIZE)
```



sharding 也可叫 拆分、division

md5 16^32 用在登入密碼加密，有可能有衝突，現在已經已經不怎麼安全啦

SHA512

密碼加鹽



## How to Scale

就是要Scale Database 的問題，因為DB 要是被訪問多了，會掛。

假如user有1k, Server，DB都OK, 最大的問題是什麼？

它病死了！

> ##### [单选题]除了 QPS 承受力的问题以外，还有什么问题是“最主要”需要考虑的？
>
> 如果只用一台数据库
>
> A.硬盘大小7.42% 选择
>
> B.CPU 的运算速度8.71% 选择
>
> C.单点失效 Single Point Failure82.66% 选择
>
> D.价格是否昂贵1.21% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是C
>
> **正确答案:**C
>
> **解析:**
>
> 硬盘大小，CPU运算速度，价格当然也重要。但是问题最大的还是单点失效，即如果挂了没有其他机器可以马上替代的问题。

網站不能用=>數據全丟了=>用戶不來啦

Server是無狀態的，是不存用戶的信息的。

如果想增加數據庫的話，我們該怎麼拆分數據？就是Sharding，or partition，此外還要做Replica數據複製。

希望能用機器去拆分掉進來的流量。

- Sharding
  - 分攤讀寫流量
  - 不會一個掛就全掛
- Replica
  - 一式三份，兩台近，一台遠
  - 分攤讀請求

> - 一般导致数据库挂了的原因是什么？硬盘损坏么？
>   - 也可能运算量太大卡主了
> - 那负责拆分的机器的qps是不是要很大
>   - 因此通常是每台 WebServer 自己根据同样的算法来计算出该去哪一台数据库存取数据，而不是都跑到一个中心节点去。
> - 所以说数据拆分是因为 分担流量，不是因为太多数据一台电脑装不下是吗
>   - 两个都是目的。大部分时候是为了分摊流量。也有因为装不下需要分摊的情况。



## Sharding in SQL vs NoSQL

NoSQL多是自己就提供好了

### Vertical

照table的不同類型，粗暴簡單

可以把user不常改的跟常改的分去到兩個不同的 Table，流量就分開了

##### 缺點：可能就是洗菜、切菜就是比較久，煮很快，所以不該都一個人

[单选题]Vertical Sharding 不能解决什么问题？

A.数据库 table 很多的情况6.64% 选择

B.一个 table 中有很多关联度不大的 columns8.77% 选择

C.一个 table 里存储的内容太大，且 columns 无法再做拆分84.58% 选择

![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是C

**正确答案:**C

**解析:**

Vertical Sharding 是按照 column / table 来进行的，如果一个表单（table）里存储的内容太多，且 column 数目又无法再拆分，就无法使用 Vertical Sharding 了



### Horizontal

- 新的數據放新的好嗎？
  - 所有數據被訪問的機率是相等的這個假設是錯的！當然一般是新的被訪問得多。一年前寫的都比較少在過問了。

##### [单选题]新数据放新机器，老数据放老机器的问题是什么？

A.数据访问不均匀45.88% 选择

B.数据存储不均匀12.10% 选择

C.取数据时无法确定数据存在哪儿42.02% 选择

![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是B

**正确答案:**A

**解析:**

根据数据的新旧程度来拆分的话，新数据的访问次数比旧数据的访问次数是要明显多的，会导致数据访问不均匀的问题。
这种方法并不会导致存储不均匀，最多只有最新的一台机器的数据相对少一些，其他的机器都还是均匀的。也不会导致不知道数据去哪台机器取，比如根据 id 来拆分，0~99在1号机器，1-199 在2号机器的话，根据 id 可以算出对应的机器是哪个。



#### 模三好嗎？

買新機器／有機器掛時就要大遷移了、

- 慢，容易􏰀成数据的不一致性
- 迁移期间，服务器压力增大，容易挂

> ##### [单选题]理想状况下，3台机器变4台机器，多少数据需要迁移？
>
> A.33.3%15.00% 选择
>
> B.25%65.56% 选择
>
> C.50%2.30% 选择
>
> D.75%17.14% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 理想状况下，这台新机器存储 1/4 的数据，因此需要移动的数据也是 1/4。

就是理想下只想移動25%，不要全都移動

> - 对于登入数据，如果按新旧存放，是否还会遇到“C.取数据时无法确定数据存在哪儿”的问题？因为用户名不是sequential的，而用户登入时并不知道自己的id
>   - yes



#### Consistent Hash

```bash
A general database method for performing a horizontal shard is to take the id against the total number of database servers n and then to find out which machine it is on. The downside of this approach is that as the data continues to increase, we need to increase the database server. When n is changed to n+1, almost all of the data has to be moved, which is not consistent. In order to reduce the defects caused by this naive's hash method (%n), a new hash algorithm emerges: Consistent Hashing, Consistent Hashing. There are many ways to implement this algorithm. Here we implement a simple Consistent Hashing.

Take id to 360. If there are 3 machines at the beginning, then let 3 machines be responsible for the three parts of 0~119, 120~239, 240~359. Then, how much is the model, check which zone you are in, and which machine to go to.
When the machine changes from n to n+1, we find the largest one from the n intervals, then divide it into two and give half to the n+1th machine.
For example, when changing from 3 to 4, we find the third interval 0~119 is the current largest interval, then we divide 0~119 into 0~59 and 60~119. 0~59 is still given to the first machine, 60~119 to the fourth machine.
Then change from 4 to 5, we find the largest interval is the third interval 120~239, after splitting into two, it becomes 120~179, 180~239.
Suppose all the data is on one machine at the beginning. When adding to the nth machine, what is the distribution of the interval and the corresponding machine number?

Example
Example 1:

Input:
 n = 1, 
Output:
[
  [0,359,1]
]
Explanation:
represent 0~359 belongs to machine 1.
Example 2:

Input:
 n = 2,
Output:
[
  [0,179,1],
  [180,359,2]
]
Explanation:
represent 0~179 belongs to machine 1.
represent 180~359 belongs to machine 2.
Example 3:

Input:
n = 3,
Output:
[
  [0,89,1]
  [90,179,3],
  [180,359,2]
]
Clarification
If the maximal interval is [x, y], and it belongs to machine id z, when you add a new machine with id n, you should divide [x, y, z] into two intervals:

[x, (x + y) / 2, z] and [(x + y) / 2 + 1, y, n]

Notice
You can assume n <= 360. At the same time, we agree that when there are multiple occurrences in the maximum interval, we split the machine with the smaller number.
For example, the size of 0~119, 120~239 is 120, but the number of the previous machine is 1, and the number of the next machine is 2, so we split the range of 0~119.
```





指的是對於ｎ台或 n+1 台機器時會是一致的

一致性哈希表存在每個server上。

- 如果在相鄰的兩個各自挪一些來
  - 缺陷：
    - 仍是會有一台特別load重
    - 遷移時就只有兩個鄰居，他們兩個人特別負載重

> - 360这个数值是经验值么？这个数字对于任何数量的机器都合适么？
>   - 3*60 只是为了让理解一个圆有 360°，比较形象。这个数字当然不是实际的工程中使用的数字。实际使用的数字一般是 **2^64 ==> 宇宙爆炸的機率***
> - 反正都要用一个表来记录key->db号码， 为什么还要hash 2^64呢？ 直接把key和机器号码存到表里不行吗？
>   - 没有 Key->db号码的这张表。***通过 key 得到 db 是靠 consistent hashing 这个算法计算出***来的，而不是把每个 key 存在哪个 db 都存下来。

讓不同的key的時候的機率是2^64幾乎是宇宙爆炸的機率。

> ##### [单选题]机器 D 加入 Consistent Hash Ring 以后，应该问谁要数据？
>
> A.机器 A78.58% 选择
>
> B.机器 B6.53% 选择
>
> C.机器 C14.89% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是C
>
> **正确答案:**A
>
> <img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdcduksozaj30og0jatfy.jpg" alt="image-20200330234246254" style="zoom:67%;" />



Virtual node

理想新加入的機器的「分身」可以去均勻占到不同的前ｎ台機器的分身。如一台切成1000個，理想就是其他的10台，每台可以分到100個我的分身。

> ##### [单选题]找比某个数大的最小值可以用什么数据结构？
>
> A.堆 Heap24.45% 选择
>
> B.红黑树 Red-black Tree(Balanced Binary Search Tree)65.64% 选择
>
> C.哈希表 HashMap2.45% 选择
>
> D.链表 Linked List7.45% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> Heap 只能找全局最大最小。

要增刪查改還是用Binary Search Tree, 可快速找到比某數大的最小數。

從順時間碰到的node的真實機器作遷移

> - key如何设计才能保证hash算出来几乎均匀分布在0到2的64次方这么大的范围？
>   - 选择一个好的哈希函数就行了，比如： MurmurHash, xxHash, MetroHash or SipHash1–3
> - 问题同上面的同学：怎么保持key均匀分布？
>   - 选择一个好的哈希函数是可以保证这个性质的。https://en.wikipedia.org/wiki/Hash_function#Uniformity
> - 这个哈希算法是用来做数据库horizontal sharding的吗，它能用在分配服务器上吗？能用在vertical sharding上吗？
>   - 是的，用来做 **Horizontal Sharding**。不能用在 Veritical Sharding 上。Vertical Sharding 是按照 column / table 进行 sharding 并不按照数据本身的值来进行 sharding。***他可以用在分配数据服务器上***，但是不能用在分配 web 服务器上。**因为 web 服务器是 stateless 的，不需要固定的去同一个 web server，只需要随机分配即可。**
> - 新增加机器时，增加的虚拟的点的位置是随机的么？
>   - 本质上都是根据机器名字 hash 出来的，不能认为是随机的。



#### Consistent HashⅡ

```bash
描述
在 Consistent Hashing I 中我们介绍了一个比较简单的一致性哈希算法，这个简单的版本有两个缺陷：

增加一台机器之后，数据全部从其中一台机器过来，这一台机器的读负载过大，对正常的服务会造成影响。
当增加到3台机器的时候，每台服务器的负载量不均衡，为1:1:2。
为了解决这个问题，引入了 micro-shards 的概念，一个更好的算法是这样：

将 360° 的区间分得更细。从 0~359 变为一个 0 ~ n-1 的区间，将这个区间首尾相接，连成一个圆。
当加入一台新的机器的时候，随机选择在圆周中撒 k 个点，代表这台机器的 k 个 micro-shards。
每个数据在圆周上也对应一个点，这个点通过一个 hash function 来计算。
一个数据该属于哪台机器负责管理，是按照该数据对应的圆周上的点在圆上顺时针碰到的第一个 micro-shard 点所属的机器来决定。
n 和 k在真实的 NoSQL 数据库中一般是 2^64 和 1000。

请实现这种引入了 micro-shard 的 consistent hashing 的方法。主要实现如下的三个函数：

create(int n, int k)
addMachine(int machine_id) // add a new machine, return a list of shard ids.
getMachineIdByHashCode(int hashcode) // return machine id

```



## Replica

> ##### [多选题]下列关于 Backup 和 Replica 的区别描述正确的有？
>
> A.Backup 一般是周期性的，Replica 是实时的31.83% 选择
>
> B.Backup 一天做一次7.07% 选择
>
> C.Replica 一般一式三份27.59% 选择
>
> D.Backup 可以分摊读请求1.54% 选择
>
> E.Replica 可以分摊读请求29.77% 选择
>
> F.有了 Replica 之后就不需要 Backup 了2.21% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是ACE
>
> **正确答案:**ACE
>
> **解析:**
>
> Backup 一般一天做一次，但是这个完全是因人而异，不是强制的。
> Backup 存储的是离线数据，无法分摊在线读请求。
> **虽然 Replica 很强大，但是 Backup 也是很有必要的，可以认为是一个双保险。且可以服务于一些离线数据计算，这样不会给在线数据库带来压力**。

雙重保險

**不是每種DB都有replica，所以backup還是保險**

更穩定，就是發展的先後問題。

> - replica和backup代价是一样的吗？比如说都需要一台机器？是不是说replica的机器可能性能好一点，而backup对机器性能没有要求
>   - 有的。你说的方式就是很多 NoSQL 现在用的方式，选择一个 Replica 写进去，然后这个 Replica 负责同步给其他的 Replica。 ***Replica 之间的地位是等价的，没有 master-slave 的上下级之分。***



### SQL - 用 MasterSlave VS NoSQL 用等價的replica w/ Consistent Hashing 作傳遞

- 也可手動作 Consistent Hash Ring

#### Write Ahead Log

就只會一直追加

所以slave上讀會比較慢



- Master 掛了時要是Slave還沒拉過去，雖然Slave被升級成了Master，但data還是就不見了。

- 也要根據這個支持把 transaction 反向。

> - How to do consistent hashing for a web server? For DB, the web server can compute the hashcode and then choose DB. Which component to do this for Web Server? DNS? NGIX?
>   - ***Web Server 是不需要做 Consistent Hashing 的。因为 Web Server 是 stateless 的，你不需要保证每个用户每次访问的都是同一个 Web Server***，随机来一个 Server 服务他就可以了，就跟你去银行不一定每次都去一个窗口排队，哪个人少去哪个排队就可以了。只有 DB 才需要做 Consistent Hashing 因为你的钱如果存在工商银行你去建设银行是取不到钱的。 **Web Server 只需要做 Load Balancing ，这个步骤是 NGINX 或者专门的 Load Balancing 的硬件 或者 AWS 的 Load Balanacing 服务负责做的**。
> - replica和backup代价是一样的吗？比如说都需要一台机器？是不是说replica的机器可能性能好一点，而backup对机器性能没有要求
>   - 代价不一样。replica 要实时，而且要服务在线请求，要求是比较高的。backup 只是做一下存储备份，不服务用户，要求比较低。
> - ***replica方法除了master slave，还有别的方法吗，比如说所有服务器都是master，都能接受写操作，隔一段时间同步一次***
>   - ***有的。你说的方式就是很多 NoSQL 现在用的方式，选择一个 Replica 写进去，然后这个 Replica 负责同步给其他的 Replica。 Replica 之间的地位是等价的，没有 master-slave 的上下级之分**。*
> - "下列关于 Backup 和 Replica 的区别描述正确的有？" 为什么replica一般一式三份？
>   - 經驗值
> - Replica在一致性哈希环上顺时针存三份我理解的是紧挨着的3个位置，对吗？这样读请求来的时候可以分摊给这3个机器吗？
>   - 对的。***读请求可以分摊给replica***。





## Ex.1 Sharding User Table



- 某個數據庫如按哪個key, Column去sharding好？

  User Table怎麼算sharding 好？

  ***就是說要拿什麼去跑一次consistent hash去得到機器的編號，然後連上那台機器，然後去那台機器拿出數據呢？***

  - 怎麼取數據就怎麼拆數據

    就是看最常見是按什麼去查呢？就把這個拆開去作sharding吧。

    *舉例：**user_id是最常被其他的表單用到的foreign_key，就用它作拆分***

    - 但一般都是用username找用戶啊？
      - ***就再建個表單作username => user_id映射，多查一個步驟就好**。*

- Insert時怎辦？該去哪台數據庫作insert呢？

  - ***同一台機器時可以設sequential id，就是有另張表紀錄這張表的sequential id到了哪了，然後會加鎖去保持連續性。***
  - 這時可以自己自建一個uuid作為用戶的user_id,  不同人不會撞啦！***因為是uuid，宇宙爆炸的機率***
    - 然後再拿去作consistent hashing
  - **擴機器時怎辦？uuid是字串，本來人少時是用整數呀，怎辦？**
    - ***建個表，在一個新的service裡（這個可以全局共享），就是要先去那個表查，那個表在查時會加鎖，再map到uuid。***
      - 也就是說用加鎖保證數據的原子性。
      - 創建用戶也不是大QPS，所以問題也不是特大。

> ##### [单选题]User Table 最常见的需求是按照什么去查询？
>
> A.username21.85% 选择
>
> B.id (user_id)76.69% 选择
>
> C.phone number0.09% 选择
>
> D.email1.37% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是A
>
> **正确答案:**B
>
> **解析:**
>
> user_id 会作为其他 Table 的 Foreign key 存在，所以是最频繁的查询需求。

> - ***这个新的表单存储username, userid, 这个不需要sharding对吧？ 因为读取比较少？***
>   - ***如果读取比较少的情况下，不 sharding 也没问题。不过一般这类 Key-value 的查询都会放在 NoSQL 数据库里，默认就会 sharding。***
> - 好像可以用当前时间加其他的限制条件来创建ID，这样可以让ID有其他的信息，这样好么？
>   - ***这样做也是可以的，相当于denormalization，但是有一定风险，要注意保持id的随机性，否则可能会让id的生成变得predictable***。
> - 如果table QPS需求大的话，而且已经采用了自增id，是不是就不用自增id， 创建一个新table， 用uuid来做key， 然后把原有数据移植到新的table？ 然后更新其他 引用它的table的foreign key？
>   - 更新 foreign key 是一个很大的工程（引用太多了。而且随时可能更改）。***所以最后一点说的是，创立一个单独的 UserIdService 来负责产生这个全局自增的 user_id***。**更新 foreign key 这个并不现实**。
> - 可以通过hash把原来的id改成uuid吗
>   - ***uuid是有标准的生成方式的，不能仅仅通过求Hash的方式来获得uuid:*** https://en.wikipedia.org/wiki/Universally_unique_identifier#Versions
> - 这个UserIdservice是不是一种分布式锁啊？
>   - ***原理有些类似，但是这个还算不上一个general-purpose的分布式锁，只是在系统中设计了一个单点来保证生成ID的顺序和唯一性***。





## Session Table Sharding

> ##### [单选题]Session Table 通常按照哪一项去查询？
>
> A.session key (session token)84.15% 选择
>
> B.user_id14.54% 选择
>
> C.expire_at1.31% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A
>
> **正确答案:**A

> - *为什么哪一项最常用就要根据哪一项去sharding呢，能详细解释一下吗*
>   - ***不是哪一项常用就按照哪一项去 sharding，是按照哪一项查询***就按照哪一项 sharding。假如一个数据有 col1, col2 两项，按照 col1 sharding 的意思就是，如果两条数据的 col1 相同，就会被分配在同一台机器上。所以当你按照 col1 查询的时候，才能保证在同一台机器上找到这两条数据。如果你查询是按照 col1 来查询，存的时候却按照 col2 来sharding 的话，那么就没法保证 col1 相同的都在同一台机器上，这样 sharding 的意义就没有了，***sharding 就是要让你能分摊查询请求到不同的机器***，***如果你的一次查询需要去所有机器汇总结果的话，这个 sharding 就是失败的 sharding***。



## News Feed / Timeline Shardings

> - *TimeLine table 即 Post Table 刚才课上说到了是以User ID做为sharding key。 我有一个问题：如果我想查 Post 详情的话， 那是不是每次请求都要带上 User ID 才能定位到具体某台机器上。但是基本获取Post 详情的请求都只会带 Post ID而不是 Post ID 和 User ID啊。 求解答~*
>   - **这种情况下，通常的做法是 post_id 里，前缀就带上 user_id。这样可以通过 post_id 得到 user_id。此时 post_id** 通常是一个字符串，可以自定义格式。*
> - news feed一般是会专门存一个table吗？比如我要看我的news feed，是**拿我的user id去news feed table里面找，而不是拿我的所有关注user的id去post table里面找然后汇总**？那么这个news feed table里面的信息总归是通过去post table里面查找汇总好了以后存在news feed table里的吧？可不可以介绍一下： 1. 这个table的schema。 2. 去post table查找和汇总发生在什么时候？
>   - *news feed 一般就是一个专门的 table。*
>     *news feed table 的 schema 在 PPT 里有，你看一下。视频里也有讲到的。*
>     ****去 post table 里查找和汇总可能不会发生，因为 news feed table 可以通过 denormalize 的方法把 post 的内容复制一份存在 news feed table*** 里来加速这个查询过程。*



Ref:

1. https://afghl.github.io/2016/07/04/consistent-hashing.html
2. http://blog.codinglabs.org/articles/consistent-hashing.html



## leetcode可能怎麼sharding?

submission, user, timestamp, problem, status

> ##### [单选题]LintCode Submission Table 按照什么进行 Sharding？
>
> A.user_id13.52% 选择
>
> B.submission_id19.07% 选择
>
> C.problem_id4.17% 选择
>
> D.status0.28% 选择
>
> E.用两个表单，分别按照 user_id 和 problem_id 来 sharding62.96% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是E
>
> **正确答案:**E

需求１我們要查詢某個題的所有提交紀錄

Where problem_id = 999;

需求２我們要查詢某個人的所有提交紀錄

Where user_id = 999;

如果按user_id作sharding時，那當被查詢需求１時，就要去每台機器都拿過來，這樣效率就低。

NoSQL一般可Sharding, 也就比較不支持multi-index。麻煩。

用於篩選的info可以存兩份。

> - 可以把code存在一个单独的table里面然后让两个表都去reference一个code id。当然也可以把code冗余地存在两个表中。前一种方法省空间，但是需要读两次数据库，后一种方法浪费一点空间但是只需要读一次数据库。



## Rate Limiter

![image-20200403221207316](https://tva1.sinaimg.cn/large/00831rSTgy1gdgxpdr0mpj31ci0lae0x.jpg)

主要滿足大多人的滿意度、別有惡劣的影響

![image-20200403221757444](https://tva1.sinaimg.cn/large/00831rSTgy1gdgxvl4bxej31f00kmq6n.jpg)

> - key,你这个event+feature+ts，无法区分是谁，哪个用户来的req啊？你如何block恶意的点击呢？
>   - 这里举的只是一个简单的例子，实际中feature里面除了ip也可以包含user id之类的信息，你可以根据自己的需要去扩展。
> - memcahed是一个字典还是一个自定义的类？
>   - memcached是一个内存型key-value数据库，你可以把它当作字典用。

![image-20200403222029916](https://tva1.sinaimg.cn/large/00831rSTgy1gdgxy3he6jj31100js4k6.jpg)

## Rate Limiter (Mine) 限流

ref: https://www.youtube.com/watch?v=e3-MTmtUpf4

限流就是如

A系統調(2000/s) B系統的接口，B處理流量的能力如 (1000/s)，B會被搞掛

所以

A --請求<限流> --> B接口 (1000/s)

### Leaky Bucket 漏桶算法 (到底是漏桶還是漏斗?)

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbjtx1704j30do0ekwh9.jpg" alt="image-20200801194536656" style="zoom:50%;" />

- 一滴水代表一個http請求，把請求先裝到一個漏桶去，就很多滴水，出漏斗時表示去調B的接口了，如果漏出的速度比較慢，就是杯子會慢慢滿了，自己就會流出來了，叫作系統流量的最大值已經被超過。當超過漏桶容量時
  - 比較直接就是A再流進來系統就直接吐掉了
  - 或是，有人性一點，再進來的水滴加一個隊列，再慢慢把隊列的丟進去漏桶去
  - 當然漏桶自己本身當然也是個隊列啦。
  - 量是根據第三方的限量去設計的
  - 可強制限制調用的速率
- 思路就是：
  1. 請求先進入到漏桶裡
  2. 漏桶以一定的速度出水
  3. 當水請求較大，可能會溢出
  4. 能強行限制數據調用的速率



### Token Bucket 令牌桶算法

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200801205923248.png" alt="image-20200801205923248" style="zoom:50%;" />

- 這個是用得最多，一般在分布式的限流就是用這個
- 上面藍色是個令牌的池子，每隔一秒會往這個池子裡面放一張令牌
- 左邊是A系統要調時，會先去令牌池拿張牌出來再去調B接口，就是B前面有一道門，池子裡就像是keys，別人要先去撈keys，才能開門
- 令牌無時無刻都在丟
  1. 溢出時：如果拿得比較慢，令牌桶會溢出，滿了就滿了，令牌桶新生成的丟不進去了，滿跟不滿都沒區別，我用老、新令牌沒差，都是可以開門的
  2. 沒得拿時：當A去拿令牌池裡的keys，發現沒有keys，其他沒令牌拿的9次就等待，不然就是拒絕服務，或也是把請求丟去隊列等著



### 差別：

1. 如果有秒殺，如果有1000個商品，12點前令牌就要預處理，要保證有1000個令牌，因為12點那瞬間會有1000個併發操作的「突發流量」的令牌保證，保證業務能玩下去
   - 限制了平均速率
   - 可接受突發狀況
   - 會以一個恆定的速度往令牌池放令牌
   - 沒令牌時，拒絕
2. 相對的，漏斗就是丟滿了就溢出了 
   - 滿時，**熔斷**



## More Cases

ref: https://zhuanlan.zhihu.com/p/21103657

