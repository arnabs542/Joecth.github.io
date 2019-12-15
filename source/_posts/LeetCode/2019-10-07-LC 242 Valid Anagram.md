---
layout: post
categories: LC
tag: [Michelle] 



---



```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1

        d2 = {}
        for i in range(len(t)):
            if t[i] in d:
                d[t[i]] -= 1
                if d[t[i]] == 0:
                    del d[t[i]]                    
            else:
                d2[t[i]] = i
        print(d, d2)
        return not d2 and not d
```

