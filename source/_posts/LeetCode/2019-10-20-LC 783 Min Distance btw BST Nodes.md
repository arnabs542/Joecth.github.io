---
layout: post
categories: LC
tag: [F, LC] 


---



```python
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root is None:
            return
        
        self.minDiffInBST(root.left)
		# evaluate and set the current node as the node previously evaluated
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
		
        self.minDiffInBST(root.right)
        return self.res
```



```python
class Solution(object):
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res
```





```python
class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diff = float('inf') # Largest possible difference
        last_visited_node = None # Track the last visited node in the sorted sequence to calculate difference in between adjacent elements. 
        stack = [] # For Iterative in-order traversal
        node = root
        while stack or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if last_visited_node and node.val - last_visited_node.val < diff:
                    diff = node.val - last_visited_node.val  
                last_visited_node = node
                node = node.right
        return diff
```

