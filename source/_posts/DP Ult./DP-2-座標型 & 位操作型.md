---
layout: post
categories: DP Ult.
tag: [] 
date: 2019-09-27

---



## Warm up!







## 座標型 DP

數組下標 i, j 就是座標 i, j 

### Unique Paths II - w/ 障礙物



<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200927172341608.png" alt="image-20200927172341608" style="zoom:50%;" />

```python
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        # return self.helper_0927(obstacleGrid) # I prefer mine. 
        return self.my_linghu_0927(obstacleGrid)
        
    def my_linghu_0927(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0:
            return 0
            
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]
    
    def helper_0927(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        
        for j in range(1, n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j-1]
            else:
                break
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
            else:
                break            
        # print(dp)
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[-1][-1]
```



## 序列型 DP

### 515 Paint House

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5ct6r4dbj311c0i8te3.jpg" alt="image-20200927174959814" style="zoom:50%;" />



#### 不想管什麼紅藍綠

記錄了油漆前N-1棟房子的最小花費的話，仍是不夠因為不知道前一棟的顏色。

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5ejfkcs6j30sw0emwjd.jpg" alt="image-20200927184949048" style="zoom:50%;" />

```python
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        n = len(costs)
        if n == 0:
            return 0
        dp = [[0] * n for _ in range(3)]
        for i in range(3):
            dp[i][0] = costs[0][i]
        
        for j in range(1, n):
            # dp[0][j] = min(dp[1][j-1], dp[2][j-1]) + costs[j][0]
            for i in range(3):
                dp[i][j] = min(dp[(i+1)%3][j-1], dp[(i+2)%3][j-1]) + costs[j][i]
         
        # return min(dp[:][-1]) #INVALID
        return min(color[-1] for color in dp)
```

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5fcsx44dj30rw0da78z.jpg" alt="image-20200927191802924" style="zoom:50%;" />



## 劃分型 DP

### 512 Decode Ways

從德軍獲得密碼

dfs 硬搜也ok... 

知道最後一段後，需要知道數字串前n-1和n-2個字符的解密方式數

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5fiqwvdrj30s408ugr8.jpg" alt="image-20200927192345919" style="zoom:50%;" />



```python
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        # return self.helper_0927(s)
        # return self.helper_0927_neat(s)
        return self.hwd_0927(s)
    
    def hwd_0927(self, s):
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i >= 2 and s[i-2] == '1'or s[i-2] == '2' and s[i-1] <= '6':
                dp[i] += dp[i-2]
        return dp[-1]
            
        
    def helper_0927_neat(self, s):
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1       # VS Line33!..  是因為設為0的話 後面會不對… 所以這樣設
        dp[1] = 1 if s[0] != '0' else 0
        if dp[1] == 0:
            return 0
            
        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            # if 10 <= int(s[i-1-1:i-1+1]) <= 26:
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
        
    def helper_0927(self, s):
        n = len(s)
        if n == 0:
            # return 1      # EDGE CASE
            return 0
            
        dp = [0] * n    # till ith pos, the max ways
        if s[0] == '0':
            return 0
        dp[0] = 1
        
        if n == 1:
            return dp[0]
        
        if s[1] != '0':
            dp[1] += 1
        if 10 <= int(s[:1+1]) <= 26:
            dp[1] += 1          # OOR
        
        for i in range(2, n):   # sub-problem, 
            # dp[i] = dp[i-1] + dp[i-2]       # conditoinally
            if s[i] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
        # print(dp)
        return dp[-1]
```



- 劃分型用了序列型的思想，但是多了個「分段」，要討論「最後的一段」



## 座標型 DP

以 i, j結尾

### 110 Minimum Path Sum

- 從上面不然就是左邊過來的

- 不等於 unique path (那是求方式數)

```python
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        # return self.helper_0927(grid)
        return self.hwd_0927(grid)
        
    def hwd_0927(self, grid):    
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                    continue
                dp[i][j] = sys.maxsize
                if i > 0:
                    # dp[i][j] = dp[i-1][j] + grid[i][j]
                    # dp[i][j] = min(dp[i-1][j], dp[i][j]) + grid[i][j]   # BUG!!!
                    dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j-1] + grid[i][j], dp[i][j])
        # print(dp)
        return dp[-1][-1]
        
    def helper_0927(self, grid):    
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[0][j] = dp[0][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][0] = dp[i-1][0] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+ grid[i][j]
        print(dp)
        return dp[-1][-1]
```

- 如果沒有限制只能向下跟向右話就是只能蒐



> - 为什么移动方向不是向右或者向下的话，只能用搜索不能用dp来做？
>
>   - 如果是几个方向都可以走, 那么就会违背动态规划的 无后效性原则.
>
>     **无后效性原则**: 已经被计算出来的状态不受那些未被计算出来的状态的影响.



#### 路徑打印

- 動態的選擇中，是有個來源的，所以最後可以去回溯

- 但如果是順的話，不行，因為這樣就成了 遞歸了
- 肯定是「存在性」和「最值」；「方案數」肯定不在這之內的

```python
    def minPathSum(self, grid):
        # write your code here
        # return self.helper_0927(grid)
        # return self.hwd_0927(grid)
        return self.hwd_0927_print_path(grid)
        
    def hwd_0927_print_path(self, grid):    
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        pi = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                    continue
                dp[i][j] = sys.maxsize
                if i > 0:
                    # dp[i][j] = dp[i-1][j] + grid[i][j]
                    # dp[i][j] = min(dp[i-1][j], dp[i][j]) + grid[i][j]   # BUG!!!
                    dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j])
                    if dp[i][j] == dp[i-1][j] + grid[i][j]:
                        pi[i][j] = 0
                if j > 0:
                    dp[i][j] = min(dp[i][j-1] + grid[i][j], dp[i][j])
                    if dp[i][j] == dp[i][j-1] + grid[i][j]:
                        pi[i][j] = 1
        # print(dp)
        path = [[0] * 2 for _ in range(m+n-1)]
        i = m - 1
        j = n - 1
        for p in range(m+n-2, -1, -1):
            path[p][0] = i
            path[p][1] = j
            if pi[i][j] == 0:
                i -= 1
            else:
                j -= 1
        
        for p in range(m+n-1):
            print("({}, {}): {}".format(path[p][0], path[p][1], grid[path[p][0]][path[p][1]]))
        
        return dp[-1][-1]
```

Input

```
[[1,5,7,6,8],[4,7,4,4,9],[10,3,2,3,2]]
```

Your stdout

```
(0, 0): 1
(1, 0): 4
(1, 1): 7
(2, 1): 3
(2, 2): 2
(2, 3): 3
(2, 4): 2
```

Output

```
22
```

Expected

```
22
```



#### 空間優化  easy





### 553 Bomb Enemy

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5idx351jj30qu0bwn0p.jpg" alt="image-20200927210251313" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5if1cp3xj30qi0cs41z.jpg" alt="image-20200927210359889" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5igjyxtzj30rc0cm42x.jpg" alt="image-20200927210525251" style="zoom:50%;" />



★ 需要注意的是 Right 及 Left 時候，他們的依賴得先出來

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5ijekw5cj30qc098goi.jpg" alt="image-20200927210811516" style="zoom:50%;" />

- Notice: You can only put the bomb at an empty cell.

```python
class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
            
        up = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                up[i][j] = 0
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == 'E':
                    up[i][j] += 1
                if i > 0:
                    up[i][j] += up[i-1][j]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                down[i][j] = 0
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == 'E':
                    down[i][j] += 1
                if i < m-1:
                    down[i][j] += down[i+1][j]
        
        for j in range(n):
            for i in range(m):
                left[i][j] = 0
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == 'E':
                    left[i][j] += 1
                if j > 0:
                    left[i][j] += left[i][j-1]
        
        for j in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                right[i][j] = 0
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == 'E':
                    right[i][j] += 1
                if j < n-1:
                    right[i][j] += right[i][j+1] 
        
        print(up)
        print(down)
        print(left)
        print(right)
        
        g_max = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    cur = up[i][j] + down[i][j] + left[i][j] + right[i][j]
                # elif grid[i][j] == 'E':
                #     cur                
                    g_max = max(g_max, cur)
        return g_max
```



### 總結

- 給定輸入為序列或grid
- 以 i j 結尾的某性性質
- 滾動
- 打印路徑



## 位操作 DP

- &, |, ^, !

- 逐位操作

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5jp9jjy2j30ny0aemz8.jpg" alt="image-20200927214825046" style="zoom:50%;" />

### 664 Counting Bits

![image-20200927232840980](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5mlmxpouj30tm0am77h.jpg)

![image-20200927233046018](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5mnta6gcj30ti0eetdx.jpg)

![image-20200927233055808](/Users/joe/Library/Application Support/typora-user-images/image-20200927233055808.png)

