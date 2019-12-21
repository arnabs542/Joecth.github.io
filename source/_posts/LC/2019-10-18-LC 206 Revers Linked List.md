---
layout: post
categories: LC
date: 2019-10-18
tag: [Linked-List] 



---



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        curr = head
        pre = None
        while curr:
            tmp = curr.next 
            curr.next = pre
            pre = curr
            curr = tmp
            
        return pre
```

