---
layout: post
categories: SystemDesign
tag: []
date: 2019-04-05
---



### Index

![image-20200405214845930](https://tva1.sinaimg.cn/large/00831rSTgy1gdj89p8x7zj31140fqdpo.jpg)

![image-20200405215030180](https://tva1.sinaimg.cn/large/00831rSTgy1gdj8bi4vkpj31180gw105.jpg)

為了減少磁盤磁頭挪動找的次數，二叉的話樹會太高。

![image-20200405215156714](https://tva1.sinaimg.cn/large/00831rSTgy1gdj8czu4cmj30tu0dyjxn.jpg)

唯一：如user_name, email, phone_number

聯合：關手到兩個col的需求要建聯合索合

條件：去篩掉不付錢的，他們的index太大了，我不想查到他們

★聯合索引不能解決分別查 A 的範圍和 B 的範圍然後再求交集這件事情，它是照第一鍵排序後，當第一鍵有相等值的話再照第二鍵去排。然後將查到的id再去原表裡查，也是座標排序法--x不等的照x排序，x相等的按照y排序。



# LBS

Location Based Service



## Uber 技術棧

派單 vs 搶單

### 派單模式

- ringpop ，一種去中心化的架構
- Channel, 高效 RPC
- Google S2
- Riak



### T Channel

一種RPC(遠程函數調用)協議。怎麼把不同進程間內存作序列化傳輸及反序列化解析。

RPC 服務器之間的，HTTPS話還要對資訊作加密，防用戶端的hacker之類。

如果流量不大的話用 http 也ok, http 比較現成，比較好寫，如果要寫thrift還要定義結構，不如json方便。http相對rpc要慢一些，其實主要是設計為客戶端跟服務器之間的通信，而客戶端問題多，搗亂的人多，需要驗證，要提供放cookie裡的驗證，一下就好幾k到好幾10k，而服務器之間其實可能就只要幾百個字節。

RPC還多了壓縮，讓效率高、延遲低。server2server就放LAN, 也不用加密。不用擔心不合理的傳來的數據。防驗證該是firewall該做的。

> ##### [多选题]现有的比较成熟的、广泛使用的RPC协议有哪些？
>
> A.HTTP27.04% 选择
>
> B.Thrift38.66% 选择
>
> C.ProtoBuf34.30% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是AB
>
> **正确答案:**ABC
>
> **解析:**
>
> Thrift 是 Facebook 的，ProtoBuf 是 Google 的。
> Http 也可以认为是一个 RPC。

> ##### [单选题]生活中运用地最广泛的RPC协议是？
>
> A.HTTP97.39% 选择
>
> B.Thrift1.21% 选择
>
> C.ProtoBuf1.40% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A
>
> **正确答案:**A
>
> **解析:**
>
> HTTP 是 client （如 Browser) 与 server 通信的协议。是非常典型的 RPC。

> - RPC跟REST API有什么不一样
>   - rest api一般指的是定义好的http 接口，rpc是一种通信协议
> - Thrift, ProtoBuf和HTTP协议差别在哪里呢？
>   - 差别可多了，比如最主要的差别是 thrift 和protobuf 的通信量相对 http 都很小，速度也就快很多。其他的差别，建议您可以去 Google 一下 thrift 和 protobuf，或者写一下 thrift 的调用代码和http 的调用代码来体会。
> - RPC跟RESTful API 有什么不同？
>   - RPC 是一类协议的统称，Restful API 是一种编码规范。
>     Restful API 也是一种 RPC。我们说过 RPC 的时候通常说的意思是“远程调用”，我们说 Restful API 的时候通常指的是 "GET https://xxx/api/users/" 之类的 Web API 设计。Web API 当然也是一种“远程调用”
> - 请问 用Flask写的API和用grpc写的API有什么区别？两者对比有什么好处呢
>   - **Flask 之类的 Web Framework 写的 API就是一个 HTTP API。相比于 GRPC 或者 Thrift 之类写的 API 而言，最主要的区别是 HTTP 的 Request 整个数据传输一般比较大，因为要包含 HTTP Header, Cookie 之类的很多东西，其实很多时候用不上。所以 GRPC 之类的会高效不少**。
> - client make a request to server 是都要用HTTP协议？
>   - 不一定的，也有用其他协议的。只是大部分都用 http，简单方便成熟。
> - server to server之间的通信的内容什么？不同伺服器上的数据？
>   - server to server 当然也是有通信的需求的。**比如在Uber设计中，GeoService 里的 server 就存储了地理位置信息，并提供了访问地理位置信息的接口。这个 GeoService 可以服务于 Uber 打车，还可以服务于 Uber 外卖。不同的其他的 server 都可以调用 GeoService 来存取数据，这就是服务器间通信。**
> - RESTful API 是基于http protocol的？
>   - 是的。



### Google S2 & Riak



## Scenario



> ##### [多选题]对于一个打车软件来说，最核心的两个功能是什么？
>
> A.支付功能10.34% 选择
>
> B.汇报位置34.47% 选择
>
> C.匹配乘客和车辆45.34% 选择
>
> D.评分系统0.31% 选择
>
> E.一键报警0.31% 选择
>
> F.路线导航9.22% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是BC
>
> **正确答案:**BC
>
> **解析:**
>
> 支付并不是最重要的，完全可以做一个免费的打车软件，但让司机汇报自己的位置和为乘客匹配一个合适的司机是构成一个打车软件的基本功能。

- 該可以時不時更新司機位置
- 為乘客匹配司機
- 司機同意就繼續完成派單
- 直接司機告訴服務器自己在哪



會發現他一天會有幾單，會橫跨幾個城市，全市

- 有集會時會有大量單，所以透過偷偷蒐集用戶地點，我們可以提前調度司機往那邊跑。
- 但這理論上是蒐集隱私的行為哈



## Service - Geo & Dispatch

> ##### [单选题]图中漏了什么？
>
> ![图片](https://tva1.sinaimg.cn/large/00831rSTgy1gdkglvyl64j30ky0c8ju9.jpg)
>
> A.司机和乘客的双向联系23.16% 选择
>
> B.司机获取到打车订单信息45.00% 选择
>
> C.司机当前接单与否的状态31.84% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是C
>
> **正确答案:**B



> - Dispatch service 里面包含逻辑处理 + 数据存储。能否解释一下数据储存？这里的数据储存存的是什么数据？是否是司机的地理位置数据？
>   - 地理位置数据可以存在 GeoService 里。Dispatch Service 里存的是派单（Dispatch）信息的数据，比如我把哪个司机分配给了哪个乘客，这个在我们的课程中是存在 Trip Table 里。即用户点击打车就创建了一个 Trip，当分配了一个司机以后，就往里填进去被分配的司机。



## Storage - Trip & Location

> ##### [单选题]Trip Table 的读写情况如何？
>
> A.读多写少25.16% 选择
>
> B.读少写多36.25% 选择
>
> C.读写一样多38.58% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是C
>
> **正确答案:**A
>
> **解析:**
>
> 只有产生用户请求时才会产生写操作，查询操作比较多，因为每隔四秒司机都会需要查询是否有与之匹配的订单



> ##### [单选题]Location Table 的读写情况如何？
>
> A.读多写少8.05% 选择
>
> B.读少写多71.88% 选择
>
> C.读写一样多20.08% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 每隔四秒司机的位置都需要被更新，属于写操作；读取操作只有在查找乘客附近的司机时才会发生。

> - 对这个流程有些疑惑，为什么不等到driver同意pick up之后再往trip里写一个新的record，这样不是可以避免driver反复查询吗
>   - 有很多原因。首先，对那么没有成单的打车请求，也有记录数据和分析数据的需求，不仅仅是记录那些匹配上的单子。其次，当一个打车请求产生一个，我们需要提供给打车的人一个查询主体去让他查询有没有匹配上，因此势必是要创建一个 Record 的。至于这个 Record 是一个 Trip 的 Record 还是一个 PendingRequest 的 Record，这个就看你自己愿意怎么设计了。我是觉得统一都是 Trip ，用 status 来标记不同时期的状态是比较好的做法。
> - 如果app上要显示location的话是要读的吧，所以是不是应该是读写一样多呢
>   - 是的。
>     这是属于另外一个功能点的要实现的service-trip routing service。
>     其实这个系统中的Dispatch Service和Geo Web Server还可以分化出来一个专门复杂计算匹配功能的Matching Service 出来。
> - 请问driver要怎么从trip table查询他有没有被assigned到某个trip? 是对driver_id做 index，让我们可以直接search吗？
>   - 是的，对 driver_id 有 index 就行了。
> - 数据库定义 外键会不会影响性能呢？
>   - 定义外键就必须给该列建立索引，这样可以加快查询时的速度，但是相应地在数据更新的时候会花费一些时间来维护索引。



# LBS 難點

- 數據庫不好查圓，改求正方形

> 课中练习
>
> [单选题]分别对 latitude 和 longitude 建index是否可行？
>
> 你的选择:B
>
> A:可行
>
> **B:不可行**



那建複合索引ok嗎？就是二元組排序

[单选题]复合索引是否能解决 查询效率低下的问题呢？

A:可以

**B:不可以** 仍是不行



要找兩個key都在某個範圍內的range query仍是無法做的，只能找到同lat下的log的範圍。

***所以，將二維映射到一維做***

## 2D Range Query

映射到一維的range query，相當於對二維作range query

- Google S2 --  Hilbert Curve, 一維上近的，二維上的也近；反之否。
- Geohash -- Peano Curve
  - 0-9, a-z 去掉 a, i, l, o 為 base32剛好2^5, 因為長相容易看錯，發明算法的人決定去掉這四個char的
  - find longest-common-prefix

> - 所以说Hilbert mapping如果两个点二维空间接近， 一维上不一定接近对吧（比如说最中间的四个点）
>   - 是的。但是反过来是对的，一维越接近，二维就越接近。
> - Google S2怎么解决障碍物的问题？比如河流，单行线等。
>   - Google S2不能解决障碍物的问题，障碍物的问题是交给地图解决的。在或取到附近的司机之后，可以过一遍地图，查一下路径，如果不可达或者要绕远路的话可以排除掉。
> - 为什么不直接按地域分，然后在这个地域里直接用for loop算出每个坐标和用户的距离？这个是O(n) 是不是因为 SQL查询是O(logn)所以更快？
>   - 这样就要对每个用户都算一遍距离，n个用户就要对所有坐标算n次，开销很大。而用Geohash就只需要做一个range query就行了，range query一般有索引支持，做起来很快。
> - 对两个column都是range query的情况，如果用复合索引的话，虽然对第二个column是无序的，但是因为第一个的range已经选出来，这时如果delta比较小（range范围小），对于第二个column也只用遍历第一个选出来的部分，相较于加索引的log（n）会差别很大么？
>   - 你的这个假设 delta 比较小是不合理的，我们大部分的需求都是 delta 比较大的。如果你说数据小的话，那什么办法都可以，不加索引也可以。数据小是无敌的。
> - GoogleS2算法会将那些2D近，1D远的点漏掉对吧？所以它是不是精准度差？
>   - Google S2会比Geohash精准一点，因为Geohash存在一些很大的突变点，比如两个相隔很近的点刚好分到两个不同的格子的话就会使它们的前缀完全不一样。但是Google S2用的是一种突变没有那么严重的Pieano Curve，因此精准度会高一点。



## GeoHash

把地球表面分成一個個大格子，並用各個char代表，多次畫分成32份下去，無限逼近所在的位置。

公共長綴愈長，兩點愈來愈接近

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdl1zh1cgbj30sg0f2ta2.jpg" alt="image-20200407114112281" style="zoom: 33%;" />

> - geohash算法中，如果两个点在分界两边，但其实离得很近，算法会分成两个不同的字母数字么？造成的误差怎么处理呢？
>   - 会很大。一般不处理。因为人会走动，走两步，这个误差就没有了。系统设计不需要保证 100% 正确性。后面的讲解中也会提到。
> - 如何处理处在分界线两边很靠近的两点的情况？比如美国的两点很接近，但分属9和d?
>   - 这个是GeoHash的一个缺陷，即使两个点相隔很近，其字符串的前缀也有可能完全不一样。不过在实际应用中可以有一些方法来弥补，比如在数据库中找距离x点在一定范围内的所有点的时候，除了搜索跟ｘ在一个小格子内的点之外，还可以搜索出于ｘ所在的格子相零的八个格子内的点，然后再汇总结果，这样就不会漏掉答案了。

- 為何是4x8? 而不是5x10、3x6這類的1:2?
  - 因為GeoHash是一個二分法，實數可以無限往下二分除，得到很長的０１串
  - base32 去遞歸地劃地圖 <img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdl29586ydj30c808wjt0.jpg" alt="image-20200407115146360" style="zoom: 33%;" />
  - 靠得近有時候geohash還是差得大，但人剛好處於這個大分界上的機率很小，可能下一秒就不在這個分界線上了

> - Geohash为什么不直接比较二进制数，而是比较hash以后的string呢？
>   - 为了最终得出来的表示是整数位，base必须选取2的次方，因此可以将geohash存成2进制、4进制、8进制....等等。这里之所以选32进制是因为这样比较compact，而且最终生成出来的字符串可以被放在url里面，比如http://api.com/get_nearby_taxi/9q9hu3hhsjxx
> - Geohash为什么不直接比较二进制数，而是比较hash以后的string呢？
>   - 因为 GeoHash 如果存成二进制的话，肉眼不可读，不利于放在 url 里传播，也不利于别人复制粘贴。有方便“人”使用的考虑，如果只是给计算机看，二进制当然是可以的。
> - geo hash 为什么要比较string？ 不直接比较二进制数？
>   - GeoHash 用字符串有如下一些好处：
>     1. 可读性高，可以直接让人阅读和复制，类似登陆验证码你不能给人一个二进制让人输入吧
>     2. 可以放在 url 里，方便 url 的传播。

 

### Range Query in GeoHash in DB

視需求要在多少距離內去map找 longest-common-prefix

e.g. 找附近20km的車

> - 这里cassandra的row key是什么呢？
>
>   - 在 GeoHash 的例子中，row_key 可以是前 4 位的 GeoHash，后面的内容里有提到如何 sharding 的问题。
>
> - 这种找共同prefix的问题是不是通过Trie来实现更高效啊。Redis那种方法其实就是通过hashtable的方式实现trie. 那SQL和Cassandra为什么不通过trie来实现呢，节省空间吗？
>
>   - Trie 和 Hash 的效率是一样的，查找一次时间复杂度都是 O(L)，L 是字符串长度（你需要去九章算法强化班补习一下这部分的内容哦）Trie 唯一优势是空间稍微省一些。像 SQL 和 Cassandra 这种数据库的结构是不支持 Trie 的。Trie 是算法和数据结构领域的东西，而不是数据库领域的东西。没有任何数据结构原生的支持 Trie，但是所有 key-value db 都可以认为是一个 hash table on disk。
>
>     TODO: *多比較此概念, https://leetcode.com/problems/longest-common-prefix/solution/*
>
> - ***Redis的情况是要建立32^6+32^5+32^4个key吗？按讲义，9qhhvt,9q9hv,9q9h都是key***
>
>   - 是的，理论上最多会有那么多个key，不过考虑到有很多无人区（海洋，荒山，沙漠啥的），而且公司业务一般不会完全覆盖整个地球，所以实际的数量其实不会达到那么多。如果真的一台机器放不下的话还可以sharding。
>
> - cassandra的value没有null明白了，那么可不可以有“”(空字符串)呢?另外，cassandra是不是可以不设置columnkey从而只有rowkey和value呢？谢谢。
>
>   - 不可以不设置 column key ，否则无法排序`<row key, column key>` 这个二元组。也无法对 column key 进行 range query。你的需求适合直接放在 RocksDb 这种只有 key-value 的结构里，不适合放在 row key column key value 的这种结构。
>
> - 相当于一个driver的位置要放到三个key的set里面？然后会根据driver位置的变化，会动态地增删这三个set？
>   
>   - 是的，如果位置分三级的话就是要动态增删三个色它
> - cassandra 的 rowkey 和 column key 的差别是什么啊？ 可以简单说一下吗？
>   - Cassandra 中的 row key 就是 hash key 也叫做 partition key，是每次查询必须带上的（第二第三节课里有讲哦~），主要作用是当确定这个数据存在什么地方，你可以认为有一个函数叫做 `find_db_instance_by_row_key(row_key)` 能够根据 row_key 确定使用哪个 db instance，从而实现分布式存储。
>     很多 NoSQL 数据库没有 column key，比如 Redis。 Cassandra 有 Column key 的作用是，在一台数据库的机器上，所有数据是按照 row_key+column key 排好序的。所以当你确定了 row_key 是啥以后，就可以对 column key 进行范围查询，比如你可以查询 user_id（rowkey） 发的所有帖子里，在 昨天到今天这个范围内发的帖子（帖子的发表时间作为 column key），而 Redis 因为没有 column key 是做不到的。另外在后面的 Big Table 中，会详细介绍这类数据库的实现原理（BigTable 也是一个有 column key 的 db）
> - cassandra把geohash放在column key，那row key该存什么，可以全都存在同一个row key下吗？例如null？
>   
>   - Row key 存 geohash 的前 4 位。
> - cassandra的row key是什么
>   
>   - 前 4 位 GeoHash



### 雙方角度思考業務跟儲存需求

> - 为什么不需要对driver按离rider距离远近排序？
>   - 要排也行，可以在match的时候将最近的区域内的司机按距离排个序，然后选最近的。





### Scale

用戶無遷移成本，所以用戶黏性太差，分分鐘用戶就換別的用。

> ##### [单选题]司机的 Location 信息应该按照什么进行 Sharding？
>
> A.按照 User Id6.23% 选择
>
> B.整个 GeoHash10.18% 选择
>
> C.GeoHash的前4位72.04% 选择
>
> D.GeoHash的前6位11.56% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是C
>
> **正确答案:**C
>
> **解析:**
>
> 按照 User Id 是显然不对的，因为乘客的 UserId 和他附近的司机的 UserId 可能会被 sharding 到不同的地方。
> 按照 GeoHash 进行 Sharding 的话，只需要按照前 4 位进行 sharding 即可。因为乘客的查询可能是按照前4，5，6位 GeoHash 进行查询，如果是按照前 6 位进行 sharding 的话，那么 BBBB22 和 BBBB33 就会被拆分开，而我们查询的时候其实希望如果用户在 BBBB22 的话，他能够查到位置在 BBBB33 的司机。

城市不多，每個城市也是幾10個點圍出來的，可以在code裡直接寫死。

> - redis内部有自己的sharding机制么？需要自己手动写sharding算法还是只需要给sharding的column就可以？
>   - 早期的版本没有。最近新出的版本里有 auto-sharding 的机制了，但是不是 consistent hashing 的算法，用的是另外一个，有兴趣的话，可以去网上搜一下相关的内容。
> - 但是有的城市uber的用户比较多，比较频发，有的城市用户比较少，怎么样能sharding的均匀呢？
>   - Uber 的做法是为用户多的城市多配置机器。用户少的城市少配置机器。
> - 按照city sharding，如果这个城市里有很多driver，该如何判断哪一个driver离这个乘客比较近？
>   - 按照 city sharding 以后还是需要根据 geohash 去 filter 的。sharding 只是宏观上数据怎么拆分，geohash 是微观上具体每一条数据存储时的信息。我们根据 **geohash** 可以做范围查询来 filter 离乘客比较近的 driver。
> - 找到乘客周围的2-3 个城市怎么就能避免乘客算a city driver 算b city 但是其实两个人离得很近的问题？
>   - 他俩隔得很近，那么说明 a city 和 b city 隔得很近。因此找到乘客周围 2-3 个城市的意思就是，既让乘客属于 a city ，也让他属于 b city，总共查2-3次。



### Riak

Redis 有 Master slave的機制，M掛了S可以頂上去。

但其實可以用穩定性更強的DB, 更好處理掛掉後恢復的問題。

Uber也是從Redis換成了Riak。

> - master挂了的话，slave可以进行写操作吗
>   - 不行，必须起一个新的master。
> - 之前课程不是说涉及transaction要用SQL吗？ 为何这边都是用NoSQL？
>   - 这里并不需要用到 transaction，所以用 NoSQL 没有问题。且有一些 NoSQL 也支持 Transaction 了。



## Q&A

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdj8kcgjkzj30kc0m8gn8.jpg" alt="image-20200405215453781" style="zoom: 25%;" />



<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdj8kg0owrj30kc0ws779.jpg" alt="image-20200405215851312" style="zoom:67%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200407165538615.png" alt="image-20200407165538615" style="zoom:67%;" />

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdlb1n83q9j30oc0j8tby.jpg" alt="image-20200407165557659" style="zoom:67%;" />

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdlb2i72zyj30ow0msn15.jpg" alt="image-20200407165647857" style="zoom:67%;" />

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdlb36wqt9j30pa0t00yp.jpg" alt="image-20200407165727152" style="zoom:67%;" />



# Appendix

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1giblli29hij31gm0u07q8.jpg" alt="image-20200902000656510" style="zoom:67%;" />

