---
layout: post
categories: System
tag: [] 
date: 2020-03-15
---



# 秒殺

- 0點開始
- 限量100台
- 一人限購一台
- 如：搶紅包、搶火車票、搶手機

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200824202003669.png" alt="image-20200824202003669" style="zoom: 50%;" />



### QPS分析

- 平日每秒1000人訪問這頁面。秒殺時每秒數十萬人訪問該頁面，QPS增加100倍以上。

## Scenario

### 商品購買和下單流程

![image-20200824202207414](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi26516fedj30xi0g6gp6.jpg)

- 付完錢才是完成，如果沒有按時付錢，庫存是會被放開的



### 需要解決的問題們

#### 瞬間大流量高併發

server、db能承載的QPS有限，如db一般是單機 1000 QPS，需要根據業務預估併發量

#### 有限庫存，不能超賣

庫存是有限的，需要精準地保證，就是賣掉了N個商品。不能超賣，當然也不能少賣

#### 黃牛惡意請求

使用腳本模擬用戶購買，模擬出10幾萬個請求去搶購

#### 固定時間開啟

時間到了才能購買，提前一秒都不可以 (以商家的時間為準)

#### 嚴格限購

一個商家只能買固定數量個



### 需求拆解

![image-20200824202903828](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi26c7mxc1j30sq0ck40q.jpg)



## Service

### 服務結構設計

#### 單體

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gi26fynt3uj30zo0gk11x.jpg" alt="image-20200824203239695" style="zoom:67%;" />



#### 微服務

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gi26i5p40mj30zs0e211l.jpg" alt="image-20200824203446425" style="zoom:67%;" />



## Storage

### 寫

![image-20200824203827977](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi26m08ptzj30y00e8wil.jpg)

#### Q: 如何添加索引?

- 商品表: 沒有關聯其他表，所以就主鍵就ok了

- 秒殺表: 綁定了商品，所以 commodity_id 可以作索引查起來快
- 庫存表: 綁了商品、以及活動 id，要保證同一個商品跟活動 id 要綁定作唯一鍵
- 訂單表: 商品、活動以及用戶可以綁一起作唯一鍵

#### 數據流

![image-20200824204607333](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi26tz811sj31460fa77r.jpg)

- 紅框那個很重要，因為最重要的就是去搶庫存，所以那個要更新
- 一般不作外鍵，慢
- 建立索引有原則的



#### Q: 解決超賣: 秒殺操作 - 扣減庫存

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gi26z4b2plj30ja0eaq7l.jpg" alt="image-20200824205104211" style="zoom: 33%;" />



##### 解法一(X) : 事務, FOR UPDATE, 但效率低

就是說我要去更新它，所以告訴SQL鎖住

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gi270rmakwj30p00fgn23.jpg" alt="image-20200824205239608" style="zoom: 33%;" />



##### 解法二(V): 用 UPDATE 語句自帶的行鎖

這個是透過MySQL本身的機制來保證的

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200824205433454.png" alt="image-20200824205433454" style="zoom:33%;" />

#### Q: 大量請求都訪問 MySQL, 導致 MySQL 崩潰。

- 對於搶購活動來說，可能幾十萬人搶100台iphone, 實際大部分請求都是無效的，不需要下沉到MySQL

##### 解法一: 庫存預熱 by Redis

- 秒殺的本質，就是對庫存的搶奪。

- 每個秒殺的用戶來都去DFB校驗庫存，然後扣減庫存，會導致DB崩潰

- MySQL DB單點能支撐 1000 QPS, 但 Redis 單點能支撐 10萬 QPS，可以考慮將庫存信息加載到 Redis中。

- **直接通過 Redis 來判斷並扣減庫存。**

  ##### Redis:

  - kv pair, 也可持久化
  - 支持
    - string
    - hash
    - list
    - set
    - zset
  - 單線程的數據庫，沒有併發的問題。通過IO多路復用實現併發，大家進來就是一個個排隊
  - 主持主備容災 (Disaster Tolerance) 存儲，主掛了，小弟會趕緊頂上去
  - 所有單個指令操作都是原子的，要麼完全ok或失敗。
  - 多個指令可以通過 Lua 腳本實現原子性
  - 因為所有操作都在 內存中，所以性能極高，單機一般可以到10萬數量級
  - 可作為Cache、DB、MQ

- 提前放到Redis預熱，它來判斷庫存

#### Q: 何時預熱? 

- 活動前呀!

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200824210846277.png" alt="image-20200824210846277" style="zoom:50%;" />

- **開始通過redis 減庫存**

現在直接去讀redis庫存，如果庫存小於0就結束；一個redis是單線程的，不會有併發的問題。創了訂單才會去DB扣庫存；

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gi27khniyyj312k0feaia.jpg" alt="image-20200824211136832" style="zoom:50%;" />

#### Q: 使用Redis 的問題 -- 仍有超賣問題，超賣在redis也要解決

##### 方案一 -- 仍有放行的問題:

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200824211410268.png" alt="image-20200824211410268" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gi27o0eo75j311c0ek42p.jpg" alt="image-20200824211500506" style="zoom:50%;" />



##### 方案二: 通過 Lua 腳本執行原子操作，redis 2.6版後

就是把剛剛redis的 GET 跟 DECR 合而為一了，在一個事務裡去操作

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200824211654764.png" alt="image-20200824211654764" style="zoom:50%;" />

現在redis對於DB就只放給它100而已，性能也夠了。但現在會有的問題是：



#### Q: 如果秒殺量是1萬台、10萬台呢？==> MySQL仍撐不了

可通過MQ去削峰，讓量慢慢地放過去

- 點了商品，他會讓我等一、兩秒，讓redis(一秒十萬個)慢慢去找MySQL(集群，所以也是可以一秒一萬個)

  <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200824212243509.png" alt="image-20200824212243509" style="zoom:50%;" />



##### MQ

- 如去星巴克取餐這類，步調不一致的問題解決
- 解耦和async的操作
- mq一般是帶有重試能力

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200824212727568.png" alt="image-20200824212727568" style="zoom: 33%;" />

##### q: 如果極端之下MQ出現部份投遞失敗怎辦？

RabbitMQ, Kafka, RocketMQ

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gi283k35tvj314o0g8tdo.jpg" alt="image-20200824212957025" style="zoom: 50%;" />

- 沒長度限制的
- redis是集群的；剛剛講的10萬是單機的
- 失敗可能是網路原因

### 讀