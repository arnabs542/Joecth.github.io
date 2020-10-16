---
layout: post
categories: SystemDesign
tag: []
date: 2019-04-15


---







存 : sharidng、写、failure

查:

# BigTiger

★ 應該先關注「寫」再來才是「讀」

### 讀

- 如何在文件作快速查詢？

  - 對於文件很多數據找到key排序

  - 也是 NoSQL常用的概念

    <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200804230436057.png" alt="image-20200804230436057" style="zoom:50%;" />

- 大表時怎辦？

  - 拆成很多個小表，這樣每個小表內部是個排過序的kv串，在底下用元數據保存小表位置

    ![image-20200804230659530](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghfubji1asj315g0kc761.jpg)

- 超大表呢？

  - 小表再拆出小小表

    ![image-20200804230812457](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghfubobrjkj316s0nywh0.jpg)



### 寫

DB只是負責查詢跟組織的，存是存到FS裡去的。

- 怎麼寫數據？
  - ![image-20200804231646400](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghfubmnyhdj316g0imwfz.jpg)



- 內存表過大怎辦？

  - 要是內存寫到64MB就打入DISK

    <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200804231815438.png" alt="image-20200804231815438" style="zoom:50%;" />



- 如何避免丟失數據

  - Log

    <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200804231938213.png" alt="image-20200804231938213" style="zoom:50%;" />



- 所以現在下面三者構成了一個「小表的數據」
  1. 內存表
  2. 一些小小表
  3. Log



- 如何讀數據？
  - 比方要找B了，因為小小表內有序，內存外無序，所以找的時候要找所有的小小表還有內存表，而且disk還要遍歷或二叉找都是很慢的
  - ![image-20200804232415145](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghfubnip3yj313i0mwdi9.jpg)



- 怎加速呢？
  - 最好的方式就是建立索引
  - 我們在寫入小小表時，可以固化個索引並預加載到內存
  - ![image-20200804233037481](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghfubj6z2sj315g0kc761.jpg)



- 继续加速?
  - 用 Bloom Filter, 有可能在的塊才去找
  - 所以小小表就變成了數據塊、索引、Bloom Filter



- 如何將表存入 GFS?
  - 兩者都是64MB的chunk，可映射上，好管理
  - <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200804233433530.png" alt="image-20200804233433530" style="zoom:50%;" />



- 表的邏輯視圖是什麼？
  - 身高體重可以變column family
  - ![image-20200804233540415](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghfubl4n0ij316m0nyq5x.jpg)



- 怎麼映射為物理存儲？

  - 找到key的規則，將行、列、時間戳作為key

  - 都存一起有什麼好處呢？

    - 可以將相同的key聚合在一起，是NoSQL的經典更有效的作法，所以天然不支援join操作，

      也說明了為什麼MySQL在scale天然會出各種問題

    ![image-20200804233835009](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghfubizt4wj316i0g0abv.jpg)



- 架構是什麼呢？

![image-20200804234021399](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghfubk1hk9j31440mkwh9.jpg)



- <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghf8mst00qj30v003smze.jpg" alt="image-20200805002026433" style="zoom: 33%;" />

