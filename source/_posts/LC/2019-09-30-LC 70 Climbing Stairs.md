---
layout: post
categories: LC
date: 2019-09-30
tag: LC-DP
---
```python
def f(n):
	dp = [-1 for i in range(n+1)]
	for i in range(2, n+1):
		dp[i] = dp[i-1] + dp[i-2]
	return dp[n]
```

O(n) , O(n)



```python
def f(n):
  dp1, dp2 = 1, 1
  for i in range(2, n+1):
    dp2, dp1 = dp1 + dp2, dp2
   return dp2
```

O(n) , O(1)

