---
layout: post
categories: LC
date: 2019-10-19
tag: [TODO, F] 



---



```python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        c = 1
        for i in range(1, len(nums)):
            c = c + 1 if nums[i] > nums[i-1] else 1
            res = max(res, c)
        return res
```

