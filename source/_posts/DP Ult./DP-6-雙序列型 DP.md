---
layout: post
categories: DP Ult.
tag: [] 
date: 2019-10-08
---



# 雙序列!

### 77 LCS

- github, gitbucket, svn 版本控管的diff即用此
  LCS --> 對應到「我沒動的地方」就是我改得最少的地方

- 一個已是指數級別
- 二個序列的最長的對應「對子」，且「對子不相交」。



#### 1 確定狀態

- 設A 長度是m, B長度是n

##### 最後一步

- 觀察 A_m-1 & B_n-1 這兩個字符是否作為一個對子在最優策略中，即兩人的尾巴
  1. 對子中沒有A的尾巴
  2. 沒有B的尾巴
     <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjdg9f1ej3j314w0j2gwq.jpg" alt="image-20201004175354638" style="zoom:50%;" />
  3. 兩人的尾巴都在
  4. 兩人的尾巴都不在，在 1、2裡都考慮了。

> ##### Q: 这题中如果A字符串的最后一个字符和B字符串的最后一个字符相等，那么我们可以认为这两个字符在最长公共子序列里面。这句话是否正确？
>
> A： YES

否則會有相交

##### 子問題 

f_i_j -- A的前i個、B的前j個



#### 2 轉移方程

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjdgfuvmpyj312e0hygwa.jpg" alt="image-20201004180005253" style="zoom:50%;" />



#### 3 初始條件和邊界

- 空串和任何人的都是0
- 0也處理了，所以不會有越界



#### 4 計算順序

→

##### 時: MxN

##### 空: MxN



#### Coding!

```python
        return self.my_1004(A, B)
        
    def my_1004(self, A, B):
        m, n = len(A), len(B)
        f = [[0] * (n+1) for _ in range(m+1)]
        pi = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                f[i][j] = max(f[i][j-1], f[i-1][j])
                if f[i][j] == f[i-1][j]:
                    pi[i][j] = 1
                else:
                    pi[i][j] = 2
                
                if A[i-1] == B[j-1]:
                    f[i][j] = max(f[i][j], f[i-1][j-1]+1)
                    if f[i][j] == f[i-1][j-1] + 1:
                        pi[i][j] = 3
        # print(f)
        # print(pi)
        res = [''] * f[m][n]
        p = f[m][n] - 1
        i, j = m, n
        # print(i, j)
        while i > 0 and j > 0:
            if pi[i][j] == 1:
                i -= 1
            elif pi[i][j] == 2:
                j -= 1
            else:
                res[p] = A[i-1]
                p -= 1
                i -= 1
                j -= 1
        # print (res)
        return f[m][n]
```



### 29 Interleaving String

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjdhj2104nj30qw0ckq7q.jpg" alt="image-20201004183744506" style="zoom: 33%;" />

#### 1  確定狀態 

- X 的長度是 m+n

- X的尾巴一定要嘛是A的尾，不然就是B的尾巴
  <img src="/Users/joe/Library/Application Support/typora-user-images/image-20201004183926700.png" alt="image-20201004183926700" style="zoom:33%;" />

- 都想知道A的前多少個跟B的前多少個能不能形成X的多少個!

##### 子問題!

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201004184220676.png" alt="image-20201004184220676" style="zoom:33%;" />



#### 2 轉移方程

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201004184315671.png" alt="image-20201004184315671" style="zoom:50%;" />



#### 3 初始和邊界

兩人都是空串時，當然是囉!

#### 4 計算順序

→

時、空同以前



### 119 Edit Distance

- 插、删、替换，讓A變成B

- 在自然語言處理裡很常的算法
- 最後的目標就是把A變成B，

#### 1 確定狀態

##### 最後一步!!!!

- 看B的尾巴怎麼過來的?!
  1. 插
  2. 改
  3. 刪
  4. 免費的午餐，直接看前面

##### 子問題

↑



#### 2 轉移方程

![image-20201004213133814](https://tva1.sinaimg.cn/large/007S8ZIlgy1gjdmjvonw1j30zq0c0n3g.jpg)



#### Coding!

```python
class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        # return self.helper_1003(word1, word2)
        return self.helper_1003_O_1(word1, word2)
        
    def helper_1003_O_1(self, A, B):
        m, n = len(A), len(B)
        
        # f = [[0] * (n + 1) for _ in range(m + 1)]
        f = [[0] * (n + 1) for _ in range(2)]
        now = old = 0
        for i in range(m + 1):
            old = now
            now = 1 - now
            for j in range(n + 1):
                if i == 0:      # insert, insert, ...
                    f[now][j] = j
                    continue
                
                if j == 0:      # delete, delete, ...
                    f[now][j] = i
                    continue
                    
                # insert, delete, ...
                f[now][j] = min(f[old][j], f[now][j - 1], f[old][j - 1]) + 1
                if A[i - 1] == B[j - 1]:
                    f[now][j] = min(f[now][j], f[old][j - 1])
        return f[now][n] 
        
    def helper_1003(self, A, B):
        m, n = len(A), len(B)
        
        f = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:      # insert, insert, ...
                    f[i][j] = j
                    continue
                
                if j == 0:      # delete, delete, ...
                    f[i][j] = i
                    continue
                    
                # insert, delete, ...
                f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
                if A[i - 1] == B[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
        return f[m][n]
```



#### 應用

如在NLP裡要根據一篇文章寫一個summary，如有個人寫的標準答案: 川普幹了什麼事

兩個字符串怎麼比呢？可算兩個東西的LCS、或最小編輯距離 -- 按詞來算的。

比如說
Ans: Trump is visiting China

My: Trump will ~~be~~ visiting ~~the country~~ China.   will 要改成 is； 所以跟Ans的最小編輯距離就是4

- 用最小編輯距離可以找你可能打錯卻本來想要找的字

​					

### 154 Regular Expression Matching

包含 ‘.' & '*' 想辦法要match 上。

#### 1 確定狀態

- 仍是看最後一步: 關注最後的字符

  <img src="/Users/joe/Library/Application Support/typora-user-images/image-20201007230159162.png" alt="image-20201007230159162" style="zoom:33%;" />

- B是從左往右，所以一定是一段一段對應
  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjh62hllzcj314a0fy4af.jpg" alt="image-20201007230330701" style="zoom: 50%;" />



#### 2 轉移方程

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201007232704610.png" alt="image-20201007232704610" style="zoom:50%;" />

#### 3 初始條件

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjh6sy6jwbj312i0e6wls.jpg" alt="image-20201007232857658" style="zoom:50%;" />



#### 4 計算順序

→

時、空都是 O(MxN), 空可滾動

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201007235005631.png" alt="image-20201007235005631" style="zoom:50%;" />



### 192 Wildcard Matching

'?' 和 '*' ，這邊的 * 不再和前面的人結合，真正厲害的就是1 個*

仍是研究尾巴

- 智慧在於: 不去枚舉B的*到底是匹配了幾個，我就先匹配一個，剩下的下一步去做決定



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjh7cj9h1qj30kc0is0wy.jpg" alt="image-20201007234746393" style="zoom:50%;" />



#### 668 Ones And Zeroes

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjh7huz8xtj312a0fmtgg.jpg" alt="image-20201007235253840" style="zoom:33%;" />

#### 雙背包

![image-20201007235609438](https://tva1.sinaimg.cn/large/007S8ZIlgy1gjh7l9beqxj30zc0ektgk.jpg)



#### 4 計算順序及分析

![image-20201008000157115](https://tva1.sinaimg.cn/large/007S8ZIlgy1gjh7rals8rj313s0iqgti.jpg)

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201008000956818.png" alt="image-20201008000956818" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjh80c59ipj30ou0lcjyv.jpg" alt="image-20201008001039081" style="zoom: 67%;" />





### 課後測驗

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20201008001412167.png" alt="image-20201008001412167" style="zoom:50%;" />



### 118 Distinct Subsequences

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjh88n3m77j30mq0fegq0.jpg" alt="image-20201008001837697" style="zoom: 33%;" />

- 跟 LCS不是同個概念，主要是A、B非對稱，因為是求B在A中出現多少次，所以B中需要連出找對子! 這題求的是加法，而當時LCS求的是 MAX!

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gjh8fyv1b4j310a0es792.jpg" alt="image-20201008002540518" style="zoom:50%;" />

