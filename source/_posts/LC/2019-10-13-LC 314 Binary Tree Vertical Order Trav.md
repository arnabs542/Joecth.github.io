---
layout: post
categories: LC
date: 2019-10-13
tag: [Michelle, TODO, F, Tree] 



---



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        cols = defaultdict(list)
        que = deque([(root, 0)])
        while que:
            node, col = que.popleft()
            cols[col].append(node.val)
            if node.left:
                que.append((node.left, col-1))
            if node.right:
                que.append((node.right, col+1))
        return [cols[i] for i in sorted(cols)]
```

