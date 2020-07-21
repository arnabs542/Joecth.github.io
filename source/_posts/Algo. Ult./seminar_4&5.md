---

layout: post
categories: AlgoUlt.
tag: []
date: 2019-06-9

---



思考何時用雙指針

# Seminar 4

## 1849. Grumpy Bookstore Owner

1. 枚舉脾氣變好的開始日期，再計算所有好脾氣的顧客

2. 用一個滑窗來處理當前sliding window內的情況

   - [ ] ​	A. 紀錄sliding window 內customers 的個數

   - [ ] ​	B. 紀錄sliding window 內好評customers 的個數 

   - [x] ​	C. **紀錄sliding window 內差評customers 的個數. V**	

   ​			答案怎麼打擂台？！

```python
class DataType:
    GOOD = 0
    BAD = 1

class Solution:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param X: X days
    @return: calc the max satisfied customers
    """
    def maxSatisfied(self, customers, grumpy, X):
        # write your code here
        # 1. sliding window 紀錄區間內差評人數的個數
        # 2. 找所有天中原本就是好評人的個數
        # 3. 原本好評+區間內最好差評人數 = 答案
        n = len(customers)
        if n == 0:
            return 0
            
        left = 0
        right = X - 1
        
        now_sum = 0 # 當前區間的差評人數
        for i in range(X):
            if grumpy[i] == DataType.BAD:
                now_sum += customers[i]
        
        maximum_bad_number = now_sum
        
        while right + 1 < n:
            right += 1
            if grumpy[right] == DataType.BAD:
                now_sum += customers[right]
        
            if grumpy[left] == DataType.BAD:
                now_sum -= customers[left]
            
            left += 1
            maximum_bad_number = max(maximum_bad_number, now_sum)
            
        satisfied_number = 0
        for i in range(n):
            if grumpy[i] == DataType.GOOD:
                satisfied_number += customers[i]
        
        return satisfied_number + maximum_bad_number
```





## 1850. 撿蘋果

- 目的：枚舉兩個區間

![image-20200609100156524](https://tva1.sinaimg.cn/large/007S8ZIlgy1gflt4ayfi1j30ys0gc44n.jpg)

![image-20200609100606181](https://tva1.sinaimg.cn/large/007S8ZIlgy1gflt8o6v50j30zm0huwlh.jpg)

當已知隔板，可知左邊最大、右邊最大是多少，ref: penbox





## 1375. Substring With At Least K Distinct CharactersFollow

- Description
- Leaderboard
- Note
- Discuss
- Solution
- 
- My Submissions
- Open IDE

### 雙指針的變式 -- 計數型雙指針

#### 雙指針的類型：

##### 同向雙指針

- sliding window

##### 相向雙指針

- Two sum 類型問題

##### 背向雙指針

- 最長回文子串

##### 計數型雙指針

- 通過雙指針解決計數問題
- 問法：滿足某條件的....有多少個

##### 模擬型雙指針

- 通過雙



- 判斷是否為「好串」
- 判斷以區間為前綴是否滿足條件





## 1219. 加熱器

1. 二分：對每個房屋的位置在加熱器數組中用二分，找到最后一个比你小的加热器一個半徑　nlogn

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200609105609685.png" alt="image-20200609105609685" style="zoom:67%;" />



2. 优化一：直接雙指針貪心

   ![image-20200609110723097](https://tva1.sinaimg.cn/large/007S8ZIlgy1gflv0ebmj9j30vy0agdis.jpg)

   

3. 优化二：二分「加热器的半径」+ 双指针，有機會更好想

![image-20200609111124815](https://tva1.sinaimg.cn/large/007S8ZIlgy1gflv4llibmj30pe0b2ju2.jpg)

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200609111225705.png" alt="image-20200609111225705" style="zoom:67%;" />

![image-20200609111539663](https://tva1.sinaimg.cn/large/007S8ZIlgy1gflv922yz9j30q60oqaiw.jpg)





## 1879.twoSumVII

![image-20200609112642341](https://tva1.sinaimg.cn/large/007S8ZIlgy1gflvki9wvxj30le09wtb1.jpg)



![image-20200609113454765](https://tva1.sinaimg.cn/large/007S8ZIlgy1gflvt4k12kj30qi0ooqb6.jpg)

![image-20200609113602841](https://tva1.sinaimg.cn/large/007S8ZIlgy1gflvu9fq9vj30u40fmq9m.jpg)





<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200609113733945.png" alt="image-20200609113733945" style="zoom:67%;" />





# Seminar 5

## 677.大島的數量

![image-20200611093923800](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo3ph93a1j30he0buq5n.jpg)

![image-20200611094851670](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo3zcfmkkj30u00ub165.jpg)





## 598.僵屍矩陣

- 爛橘子感染
- 程序員的病毒
- 「感染的起點」，從僵屍開始 BFS



![image-20200611095527541](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo4692l8uj30r80ruwli.jpg)

![image-20200611095832430](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo49emrm0j30t40vcamu.jpg)





#### 加now_day

![image-20200611100705633](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo4idhzguj30ti0v2wpg.jpg)



#### 也可以内嵌算human number 

![image-20200611101052102](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo4m9fqsjj30x20qo7br.jpg)





## 573.郵局的建立II

visited 非共享的，

每次的



![image-20200611101757179](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo4ttxr3rj30qk10utix.jpg)





但這樣會是 O(n^4)的



![image-20200611102340291](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo4zjyz5bj30ta0su4co.jpg)

**１１４line这样写的话，可能一个房子被经过多次**



so, better as following

![image-20200611102837431](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo54r3786j30ug0k0jz5.jpg)





![image-20200611103125603](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo57o772oj30vk0qwtht.jpg)

倒過來！從房子找空地！





#### 該怎麼從房子數來BFS?

![image-20200611104641237](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo5nhua62j30pu0l4436.jpg)

![image-20200611104818468](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo5p6k3e0j30sm0vuaqb.jpg)

![image-20200611105245274](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo5ttq9oqj30u00w07f1.jpg)



## 616.課程安排

- 拓展較少，一般都就裸題

- 預處理所有課程的入度，將所有入度為０的點入隊，並逐漸出隊，並將出隊相連的節點的入度減１
- 若一節點入度變為０，則將其入隊

- BFS 結束後，ans序列長度若與課程總數相等，則是一個拓撲序
- 否則不存在拓撲序



#### BAD, O(VE) or O(n*m)

一般要求 O(V+E) or O(n+m)

所以

![image-20200611110413633](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo65sexw1j30mk0modme.jpg)





![image-20200611110653860](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo68h2646j30fe01edg7.jpg)

#### Better↓，O(V+E) or O(n+m)

![image-20200611110609155](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo67rdcv6j30sm0vcn53.jpg)





## 434.島個數II

### BFS

- O(n^2) * len(queue)

### 並查集

- 



![image-20200611111435222](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo6gomjm4j31nk0k4zsl.jpg)

#### ![image-20200611112039152](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo6mwtnb3j31nk0quan3.jpg)

這寫法不具壓縮



#### 壓縮路徑

![image-20200611112128985](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo6nqyrutj31d20iwqbd.jpg)

![image-20200611112428660](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo6qtvn7wj30gw0iwada.jpg)

「之後找就都是O(1)的操作了」，是個均攤O(1)的操作

![image-20200611112740580](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo6u94fakj30n20dcalx.jpg)

![image-20200611112850990](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo6vft814j30vf0u0n8i.jpg)

![image-20200611113032781](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo6x56v7qj30re0qa0zj.jpg)



把s改為is_ialand

![image-20200611113056937](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo6xlfmyvj30u00yu13v.jpg)





![image-20200611113609070](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo72y8ny8j30pw0voqbt.jpg)

![image-20200611113842739](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfo75oajyfj30u00vgn6j.jpg)



# 雙指針的其它實現討論

### Grumpy bookstore

![image-20200612194355441](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpqsr818cj30x60ien3w.jpg)

![image-20200612194622939](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpqvauwoej30aw0323z6.jpg)

![image-20200612195027886](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpqzk8vfnj30uo0g6dl4.jpg)



# BFS Discussion

### 1828.湖面逃跑 ★★★

from Akuna Capital

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfprwqg1euj30gs0gmakw.jpg" alt="image-20200612202220431" style="zoom:50%;" />

![image-20200612202608173](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfps0o2al5j30i407a407.jpg)

![image-20200612203448516](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfps9p40caj30lk0ca0wk.jpg)

![image-20200612203632013](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpsbhalxsj30da04kab2.jpg)

![image-20200612204903384](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpsojt083j30gq0baq6i.jpg)

![image-20200612204516486](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpskkym5vj30t20duaey.jpg)

![image-20200612204556569](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpsla2e9oj30gu02c3z9.jpg)



### 1070.Merge Account ★★★

![image-20200612213238736](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfptxvu73bj30cq0bwq6x.jpg)

![image-20200612214646335](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfpucl36woj30dq08a416.jpg)