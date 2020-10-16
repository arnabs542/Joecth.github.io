---
layout: post
categories: Mock
tag: [] 
date: 2019-09-13
---



- Attendees:

  Wu, Sisi, Congcong & Me

  

- Pros: 個人覺得自己對於一路下來的優化思路很清楚又流暢

- Cons: 最初的解釋裡，dp盲想思考錯誤，在coding foo3過程中發現應是要對 pre_sum作dp，但這點在最初並未闡明清楚

- Special Takeaways:

  1. 貪心也可解釋
  2. 2D時的 follow-up
  3. 對 array 性質闡明的問題
     - 是否有負?	  ==> 對解有影響
     - 是否sorted?  ==> 對解有影響
     - 是否都整數?  ==> 對解沒影響

- Similar to:

  - Best Time to Buy and Sell Stock



```python
arr 
    max sum(subarry)

[3 -5 7 8]
 i    j 
sum([:3])

[-1,-2,-3,1,2,3]:    12:23

    for i in range(n) 
        pre = Math.max(0, pre);
        # 贪心，到i时
        
        pre = pre + cur[i];
        result = Math.max(result, pre);# THIS IS RESULT
    return result;

class Solution:
    res 
    # O(N^3)
    def foo1(self, arr):
        for i in range(n):
            for j in range(n):
                res = sum()    # O(N)
    
    pre_sum
    3 -5 7 8
    3 -2 5 13 pre_sum ==> O(1) for interval sum
    res 
    # O(N^2)
    def foo2(self, arr):
        for i :
            for j:
    """ 2:30 """
        
    # O(N) TIME ; O(1) SPACE
    # at ith pos, max(sum(subarray)) ==> work on pre_sum需要讲!
    
    
    # dp 含义
    # dp 递推关系/转移方程
    # pre -> current
    def foo3(self, arr):
        n = len(arr)
        pre_sum = [0] * n
        pre_sum[0] = arr[0]    # 当presum < 0 就可直接清了

        for i in range(1, n):    # O(N)
            pre_sum[i] = pre_sum[i-1] + arr[i]
        # dp should be based on pre_sum 
        
        # dp = [0] * n
        # dp[0] = pre_sum[0]    ==> 
        res = prev_sum[0]
        cur_min = pre_sum[0]
        for i in range(1, n):
            # dp[i] = max(dp[i-1], pre_sum[i] - cur_min)
            # dp[i] = max(dp[i-1], pre_sum[i] - cur_min)
            res = max(res, pre_sum[i] - cur_min) 
            cur_min = min(cur_min, pre_sum[i])
        # return dp[-1]
        return res
    """ 2:30 ~ 2:43 """
    minus?
    sorted?
    int?
    OOR?
    where's DP?  ==> Line.37
    时间、哪里好？哪里不好？
    Clarification
    codine
    bug? test_cast?
    communication?
    explanation of Alg?
    def foo4_2D(self, arr):
        # pass
        follow up ?!    4 5 -11 13 
                        5 9  10
        max rectangle
    
# test cases
print(Solution().foo3([2, -6, 8, 9]))
```

My link: https://coderpad.io/NZTYRAGH