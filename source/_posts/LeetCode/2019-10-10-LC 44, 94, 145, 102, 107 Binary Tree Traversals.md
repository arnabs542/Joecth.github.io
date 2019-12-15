---

layout: post

categories: LC

tag: [Tree] 

---

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        l = []
        l.append(root.val)
        l += self.preorderTraversal(root.left)
        l += self.preorderTraversal(root.right)
        
        return l
      
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        
        l = self.inorderTraversal(root.left)
        l += [root.val]
        l += self.inorderTraversal(root.right)
        
        return l
      
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        l = self.postorderTraversal(root.left)
        l += self.postorderTraversal(root.right)
        l += [root.val]
        
        return l
```





```python

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        res = []
        while que:
            level_len = len(que)
            level_l = []
            for i in range(level_len):
                v = que.popleft()
                # print(v.val)
                level_l = level_l + [v.val]   # level_l
                if v.left:
                    que.append(v.left)
                if v.right:
                    que.append(v.right)
                
            res += [level_l]
            
        return res
        
```



```python
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        que = deque([root])
        while que:
            level_l = []
            for i in range(len(que)):
                v = que.popleft()
                level_l += [v.val]
                
                if v.left:
                    que.append(v.left)
                    
                if v.right:
                    que.append(v.right)
        
            res += [level_l]
        
        return res[::-1]
```

