---
layout: post
categories: LC
date: 2019-10-02
tag: [Michelle] 


---



```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        a = abs(x)
        
        while(a != 0):
            tmp = a % 10
            num = num * 10 + tmp
            a = a // 10
            # print(a)
        if x >= 0 and x == num:
            return True
        else:
            return False
            
```

