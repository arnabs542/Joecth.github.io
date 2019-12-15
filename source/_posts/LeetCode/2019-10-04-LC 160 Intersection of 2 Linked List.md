---
layout: post
categories: LC
tag: [F, Linked-List] 


---

```python
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
            
        return p1
```





#### Approach 1: Brute Force

For each node ai in list A, traverse the entire list B and check if any node in list B coincides with ai.

**Complexity Analysis**

- Time complexity : O(mn)*O*(*m**n*).

- Space complexity : O(1)*O*(1).

  

------

#### Approach 2: Hash Table

Traverse list A and store the address / reference to each node in a hash set. Then check every node bi in list B: if bi appears in the hash set, then bi is the intersection node.

**Complexity Analysis**

- Time complexity : O(m+n)*O*(*m*+*n*).

- Space complexity : O(m)*O*(*m*) or O(n)*O*(*n*).

  

------

#### Approach 3: Two Pointers

- Maintain two pointers pA*p**A* and pB*p**B* initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
- When pA*p**A* reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pB*p**B* reaches the end of a list, redirect it the head of A.
- If at any point pA*p**A* meets pB*p**B*, then pA*p**A*/pB*p**B* is the intersection node.
- To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) < A.length (=6), pB*p**B* would reach the end of the merged list first, because pB*p**B* traverses exactly 2 nodes less than pA*p**A* does. By redirecting pB*p**B* to head A, and pA*p**A* to head B, we now ask pB*p**B* to travel exactly 2 more nodes than pA*p**A* would. So in the second iteration, they are guaranteed to reach the intersection node at the same time.
- If two lists have intersection, then their last nodes must be the same one. So when pA*p**A*/pB*p**B* reaches the end of a list, record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no intersections.

**Complexity Analysis**

- Time complexity : O(m+n)*O*(*m*+*n*).
- Space complexity : O(1)*O*(1).