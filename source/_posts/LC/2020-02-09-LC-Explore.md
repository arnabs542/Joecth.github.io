---
layout: post
categories: LC
tag: []
date: 2020-01-11

---





|                                                 |      |      |      | status | coded |      |
| ----------------------------------------------- | ---- | ---- | ---- | ------ | ----- | ---- |
| [17 Letter Combinations of a Phone Number](#17) |      |      |      | v      | v     |      |
| [301 Remove Invalid Parentheses](#301)          |      |      |      | HARD   |       |      |
| [139 Word Break](#139)                          |      | DP   |      | v      | v     |      |



## Sorting and Searching

|                               |      |      |      | status | coded |      |
| ----------------------------- | ---- | ---- | ---- | ------ | ----- | ---- |
| [29 Divide Two Integers](#29) |      |      |      | v      | v     |      |
| [50 Pow](#50)                 |      |      |      |        |       |      |
| [75 Sort Colors](#75)         |      |      |      | v      | v     |      |



## DP

|                                     |      |       |      | status | coded |      |
| ----------------------------------- | ---- | ----- | ---- | ------ | ----- | ---- |
| [32 Longest Valid Parentheses](#32) |      | Stack |      | v      | v     |      |
|                                     |      |       |      |        |       |      |
|                                     |      |       |      |        |       |      |



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