---
categories: LC
tag: [F, TODO, ComeO] 
date: 2019-10-22



---



```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr +=1
                # p0 ~ curr 的 elems 得要是唯一的
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
                # curr += 1    # for case [1,2,0] ==> [1, 0, 2]
            print(nums)
            
```

