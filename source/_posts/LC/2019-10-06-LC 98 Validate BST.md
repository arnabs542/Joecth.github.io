---
layout: post
categories: LC
date: 2019-10-06
tag: [Michelle, TODO] 



---



```python
class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    def isValidBST(self, root, lo=float('-inf'), hi=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if not lo < root.val < hi:
            return False
        
        return self.isValidBST(root.left, lo, min(root.val, hi)) and \
               self.isValidBST(root.right, max(lo, root.val), hi)
```

