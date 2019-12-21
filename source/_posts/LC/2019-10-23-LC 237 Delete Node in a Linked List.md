---
categories: LC
tag: [F, TODO, ComeO, Backpack] 
date: 2019-10-23



---



```python

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """ 
        node.val = node.next.val
        node.next = node.next.next
```

