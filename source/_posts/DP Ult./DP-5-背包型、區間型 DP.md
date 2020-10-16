---
layout: post
categories: DP Ult.
tag: [] 
date: 2019-10-10

---



## Warm up!



# 背包 0/1 & 完全 & 優化

### 125 Backpack II

即 0/1 背包，裝最大價值

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjk556frddj31240hs7c2.jpg" alt="image-20201010124808594" style="zoom:50%;" />

之前care過 

1. 能不能
2. 方案數
3. 現在是最大值

#### 1 最後一步 & 子問題

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201010125357138.png" alt="image-20201010125357138" style="zoom:50%;" />



#### 2 轉移方程

- 價值也可以是小數或負數也ok
- 但載重一定要是整數，不然arr開不了，因為下標的問題



#### Coding w/ 路徑打印

```python
        
    def my_1009(self, n, A, V):
        m = len(A)
        # dp means, with previous i items & at most j size, the max value 
        dp = [[0] * (n+1) for _ in range((m + 1))] 
        dp[0][0] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                # if j >= A[i - 1]:
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - A[i - 1]] + V[i - 1])
        return dp[m][n]
    
        
    def hwd_1009(self, n, A, V):
        m = len(A)
        # dp means, with previous i items & exactly j size, the max value 
        dp = [[0] * (n+1) for _ in range((m + 1))] 
        pi = [[0] * (n+1) for _ in range((m + 1))] 
        dp[0][0] = 0
        for j in range(1, n + 1):
            dp[0][j] = -1       # 代表「拼不出來」
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] # Not take 
                pi[i][j] = 0
                # if A[i - 1] > j:  # BUG!!
                # if j >= A[i - 1]: # 雖然 AC，但 邏輯上檢查不完全
                if j >= A[i - 1] and dp[i - 1][j - A[i - 1]] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - A[i - 1]] + V[i - 1])
                    if dp[i][j] == dp[i - 1][j - A[i - 1]] + V[i - 1]:
                        pi[i][j] = 1
    
        res = 0
        j = 0
        # print(pi)
        for w in range(n + 1):
            if dp[m][w] != -1:
                res = max(res, dp[m][w])
                if res == dp[m][w]:
                    j = w
        
        selected = [False] * m
        for i in range(m, 0, -1):
            if pi[i][j] == 1:
                selected[i - 1] = True
                j -= A[i - 1]
            else:
                selected[i - 1] = False
        # print(selected)
        
        for i in range(m):
            if selected[i]:
                print('Item: ', i, ' weight: ', A[i], ' Value: ', V[i])
        return res
        # return res  # SAME as FOLLOWING LINE
        # return max(dp[m])
        # return dp[m][n] # WRONG!!!
```





### 440 Backpack III

完全背包，要注意左上來的已經包含在左邊來的裡了

##### ∞個 for 每種物品

- 我會選「性價比」高的，然後只取它 !!!
  - 很不幸，會是錯的！
    <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjkbwomycxj31100eoqcs.jpg" alt="image-20201010164210993" style="zoom:50%;" />
  - 仍是「貪心思想錯誤」! 仍該用動態規劃來思考!



#### 2 轉移方程

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjkc04dd5gj310k0iidq2.jpg" alt="image-20201010164532441" style="zoom: 50%;" />

##### 優化

1. **畫圖 -- 畫個表格 ==> V！**
2. 小例子 --> 也累
3. 看式子 --> 累



###### ∵

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjkcab777gj30z00ecwld.jpg" alt="image-20201010165519348" style="zoom:50%;" />



###### ∴

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjkcb9jqbwj311y0iktnm.jpg" alt="image-20201010165614668" style="zoom:50%;" />



#### Coding!

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201010165814198.png" alt="image-20201010165814198" style="zoom: 67%;" />



#### 終極優化

→ ，based on 先畫個圖分析

easy

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjkchq00zlj30ig0iogqc.jpg" alt="image-20201010170226916" style="zoom: 67%;" />



​																					**↓ 終極優化**



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjkcjcoh9pj30hi0iijvy.jpg" alt="image-20201010170401214" style="zoom:67%;" />



## 背包總結

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201010170745651.png" alt="image-20201010170745651" style="zoom: 50%;" />



## 拓展

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201010171002524.png" alt="image-20201010171002524" style="zoom: 50%;" />





# 區間型 DP

涉及去頭和去尾，從原來的開始到結尾的，**子區間**!

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjkcs1qh0uj30uy0aqdjr.jpg" alt="image-20201010171222572" style="zoom:33%;" />

### 667  Longest Palindromic Subsequence

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201010171334109.png" alt="image-20201010171334109" style="zoom:33%;" />

#### 1 確定狀態



#### Coding!

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201010235905861.png" alt="image-20201010235905861" style="zoom: 67%;" />



#### 記憶化蒐搜

- 動態規劃編程的另一個選擇，不算是一種新的算法，就只是一種「寫法」
- 之前的dp 一般叫作**遞推 --  Recurrence**, 從簡單開始，逐漸變複雜 -- **自下而上**，總之，遞推本身就是從最簡單的情況，推到最複雜的情況。跟求問題的順序是反過來的，我要的就是f(100)，你給我從0開始推；
- 反之，記憶化蒐索是去找 f(99) -- 是**自上而下的過程**
  - 無法用滾動arr作空間優化
- <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjkoq8j8nzj311o0i4qdf.jpg" alt="image-20201011000548070" style="zoom:50%;" />



##### Coding!

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011001309274.png" alt="image-20201011001309274" style="zoom: 67%;" />



<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011001405561.png" alt="image-20201011001405561" style="zoom: 67%;" />

###### 複雜度分析

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011001606302.png" alt="image-20201011001606302" style="zoom:67%;" />



###### 注意三項

1. 初始化 @ L51
2. 入口 return @ 15
3. 先算遞歸 @ 31~33

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011001933744.png" alt="image-20201011001933744" style="zoom: 67%;" />





### 396 Coins In A Line III -- 區間 + 博奕

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011002023215.png" alt="image-20201011002023215" style="zoom:33%;" />



- 有兩個數字和 --> 都不用記，只要記「差」
- 哪句話看出「區間型」? 如何判斷出?
  - ==> 每次只能取第一個數或最後一個數!
  - 如果是任取，就不會是區間

#### 1 確定狀態

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011004400903.png" alt="image-20201011004400903" style="zoom:33%;" />

- Sy、Sy' 又怎麼知道是多少呢？ --> 這不就是原來面對的「子區間」的一個最大的得分嘛!!
  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjkpwji8q1j310y0ew0y4.jpg" alt="image-20201011004627784" style="zoom: 33%;" />



#### 2 轉移方程

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjkpxncua6j310y0c448u.jpg" alt="image-20201011004731716" style="zoom:50%;" />



#### Coding!

- 融合了區間 + 博奕的時候有兩步可以走，到底走哪一步，取max
- 本來有兩個數字和，我都不用記，就取「差」
- 最後最關鍵的是「相對的數字差」而不是絕對的數值

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011003319755.png" alt="image-20201011003319755" style="zoom: 67%;" />



### 430 Scramble String

- 劈成兩半、再來就是交換
- dfs 天文數字，但至少可做
  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjl3vpfm7ej31140h0k10.jpg" alt="image-20201011085001859" style="zoom:50%;" />

#### 1 確定狀態

- 枚舉S
  - 在什麼地方砍
  - 是不是交換兒子
  - S、T不過都是原來的子區間

##### 子問題

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011085609763.png" alt="image-20201011085609763" style="zoom:50%;" />

###### 代數法降維

1. 1有等號

   ![image-20201011085749889](https://tva1.sinaimg.cn/large/007S8ZIlgy1gjl43sffhij30vi0giqaz.jpg)



#### 2 轉移方程

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjl4b6bn19j310w0i0qbo.jpg" alt="image-20201011090455094" style="zoom:50%;" />



#### 4 計算順序

###### 不可滾動數組，因為可能用到之前所有的



#### Coding!

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011091502028.png" alt="image-20201011091502028" style="zoom: 67%;" />



<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011091559104.png" alt="image-20201011091559104" style="zoom: 67%;" />

- 14行應該要是 bolean



#### 記憶化搜索

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011092308508.png" alt="image-20201011092308508" style="zoom: 67%;" />



<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011092440733.png" alt="image-20201011092440733" style="zoom:67%;" />



### 168 Burst Balloons

#### 消去型題 -- 千萬不要順著題目做!! 

- 因为去掉東西，還得保存序列中，誰跟誰相鄰，千萬動規是不能紀錄狀態的；一定要「倒著想」

- 在這些氣球被弄破前，a2也是像一堵牆，它的左右邊也都是獨立的 --> 可被各個擊破
- 矩陣相乘也是一樣的思想!

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011203603173.png" alt="image-20201011203603173" style="zoom:67%;" />





#### 1 確定狀態

##### 最後一步

###### 的左邊

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjlomonucqj30pu0fgtei.jpg" alt="image-20201011204756120" style="zoom:33%;" />

##### 子問題

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjloqa0l9gj313u0d6teg.jpg" alt="image-20201011205123231" style="zoom:50%;" />

- 因為邊邊一定有兩個不能扎破的



#### 2 轉移方程

- 要枚舉 k = 「中間那個氣球」，i和j不能扎破，枚舉中間所有的k



#### 3 初始條件和邊界

##### 初始 -- i & j 相鄰時為0

i ~ j, 長度是 j - i + 1

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjloxse48gj30so0bkq69.jpg" alt="image-20201011205837377" style="zoom: 33%;" />



#### 4 計算順序

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjloz99pmsj30ra0hk796.jpg" alt="image-20201011210003587" style="zoom:33%;" />



#### Coding!

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201011211559261.png" alt="image-20201011211559261" style="zoom: 67%;" />

- 22 行，需要加上 ↓, or RE

  ```java
  int[][] f = new int[n][n];
  ```

  

## 總結

### 背包型收尾了

- 物品重量、價值
- 狀態用物品個數和當前重量
  - 狀態必用當前重量，除了 Backpak VI
- 單個物品，∞多物品



### 區間型

- 用左右端點 : f_i_j
- 記憶化搜索



### 矩陣乘法動態規劃



