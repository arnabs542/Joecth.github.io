---
layout: post
categories: System
tag: [] 

---

### https://kknews.cc/zh-tw/code/8vljmng.html

https://www.zhihu.com/question/319817091

## Cache

對比**disk** and **memory**, 內存貴，跟disk比，它寫跟讀快很多

#### local disk V.S. memory

能不能把一部份的數據放到memory讓它快?

讀不到才去worker 找，

Cache kv對，很快，repeated Query可這樣做，當一個fn被多次調用，就是要加 Cache

<img src="https://camo.githubusercontent.com/7acedde6aa7853baf2eb4a53f88e2595ebe43756/687474703a2f2f692e696d6775722e636f6d2f51367a32344c612e706e67" alt="img" style="zoom:48%;" />

方法算法被多次叫怎辦？就是說要加Cache。

![image-20200711204719225](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggnblny6qkj312c0g8qch.jpg)

緩存的應用很多。

DB會受益；同個URL來，他不的

本地的缓存就自己本地拿了，不会再去 server端。



#### Cacheing service : Memcache, Redis



<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd3rkssomcj310c0kgaj0.jpg" alt="image-20200206192031055" style="zoom:50%;" />

### Cache aside

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ggrhq7cinxj30zk0ign31.jpg" alt="image-20200715112132396" style="zoom: 50%;" />

照理redis不需要知道業務邏輯，應該都是client控制的，所以redis跟db應該沒分前後

並發時噁心

機率非常低，還可以設上個ttl，讓他自動expire，減小髒的機率，髒指的就是cache、db不同

這個是最常用的

### Cache Aside 也會有的併發的問題，但概率很低，也可以設ttl解

![image-20200206192751483](https://tva1.sinaimg.cn/large/00831rSTgy1gd3rkxfaonj30uc0hk44g.jpg)







## 2.

分布式cache

redis是個緩存服務，如果用redis他有很多模式，最好的就是如果有三台機器，希望每台都分擔些

traffic用一致性哈希　不同key知道要去哪台找，每個node 就是 1/n

雲計算就是堆機器。

##### 缺點：

要是一個機器掛了，有時有個備份。要是一台機器突然沒了，要是用consistent哈希，會重新算每個從 1/5變1/4。cache miss就是去　DB拿。要是突然一台掛了，瞬間會對，一致性哈希有個hash ring。目標就是當一個走了後，盡量讓原來的機器，每個機器要從1/4 --> 1/3　差為1/12。每台要增加這麼多的數據量。讓遷坤大挪移緩和點。

一致性哈希是說讓遷移。讓

distributed hash　就是取模

CDN　content distributed network，也是緩存，更像file system。縣到市市到省

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd3rl19ugwj30ze0k0wp2.jpg" alt="image-20200206194335424" style="zoom:50%;" />

　

### Read/Write Through

使用者寫到cache, cache自己會負責跟db更新，不用你來管，對應用來說簡單多。

嚴格上跟memorycached、redis不一樣，這種cache是知道業務邏輯是知道schema、數據的。

##### Cache　**就是個Service了**

調cache的人就舒服了什麼都不用管，服務本身在做cache

它會同步寫到db，必須DB完成後才能返回給３，會慢一點寫慢一點，讀仍是快

把client做的邏輯給cache做



<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd3rl5r877j30ea0k8go4.jpg" alt="img" style="zoom:67%;" />

![image-20200722112920219](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggzlagwgjvj30yi0e8qai.jpg)

##### Disadvantage(s): write through

- When a new node is created due to failure or scaling, the new node will not cache entries until the entry is updated in the database. **Cache-aside in conjunction with write through can mitigate this issue.**　來個新node要去db找來寫代價大

- Most data written might never be read, which can be minimized with a TTL.　給個死掉的時間

  <img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd3rl9vcz3j30s60k0dty.jpg" alt="image-20200206195432938" style="zoom:50%;" />





### Write-behind　↓　下面

cache不是馬上去更新db，當大量高併發寫時，撐不住，所以先buffer一下個10秒

k:v1, v2, v3，直接就一次v3就好了 

DB可batch更新　時間到或queue到其值

萬一buffer時掛了怎辦？linux RO



![img](https://tva1.sinaimg.cn/large/0082zybpgy1gbn4cmhb4sj30lu0k8aao.jpg)

##### Refresh ahead... ↓

##### 

简单的说就是在缓存数据过期前，能自动的刷新缓存数据。举个例子来说，某条数据在缓存中，过期时间是60秒。我们给他设置一个参数，比如是0.8，60x0.8=48秒，那么在前48秒访问该数据，就照正常的取法，直接返回缓存中的数据。当在48-60秒这个区间取数据时，缓存先将之前缓存的结果返回给外部应用程序，然后异步的再从数据库去更新缓存中的值，以尽可能的保证缓存的值是最新的。如果取数据的的时候超过了60秒，就安装read-through的方式。
 Refresh-ahead是对未来数据的访问情形的估算，我们猜测这个数据在过期后，仍然可能被频繁的访问，那么这种设计的策略获得的优势会更明显。
 但是，如果有大量的数据是用refresh-ahead策略，但是这个数据被重新缓存后，又一次都没有被访问过，那这个策略就是很失算的了。
 那么，有人可能会问，既然如此，我把过期的时间延长不就好了，之前60秒过期，改成6000秒过期，这样就不会用Refresh-ahead策略来刷新数据了。
 然而，事实是缓存的数据越久，出现脏数据的可能性也就越大，更重要的是，如果你的估算也是失误的，大量的超期缓存数据没有被实际访问，那么你就浪费了很多的内存，做了无用的事情，这也是应该避免的。



作者：周小春
链接：https://www.jianshu.com/p/6321d4f823c1
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

