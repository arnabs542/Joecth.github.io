---
layout: post
categories: SystemDesign
tag: []
date: 2020-03-03
---



The coaching habit

# Design G-Sheet

![image-20200819111802026](https://tva1.sinaimg.cn/large/007S8ZIlly1ghvybcu4prj313u0ja7c4.jpg)

<img src="https://tva1.sinaimg.cn/large/007S8ZIlly1ghvy9lckzhj30em0eugo8.jpg" alt="image-20200819111621876" style="zoom:50%;" />



## DataStucture

### How to store the content of a sheet?

- Array
- LinkedList

<img src="https://tva1.sinaimg.cn/large/007S8ZIlly1ghvydeljqpj30wo0eite8.jpg" alt="image-20200819112000244" style="zoom:80%;" />

- B花的空間大一些
- B的複雜度要討論 = =……
- **update 一定是主要操作!!**，insert 慢，怎弄都ok，都會「ref」

<img src="https://tva1.sinaimg.cn/large/007S8ZIlly1ghvyfqu5g6j30z80lgwld.jpg" alt="image-20200819112216095" style="zoom:67%;" />



![image-20200819112431102](https://tva1.sinaimg.cn/large/007S8ZIlly1ghvyi3504rj314k0eygrr.jpg)



## Algorithm

#### Question: 循環依賴

- \#REF!

怎麼找：

- Topo
- 快慢指針
- UF



### How many memory does one cell need?

- 8k?!

### What's the max number of cells?

- 2000000個? 為何？
  - 



![image-20200819113348574](https://tva1.sinaimg.cn/large/007S8ZIlly1ghvyrs2tymj30o00f8dj3.jpg)





![image-20200815232403114](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghrwtppkl4j30tu0to7ai.jpg)





## Conflic

Acquire Mutex

![image-20200815232555601](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghrwvw0octj316s0r4ak6.jpg)





![image-20200819005225841](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghvg8idhebj312s0j27ai.jpg)



## Computer Network

### Latency VS Consistency



![image-20200819102208942](https://tva1.sinaimg.cn/large/007S8ZIlly1ghvwp7sod5j312s0icn21.jpg)



![image-20200819102329411](https://tva1.sinaimg.cn/large/007S8ZIlly1ghvwqli121j312k0k0aeu.jpg)

- 實現複雜，因為要預測
- 時間戳



## Software Engineering

### How to design the System?

![image-20200819102620406](https://tva1.sinaimg.cn/large/007S8ZIlly1ghvwtkkiijj313m0lyadq.jpg)



## Design Thinking

### How to avoid conflicts?

- 不同人看到不同顏色，從產品出發



## Summary

![image-20200819102758903](https://tva1.sinaimg.cn/large/007S8ZIlly1ghvwv9lrauj314e0i80yx.jpg)