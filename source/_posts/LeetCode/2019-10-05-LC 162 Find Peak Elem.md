---
layout: post
categories: LC
tag: [Michell, TODO, F] 



---



```python
    def findPeakElement(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    # def findPeakElement(self, N: List[int]) -> int:
        N = nums
        L, _ = len(N), N.append(-math.inf)
        for i in range(L):
            if N[i] > N[i+1]: return i
```

