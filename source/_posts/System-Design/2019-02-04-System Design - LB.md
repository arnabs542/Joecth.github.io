---
layout: post
categories: System
tag: [] 

---

### 

怎麼random選一個server，LB要保證

NGINX 異步



## SNAKE

* Scenario: case/interface
* Necessary: constrain/hypothesis
* Application: service/algo
* Kilobit: data
* Evolve



使用redis 緩存的地方

* 獎品，數量少，更新頻率低，最佳的全量緩存對象
* 優惠券，一次性導入，優惠券編碼緩存為set類型
* 中獎紀錄，讀寫差不多，可以緩存部分統計數據
* 黑名單



## Loading Balancing

### Load Balancer

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd3rkbx8ooj319y0acwkc.jpg" alt="image-20200205225415969" style="zoom:50%;" />

1. Smart Clients

   如果host recover了，就要能夠識別

   系統大了，LB可能是單獨的機器

   等著，占著一個線程，回來才release，上面的那條線是同步的假定，異步的效能會比較好

   * nginx async

     

2. Hardware LB

3. Software LB

   - **HAProxy** 是個比較popular 的software, 加了機器要自己再改配置
   - Service Discovery 改配置文件
   - ![image-20200711200135289](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggnaa27ds3j314e0la474.jpg)
   - 9000會forward到其他的三個機上去

<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gblx1909c6j31c20i2h6v.jpg" alt="image-20200205225556197" style="zoom:50%;" />

​	





### 設計 Serverside Load Balancer 選server

LB 不是個單獨的機器，只是在運行時在代碼裡的一個 client，如下↓

![image-20200711200432006](/Users/joe/Library/Application Support/typora-user-images/image-20200711200432006.png)

<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gblyao5twoj314a0jk7jx.jpg" alt="image-20200205233939163" style="zoom:50%;" />



#### Clien-Side LB 

<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gblyb6gizej314y0lik65.jpg" alt="image-20200205234009523" style="zoom:50%;" />

Load balancing 可以用一致性哈希的機制　key是一樣永遠會去一樣的機器

希望對某一個key去固定的server取緩存

##### Smart Consistent Hash 選 Server 

這個是Sticky

也有上面三點可以根據去選

1. Availability
2. Performance 看誰閒
3. 地理，怎麼判斷route到哪個國家？





#### Spring Cloud - Ribbon Library

來了新的ABC Service，LB會知道，因為有Service Registration，LB會考慮第11個進來

Smart LB, 到底該發給哪個Server? 需要SMART!

<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gblyg6va34j30z20pqgw1.jpg" alt="image-20200205234458185" style="zoom:50%;" />

##### １ AvailabilityFilteringRule 

​		10秒、100, 1000秒再試 exponential

##### ２ WeightedResponseTimeRule 

​		要等愈長，權重給它愈小，我相對應該要發給response快的。

​    **但不知道是DB慢還是API自己慢**，還可講更底層的 TLS(Transpor Layer Security)、握手等機制都是routing的因素，所以smart LB都要考慮



## System Design Primer - GitHub

https://github.com/kevingo/system-design-primer-zh-tw#how-to-approach-a-system-design-interview-question　

而

<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gblyxvhf3ij30sb0ixwfc.jpg" alt="img" style="zoom:48%;" />

![image-20200711201841909](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggnaryy7bhj312o0icqgf.jpg)



![image-20200711202012221](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggnatffvd9j30xo09wae1.jpg)

#### SSL:

 怕 man in the middle 監聽；但 SSL 到門口就可以停下來了，內部自己人不需要用SSL, SSL需要去裝Certification X.509 的認證，需要被 CA給授權，是頒發下來的

#### Session persistent:

 可以根據cookie、一致性哈希去路由到某個固定的機器去維持一個session，每次都發到一個固定的 Worker上，這樣永遠在跟這個Worker打交道，session的數據放在memory，機器會直接記得你放的東西，就是Session Data，

![image-20200711202240110](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggnaw03p78j30ze0c6aga.jpg)



* Sticky session / cookies 指的就是之前提到的 constant hash

* 傳輸層安全性協定（英語：Transport Layer Security，縮寫：TLS）及其前身安全通訊協定（英語：Secure Sockets Layer，縮寫：SSL）是一種安全協定，目的是為網際網路通訊提供安全及資料完整性保障。

* TLS與SSL協定可加密客戶端與伺服器端的網路通訊，它們利用憑證來建立身分鏈，以確保客戶端所通訊的對象是經過驗證的合法伺服器。而進行HTTPS監聽的方法則是在客戶端與伺服器端之間建立一個中間代理人，類似中間人攻擊（man-in-the-middle）的手法，這些可執行HTTPS監聽的安全產品會先攔截流量、檢查流量內容，再重建連結。

* 内部自己用RPC

* Load balancers can be implemented with hardware (expensive) or with software such as HAProxy.

  Additional benefits include:

  - SSL termination

     

    \- Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations

    - Removes the need to install [X.509 certificates](https://en.wikipedia.org/wiki/X.509) on each server

  - **Session persistence** - Issue cookies and route a specific client's requests to same instance if the web apps do not keep track of sessions === 如購物車時



#### Faile Over

* 

  - ### Fail-over

    #### Active-passive failover 有替補的當主要的掛了時馬上補上去

    不停發 心動，如果沒有了，就趕緊找候補代替他

    With active-passive fail-over, heartbeats are sent between the active and the passive server on standby. If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service.

    The length of downtime is determined by whether the passive server is already running in 'hot' standby or whether it needs to start up from 'cold' standby. Only the active server handles traffic.

    Active-passive failover can also be referred to as master-slave failover.

    #### Active-active

    In active-active, both servers are managing traffic, spreading the load between them.

    If the servers are public-facing, the DNS would need to know about the public IPs of both servers. If the servers are internal-facing, application logic would need to know about both servers.

    Active-active failover can also be referred to as master-master failover.




### LB Traffics 

* 

  ### Layer 4 load balancing

  第四層看不了 Session，只有下面粗字的能看

  Layer 4 load balancers look at info at the [transport layer](https://github.com/kevingo/system-design-primer-zh-tw#communication) to decide how to distribute requests. Generally, this involves the **source, destination IP addresses, and ports** in the header, but not the contents of the packet. Layer 4 load balancers forward network packets to and from the upstream server, performing [Network Address Translation (NAT)](https://www.nginx.com/resources/glossary/layer-4-load-balancing/).

  ##### NAT

  - **NAT** - Network Address Translation (NAT) 

    就是 public IP 要 map進去內部的IP

    對外會把ip映射成一個對外的ip

    當在配置一個data center 時，內外ip的mapping

    ![image-20200711203254172](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggnb6o69t6j30ww0a60x6.jpg)

  

  ### Layer 7 load balancing

  能做的事比 L4更多，愈下面愈快，RPC就是快

  Layer 7 load balancers look at the [application layer](https://github.com/kevingo/system-design-primer-zh-tw#communication) to decide how to distribute requests. This can involve contents of the **header, message, and cookies**. Layer 7 load balancers terminates network traffic, reads the message, makes a load-balancing decision, then opens a connection to the selected server. **For example, a layer 7 load balancer can direct video traffic to servers that host videos while directing more sensitive user billing traffic to security-hardened servers.** 
  比較好的網關，對於REST過來的URL, 會根據 URLroute 到不同的服務

  E.g.: 

  	- xxx.com/account/XXXX -> billing/account service
  	- xxx.com/video/YYY -> video_service

  - **spring cloud zuul**裡就有得配置　将path ==> serviceId 

  

  <img src="https://camo.githubusercontent.com/1d761d5688d28ce1fb12a0f1c8191bca96eece4c/687474703a2f2f692e696d6775722e636f6d2f354b656f6351732e6a7067" alt="img"  />

  At the cost of flexibility, ***layer 4 load balancing requires less time and computing resources than Layer 7***, although the performance impact can be minimal on modern commodity hardware.

  ​		愈底下愈快啊　如Application Server用IPC　肯定比http快



### Horizontal scaling	 加機器，而不是加单一台的性能

Load balancers can also help with horizontal scaling, improving performance and availability. Scaling out using commodity machines is more cost efficient and results in higher availability than scaling up a single server on more expensive hardware, called **Vertical Scaling　==>　加CPU、RAM**. It is also easier to hire for talent working on commodity hardware than it is for specialized enterprise systems.

#### Disadvantage(s): horizontal scaling

- Scaling horizontally introduces complexity and involves cloning servers
  - Servers should be **stateless**: they should not contain any user-related data like sessions or profile pictures　**不管去哪台web server機器都應該要是一樣的　不該有session這樣的東西**
  
    ***↑ Server 是Stateless, ↓ Session是Stateful***
  
  - **Sessions** can be stored in a centralized data store such as a [database](https://github.com/kevingo/system-design-primer-zh-tw#database) (SQL, NoSQL) or a persistent [cache](https://github.com/kevingo/system-design-primer-zh-tw#cache) (Redis, Memcached). **Session 就是 Stateful**
- Downstream servers such as caches and databases need to handle more simultaneous connections as upstream servers scale out

​		

### Disadvantage(s): load balancer

- The load balancer can become a performance bottleneck if it does not have enough resources or if it is not configured properly.　掛了就沒

- Introducing a load balancer to help eliminate single points of failure results in increased complexity. 系統複雜了，也是會有問題

  

- A single load balancer is a single point of failure, configuring multiple load balancers further increases complexity.

- ### Source(s) and further reading

  - [NGINX architecture](https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/)
  - [HAProxy architecture guide](http://www.haproxy.org/download/1.2/doc/architecture.txt)
  - [Scalability](http://www.lecloud.net/post/7295452622/scalability-for-dummies-part-1-clones)
  - [Wikipedia](https://en.wikipedia.org/wiki/Load_balancing_(computing))
  - [Layer 4 load balancing](https://www.nginx.com/resources/glossary/layer-4-load-balancing/)
  - [Layer 7 load balancing](https://www.nginx.com/resources/glossary/layer-7-load-balancing/)
  - [ELB listener config](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html)　　這個是亞馬遜自己開發的



##### LB 某種意義上就是 reversed proxy (Web Server)了

![image-20200711204112504](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggnbfav77vj31200nunc2.jpg)

ref : 

https://www.youtube.com/watch?v=RlkA1NRoYJ8&list=PLbhaS_83B97vSWVslD63vjIi5OTYmSVrk&index=80