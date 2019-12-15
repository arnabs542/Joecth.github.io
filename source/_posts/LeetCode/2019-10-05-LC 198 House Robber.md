---
layout: post
categories: LC
tag: [Michell] 


---

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [i for i in range(len(nums))]
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp[-1]
```

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        #if not nums:
        #    return 0
        
        #if len(nums) == 1:
        #    return nums[0]
        #elif len(nums) == 2:
        #    return max(nums[0], nums[1])
        
        # dp = [i for i in range(len(nums))]
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        dp0 = 0
        dp1 = 0
        for i in range(0, len(nums)):
            dp0, dp1 = dp1, max(dp1, dp0 + nums[i])
        return dp1
```

