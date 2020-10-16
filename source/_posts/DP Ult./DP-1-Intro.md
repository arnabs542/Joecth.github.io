---
layout: post
categories: DP Ult.
tag: [] 
date: 2019-09-16
---



# My

## House Robber

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums : return 0
        if len(nums) == 1: return nums[0]
        # return self.O_1(nums)
        return self.O_SeqDP_2xN(nums)
        return self.O_SeqDP_2x1_arr(nums)
    
    def O_SeqDP_2x1_arr(self, nums):
        n = len(nums)
        
        """
        dp[0]: no-rob
        dp[1]: rob
        """
        dp = [0 for i in range(2)]
        dp[1] = nums[0]
        
        for j in range(1, n):
            prev_norob = dp[0]
            dp[0] = max(dp[0], dp[1])
            dp[1] = prev_norob + nums[j]
            # print(dp)
        return max(dp)
        
    
    def O_SeqDP_2x1(self, nums):
        n = len(nums)
        norob = 0
        rob = 0
        
        for j in range(n):
            prev_norob = norob
            norob = max(norob, rob)
            rob = prev_norob + nums[j]
        return max(norob, rob)
    
    def O_SeqDP_2xN(self, nums):    # ==> 3xN
        """
        # dp[0][j] up to jth house, no-rob, max profit
        # dp[1][j] up to jth house, rob, max profit
        """
        n = len(nums)
        dp = [[0] * n for i in range(2)]
        # print(dp)
        
        for j in range(n):
            dp[0][j] = max(dp[0][j-1], dp[1][j-1])
            dp[1][j] = dp[0][j-1] + nums[j]
        
        # print(dp[-1])
        return max(dp[-1])  # 肯定至少要抢一天
        return max(dp[:][-1])
        return max(dp[0][-1], dp[1][-1])
    
    def O_1(self, nums):
        n = len(nums)
                
        dp = [nums[0], max(nums[0], nums[1]), 0]
        if n == 0: 
            return 0
        elif n <= 2:
            return dp[n-1]
        
        for i in range(2, n):
            dp[i%3] = max(dp[(i-2)%3]+nums[i], dp[(i-1)%3])
        
        return dp[(n-1)%3]
        
    def O_N(self, nums):
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]
        elif n == 2: return max(nums[0],           nums[1])
        elif n == 3: return max(nums[0] + nums[2], nums[1])

        # up to ith house, maximum $ I can get
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # dp[2] = max(dp[0] + nums[2], dp[1]) 
                    
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]
    
    
    def rob_old(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0]+ nums[2], nums[1]) 
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        dp[2] = max(dp[0]+ nums[2], dp[1])
        
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
        return dp[i]
            
```



# 概念們

### Q: 金字塔

##### 給你下面的數字金字塔, 你需要從頂部走到底部, 在這個過程中你途徑的數字之和最大是多少?

```
        7 
       / \
      3   8
     / \ / \
    8   1   0 
   / \ / \ / \
  2   7   4   4
 / \ / \ / \ / \  
4   5   2   6   5 
```

- 如何編程實現？(假設N為金字塔的層數)
  - [x] Recursion - 遍歷所有的路徑，找出最大值，時間複雜度 O(2^N)
  - [ ] Greedy - 每次都走更大的點，時間複雜度 O(N^2)
  - [x] DP- O(N^2)

### Q: 2D Matrix 

##### 給定一個矩陣網路，機器人左上走到右下不可退，哪個時間更少時間？

- [x] 求有多少種方式可以走到右下角 ==> 如果用DP，可以把指數複雜度變polynomial!
- [ ] 輸出所有走到右下角的路徑
- [ ] 需要花費同樣的時間



### Q: 經典背包

##### 有一些物品，每個有一定的重量和價值。給一個背包，它的裝載重量有限。我應該用什麼策略裝物品才能拿走最大的總價值？

- [ ] 按照價值從大到小排序，能拿就拿
- [ ] 按照重量從大到小排序，能拿就拿
- [ ] 計算每個物品的性價比，按照性價比從大到小排序，能拿就拿
- [x] 以上都不對

> 这是很经典的一类动态规划问题, 资源分配型的背包问题. 对于ABC选项我们可以举一个例子看看。
> A.我们一个背包装载重量是10，有三个物品，重量分别为5、4、7，价值分别为6、4、9，按照我们的策略先拿价值高的物品，拿了第三个物品后，我们的背包就无法在放入其他物品了。但是我们可以发现如果我们拿第一个和第二个物品，我们可以获得更大的价值。同理也可以举出先拿价值小的策略的反例。
> B.我们一个背包装载重量是10，有三个物品，重量分别为9、4、3，价值分别为1、5、10，按照我们的策略先拿重量高的物品，拿了第一个物品后，我们的背包就无法在放入其他物品了。但是我们可以发现如果我们拿第二个和第三个物品，我们可以获得更大的价值。同理也可以举出先拿重量小的策略的反例。
> 有同学就会有疑问了，我们为什么不按照性价比来拿呢，那么我们来看一下C选项，如果我们一个背包装载重量是10，有三个物品，重量分别为9、4、6，价值分别为20、8、13，我们按照性价比排序，性价比最高的是第一个物品，我们按照策略先拿第一个物品，然后背包不能放入其他物品，其实我们可以发现二三两个物品的价值是超过第一个物品的，我们可以获得更大的价值。同理也可以举出先拿价值小的策略的反例。
> 这样一个问题，贪心求的只是局部最优解，这一题中无法得到全局最优解，所以我们需要用到动态规划。动态规划的做法我们会在后面的章节讲到，准备感受动态规划的魅力吧!



## What ?

- 一般就是给個「最優解」或是「方式數」

- <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj0xwpxfnvj30ss0hqgv5.jpg" alt="image-20200923221204941" style="zoom:50%;" />



### Q: Coins Change

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj0yex7hc4j314c0kkwx4.jpg" alt="image-20200923222934441" style="zoom:50%;" />



#### DFS -- 爆棧

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        # return self.helper_dfs_0923(coins, amount)
        ans = self.helper_dfs_0923(amount) # TLE on lintcode, but 2000ms AC here
        return ans if ans != sys.maxsize else -1
    
    # @lru_cache
    # def helper_dfs_0923(self, coins, amount):
    @lru_cache(maxsize=None)    # ==> 只給到996次, 爆棧
    def helper_dfs_0923(self, amount):
        if amount == 0:
            return 0
        
        res = sys.maxsize
        for coin in self.coins:
            if amount >= coin:
                # res = min(self.helper_dfs_0923(coins, amount-coin) + 1, res)
                res = min(self.helper_dfs_0923(amount-coin) + 1, res)
        return res
```



#### DP



##### 成份一: 確定狀態

- 最後一步！
- 子問題！



##### 成份二: 轉移方程

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj10x9gsptj315a0eq7fn.jpg" alt="image-20200923235619275" style="zoom:50%;" />



##### 成份三: 初始條件(0時候) & 邊界情況 (上下都不越界)

![image-20200924001745796](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj11jg15bnj30ze0gwdpz.jpg)



##### 成份四: 計算順序？

- 小到大 > 大到小，一般情況
- 原則: 當要算左邊時，右邊都已經算過了! 

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj11llf83aj314k0c8dkx.jpg" alt="image-20200924001950739" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj11n8e6kbj310q0ikjw8.jpg" alt="image-20200924002125288" style="zoom:50%;" />

- 多快? ==> 27* 3

  任何一個狀態只算了一次！

  ![image-20200924092101595](/Users/joe/Library/Application Support/typora-user-images/image-20200924092101595.png)



##### Coding!

```python
    def coinChange(self, coins, amount):
        # write your code here
        self.coins = coins
        # return self.helper_dfs_0923(coins, amount)
        # return self.helper_dfs_0923(amount) # TLE
        return self.helper_dp_0923(coins, amount)
    
    def helper_dp_0923(self, A, M):
        f = [0] * (M+1)
        n = len(A)
        f[0] = 0
        for i in range(1, M+1):
            f[i] = sys.maxsize
            # last coin A[j]
            # f[i] = min{f[i-A[0)+1, ....,f[i-A[n-1]]+1}
            for j in range(0, n):
                if i >= A[j] and f[i-A[j]] != sys.maxsize:
                    f[i] = min(f[i-A[j]] + 1, f[i])
            # print(f)
        if f[M] == sys.maxsize:
            f[M] = -1
        return f[M]
```





Onsite



## 計數型DP

### Q: 機器人走路 -- 再聊加法原理

- 確定狀態
  - 最後一步
    - 無論機器人用何方式到達右下角，總有最後挪動一步:
      - 右
      - 下
    - 就加法原理，原則為，當計數型DP時，常使用此思維
      - 無重覆
      - 無遺漏
  - 子問題!
- 轉移方程
  - 上面來跟左邊來
- 初始條件和邊界情況
  - f 0 0 = 1
  - i==0時和j==0時只有單邊來
- 計算順序
  - 是因為「現在要算的需要之前的」



## 存在型DP

### 116 Jump Game

青蛙從0跳到最後一塊石頭

1. 確定狀態

   - 要可以到i ==> f[j] 表示青蛙能否跳到石頭 j

   - 子問題 ↑

     

2. 設 f[i] 表示青蛙能不能跳到石頭 j 

   ![image-20200924195854904](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj1zoga968j311w0fsago.jpg)

- 最值型

  - Min & Max

- 計數型

  - +

- 存在型 (可行性型)

  - Or , And

    

3. 初始條件和邊界情況

   - 初始條件: f[0] = True，因為一開始就在這

   - 邊界問題:  沒有

     

4. 計算順序

   - 小到大，左到右
   - 時間複雜度: O(N^2) ==> **又要枚舉 j,  又要枚舉 i** 
   - <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200924200323268.png" alt="image-20200924200323268" style="zoom:50%;" />

```python
    def canJump(self, A):
        # write your code here
        """
        1 final step 
            fr prev loc i, and i + A[i] >= X
          so, sub-problem
          
        2 transition fn: f[j] = OR(f[i] and i+A[i] >= j)
        3 boundary: f[0] = True, no OOR
        4 ->
        """
        
        n = len(A)
        f = [False] * n
        f[0] = True
        for j in range(1, n):
            for i in range(j):
                # f[j] = 
                if f[i] and i + A[i] >= j:
                    f[j] = True
                    break
        return f[-1]
```



## DP時間複雜度關聯性

1. 狀態的數量

2. 初始態邊界的數量

   > 通常来说, 动态规划的时间复杂度 = 状态数 * 状态转移代价。
   > 计算顺序是从前往后或者从后往前并不会影响动态规划的时间复杂度，但是在某些情况下会影响计算结果的正确性，初始态边界的数量只会影响初始化时间复杂度，而这一部分的时间复杂度是很低的，所以一般情况下动态规划的时间复杂度不会考虑这一部分。



## Sum Up

1. 確定狀態
   - 最後一步
   - 子問題
2. 轉移方程
   - 最值 min, max
   - 方案數 +
   - 可行數 or, and

3. 初始條件和邊界情況
   - 細心、考慮周全
4. 計算順序
   - 利用之前的計算結果



## FQA

- 涵蓋所有動規考題
  - 是
- 常見動規類型
  - [x] **座標型 20% -- 機器人走路**
  - [ ] **序列型 20% -- f[1] 也是有兩個，但如果說「前幾個」就好思考**
  - [ ] **划分型 20%**
  - [ ] **區間型 15%**
  - [x] 背包型 10%
  - [x] 最長序列型 5%
  - [ ] 博奕型 5%
  - [ ] 綜合型 5%
    - 區間博奕

- 時、空優化
  - 滾動
  - 如何降維
- DP
  - 打印路徑

- 變種突破
- 不知道就是不知道了很難臨時搞



<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200924215239461.png" alt="image-20200924215239461" style="zoom:50%;" />



### Q: 金字塔 -- 解

在金字塔的頂端，每次都可以選擇往左下或右下走，每次

比dfs 高效很多!!!

- DFS -- 有三條路徑可以走到 7 ，當金字塔更大，要走下去路徑數就是個指數級別增加，取決於路徑數，--> 指數級別  --> 2^N

- DP -- 把子問題的狀態保存下來了! 防多次的遍歷，跟狀態數相關，這邊就是點的個數，兩個for遍歷所有狀態，把轉移方程填到for循環裡計算，
  兩個for外計算答案 --> NxN

  並沒有所有路徑都走一遍，但卻計算了所有的**可能性**；已經保存了最優解，用來去更新 7 、跟-2的最優解；
  **把局部的最優解放到了子問題所代表的狀態上面，用狀態代表路徑他們的最優解，然後我們不斷進行轉移**

##### Steps

1. dp[i, j] = 走到 i, j這點時的最大財富值

2. 金字塔col不清晰。斜著來, 通过一個節點寫出
   ![image-20200924221230404](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj23jf7sgtj310w0ik11x.jpg)

   

3. 初始化，這題比較easy -- dp[1, 1] = 3

   當下標不合法，就是不取!

4. 最後就是第四層找一個



<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200924222442700.png" alt="image-20200924222442700" style="zoom:50%;" />



## Maximum Product Subarray

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj38ydsqp5j312a0eqjzf.jpg" alt="image-20200925220522498" style="zoom:50%;" />

