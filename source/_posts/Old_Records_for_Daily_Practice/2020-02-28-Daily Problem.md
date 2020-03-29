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



###  Sudoku Check

```python
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        dict_cols = defaultdict(defaultdict)
        for i in range(len(board)):
            dict_row = defaultdict(str)
            if i % 3 == 0:
                dict_boxes = defaultdict(defaultdict)
            
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in dict_row:
                        return False
                    else:
                        dict_row[board[i][j]] = True
                        
                    if board[i][j] in dict_cols[j]:
                        return False
                    else:
                        dict_cols[j][board[i][j]] = True
                        
                    # if board[i][j] in dict_boxes
                    if 0 <= j % 9 <= 2:
                        if board[i][j] in dict_boxes[0]:
                            return False
                        dict_boxes[0][board[i][j]] = True
                    elif 3 <= j % 9 <= 5:
                        if board[i][j] in dict_boxes[1]:
                            return False                        
                        dict_boxes[1][board[i][j]] = True
                    elif 6 <= j % 9 <= 8:
                        if board[i][j] in dict_boxes[2]:
                            return False                        
                        dict_boxes[2][board[i][j]] = True
        return True
```



### ~~Sum of Squares~~



### RM Duplicate from Sorted Linked List

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head :
            return head

        cur = head
        
        while cur.next:
            if cur.next.val == cur.val: # TODO check cur.next
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
```



### ~~N-Queens~~



### ~~Remove One Layer of Parentheses~~

```python
'''
algo.
( score+1
) -1
res = []
if score == 0:
    item.pop()
    res.append(item[1:-1])
return ''.join(res)
'''

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        score = 0
        item = ''
        res = []
        
        for i in range(len(S)):
            # if S[j] == 0:
            if S[i] == '(':
                score += 1
            elif S[i] == ')':
                score -= 1
            item += S[i]    # '(() ...'
            
            if score == 0:
                res.append(item[1:-1])  # NO OOR since slicing helps handle it
                item = ''
        return ''.join(res)
```



### Count Primes

```python
'''
0 1 2 3 4 5 6 7 8 9 10 11 
x x v v   v   v         v
'''
class Solution:
    def countPrimes(self, m: int) -> int:
        n = m - 1
        if n <= 1:
            return 0
            
        isPrime = [None] + [None] * n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2, n+1):
            if isPrime[i] == None:
                isPrime[i] = True
                for j in range(i*2, n+1, i):
                    isPrime[j] = False
        return sum(isPrime)
```



###  Inorder Successor

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
      5
    3     6
   2  4 
'''    
class Solution:
    # def __init__(self):
        # self.flag = False
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode': 
        if not root:
            return None
        # self.result = []
#         self.helper(root, p, [])
        return self.helper(root, p.val)
#         if not self.result:
#             return None
#         else:
#             return self.result[0].val
    '''
          5
        3     33
       2  4     40
               34
                 36 v
    '''  
    def helper(self, root, target):
        cur = root
        suc = None
        while cur:
            # suc = cur
            if target > cur.val:
                cur = cur.right
            elif target == cur.val:
                cur = cur.right
                # if target == cur.val:
            else:
                suc = cur
                cur = cur.left
        return suc
```



### Number of Connected Components in an Undirected Graph



### Split BST

Ref: 

- https://www.coursera.org/lecture/data-structures/split-and-merge-22BgE
- https://leetcode.com/problems/split-bst/discuss/159985/Python-DFS-tm

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
          4                 V == 2
        /   \
      2      6
     / \    / \
    1   3  5   7
'''
class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        return self.helper(root, V)
    
    def helper(self, root, V):
        if not root: 
            return [None, None]
        
        if V < root.val:
            R1, R2 = self.helper(root.left, V)    # keep splitting LHS, 
                                             # R1 means LEFT, R2 means RIGHT
                                             # [2->1, 3]
            # Merge R1 and root.right with root 
            self.merge(R2, root.right, root)      # [3 subtree, 657, 4]
            return [R1, root]                       # [2, 4]
        
        else: # V >= root.val
            R1, R2 = self.helper(root.right, V) # if V==5 or 5.5 
                                                # [5, 6->7]
            self.merge(root.left, R1, root)          # [2 subtree, 5, 4]
            return [root, R2]                   # [4, 6]
            
    def merge(self, l, r, T):
        T.left = l
        T.right = r
```



### Find the Closest Points

```python
import math
import heapq
from collections import deque 
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # return self.helper_heap_KlgK(points, K)
        return self.helper_Q_select(points, K)
    
    def helper_Q_select(self, points, K):
        dis = []
        for pt in points:
            dis.append(self.distance(pt, [0,0]))
        
        self.Q_select(dis, K, points) # 0, len(dis)-1, K)
        return points[:K]
        
    def Q_select(self, dis, K, points):
        
        l, r = 0, len(dis)-1
        while l < r:
            meetup = self.partition(dis, l, r, points)

            if meetup == K:
                return 
            elif meetup < K:
                l = meetup + 1
            else:
                r = meetup - 1        
                
    def partition(self, arr, low, high, points):
        # def swap(x, y):
        #     x, y = y, x
            
        i = low - 1
        pvt = arr[high]      
        '''
              3    0 5 4 1 8 2 2
        low              high 
        X    X X 2 Y Y Y Y 
               i         4   
        # 0 1 2 2
        '''
        for j in range(low, high):
            if arr[j] <= pvt:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                points[i], points[j] = points[j], points[i]
                # swap(arr[j], arr[i])      # NO USE
                # swap(points[j], points[i])
            
        # swap(arr[i+1], arr[high])
        # swap(points[i+1], points[high])
        arr[i+1], arr[high] = arr[high], arr[i+1]
        points[i+1], points[high] = points[high], points[i+1]
        return i+1
    
    def partitionX(self, arr, l, r, points): # 18, 26, 20
        pvt = arr[l]
        pvt_point = points[l]
        i = l+1
        j = r
                    
        while i < j:
            '''
               3 2 1 5 0 8 7 4   
             pvt i i i
                       j, 

               3 2 1 0
             pvt  
                     i
            '''            
            while arr[i] < pvt and i < j:
                i += 1
            while arr[j] > pvt and i < j:
                j -= 1
            # if i < j:
            if True:
                arr[i], arr[j] = arr[j], arr[i]
                points[i], points[j] = points[j], points[i]
                # i += 1
                # j -= 1
        # arr[l], arr[i] = arr[i], pvt   # arr[l] WRONG!
        # points[l], points[i] = points[i], pvt_point   # arr[l] WRONG!
        return j
        
        
    
    def helper_heap_KlgK(self, points, K):  # should use max-heap since we pop out unwanted ones   
        l = []
        for pt in points:   # O(N*lg(K))
            # heapq._heappush_max(l, (self.distance(pt, [0,0]), pt))
            heapq.heappush(l, (-1*self.distance(pt, [0,0]), pt))
            if len(l) == K+1:
                heapq.heappop(l)
        
        Q = deque()
        for j in range(len(l)):
            _, pt = heapq.heappop(l)
            Q.appendleft(pt)
            
        return Q
    
    def helper_heap_NlgN(self, points, K):
        
        l = []
        for pt in points:   # O(N*lg(N))
            # l.append(self.distance(pt, [0,0]), pt)
            heapq.heappush(l, (self.distance(pt, [0,0]), pt))
            
        ans = []
        for j in range(K):
            _, pt = heapq.heappop(l)
            ans.append(pt)
            
        return ans
    
    def kClosest_old(self, points: List[List[int]], K: int) -> List[List[int]]:
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
            
    def distance(self, xy, xy2=[0,0]):
        return math.sqrt((xy[0]-xy2[0])**2 + (xy[1]-xy2[1])**2)#, xy[0], xy[1]
```

**For Quick-Select Complexity Analysis**

- Time Complexity: *O*(*N*) in *average case* complexity, where *N* is the length of `points`., worst when O(N^2)
- Space Complexity: *O*(*N*).



### Duplicate Subtrees

```python
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        """
        serialize each node in post order
        """
        self.mapping = defaultdict(int)
        self.res = []
        self.helper(root)
        return self.res
        
    '''
                1
       /                    \
      2 (2 (4 # #) #)         3
     /          / \
    4 (4 # #)      2   4
                   /
                  4 (4 # #)
    '''
    
    def helper(self, root):
        # post order 
        if not root:
            return "#"
        # if not root.left and not root.right:
            
        
        L = self.helper(root.left)
        R = self.helper(root.right)
        
        pattern = "({} {} {})".format(root.val, L, R)
        # 4 # #
        self.mapping[pattern] += 1

        if self.mapping[pattern] == 2:
            self.res += [root]    
        return pattern
```



###  K Closest Elements

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use a max-heap to maintain 
        # return self.helper_random_when_tie(arr, k, x)
        return self.helper(arr, k, x)
    def helper(self, arr, k, x):
        num_rm = len(arr) - k
        l, r = 0, len(arr)-1
        for i in range(num_rm):
            if abs(arr[l]-x) <= abs(arr[r]-x):
                r -= 1
            else:
                l += 1
        return arr[l:r+1]
  ref: https://www.bilibili.com/video/av92867152?from=search&seid=10589543388785979484
```



### Index of Larger Next Number 

![image-20200322202508690](https://tva1.sinaimg.cn/large/00831rSTgy1gd2z6g4039j318i0r4h4c.jpg)



### Number of Meeting Rooms

```python
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        arr = sorted(intervals, key=lambda x: x[0])
        """
        0   5   10.  15   20.  25.  30     
        s.                           e 
            s    e
                     s     e 
        """
        count = 0
        ends = []
        for i in range(len(arr)):
            if not ends:
                ends.append(arr[i][1])
                count += 1
            # can use while, to compare arr[i][0] with all ends, but we dont' have to store so manu 
            # but if it's ends is sorted ACS, we can compare only once , so , use min-heap
            else:
                # if ends[0] < arr[i][1]:
                if ends[0] <= arr[i][0]:    
                    """結束的那瞬間跟別人開始時一樣是OK的，第二組人馬還是可以用"""
                    # count += 1
                    heapq.heapreplace(ends, arr[i][1])
                else:
                    count += 1
                    heapq.heappush(ends, arr[i][1])
            
        
        return count
```

### ~~Primes~~

### Multiply Strings

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = self.string2num(num1)
        b = self.string2num(num2)
        
        return str(a*b)
        
    def string2num(self, n):
        ret = 0
        for i in range(len(n)):
            digit = ord(n[i]) - ord('0')
            ret = 10*ret + digit
        
        return ret
```



### Remove Adjacent Duplicate Characters

```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        return self.helper2(S)
    
    def helper2(self, S):
        # if len(S)
        tmp = []
        for i in range(len(S)):
            if tmp and tmp[-1] == S[i]:
                tmp.pop()
            else:
                tmp.append(S[i])
                
        return ''.join(tmp)
```

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:  
        return "".join(self.helper(s, k))
    
    def helper(self, s, k):
        stack = [['#', 0]]
        for i in range(len(s)):
            if stack[-1][0] != s[i]:
                stack.append([s[i], 1])
            else:
                # stack[-1] = [stack[-1][0], stack[-1][1]+1]
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        res = ''
        for j in range(len(stack)):
            res += stack[j][0] * stack[j][1]
            
        return res
```



### Common Characters

```python
from collections import Counter, defaultdict
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        c_maps = Counter(A[0])
        # keys, values = c_maps.keys(), c_maps.values()
        
        for i in range(1, len(A)):
            ret = defaultdict(int)
            for j in range(len(A[i])):
                if A[i][j] in c_maps and c_maps[A[i][j]] > 0:
                    ret[A[i][j]] += 1
                    c_maps[A[i][j]] -= 1
            c_maps = ret
        
        res = ''
        for k in ret:
            res += k * ret[k]
            
        return list(res)
```



### ~~Matrix Transpose~~



### Convert to Hexadecimal





###  Remove Character to Create Palindrome

==> Turn into LCS if num of deletion is not limited



### Convert Fraction to Decimal



### 

### 