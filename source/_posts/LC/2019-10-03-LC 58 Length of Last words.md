---
layout: post
categories: LC
date: 2019-10-03
tag: [Michelle] 



---



```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        local_count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                local_count = 0
            else:
                local_count += 1
                count = local_count # to prevent 'Hello ' case
        return count
```

