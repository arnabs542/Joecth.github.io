---
layout: post
categories: LC
tag: [F] 


---



```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # if not nums1:
        #     return nums2[len(nums2)//2]
        # if not nums2:
        #     return nums1[len(nums1)//2]
        
        tmp = sorted(nums1 + nums2)
        return tmp[len(tmp)//2] if len(tmp) % 2 else (tmp[len(tmp)//2] + tmp[len(tmp)//2 - 1])/2
```



![image-20191021225248065](https://tva1.sinaimg.cn/large/006y8mN6ly1g867mxsgzuj310o0mwqij.jpg)