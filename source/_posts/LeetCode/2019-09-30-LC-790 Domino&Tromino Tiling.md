---
layout: post
categories: LC
tag: [LC-DP, TODO] 
---

Problem: 2x1 XX

```python
def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 1:
            return 0
        N += 1
        module = pow(10, 9)+7   
        dp = [[0, 0]*N for _ in range(N)]
        dp[0][0], dp[1][0], dp[1][1] = 1, 1, 2
        for i in range(2, N):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-2][1]
            dp[i][1] = dp[i-1][0]*2 + dp[i-1][1]
        return dp[N-1][0] % module
```

Ref:

![image-20191001181252686](https://tva1.sinaimg.cn/large/006y8mN6ly1g7iv5nfkjdj31hl0u01ds.jpg)

![image-20191001183553311](https://tva1.sinaimg.cn/large/006y8mN6ly1g7ivtlhge4j31580katgw.jpg)

Ref: https://www.jianshu.com/p/2104df9de5d5