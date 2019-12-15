---
layout: post
categories: LC
tag: [Michelle, backtracking, TODO] 


---

```python
class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        
        result = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for j in self.permute(n):
                # print(nums[i], j)
                result.append([nums[i]] + j)
        return result
```

https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

```python
class Solution(object):
    def permute_dfs(self, path, nums, result):
        if len(nums) == 1:
            result.append(path+nums)
            return
        else:
            for i in range(0, len(nums)):
                tmp_list = nums[:]
                pop_out = tmp_list.pop(i)
                self.permute_dfs(path+[pop_out], tmp_list, result)


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permute_dfs([], nums, result)
        return result
```



![image-20191003115310184](https://tva1.sinaimg.cn/large/006y8mN6ly1g7kvffagflj30pm0fg0us.jpg)

ref: https://www.youtube.com/watch?v=nrHTtjkYEyQ

![image-20191003102218161](https://tva1.sinaimg.cn/large/006y8mN6ly1g7kssw1ayej31ic0mcdzm.jpg)

![image-20191003105327148](https://tva1.sinaimg.cn/large/006y8mN6ly1g7ktpb6c1oj31d80n07km.jpg)

![image-20191003110018474](/Users/joe/Library/Application Support/typora-user-images/image-20191003110018474.png)

![image-20191003105739813](https://tva1.sinaimg.cn/large/006y8mN6ly1g7kttnsg14j31a40mqne7.jpg)