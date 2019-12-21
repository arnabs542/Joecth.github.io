---
layout: post
categories: LC
date: 2019-10-05
tag: [Michell, F] 



---



```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        has_same = 0
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
                continue
            
            diff = abs(i-d[nums[i]])
            if diff <= k:
                return True
            else:
                d[nums[i]] = i
```

![image-20191005140238973](https://tva1.sinaimg.cn/large/006y8mN6ly1g7naev35arj30ju0boabh.jpg)