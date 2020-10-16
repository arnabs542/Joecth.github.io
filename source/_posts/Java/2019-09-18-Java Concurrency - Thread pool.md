---
layout: post
categories: Java
tag: [] 
date: 2019-09-16

---



# Java Concurrency 線程池原理剖析



1. 為什麼用線程池？優勢是什麼？
2. 線程池如何使用？
3. 線程池有哪些重要的參數？
4. 線程池底層的工作原理？
5. 線程池工作中用過嗎？生產上如何合理配置參數？



### Q: 什麼是線程池？

![image-20200918200748942](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv27v5cqdj31d00l8129.jpg)



### Q: 為什麼使用線程池？

![image-20200918200827930](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv28klsm1j31j40oye82.jpg)

- 車管所對車作統一管理、上牌，上下班限號限行，如果沒有這套管理任車輛隨便走大家會水洩不通。



### Q: 線程池的優勢

![image-20200918200913889](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv29ae47hj31ia0hwwpt.jpg)

- 我在創建、銷毀線程都是需要時間和資源的。

  希望可以直接把時間花在執行的時間

- 不需要線程的創建時間的等待，可以直接把線程拉出來用了就對

- 方便管控很重要！因為JAVA跑時是要內存，很多個線程加在一起容易OOM溢出，也讓響應速度慢了



### Q: 線程池的核心參數

![image-20200918201224070](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2cl8hcij318c0nc7ez.jpg)

- 7個全都要記！



![image-20200918201305020](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2dar15cj31kk0q2h5v.jpg)

- 線程工廠後面會有例子
- 拒絕策略很特別！

##### JDK源碼

![image-20200918201600363](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2gdt8hzj30u00x6wz7.jpg)



### Q: 線程池的工作流程

![image-20200918201714577](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2hmjki1j31jg0n2dv4.jpg)



![image-20200918201737476](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2i0k4q3j31eq0n4qci.jpg)

- 線程要是飽和，就要使用任務拒絕策略



### Q: 線程池的拒絕策略

![image-20200918201943676](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2k7e7ylj31f60pqala.jpg)

- 要看業務去選擇



### Q: 如何合理设置線程池參數

![image-20200918202058230](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2li0mkvj31gq0d4n2a.jpg)



- 一直不放掉，對系統也不好

##### ★原則★

![image-20200918202136955](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2m6lo65j31iy0nsww5.jpg)

![image-20200918202701617](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2rsxdnzj30xc0tcwpw.jpg)

![image-20200918202826058](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2t9jb54j30wm0to7ga.jpg)



![image-20200918202952663](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2uriudlj31bu0dg106.jpg)

![image-20200918203026969](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2vd08q9j30wg0j8gu5.jpg)

Then OK! 10任務





### 拓展點：Java內置線程池

![image-20200918203229606](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2xhnundj31jw0ownaw.jpg)



##### 不建議用Executor

![image-20200918203250443](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv2xudrzjj31iu0i0tiv.jpg)



### Q: 跟kafka、rabbitMQ差別？

- 不是線程池的工作，這邊是自定義任務

- 我創建線程池

- 下單，建訂單就不能拋了



### Q: 怎知道機器可以開到幾個thread?

- 雲機器可以配置的？會有一輪壓測，不斷把系統用非常大的QPS去壓，對機器作監控去把線程池一點點一點點地調大



### Q: 除了JDK線程池，有什麼第三方線程池實現?

- RPC框架也有自己的線程池

- 阿里的double一定有他的線程池的，他的rabbitMQ也是有線程池的



### Q: Jmeter 性能測試步驟

![image-20200918204152805](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv379irz9j316c0t2ndf.jpg)



### Q: 你心裡的題目呢？

最长回文子串

动规 - 股票

k个一组链表反转!!!

数组中第k大的元素

git项目把公司出现的面试题作汇总

![image-20200918204620820](https://tva1.sinaimg.cn/large/007S8ZIlgy1giv3bwtkg5j316e0syn5e.jpg)

- https://github.com/afatcoder/LeetcodeTop/blob/master/baidu/backend.md



##### 環境

- spring mybatis redis mq mysql 設計模式

  spring mybatis redis mq mysql 設計模式

  spring boot, tomcat

  Java體系相關的中間件，Java的高級特性，spring必須會，spring Cloud springboot tomcat

  每個工作會有他自己技術棧，阿里、美團、拼多多、JD都是java寫的

  go也是跟java比較像

  

  java的問題: 相對實現重，而且基於JVM；阿里

  go: 天生可高併發；開發快，小

  

  - Java EE 原聲的那一套，什麼 JSF，是不是完全不用學了

  - - springcloud rocketMQ sentinel Redis MySQL

  

  - SSH 現在還考的多嗎

  - - 小公司會再問，CRUD、SSM

  - restful vs rpc?

  - - 自己可以先RPC demo級別的，自己實現一個就ok

    - - 重要的是：

      - - rpc線程池
        - serialization
        - 異常處理

    - 去看dubbo ， HSF，spring Cloud吧

