---
layout: post
categories: LC
tag: [Michelle] 


---


```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1

        for k in d.keys():
            if d[k] == 1:
                return k
```
