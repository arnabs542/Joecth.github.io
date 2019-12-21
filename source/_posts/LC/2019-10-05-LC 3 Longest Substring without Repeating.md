---
layout: post
categories: LC
date: 2019-10-05
tag: [Michell, TODO, F] 



---



```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        start = 0
        dt = {}
        for i,c in enumerate(s):
            if c in dt:
                start = max(start,dt[c]+1)
            maxlen = max(maxlen,i-start+1)   
            dt[c] = i
        return maxlen 
```

