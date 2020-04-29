---
layout: post
categories: SystemDesign
tag: []
date: 2019-04-10

---



# General



# Pre-requisite

## Serialization

- 把RAM裡的數據存上disk或傳輸，如array ==> "[1, 2, 3]"
  - 不能讓別人來自己的RAM拿，重開機也都不同了
- 不同類可以定義不同。
- java 的 toString() 只是要打出來看，沒要反序列化，不見得算是
- 如果序列化沒要給人看，還會考慮盡量小
  - FB有 thrift，是一個RPC的庫，可做序列化、反序列化，可壓縮數據，如定義一個class結構，只要我的obj是滿足那個類的，就可以丟進去，肉眼不可讀，壓縮率高。當我們加屬性，反序列化還要不出錯！
  - Google有protobuf。類似的事。
- JSON / XML (Web1.0、Android),
  - 現在Web都是JSON，空間小，可讀
  - 如POST過來有各屬性及其對應的values 



## Cookie & Session

- cookie 客戶端
  - 把 Token放在Cookie裡，長度有限制的，一般跟身份認證有關。
  - CSRF 偽造用戶的表單；當post來的時候必帶CSRF，當生成網頁時才會生成，有一定時間如５分鐘內。動態碼去避免攻擊
  - 可設有效期
- Session 服務器
  - Authentication Token 
  - Session Table 存 Authentication Token，看哪個用戶登入了
  - 一般存在數據庫裡較多



## Message Queue

- 是個Queue, FIFO
- 1. 任務慢. 2. 需要重試
- 消息隊列不放聊天的消息；一般是放任務ID之類的
- 生產者、消費者模型 -- 多線程題
  - 兩邊速率不一致
  - 倉庫就是緩衝
- Web 用 MQ緩衝，worker 去拿 MQ，好了後worker寫到DB，Web自己去刷新或時不時看下DB
  - Cache, DB 都是最基本構成
- 評測機 - 生產消費者、MQ
- 發email - 要是發失敗的話，也是MQ可以幫忙的

- 一般常用的
  - RabbitMQ, 
  - Redis 什麼都會一點，可當數據庫(比不過SQL, NoSQL)、緩存(比不過Memcached)、消息隊列(比不過RabbitMQ)；但速度比較快，內存級別速度，存取效率非常快
  - AWS Simple Queue Service 消息隊列的雲服務；保證兩個worker拿不會有不同人重覆處理。浪費，也可能有問題如重覆扣錢。螞蟻是處理萬億級別的，用的消息隊列機制很牛。
- 鏡像機制，兩台MQ一直作鏡像，一台專門copy，雙Master, 同時分擔讀和寫
- 重試機制。
- 12306一定會有message queue，一堆的請求不會馬上被解決掉，看先來後到。
- 可設優先級
- 可有子queue。如登機時不同的排隊。隊列之間是可以併發的，但同一個隊列是FIFO的

> - 消息队列 - AWS SQS 和GCP Cloud pub/sub
> - kafka做message queue的场景也挺多的吧。
>   - 是的







# Chat System

> [单选投票题]微信是点对点通信么？
>
> 你的选择:B
>
> 感谢您参与投票！
>
> A:是的(20.62% 选择)
>
> B:不是(79.38% 选择)



## Message Service == > Storage

> ##### [多选投票题]我们需要在聊天软件的Message Table里存储什么？
>
> 您选择的答案是ABCDEG
>
> 感谢您参与投票！
>
> A.消息的主键 id14.74% 选择
>
> B.发送人15.94% 选择
>
> C.收件人15.67% 选择
>
> D.ip 地址2.66% 选择
>
> E.发送时间16.09% 选择
>
> F.信息类型11.38% 选择
>
> G.信息内容14.84% 选择
>
> H.会话 id8.69% 选择

表單的設計很重要，不然效率太差。



## 增加 Thread Table 

不用 Session這個字，而用Thread, 就是一個Conversation。

> ##### [单选题]这样的Thread Table有什么问题？
>
> A.信息会有遗漏12.08% 选择
>
> B.信息查询比较慢50.14% 选择
>
> C.有些信息是私有的37.78% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是B
>
> **正确答案:**C　－－　如你讀了但我還沒讀但群裡對我而言就變已讀

> - 假如需要知道A&B之间的对话历史 怎么知道他们的thread ID呢
>   - 可以根据 participant_hash_code 去反向查询到 thread_id。课里有讲到。



## 拆，加User Thread Table

> - 存last_message 是为了显示在界面上面吗？
>   - yes
> - 为什么用id做primary key做sharding会影响效率？
>   - 因为一般我们查询UserThread都是根据user_id去查的，因此要按照user_id来做sharding，这样当我们想获取某一个用户的所有thread_id的时候，就可以直接计算出数据所在的shard。如果用id来做sharding的话，就只能广播到每一台机器查询，然后再汇总结果。
> - 为什么这里直接就用了SQL型数据库？noSQL完全不能用吗？
>   - 用 NoSQL 和 SQL 都可以的。这个课里的观点一直都是，你喜欢用哪个就用哪个。很少一定要用 SQL 或者一定要用 NoSQL。这里会讲解按照 SQL 是如何存储的，后面会讲解按照 NoSQL 是如何存储的，两种方法都可以。



> ##### [单选题]这样的存储方式有什么弊端？
>
> A.需要跨表查询比较慢63.87% 选择
>
> B.信息会有遗漏5.72% 选择
>
> C.限制sharding效率30.41% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A
>
> **正确答案:**A

**跨表用到 JOIN就會慢，要解決掉…**



## 合，

把公有復制到每個人裡去

這樣做時，當要拿當前用戶資料時，就可以一張表出來，不用再做JOIN；但也有壞處

> ##### [多选题]全部放在一个 UserThread 表单里有什么坏处？
>
> A.需要跨表查询比较慢3.02% 选择
>
> B.冗余存储50.89% 选择
>
> C.更新可能会造成的数据不一致问题41.56% 选择
>
> D.信息会有遗漏4.53% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是BC
>
> **正确答案:**BC

Updated_at 雖是共享，也是分在每個裡，因為要用他做排序

更新操作是避不開的。

> - 这里合成一张表算denormalization吗？
>   - Yes
> - 能两全吗？
>   - 系统设计很多都是trade off，如果有完美的方法我们肯定会优先用完美的方法的，这里的话只能是选定一个方案然后再用一些手段(比如Cache)去减轻其缺点带来的影响。
> - 这算不算在内存里做JOIN操作？
>   - 可以这么理解。
> - 所以在面试中是不是用SQL数据库比较好分析这个题？面试官如果没有要求用noSQL就不要提？
>   - 看你更熟悉哪个。其实 Chat System 是更适合使用 NoSQL 的。你设计的时候用 SQL 问题也不大。面试官一般会根据需要向你针对性提问的。



**所以比較下來，拆還是比較清晰，Thread、用戶分開，比較 DECOUPLE，如果問到 JOIN 再用「合」放在一起，復制幾份，反正字節字不多，全拿出來不用再JOIN。實際工程去 Cache拿，避開 JOIN**



## 怎麼查 Thread ID? 

當用戶發信息時或建群聊時，所以要針對現有看是否他們有現有群

- 用參與者查有沒有他們的Thread
  - 可樣在 Tread Table 增加一個 participants_hash_code，這樣有以前的群就可以找到
    - user排好序後，大家串一起做個uuid，看有沒有以前的群
    - 可以把這個uuid作index查就很快
    - 為何要hash? 群聊太長啦
    - uuid就不用去考慮相撞，概率不可能

> - 群聊的话可以有新的用户加进来，这时候要更改这个hash code吧？
>   - Yes
> - 如果有些群聊有人加入有人退出怎么办？participant_hash_code也要改变吗？
>   - Yes, 也要改變。
> - 如果participant更新是不是要重新generate uuid？
>   - 是的，需要重新生成 participant_hash_code



## Message Table 表單結構

用戶就是一直聊一直聊

要找寫快的，所以NoSQL, 有機會 1.5M QPS，檢索就是 kv。

> ##### [单选题]需要查询thread里的message时sharding key（row key）是什么？
>
> A.user_id11.42% 选择
>
> B.created_at9.40% 选择
>
> C.thread_id56.81% 选择
>
> D.participant_hash_code22.36% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是D
>
> **正确答案:**C

> - 支持消息撤回(recall)的话，一条消息在还允许撤回的这个time window里，也是写在message table里吗？具体撤回是怎么实现的呢？
>   - 增加一个类型的 message，这种 message 就表示要撤回哪条信息。然后客户端拿到这样的信息以后在客户端把消息隐藏掉。这里可能有另外一种容易想到的但是是错的方法是给 message 增加一个是否被撤回了的标记。这种方法有问题的原因是，一般 mobile client 上的信息更新都是增量式的，也就是说，一旦一个消息被下载下来，会在 client 端里也存储一份，并且不会再去检测这条消息是否有被更新过（否则那 client和 server 负担就都大了）因此需要通过“增量式”的方式来更新这条数据的信息，那么自然就是通过一条新的 message 来撤回老的 message。
> - 在cassandra里，可以理解为row key 就是等于 sharding key 吗？有任何反例吗？
>   - row_key = sharding_key 没错，没有反例，就是一个东西的不同称呼。



## NoSQL with Thread Table

也可以用SQL，兩者都Ok。

index by thread_id 以及 participant_hash_code

> ##### [单选题]Thread Table 如果使用 NoSQL 该如何存储？
>
> A.一张表单，row_key为 user_id3.44% 选择
>
> B.两张表单，row_key为 participant_hash_code 和 user_id7.07% 选择
>
> C.两张表单，row_key分别为 thread_id 和 user_id21.41% 选择
>
> D.两张表单，row_key分别为 thread_id 和 participant_hash_code68.07% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是D
>
> **正确答案:**D

用雙表去模擬SQL的單表雙index(背後也是幫建表加速)

也不range query就不用 column, 所以可以就 RocksDB

> - 可以根据created_at来排序column_key 吗？这样可以找到最新20条消息？
>   - 这个其实可以在获取完thread列表之后再按照last_message的时间戳在客户端进行排序，这个排序工作量很小，不需要在服务端做。



## NoSQL for User Table

> ##### [单选题]UserThread Table 用什么做sharding key（row key）？
>
> A.user_id68.04% 选择
>
> B.created_at1.37% 选择
>
> C.thread_id24.24% 选择
>
> D.participant_hash_code6.35% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是C
>
> **正确答案:**A

怎麼取就怎麼sharding...

> - 当web server收到一条群聊的消息，他要怎么知道要往哪些用户发送呢？方法1的thread table已经没有participant_user_ids，只能靠user thread table来得知有谁是属于这个thread。但是user thread table的sharding row key是user id，所以如果要查询participant list，只能scan完所有的user 才能知道谁是属于这个thread。
>   - 需要增加一个 ThreadParticipant 的 Table。记录谁参与了哪些 Thread。



## Flow 

B polling

每隔一段時間的PULL就是POLL



## Scale, GCM & APNS

- 怎麼讓消息更實時？
  - PUSH NOTIFICATION
- PUSH: 手機上
  - Android GCM (Google Cloud Messaging)
  - Windows 也有它自己的推送系統
  - iOS APNS (Apple Push Notification Service)
    - 不同的手機有device token, app註冊完會有, APNS會發給手機, server 拿這個當 push token 去推送給 B，B再過去取 Web Server 取。局限性呢？

> ##### [单选题]这样的方法有什么局限性？
>
> A.获取新消息时可能有延迟26.92% 选择
>
> B.数据库压力过大10.22% 选择
>
> C.消息丢失概率大12.08% 选择
>
> D.无法支持web端50.79% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是D
>
> **正确答案:**D

> - 这个push notification system在手机系统上是指的它实际运行过程中是在用户的手机上吗？（比如用户手机就是一个server）还是说apple有其他外的服务器来支持apns？
>   - 用户的手机是一个 client 不是一个 server，用户的手机不需要给其他人提供服务，他只问被人要服务。Push Notification System 是 Apple/ Google 单独搭建的一套服务器系统，专门用来提供 push 服务。
> - 是不是现在也有些浏览器提供push notification？比如Chrome？
>   - 浏览器的push notification本质上就是一个弹出的对话框，本质上还是网页自己基于websocket一类的技术实现的，跟GCM/APNS原理不一样。
> - 不太理解为什么server不直接和B通讯呢？通过GCM作为中介的好处是？
>   - APNS/GCM都是专门用于移动端的消息推送的，为消息推送提供了一个与操作系统深度整合的、高度优化的框架，如果不用这个的话，就得自己重新造一套这样的消息推送框架，费时费力，而且标准不一。而且假设你有50个app, 如果每个app都需要链接各自的push服务器的话，会给手机带来很大的负担。具体的讨论可以看这里：https://stackoverflow.com/questions/31645010/why-it-is-preferred-to-use-gcm-for-push-notifications

沒有提供給所有的browser推送系統的。該怎辦呢？



### Socket

解決的辦法就是自己搭push的服務，不要依賴第三方的push 通知服務。實時性會更高。

★ HTTP 只支持客戶端向服務器獲取數據，因為Server不知道客戶在哪； client to server 是有ip、域名的

Socket是讓服務器可以主動向客戶端推數據。

Socket, 跟 http一樣都是tcp/ip，本來就都可以雙向通信。http不能保持連接，socket可以。

要是push server掛的話，就回到PULL，10秒拉一次，反正client是知道連接斷開了的

> - 为什么不用 long polling呢
>   - 当clients很多的时候，long polling会让server返回大量的空结果（没有新信息的时候），这样会给server带来很大的负担，比较浪费资源。
> - Push server needs to keep too many connections, would not this be a problem?
>   - yes, so push server always push messsges async
> - push server是不是和message queue/kafka差不多？
>   - 不是的，push server 和 message queue 是完全不同的东西。push server 里就是通过 socket 连着用户，有消息就推一下而已。而 message queue 是把需要执行的任务信息存储在 queue 里，等着执行任务的进程来逐个领取的一个中间缓存机构。**本质上来说 push server 是 stateless 的，是不存数据的。message queue 是 stateful 的，是存数据的**。*就跟 web server 和 database 之间的本质区别一样。*
> - 如果A或者B离线呢，消息存在哪？
>   - 消息存在 Message Service 里（数据库里），socket 只是“提醒” 的作用，并不是说消息只从 socket 走。你可以认为 socket 里走的数据是“嘿你有消息了，去服务器拿一下”，然后用户去服务器拿到最新消息。



### Group Chat

大群裡，可能只有很少人在線，就是只有很少人需要被即時推送。

這樣也不需要優化得那麼實時。

> - 相較於使用channel 篩選在線用戶的方式, 老師後面有說可以建一個 online status 的 table, 那我是不是可以直接從online status裡面檢查群聊還有在線的, 直接send message給在線的就好. 感覺好像比用channel還要subscribe的方式簡單?
>   - 不行。online status table 里在线不代表这个人已经连接上了 push socket（虽然大概率是连着的），但是这种反向调用关系是不好的架构设计，类似写代码的时候底层函数调用了上层函数，会导致系统之间的依赖关系出现循环依赖。
> - 一般来说是多少人以上的群采用channel service呢？还是说哪怕两个人私聊也算一个两个人订阅的channel?
>   - 一般可能10+ 人才会走 public channel。如果是私聊，走的是 private channel，也就是说，比如你的 user_id 是 10，那么所有和你私聊的信息，都走到 "#user_10" 这个channel里去（这个channel名字的格式你自己可以随意定义）。你一上线也会自己订阅这个channel。这个channel 只属于你自己，不和别人共享。
> - 这里的channel service可以换成message queue么？生产者也是只用发一次消息，然后订阅的消费者去取这些消息？这里channel service和massage queue有什么区别？谢谢
>   - 不可以。channel service 是 fanout，是广播。一条消息会被多个 subscriber 拿到。message queue 不是广播，一条任务消息必须保证只被一个 task worker 拿到。
> - channel service 可以用kafka么？
>   - 这样用不太对。kafka 是消息队列，channel 是一个 key-value 的存储 + 信息 fanout。
> - 所以用户下线以后就自动取消订阅channel service吗？
>   - 用户下线的时候push server会知道用户下线了，然后push server会把这件事通知给channel service。
> - 如果用户不在线的话，历史消息怎么办呢？是储存在channel service里面吗？
>   - 用户不在线的时候channel service就不会给相应用户推送，也不会保存这条消息，channel service只是为了给在线用户实时推送消息，至于历史消息是用户上上线的时候自己去Message Service里面pull的。
> - 以前课提到的明星效应问题可以考虑用pull， 我们的大group 也有点类似明星效应问题，但是不用pull，是不是因为消息系统有实时性的要求？
>   - 大 Group 是 500 个人的 Group。这个和明星的 50m 的粉丝不是一个量级的。这里用 push 的原因最主要还是用户行为，人们阅读聊天信息通常都是被动的。而人们阅读 SNS 的信息通常都是主动的。
> - 那么实际实现的时候，是针对大群才用 channel service？
>   - 不是。都会用到 channel，只是走 Public channel 还是 private channel 的区别。比如私信，或者小群，可以走每个人 private channel，这些 private channel 只有用户自己订阅，其他人不会订阅。而大群就放在 Public channel，里面会有好多人。
> - 所以对于未上线用户，channel service最终还是会把历史消息存到数据库里，等待用户上线pull？
>   - 并不是 channel service 把历史消息存到数据库里。消息最开始就先经过 Message Service，先被存储在了数据库里，然后才通过 channel service 去提醒用户查看。通过 channel 和 push server / socket 走的信息都是提醒信息，你可以认为里面的内容是“嘿，你有新消息了，快去服务器取”，而不要把 channel service 当作了消息本身最开始被传递到的地方。
> - 所以channel service 是fan out的，然后push server是点对点的给client推送的？
>   - 没错， channel server 是负责 fanout 的，push server 是点对点完成具体推送的。

### Channel Service QA

> - channel和Thread为什麽不是一一对应的关系？
>   - channel是架构上的逻辑，thread是具体到代码实现层的，不是一个层面的概念
> - Channel service要自己写吗？还是说有什么线程的软件？
>   - 自己寫
> - 系统怎么知道哪些消息已经被poll过，或者是从channel发送的？会不会有重复
>   - client可以通过告诉server自己本地已有的最新一条信息是哪条，或者告诉server自己随后一次同步的时间戳，然后server就直接返回该时间戳之后的消息。另外每个message都是有id的，所以即使client收到了两条一样的消息client也能识别出来是同一条消息。
> - channel name也应该存在其他table里面吧？要不然web service收到一个讯息时怎么知道该送往哪个channel呢？是该加入在user thread table吗？
>   - 不需要有一个单独的 table。web service 收到 channel 信息的时候直接转给 channel service 去 push 即可。很多时候 web service 不是直接从 client 那里得到 channel name。而是直接构造。比如 thread 的channel 可以就叫 `#thread1` `#thread2` 这种。有一个规则可以构造即可。
> - 为什么不对每个thread做channel, personal channel有什么message?对personal channel推送的时候前端怎么知道属于哪个thread?这是一种针对人数少的群的优化么？
>   - 如果对每个 thread 都做一个channel，是可以的。只是不够高效，因为很多用户的 threads 里很多是1对1的聊天，这种做到 channel 里不划算。所以通过一个统一的 personal channel，来推送某个用户1对1或者人数比较少的thread 里的信息提醒。personal channel 推送的时候，可以根据 channel 的名字来解析出属于哪个用户，比如 personal channel 的名字格式可以定义为："personal#1234" 表示是 1234 这个用户的 channel。
> - 所以channel是messaging service 创建的，对用户透明？
>   - channel是由单独的channel service创建的，messaging service将推送群聊消息的任务委托给channel service，然后channel service再自己去把消息push给群里的在线用户。这整个过程对用户是透明的，用户眼中只有"群"的概念，没有channel的概念。
> - 不太明白#personal::user_1的用法。即使是1对1私聊user_1也可以跟user_2,user_3同时进行，这时难道#personal::user_1里有user_2和user_3吗？消息串了怎么办？而且user_2,user_3不也有自己的personal channel吗？
>   - \#personal:user1是user1的私人频道，只有user1一个人订阅，所有发给user1的私信都会在这里推送。比如user2给user1发消息的时候，messaging service收到消息之后会让channel service向#personal:user1推送一条消息｛thread: user1#user2, from: user2, content: xxxx}，此时user1收到消息之后，识别出该消息是来自user2的私信，因此显示在跟user2的聊天框里，消息是不会串的。

> - 老师可不可以简单解释一下“对方正在打字”这个功能是怎么实现的？
>   - 问得好！这个叫做 TypyIndicator，有的公司专门拿来做面试题。实现方式其实很简单，首先 Storage 这个方面其实这个信息是不需要存储的，即便要存储（比如为了做数据分析）也就是存储最后一次 type 的时间就好了。 client A 检测到用户正在输入以后，发一个轻量级的消息给 server， server 通过 push service 发正在输入的信息给 client B，然后 client B 就显示用户正在输入。约定一个检测时间，比如当用户在输入框里输入的时候，大概每隔1-3s 就发送一次这种信息 push（具体取几秒钟看产品经理怎么拍脑袋了）。



活躍時就poll先休息，所以會用推的比較快



## 多機登陸

session中紀錄用戶info



## On-line status

可用push的socket去看是否在線嗎？

實時性要求不高，可以用PULL.　

> - 如果server发现用户在一定时间内没有pull请求，是不是可以标记为offline，然后对他的所有好友也告知此人offline？
>   - 可以，不过一般不是server主动去push通知其好友用户A已经offline，而是好友在自己发出heartbeat pull或者主动请求好友在线信息的时候服务器才告诉该好友用户A已经下线。



# QA

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200410203715392.png" alt="image-20200410203715392" style="zoom:50%;" />



<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200410210741607.png" alt="image-20200410210741607" style="zoom:50%;" />



<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdoz6w1gbxj30i20ye0we.jpg" alt="image-20200410210804359" style="zoom:50%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200411222125219.png" alt="image-20200411222125219" style="zoom:50%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200411222144074.png" alt="image-20200411222144074" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gdq6ydxcquj30ii0mk40f.jpg" alt="image-20200411222215512" style="zoom:50%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200411222247062.png" alt="image-20200411222247062" style="zoom:50%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200411231451591.png" alt="image-20200411231451591" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gdq8ivyb8cj30n20w010o.jpg" alt="image-20200411231633812" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gdq8keeocxj30m20oq794.jpg" alt="image-20200411231800981" style="zoom:50%;" />