---
layout: post
categories: SystemDesign
tag: []
date: 2020-02-05
---



# 找月球上第k大的數據

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gi80ysv6phj312w07kagl.jpg" alt="image-20200829215631253" style="zoom:67%;" />



一台台扁長的機器

一萬就是說這機器上有很多數字，別揪結，就是大

有n台機器，怎麼找全部起來第

壓縮扯遠了

Kth biggest number

我人在地球，這批機器是在月球，主要是說傳輸我到機器的距離很長，帶寬對我是個很大的問題，一般最終的問題就是在帶寬。sql去查，上億條就是map reduce之類的優化，找到了index，還是有上億個，至少上MB了，要一下返回，整個數據中心的網路都堵啦，網路傳不過去，太多啦。

![image-20200829220410378](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi816q553hj311q0hyq6x.jpg)

眼、嘴、手都用上。在扯XD。

### 解一: n台機器就是N*k => 然後再找出第k大

![image-20200829220736573](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi81aawsh8j31280i479b.jpg)

最大的問題是：假如k是一萬呢？100台機器，不然返回了100萬個數？我要等半天！

我在地球耶。



### 解法二：

![image-20200829221211451](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi81f2xwgyj313a0i4wlr.jpg)

1. 我把每台的第k個數返回，我用到的就是n
2. 我拿到每個機器的第k大的，我要找min數

重點是要減少round trip





# 排序超大数



![image-20200829221654279](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi81jz5d2cj312g0m2wu1.jpg)



## radix sort，要都是等長的，如都是三位

runtime是 n*k，k表digit數，bucket sort也是一樣幾乎 線性，比快排快

