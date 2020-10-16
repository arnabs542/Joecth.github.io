---
layout: post
categories: System
tag: [] 
date: 2020-02-05
---



# TinyURL

- [0-9, a-z, A-Z] 一共62個，62^6 ~= 56.8 Billions unique Strings 應是夠用的
- 要考慮到其他國家的string 這邊當然主要只是英文字母
- Similar: bit.ly, goo.gl 
- 簡答的通常是這個系統的一個功能



![image-20200801212636104](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbmqzsggoj30q00fqq51.jpg)

## Read Heavy



## Constraints

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbmt7b338j30pa0batf5.jpg" alt="image-20200801212843299" style="zoom: 50%;" />



## REST APIs

### 長做短

#### Goo

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbmuaiyitj30q60e2wjr.jpg" alt="image-20200801212946459" style="zoom:50%;" />

- 201 - created
- content-typ是告訴你body是什麼
- 怎麼去客製化url?
  - body可以加個參數像是defaul none
- Response e.g.

![image-20200801213136358](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbmw80drzj30l20oodq6.jpg)





#### Bitly

![image-20200801213226710](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbmx33xswj30um0f0agv.jpg)

![image-20200801213255365](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbmxkp980j30xk0c0teo.jpg)





### 短回長

![image-20200801213345334](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbmyfkjlpj30lu07odis.jpg)

- 3XX redirection
- **301 moved Permanently**

![image-20200801213408593](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbmyvowbyj30z60rm18f.jpg)

- Header 裡會有個key 就是location知道要redirect到哪裡
- 我收到301跟它的loc後，會再發一個網址去我要去的地方

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbn1qu2i5j30am04ogm8.jpg" alt="image-20200801213656344" style="zoom:33%;" />







<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbmzm8bsfj30jw0ciwin.jpg" alt="image-20200801213452950" style="zoom: 33%;" />



## Service

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbn05k9ynj30i407k0vl.jpg" alt="image-20200801213523160" style="zoom: 50%;" />



## Storage

![image-20200801213946574](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbn4qhmtyj30t00f0wpp.jpg)





<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbpxnpwgzj30hs0amaca.jpg" alt="image-20200801231648267" style="zoom:50%;" />

- 2 跟3要綁事務了

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200801225936514.png" alt="image-20200801225936514" style="zoom: 33%;" />

![image-20200801230337236](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbpjz88wfj30yq0lyn1c.jpg)

ref: https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR

- 黃色那塊是就是lazy cleanup

![image-20200801231309317](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbptwfkwdj30s00hk46g.jpg)

![image-20200801231319438](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghbpu1y125j30ws0kg129.jpg)

