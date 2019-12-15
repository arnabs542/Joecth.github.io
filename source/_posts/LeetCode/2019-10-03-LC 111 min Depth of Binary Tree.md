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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) +1
```



![image-20191003173726293](https://tva1.sinaimg.cn/large/006y8mN6ly1g7l5dp3uy6j30u00v5tcj.jpg)