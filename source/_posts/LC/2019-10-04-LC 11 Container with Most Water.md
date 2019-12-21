---
layout: post
categories: LC
date: 2019-10-04
tag: [F] 


---



```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        result = 0
        
        while l < r:
            water =  min(height[l], height[r]) * (r - l)
            
            if water > result:
                result = water
        
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return result
            
```

