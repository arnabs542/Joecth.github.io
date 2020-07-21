---
layout: post
categories: AlgoUlt.
tag: []
date: 2019-05-30
---





## 645. 識別名人

- 其他人他都不認識的，他就是名人
- 最多只會有一個名人，或「不存在」，不會有兩個名人

- 降低兩兩比較的時間！Trick! ==> 
- as 892 Alien Dictionary, as 1836 Reaching Point

```python
"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""
class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # return self.bf_NxN(n)
        return self.O_N(n)
        
    def O_N(self, n):
        # 候選人＝ 0 
        # for 循環遍歷其他的人 (1~n-1): i
        #     if i 認識候選人：
        #         i　不可能是名人
        #     if i 不認識至選人：
        #         候選人不可能是名人
        #         i　可能是名人
        #         ==> 讓 i 成為最後的候選人
        
        # for 所有人判斷該候選人是否是名人
        cand = 0    # candidate
        for i in range(1, n):
            # if Celebrity.knows(i, cand):
            #     cand = cand
            if not Celebrity.knows(i, cand):
                cand = i
        
        for i in range(n):
            if i == cand:
                continue
            if Celebrity.knows(cand, i) or not Celebrity.knows(i, cand):
                return -1
        return cand    
    
    def bf_NxN(self, n):
        # Write your code here
        # for  所有人
        #   判斷這個人是否是名人 ==> for其他所有人看是否其他人認識ｉ、ｉ是否認識其他人 
        for i in range(n):
            is_celebrity = True
            for j in range(n):
                if i == j:
                    continue
                    
                if Celebrity.knows(i, j) or not Celebrity.knows(j, i):
                    is_celebrity = False
            if is_celebrity:
                return i
        return -1
```



## 654. 稀疏矩陣乘法

- 將兩個Matrix 相乘，



1. <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfdpp1hf9gj30qa0c4q4t.jpg" alt="image-20200602095856594" style="zoom:50%;" />

   As Merge 2 sorted array, 雙指針讓兩條的值相等時再相乘

   <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200602100301997.png" alt="image-20200602100301997" style="zoom:67%;" />

   

   Further:

- 現在有兩個向量，非常稀疏，其中假設非0個數為n, 如何 O(n) 時間得到這兩個向量的乘積？

  - 如果是用arr存的話，再怎樣也要O(N)
  - **(Index, val)**; LinkedList存才行  Arraylist<Node> or LinkedList<Node>
    
    - Two pointer method!
- <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfdqlv9hfrj308g08gt9m.jpg" alt="image-20200602103032402" style="zoom:50%;" />
  
- 　給過來的要是Node才有意義，如果是Array的話就沒意義了
  
    

2. PUSH method

```python
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    # 
    def multiply(self, A, B):
        # write your code here
        # return self.BF(A, B)
        return self.two_pointers(A, B)  # optimization 1
        return self.push_model(A, B)    # optimization 2
        
    # PUSH model: 通過原料加到結果裡面
    # 不是對於每個C裡的每個值拿A、B裡的每一個東西，而是看A裡面的每個值會對C裡的
    # 哪些值產生影響
        
    def push_model(self, A, B):
        n = len(A)
        m = len(A[0])
        k = len(B[0])
        
        C = [[0] * k for i in range(n)]
        
        # 如果A中非0元素為常數級別 ==> O(N^2)
        for i in range(n):
            for j in range(m):
                """ 以下兩行為PUSH model的優化 """
                if A[i][j] == 0:    # 但B裡面還是沒有優化到
                    continue
                for t in range(k):
                    C[i][t] += A[i][j] * B[j][t]
        
        return C        
    
    
    def two_pointers_new(self, A, B):
        n = len(A)
        m = len(A[0])
        k = len(B[0])
        
        row_vec = []
        
        
    def two_pointers(self, A, B):
        n = len(A)
        m = len(A[0])
        k = len(B[0])
        
        # 假設 n, m, k 是相同數量級
        # O(n^2)
        row_vector = [
            [
                (j, A[i][j])
                for j in range(m)
                if A[i][j] != 0
            ]    
            for i in range(n)
        ]
        
        # O(n^2)
        col_vector = [
            [
                (i, B[i][j])
                for i in range(m)
                if B[i][j] != 0
            ]    
            for j in range(k)
        ]
        # Java C++ 只能Hashmap套ArrayList
        
        # O(n^2 * O(self.multi()))
        C = [
                [
                    self.multi(row, col)
                    for col in col_vector
                ]
                for row in row_vector
            ]
        
        # C = [[0] * k for i in range(n)]
        return C
        
        # row = [(0,1), (2,3), (3,5)]
        # col = [(1,2), (3,5)]
        
    # O(len(row) + len(col)) ==>  行向量與列向量中非0元素的個數
    # ==> 假設非0元素個數是常數級  ==>  O(1), 如 1000x1000，但只有10、20個有值
    # As Merge Two sorted array
    """
    A = [
            [1,0,0],
            [-1,0,3]
        ]
        
    B = [
            [7,0,0]
            [0,0,0]
            [0,0,1]
        ]
        
    mapping_A:
        0: [0]
        1: [0,2]
            　↑
    
    mapping_B:
        0:[0]
        1:[]
        2:[2]
        　 ↑
    """
    def multi(self, row, col):
        # 雙指針
        i = 0
        j = 0
        ans = 0 # 向量相乘後的結果
        while i < len(row) and j < len(col):
            index1, val1 = row[i]
            index2, val2 = col[j]
            if index1 < index2:
                i += 1
            elif index1 > index2:
                j += 1
            else:
                ans += val1 * val2
                i += 1
                j += 1
        return ans
                
    # PULL model
    def BF(self, A, B):
        m, n, k = len(A), len(A[0]), len(B[0])
        C = [[0 for _ in range(k)] for _ in range(m)]
        
        for i in range(m):
            for j in range(k):
                for t in range(n):
                    C[i][j] += A[i][t] * B[t][j]
        return C
    
    def BF_old(self, A, B):
        n = len(A)
        m = len(A[0])
        k = len(B[0])
        
        C = [[0]*k for i in range(n)]
        for i in range(n):
            for j in range(k):
                # C[i][j] = A[i][t] * B[t][j]
                for t in range(m):
                    C[i][j] += A[i][t] * B[t][j]
        return C
```



## 140. 快速冪

- 求 a**n%b
- 其中 n非常大 (n <= 10**9)
- 如何獲得logn的複雜度？
- 思想：a*^1000 <== (a^500)^2
- a ^ 10000000000 <== a ^ 5000000000 <== 
- 問題規模: n -> n/2 -> n/4 -> n/8 -> n/16
- 討論平方關係：
  - x^(n/2) * x(^n/2): O(N)，只是divide & conquer，但每個還是重複算了
  - x^(n/2) ** 2: O(logN)   思想不同上面的！是真正的切半
- related to 949 fibII、65



## Freq:

----------------- 很常見 

 1. BFS
 2. 模擬(interger -> roman OA)、隱式圖老題 (數獨、word ladder (X)，word break Ⅱ 必須要最優化, dfs暴力指數級，dp(O(N)))、K largest ... (Amazon)

----------------- 比較常見

3. DFS、二叉樹、基礎DP(背包、序列型dp、坐標型dp、雙序列型dp(LCS)、常見的問題(LIS、LPS))、二分答案、前缀和

4. LRU、LFU、雙指針 (Sliding Window), LInkedList (老題、快慢、環、相交點)、Copy Linked List with random pointer、掃描線、單調棧

----------------- 基本不怎麼出現

5. 二分搜索、數據結構(heap, quick select)、比較難的DP(區間DP、概率DP、狀態壓縮DP (TSP)), Union find, sort, trie (quantcast(OA)), segment tree，紅黑樹(G)，dfs非遞歸實現 (樹的非遞歸遍歷)、矩陣快速冪
6. Floyd, dij, spfa



Graph ==> BFS, DFS, targan(Amazon), Union find, dij, Floyd (最小生成樹)

- Find Critical connection (Amazon!) V



A onsite: Stone Game

Word Ladder 2





# Seminar 3

- 



## 1310. 數組除了自身的乘積

1. 左往右，前綴積: prefix[i] = nums[0] * ... * nums[i]
2. 右往左，後綴積: suffix[i] = nums[i] * ... * nums[n-1
3. 遍歷所有位置 outpus[i] = prefix[i-1] * suffix[i+1]

```python
class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        # return self.O_N(nums)
        return self.O_1(nums)
        
    def O_1(self, nums):
        # 從前往後掃，把當前的前綴積放到output中
        # 從後往前掃，把當前的後綴積乘上output[i]
        n = len(nums)
        if n == 0:
            return []
            
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
        
        
    def O_N(self, nums):
        # 1. 左往右，前綴積: prefix[i] = nums[0] * ... * nums[i]
        # 2. 右往左，後綴積: suffix[i] = nums[i] * ... * nums[n-1
        # 3. 遍歷所有位置 outpus[i] = prefix[i-1] * suffix[i+1]
        n = len(nums)
        if n == 0:
            return []
            
        output = [0] * n
        prefix = [0] * n
        suffix = [0] * n
        
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        suffix[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        for i in range(n):
            if i == 0:
                output[i] = suffix[i+1]
                continue
            if i == n - 1:
                output[i] = prefix[i-1]
                continue
            
            output[i] = prefix[i-1] * suffix[i+1]
        return output
```



## 1844. 子數組和為K II

- 為何不能用雙指針？
  - 因為有負數的。。。太慘。。
- 基础版：838子数组和为K
- Follow up: 1507.和至少為K的最短長度

![image-20200604103838917](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfg232v0fqj30wg0eqadb.jpg)



## 1507. 和至少为K的最短长度

![image-20200604105311696](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfg2ia573fj30y80jcn3e.jpg)

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfg2oc4xwbj30im0ictc7.jpg" alt="image-20200604105910757" style="zoom:67%;" />



## 391. 數飛機

- 差分前綴和
- 根據原數組獲得差分數組 ==> 求前綴和
- 什麼是差分數組？

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200604112647832.png" alt="image-20200604112647832" style="zoom:67%;" />



## 194. 寻找单词

1. BF 雙指針

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200604113217218.png" alt="image-20200604113217218" style="zoom:67%;" />

2. 大暴力 2^N 空間

3. hashmap 存所有字母出現的位置
   - o:[2,4,9,15]
   - index = 5
   - 去找下一個o
     - 二分
   - aaaaaaaaaaa
     - a: [1,2,3,4,5,6,7,8,9,10]
     - index = 4
   - O(m x logN x k)
4. 當前字符串的後一個任意字符的位置 ★待學習　



#### Sol 

##### O(N^2) 的預處理，太慢

![image-20200612185220046](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfppb5ahcjj30ry0dcaf6.jpg)



##### O(N) 預處理 by 後往前遞推！

![image-20200612191700269](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpq0quxeuj30ia0kc7be.jpg)

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfppn80qp6j308c03wgmj.jpg" alt="image-20200612190400078" style="zoom: 67%;" />

![image-20200612190519367](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfppol54aej30c600m74i.jpg)



## 946. 233 Matrix

```python

MOD = 10000007
class Matrix:
    def __init__(self, n, m):
        self.mat = [[0 for j in range(m)] for i in range(n)]
        self.n = n
        self.m = m
    
    # A * B ==> A.__mul__(B)    n*m (x) m*k
    def __mul__(self, matrix):
        k = len(matrix.mat[0])
        tmp = Matrix(self.n, k) # TODO:

class Solution:
    """
    @param X: a list of integers
    @param m: an integer
    @return: return an integer
    """
    def calcTheValueOfAnm(self, X, m):
        # write your code here
        if not X and m == 0:    # 特判
            return 0
        # return self.O_NxM_MLE(X, m)
        # return self.O_N_TLE(X, m)
        # return self.O_lgN(X, m)   # TODO ... not OK now
        return self.sol(X, m)
        
    def sol(self, X, m):
        # write your code here
        n = len(X)
        if(n == 0 and m == 0):
            return 0
        if(m == 0):
            return X[n - 1]
        self.n, self.mod = n + 2, 10000007
        A = [[0 for j in range(n + 2)] for i in range(n + 2)]
        for i in range(n + 1):
            A[i][0] = 10
        for i in range(n + 2):
            A[i][n + 1] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                A[i][j] = 1
        tmp = self.power(A, m);
        ans = tmp[n][0] * 23 + tmp[n][n + 1] * 3
        for i in range(1, n + 1):
            ans += tmp[n][i] * X[i - 1]
        return ans % 10000007
        
    def mul(self, A, B):
        tmp = [[0 for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            for k in range(self.n):
                if (A[i][k] == 0):
                    continue
                for j in range(self.n):
                    tmp[i][j] = (tmp[i][j] + A[i][k] * B[k][j]) % self.mod
        return tmp

    def power(self, A, a):
        B = [[0 for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            B[i][i] = 1
        while a > 0:
            if (a % 2 == 1):
                B = self.mul(B, A)
            A = self.mul(A, A)
            a //= 2
        return B

        
    def O_lgN_tmpl(self, X, m):
        pass    # TODO:
    
    
    """
    23      10*A[0][0]+3        10*A[0][1]+3        10*A[0][2]+3
    a1      a1+↑
    a2      a2+↑
    a3      a3+↑
    a4      a4+↑
    """    
    def O_lgN(self, X, m):  # FastPow, Buggy... for m, n and DIM
        n = len(X)
        col = [0] * (n+2)
        col[0] = 23
        
        for i in range(1, n+2-1): #  23
            # print(col)
            col[i] = X[i-1]       #  a1
                                  #  a2
                                  #  a3
                                  #  3
        col[-1] = 3
        print("col: {}".format(col))
        # T : (n+2) x (m+2)
        """""
        doc WRONG!!! ↓  n should be equal to len(vec)
        [   
            [10, 0, 0, 0, 1],
            [10, 1, 0, 0, 1],
            [10, 1, 1, 0, 1],
        ]
        
            CORRECT　↓  for [0,0,3], 2
        [   
            [10, 0, 0, 0, 1],
            [10, 1, 0, 0, 1],
            [10, 1, 1, 0, 1],
            [10, 1, 1, 1, 1],
            [10, 1, 1, 1, 1],            
        ]            
        
        """
        # T = [[0] * (m+2) for _ in range(n+2)]   # WRONG!!!
        T = [[0] * (n+2) for _ in range(n+2)]
        for i in range(n+2):
            T[i][0] = 10
            T[i][-1] = 1
        # print("T: \n{}".format(T))
        
        for i in range(1, n+2):
            for j in range(1, n+2):
                if i >= j:
                    T[i][j] = 1
        print("T OK: \n{}".format(T))

        for j in range(m):
            col = self.transform(T, col)
            col[-1] = 3
            print(col)
            
        return col[-2]
        
    def transform(self, A, vec):    # diff frome general __mul__ 'cause of DIM issue, so better use class template...
        n, m = len(A), len(A[0])
        print(n, m, len(vec))
        k = 1
        C = [0 for j in range(n+1)]

        
        for i in range(n):
            for j in range(m):
                C[i] += A[i][j] * vec[j]
        return C
    
    # def mul(self, A, B):
    #     n, m, k = len(A), len(A[0]), len(B[0])
    #     print(n, m, len(B), k)
    #     C = [[0 for _ in range(k)] for _ in range(n)]
    #     for i in range(n):
    #         for t in range(k):
    #             for j in range(m):
    #                 C[i][t] = A[i][j] * B[j][t]
    #     return C
        
        

    def O_N_TLE(self, X, m):
        n = len(X)
        # T = [[0] * (m+1) for _ in range(n+1)]
        col = [0] * (n+1)
        col[0] = 23
        
        # for j in range(1, m+1):
        #     T[0][j] = 10*T[0][j-1] +  3
        
        for i in range(1, n+1):
            col[i] = X[i-1]
            
        for j in range(1, m+1):
            # print(T)
            for i in range(0, n+1):
                if i == 0:
                    col[i] = 10 * col[i] + 3
                else:
                    col[i] = col[i] + col[i-1]
            
        # print(T)
        return col[n] % MOD
        
    def O_NxM_MLE(self, X, m):
        n = len(X)
        T = [[0] * (m+1) for _ in range(n+1)]
        T[0][0] = 23
        
        for j in range(1, m+1):
            T[0][j] = 10*T[0][j-1] +  3
        
        for i in range(1, n+1):
            T[i][0] = X[i-1]
        
        # print(T)
        for i in range(1, n+1):
            for j in range(1, m+1):
                T[i][j] = T[i-1][j] + T[j][i-1]
        # print(T)
        return T[n][m] % MOD
```



## 前綴和的定義和實現

![image-20200611002631135](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfnnqe58rzj30qg0cg77y.jpg)

![image-20200611002923263](/Users/joe/Library/Application Support/typora-user-images/image-20200611002923263.png)

![image-20200611003241851](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfnnwnq0x7j30ue0eg79y.jpg)

![image-20200611003404254](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfnny2cwesj30ts0cmzmq.jpg)



#### 2D

![image-20200612101348111](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpably4w2j30ue0em44a.jpg)

![image-20200612102108325](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpaj7hx6oj30tu0emqde.jpg)

![image-20200612102132182](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpajm0uz8j30tu0dw0xw.jpg)



#### 動規V.S.前綴和

- 前綴和是一種特殊的動規

- e.g.

  - 打劫房屋

  - 不同路徑2D DP, 也是一種前綴和、DP、

  - 爬樓梯

    - dp = dp[i-1] + dp[i-2]

  - 股票

    - DP思維: dp[i] profit

      - dp[i] = max(dp[i-1], a[i] - min_cost)

    - 前綴思想：

      - 前綴最小值

        Min_price, max_profit

    - 思維路徑：
      - 先想簡單的方法試起
        1. 前綴
           1. 前綴最小、最大
           2. 前綴和
        2. 雙指針
      - 再想進階的辦法
        1. 動規

  - 簡單法做起



