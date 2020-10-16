---
layout: post
categories: DP Ult.
tag: [] 
date: 2019-09-27

---



## Warm up!



## 劃分型 DP

- 给定長度為N的序列或字符串，要求劃分成若干段
- 段數不限或指定K段
- 每一段滿足一定的性質

### 513 Perfect Squares

#### Time Complexity推導

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5ojb32x7j313g0ec7cn.jpg" alt="image-20200928003538198" style="zoom:50%;" />![image-20200928003846192](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5omiotodj31420ekwna.jpg)

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5ojb32x7j313g0ec7cn.jpg" alt="image-20200928003538198" style="zoom:50%;" />![image-20200928003846192](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj5omiotodj31420ekwna.jpg)

![image-20200928004043752](/Users/joe/Library/Application Support/typora-user-images/image-20200928004043752.png)



### Follow Up

- 問多少種方式

  剛剛是取min，現在是「方式數」就是「求和」--> 肯定就不需要再 + 1了

- 能不能把N表示成恰好K個完全平方數之和
  這是一個「可行性」的問題，就難了點， f_i_k = f[i - j^2] [k-1]

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200929234459512.png" alt="image-20200929234459512" style="zoom:50%;" />

- 藍筆的地方是題目換成「能不能至多K個」時候要改成去看的範圍



### 108 Palindrome Partitioning II

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7z3z5xbhj31600huaf8.jpg" alt="image-20200930001239833" style="zoom:50%;" />



#### 1 確定狀態 -- 最後一步&子問題

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7z5tswwzj30ww0k47ao.jpg" alt="image-20200930001427031" style="zoom:50%;" />



#### 2 轉移方程

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7z6xdf54j312m0dg7bh.jpg" alt="image-20200930001530018" style="zoom:50%;" />



#### 3 初始條件和邊界情況

##### ★★ 用序列型，考慮「前i個」定義「空串」的好處！空串就是 0個 回文串

- 如下，f[-1] 未被定義

- 所以「前幾個」就有「前0個」；哪怕**最後一段就是整個**，也有0可以來幫助！

- 當然，空串其實也是個回文串

  

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200930001928066.png" alt="image-20200930001928066" style="zoom:50%;" />





##### ★★ 回文串判斷 & 降時間複雜度優化

- 最Naive是 N^3

- 用生成回文串作思考
- 思考中心擴展

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7zirtcnsj315o0gqdn3.jpg" alt="image-20200930002652597" style="zoom:50%;" />

- 所以枚舉所有char以及中線當對稱軸 ==> N^2

  - 兩端相等，就擴展，不需要再從頭到尾看一遍

- ★☆ 所以可以記錄  isPalin ！用上 N^2

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7znfjwwqj31500iw0z5.jpg" alt="image-20200930003122216" style="zoom:50%;" />

因此，最後為：

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj7zoj07vdj30pe0f4af7.jpg" alt="image-20200930003225255" style="zoom: 33%;" />



####  Coding

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj800ioolhj30f40iy0wy.jpg" alt="image-20200930004356144" style="zoom:67%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200930004555286.png" alt="image-20200930004555286" style="zoom:67%;" />





### 437 Copy Books

#### 分析

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8vb33deoj315c0jgdqu.jpg" alt="image-20200930184637444" style="zoom:50%;" />



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8vc8zks9j315k0i4aj4.jpg" alt="image-20200930184747901" style="zoom:50%;" />

#### 1 確定狀態

##### 最後一步

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200930185014238.png" alt="image-20200930185014238" style="zoom:50%;" />

##### 子問題

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8vhkm7d7j30yo0cgwj6.jpg" alt="image-20200930185254187" style="zoom: 33%;" />



#### 2 轉移方程

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8wr2itqpj317o0dak11.jpg" alt="image-20200930193638323" style="zoom:50%;" />

- 此處的概念為「反向」的木桶原理



#### 3 初始條件和邊界情況

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8wsswvznj30tk0dwgrf.jpg" alt="image-20200930193817794" style="zoom:50%;" />



#### 4 計算順序

→

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8wtu23u1j30za0gqq7d.jpg" alt="image-20200930193917914" style="zoom:50%;" />



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8wvv5caoj30y80eidkk.jpg" alt="image-20200930194114603" style="zoom:50%;" />

- 和如果反向時可以讓A那串的相加，就是求min的過程裡的那個A的和變 O(1)



#### Coding!

![image-20200930194743914](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8x2mdqshj30lo0jmjwc.jpg)



### 劃分小結

- 要求將一個序列或字符串劃分成若干滿足要求的片段
- 解決方法: 最後一步 -> **最後一段**
  - 就是看最後一段怎麼劃出來的
- 枚舉最後一段的起點!



- 如果題目不指定段數
  - 用 f[i] 表前i個元素分段後的最值、可行性、方式數: Perfect Squares、Palindrome Partition II
- 如果題目指定段數
  - 用 f_i_j 表前i個元素分成 j 段後的最值、可行性、方式數: Copy Books



## 博奕型 DP

- 先手 --> 當前要走的人
- 不要有後手的概念--> 所以就是出招後先手換人，新的先手面對一個「新的局面」



### 394 Coins in a Line

- 博奕型，一定就是「存在型」==>「先手有沒有存在一種**贏的可能**」

#### 1 確定狀態

- 透過「第一步」分析，而不是最後一步
  - 因為局面越來越簡單，石子數越來越少
  - 如果是「加石頭」，反而是應該按「最後一步」去想，因為最後一步之前的「N」反而是「更小」

- 後手面對 N-1個或N-2 個

- 先手Alice一定選擇能讓自己贏的一步
  - 因為雙方都是採取最優策略
- 假設後手Bob面對 N-1個石頭，其貫和他是新局面的新手一樣

##### 必勝 vs 必敗

- 必勝 -- 在當下的局面，走出一步讓對手「必敗」
- 必敗 -- 自己無路可逃



#### 2 轉移方程

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200930210237276.png" alt="image-20200930210237276" style="zoom: 50%;" />



#### 3 初始條件和邊界情況

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8zawy7p9j30ni0bo0ve.jpg" alt="image-20200930210454393" style="zoom:50%;" />



#### 4 計算順序

→，時間N，空間可滾動



#### Coding!

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8zf23uluj31840i6dnd.jpg" alt="image-20200930210853241" style="zoom:67%;" />

- 其實就  return n%3 !=0 就ok，
- 但觀察過程很重要！否則當題目被改了後，就不見得有這個規律了!



## 背包型 DP

- 也可用dfs搜索，把所有可以放入背包的物品方案求一遍
  - 但是直接的搜索需要指数复杂度时间。

### 92 Backpack -- 可行性 0/1背包

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj8zqq4a2xj30q603mjtv.jpg" alt="image-20200930212005824" style="zoom:50%;" />

Easy for me.

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200930212555292.png" alt="image-20200930212555292" style="zoom:67%;" />

- ★★ HWD code的思維總是可以把 if & else 拆成「sequencial」的，好神奇。。



### 背包小结

- 不能只開  f_i ，貪心不對！
- 前 i 個物品能拼出的重量:
  - 前 i-1個物品能拼出的重量
  - 前 i-1個物品能拼出的重量 + 第 i 個物品重量 A_i-1

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200930213204703.png" alt="image-20200930213204703" style="zoom: 50%;" />



### 563 Backpack V -- 計數型 0/1背包

- 問「有多少種組合加起來是Target？」



#### 3 初始條件和邊界情況

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200930215214560.png" alt="image-20200930215214560" style="zoom:33%;" />

![image-20200930215300707](https://tva1.sinaimg.cn/large/007S8ZIlgy1gj90oylkn8j30fu0kutdl.jpg)



#### 終極優化!

- 右往左讓空間變 N

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj90x63572j30f40gcwht.jpg" alt="image-20200930220053889" style="zoom:50%;" />

- w的結尾也不用走到 0，不然就越界了
- 仍是需要先二維的「說起」，就是因為我只需要正上跟左上，而右上的不再需要了，何不就「覆蓋掉」了呢! 



### 564 Backpack VI -- 計數型 (Combination Sum IV)

每個Ai可以用多次

很像 Coin Change! -- 枚舉最後一個數，或最後一枚硬幣是幾



#### 1 確定狀態

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj92inq042j31360guqa7.jpg" alt="image-20200930225608696" style="zoom:50%;" />

##### 子問題

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200930225635900.png" alt="image-20200930225635900" style="zoom:33%;" />



#### 2 轉移方程

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200930225549579.png" alt="image-20200930225549579" style="zoom:50%;" />



#### 3 初始和邊界情況

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200930225806218.png" alt="image-20200930225806218" style="zoom: 33%;" />

#### 4 計算順序

→

##### 空間: O(Target)

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj92vqfyh3j30kq0d8wi8.jpg" alt="image-20200930230842787" style="zoom:50%;" />



### 所有路徑打印

- Dfs

### 背包小結

- 關鍵點: 最後一步!
  - ***如果物品無序，就看最後一個背包裡的物品是誰***
  - 有序，最後一個看它有沒有進
- 最後一個物品有沒有進背包
- 背包的總承重一定要放在arr裡!
- V、VI差別在 
  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj92zm0ry5j30x00do453.jpg" alt="image-20200930231226207" style="zoom: 33%;" />





## 背包路徑打印

打印最多物品的那個方案 -- 最優解的那一種路徑

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj96o5sdtzj312a0ko7de.jpg" alt="image-20201001011948590" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gj96p6vy55j30k40660uf.jpg" alt="image-20201001012049471" style="zoom: 50%;" />

