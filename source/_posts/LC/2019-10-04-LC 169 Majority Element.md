---
layout: post
categories: LC
date: 2019-10-04
tag: [Michell, F] 


---



```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(nums)):
            curr = d.get(nums[i], 0)
            if curr == len(nums)//2:
                return nums[i]
            d[nums[i]] = curr + 1
            
```

