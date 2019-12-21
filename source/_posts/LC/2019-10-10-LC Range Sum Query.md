---
layout: post
categories: LC
date: 2019-10-10
tag: [Michelle, TODO] 




---



```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.accu = []
        tmp = 0
        # print(nums)
        for i in range(len(nums)):
            tmp = tmp + nums[i]
            self.accu += [tmp]
            # print(self.accu)

    def sumRange(self, i: int, j: int) -> int:
        return self.accu[j] - self.accu[i-1] if i else self.accu[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```

