---

layout: post
date: 2019-10-03
categories: LC
tag: [Michelle, Tree] 

---


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result, current = [], [root]
        
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            current = next_level
            result.append(vals)
            
        return result[::-1]
```

