---
layout: post
categories: LC
date: 2019-10-13
tag: [F] 




---



```python
from collections import defaultdict
class Solution:

    def __init__(self, nums: List[int]):
        self.num = nums
        self.d = defaultdict(list)
        for i in range(len(nums)):
            self.d[nums[i]].append(i)
        print(self.d)
        
    def pick(self, target: int) -> int:
        return random.choice(self.d[target])
```

