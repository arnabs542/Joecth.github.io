---
layout: post
categories: SystemDesign
tag: []
date: 2020-03-18

---



# Design User System

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