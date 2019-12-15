---
layout: post
categories: LC
tag: LC-DP
---
### 198. house robber

```python
# -*- coding: utf-8 -*-
class Solution:
    def rob(self, nums):
        nums = list(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:   # duplicated with lineno.19, but OK, clear to understand
            return max(nums[0], nums[1])

        dp = [0 for i in range(len(nums))]
        for idx, num in enumerate(nums):
            if idx == 0:
                dp[0] = nums[0]
            elif idx == 1:
                dp[1] = max(nums[0], nums[1])
            else:
                dp[idx] = max(dp[idx - 2] + nums[idx], dp[idx - 1])

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    ex1_in = [1, 2, 3, 1]
    ex2_in = [2, 7, 9, 3, 1]

    ans = sol.rob(ex1_in)
    print("ans1: {}".format(ans))
    assert (4 == ans)

    ans = sol.rob(ex2_in)
    print("ans2: {}".format(ans))
    assert (12 == ans)
```

