---
layout: post
categories: LC
tag: [F] 

---



```python

class Solution:
    def isValid(self, s: str) -> bool:
        if not str:
            return True
        stack = []
        lookup = {'(':')', '{':'}', '[':']'}
        for c in s: # c: (,  s: ()[]{}
            if c in lookup:
                stack.append(c)
            else:
                if not stack :  # len(stack) == 0, for "]" case
                    return False
                if c != lookup[stack.pop()]:
                    return False
        # return True  
        return len(stack) == 0
```

