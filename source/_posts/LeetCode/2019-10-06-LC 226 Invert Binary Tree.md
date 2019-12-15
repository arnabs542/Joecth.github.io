---
layout: post
categories: LC
tag: [Michelle, TODO, Tree] 


---

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

