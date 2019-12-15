---
layout: post
categories: Probability
tag: [] 



---

### Baysian

$$
P(A|C) = \frac{P(A\cap C)}{P(C)},  
P(C|A) = \frac{P(A\cap C)}{P(A)}   \\
Thus, P(A|C) = \frac{P(C|A) * P(A)}{P(C)}
$$



### Independent

$$
P(A|C) = \frac{P(A\cap C)}{P(C)}=\frac{P(A)*P(C)}{P(C)}=P(A) \\  
P(C|A) = \frac{P(A\cap C)}{P(A)}=\frac{P(A)*P(C)}{P(A)}=P(C)   \\
%Thus, P(A|C) = \frac{P(C|A) * P(A)}{P(C)}
$$

![v2-d331a465a66032ebc14b6f24feae2457_b](https://tva1.sinaimg.cn/large/006tNbRwly1g9s1bgefz3j30hs0ffabh.jpg)



- posterior probability
- priori probability



------

**为什么朴素贝叶斯如此“朴素”？**

因为它假定所有的特征在数据集中的作用是同样重要和独立的。正如我们所知，这个假设在现实世界中是很不真实的，因此，说朴素贝叶斯真的很“朴素”。