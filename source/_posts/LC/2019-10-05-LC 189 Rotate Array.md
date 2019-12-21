---
layout: post
categories: LC
date: 2019-10-05
tag: [Michell, TODO, F] 



---



```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
        
            
            
```

20