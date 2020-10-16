---
layout: post
categories: Study Notes
tag: [] 
date: 2020-10-07

---





# Conclusion 

1. prev: A/B , now A/B/n and MVT
2. know 
   - VWO
   - Google Optimize
   - Bandit
     
3. Discussion:
   - MVTAB should be just the same as Multi-Armed Bandit, they're the same!  ?
   - How about the 3 algorithms mentionsed in Multi-Armed Bandit?
   - Contextual Bandit is goal! --> Customization for diff users



#### TODO:

1. Understanding **algorithmes** for Multi-Armed Bandit
2. Experiment on **Google Optimize** for A/B Testing





## Terms:

### MVT & A/B(/n) Testings

- CRO - Conversion Rate Optimization
- VWO - [VWO | #1 A/B Testing Tool in the World](https://vwo.com/)
- Experiements on ***Google Optimize***

- **Web Optimization**

  

### Bandit

- super arm --  collection of **base arm**s
  - return profit of this porfolio, comprise of gain fr each base arm
- base arm -- arm in single-armed bandit
- [**Contextual Bandit**](https://www.optimizely.com/optimization-glossary/multi-armed-bandit/)
  - Rely on incoming user context data as it can be used to help make better algorithmic decisions in real time
  - Sounds like "Recommendation"
  - No Loser ?! 
- [CTR](https://www.optimizely.com/optimization-glossary/click-through-rate/)



# Multivariate Testing (MVT)  vs A/B & A/B/n Testing (Split URL Testing)



|             | A/B                                                          | Multivariate                                                 |      |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| Methodology | ● BINARY split the traffic  <br />● Cmp 2 versions of a page using live traffic split<br />● Bucket site visitors -- videos, buttons, sign-up?!<br />● To know which page is more effective | ● FACTORIAL split, since mult elements<br />● Cmp higher num of vars<br />● Reveal more info abt "How these vars interact w/ on another"<br />● Traffic also split<br />● To measure the effectiveness each design comb has on the ultimate goal<br />● To find 1st design, To find impact of each elements |      |
| Common uses | ● Eval a page design, ONE element for debate<br />● The num of click on each version of <br />"***the call to action can be compared***"<br />*● Even though many design elements are changed in this kind of A/B test, <br />ONLY the impact of the design as a whole on each page's business goal is tracked, <br />NOT individual elements.* <br />-- 皮鞋不是搭什麼都好看!<br />● A/B/C/D Test, e.g cartoon mouse vs. coils of a boa constrictor on newsletter | ● Eval a page design, MANY element for debate<br />● The num of click on each version of <br />"***the call to action can be compared***"<br />*● Even though many design elements are changed in this kind of A/B test, <br />ONLY the impact of the design as a whole on each page's business goal is tracked, <br />NOT individual elements.* <br />-- 皮鞋不是搭什麼都好看!<br />● A/B/C/D Test, e.g cartoon mouse vs. coils of a boa constrictor on newsletter |      |
| Best Used   |                                                              |                                                              |      |
| Pros        | ● Speedy                                                     |                                                              |      |
| Limitations | ● Best for 2~4 elements<br />● NOT reveal interaction between vars on a SINGLE page | ● Amount of traffic needed ∵ Complex, Factorial<br />● 25 combinations at most, even high traffic site<br />● IMPORTANT to eval cycle of testing & redesign ∴ well-designed A/B can help sometimes |      |

- A/B Testing
  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjgstds8naj30b60fnweq.jpg" alt="Tracks clicks on CTA" style="zoom: 67%;" />

- A/B/n Teting
  A/B/C/D Test!
  Numerous versions of the page at the same time and split the traffic evenly.

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjgw5p2qi3j30dw08mgn1.jpg" alt="ab-test" style="zoom:67%;" />

  ref: https://mixpanel.com/topics/ab-tests-vs-multivariate-tests/

- Multivariate Testing
  <img src="https://images.ctfassets.net/zw48pl1isxmc/5CWHZOz8JO6oi4iK0YSiWc/ca12d4922be3e79a74e8f3267af62e6d/mvt_browser-table.png" alt="Browser" style="zoom: 67%;" />



![mvt-testing-3](https://tva1.sinaimg.cn/large/007S8ZIlgy1gjgw8vala3j308p06raa6.jpg)

​		ref: https://www.softwaretestinghelp.com/multivariate-testing-and-ab-testing/



### Experiment analysis

https://www.softwaretestinghelp.com/multivariate-testing-and-ab-testing/



# Multi-Armed Bandit

- Same acronym to Multivariate A/B Test

- Contextual Bandit should be "Customization"



### Algorithms

- Epsilon-Greedy
- **UCB Theory (Upper Confidence Bound)** --> already close to optimization profit
  - Combination explosion Online learning not 
  - CUCB算法将组合优化和在线学习无缝对接实现了前面图示中的反馈回路
- Thompson Sampling (Bayesian)
- Reinforcement Learning



### Related Resources

- [组合在线学习：实时反馈玩转组合优化](https://mp.weixin.qq.com/s?__biz=MzAwMTA3MzM4Nw==&mid=2649441835&idx=1&sn=abf10e00dd2354a0f256620b9e1fcda9&chksm=82c0afafb5b726b9a4cdb4d9112deba1bfe72803b20fd5f10bd7dd00b798214fbce750d4503f#rd) by MS Institute, 2017
- Combinatorial Multi-Armed Bandit: GeneralFramework, Results and Application



#### Study Links:

https://cloud.tencent.com/developer/article/1400274