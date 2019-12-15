---
layout: post
categories: LC
tag: [ComeO, TODO, F] 



---



```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0:1} # prefix sum array
        res = s = 0
        for n in nums:
            s += n # increment current sum
            res += sums.get(s - k, 0) # check if there is a prefix subarray we can take out to reach k
            sums[s] = sums.get(s, 0) + 1 # add current sum to sum count
        return res
```



![image-20191013180255420](https://tva1.sinaimg.cn/large/006y8mN6ly1g7wqpggtp7j30sk0p6aj8.jpg)

![image-20191013181655295](https://tva1.sinaimg.cn/large/006y8mN6ly1g7wqpezqocj30s80pa12w.jpg)

![image-20191013182807071](https://tva1.sinaimg.cn/large/006y8mN6ly1g7wr10p1g3j30ye0r2h1t.jpg)

![image-20191013184334864](https://tva1.sinaimg.cn/large/006y8mN6ly1g7wrh387aej30xy0q8dt9.jpg)