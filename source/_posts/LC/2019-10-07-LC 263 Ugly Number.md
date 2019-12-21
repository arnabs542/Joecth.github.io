---
layout: post
categories: LC
date: 2019-10-07
tag: [Michelle, TODO] 



---



```python
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
        return num == 1
```

