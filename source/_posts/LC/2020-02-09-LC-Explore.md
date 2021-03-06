---
layout: post
categories: LC
tag: []
date: 2020-01-11

---



## Thoughts

* *Find permutatino of s within b ==> find all anagram of s within b*



## Easy

|                      |      |      |      | status | Coded |      |
| -------------------- | ---- | ---- | ---- | ------ | ----- | ---- |
| [67 Add Binary](#67) |      |      |      | v      | v     |      |
|                      |      |      |      |        |       |      |
|                      |      |      |      |        |       |      |

```python
'''
10101 => 10101
1011  => 1101

1100110 => 010011
10111   => 11101

'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        
        if len(b) > len(a):
            a, b = b, a
        
        a, b = a[::-1], b[::-1] # 10101, 1101
        carry = 0
        i, j = 0, 0
        res = ''
        while i < len(b):
            m = ord(a[i]) - ord('0')
            n = ord(b[i]) - ord('0')
            
            # carry, digit = (m+n)//2, (m+n)%2+carry
            carry, digit = (m+n+carry)//2, (m+n+carry)%2
            res += str(digit)
            i += 1
        
        # i == 4
        while i <= len(a) - 1:  # 4 <= 5-1
            m = ord(a[i]) - ord('0')
            carry, digit = (m+carry)//2, (m+carry)%2
            res += str(digit)
            i += 1
            
        if carry == 1:
            res += str(carry)
            
        return res[::-1]
```



fib memory

```python

def fib(n, mem=[]):
	if n == 0 or n == 1:
    return 1
  else:
    if mem[n] == 0:
      mem[n] = fib(n-1) + fib(n-1)
  return mem[n]
```





|                                                 |      |      |      | status | coded |      |
| ----------------------------------------------- | ---- | ---- | ---- | ------ | ----- | ---- |
| [17 Letter Combinations of a Phone Number](#17) |      |      |      | v      | v     |      |
| [301 Remove Invalid Parentheses](#301)          |      |      |      | HARD   |       |      |
| [139 Word Break](#139)                          |      | DP   |      | v      | v     |      |



### Bit Manipulation

|                                |                                         |      | status | coded |      |
| ------------------------------ | --------------------------------------- | ---- | ------ | ----- | ---- |
| [190 Reverse Bits](#190)       | zfill("1100") --> 前面補齊0讓這串到32位 |      | v      | v     |      |
| [7 Reverse Interger](#7)       |                                         |      | v      | v     |      |
| [191 Number of 1's bits](#191) |                                         |      | v      | v     |      |
| [461 Hamming Distance](#461)   |                                         |      | v      | v     |      |



### <a name="7">7</a>

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:return 0
        
        flag = -1 if x < 0 else 1
        y = list(str(abs(x)))
        self.helper(y, 0, len(y)-1)
        
        res = int(''.join(y))
        
        # print(res)
        if flag == 1:
            return flag*res if flag*res <= 2**31-1 else 0
        else:
            return flag*res if flag*res >= -2**31 else 0
        
    
    def helper(self, s, l, r):
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        self.helper(s, l+1, r-1)
```



### <a name="190">190</a>

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
```



### <a name="191">191</a>

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        mask = 1
        while n:
            # print(n)
            if n & mask != 0:
                count += 1
            n >>= 1
        return count
```



### <a name="461">461</a>

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        return self.count1s(ans)
        
        
    def count1s(self, num):
        count = 0
        mask = 1
        while num:
            if num & mask != 0:
                count += 1
            num >>= 1
            
        return count
```





## Sorting and Searching

|                                                              |      |      |          | status | coded |      |
| ------------------------------------------------------------ | ---- | ---- | -------- | ------ | ----- | ---- |
| [29 Divide Two Integers](#29)                                |      |      |          | v      | v     |      |
| [50 Pow](#50)                                                |      |      |          |        |       |      |
| [75 Sort Colors](#75)                                        |      |      |          | v      | v     |      |
| [692 Top K frequent words](#692)                             |      |      |          | v      | v     |      |
| [973 K Close points to origin](#973)                         |      |      |          | v      | v     |      |
| [215 K largest element in an Array](#215)                    |      | heap | Q-select | v      | v     |      |
| [34 Find First and Last Position of Element in Sorted Array](#34) |      |      |          | v      | v     |      |



### <a name="215">215</a>

```python
'''
def partition(l, r, arr)
    3 5 2 1 5 6 4   k=2

    pvt 3 l 2 r 4

    fn to set 3 at idx2
    while l<r:
        while arr[i] 5 < 3: wrong
            l ++
        l 2
        while arr[j]  > 3: till 1 idx -4 == idx 3
            r -- 
        r 3
        swap(arr[l], arr[r])
      3 1 2 5 5 6 4 
          l
          r
      2 1 3 5 5 6 4   
        return l
    
2 1 3 5 5 6 4   
1 2 3 4 5 6  2nd large means idx 4 == 6 - 2 
K largest means K_idx = len(arr) - K small
while l < r
    idx = partition()    
    K_idx = len(arr) - K
    if K_idx < idx:
        r = idx - 1
    elif k_idx > idx:
        l = idx +1
    else:
        break
return arr[K_idx]
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        # return self.helper_heapq(nums, k)
        return self.helper_Q_select(nums, k)
    
    def helper_Q_select(self, nums, k):
        # if i >= j:
        #     return 0
        
        i, j = 0, len(nums)-1
        # 1 2 3 4 5 6
        
        # k = 2 ==> idx 4.  6-2
        k_idx = len(nums) - k
        while i < j:
            # pvt_idx = self.partition(i, j, nums)
            pvt_idx = self.partition(nums, i, j)
            if k_idx < pvt_idx:
                j = pvt_idx - 1
            elif k_idx > pvt_idx:
                i = pvt_idx + 1
            else:
                break
        return nums[k_idx]
    
    def partition(self, arr,low,high): 
        i = low-1        # index of smaller element 
        pivot = arr[high]     # pivot 

        for j in range(low , high): 

            # If current element is smaller than or 
            # equal to pivot 
            if   arr[j] <= pivot: 

                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 

        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return i+1

    def partition_X(self, l, r, arr):
        def swap(x, y):
            x, y = y, x
        
        i, j = l, r
        pvt = arr[l]
        while i < j:
            while arr[i] < pvt and i < j:
                i += 1
            while arr[j] > pvt and i < j:
                j -= 1
            swap(arr[i], arr[j])
                 
    def helper_heapq(self, nums: List[int], k: int) -> int:
        # l = nums
        if not nums:
            return 0

        heapq.heapify(nums) #O(N)
        ks = len(nums) - k + 1
        for i in range(ks-1):
            heapq.heappop(nums) # ks * O(lgN)
        return heapq.heappop(nums)
```

- Time complexity : O(*N*) in the average case, O(*N*2) in the worst case.
- Space complexity : O(1).



## DP

|                                     |      |                                                         |      | status | coded |           |
| ----------------------------------- | ---- | ------------------------------------------------------- | ---- | ------ | ----- | --------- |
| [32 Longest Valid Parentheses](#32) |      | Stack                                                   |      | v      | v     |           |
| [518 coin changes 2](#518)          |      |                                                         |      | v      |       |           |
| [91 Decode Ways](#91)               |      | backtracking並紀錄樹的每條路徑，就像wrod break時做的dfs |      |        |       | dp[0] = 1 |



### <a name="91">91</a>

https://www.tianmaying.com/tutorial/LC91

```python
class Solution:
    def numDecodings(self, s):
        if not s: return 0
        len_s = len(s)
        dp = [1] + [0] * len_s
        for i in range(1, len_s + 1):
            if s[i - 1] != '0': 
                dp[i] += dp[i - 1]
            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26: 
                dp[i] += dp[i - 2]
        return dp[len_s]
```



### <a name="29">29</a>

```python
'''
for example, if we want to calc (17/2)

ret = 0;

17-2 ,ret+=1; left=15

15-4 ,ret+=2; left=11

11-8 ,ret+=4; left=3

3-2 ,ret+=1; left=1

ret=8;
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """        
        if not dividend:
            return 0
        
        flag = 1
        if dividend * divisor < 0:
            flag = -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        Q = 0
        while dividend >= divisor:
            temp, q = divisor, 1
            print('temp out', temp)

            while dividend >= temp:
                dividend -= temp
                Q += q
                temp <<= 1				# CRUCIAL!! <<=
                # print('temp ', temp)
                q <<= 1
                # print('q ', q)


        # q = 0
        # while dividend:
        #     dividend -= divisor
        #     q += 1
            
             
        if flag == 1:
            return min(Q, 2**31-1)
        else:
            return max(-1*Q, -1*2**31)
```



### <a name="32">32</a>

```python
    
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        # S ( pushback the index
        #   ) pop
        # S = []
        g_max = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:       # to prevent OOR
                    val = stack.pop()
                if not stack:
                    stack.append(i)
                g_max = max(g_max, i-stack[-1])     # pop後，拿棧頂的值
        return g_max
```



### <a name="34">34</a>

```python
from bisect import * # bisect_left() bisect_right()
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        # if len(nums) == 1:
        #     if nums[0] == target:
        #         return [0,0]
        #     else:
        #         return [-1,-1]
        
        # l, r = 0, len(nums)-1
        l, r = 0, len(nums)
        while l<r:
            mid = l + (r-l)//2
            if target <= nums[mid]:     # [5,7,7,8,8,10]
                r = mid
            else:
                l = mid + 1
                # r = mid
        
        # i, j = 0, len(nums)-1
        i, j = 0, len(nums)
        while i<j:
            mid = i + (j-i)//2
            if target < nums[mid]:
                j = mid
            else:
                i = mid + 1
        
        # print(l, i)
        if l == i:# and nums[l] != target:
            return [-1, -1]
        
        return [l, i-1]
```



### <a name="50">50</a>

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ''' TLE
        res = 1.0
        for _ in range(abs(n)):
            if n > 0:
                res *= x
            else:
                res /= x
        return res
        '''
        
        m = abs(n)
        p, q = 1, x
        while m > 0:
            if (m & 1) == 1:
                p *= q
            m //= 2
            q *= q
            
        return 1/p if n < 0 else p
```



##### Recursive

```python
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        
        if n == 1:
            return x
        
        m = n // 2
        if n < 0:
            m = -m
            x = 1/x
            
        res = self.myPow(x, m)
        
        if (n & 1) == 0:
            return res * res
        return res * res * x

```





## Recursion



### <a name="17">17</a>

*Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.*

*A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.*

```python
# 2 3 4
# a d g
# b e h
# c f i

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.d = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
                           
        # states = [1 for i in range(len(digits))]    # 234 -> [1,1,1]
        # item = 
        self.result = []
        item = ''
        self.helper(0, digits, item)
        return self.result
    
    def helper(self, level ,digits, item):
        if level == len(digits) and item not in self.result:
            if len(item) == len(digits):
                self.result.append(item)
            return 
        
        ref = digits[level:]
        # for num in range(len(ref)): # didn't require permutation so we don
            # chars = self.d[ref[num]]
        if True:
            chars = self.d[ref[0]]
            for c in chars:
                item += c
                self.helper(level+1, digits, item)
                item = item[:-1] #item[-1] +   # shouldn't be pop()
                self.helper(level+1, digits, item)
            # item = item[:-1]
            # level += 1
```



### <a name="139">139</a>

##### DP

```python
#       l e e t c o d e
# dp [F F F F T             ] 

# for i in s:


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        # dp0 means "" in d == > True
        
        # dp1 = dp0 && l in dict?  s[0:1]
        
        # dp2 = dp0 && le in dict? s[0:2]  or  
        #       dp1 && e in dict?  s[1:2]
        
        # dp3 = dp0 && lee in dict?  s[0:3]  or  
        #       dp1 && ee in dict?   s[1:3] or
        #       dp2 && e in dict?    s[2:3]
        
        # dp4 = dp0 && leet in dict?  or  
        #       dp1 && ed in dict? or
        #       dp2 && d in dict? or
        '''
        dp = [1] + [0 for i in range(len(s))]
        wordSet = set(wordDict)
        for i in range(1, len(s)+1):
            for j in range(0, i):
                # dp[i] += dp[i] + wordDict.get(s[i-1:j-1])   # dp1 = dp0 + d.get(s[0:1])
                dp[i] += dp[j] and s[j:i] in wordSet #wordDict.get(s[j:i])
                # print(dp)
        return dp[-1]
```





<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gbpjjeli2bj31kn0u0n0n.jpg" alt="image-20200209021111564" style="zoom:50%;" />

![image-20200209002506411](https://tva1.sinaimg.cn/large/0082zybpgy1gbq8o5w8lhj31l80tc0w1.jpg)

<img src="https://tva1.sinaimg.cn/large/0082zybpgy1gbpjjp0joyj31k70u0wiw.jpg" alt="image-20200209003837603" style="zoom:50%;" />



##### bfs

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from collections import deque
        q = deque([s])
        seen = set() 
        while q:
            s = q.popleft()    # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False
```



### <a name="301">301</a>

```python
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
                  
        ans = []
        lefts_to_remove, rights_to_remove = 0, 0
        lefts, rights = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                lefts += 1
            elif s[i] == ')':
                if lefts > 0:
                    lefts -= 1
                else:
                    rights_to_remove += 1 #if right doesn't have a matching left, it should be removed
        lefts_to_remove = lefts #if we have more lefts than rights, extra lefts should be removed
        
        self.backtracking(0, 0, s, 0, '', ans, lefts_to_remove, rights_to_remove)
        if not ans:
            ans.append('')
        
        return ans
                    
    
    def backtracking(self, lefts, rights, s, ind, cur_str, ans, lefts_to_remove, rights_to_remove):
        if ind == len(s):
            if lefts == rights and lefts_to_remove==0 and rights_to_remove==0 and cur_str not in ans:
                ans.append(cur_str)
            return
        
        if s[ind] == '(':
            if lefts_to_remove > 0:
                self.backtracking(lefts, rights, s, ind+1, cur_str, ans, lefts_to_remove-1, rights_to_remove)
            self.backtracking(lefts+1, rights, s, ind+1, cur_str+'(', ans, lefts_to_remove, rights_to_remove)
            
        elif s[ind] == ')':
            if (lefts==0 or lefts>=rights) and rights_to_remove > 0:
                self.backtracking(lefts, rights, s, ind+1, cur_str, ans, lefts_to_remove, rights_to_remove-1)
            if lefts > rights:
                self.backtracking(lefts, rights+1, s, ind+1, cur_str+')', ans, lefts_to_remove, rights_to_remove)
            
        else:
            self.backtracking(lefts, rights, s, ind+1, cur_str+s[ind], ans, lefts_to_remove, rights_to_remove)
```





## Lai Offer

|                       |      |      |      | status | coded |      |
| --------------------- | ---- | ---- | ---- | ------ | ----- | ---- |
| [75 Sort Colors](#75) |      |      |      |        |       |      |
|                       |      |      |      |        |       |      |
|                       |      |      |      |        |       |      |



### <a name="75">75</a>

![image-20200208231937717](https://tva1.sinaimg.cn/large/0082zybpgy1gbpekpqfdcj30b60900u8.jpg)

![image-20200208232444790](https://tva1.sinaimg.cn/large/0082zybpgy1gbpeq1jl8ij30rw116k6y.jpg)

![image-20200208232746397](https://tva1.sinaimg.cn/large/0082zybpgy1gbpet5afu8j30u00zxnax.jpg)



### <a name="518">518</a>

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200209233108458.png" alt="image-20200209233108458" style="zoom:50%;" />





### <a name="973">973</a>

```python
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ''' N*log(N)
        # Q-sort tech
        # [dis1, dis2, dis3]
        if not points or not K:
            return 0
        l = []
        for xy in points:
            heapq.heappush(l, (self.distance(xy), xy[0], xy[1]))  # n*log(n)
            # if len(l) > K:
            #     heapq._heappop_max(l)

        # map(points, self.distance)
        # for point in points:
        #     self.distance(point)
        
        res = []
        for i in range(K):
            dis, x, y = heapq.heappop(l)
            res.append([x,y])
            
        return res
        '''
        l = []
        for xy in points:
            dist = self.distance(xy)
            dist = -1*dist
            if len(l) <= K-1:
                heapq.heappush(l, (dist, xy))
            else:
                # print('---', dist)
                if dist > l[0][0]:
                    heapq.heappop(l)
                    heapq.heappush(l, (dist, xy))
                    
        res = []
        # for i in range(len(l)):
        for i in range(K):
            res.append(heapq.heappop(l)[1])
        return res
            
    def distance(self, xy):
        return math.sqrt(xy[0]**2 + xy[1]**2)#, xy[0], xy[1]
```



##### Build-in

```python

# Python program for implementation of  
# above approach 
  
# Function to return required answer 
def pClosest(points, K): 
  
    points.sort(key = lambda K: K[0]**2 + K[1]**2) 
  
    return points[:K] 
  
# Driver program 
points = [[3, 3], [5, -1], [-2, 4]] 
  
K = 2
  
print(pClosest(points, K)) 
```

