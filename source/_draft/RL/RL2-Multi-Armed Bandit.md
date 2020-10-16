```
layout: post
categories: RL
tag: [] 
date: 2020-10-13
```



# Explore-Exploit Dilemma

- Epsilon-greedy: used all thru RL!
- Optimistic Initial Values
- UCB1 (Upper Confidence Bound)
- Thompson Sampling (Bayesian Bandit)



## Epsilon-greedy

- Short-sighted

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201014121332169.png" alt="image-20201014121332169" style="zoom:50%;" />

#### Exploration

- so we can collect data about each bandit!
  - want our estimates of their  **win rate** to be accurate
  - if epsilon == 0.1, means 90% of time we use exploitation, 10% of time we explore new bandit.

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjoqsnfw7zj310o042abs.jpg" alt="image-20201014121935941" style="zoom: 33%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201014121959167.png" alt="image-20201014121959167" style="zoom: 33%;" />

