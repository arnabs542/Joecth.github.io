---
layout: post
categories: AlgoUlt.
tag: []
date: 2019-07-03

---



1. 2^n ==> n^2
2. 無循環依賴、無序應該不是；但無序的也可能是就是背包型



# DP appendix 2

## 1147. 工作安排 

- 求「價值最大」＝＝＞ 最優值

- 每天要決定是L or H or X

- 跟 house Robber 像, 但多了一個狀態「選擇難or易」

- |      |       |      |       |       |
  | ---- | ----- | ---- | ----- | ----- |
  | L    | **4** | 2    | 3     | **7** |
  | R    | 3     | 5    | **6** | 9     |

![image-20200703202854308](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge244w23tj31100icwo7.jpg)



- 坐標型DP

- 簡化後可以是「令dp[i] 表前i周可完成的最大價值」，狀態轉移方程：
  - dp[i] = max(dp[i-1] + low[i], dp[i-2] + high[i])
- 初始化：
  - dp[0] = low[0]
  - ![image-20200703203413184](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge29kbm7ej30o20gc7a0.jpg)

- 什麼情況不是返回 dp[n-1]? 
  - 當價值有可能有負數的時候
  - 因為i已經假設第i天有做事
  - 可以透過進行拓維解決、加個「不做事」的維度

- 滾動優化，一起模 3

![image-20200703210638577](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge37afck7j30o20fujyz.jpg)



## 77.LCS 最長公共子序列 

- LCS
- LIS
- LCA
- TSP
- 2^N, N位，用DP降到 N^2
- 给两個字串的，為「匹配型動規」
  - LCS
  - Edit Distance
  - Interleaving Substring
  - Wildcard Matching
  - Regular Expression Matching

- **dp[i] [j] 表 A的前i元素與 B的前i元素的最長LCS長度**

- N個字符，有N個不同前綴 X ==> N+1才對
  - 還有空串！空串是任意串的前綴；如空arr是任何arr的前綴

![image-20200703205030160](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge2qhuja2j30uy0dcdlf.jpg)





![image-20200703205331747](/Users/joe/Library/Application Support/typora-user-images/image-20200703205331747.png)



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gge2upqxmhj30ug0dyn2t.jpg" alt="image-20200703205433751" style="zoom:67%;" />



- 初始的邊上是0
- 如果是edit distance 的化 邊邊應該是 i或j的值
- 大問題依賴小問題

![image-20200703205747834](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge2y33wrrj30zk0fun6b.jpg)

​		＆interleaving

- 区间型是小依賴大
  - i倒過來，j正過去
  - Stone Game

- 滚動數組 一起模 2 即可，如下，依賴得少才好滾

![image-20200703210458738](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge35k1lo6j30ue0k6n6u.jpg)



## 76.最長上升子序列 LIS 

- subsequcne 

- longest ==> 動規
- **不能交換順序，是有序的！**；背包可以交換，只是一個集合，是可換序的特例DP解法

- dp[i] 的定義？

![image-20200703211312555](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge3e6f2hjj316k0noqd4.jpg)

- A為何錯？
  - 下面這個５就拼不上了

![image-20200703211703227](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge3i4pr9tj30m00ee77s.jpg)

![image-20200703211820236](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge3jg7ltkj30mk0daadf.jpg)

- 初始狀態 dp[i] = 1
  - 是说，「每個數就選它自己而已」，都以自己開始、結尾
  - <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gge3nfsgvcj30pu0cmgnv.jpg" alt="image-20200703212210255" style="zoom:50%;" />
  - 只初始化dp[0] 是不夠的，這也是座標型，就是看怎麼跳
  - 這不一定要從0這個位置開始選，每個數都可能成為起點

![image-20200703212036165](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge3lszejnj30o60gin3h.jpg)

- O(N^2)
- 

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gge3q1olo0j30iu0ccgq6.jpg" alt="image-20200703212440013" style="zoom:50%;" />



## 91.最小調整代價

- ![image-20200703213059015](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge3wmh1s6j311e0gg7b5.jpg)

- 轉移方程
  - 

![image-20200703213322963](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge3z3x4h4j30qc0j2q62.jpg)

![image-20200703213551446](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge41on9x5j30og0b878b.jpg)



- 200^3 
- ![image-20200703213631392](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge42dgrt1j30sg0hiwjo.jpg)

- 滾動數組：第一維模2就完成



![image-20200703213714291](https://tva1.sinaimg.cn/large/007S8ZIlgy1gge4349ar1j30qe0o27gl.jpg)



- 動規類型
  - **座標型**: Triangle, Unique Path, Jump Game
  - **前綴型**
    - 匹配型: LIS, Wildcard Matching
    - 划分型: Word Break
  - **區間型**: Stone Game
  - **背包**: Backpack 系列
  - 博奕型: Coins in a Line
  - 狀態壓縮型: TSP(Traveling Salesman Problem)
  - 樹型: Binary Tree Maximum Path Sum
  - 圖型: (面試基本沒考過) NOI
  - on lintcode



# DP  appendix 3

## 1018.香檳塔

- 類似題: 座標型動規，有座標的info在
- similar to Triangle
  <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200712201733032.png" alt="image-20200712201733032" style="zoom:33%;" />

- 

![image-20200712203228254](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggogsiqo19j30zu0isna9.jpg)

- 空間優化，模2

![image-20200712203258726](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggogt1pj5uj31020iqna9.jpg)



## 200.最長回文子串 

- Manacher's 馬拉車算法， O(N)
- 背向雙針 O(Nx(2N-1))
- 動規: 區間型動規，子串、子數組

![image-20200712204113836](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggoh1mpbr3j30yu0a8tam.jpg)

![image-20200712204248042](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggoh39walhj30tw0cwgnx.jpg)

![image-20200712204333437](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggoh41ojf1j31ak0l0tlc.jpg)

- 是否可用滾動優化？可

- 石子Stone Game合并不能滚動，因為最後還是模N

   

## 119.編輯距離

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ggohyaoonzj30ze0j2aen.jpg" alt="image-20200712211236545" style="zoom: 50%;" />

- 匹配型動規
- dp[i] [j] 

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ggohzectnqj314w09gwgk.jpg" alt="image-20200712211341183" style="zoom:67%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ggoi0wqzwfj311w0bqq60.jpg" alt="image-20200712211508710" style="zoom:50%;" />

![image-20200712211920952](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggoi5ch6tej312a0ho7an.jpg)







![image-20200712211952831](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggoi5ub3nxj31780lq7gi.jpg)

![image-20200712212103748](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggoi7241kbj30z80ky4c5.jpg)

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200712212200733.png" alt="image-20200712212200733" style="zoom: 33%;" />

- 能滾嗎？
  - 模2可滚，初始化不能放一开始了，得一邊dp一邊初始



## 1565.飛行棋

- 如果可以往前跳又可以往後跳，就沒有方向性了，就不能動規了
- 不會往前飛，就是不能循環依賴 ==> Topological Sort 檢測圖裡有沒有循環依賴的關係

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200712213048000.png" alt="image-20200712213048000" style="zoom:33%;" />

- 座標型，1D座標動規，用傳送門還有dice跳

![image-20200712213327557](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggoijyw55aj30ti0aiq6i.jpg)

![image-20200712213554267](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggoimjyqkuj30uo0han4n.jpg)

![image-20200712213639171](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggoinaj186j30u00hewhe.jpg)

