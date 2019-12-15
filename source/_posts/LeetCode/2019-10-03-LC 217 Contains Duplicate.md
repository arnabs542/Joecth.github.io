---
layout: post
categories: LC
tag: [Michelle] 


---


```python
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
            if d[nums[i]] > 1:
                return True
        return False
```
