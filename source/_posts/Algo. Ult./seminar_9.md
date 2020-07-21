---
layout: post
categories: AlgoUlt.
tag: []
date: 2019-06-24

---



# DP

- 子問題們

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gg34on0q2bj30ny0h8jy8.jpg" alt="image-20200624093637867" style="zoom:50%;" />



### 什麼題目可以用DP?

- 方案數
- 最大最小值（如求收益），當二分不行時
- 可行性（能不能）





### 107. Word Break

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200624094830531.png" alt="image-20200624094830531" style="zoom:67%;" />



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gg352pwxqfj30p80e40xw.jpg" alt="image-20200624095014072" style="zoom:67%;" />

- 填表的顺序是一样的对吧?!　
  - 大方向是
- 記憶化不需要考慮求解順序

- DP的for循環的順序重要，錯的時候會導致答案錯誤



### 91. 最小調整代價

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gg357xm6stj30u00di0vm.jpg" alt="image-20200624095514358" style="zoom:67%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200624101830924.png" alt="image-20200624101830924" style="zoom:67%;" />



<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200624102212142.png" alt="image-20200624102212142" style="zoom:67%;" />

## 

- 什麼時候能用？
  - i -> i-1, i-2

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gg3621higdj30n605kq4m.jpg" alt="image-20200624102410875" style="zoom:67%;" />



### 274. Make binary tree average

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200624104138269.png" alt="image-20200624104138269" style="zoom:67%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200624104943995.png" alt="image-20200624104943995" style="zoom:67%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gg36u9jmd4j30um0dw432.jpg" alt="image-20200624105118707" style="zoom:67%;" />

- 離散化

- dp: map, 把以node為根的子樹全部修改完成後，根節點的值為value的最小花費
- {node: ({value: 把node修改成value的最小花費}}, a neted map

- dp = {

  - 5 -> {5: 0}
  - 3 -> {3: 1, 5: 1}
  - 2 -> {3:2, 5:2, 2:2}

  }

![image-20200624110829530](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg37c6jqawj31oc0u0qol.jpg)



##### Super Hard

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200624113724685.png" alt="image-20200624113724685" style="zoom:50%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200624114245275.png" alt="image-20200624114245275" style="zoom:67%;" />





# 多重背包的通用及優化

### 798.背包問題VII

- 非無限取，每種有限取

##### 方法一：拆開轉成0/1背包

```python
    def solution(self, n, prices, weight, amounts):
        
        # n: 背包容量
        # prices: 等效 0/1 背包的物品體積
        # weight: 等效 0/1 背包的物品價值
        # m: 總共的物品個數 (原來的)
        
        m = len(prices)
        
        processed_prices = []
        processed_weight = []
        
        dp = [0] * (n+1)
        
        for i in range(m):
            for k in range(amounts[i]):
                processed_weight.append(weight[i])
                processed_prices.append(prices[i])
        
        processed_item_number = len(processed_weight)
        for i in range(processed_item_number):
            for j in range(n, processed_prices[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - processed_prices[i]] + processed_weight[i])
        return dp[n]
```

- Follow up: 如果 amounts[i] <= 10 ^9怎辦？



##### 方法二: 優化物品數量

```python
    # amounts[i] <= 10**9 很大時, 減少物品數量到lg級別
    # m * log(K) * n
    # 未優化的話是 m * K * n
    def solution_opt(self, n, prices, weight, amounts):
        # n: 背包容量
        # prices: 等效 0/1 背包的物品體積
        # weight: 等效 0/1 背包的物品價值
        # m: 總共的物品個數 (原來的)
        
        m = len(prices)
        
        processed_prices = []
        processed_weight = []
        
        dp = [0] * (n+1)
        
        for i in range(m):
            base = 1
            while amounts[i] >= base:
            # for k in range(amounts[i]):
                processed_weight.append(weight[i] * base)
                processed_prices.append(prices[i] * base)
                amounts[i] -= base
                base *= 2
            
            if amounts[i] > 0:
                processed_weight.append(weight[i] * amounts[i])
                processed_prices.append(prices[i] * amounts[i])
        
        processed_item_number = len(processed_weight)
        for i in range(processed_item_number):
            for j in range(n, processed_prices[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - processed_prices[i]] + processed_weight[i])
        return dp[n]
```

