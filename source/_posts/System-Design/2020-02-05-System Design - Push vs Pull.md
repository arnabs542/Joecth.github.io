---
layout: post
categories: System
tag: [] 

---



# Long-Polling vs WebSockets vs Server-Sent Events

## push vs pull

一般經常用到的service architecture 有 queuing, REST, RPC(Remote Procedure Call) 是服務之間怎麼交流

![image-20200206230736407](/Users/joe/Library/Application Support/typora-user-images/image-20200206230736407.png)

S 不一定要知道 C 的 ip, 上網看用戶的就是 C。 

 

![image-20200206231014572](/Users/joe/Library/Application Support/typora-user-images/image-20200206231014572.png)

定點對應服務



基本http請求就是 push請求



### Long-Polling

什麼是HTTP 

- 用戶開connection 並向server請求data
- server 算response
- server送回response



#### Ajax Polling 對應的也是 PUSH

每隔一段時間發一個請求去問好了沒，每0.5秒發一次

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200206231603559.png" alt="image-20200206231603559" style="zoom:50%;" />

老有人來煩server。

中間也有個latency



#### HTTP Long Polling - 對應的也是 PUSH

不是馬上response回來，connection一直hold，等在那邊直到好了被通知再發一個真正的請求過去

之前的請求只是要知道「什麼時候好」

有個timeout　



### WebSockets - PULL

#### Full-duplex

bidirectional



![image-20200725122407012](/Users/joe/Library/Application Support/typora-user-images/image-20200725122407012.png)



**C、S兩邊都可以發請求，同時的**。half-duplex 是只有一邊發。

小負擔、幾乎實時、S不需要C的請求，也可以發過去。

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gbn4dopv4ij30w40ggag2.jpg" alt="image-20200206232250565" style="zoom:50%;" />

Server可以PUSH, 發請求，即時拿到。

一般C對S發的Socket是收到response後就關掉了

是「不斷的」所以S可以找到C。

#### SSE

用的是長連結

![image-20200206232544827](https://tva1.sinaimg.cn/large/0082zybpgy1gbn4dvvbxfj310e0fqgu4.jpg)

S 可以即時PUSH!