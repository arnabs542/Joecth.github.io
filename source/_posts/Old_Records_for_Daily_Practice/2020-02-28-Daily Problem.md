---

layout: post
categories: Daily
tag: []
date: 2020-02-28

---



### Anagram in a string

```python
def find_anagrams(s, t):
  # Fill this in.

print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]
```

```python
from collections import Counter
class Solution:
    def findAnagrams_Counter(self, s: str, p: str) -> List[int]:    # Took 7300 ms
        window = len(p)
        c_p = Counter(p)
        
        res = []
        for i in range(window-1, len(s)):   # 2
            pat = s[i-window+1:i+1]
            # print(pat)
            c_pat = Counter(pat)  
            
            if c_p == c_pat:
                res.append(i-window+1) 
        return res
            

    def findAnagrams(self, s: str, p: str) -> List[int]:    # 100 ms
        if not s or not p:
            return []
        
        enc_p = self.encoder(p)
        win = len(p)
        # enc_s = self.encoder(s[:win])
        
        offset = win-1
        res = []
        '''Dynamically update pattern in s'''
        # for i in range(offset, len(s)):
        enc_c = [0] * 26
        j = 0
        for i in range(len(s)):
            enc_c[ord(s[i]) - ord('a')] += 1
            if i - j >= win:
                enc_c[ord(s[j]) - ord('a')] -= 1
                j += 1
            if enc_c == enc_p:
                res.append(j)
        return res
        
    def findAnagrams_TLE(self, s: str, p: str) -> List[int]:    # TLE
        ''' TLE, SHOULD Dynamically  Update enc_tmp'''
        if not s or not p:
            return []
        
        enc_p = self.encoder(p)
        win = len(p)
        
        offset = win-1
        res = []
        for i in range(offset, len(s)):
            start = i - win + 1
            sub_s = s[start:i+1]
            # print(sub_s)
            enc_tmp = self.encoder(sub_s)  # 2 - (3-1) : 3  # No OOR
            
            if enc_tmp == enc_p:
                res.append(start)
        return res
```



### ~~Reverse Words~~

```python
def reverse_words(words):
  # Fill this in.

s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can
```

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        l = s.split()[::-1]
        res = ' '.join(l)
        
        return res
```

### ~~Reverse Words Ⅱ~~

Given an input string , reverse the string word by word. 

**Example:**

```
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
```

```python
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        t = ' '.join(''.join(s).split()[::-1])
        
        for i in range(len(s)):
            s[i] = t[i]
```

### ~~Reverse Words Ⅲ~~

**Example 1:**

```
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        t  = s.split()
        res = []
        for w in t:
            w = w[::-1]
            res.append(w)
        
        return ' '.join(res)
```



### ~~Find Subtree~~

Given 2 binary trees t and s, find if s has an equal subtree in t, where the structure and the values are the same. Return True if it exists, otherwise return False.

Here's some starter code and an example:

```python
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"(Value: {self.value} Left: {self.left} Right: {self.right})"

def find_subtree(s, t):
  # Fill this in.

t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))
"""
Tree t:
    1
   / \
  4   5 
 / \ / \
3  2 4 -1

Tree s:
  4 
 / \
3  2 
"""

print(find_subtree(s, t))
# True
```

```python
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
            # self.isSubtree()
        # self.t = t
        return self.preorder(s, t) or self.preorder(t, s)
        
    def preorder(self, root, ref):
        if not root:
            return False
        ans =  self.is_sametree(root, ref)
        
        L_has_same = self.preorder(root.left, ref)
        R_has_same = self.preorder(root.right, ref)
        return ans or L_has_same or R_has_same
        
    def is_sametree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        return s.val == t.val and self.is_sametree(s.left, t.left) and self.is_sametree(s.right, t.right)
```



### ~~Sorted Square Numbers~~

```
def square_numbers(nums):
 # Fill this in.

print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]Solve this problem in O(n) time.
```



### ~~Picking up Change?!~~



### Determine if numbe -- Hard if not able to use built-in...

Given a string that may represent a number, determine if it is a number. Here's some of examples of how the number may be presented:

```
"123" # Integer
"12.3" # Floating point
"-123" # Negative numbers
"-.3" # Negative floating point
"1.5e5" # Scientific notation
```

Here's some examples of what isn't a proper number:

```
"12a" # No letters
"1 2" # No space between numbers
"1e1.2" # Exponent can only be an integer (positive or negative or 0)
```

Scientific notation requires the first number to be less than 10, however to simplify the solution assume the first number can be greater than 10. Do not parse the string with int() or any other python functions.



## Swap bits -- A Neat Bitwise Trick For Swapping Even and Odd Bits

```
def swap_bits(x):
    EVEN = 0b10101010
    ODD = 0b01010101
    return (x & EVEN) >> 1 | (x & ODD) << 1
```



### String to Integer(atoi)

```python
class Solution:
    def myAtoi(self, str: str) -> int:
        t = str.strip()
        if not t:
            return 0
    
    
        if t[0] not in '+-1234567890':
            return 0
        
        flag = 1
        if t[0] == '-':
            if len(t) == 1:
                return 0
            flag = -1
            t = t[1:]
        elif t[0] == '+':
            if len(t) == 1:
                return 0
            t = t[1:]
        
        if t[0] not in "1234567890":
            return 0
        
        # chech 0s and " "
        q = 0
        while q < len(t):
            if t[q] in "1234567890":
                break
            q += 1
                
        if q == len(t):# or q == 0:
            return 0
            
        t = t[q:]
        res = 0
        tmp = 10
        
        for idx in range(len(t)):
            if t[idx] not in "1234567890":
                break
            digit = (ord(t[idx]) - ord('0'))
            # print(digit)
            # res *= tmp
            res = tmp*res + digit
            # tmp *= 10

    
        ans = res*flag
        if flag == 1:
            return min(ans, 2**31 - 1)
        else:
            return max(ans, -2**31)
```



### ~~Rotate Matrix~~

### Pow

##### Wrong, This doesn't solve overflow issue for [-2^(31), 2^31-1]

```python
# import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x  == 1: 
            return 1
        if n == 1:
            return x
        if n < 0:       #2**(-3) ==  1/2**3 == 2* 2**(-4)
            # n = -(n+1)
            n = abs(n) + 1
            return x * (1/self.pos_pow(x, n))
        return self.pos_pow(x, n)
            
    def pos_pow(self, x, n):
        # print(x, n)
        res = 1    
        while n > 0:
            if n % 2 != 0:
                res *= x
            # x = x ** 2      # TODO: CAUTIOUS, Numerical result out of range for (2, -2**31)
            x = x * x         # SHOULD USE THIS!
            n = n//2
            
        return res
    '''
    for neg number: 
    [-2**31, 2**31 -1]
    
res   base index
1     2    9      ** --> ans!
2     4    4
2     16   2
2     256  1


1     2    10
1     4    5
4     16   2
4     256  1
    '''       
```



##### Correct

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if n == 1:
            return x
        if n < 0:
            # return XXXX # TODO
            n1 = abs(n) - 1                         # n == -2**31
            return (1/x) * (1/self.pos_pow(x, n1))  # 2^(-4) == 1/2^4 ==  1/2 * 1/2^3
        return self.pos_pow(x, n)
    
    def pos_pow(self, base, idx):
        res = 1
        while idx > 0:
            # print(base, idx)
            if idx % 2 == 1:
                res *= base
            base *= base
            idx //= 2
        return res
        
    '''
    res base    idx
    1   2       10
    1   4       5
    4   16      2    
    4   256     1
    ans 
    '''    
```



### ~~Sqrt~~

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        # if x <= 1:
        #     return x
        l, r = 0, x
        
        while l <= r:
            mid = l + (r-l)//2
            print(l, r, mid)
            if  mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid > x:
                r = mid - 1
            else:
                l = mid + 1
```



### Missing Ranges

Given a sorted integer array ***nums\***, where the range of elements are in the **inclusive range** **[\*lower\*, \*upper\*]**, return its missing ranges.

```python
'''
0 1 3         50
start       1+1 = 2   4
'''

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [str(lower) + "->" + str(upper)] if lower != upper else [str(lower)]


        res = []
        # item = ""
        if nums[0] != lower:
            # print('aaaaaaa')
            item = "{}->{}".format(lower, nums[0]-1) if lower != nums[0] - 1 else "{}".format(str(lower))
            res.append(item)
            
        start, end = float('-inf'), float('inf')
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - prev > 1:
                start, end = prev + 1, nums[i] - 1
                item = "{}->{}".format(start, end) if start != end else str(end)
                res.append(item)
            prev = nums[i]
        if nums[-1] != upper:
            item = "{}->{}".format(nums[-1]+1, upper) if nums[-1] + 1 != upper else "{}".format(str(upper))
            res.append(item)
            
        return res    
```



###  Inorder Successor