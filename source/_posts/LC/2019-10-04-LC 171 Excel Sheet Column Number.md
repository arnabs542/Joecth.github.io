---
layout: post
categories: LC
date: 2019-10-04
tag: [Michell] 



---



```python
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        
        for i in range(len(s)):
            result *= 26
            result += ord(s[i]) - ord('A') + 1
            
        return result
```

