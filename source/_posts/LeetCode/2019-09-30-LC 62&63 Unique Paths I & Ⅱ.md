---
layout: post
categories: LC
tag: LC-DP
---
1 state variables

2 init

| 1    | 1     | 1     | 1    |
| ---- | ----- | ----- | ---- |
| 1    | ２    | ３ｍ↓ |      |
| 1    | ３ｎ→ | ６n+m |      |
| 1    |       |       |      |

3 equation
$$
[i][j] = [i-1][j] + [i][j-1]
$$
4 result

### LC 62.

```python
def f(x, y):
  dp = [[0]*(x+1) for _ in range(y+1)] ## take out of board into consideration as 0
  dp[1][1] = 1
  for i in range(1, y+1):
    for j in range(1, x+1):
      dp[i][j] = dp[i-1][j] + dp[i][j-1]
  return dp[y][x]
```



### LC 63.　w/ Obstructions

之前走的２Ｄ地圖是有障礙物的

#### Diff: at Initialization

| 1    | 1    | 0    | 0    |
| ---- | ---- | ---- | ---- |
| 1    |      |      |      |
| 0    |      | 0/1  |      |
| 0    |      |      |      |

```python
def f(x, y):
  dp = [[0]*(x+1) for _ in range(y+1)] ## take out of board into consideration as 0
  dp[1][1] = 1
  for i in range(1, y+1):
    for j in range(1, x+1):
      if obstacle[i][j] != 1:　### MAIN diff!
      	dp[i][j] = dp[i-1][j] + dp[i][j-1]
  return dp[y][x]
```



Ref:

![image-20190930221007253](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hwe6l5e7j30hc0em78r.jpg)





### DP vs 計劃遞歸(Memorization)

Memorization omits loop of varaibles.

Ref:

![image-20190930214729348](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hvqn3ekxj30w40fadn0.jpg)

![image-20190930214602150](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hvp6agvkj30x20fo464.jpg)

![image-20190930214630627](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hvplk9kmj30uq0cq78y.jpg)