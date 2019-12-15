---
layout: post
categories: LC
tag: [TODO, F] 



---



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        Q = collections.deque([(root,None)])
        d = {}
        while Q:
            iters = len(Q)
            rec = []
            for i in range(iters):
                a,b = Q.popleft()
                rec.append(a)
                if a.left: Q.append((a.left,a))
                if a.right: Q.append((a.right,a))
                # 建立对应关系
                d[a] = b
        # rec records the last level node
        s = set(rec)
        res = []
        while len(s) != 1:
            s = set()
            for node in rec:
                s.add(d[node])
            res += rec
            rec = list(s)
        return list(s)[0]
```

