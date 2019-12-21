---
layout: post
categories: LC
date: 2019-10-17
tag: [TODO, F, DP] 


---


```python
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
				dp = {}
        for i in xrange(len(A)):
            for j in xrange(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
```

```python
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        # [3,6,9,12,13]
        # when i=1, A[i]=6:
        # dp=[{3:2}]
        # when i=2, A[i]=9:
        # dp=[{3:2}, {6:2, 3:3}]
        # when i=2, A[i]=12:
        # dp=[{3:2}, {6:2, 3:3}, {9:2, 6:2, 3:4}, {10:2, 7:2, 4:2, 1:2}]
        # return max([2,3,4,2])
    
        dp = [dict()]
        for i in range(1, len(A)):
            dp.append({})
            for j in range(i):
                dp[i][A[i] - A[j]] = dp[j].get(A[i] - A[j], 1) + 1
        # print(dp)
        # print(max([max(i.values()) for i in dp if i.values()]))
        ret = max([max(i.values()) for i in dp if i.values()])
        return ret
```
