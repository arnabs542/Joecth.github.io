---
layout: post
categories: LC
date: 2019-10-01
tag: [F] 


---



```python
def removeDuplicates(self, nums: List[int]) -> int:
    curr = 0
    for idx in range(len(nums)):
        # if nums[curr] == nums[idx]:
            # curr += 1
        # else:
        if nums[curr] != nums[idx]:
            curr += 1
            nums[curr] = nums[idx]
            
    nums = nums[:curr+1]
    return len(nums)
```


​                

![image-20191002003507533](https://tva1.sinaimg.cn/large/006y8mN6ly1g7j67ec3ozj30qe0meq60.jpg)