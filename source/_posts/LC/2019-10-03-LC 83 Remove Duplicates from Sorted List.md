---

layout: post
date: 2019-10-03
categories: LC
tag: [Michelle] 

---



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        # val = head.val
        while curr:
            val = curr.val
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        
        return head
                
```

