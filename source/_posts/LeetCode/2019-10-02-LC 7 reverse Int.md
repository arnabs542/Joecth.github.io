---
layout: post
categories: LC
tag: [Michelle] 


---

```python
class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        
        # return the abs value of a number 
        a = abs(x)
        
        while(a != 0):
            # 123
            # a=123
            # num=0
            # First Ite
            # a = 12
            # num = 3
            # Second Ite
            # a = 1
            # num = 32
            # Third Ite
            # a = 0
            # num = 321
            tmp = a % 10
            print('a', a)
            print('tmp', tmp)
            num = num*10 +tmp
            print('num', num)
            a = int(a/10)
        
        if x > 0 and num < 2147483647:
            return num
        elif x < 0 and num <= 2147483647:
            return -num
        else:
            return 0
```

