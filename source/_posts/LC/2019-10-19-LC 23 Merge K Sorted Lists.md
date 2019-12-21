---
layout: post
categories: LC
date: 2019-10-19
tag: [F, D&C, PriorityQueue] 


---



```python
class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q, h = len(lists), []
        for i in range(q):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i, lists[i]))
        
        rhead = rtail = ListNode(0)
        
        while h:
            i, n = heapq.heappop(h)[1:]
            rtail.next = n
            rtail = rtail.next
            if n.next:
                heapq.heappush(h, (n.next.val, i, n.next))
                
        return rhead.next
```



```python
def mergeKLists(self, lists):
    if not lists:
        return 
    if len(lists) == 1:
        return lists[0]
    mid = len(lists)//2
    l = self.mergeKLists(lists[:mid])
    r = self.mergeKLists(lists[mid:])
    return self.merge(l, r)

def merge(self, l, r):
    dummy = cur = ListNode(0)
    while l and r:
        if l.val < r.val:
            cur.next = l
            l = l.next
        else:
            cur.next = r
            r = r.next
        cur = cur.next
    cur.next = l or r
    return dummy.next
```

