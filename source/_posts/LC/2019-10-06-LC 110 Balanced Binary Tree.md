---
layout: post
categories: LC
date: 2019-10-06
tag: [Michell, TODO, F] 



---



```python
class Solution_iterative_postorder:
    def isBalanced(self, root):
        stack = [(0, root)]
        depth = {None: 0}
        while stack:
            seen, node = stack.pop()
            if node is None:
                continue
            if not seen:
                stack.extend([(1, node), (0, node.right), (0, node.left)])
            else:
                if abs(depth[node.left] - depth[node.right]) > 1:
                    return False
                depth[node] = max(depth[node.left], depth[node.right]) + 1
        return True


class Solution_recursive_without_extra_variable:
    def isBalanced(self, root):
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return dfs(root) != -1


class Solution_recursive_with_switch_variable:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.switch = True

        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                self.switch = False
            return max(left, right) + 1

        dfs(root)
        return self.switch
```

