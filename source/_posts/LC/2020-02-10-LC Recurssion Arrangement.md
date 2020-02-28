---
layout: post
categories: LC
tag: []
date: 2020-02-10

---



## Binary Tree

|                                |      |      |      |      |      |      |
| ------------------------------ | ---- | ---- | ---- | ---- | ---- | ---- |
| [Maximum depth of Binary Tree] |      |      |      |      |      |      |
| [Symmetric Tree]               |      |      |      |      |      |      |
| [Path Sum]                     |      |      |      |      |      |      |
| [Count Univalue Subtrees]      |      |      |      |      |      |      |
|                                |      |      |      |      |      |      |





|                             |      |      |      | status | coded |      |
| --------------------------- | ---- | ---- | ---- | ------ | ----- | ---- |
| [39 Combination Sum](#39)   |      |      |      | v      | v     |      |
| [40 Combination Sum Ⅱ](#40) |      |      |      | v      | v     |      |
| [77 Combinations](#77)      |      | easy |      | v      | v     |      |
| [79 Word Search](#)         |      |      |      |        |       |      |



### <a name="39">39</a>

```python
from collections import Counter
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: 
            return []
        self.result = []
        # self.counters = {}
        l = sorted(candidates, key=lambda val: val)
        self.helper(l, 0, target, [], 0)
        
        return self.result

    '''
    
    '''
    def helper(self, l, idx, rem, item, level):
        if rem == 0:
            self.result.append(item.copy())
            return
        if idx == len(l) or rem < l[idx] or rem < 0:
            return
        
        # 2 3 6 7     7               2
        elem = l[idx]
        item.append(elem)
        rem -= elem
        # if rem < elem:        SHOULDN'T TRUNCATE HERE 
        #     return      #1 < 2       2 2 
        self.helper(l, idx, rem, item, level+1)
        item.pop()
        rem += elem
        self.helper(l, idx+1, rem, item, level+1)   
```



### <a name="77">77</a>

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.helper(n, k, 0, []) 
        
        return self.result
    
    def helper(self, n, k, idx, item):    # 4, 2 # no level since already have len(item)
        if len(item) == k:
            self.result.append(item.copy())
            return
        
        for i in range(idx, n):
            item.append(i+1)
            self.helper(n, k, i+1, item)    # i, level
            item.pop()
```



### <a name="40">40</a>

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        result = []
        candidates.sort()
        self.gen(0, candidates, [], result, 0)
        return result
    
    def gen(self, i, nums, items, result, total):


        if i == len(nums):
            return
        
        items.append(nums[i])
        total += nums[i]
        # if sum(items) == self.target:
        if total == self.target:
            if items not in result:
                result.append(items)
            return
        
        if total <= self.target:   # to prune as early as possible
            self.gen(i+1, nums, items.copy(), result, total)
            
        items.pop()
        total -= nums[i]
        self.gen(i+1, nums, items.copy(), result, total)
        
```



### <a name="79">79</a>

```python
from copy import deepcopy
# from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return []
        
        ans = False
        # visited = [[False for j in range(len(board[0]))]for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[False for j in range(len(board[0]))]for i in range(len(board))]
                    ans = self.helper(board, i, j, word, False, visited) or ans  
                    if ans:
                        return ans
        return ans
    
    '''
    First version failed AT:
    [["C","A","A"],
     ["A","A","A"],
     ["B","C","D"]]
    "AAB"
    '''
    def helper(self, board, row, col, item, ans, visited):
        # if not item:
        #     return True
        if visited[row][col] == True:
            return False
        
        if board[row][col] == item[0]:
            visited[row][col] = True
            if len(item) == 1:
                return True
            else:
                item = item[1:]
        else:
            return False
        
        if row < len(board)-1:
            # print(row, col)
            if not visited[row+1][col]:
                tmp = visited[row+1][col]
                # ans = self.helper(board, row+1, col, item, ans, deepcopy(visited)) or ans
                ans = self.helper(board, row+1, col, item, ans, visited) or ans
                visited[row+1][col] = tmp
            if ans:
                return True
        if row > 0:
            if not visited[row-1][col]:
                tmp = visited[row-1][col]
                # ans = self.helper(board, row-1, col, item, ans, deepcopy(visited)) or ans
                ans = self.helper(board, row-1, col, item, ans, visited) or ans
                visited[row-1][col] = tmp
            if ans:
                return True
        if col < len(board[0])-1:
            if not visited[row][col+1]:
                tmp = visited[row][col+1]
                # ans = self.helper(board, row, col+1, item, ans, deepcopy(visited)) or ans
                ans = self.helper(board, row, col+1, item, ans, visited) or ans
                visited[row][col+1] = tmp
            if ans:
                return True
        if col > 0:
            if not visited[row][col-1]:
                tmp = visited[row][col-1]
                # ans = self.helper(board, row, col-1, item, ans, deepcopy(visited)) or ans
                ans = self.helper(board, row, col-1, item, ans, visited) or ans
                visited[row][col-1] = tmp
            if ans:
                return True
            
        return False
```

