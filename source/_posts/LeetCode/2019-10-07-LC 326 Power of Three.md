---
layout: post
categories: LC
tag: [Michelle] 



---



```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 2:
            return False
        
        tmp = n
        while tmp > 3:
            if tmp % 3 == 0:
                tmp /= 3
            else:
                return False
        
        if tmp == 3:
            return True
        return False
            
```

