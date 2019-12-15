---
categories: LC
tag: [F, Tree] 


---



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
```





```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         if inorder and postorder:
#             ind = inorder.index(postorder.pop())

#             node = TreeNode(inorder[ind])
#             node.left = self.buildTree(inorder[:ind], postorder)
#             node.right = self.buildTree(inorder[ind+1:], postorder)
#             return node
        
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)

        return root
```

