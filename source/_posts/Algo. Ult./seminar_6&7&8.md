---
layout: post
categories: AlgoUlt.
tag: []
date: 2019-06-16
---



# Seminar 6. BFS Advanced



![image-20200616093336824](https://tva1.sinaimg.cn/large/007S8ZIlgy1gftvn216ofj310c0jgdn3.jpg)

- 什麼時候用BFS而不用DFS?

![image-20200616093533547](https://tva1.sinaimg.cn/large/007S8ZIlgy1gftvozc29sj310809q421.jpg)

- Topological Sort



## 630. 騎士的最短路徑 II

-  BFS 模版

  ```python
  Queue = colleciton.deque()
  distance = {}
  
  for start_point in start_points:
    Q.append(start_point)
    distance(start_point) = 0
   
  while Q:
    now = queue.popleft()
    for neighbor in neighbors[now]:
      if self.is_valid(neightbor):
        Q.append(neighbor)
        distance[neighbor] = distance[now] + 1
  
  return diatance[destination]
  ```

- Follow up:

  - 輸出路徑的題，在BFS, DFS, DP中都有，其中DFS最常見

  - BFS和DP中，輸出路徑 -> 數據結構存儲

  - 存什麼？

    - [x] A. 每個點的上一個點？最後從終點不斷往前找前一個點
    - [ ] B. 每個點的下一個點？最後從起點一直往後找下一個點

  - 雙向BFS

    - 相遇時得到了答案

      <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200616100657736.png" alt="image-20200616100657736" style="zoom: 25%;" />

    - <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gftwmqhbxvj30um0gc0vy.jpg" alt="image-20200616100800150" style="zoom:25%;" />

      ```
      
      ```

      

## 1516. 異或和 X





## 892. 外星人詞典

- wrt, wrf, er, ett, erftt

  - t -> f

  - w -> e

  - e -> r

  - r -> t

  - So, 

    - t -> f
    - w -> e -> r
      - wertf

  - <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gftxa5yc1zj30gq0nogr5.jpg" alt="image-20200616103030839"  />

    ![image-20200616103238325](https://tva1.sinaimg.cn/large/007S8ZIlgy1gftxcd54ggj30gk0do0xd.jpg)

  - 舉列有環時不會進while，直接空 return

  - （abc, ab）得早期return處理掉

  - Time: 

  - https://paste.ubuntu.com/p/W2J52HPVwq/

    

## 1565. 飛行棋 I ![image-20200616110036736](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfty5hccf5j30h40lggpf.jpg)

WRONG!

Reason: didn't check whether "9" can be directly transmitted

![image-20200616110926749](https://tva1.sinaimg.cn/large/007S8ZIlgy1gftyeoh6ebj30d6030q3i.jpg)



![image-20200616111137543](https://tva1.sinaimg.cn/large/007S8ZIlgy1gftygxs7okj30h80n8gqj.jpg)



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gftyibb8b7j308402wweq.jpg" alt="image-20200616111256890" style="zoom: 50%;" />

how to fix?

![image-20200616111419729](https://tva1.sinaimg.cn/large/007S8ZIlgy1gftyjr3kyuj30ea0awdi5.jpg)



- SPFA 最短路算法, 被淘汰，因為太慢了，但用起來夠了



- Dij, Floyd, 這兩個可以拿來替換，他們都帶人名的，大不了可以不會

- 可做1364

- 放後面也可以

  ![image-20200616111955720](https://tva1.sinaimg.cn/large/007S8ZIlgy1gftypnbvbyj30xk0kswme.jpg)



- ### DP

  <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200616113300330.png" alt="image-20200616113300330" style="zoom:67%;" />





- push vs pull in DP

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gftz5g5zsnj30f60m4782.jpg" alt="image-20200616113511064" style="zoom:67%;" />



## 拓展知識

### 1364.最短路徑, as 飛行棋

- [ ] TODO..., not yet finished

### 1515.異或和

- 競賽題。。。

- 雙向BFS

  - 降時間，但有時不一定能降，像騎士就無法降時間
  - 但這題在中間會和就可以在中間會和

- 1 <= n, m <= 20

  - 組合數 C(20, 40) ==> 非常大

  - 約2^(n+m)，2^40 次方　再小一點

    <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfufb10aywj30aq094wgf.jpg" alt="image-20200616205407495" style="zoom:33%;" />

  - 2^40是2^12，稳爆；2^20约10^6，可接受
    ![image-20200616213141875](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfuge4qs73j30k40ks7b0.jpg)



### 794.滑動拼圖 II





# Seminar 7 

## Preview

### 1181.二叉樹的直徑

- 分治

- 遞歸

- Root    -> root.left

  ​			-> root.right

- M_D = max_diameter; M_C = max_chain

  - return max(M_D_root, M_C_root)

    <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfu9xow74tj30ma0b249p.jpg" alt="image-20200616174814887" style="zoom:80%;" />

- 定義、出口、拆解

  - def dfs(root):
    	if not root:
      		return [0, 0]
      	left_M_D, left_M_C = self.dfs(root.L)
      	right_M_D, right_M_C = self.dfs(root.R)
      	M_D = max(left_M_D, right_M_D, left_M_C + right_M_C)
      	M_C = max(right_M_C, right_M_C) + 1	

    ​	return [M_D, M_C]

  ![image-20200616194351449](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfud9xokowj30eu0d4tby.jpg)



## 1469.樹上最長路徑-dfs解法

![image-20200621121725802](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfzsh05ytnj30ws0jm4qp.jpg)

Time: O(N), 10^5

Space: O(N), 10^5

- 

#### DFS ==> 爆 Stack



#### BFS

![image-20200621124751035](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfztcm972yj30le02w40h.jpg)



## START

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200618093143030.png" alt="image-20200618093143030" style="zoom:67%;" />

### 分治

- 

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfw6ut4teij30ou01ut9g.jpg" alt="image-20200618093252701" style="zoom:67%;" />

- 把整棵樹的問題分解成左右子樹的問題，用相同的方法去解決它們

- 分治是思想，
  - 遞歸是實現藉由調用自己實現
  - 也可以棧實現

### 94.Binary Tree Maximum Path SumFollow

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200618094817945.png" alt="image-20200618094817945" style="zoom:67%;" />



- **要初始化为 -sys.maxsize，不然会这样挂掉**

![image-20200618100018499](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfw7ndkm8tj30tu0d642s.jpg)



### 535.打劫房屋 II

- 强行分治不行，未考虑相邻的房子无法打劫的问题

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200618101046235.png" alt="image-20200618101046235" style="zoom:67%;" />

![image-20200618101136307](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfw7z6khqqj30l00f6k2e.jpg)



- 指数级了！下面這些才是必需要枚舉的情況，這題不需要
  - 子集
  - 全排列
  - ｎ皇后
- 如果無法得出正確答案，說明什麼？
  - 返回的info不夠
- 增加返回值的種類
  - Max_not_in_profit_L
  - Max_in_profit_L
  - Max_not_in_profit_R
  - Max_in_profit_R

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfw85whozwj30l40emaic.jpg" alt="image-20200618101806841" style="zoom:80%;" />

![image-20200618102718964](/Users/joe/Library/Application Support/typora-user-images/image-20200618102718964.png)



##### 只返回一个值行不行？

![image-20200618103046363](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfw8j2otn7j31080mgtkg.jpg)

全局不推薦，不好！

全局可能被其他的function影響，對多線程也不好



### 453.二叉樹拆成鏈表

- TODO:
  - 1.right = 2
  - 4.right = 5

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200618104542919.png" alt="image-20200618104542919" style="zoom:67%;" />

- 通過考慮怎麼合上，思考要傳什麼進去



### 262. Heir Tree 繼承人樹 

- 不真的删，前是建標記，所以別修改father's child list
- Lazy Delete: 晚點再刪, 同 **859.Max Stack**
- 設計的意味，設計data base了

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200618110201357.png" alt="image-20200618110201357" style="zoom:67%;" />

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200618110244262.png" alt="image-20200618110244262" style="zoom:67%;" />



### 915.BST的中序前驅節點

- [ ] A. O(N)
- [ ] B. O(logN)
- [x] **C. O(h)** 未必要平衡，所以比B合適 

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200618110810029.png" alt="image-20200618110810029" style="zoom:50%;" />

- 

![image-20200618111311048](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfw9r6qw21j30qg0bin0j.jpg)

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200618111652378.png" alt="image-20200618111652378" style="zoom:67%;" />

![image-20200618111735472](/Users/joe/Library/Application Support/typora-user-images/image-20200618111735472.png)



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfw9y0qo8qj30jo09ctba.jpg" alt="image-20200618111945429" style="zoom:80%;" />



### 106.有序鏈表轉化為二叉搜索樹

- 操作型，很自閉

#### 方法一 O(NlogN)

- <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200618112325499.png" alt="image-20200618112325499" style="zoom:67%;" />

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfwa3qor9xj30oo0eytbq.jpg" alt="image-20200618112515315" style="zoom:67%;" />

- N個中點，合併N次，所以N次
  
  - 但每次要 N/2 去找 n/2這位置，所以 lg(N)，也就是層數



#### 方法二 O(N)

- 優化成 O(N)

![image-20200618113102707](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfwa9s2vuqj30rc0em0ys.jpg)

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gfwae3w36aj30kk0p4tfp.jpg" alt="image-20200618113512990" style="zoom:67%;" />





# Seminar 8.DFS Advanced

### 427.生成括號



### 780.删除無效的括號 -- FB 經典考察題

![image-20200623100145480](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg1zshzimlj31910u0alx.jpg)

![image-20200623100911708](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg2005je5tj30nc0bignm.jpg)



### 107.單詞拆分 - DFS

### 582.單詞拆分 II - DFS

### 683.單詞拆分 III

### 652.因式分解

![image-20200623103826795](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg20ul2zsnj310w0fg0w4.jpg)

![image-20200623105709890](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg21e2tradj30ta0nqn5g.jpg)

![image-20200623105804188](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg21ezqmakj30bg0g6di2.jpg)

![image-20200623110202303](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg21j5vjkmj30kq0qw44h.jpg)



### 815 課程表 IV -- 所有方案

![image-20200623110952163](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg21rbnu6xj30lq0uwaka.jpg)

NxN!  ==> Nx2^N



### 1514.掃地機器人

![image-20200623112202612](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg223ybw6kj30f60pcdkn.jpg)



### 121. Word Ladder II

![image-20200623112455008](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg226xmki6j30jy0eggom.jpg)

![image-20200623112636438](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg228pez4qj30oi0sadp2.jpg)

![image-20200623112809693](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg22abpwmxj30ok0i8wkt.jpg)

![image-20200623113321163](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg22fsi2c7j31030u019s.jpg)



K: 字符串長度

O(N + 26*K) # V+E



## A* -- 794.Sliding Puzzle II

- g(x): 離起點的距離

  h(x): 離終點的距離 (估算)

  f(x): = g(x) + h(x)

- <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200627115533364.png" alt="image-20200627115533364" style="zoom:67%;" />

- 定義起發式函數一般是固有招，定義得好，走得快

- 優先隊列, 用heap存狀態
  
- Heap: (f(x), g(x), state, start_x, start_y)
  
- while heap:
  - now_state... = heappop(heap)
  - if ...
    - return 最短距離 (g)
  - for next_state in self.find_next_states:
    - 加入heap = (f(new_te))
- <img src="/Users/joe/Library/Application Support/typora-user-images/image-20200627121024702.png" alt="image-20200627121024702" style="zoom:67%;" />

![image-20200627124522973](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg6qzyi8blj30ri0eater.jpg)



- 要更快就得這樣早期return, 不然就回到了原始BFS了

![image-20200627124844371](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg6r3eq3qsj30q40haqch.jpg)







- 解法一

![image-20200627125408859](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg6r90w359j318l0u0kc6.jpg)



- 解法二
  - As SPFA used in 飛行棋
- 但都是highly dependent on **get_h**, 所以這題用這算法還是可能有CASE錯。
  實際運用時，可以允許小偏差

```python
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
import heapq
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # write your code here
        if len(init_state) == 0 or len(init_state[0]) == 0:
            return -1 
        
        n = len(init_state)
        m = len(init_state[0])
        
        open_set = []
        close_set = set()
        value_to_index = {}
        
        
        # find init 0
        for i in range(n):
            for j in range(m):
                if init_state[i][j] == 0:
                    start_x, start_y = i, j
                value_to_index[final_state[i][j]] = (i, j)
                    
        
        # final_state中每个值所在的位置
        
        
        
        
        # (f(x), g(x), state, start_x, start_y)
        open_set.append((0, 0, self.list_to_tuple(init_state), start_x, start_y))
        close_set.add(self.list_to_tuple(init_state))

        while open_set:
            f, g, now_state, x, y = heapq.heappop(open_set)
            
            if self.tuple_to_list(now_state) == final_state:
                return g
            
            for next_state, next_x, next_y in \
            self.find_next_state(now_state, x, y, close_set):
                heapq.heappush(open_set, 
                (g + 1 + self.get_h(next_state,value_to_index), 
                g + 1, next_state, next_x, next_y))
                close_set.add(now_state)
        
        return -1 
        
        
    def find_next_state(self, now_state, x, y, close_set):
        next_state_list = []
        
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y 
            if not self.is_valid(next_x, next_y, now_state):
                continue 
        
            # deep copy
            next_state = self.tuple_to_list(now_state)
            next_state[x][y], next_state[next_x][next_y] = \
            next_state[next_x][next_y], next_state[x][y]
            
            next_state = self.list_to_tuple(next_state)
            if next_state in close_set:
                continue 
        
            next_state_list.append((next_state, next_x, next_y))
        return next_state_list   
        
    def get_h(self, now_state, value_to_index):
        # sigma（每个数字所在的位置的dx+dy）
        h = 0
        n = len(now_state)
        m = len(now_state[0])
        for i in range(n):
            for j in range(m):
                final_x, final_y = value_to_index[now_state[i][j]]
                h += abs(final_x - i) + abs(final_y - j)
        return h 

     def get_h2(self, now_state, value_to_index):
      	return random.randint(1, 100)
        
    def is_valid(self, x, y, now_state):
        if x < 0 or y < 0 or x >= len(now_state) or y >= len(now_state[0]):
            return False 
        return True
        
        
    def list_to_tuple(self, l):
        result = [tuple(x) for x in l]
        return tuple(result)
    
    def tuple_to_list(self, t):
        result = [list(x) for x in t]
        return result
```

- get_h：必須要是一個能作正確引導的，不然答案不見得正確的, 如，用get_h2時，肯定就是完了
- 全走時會比較差



##### 解法1, min_dist w/ 打擂台

```python
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
import heapq
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # write your code here
        if len(init_state) == 0 or len(init_state[0]) == 0:
            return -1 
        
        n = len(init_state)
        m = len(init_state[0])
        
        open_set = []
        close_set = set()
        value_to_index = {}
        
        
        # find init 0
        for i in range(n):
            for j in range(m):
                if init_state[i][j] == 0:
                    start_x, start_y = i, j
                value_to_index[final_state[i][j]] = (i, j)
                    
        
        # final_state中每个值所在的位置
        
        
        
        
        # (f(x), g(x), state, start_x, start_y)
        open_set.append((0, 0, self.list_to_tuple(init_state), start_x, start_y))
        close_set.add(self.list_to_tuple(init_state))
				count = 0
        min_dist = sys.maxsize
        while open_set:
            f, g, now_state, x, y = heapq.heappop(open_set)
            
            """ 解法一 """
            if g > min_dist:
              	continue
                
            if self.tuple_to_list(now_state) == final_state:
                # return g
                min_dist = min(min_dist, g)
                continue
            """ 解法一 END """            
            
            for next_state, next_x, next_y in \
            self.find_next_state(now_state, x, y, close_set):
                heapq.heappush(open_set, 
                (g + 1 + self.get_h(next_state,value_to_index), 
                g + 1, next_state, next_x, next_y))
                close_set.add(now_state)
        
        return -1 
        
        
    def find_next_state(self, now_state, x, y, close_set):
        next_state_list = []
        
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y 
            if not self.is_valid(next_x, next_y, now_state):
                continue 
        
            # deep copy
            next_state = self.tuple_to_list(now_state)
            next_state[x][y], next_state[next_x][next_y] = \
            next_state[next_x][next_y], next_state[x][y]
            
            next_state = self.list_to_tuple(next_state)
            if next_state in close_set:
                continue 
        
            next_state_list.append((next_state, next_x, next_y))
        return next_state_list   
        
    def get_h(self, now_state, value_to_index):
        # sigma（每个数字所在的位置的dx+dy）
        h = 0
        n = len(now_state)
        m = len(now_state[0])
        for i in range(n):
            for j in range(m):
                final_x, final_y = value_to_index[now_state[i][j]]
                h += abs(final_x - i) + abs(final_y - j)
        return h 
        
		def get_h2(self, now_state, value_to_index):
      	return random.randint(1, 100)
      
    def is_valid(self, x, y, now_state):
        if x < 0 or y < 0 or x >= len(now_state) or y >= len(now_state[0]):
            return False 
        return True
        
        
    def list_to_tuple(self, l):
        result = [tuple(x) for x in l]
        return tuple(result)
    
    def tuple_to_list(self, t):
        result = [list(x) for x in t]
        return result
```



##### 解法1+2, 加上SPFA

```python
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
import heapq
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # write your code here
        if len(init_state) == 0 or len(init_state[0]) == 0:
            return -1 
        
        n = len(init_state)
        m = len(init_state[0])
        
        open_set = []
        # close_set = set()
        close_set = {}
        value_to_index = {}
        
        
        # find init 0
        for i in range(n):
            for j in range(m):
                if init_state[i][j] == 0:
                    start_x, start_y = i, j
                value_to_index[final_state[i][j]] = (i, j)
                    
        
        # final_state中每个值所在的位置
        
        
        # (f(x), g(x), state, start_x, start_y)
        open_set.append((0, 0, self.list_to_tuple(init_state), start_x, start_y))
        # close_set.add(self.list_to_tuple(init_state))
        close_set[self.list_to_tuple(init_state)] = 0
				count = 0
        min_dist = sys.maxsize
        while open_set:
            f, g, now_state, x, y = heapq.heappop(open_set)
            
            """ 解法一 """
            if g > min_dist:
              	continue
                
            if self.tuple_to_list(now_state) == final_state:
                # return g
                min_dist = min(min_dist, g)
                continue
            """ 解法一 END """            
            
            for next_state, next_x, next_y in \

            """ 解法二 修改 find_next_state裡的條件，並傳入 g"""
            self.find_next_state(now_state, x, y, close_set, g):
                heapq.heappush(open_set, 
                (g + 1 + self.get_h(next_state,value_to_index), 
                g + 1, next_state, next_x, next_y))
                # close_set.add(now_state)
                close_set[next_state] = g + 1
        
        if min_dist == sys.maxsize:
          return -1
        return min_dist
        # return -1 
        
        
    def find_next_state(self, now_state, x, y, close_set, g):
        next_state_list = []
        
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y 
            if not self.is_valid(next_x, next_y, now_state):
                continue 
        
            # deep copy
            next_state = self.tuple_to_list(now_state)
            next_state[x][y], next_state[next_x][next_y] = \
            next_state[next_x][next_y], next_state[x][y]
            
            next_state = self.list_to_tuple(next_state)
            if next_state in close_set and close_set[next_state] >= g + 1:
                continue 
        
            next_state_list.append((next_state, next_x, next_y))
        return next_state_list   
        
    def get_h(self, now_state, value_to_index):
        # sigma（每个数字所在的位置的dx+dy）
        h = 0
        n = len(now_state)
        m = len(now_state[0])
        for i in range(n):
            for j in range(m):
                final_x, final_y = value_to_index[now_state[i][j]]
                h += abs(final_x - i) + abs(final_y - j)
        return h 
        
		def get_h2(self, now_state, value_to_index):
      	return random.randint(1, 100)
    
    def is_valid(self, x, y, now_state):
        if x < 0 or y < 0 or x >= len(now_state) or y >= len(now_state[0]):
            return False 
        return True
        
        
    def list_to_tuple(self, l):
        result = [tuple(x) for x in l]
        return tuple(result)
    
    def tuple_to_list(self, t):
        result = [list(x) for x in t]
        return result
```



- 實際用的時候可以有點小偏差



## 單調隊列 - 1507.和至少為K的最短子數組

```python
class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        # Write your code here.
        # return self.O_N3_TLE(A, K)
        # return self.mono_Q(A, K)
        return self.my_mono_Q(A, K)
    
    def my_mono_Q(self, A, K):
        N = len(A)
        pre_sum = [0] * (N+1)
        for i in range(N):
            pre_sum[i+1] = pre_sum[i] + A[i]
            
        Q = collections.deque()
        ans = sys.maxsize
        for j in range(N+1):
            # 考慮A裡有負數的情況, pre_sum就會下降了；它對 pre_sum 造成了一個山谷
            # 1. 到山谷才能拿到的值，經過山谷之前只會更小，所以前面不會再是答案
            # 2. 山谷之前只是讓長度更長不會更短
            while Q and pre_sum[j] <= pre_sum[Q[-1]]:
                Q.pop() # 塞的時候從右邊check
            
            # 都是正數的情況
            while Q and pre_sum[j] - pre_sum[Q[0]] >= K:
                i = Q.popleft() # 找答案時候從左邊
                ans = min(ans, j - i)
                
            Q.append(j)
        
        return ans if ans < sys.maxsize else -1
    
    def mono_Q(self, A, K):
        """
        [(0,-1), (3,0), (7,1), (13,2), (14,3), (9,4), (19,?)]
        
        # K = 10
        i:      0,  1,  2,  3,  4
        A[i]    3,  4,  6,  1,  -5
        sum:    3,  7,  13, 14, 9
        now_sum = 13
        
        Q.popleft()
        1. now_sum - 0 >= K?
        ans = min(ans, 2 - (-1))
        
        2. now_sum - 3 >= K? √
        ans = min(ans, 2 - (0))
        
        3. now_sum - 7 >= K? x
        break
        
        ★ 第二部分
        2. (9, 4)
        - 9 < 14?
        pop()
        - 9 < 13?  
        pop()
        - 9 < 7?
        break
        """
    
        N = len(A)
        pre_sum = [0] * (N+1)
        # for i in range(len(A)):
        #     pre_sum[i+1] = pre_sum[i] + A[i]
        for i, n in enumerate(A):
            pre_sum[i+1] = pre_sum[i] + n
        
        ans = N + 1
        Q = collections.deque()
        
        for j in range(N + 1):
            """★ 第二部分"""
            while Q and pre_sum[Q[-1]] >= pre_sum[j]:
                Q.pop()
            
            while Q and pre_sum[j] - pre_sum[Q[0]] >= K:
                i = Q.popleft()
                ans = min(ans, j - i)
            
            Q.append(j)
        
        return ans if ans < N+1 else -1
        
        
        
        
    def O_N3_TLE(self, A, K):
        n = len(A)
        # pre_sum = [0] * (N-1)
        min_len = sys.maxsize
        for i in range(n):
            if A[i] >= K:   # 要的是至少為K，不是剛好等於K
                return 1
            for j in range(i+1, n+1):
                cur_sum = sum(A[i:j])
                if cur_sum >= K:   # 要的是至少為K，不是剛好等於K
                    min_len = min(min_len, j-i)
                # print(i, j, cur_sum)
                
        if min_len == sys.maxsize:
            return -1
        return min_len
```

- 若二分答案還得再多一個 logN





