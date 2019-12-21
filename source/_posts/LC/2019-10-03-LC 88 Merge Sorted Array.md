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

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail = m + n - 1
        l1, l2 = m, n
        # left1, left2 = m, n
        
        while l1 and l2:
            if nums1[l1-1] <= nums2[l2-1]:
                nums1[tail] = nums2[l2-1]
                l2 -= 1
            else:
                nums1[tail] = nums1[l1-1]
                
                l1 -= 1
            # print(nums1)
            # print(l2)
            tail -= 1
            
        if l1:
            pass
        
        if l2 > 0:
            nums1[:l2] = nums2[:l2]
            
                
```

