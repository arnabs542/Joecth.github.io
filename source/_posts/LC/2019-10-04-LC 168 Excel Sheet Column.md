---
layout: post
categories: LC
date: 2019-10-04
tag: [Michell, TODO] 


---



```python
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        N = 26
        tmp = n
        result = ''
        while tmp:
            digit = (tmp-1) % N
            carry = (tmp-1) // N
            tmp = carry
            print(digit)
            result = chr(digit + ord('A')) + result 
        # print(result)
        return result
```

