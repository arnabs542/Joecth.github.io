---
layout: post
categories: LC
date: 2019-10-03
tag: [Michelle] 


---


```python
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        while head and head.val == val:
            head = head.next
        
        curr = head
        
        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next    
        return head
```
