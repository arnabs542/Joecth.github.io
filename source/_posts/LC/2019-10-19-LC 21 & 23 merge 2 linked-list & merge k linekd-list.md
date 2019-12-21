---
layout: post
categories: LC
date: 2019-10-19
tag: [TODO, F, Linked-List] 


---



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        # dummy1.next = l1
        # dummy2 = ListNode(0)
        # dummy2.next = l2
        prev = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        prev.next = l1 if l1 else l2
        return dummy.next
```



```python
class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        nums, dum = [], ListNode(0)
        p = dum
        for l in lists:
            while l:
                nums.append(l)
                l = l.next
        for i in sorted(nums, key = lambda l: l.val):
            p.next = i
            p = p.next
        return dum.next
```

