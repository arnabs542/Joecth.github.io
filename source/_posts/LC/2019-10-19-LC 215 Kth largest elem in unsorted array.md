---
layout: post
categories: LC
date: 2019-10-19
tag: [PriorityQueue] 



---



```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.nlargest(k, nums)[-1]

        heap = nums[:k]
        heapq.heapify(heap)  # create a min-heap whose size is k 
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
            # or use:
            # heapq.heappushpop(heap, num)
        return heap[0]
```



```python
def findKthLargest4(self, nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for _ in xrange(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)

```

O(k + (n-k)lgk), min-heap

https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).

https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60535/Python-min-heap-and-quick-partition-solutions-(O(nlogn)-and-O(n)-time-complexities).

![image-20191020221341178](https://tva1.sinaimg.cn/large/006y8mN6ly1g850vwuwa4j30z00mujvz.jpg)

![image-20191020222727380](https://tva1.sinaimg.cn/large/006y8mN6ly1g851a6z53yj30yu0nsqbc.jpg)