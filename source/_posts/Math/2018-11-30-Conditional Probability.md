---
layout: post
categories: Probability
tag: [] 



---

Ref: https://zhuanlan.zhihu.com/p/35976057

## 事件的独立性

根据定义，两个事件*A*和*B*是*独立的，*如果：



![img](https://pic4.zhimg.com/80/v2-024ebd7be22be3792d0eb85ee51e8453_hd.jpg)



使用条件概率，我们可以提供一个稍微不同的定义。以来：



![img](https://pic1.zhimg.com/80/v2-92899762e2fa58123284becb28237144_hd.jpg)



并且*P（A∩B）* = *P（A）P（B）*：



![img](https://pic3.zhimg.com/80/v2-3ed71d1794cce026ac70140049e6813e_hd.jpg)





只要*P（B）* > 0，对于独立的*A*和*B*，我们有*P（A | B）* = *P（A）* ; 换言之，*B* 不会以任何方式影响*A*的概率。同样，我们可以证明对于*P（A）* > 0，我们有*P（B | A）* = *P（B）*。

独立也延伸到事件的补充。回想一下，*P（B ^ C）* 是*B*没有发生的概率，或1 - *P（B）* ; 由于条件概率服从通常的概率公理，我们有*P（B ^ C | A）* = 1 - *P（B | A）*。那么，如果*A*和*B*是独立的：



![img](https://pic4.zhimg.com/80/v2-b1171212d1b5d818d21fb9dda0a70a53_hd.jpg)