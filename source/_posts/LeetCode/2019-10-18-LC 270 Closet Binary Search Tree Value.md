---
layout: post
categories: LC
tag: [F] 



---



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return 0
        
        que = deque([root])
        min_g = float('inf')
        res = que[0].val
        
        while que:
            v = que.popleft()
            if abs(v.val - target) < min_g:
                min_g = abs(v.val - target)
                res = v.val
            if v.left:
                que.append(v.left)
            if v.right:
                que.append(v.right)
        return res
```

