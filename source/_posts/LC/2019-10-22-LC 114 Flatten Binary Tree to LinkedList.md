---
categories: LC
tag: [F, Tree] 
date: 2019-10-22



---



```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        pre = None
        stack = [root]
        while stack:
            r = stack.pop()
            if pre:
                pre.left = None
                pre.right = r
            pre = r
            if r.right:
                stack.append(r.right)
            if r.left:
                stack.append(r.left)
```





```python
def __init__(self):
    self.prev = None
    
def flatten(self, root):
    if not root:
        return None
    self.flatten(root.right)
    self.flatten(root.left)
    
    root.right = self.prev
    root.left = None
    self.prev = root
```

