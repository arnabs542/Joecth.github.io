---
layout: post
categories: DP Ult.
tag: [] 
date: 2019-09-27

---



## Warm up!

![image-20200928000737476](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5nq5zmcoj30ny132aem.jpg)

![image-20200928000755440](/Users/joe/Library/Application Support/typora-user-images/image-20200928000755440.png)



## 序列型 DP

- 給定一個序列
- 動規方程中的f[i]下標表示**前i個元素 a_0, a_1, ... a_i-1**的某種性質
  - VS 座標型的 f[i] 表示以 a_i為結尾的某種性質
- 初始化中，f[0]表示空序列的性質
  - VS 座標型中的 f[0] 是以 a_0為結尾的子序列性質



### 843 Digital Flip

1. 解法一: 2^N 枚舉
2. 解法二: dp



#### 1 確定狀態

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj6hsj2vwoj30ye0bgq6q.jpg" alt="image-20200928172751126" style="zoom:50%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200928173514213.png" alt="image-20200928173514213" style="zoom:50%;" />



#### 2 轉移方程

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj6ia7y9k6j312q0d213h.jpg" alt="image-20200928174455027" style="zoom:50%;" />



#### 3 初始條件 & 邊界條件 

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200928174859199.png" alt="image-20200928174859199" style="zoom:50%;" />



#### 4 方向

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj6if9ym4ej312k0cmn48.jpg" alt="image-20200928174947545" style="zoom:50%;" />

```python
class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """
    def flipDigit(self, nums):
        # Write your code here
        # return self.my_0928(nums)
        return self.hwd_0928(nums)
        
    def hwd_0928(self, A):
        n = len(A)
        if n <= 1:
            return 0

        f = [[0] * 2 for _ in range(n+1)]
        f[0][0] = f[0][1] = 0   # Initialization
        # first digits: A[0....i-1]
        for i in range(1, n+1):
            for j in range(2):
                f[i][j] = sys.maxsize
                # A[i-1] --> j, should I flip?
                t = 0
                if A[i-1] != j:
                    t = 1   # INDICATOR
                
                # A[i-2] --> k
                for k in range(2):
                    if k == 0 and j == 1:
                        continue
                    f[i][j] = min(f[i][j], f[i-1][k] + t)
        # print(f)
        # CASE:[1,0,0,1,1,1]
        # [[0, 0], [1, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2]]
        return min(f[n][0], f[n][1])
        
    def my_0928(self, nums):
        """
        [   1,  0,              0,  1,  1,  1]
    dp_i         
    to 0    1   min(1, 0) + 0   
    to 1    0   min(1, 0)X + 1
            
        """
        n = len(nums)
        if n <= 1:
            return 0
        dp = [[0] * n for _ in range(2)]
        if nums[0] == 0:
            dp[1][0] = 1
        else:
            dp[0][0] = 1

        for j in range(1, n):
            for i in range(2):
                dp[i][j] = sys.maxsize
                if nums[j] == 0:
                    dp[0][j] = min(dp[0][j-1], dp[1][j-1])
                    # dp[1][j] = min(dp[0][j-1], dp[1][j-1]) + 1
                    dp[1][j] = dp[1][j-1] + 1
                else:
                    dp[0][j] = min(dp[0][j-1], dp[1][j-1]) + 1
                    # dp[1][j] = min(dp[0][j-1], dp[1][j-1]) 
                    dp[1][j] = dp[1][j-1]   # !!!
        # print(dp)
        return min(dp[0][-1], dp[1][-1])
        
```







### 516 Paint House II

1. K 色

#### 2 轉移方程

- 為何加的是cost[i-1] 的? 

  - 因為前i棟房子，最後一棟是 i-1! ，本身這棟房子也記得染

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj6lkaq6xsj31460h0dmp.jpg" alt="image-20200928193823867" style="zoom:50%;" />

  ![image-20200928193913000](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj6ll4x49yj313g0d0jzi.jpg)

- 現在就是k 和 j 不能相等，約束條件相對於就是變了而已；剛剛是 k 和 j   不能是 (0, 1)
  這樣的約束條件可以造出很多很多
  不能是紅、藍呀、藍色下個不能是綠色呀，要會自己變通

  

##### <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200928194431259.png" alt="image-20200928194431259" style="zoom:50%;" />時間優化 !!!

1. 看式子，並展開:
   - 自己把式子展開後再觀察就會發現
2. 畫圖
   - 因為可以把2D的arr 畫一畫，然後自己在推的過程中就會找到哪裡可以優化。
3. ★ 畫小例子 ★
   - 找個n小k小的例子，可以找到



★ ★ 除了自己外的最小值怎算 ?

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200928195213871.png" alt="image-20200928195213871" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj6m2p1es0j31240hggx2.jpg" alt="image-20200928195605730" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj6m3phuxgj30vc0gg79e.jpg" alt="image-20200928195703588" style="zoom:50%;" />

```python
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        return self.my_0928(costs)
        
    def my_0928(self, costs):
        """
        1   knowing i-1 's min cost & color ==> recorded
            sub-problems
        2   transition fn:
            f[i] = min(f[i-1][not my color]) + my cost, lowest cost of prev i houses
        3   check init condition:
                no house: ==> no costs
            check boundary:
                None
        4   ->
        # FAILED CASE: [[1,2,3],[1,4,6]], should be 3, mine is 2 ==> 該紀錄 min_color_2nd
        # 打擂台時的順序?! 
            要先打第二名再打第一名! 順序重要，不然會被 overwritten；不然就是用 if elif 再放空個else的方式。。 WRONG!!!!
            討論!
        """
        if not costs or not costs[0]:
            return 0
            
        m = len(costs)
        k = len(costs[0])
        f = [[0] * k for _ in range(m+1)]
        for c in range(k): # INIT
            f[0][c] = 0
            
        # # O(NxKxK)
        # for i in range(m+1):
        #     for j in range(k):
        #         f[i][0] = min(f[i][1], f[i][2], ... f[i][k-1]) + costs[i][0]
        #         f[i][j] = min()
    
        # O(NxK), 空間可以壓縮成 O(K), 現在是 O(NxK)
        for i in range(1, m+1):
            # minimum = sys.maxsize
            # minimum_2nd = minimum
            # first_min = sys.maxsize
            # second_min = sys.maxsize
            first_min = second_min = -1 # HWD's style!
            for j in range(k):
                # if f[i-1][j] < first_min:   # BUG!
                if first_min == -1 or f[i-1][j] < f[i-1][first_min]:
                    second_min = first_min
                    first_min = j
                # elif f[i-1][j] < second_min:
                elif second_min == - 1 or f[i-1][j] < f[i-1][second_min]:
                    second_min = j
                    
            #   My orig REDUNDANT HERE
            #     # minimum = min(f[i-1][j], minimum)  
            #     if f[i-1][j] < minimum_2nd:
            #         # minimum_2nd = f[i-1][j]
            #         min_color_2nd = min_color
                    
            #     if f[i-1][j] < minimum:
            #         # minimum_2nd = minimum
            #         # minimum = f[i-1][j]
            #         min_color_2nd = min_color
            #         min_color = j
            # print(min_color, min_color_2nd)
            # print(first_min, second_min)
            
            for j in range(k):
                if j != first_min:
                    # f[i][j] = minimum + costs[i-1][j]
                    f[i][j] = f[i-1][first_min] + costs[i-1][j]
                else:
                    # f[i][j] = minimum_2nd + costs[i-1][j]
                    f[i][j] = f[i-1][second_min] + costs[i-1][j]
            # print(f)
        return min(f[-1])
```



### 149 Best Time to Buy and Sell Stock

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj6nwqa05lj30sc0by77n.jpg" alt="image-20200928205933343" style="zoom:50%;" />

#### 法一: 枚舉每天賣時，前面的最低買點

#### 法二: 貪心



### 150 Best Time to Buy and Sell Stock II

- 買賣任意多次，不需要記**已經買了幾次**

- 貪心 -- 只要是上升線就買&賣
  ![image-20200928211245691](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj6oah2pjvj30uu0di75p.jpg)

- 凡是自己想出來的貪心，就一定要證明一下
  - 假設「最優策略不是按我說的這樣」，並且「結果不會更差」
  - 唯一一種不符號這種策略的就是隔多天才賣了的
    - p15-p10 = (p15-p14) + (p14-p13) + ... + (p11-p10)
      如果每天的都大於0，最後兩個加起來是一樣的，所以就改成天天操作的策略吧!
    - 如果有一段是下滑的話，每天操作的貪心都還是比較好的，所以每天操作的結果會更好!



### 150 Best Time to Buy and Sell Stock III

最多只能兩次買賣! 需要紀錄「已經買賣了多少次」

![image-20200928212301077](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj6ol4s4poj30z60dsgrc.jpg)

#### 1 確定狀態

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200928212523217.png" alt="image-20200928212523217" style="zoom:50%;" />

##### 紀錄階段

- ★當天獲利當天結算。

  - 因為如果第十天再結算還要for去知道是在哪天買的

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7fuop9jgj31040hegta.jpg" alt="image-20200929130620760" style="zoom:50%;" />

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7fwik8jaj31080hc46c.jpg" alt="image-20200929130806631" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7fy5gh0nj30zs0h0tb2.jpg" alt="image-20200929130936298" style="zoom:50%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200929131130598.png" alt="image-20200929131130598" style="zoom:50%;" />



#### 2 轉移方程

#### 3 初始條件和邊界情況

##### 初始探討:

​	如果用座標型，f_0 代表就是「第0天結束了」，我就可能已經做了事了，可能在階段1、2或3，麻煩

所以用序列型方便! 「前0天」作初始化

##### 邊界探討

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200929131702636.png" alt="image-20200929131702636" style="zoom:50%;" />



#### 4 計算順序

→

##### 時間 - N

##### 空間 - N --可優化至--> 1



#### Coding!

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200929132406604.png" alt="image-20200929132406604" style="zoom:50%;" />

![image-20200929132527648](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7gel4jigj30ls0iuq8n.jpg)

```

```





### 150 Best Time to Buy and Sell Stock VI

- K 次買賣! --> 不只是五個階段了

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7gjqkmmyj311w0auwie.jpg" alt="image-20200929133025977" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7gkcsiezj311m0a4te8.jpg" alt="image-20200929133101468" style="zoom:50%;" />

- ==> 2k+1 個階段



### 3 初始條件和邊界情況

![image-20200929133325442](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7gmu5xvij311s0hwahd.jpg)



### 4 計算順序

→

##### 時間 - N

##### 空間 - NK --可優化至--> K



### Coding!

![image-20200929133556185](/Users/joe/Library/Application Support/typora-user-images/image-20200929133556185.png)

- 為何早return? 如果K很大、N也很大，會ME，開爆array；所以K一大後，拿貪心就可以了
- 把上一題的 5 都變成 2*K + 1 就都ok了

![image-20200929133843967](/Users/joe/Library/Application Support/typora-user-images/image-20200929133843967.png)



- 所以重點是在「把階段間的關係釐清楚」



#### 滾動!

- i --> now
- i-1 --> old

![image-20200929134225338](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7gw884k7j30nc0iwafy.jpg)

![image-20200929134247959](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7gwl85gfj30na0iywkb.jpg)



## 小結

- 每一步依賴於前一步的「某種狀態」

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7h004nx6j311c0ekamz.jpg" alt="image-20200929134602405" style="zoom:67%;" />





## Appendix

### 最長序列型 DP

- 找最長子序列

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7h4s9yyhj30pm0e2jvf.jpg" alt="image-20200929135040001" style="zoom:50%;" />



- i在j前，以i結尾的，也一定要是最長的
- 要知道以 a_i 結尾的「最長長度」 -- 規模更小的小問題



#### 2 轉移方程

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200929135455220.png" alt="image-20200929135455220" style="zoom:50%;" />

#### 3 初始條件和邊界情況

##### 初始 -- 不用, 空! 

- 如果所有狀態都可以用轉移方程算出，就不需要啦



#### 4 計算順序

→

##### 時間: N^2 --> NLogN

##### 空間: N --> 不可滾動，因為取決前面的所有狀態

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200929135918697.png" alt="image-20200929135918697" style="zoom:50%;" />



### 雙 Array 交換上升



### 俄羅斯套娃

二維是不能直接排序的

- 這些倒排y的數的LIS，就是信封求的最長嵌套，因為同長度是倒著排，同長只能選一個信封! 而達成了同長不能嵌套

- 這題的數據需要 NLogN LIS才能過

  

- ![image-20200929144947550](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7iuo7m3sj30wk0bawk6.jpg)
  透過將長度進行排序，將二維題目降為一維!!!



# 電面

Tech Screen

- CodePad
- CodeIO
- G-Doc

- 有線控的耳機

- repeat、交流，我到哪一步了？
- 考驗聽力、口語，要pardon、can you say that again? 
- 最高標準自我要求
- 自介，開始做題，問組裡做什麼、下一步什麼時候、包裏不是現在問，可催HR去知道下一步是onsite還是怎樣？或加面？控制到很少了後如10個人再onsite
- Data 的coding? 
  - AI 就機器學習相關
- 實踐棧、堆也可能
- 要推遲比較長時間要有理由
- 不會管你背景





## 