---
layout: post
categories: SystemDesign
tag: []
date: 2019-03-18

---



# Design User System

## Memcached

~~~bash
538. 内存缓存
中文English
实现下列几个方法：
1.get(curtTime, key). 得到key的值，如果不存在返回2147483647
2.set(curtTime, key, value, ttl). 设置一个pair(key,value)，有效期从curtTime到curtTime + ttl -1 , 如果ttl为0，则一直存在
3.delete(curtTime, key). 删除这个key
4.incr(curtTime, key, delta). 给key的value加上delta，并且返回 如果不存在返回 2147483647。
5.decr(curtTime, key, delta). 给key的value减去delta，并且返回 如果不存在返回 2147483647。

Example
样例1

get(1, 0)
>> 2147483647
set(2, 1, 1, 2)
get(3, 1)
>> 1
get(4, 1)
>> 2147483647
incr(5, 1, 1)
>> 2147483647
set(6, 1, 3, 0)
incr(7, 1, 1)
>> 4
decr(8, 1, 1)
>> 3
get(9, 1)
>> 3
delete(10, 1)
get(11, 1)
>> 2147483647
incr(12, 1, 1)
>> 2147483647
```**样例1**

get(1, 0)

2147483647
set(2, 1, 1, 2)
get(3, 1)

1
get(4, 1)

2147483647
incr(5, 1, 1)

2147483647
set(6, 1, 3, 0)
incr(7, 1, 1)

4
decr(8, 1, 1)

3
get(9, 1)

3
delete(10, 1)
get(11, 1)

2147483647
incr(12, 1, 1)

2147483647

Clarification
实际上，如果内存不足，存缓存服务器将驱逐key，并且它还支持各种值类型，如字符串和整数。 在我们的例子中我们将这个问题简化了，我们可以假设我们有足够的内存，所有的值都是整数。

在谷歌上搜索“LRU”和“LFU”以获取有关memcache如何逐出数据的更多信息。
~~~



```python
class Resource:
    
    def __init__(self, value, expired):
        self.value = value
        self.expired = expired

INT_MAX = 0x7fffffff

class Memcache:

    def __init__(self):
        # initialize your data structure here.
        self.client = dict()
    
    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return an integer
    def get(self, curtTime, key):
        # Write your code here
        if key not in self.client:
            return INT_MAX
        res = self.client.get(key)
        if res.expired >= curtTime or res.expired == -1:
            return res.value
        else:
            return INT_MAX

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} value an integer
    # @param {int} ttl an integer
    # @return nothing
    def set(self, curtTime, key, value, ttl):
        # Write your code here
        if ttl:
            res = Resource(value, curtTime + ttl - 1)
        else:
            res = Resource(value, -1)

        self.client[key] = res 
        
    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return nothing
    def delete(self, curtTime, key):
        # Write your code here
        if key not in self.client:
            return

        del self.client[key]

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def incr(self, curtTime, key, delta):
        # Write your code here
        if self.get(curtTime, key) == INT_MAX:
            return INT_MAX
        self.client[key].value += delta

        return self.client[key].value

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def decr(self, curtTime, key, delta):
        # Write your code here
        if self.get(curtTime, key) == INT_MAX:
            return INT_MAX
        self.client[key].value -= delta

        return self.client[key].value
```



## Mini Cassandra

Cassandra is a NoSQL database (a.k.a key-value storage). One individual data entry in cassandra constructed by 3 parts:

1. row_key. (a.k.a hash_key, partition key or sharding_key.)
2. column_key.
3. value

row_key is used to hash and can not support range query. Let's simplify this to a string.
column_key is sorted and support range query. Let's simplify this to integer.
value is a string. You can serialize any data into a string and store it in value.

Implement the following methods:

1. `insert(row_key, column_key, value)`
2. `query(row_key, column_start, column_end)` return a list of entries

```bash
502. Mini Cassandra
中文English
Cassandra is a NoSQL database (a.k.a key-value storage). One individual data entry in cassandra constructed by 3 parts:

row_key. (a.k.a hash_key, partition key or sharding_key.)
column_key.
value
row_key is used to hash and can not support range query. Let's simplify this to a string.
column_key is sorted and support range query. Let's simplify this to integer.
value is a string. You can serialize any data into a string and store it in value.

Implement the following methods:

insert(row_key, column_key, value)
query(row_key, column_start, column_end) return a list of entries
Example
Example 1:

Input:
  insert("google", 1, "haha")
  query("google", 0, 1)
Output: [(1, "haha")]
Example 2:

Input:
  insert("google", 1, "haha")
  insert("lintcode", 1, "Good")
  insert("google", 2, "hehe")
  query("google", 0, 1)
  query("google", 0, 2)
  query("go", 0, 1)
  query("lintcode", 0, 10)
Output:
  [(1, "haha")]
  [(1, "haha"),(2, "hehe")]
  []
  [(1, "Good")]
```



```python
"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""

from collections import OrderedDict
class MiniCassandra:
    
    def __init__(self):
        # do intialization if necessary
        self.hash = {}
    """
    @param: row_key: a string
    @param: column_key: An integer
    @param: value: a string
    @return: nothing
    """
    def insert(self, row_key, column_key, value):
        # write your code here
        if row_key not in self.hash:
            self.hash[row_key] = OrderedDict()
        self.hash[row_key][column_key] = value

    """
    @param: row_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, row_key, column_start, column_end):
        # Write your code here
        rt = []
        if row_key not in self.hash:
            return rt

        self.hash[row_key] = OrderedDict(sorted(self.hash[row_key].items()))
        for key, value in self.hash[row_key].items():
            if key >= column_start and key <= column_end:
                rt.append(Column(key, value))

        return rt
        
    # def query(self, row_key, column_start, column_end):
        # write your code here
        # return []
        
        # print(self.od[row_key])
        # return self.od[row_key]#[column_start:column_end]
```



## Friendship Service

```python
from collections import defaultdict
class FriendshipService:
    
    def __init__(self):
        # do intialization if necessary
        self.fans = defaultdict(list)
        self.followings = defaultdict(list)
    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    def getFollowers(self, user_id):
        # write your code here
        # return []
        return sorted(self.fans[user_id])
    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    def getFollowings(self, user_id):
        # write your code here
        # return []
        return sorted(self.followings[user_id])
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, to_user_id, from_user_id):
        # write your code here
        if to_user_id not in self.followings[from_user_id]:
            self.followings[from_user_id] += [to_user_id]
            # self.followings[from_user_id].sort()
        if from_user_id not in self.fans[to_user_id]:
            self.fans[to_user_id] += [from_user_id]
            # self.followings[from_user_id].sort()
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, to_user_id, from_user_id):
        # write your code here
        # self.followings[from_user_id].pop(self.followings[from_user_id].index(to_user_id))
        # self.fans[to_user_id].pop(self.fans[to_user_id].index(from_user_id))
        a = self.followings[from_user_id]
        b = self.fans[to_user_id]
        if from_user_id in self.followings:
            if to_user_id in a:
                a.pop(a.index(to_user_id))
        if to_user_id in self.fans:
            if from_user_id in b:
                b.pop(b.index(from_user_id))
```



## LRU

```python
from collections import OrderedDict
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.od = OrderedDict()
        self.capacity = capacity
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.od:
            return -1
        ret = self.od[key]
        del self.od[key]
        self.od[key] = ret 
        
        return ret
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.od:
            del self.od[key]
        else:
            if len(self.od) >= self.capacity:
                del self.od[next(iter(self.od))]
        self.od[key] = value
```







註冊、登錄、查詢 (看別的好友之類)、修改info

> ##### [单选题]以下四个操作哪个最频繁？
>
> A.注册3.36% 选择
>
> B.登录44.02% 选择
>
> C.用户信息查询50.67% 选择
>
> D.用户信息修改1.94% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是B
>
> **正确答案:**C



### Scenario

### Service

- Authentication Service
- UserService
- FriendshipService

### Storage

check SQL & NoSQL & Redis 對 QPS數的支持

> ##### [多选题]注册，登录，信息修改使用哪种数据库可以满足？
>
> A.MySQL60.32% 选择
>
> B.Cassandra18.05% 选择
>
> C.Redis13.46% 选择
>
> D.Memcached8.18% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是ACD
>
> **正确答案:**ABC
>
> **解析:**
>
> Memcached 不能持久化存储数据，不适合用来存储用户信息



> * Q: 10k ~ 100k QPS?
>   * 看需求。可以使用单台redis或者使用多台Cassandra的集群，又或者如果你的场景需要高可靠性的事务支持，但是读多写少，那就MySQL做持久化+memcached做cache优化。不同的数据库有不同的功能，这里列出的QPS只是为了告诉你各个数据库的承载能力，不是说xxxQPS就一定要用xxx数据库，QPS不是唯一决定因素，需要结合实际需求分析。
>
> * 为什么Mysql只支持1k 的QPS,但facebook 依然会选择。 facebook的QPS应该远高于1k吧
>   * 单机1k左右，但是facebook的是mysql集群，QPS肯定不是这个量级的
> * redis，memcached会比普通的存储贵吗
>   * redis memcached 用 memory 多，肯定比主要用 disk 的机器要贵的。



讀多寫少，代表經常不會變！

> ##### [多选题]文件系统可以用作缓存么？如果可以，可以做什么的缓存？
>
> A.不可以1.22% 选择
>
> B.用来做网络请求的缓存。30.30% 选择
>
> C.用来做计算结果的缓存34.45% 选择
>
> D.用来做数据库的缓存34.04% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是BD
>
> **正确答案:**BC
>
> **解析:**
>
> 缓存的目的是让访问变得更快。文件系统的访问比网络访问快，一些耗时很长的计算得到的结果也可以缓存在文件中，但是文件系统的访问速度和数据库的访问速度基本上是差不多，所以一般不会用文件系统来做数据库的缓存，意义不大。



> ##### [多选题]下面哪些写法是“不对”的？
>
> 哪些写法可能造成数据的不一致？也就是数据库和缓存中存储的数据不一样。
>
> A.db.set; cache.set29.67% 选择
>
> B.db.set; cache.delete29.48% 选择
>
> C.cache.set; db.set29.83% 选择
>
> D.cache.delete; db.set11.02% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是ABCD
>
> **正确答案:**ABCD



> ##### [单选题]有没有可能第一个执行失败，第二个执行成功？
>
> A.可能，会造成数据不一致55.52% 选择
>
> B.可能，不会造成数据不一致12.52% 选择
>
> C.不可能，不会造成数据不一致31.96% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是A
>
> **正确答案:**C
>
> **解析:**
>
> 不可能。程序的执行是顺序执行的，第一个语句执行出错以后，第二个语句就不会执行了，用户会收到整个 setUser 操作失败的信息。



> ##### [多选题]cache.delete + db.set 什么情况下会造成数据不一致？
>
> A.多线程38.22% 选择
>
> B.多进程28.27% 选择
>
> C.多机器28.65% 选择
>
> D.cache.delete 成功但 db.set 失败4.87% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是D
>
> **正确答案:**ABC
>
> **解析:**
>
> 多机器的话自然而然也是多进程的。



> ##### [单选题]能否给数据库和缓存的操作加锁来保证数据一致性？
>
> A.可以加锁47.11% 选择
>
> B.加不了锁52.89% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 加锁以后只能保证在同一个数据上的操作顺序执行，但是无法执行“回滚”，也就是说如果第一个操作成功，第二个操作失败了，也会导致数据的不一致。
> 另外互斥锁（mutex）是多线程内共享的，多进程内无法共享。如果要加锁，只能使用分布式锁，比如 Zookeeper，但是这会导致读取效率急剧降低。得不偿失。

> ##### [单选题]User Table 的 Cache Hit Rate 一般有多少？
>
> A.20%5.16% 选择
>
> B.50%8.32% 选择
>
> C.95%24.54% 选择
>
> D.98%61.98% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是D
>
> **正确答案:**D
>
> **解析:**
>
> hit rate = cache hit / (cache hit + cache miss)



- 我们允许数据库和缓存有“短时间”内的不一致，但最终会一致。



> * database.set(key, user);cache.set(key)我觉得没有脏数据啊。当第一个线程1执行到15-16行之间的时候。假如有另一个线程2进入setUser这个函数。线程2的cache.set也会覆盖线程1的cache.set结果的啊，所以旧数据就被覆盖了啊。没有脏数据啊，求解释？
>
> 假设执行顺序如下：
>
> ```
> thread 1 line 15: database.set(user) // old data
> thread 2 line 15: database.set(user) // new data
> thread 2 line 16: cache.set(user) // new data
> thread 1 line 15: cache.set(user) // old data
> ```
>
> 最后 cache 里是 old data, database 里是 new data
>
> 线程2的cache.set也会覆盖线程1的cache.set结果的啊
> 在上面列举的情况中，是 thread 1 覆盖了 thread 2。要注意 user 是一个局部变量。thread 2 里的 user 和 thread 1 里的 user 的内容是不同的。



如果寫真的太多太多了，在Cache Aside下，就是加DB啊。



> * redis包含cache和一个db，是说redis里面包含了relational database management system , rdbms么？ 我记得redis只是缓存，没mysql的呢。
>   * redis可以跟mysql配合使用，redis会完全接管mysql，自己从mysql里面load数据，所以在外界**看起来**就像是redis里面包了一个mysql一样。并不是说redis里面有一个mysql。



## Authentication Service

### Session

可以用uuid()算這個hash值

通常用UUID来作为Session Key(Session Token)，UUID(Universal Unique ID): UUID是由一组32位数的16进制数字所构成，所以UUID理论上的总数为16^32=2^128，约等于3.4 x 10^38。也就是说若每纳秒产生1兆个UUID，要花100亿年才会将所有UUID用完。所以通俗的称之为宇宙爆炸都不会出现重复的ID字段。

> * cookie 存在browser 的哪里？
>   * browser 就是一个 client 就是一个客户端软件，是一个 application 是一个 software，一个程序，一段代码。一个 software 要持久化的存储一个东西，最终都是存储在操作系统的文件系统上的。
> * session key一般有效期多久？
>   * 取决于网站的安全等级，比如银行类的一般浏览器关掉 session key就过期了。社交类的一般就三个月甚至更长。这个可以由网站开发人员自行定义。
> * any security problems regarding to session key?
>   * 如果你的 session key 被盗，比如你拿了你男朋友女朋友的电脑，悄悄的记录下了 session key，你就可以以你男朋友女朋友的身份登录了。所以通常一些安全性较高的网站，如银行，session key 几分钟就会失效。
> * session table 是存在数据库里， 还是存在In memory db 里面?
>   * 都是可以的。不过一般都是存在 数据库里，否则memory数据丢了所有用户都会被logout 这个体验并不好。
> * what if i never log in again? my session will live forever?
>   * 通常网站的逻辑都是最多3个月。session table 里有 expire_at 这个 field，记录了什么时候会过期。一般用户登陆以后，这一项设置为 3 个月。当然你可以根据你网站的安全性要求来设置不同的过期时间，安全性越高的网站过期时间越短。一般不会设置为永久不过期。



### Cookies

- 用户 Login 以后，为他创建一个 session 对象
- 并把 session_key 返回给浏览器，让浏览器存储起来
- 浏览器将该值记录在浏览器的 cookie 中
- 用户每次向服务器发送的访问，都会自动带上该网站所有的 cookie
- 此时服务器拿到 cookie 中的 session_key，在 Session Table 中检测是否存在，是否过期
- Cookie:HTTP协议中浏览器和服务器的沟通机制，服务器把一些用于标记用户身份的信息，传递给 浏览器，浏览器每次访问任何网页链接的时候，都会在 HTTP 请求中带上所有的该网站相关的 Cookie 信息。Cookie 可以理解为一个 Client 端的 hash table。

> ##### [单选题]Cookie 里存的东西是越多越好么？
>
> A.是的3.13% 选择
>
> B.不是96.87% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 首先 Cookie 的大小 HTTP 协议是有限制的。其次因为每次 Request 都要带上 Cookie 里的内容，因此 Cookie 里存的东西是越少越好而不是越多越好。

一般就是放個session key表明用戶身份，如掛在胸前的牌，代表授權訪問的用戶。然後去session table查是不是過期了，查uuid(就是session key), 然後知道 user_id，就是client端的hash table。

> ##### [单选题]服务器需要主动删除掉过期的 Session 么？
>
> A.需要34.19% 选择
>
> B.不需要65.81% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是A
>
> **正确答案:**B
>
> **解析:**
>
> 做 lazy loading 就好了。因为有 expire_at，无需主动删除，被动删除即可，即在用户登陆的时候发现过期了再删。

> * session table 是存在数据库里， 还是存在In memory db 里面?
>   * 都是可以的。不过一般都是存在 数据库里，否则memory数据丢了所有用户都会被logout 这个体验并不好。



device token 也可紀錄在 session table, 

> ##### [单选题]Session Table 适合存储在什么数据库里？
>
> A.Memcached21.64% 选择
>
> B.MySQL22.46% 选择
>
> C.Memcached + MySQL55.90% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是B
>
> **正确答案:**C

如果自己建個網站，用戶不多，放在Memcache裡也Ok, 就算斷了，用戶就是再重登一次，不會怎樣，畢竟不是用戶信息的不能丟的。

大網站就最好撐久點，讓體驗好，訪問效率高

> * 那个device id那一块，如何实现？有点模糊。
>   * 就是在每个device第一次登录的时候给他分配一个id，然后把这个id放到该设备的cookie中，每次访问网站的时候都要带上这个id，这样根据id就能知道当前活动的是哪台设备了。
> * db如何设计呢？如何判断这个session 是这个user，然后把之前的ipad的session logout，再让这个iphone的session建立？
>   * 如果用NoSQL，那么表中的每一行可以是{user_id, session, expire_at，其中user_id是foreign key并且建立了index方便快速查找，session在生成的时候可以encode进去user_id的信息，方便直接从session中识别出当前用户。如果是key-value NoSQL，那就直接把上述结构改为user_id ==> {session, expire_at}就行了。
>     当用户登录的时候直接生成一个新的session替换掉原来的。
>     当旧设备的session再次尝试请求数据的时候，先从session中decode出user_id，然后去查表，然后会发现表中的session跟当前的session不是同一个，那就强制logout。
> * 每个device 都会有一个 session key 吗？
>   * session key 和 device 不是绑定的关系。 session key 是记录某次登录后所形成的客户端与服务器端的保持通话的记录的 key。同一台机器上的不同的浏览器登录以后的 session key一般就是不同的。像 Google Chrome 这种支持多用户的浏览器，切换用户以后，就相当于切换浏览器一样，session 记录也是不同的。
> * 如果一个ipad来登陆来了，如何把iphone的session key给expire还是删除呢？如何判断，这2个device是一个user？如果问，如何回答。
>   * 用同一个账号登录肯定就是同一个user。如果登录之后发现在session table中该账号有一个active的session，就可以把这个session 给expire了然后写一个新的进去。
> * 登陆之后，发现该账号已经有一个active user，就可以把这个session给expire了。这个“expire”操作具体是怎样进行的？
>   * 这种情况可以直接删除该行记录。
> * 想问一下RESTful API里面比如POST一个新blog的请求会用session_key来验证user吗？
>   * 也会的，只要是需要authorization的操作都需要验证当前用户的session.



## Friendship Storage & Query

單向：Twitter, Ins, Weibo

雙向：WeChat, FB, WhatsApp

> ##### [单选题]为什么要区分 smaller_user_id 和 bigger_user_id？
>
> A.否则查询 A 和 B 是否为好友的时候会变慢55.84% 选择
>
> B.否则查询 A 的所有好友的时候会变慢32.22% 选择
>
> C.猜不到11.94% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A
>
> **正确答案:**A
>
> **解析:**
>
> 查询 A 的所有好友不会变慢，因为依然是 select * from friendship where user_id1=A or user_id2=A。

> - smaller_user_id，bigger_user_id这里，没有太理解为什么有可能多存一份好友关系。如果已建立好友关系，在什么情况下会出现再次插入同样的好友关系呢？UI端不是应该不支持再次建立好友关系的操作了吗？还是说为了逻辑上更严谨，使A和B成为好友关系只有一种数据存储模式？
>   - 作为一个有经验的工程师，除了在前端要避免重复创建好友以外，后端也是需要相同逻辑的（比如预防一些别有用心的黑客）
>     当你要存 1 和 2 是好友的时候，你可能存为 <1,2> 也可能存为 <2,1>。我们只存成 <1,2> 的形式，原因有两个，第一是方便查询，否则你查询的时候得分别差 <1,2> 是否存在和 <2,1> 是否存在。第二个是节省一半的存储空间。

雙向好友存成兩條還是比較好，雖然多一倍的量，但查詢時不需要 smaller_user_id = x or  bigger_uesr_id = x ，那個 or 的查詢操作很花時間。在線的服務需要簡單快速的查詢語句。可能明年hardware自己就快了一倍，會讓現在的速度優化沒意思。

> - 数据库存的数据越多，不会查询越慢吗？
>   - 会。但是由于据库或者有索引（索引就是用来加快数据查询速度的额外数据结构），又或者本身就是in-memory的hashtable，其查询时长随数据量的增加而增加的曲线其实非常平缓。

transaction - 事务。代表一些列操作要打包在一起，同时成果或者同时失败。比如我转你 10 块钱，你的余额要 +10，我的余额要 -10。这是两条数据库操作，必须同时成功或者同时失败。不能只有一条操作成功。这种打包，就叫做 Transaction。	

> * NoSQL支持transaction吗？
>   * 有一些支持，有一些不支持
> * 保证一个数据库中同时成功或者同时失败的语句是什么？
>   * 这个要靠数据库的transaction机制



## Cassandra as NoSQL

> ##### [多选题]什么是序列化 Serialization，下列说法正确的是
>
> A.将内存中的数据（或者某个 class 的 object）变成一个字符串的过程36.89% 选择
>
> B.JSON 是一种序列化格式27.30% 选择
>
> C.序列化的作用是让数据可以进行传输和存储34.58% 选择
>
> D.我不懂什么是序列化，请多给我讲讲1.24% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是AC
>
> **正确答案:**ABC
>
> **相关知识点:**什么是序列化 Serialization

- Row key : hash key, partition key, 去算存在哪個機器上。NoSQL主要是要實現分布式，不同機器上，不能每台機器上存一份，需要一個sharding或partition的算法。Cassandra會根據row key去算一個hash。不支援範圍查詢。

- col key : 是排序的，類似用B+樹作有序是叫LSM Tree。在同個row key之下。可以是多元組排序。

  

> - sql型数据库是只要建了index就可以支持范围查询的。--- 那sql型数据库，是自动每一个列都建index么？因为貌似每一个列都是可以range 查询的吧
>   - 准确地说是sql型数据库是建立了index就可以支持**快速的范围查询**，即使没有index也是支持范围查询的，只不过会很慢。
>     你需要手动指定为哪些列创建index，因为index是有一定开销的，除了磁盘占用会多一点之外，你每增加删除一条记录的时候数据库也都要维护相应的index。换句话说，快速的范围查询是有一定代价的，所以需要用户自己去权衡应不应该给某一个列加index。
> - 如果把user_id作为row_key, 那么在column_key里再把它放进去其实没什么意义吧？因为查的时候user_id肯定是一个确定的值、而非范围了。
>   - 对，不需要重复访进去。这里只是举个例子。因为有的时候 row_key 不是 user_id。这页 PPT 和上一页在分别讲两件事情。
> - 类似JSON？
>   - 是的，可以通过 JSON Serialize 到 value 里
> - 在NoSQL里有primary key的概念吗？应该如何避免同一个数据被存了两次
>   - 在NoSQL里有primary key的概念吗？应该如何避免同一个数据被存了两次
> - 我通过row_key(user_id) 知道数据存在那一台机器上之后，该台机器上应该是存了很多user的信息的，那我还是在进行一个for循环找到所有该用户的rows吗？再通过friend_user_id 来查找。
>   - 不是的。同一台机器上的数据是按照 row_key + column_key 排好序的，你可以理解为你可以在一台机器上按照 index 去找到你要的 row_key 的那些数据。



NoSQL是以格子為單位的，不是以行為一筆的。

> ##### [单选题]查询最近一天之内关注的好友该怎么办？
>
> A.将 timestamp 设置为 row_key7.75% 选择
>
> B.将 timestamp 设置为 column_key91.15% 选择
>
> C.不会1.10% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B

> - *column key能放多个值吗? 同时放friendID和timestamp*
>   - *yes*
> - *可以设多个Column Key吗？*
>   - *可以的 列存储可以有很多column的*
> - *如果有的时候想sort by timestamp 有的时候想sort by id怎么办*
>   - *建两张表，一张 sort by timestamp，一张 sort by id。插入或者修改数据的时候，两张表都操作一下。*
> - *想请问一下，当查询某个user的newsfeed的时候，我们只已知user_id和想查询的时间段，但是我们不知道会有哪些tweet id。Cassandra的查询不是需要提供row key & column key，才能得知value吗？ 既然我不知道会有哪些tweet id，这样我就无法得知column key是什么*
>   - *在newsfeed的column key里，第一项是 timestamp，第二项可以是 tweet id 也可以把 tweet id放在 value 里。 Cassandra的查询是不需要指定 column key 的第二项的。只要有 column key 的第一项的 timestamp 的 range 就可以了。*
> - *column_key都是cache的吗？那value是在disk上吗？*
>   - *这里主要是想解释为什么把tweet_id放在column key里面好一点。原因是weet_id所对应的tweet data可能已经在cache里了，如果把tweet id放在value中的话，那么就必须要row_key, column_key和value都读出来，这样不能充分利用cache里面的数据。但如果是把tweet id放在column key里面的话，那么读到column key的时候如果发现tweet id对应的tweet data已经在cache中了那就不需要继续去读value了，这样可以节省一步NoSQL读操作。*
> - *复合型的column key是将几个column组合成一个key？还是将原本几个column合成一个column，然后将这单个的column当key (比如合成后的单column 里数据的格式为：timestamp_tweetID)?*
>   - *前者。几个 column 组成一个 key。类似 SQL 里的 multi-column index （composite index）*
> - *这里的column_key,为什么是created_at1,tweet_id1, 这是一个复合的。第一个是按时间，第二个是按tweet id排序，是吗？*
>   - *column_key 可以是一个复合 key。你可以认为是一个二元组，然后按照这个二元组进行排序。那么 column key 在排序的时候就会先按照 created_at 排序，如果created_at 相同的才按照 tweet_id 排序。这里其实不把 tweet_id 放在 column_key 里也没有关系，最主要是需要按照 created_at 排序。*

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdb5m0zj17j30re0i0n3l.jpg" alt="image-20200329221212550" style="zoom:67%;" />

> - SQL不支持分布式吗？
>   - 是支持的，但是一般需要你手动做sharding之类的工作，用起来没有NoSQL的分布式那么简单。而NoSQL大多支持“开箱即用”的分布式。
> - *NoSQL 快是因为用的hash吗？SQL慢是因为不是hash吗？*
>   - *NoSQL快是因为其相对SQL来说少了很多功能，更轻量级。比如NoSQL通常不支持ACID的transaction, 并且大多数据模型很简单（比如memcached就只是存储key-value)，大多不支持自建index，不支持compound index， 有些甚至不支持持久化。少了很多负担，自然就多了很多优化的余地。*
> - *cassandra可以有好几个column key，用起来和SQL的multi key有什么不同？*
>   - *你说的这个是compound key吧？这个是两个不同的概念，compound key指的是在一个表中，可以用两个或多个column的组合来作为primary key，比如一个表中存了某个物体的：（x坐标，y坐标，z坐标，形状，其它信息），那么就可以以(x坐标，y坐标，z坐标）这三个column的组合来作为一个compound key，以此唯一索引一个物体。*
>     *而Cassandra可以被认为是一个巨大的二维数组，row key是第一维下标，column key是第二维下标，因此db[row key][column key]唯一决定了一个数组元素，比如db[user_name][email].*

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdb5ivnrq3j30lu0gqgms.jpg" alt="image-20200329220834459" style="zoom:67%;" />

> - cassandra 第二个表没有user_id 是怎么从user_name 找到 user_id 的？
>   - 第二个表里 username 是 key，user_id 是value，直接就查到了。
> - 在同时创建多张表单时，Cassandra的row_key是email/phone/username,user_id是不是应该放在column_key里？要不怎么找到对应的user_id。
>   - user_id 放在 column_key 或者放在 value 里都可以的。如果你放在 value 里，可以把 column_key 设置为一直是 null。也就是其实你用不上 Cassandra Column Key 排序的特性。另外一个替代的数据库是 RocksDB，这个就是纯 key-value 了。直接key=username, value=user_id 就可以。

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdb5kszh1nj30n60g4js8.jpg" alt="image-20200329221059107" style="zoom:67%;" />

> - 如果A和B的好友比较多，这样耗时比较多吧？
>   - 一般共同好友的功能在双向好友关系的社交网络中才比较有有意义。单向的话，会是“共同关注”，或者你的好友里谁关注了他，一般不会有“共同粉丝”的功能。因此这个“关注” 或者好友的量级一般都在千人这个级别（FB和微信都差不多是5k的好友限制）因此并不慢。

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdb5sm2nyoj30vs0km3zp.jpg" alt="image-20200329221827305" style="zoom:67%;" />

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdb5t57414j30wc0f676n.jpg" alt="image-20200329221858313" style="zoom:67%;" />

> - 直接在A的二度里查B不可以吗？
>   - 在 A 的二度里查询 B 查到了是二度关系，查不到是 >= 3度的关系。这里问题的需求3度也需要知道是不是3度，>3度的标记为 3+。因此只在 A的二度里查B还不够。

> - 如果一个用户没有进行登录或者注册，如何识别两次 Request 来自同一个用户呢？
>
>   - IP Address 是不可以的，因为在同一个局域网下的不同用户会共享同一个对外的 IP Address。
>
>     正确的做法，是为用户生成一个 uuid （Universal Unique ID）作为他的标识，有很多库函数可以生成这个 uuid，这是一个字符串，可以认为不同的用户一定会生成不同的 uuid。服务器端生成这个 uuid 之后返回给浏览器端，浏览器端存储在 cookie 里，之后每次请求都会带上。如果服务器发现 cookie 里没有这个 uuid 就说明可能是一个新用户，就为其分配新的 uuid，否则不改变这个 uuid。这样我们就可以用 uuid 来识别一个未登录的用户了。
>
>     这样的方法如果你清空 cookie 或者换了浏览器以后，可能会被分配到一个新的 uuid，那么你之前的 requests 和之后的 requests 就可能会被服务器识别为两个不同的用户。这个是没有办法解决的了。因为神仙也无法知道你换了浏览器以后坐在电脑前的是不是还是你自己。

