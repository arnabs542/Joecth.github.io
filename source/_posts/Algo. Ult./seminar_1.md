---
layout: post
categories: AlgoUlt.
tag: []
date: 2019-05-２３

---



## 暴力: 1835, 1827 停在原地的方案數

## 1835 停在原地的方案數 I

![image-20200526095155742](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5m5otwomj31ee0sekgd.jpg)

![image-20200526095237745](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5m6bmw5ij31em0sgh7a.jpg



![image-20200526095300143](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5m6p6z2kj31eg0nekao.jpg)

- DFS: 指數級, O(3^steps)

- DP: O(position*step); O(step^2), 

  - ```
    dp[pos][steps]
    ```

```python
        # write your code here
        return self.dp_MLE(steps, arrLen)
        return self.dp(steps, arrLen)
    # def dfs(self, steps, arrLen):
    
    def dp_MLE(self, steps, arrLen):
        n = arrLen
        dp = [[0 for _ in range(n)] for _ in range(steps+1)]
        dp[0][0] = 1
        M = 10**9 + 7
        
        # for k in range(1, steps//2+1):
        #     for i in range(n):
        for k in range(1, steps+1):
            for i in range(0, n):
                if i == 0:
                    dp[k][i] = dp[k-1][i] + dp[k-1][i+1]
                elif i == n-1:
                    dp[k][i] = dp[k-1][i-1] + dp[k-1][i]
                else:
                    dp[k][i] = dp[k-1][i-1] + dp[k-1][i] + dp[k-1][i+1]
        
            dp[k][i] %= M
        return dp[steps][0]        
        
    def dp(self, steps, arrLen):
        # VIDEO:
        #     https://youtu.be/WiYfBPmhRDk?t=895
        
        # dp[i][j] means @ i-th round, at j-th pos
        # max steps == 500, means
        # dp[250][250] = 1
        # dp[251][249] = dp[250][248, 249, 250]
        # dp[252][248] = dp[251][247, 248, 259]
        
        n = arrLen
        
        dp = [[0 for _ in range(steps//2 + 2)] for _ in range(steps+1)]
        dp[0][0] = 1
        M = 10**9 + 7
        
        # for k in range(1, steps//2+1):
        #     for i in range(n):
        for k in range(1, steps+1):
            for i in range(0, steps//2+1):
                if i == 0:
                    dp[k][i] = dp[k-1][i] + dp[k-1][i+1]
                elif i == n-1:
                    dp[k][i] = dp[k-1][i-1] + dp[k-1][i]
                else:
                    dp[k][i] = dp[k-1][i-1] + dp[k-1][i] + dp[k-1][i+1]
        
            dp[k][i] %= M
        return dp[steps][0]
```



## 156 合併區間

只是個引子?! 

- 排序、priority queue、掃描線 skyline
- 一般start排序，只有会议室是用end排序



## 1879 兩數之和



## 1563 目的地的最短路徑

- BFS: 
  1. 最短路徑
  2. 分層遍歷
  3. 拓樸排序 (有前置要求的遍歷)



- BFS or DFS ?!
  - DFS: 遞歸、棧、可能 stack overflow
  - BFS: Queue



- DFS:
  1. 所有方案

![image-20200526104615664](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5nq3o73mj31gs0t67g0.jpg)

![image-20200526104952612](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5ntvcuuoj31gw0r6n7l.jpg)

```python
from collections import deque
class MapType:
    ROAD = 0
    WALL = 1
    DESTINATION = 2

DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# (x, y) ==> x*i + y In Other languages

class Solution:
    """
    @param targetMap: 
    @return: nothing
    """
    def shortestPath(self, targetMap):
        # Write your code here
        if not targetMap: return -1
        
        Q = deque()
        visited = set()
        Q.append((0, 0))
        visited.add((0, 0))
        step = 0
        
        while Q:
            for _ in range(len(Q)):
                x, y = Q.popleft()
                # visited.add(next_x, next_y) # ?! V.S. Line39
                # [0,0]
                # [0,1], [1,0]
                # [0,2], [1,1], [2,0], [1,1]，[1,1]會被重覆放，就不是一個 O(N)了，所以必須放在下面
                
                if targetMap[x][y] == MapType.DESTINATION:
                    return step
                        
                for direction in DIRECTIONS:
                    next_x = x + direction[0]
                    next_y = y + direction[1]
                    if self.is_valid(next_x, next_y, targetMap, visited):
                        Q.append((next_x, next_y))
                        visited.add((next_x, next_y))
            
            step += 1
        return -1
        
    def is_valid(self, x, y, targetMap, visited):
        if x < 0 or y < 0 or x >= len(targetMap) or y >= len(targetMap[0]):
            return False
        if (x, y) in visited:
            return False
        if targetMap[x][y] == MapType.WALL:
            return False
        return True
        
        
```

![image-20200526110735910](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf5ocag5joj31260aateb.jpg)



## 1833 pen box  --- 56 兩數之和 + 151 Stock III

- 两個不重疊的區間問題，用隔板思考, 同Stock iii

```python
class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    # # write your code here
    # # 找有效區間: 2 pointer
    # # 找最短有效后間: 打擂台 min_len = sys.maxsize; min_len = min(min_len, now_len)
    # # 枚舉隔板位置, 左半部分最短有效區間 + 右半部分最短有效區間
    
    # # O(N)
    # min_left[i]: [0:i] 前i個元素組成的list最短有效區間長度
    # min_right[i]: [i:n-1]第i個元素之後的list最短有效區間長度
    
    # # O(N) ↑結合上面那個 O(N)
    # min_len = sys.maxsize
    # for 隔板位置 in range(n):
    #     min_len = min(min_len, min_left[隔板位置] + min_right[隔板位置+1])
        
    # i = t+1, 相較於 i=t，最短的有效區間長度變小了，代表目前這個點一定在有效區間中
    # min_left[t+1] = min(min_left[t], 右針在t+1的有效區間的長度)
    
    # 一步一步移右指針
    #     如果區間和 > target:
    #         左指針右移
        
    #     if now_sum != target:
    #         left_min[right] = 之前的最短有效區間的長度
        
    #     if now_sum == target:
    #         打擂台
    #         left_min[right] = min(之前的最短有效區間長度，當前區間長度)
            
    def minimumBoxes(self, boxes, target): # 前提：都正數
        n = len(boxes)
        if n == 0:
            return -1
        left_min = self.get_minimum_valid_length(boxes, target)
        # [1,2,3,4,5,6], target=5
        # left_min = [M,M,2,2,1]
        
        boxes = boxes[::-1] # 外面進來的 boxes 並沒有被改掉，不用擔心, 要注意會發生變化的時候或不會發生的時候
        right_min = self.get_minimum_valid_length(boxes, target)
        right_min = right_min[::-1]
        # [6,5,4,3,2,1], target=5
        # right_min = [M,1,1,1,1,1,M]
        # [1,1,1,1,1,M]
        
        ans = sys.maxsize
        for i in range(n-1):
            ans = min(ans, left_min[i]+right_min[i+1])
        if ans == sys.maxsize:
            return -1
        return ans
        
        
    def get_minimum_valid_length(self, boxes, target):
        # 當前區間和
        now_sum = 0
        n = len(boxes)
        left_min = [sys.maxsize] * n
        
        left = 0
        for right in range(n):
            now_sum += boxes[right]
            while now_sum > target:
                now_sum -= boxes[left]
                left += 1
                
            """!!! 防OOR """ 
            if right == 0:
                if now_sum == target:
                    left_min[right] = 1
                else:
                    continue
            
            if now_sum != target:
                left_min[right] = left_min[right - 1]
            if now_sum == target:
                left_min[right] = min(left_min[right - 1], right - left + 1)
        return left_min
```









# 數據範圍思考

- 如何接水

> ##### [单选题]一般评测机1s能运算多少次
>
> A.10^4-10^631.43% 选择
>
> B.10^7-10^942.86% 选择
>
> C.10^10-10^1225.71% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 我们一般认为如果最终的运算次数达到10^7-10^9就可能会超时，但是达到更大的如10^10-10^12次的计算次数时就可能会超时。比如n=10^3时，时间复杂度为O(n^2）复杂度的算法就一定不会超时，但是时间复杂度为O(N^3)复杂度的算法就大概率会超时。



> ##### [单选题]如果一个数组长为10^5，那么以下哪种算法一定会超时？
>
> A.双指针0.00% 选择	N
>
> B.前缀和2.33% 选择	N
>
> C.一维dp13.95% 选择	N
>
> D.枚举数组中的所有子区间进行O(1)判断79.07% 选择	N^2 > 10^9 必超時
>
> E.在数组中二分查找n次4.65% 选择	NlogN
>
> F.这都是些啥算法qaq0.00% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是D
>
> **正确答案:**D
>
> **解析:**
>
> 数组中的子区间个数为O(N^2)级别，因此，即使判断的时间复杂度为O(1), 总时间复杂度仍然是O(N^2). 而10^10以上级别的时间对于评测机来说需要运行的时间非常长，一定会超出时间限制。



## Analyzation

- n = 10^4 、 10^5
  - O(n) ==> 雙指針？前綴和？遍歷？DP?
  - O(nlogn) ==> 排序？二分？
- n = 10^3
  - O(n^2) ==> 二維數組？雙重循環？二維dp?
- n = 10^2
  - O(n^3) ==> 三重循環？e.g. Stone game 區間DP
- n = 10
  - O(2^n), O(n!) ==> dfs暴力？	2^n ~= 10^3, 10^6
- n = 10^9
  - 別打算開數組存或 O(n) 複雜度



## 159. 尋找旋轉排序數中的最小值 - 無重複值



## 183. 木材加工

```python
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if not L: 
            return 0
        # start, end = max(L), sum(L)
        start, end = 1, max(L)
        while start+1 < end:
            mid = start + (end - start)//2
            if self.get_pieces(L, mid) < k:
                end = mid
            else:   # 表示可以切出k段，就加長再試試
                start = mid
        
        if self.get_pieces(L, end) >= k:
            return end
        if self.get_pieces(L, start) >= k:
            return start
        return 0
        
    def get_pieces(self, L, length):
        count = 0
        for i in range(len(L)):
            count += L[i]//length
        return count
            
        
        
    #     if not L:
    #         return 0

    #     start, end = 1, max(L)
    #     while start + 1 < end:
    #         mid = (start + end) // 2
    #         if self.get_pieces(L, mid) >= k:
    #             start = mid
    #         else:
    #             end = mid
                
    #     if self.get_pieces(L, end) >= k:
    #         return end
    #     if self.get_pieces(L, start) >= k:
    #         return start
            
    #     return 0
        
    # def get_pieces(self, L, length):
    #     pieces = 0
    #     for l in L:
    #         pieces += l // length
    #     return pieces
```



##  62. 搜索旋转排序数组



## 437. 書籍複印

```python
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # return self.copyBooks_old(pages, k)
        if not pages:
            return 0
        # 使用九章算法强化班中讲过的基于答案值域的二分法。 答案的范围在 max(pages)~sum(pages) 之间，每次二分到一个时间 time_limit 的时候，用贪心法从左到右扫描一下 pages，看看需要多少个人来完成抄袭。 如果这个值 <= k，那么意味着大家花的时间可能可以再少一些，如果 > k 则意味着人数不够，需要降低工作量。
        
        # mins
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start)//2
            if self.get_min_required_people(pages, mid) <= k:
                # 人手夠的情況，時間可以再短一點
                end = mid
            else:
                # 人手不夠的情況，時間給得再多一點
                start = mid
                
        # print(start, end)
        if self.get_min_required_people(pages, start) <= k:
            return start
        # if self.get_min_required_people(pages, end) <= k:
        return end
        
    def get_min_required_people(self, pages, time_limit):
        people = 1
        time = 0
        for i in range(len(pages)):
            time += pages[i]
            if time > time_limit:
                # print(pages[i])
                people += 1
                time = pages[i] # CRITICAL!!!
                
        # print(people)
        return people
        
    def copyBooks_old(self, pages, k):
        
        if not pages:
            return 0
            
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            print(start, end)
            mid = (start + end) // 2
            if self.get_least_people(pages, mid) <= k:
                end = mid
            else:
                start = mid
        
        if self.get_least_people(pages, start) <= k:
            return start
            
        return end
        
    def get_least_people(self, pages, time_limit):
        count = 0
        time_cost = 0 
        for page in pages:
            if time_cost + page > time_limit:
                count += 1
                time_cost = 0
            time_cost += page
        print(count+1)
        return count + 1
```



## 949. Fibo II

```python
# import numpy as np 
from copy import deepcopy
MOD = 10000
class Matrix:
    def __init__(self, n, m):
        self.mat = [[0 for j in range(m)] for i in range(n)]
        self.n = n
        self.m = m 

    # A * B  ==> A.__mul__(B)  n*m (x) m*k 
    def __mul__(self, matrix):
        k = len(matrix.mat[0])
        tmp = Matrix(self.n, k)
        for i in range(self.n):
            for j in range(k):
                for t in range(self.n):
                    tmp.mat[i][j] += self.mat[i][t] * matrix.mat[t][j]
                    tmp.mat[i][j] %= MOD 
        return tmp
        
class Solution:
    """
    @param n: an integer
    @return: return an int
    """
    def lastFourDigitsOfFn(self, n):
        # write your code here
        if n == 0: 
            return 0
        # return self.O_N(n)
        # return self.O_logN(n)
        return self.O_logN_tmpl(n)
        
    def power(self, A, k):	# FAST POW
        n = len(A.mat)
        ans = Matrix(n, n)
        for i in range(n):
            ans.mat[i][i] = 1 
        while k > 0:
            if k %  2 == 1:
                ans = A * ans 
            A = A * A
            k //= 2 

        return ans    
        
    def O_logN_tmpl(self, n):    
        if n == 0:
            return 0
            
        A = Matrix(2, 2)
        A.mat = [[1, 1], [1, 0]]
        A = self.power(A, n-1)
        
        x = Matrix(2, 1)
        x.mat = [[1], [0]]
        
        ans = A * x
        return ans.mat[0][0]
            
        
    def O_logN(self, n):
        """
        # T = np.array([
        #         [1, 1], 
        #         [1, 0]
        #     ])
        # X = T.copy()
        
        # for i in range(n):
        #     X = np.dot(T, X)
        # for i in range(1, n):     # Should do this D&C
            # X = dot2x2(T, X)
        # return X[0][1]%10000
        # https://www.youtube.com/watch?v=PJT0oqZqixU        
        """
        def dot2x2(A, B):
            # m, n, k = len(A), len(A[0]), len(B[0])
            C = [[0 for _ in range(2)] for _ in range(2)]
            for i in range(2):
                for t in range(2):
                    for j in range(2):
                        C[i][t] += A[i][j] * B[j][t] % 10000
            # C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
            # C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
            # C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
            # C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
            return C
            
        def helper(T, n):
            if n <= 1:
                return T
            X = helper(T, n//2)
            tmp = dot2x2(X, X)
            
            if n % 2 == 1:
                Y = [[1, 1], 
                     [1, 0]]
                return dot2x2(tmp, Y)
            return tmp
            
        T = [[1, 1], 
             [1, 0]]
        RES = helper(T, n)
        # print(RES)
        return RES[0][1] % 10000
    
    def O_N(self, n):
        if n <= 1: 
            return n
            
        f0 = 0
        f1 = 1
        ans = 0
        for i in range(2, n+1):
            ans = f0 + f1
            f0 = f1
            f1 = ans
        return ans % 10000
            
        
```

