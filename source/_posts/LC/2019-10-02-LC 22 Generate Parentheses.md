---
layout: post
categories: LC
date: 2019-10-02
tag: [Michelle, TODO] 


---

![image-20191002214108136](https://tva1.sinaimg.cn/large/006y8mN6ly1g7k6swbmqrj30li0e4q4e.jpg)

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        
        result = []
        self.helper(n, n, '', result)
        
        return result
    
    def helper(self, l, r, item, result):
        # (()))( not OK
        if r < l: #remaining r should > l
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l-1, r, item+'(', result)
        if r > 0:
            self.helper(l, r-1, item+')', result)
```

