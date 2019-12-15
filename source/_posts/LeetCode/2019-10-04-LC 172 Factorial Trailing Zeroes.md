---
layout: post
categories: LC
tag: [Michell] 



---





```python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0 
        tmp = n
        while tmp:
            result += tmp // 5
            tmp = tmp // 5
        
        return result
#         tmp = 1
#         for i in range(n):
#             tmp *= (i+1)
#             print(tmp)
            
#         digit = 0
#         count = 0
#         while not digit:
#             digit = tmp % 10
#             if not digit:
#                 tmp = tmp // 10
#                 count += 1
#         return count         < == Output Limit Exceeded...
```

