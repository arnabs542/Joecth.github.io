---
layout: post
categories: System
tag: [] 

---



SQL - ORM, basics

# NoSQL 

Not Only SQL

本身有幾個派別如kv, document

#### 4種型式的存儲方式

1. kv
2. document store
3. wide column store
4. graph database

#### Normalize -- JOIN　在SQL ORM用的，往往一個機器

RDBMS避免冗餘



#### Denormalize -- 大量重複要寫到多份，寫就麻煩，但讀有利　 

多餘的重複寫到多個tables去，就是避免join, 

在nosql 裡大量用的 ，nosql往往為了多機器作分布

數據中心要同步數據怎麼辦？跨data-center Denormalize就兩邊都寫

寫時要保證***各國的數據中心都寫進去了***，

要知道是 read-heavy or write-heavy 大多是讀的多，

如youtube讀的人遠大於寫的人

##### 缺點：不利於寫、冗缺、如果系統write-heavy就很不利，如logging system、message que 

什麼系統是寫多的? logging系統如卡夫卡



- 要做join的話是在**applicatin layer也是middle layer?!**的　＝＝＞　<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200206221633536.png" alt="image-20200206221633536" style="zoom: 25%;" />

- 不支持ACID - *ACID* (*atomicity, consistency, isolation, durability*) is a set of properties of database transactions intended to guarantee validity ，那麼多機器不能保證事務

- nosql不好鎖，多個當然不好鎖，慢慢才最終一致, 跨機器不容易鎖呀，所以是eventually consistency

  - 例如：linkedin發了文章，不是需要馬上好友都看到，可以有latency的，我的follower之後才收到沒差

  叫作 ***eventually consistency***，可能就不是毫秒級的，是秒級的，也不會到慢到一分鐘之類

  - #### 為何是Eventually Consistency?

    - #### Quorum - 就是假如有三個人，2:1，少數服從多數，儘管第三台還沒寫到，它在第二台被寫後，也會要因為大家投票變了，要服從是變第2版

      ![image-20200715100536958](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggrfjal4ukj30ym0hw0xh.jpg)

# ACID in SQL - (*atomicity, consistency, isolation, durability*)

一台機器時，SQL就可保證事務，銀行Transaction 銀行的經典例子 - 

一個事務裡：原子性。

銀行在意事務，所以ORM比較好。如果在一個地方取，中間

帳號是個變量a, 本來有1000元，一邊要存5000元，另個人從我的帳戶也取1000元。如果沒有事務保護

數據就亂了

DBMS裡在　為保證transation可靠，所以要有ACID,事務中只能有一個會成功

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200206222645993.png" alt="image-20200206222645993" style="zoom:50%;" />



# NoSQL Cont.

- **CAP Theorem**

- 在[理論計算機科學](https://zh.wikipedia.org/wiki/理論計算機科學)中，**CAP定理**（CAP theorem），又被稱作**布魯爾定理**（Brewer's theorem），它指出對於一個[分布式計算系統](https://zh.wikipedia.org/wiki/分布式计算)來說，不可能同時滿足以下三點：[[1\]](https://zh.wikipedia.org/wiki/CAP定理#cite_note-Lynch-1)[[2\]](https://zh.wikipedia.org/wiki/CAP定理#cite_note-2)

  - 一致性（**C**onsistency） （等同於所有節點訪問同一份最新的數據副本）
  - [可用性](https://zh.wikipedia.org/wiki/可用性)（**A**vailability）（每次請求都能獲取到非錯的響應——但是不保證獲取的數據為最新數據）
  - [分區容錯性](https://zh.wikipedia.org/w/index.php?title=网络分区&action=edit&redlink=1)（**P**artition tolerance）（以實際效果而言，分區相當於對通信的時限要求。系統如果不能在時限內達成數據一致性，就意味著發生了分區的情況，必須就當前操作在C和A之間做出選擇[[3\]](https://zh.wikipedia.org/wiki/CAP定理#cite_note-3)。）

  根據定理，分布式系統只能滿足三項中的兩項而不可能滿足全部三項[[4\]](https://zh.wikipedia.org/wiki/CAP定理#cite_note-4)。理解CAP理論的最簡單方式是想像兩個節點分處分區兩側。允許至少一個節點更新狀態會導致數據不一致，即喪失了C性質。如果為了保證數據一致性，將分區一側的節點設置為不可用，那麼又喪失了A性質。除非兩個節點可以互相通信，才能既保證C又保證A，這又會導致喪失P性質。

  **BASE** is often used to describe the properties of NoSQL databases. In comparison with the [CAP Theorem](https://github.com/donnemartin/system-design-primer#cap-theorem), BASE chooses availability over consistency.

  - **Basically available** - the system guarantees availability.
  - **Soft state** - the state of the system may change over time, even without input.
  - **Eventual consistency** - the system will become consistent over a period of time, given that the system doesn't receive input during that period.



#### SQL 

ORM object relational mapping, mysql oracle都是可以被java裡搞定起來

DDL 時就是schema都是差不多的　－　Data Definition Language，DDL

#### NoSQL就有分流派了 主要就是四大流派

Key-Value資料庫、記憶體資料庫、圖學資料庫和文件資料庫.

#### Source(s) and further reading: key-value store

- [Key-value database](https://en.wikipedia.org/wiki/Key-value_database)

  如cassandra

- [Disadvantages of key-value stores](http://stackoverflow.com/questions/4056093/what-are-the-disadvantages-of-using-a-key-value-table-over-nullable-columns-or)

- [Redis architecture](http://qnimate.com/overview-of-redis-architecture/)　比較是緩存服務

- [Memcached architecture](https://www.adayinthelifeof.nl/2011/02/06/memcache-internals/)　比較是緩存服務



#### Document Store - MongoDB

##### 最重要的就是Schemaless -- 就是沒有schema, 

#### Document store，

##### Schemaless

如JSON就是kv, 就是schemaless

> Abstraction: key-value store with documents stored as values

A document store is centered around documents (XML, JSON, binary, etc), where a document stores all information for a given object. Document stores provide APIs or a query language to query based on the internal structure of the document itself. *Note, many key-value stores include features for working with a value's metadata, blurring the lines between these two storage types.*

Based on the underlying impleme

##### Source(s) and further reading: document store

- [Document-oriented database](https://en.wikipedia.org/wiki/Document-oriented_database)
- [MongoDB architecture](https://www.mongodb.com/mongodb-architecture)
- [CouchDB architecture](https://blog.couchdb.org/2016/08/01/couchdb-2-0-architecture/)
- [Elasticsearch architecture](https://www.elastic.co/blog/found-elasticsearch-from-the-bottom-up)

#### Wide column store

[![img](https://tva1.sinaimg.cn/large/0082zybpgy1gbn4cnj0ioj30g506f0t2.jpg)](https://tva1.sinaimg.cn/large/0082zybpgy1gbn4cnj0ioj30g506f0t2.jpg)
***[Source: SQL & NoSQL, a brief history](http://blog.grio.com/2015/11/sql-nosql-a-brief-history.html)***

> Abstraction: nested map `ColumnFamily>`

**Google introduced [Bigtable](http://www.read.seas.harvard.edu/~kohler/class/cs239-w08/chang06bigtable.pdf)** as the first wide column store, which influenced the open-source **[HBase](https://www.mapr.com/blog/in-depth-look-hbase-architecture) (by Hadoop)** often-used in the Hadoop ecosystem, and [Cassandra](http://docs.datastax.com/en/cassandra/3.0/cassandra/architecture/archIntro.html) from Facebook. Stores such as BigTable, HBase, and Cassandra maintain keys in lexicographic order, allowing efficient retrieval of selective key ranges.



#### Graph DB -- for social Network

##### Graph database

[![img](https://tva1.sinaimg.cn/large/0082zybpgy1gbn4cpicsqj30h40c4gps.jpg)](https://tva1.sinaimg.cn/large/0082zybpgy1gbn4cpicsqj30h40c4gps.jpg)
*[Source: Graph database](https://en.wikipedia.org/wiki/File:GraphDatabase_PropertyGraph.png)*

> Abstraction: graph

In a graph database, each node is a record and each arc is a relationship between two nodes. Graph databases are optimized to represent complex relationships with many foreign keys or many-to-many relationships.

Graphs databases offer high performance for data models with complex relationships, such as a social network. They are relatively new and are not yet widely-used; it might be more difficult to find development tools and resources. Many graphs can only be accessed with [REST APIs](https://github.com/donnemartin/system-design-primer#representational-state-transfer-rest).

##### Source(s) and further reading: graph

- [Graph database](https://en.wikipedia.org/wiki/Graph_database)
- **[Neo4j](https://neo4j.com/)**
- [FlockDB](https://blog.twitter.com/2010/introducing-flockdb)



## SQL vs NoSQL 何時用?

如mysql vs cassandra (mongoDB) 之間的區別之類的？

Reasons for **SQL**:

- Structured data
- Strict schema
- **Relational data**
- Need for complex **joins** 如用戶跟group
- Transactions　事務
- Clear patterns for scaling
- More established: developers, community, code, tools, etc
- Lookups by ***index*** are very fast

Reasons for **NoSQL**:

- Semi-structured data　　
- ***Dynamic or flexible schema***
- Non-relational data
- No need for complex joins
- ***Store many TB (or PB) of data***　
- ***Very data intensive workload*** 
- Very high throughput for IOPS (Input/Output Operations Per Second

Sample data well-suited for NoSQL:

- Rapid ingest of clickstream and ***log data*** **之前說的頻繁寫的!!**
- Leaderboard or scoring data ***就 eventually consistency 就好的***
- Temporary data, such as a shopping cart  有cache就可以搞定
- Frequently accessed ('hot') tables
- Metadata/lookup tables

##### Source(s) and further reading: SQL or NoSQL

- [Scaling up to your first 10 million users](https://www.youtube.com/watch?v=w95murBkYmU)
- [SQL vs NoSQL differences](https://www.sitepoint.com/sql-vs-nosql-differences/)



![image-20200206225707917](/Users/joe/Library/Application Support/typora-user-images/image-20200206225707917.png)

####  

![image-20200206225824207](/Users/joe/Library/Application Support/typora-user-images/image-20200206225824207.png)

![image-20200206225934479](https://tva1.sinaimg.cn/large/0082zybpgy1gbn4crkjxdj311005wdge.jpg)

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200206230007842.png" alt="image-20200206230007842" style="zoom:50%;" />

量不大時　SQL 就夠了；如ACID、data不會變的或結構的

量大時才會用 NoSQL 學校一般用不到那麼大流量啊 量大時一般沒結構，的確NoSQL也是比較靈活

雲上一般要多個機器，硬體也都比較便宜



<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd5cj2dgicj30u00wv1g9.jpg" alt="image-20200324213805414" style="zoom: 33%;" />