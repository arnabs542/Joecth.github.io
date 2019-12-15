---
layout: post
categories: LC
tag: [Michell, TODO, F] 



---



```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 兩種判斷條件：
        # DP
        # CABAC
        # B
        # ABA
        # CABAC
        result = ''
        for i in range(len(s)):
            p1 = self.getlongestpalindrome(s, i, i)
            if len(p1) > len(result):
                result = p1
            
            p2 = self.getlongestpalindrome(s, i, i+1)
            if len(p2) > len(result):
                result = p2
            
        return result
    
    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return s[l+1 : r]
```

