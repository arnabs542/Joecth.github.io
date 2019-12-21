---
layout: post
categories: LC
date: 2019-10-03
tag: [Michelle, TODO] 


---

```python
    def countAndSay(self, n: int) -> str:
        seq = '1'
        i = 0
        while i < n-1:
            seq = self.getNextseq(seq)
            i += 1
        return seq
    
    def getNextseq(self, seq):
        curr = 0
        result = ''
        for i in range(len(seq)):
            count = 1
            while i < len(seq)-1 and seq[i] == seq[i+1]:
                count += 1
                curr += 1
            result += str(count) + str(seq[i])
            curr += 1
        return result
```

