---
layout: post
categories: LC
date: 2019-10-05
tag: [Michell, TODO, F] 



---



```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # fast = slow = ListNode(0)
        fast = slow = head
        stack = []
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
            
        while slow:
            top = stack.pop()
            
            if top != slow.val:
                return False
            slow = slow.next
            
        return True
```

O(n)

O(n/2)



★　Sol w/ 2 Stacks

```python
def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        
        if head.next == None:
            return True
        
        stack = []
        
        sHead = head
        
        while sHead != None:
            stack.append(sHead.val)
            sHead = sHead.next
        
        while head != None:
            if head.val != stack.pop():
                return False
            head = head.next
        
        return True
```



```python
def isPalindrome(self, head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True

```

O(n)

O(1)