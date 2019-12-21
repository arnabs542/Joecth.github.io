---
layout: post
categories: LC
date: 2019-10-02
tag: [F, TODO] 

---



```python
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: list
        :type k: int
        :rtype: int
        """
        pre_sum = [0]+list(accumulate(nums))
        res = 0
        for i in range(len(pre_sum)):
            for j in range(i, len(pre_sum)):
                if pre_sum[j] - pre_sum[i] == k:
                    res = max(res, j - i)
        return res


obj = Solution()
print(obj.maxSubArrayLen([1, -1, 5, -2, 3], k = 3))
# https://blog.csdn.net/qq_17550379/article/details/86421075
```





```python
def maxSubArrayLen(self, nums, k):
    """
    :type nums: list
    :type k: int
    :rtype: int
    """
    pre_sum = list(accumulate(nums))
    res, dic = 0, dict()

    for i in range(len(pre_sum)):
        if pre_sum[i] == k:
            res = i + 1
        elif pre_sum[i] - k in dic:
            res = max(res, i - dic[pre_sum[i] - k])
        if pre_sum[i] not in dic:
            dic[pre_sum[i]] = i

    return res
 #https://blog.csdn.net/qq_17550379/article/details/86421075
```

O(n)



```python
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum2idx = { 0:-1 }
        res, sum = 0, 0
        for i, n in enumerate(nums):
            sum += n
            if sum not in sum2idx: sum2idx[sum] = i
            if sum-k in sum2idx: res = max(res, i-sum2idx[sum-k])
        return res
```





560. Subarray Sum Equals K
974. Subarray Sums Divisible by K
325. Maximum Size Subarray Sum Equals k
1074. Number of Submatrices That Sum to Target