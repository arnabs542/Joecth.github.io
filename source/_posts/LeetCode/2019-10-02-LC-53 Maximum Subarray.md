---
layout: post
categories: LC
tag: [F] 

---



```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        tmp_sum = nums[0]
        for i in range(1, len(nums)):
            tmp_sum = max(tmp_sum + nums[i], nums[i])
            if tmp_sum > max_sum:
                max_sum = tmp_sum
        return max_sum
```



![image-20191002154920066](https://tva1.sinaimg.cn/large/006y8mN6ly1g7jwmw170hj30qy0em40z.jpg)