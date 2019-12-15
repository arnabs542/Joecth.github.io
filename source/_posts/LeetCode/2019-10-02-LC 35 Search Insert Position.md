---
layout: post
categories: LC
tag: [Michelle, ToFindBetter] 

---

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
            elif i == len(nums) - 1:
                return len(nums)
            
```



![image-20191002232913393](https://tva1.sinaimg.cn/large/006y8mN6ly1g7k9xddqxsj30pu0dctah.jpg)