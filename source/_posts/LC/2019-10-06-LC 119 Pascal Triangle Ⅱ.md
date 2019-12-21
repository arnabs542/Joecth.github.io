---
layout: post
categories: LC
date: 2019-10-06
tag: [Michelle] 




---



```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for i in range(0, rowIndex):
            prev = res[-1]
            tmp = list(map(lambda x, y: x+y, prev+[0], [0]+prev))
            res.append(tmp)
        return res[-1]
```

