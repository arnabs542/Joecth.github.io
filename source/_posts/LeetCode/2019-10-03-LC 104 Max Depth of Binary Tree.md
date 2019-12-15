---

layout: post
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
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth, curr = 0, [root]
        while curr:
            children = []
            depth += 1
            for node in curr:
                # print(node)
                if node and node.left:
                    children.append(node.left)
                if node and node.right:
                    children.append(node.right)
                    
            curr = children
            
        return depth
```

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

