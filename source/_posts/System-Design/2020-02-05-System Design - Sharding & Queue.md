---
layout: post
categories: System
tag: [] 

---

### 

# 分片

partition  or  sharding

每個機器分一部分就是要切小塊，LB就是在做pardition　sharding更指db的存儲

日本放在日本的db，因為有 sharding　所以要routing去找數據

<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gbmy6i9wcvj30hu0k8781.jpg" alt="img" style="zoom:50%;" />

sharding　一般來說指的是db　

partition不一定是固定的，也可能增加了機器，每個就管得比較少了

照地理位置去找

![image-20200206202240123](https://tva1.sinaimg.cn/large/0082zybpgy1gbn4cs9n1vj30yg0lcdit.jpg)



<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gbmy90zsmlj30tw0k0dnz.jpg" alt="image-20200206202333357" style="zoom:50%;" />

![image-20200206202407013](/Users/joe/Library/Application Support/typora-user-images/image-20200206202407013.png)

<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gbmya9oquoj30ym0jck1l.jpg" alt="image-20200206202443059" style="zoom:50%;" />



### Partition Method

by ID, by letter, by Term

Horizontal partitioning : as by ID　風險：range分得不好，所以不平衡，怎麼evenly distributed?!

Vertical Partitioning : 按業務去分　如下圖↓

<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gbmyk67nx2j30kw0mwjyj.jpg" alt="image-20200206203421886" style="zoom:50%;" /> 

業務調整、或是中間加一層就更複雜了



## Partitioning Criteria

1. key or hash-based partitioning 
   userid每次加１的id，對100取個mod去知道哪個機器，工業中一般不用　這個是distributed hashing，用consistent hashing比較好↓
2. list partitionging 自己聲明rule 就像mongodb，自己定義
3. round-robin
4. composite

## Consistent Hashing

把所有可能的hash值分成圓五份 

這樣可能不均勻

所以就有個vnnode的概念 一個機器對應五個 vnnode

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200206204214506.png" alt="image-20200206204214506" style="zoom:50%;" />

可能一個對應256個vnnode

#### 備份↓

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200206204351704.png" alt="image-20200206204351704" style="zoom:50%;" />

如果４～５區段掛了，全給A承擔太不公平；如果有vnnode　一台機器掛了，後面的每個機器都可以均勻分擔這個量

distributed hash是大挪移要全重算…　所以一致性哈希好



## Common problems of Sharding

因為數據不是在一處，所以要去多個地方去取。

1. Join and Denormalization 去user table 去查 name ；
   讀還ok寫就麻煩了
2. Referential integrity 
3. Rebalancing 重弄分片；有某個zip數據量特大。



## LinkedIn Prob.

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200206205226121.png" alt="image-20200206205226121" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gbmz3ewua8j30x40jqn9w.jpg" alt="image-20200206205246002" style="zoom:50%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200206205350491.png" alt="image-20200206205350491" style="zoom:50%;" />



##### Expression Tree

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200206205535354.png" alt="image-20200206205535354" style="zoom:50%;" />



# Queue

#### message queue　

不會丟，可以保證不會丟失

往ｑ放東西，consumer拿東西，本身是個異步過程。 Hot-spot, burst，Q就是個buffer，

系統可以不用等在那邊，可防止 burst

- An application publishes a job to the queue, then notifies the user of job status
- A worker picks up the job from the queue, processes it, then signals the job is complete

可以buffer住一堆來的請求，讓producer不用等在那邊
consumer一直去polling　就是異步

這情況同步會降低效能 

要確定放成功了 要拿個 task_id 之後再一直去要

**[Redis](https://redis.io/)** is useful as a simple message broker but messages can be lost.

**[RabbitMQ](https://www.rabbitmq.com/)** is popular but requires you to adapt to the 'AMQP' protocol and manage your own nodes.

**[Amazon SQS](https://aws.amazon.com/sqs/)** is hosted but can have high latency and has the possibility of messages being delivered twice.

上面三個比較有名的 message queue的框架

 server取完後再去把task刪了，至少這個task還是在queue裡的 

##### 可以取出來在db or que寫 in progress，==> high availability　不丟消息

可以retry



![image-20200206211146919](/Users/joe/Library/Application Support/typora-user-images/image-20200206211146919.png)



##### Async 缺點：當計算快時比較建議用同步就好，因為que會有delay跟complexity