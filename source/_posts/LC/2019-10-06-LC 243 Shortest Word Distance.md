---
layout: post
categories: LC
date: 2019-10-06
tag: [Michelle, TODO] 




---



```python
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        l1 = -1
        l2 = -1
        curr_dist = len(words)
        
        for i, word in enumerate(words):
            if word == word1:
                l1 = i
            elif word == word2:
                l2 = i
            
            if l1 >=0 and l2 >=0:
                curr_dist = min(curr_dist, abs(l2-l1))

        return curr_dist
```

