---
layout: post
categories: LC
tag: []
date: 2020-01-11
---

2/1 setting

看兩部FLAG高頻題的video

看網紅的方向video



2/2 TODO:

Complex DataStructure

### 題目太長先放棄：

489robot room cleaner, 785, 721, 65validnumber, 133 clone graph, 636 executive time of functions, 269 alien dictionary



|                                                              | Brute  Force | Thoughts1                                                    | Thoughts2                                                    |                            | Status | coded                                                        |                                     |
| ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------- | ------ | ------------------------------------------------------------ | ----------------------------------- |
|                                                              |              |                                                              |                                                              |                            |        |                                                              |                                     |
| [84 Largest Rectangle in Histogram](#84)                     |              | ● Stack:  Greedy:   <br />                                   | Greedy<br />● Time: O(n^2) ==> O(3n) <br />● Space: O(2n) ==> O(3n) | Self-minimum               | v      |                                                              | Not in<br />~42, 907                |
| [85 Maximal Rectangle](#85)                                  |              |                                                              | Greedy<br />● Time: O(n^2) ==> O(m*3n) <br />● Space: O(2n) ==> O(3n) | Self-minimum x len(arr_2d) | v      |                                                              | Not in                              |
| [907 sum of subarrays minumums](#907)                        |              |                                                              | Greedy<br />● Time: O(n^2) ==> O(3n) <br />● Space: O(2n) ==> O(3n) | Self-minimum               | v      |                                                              | Not in<br />~84                     |
|                                                              |              |                                                              |                                                              |                            |        |                                                              |                                     |
| [392 Is SubSequence](#392)                                   |              | with deque()                                                 |                                                              |                            | v      |                                                              | Not in                              |
| [792 Number of Matching Subsequences](#792)                  |              |                                                              |                                                              |                            | v      |                                                              | Not in                              |
| [1055 Shortest Way to From String](#1055)                    |              |                                                              |                                                              |                            | v      |                                                              | Not in                              |
|                                                              |              |                                                              |                                                              |                            |        |                                                              |                                     |
| High Freq.                                                   |              |                                                              |                                                              |                            |        |                                                              |                                     |
| [953 LeetCode 953 Verifying an Alien Dictionary](#953)       |              |                                                              | 邊界check要另做                                              |                            | v      | v                                                            |                                     |
| [301Remove Invalid Parentheses](#301)                        |              |                                                              |                                                              |                            | HARD   | HARD..                                                       |                                     |
| [238 product of array except self](#238)                     |              |                                                              |                                                              |                            | v      | v                                                            |                                     |
| [67 Add Binary](#67)                                         |              |                                                              |                                                              |                            | △      |                                                              |                                     |
| [273 Integer to English Words](#273)                         |              |                                                              |                                                              |                            |        |                                                              |                                     |
| [973 K Closest Points to Origin](#973)                       |              |                                                              |                                                              |                            | v      |                                                              |                                     |
| [560 Subarray Sum equals K](#560)                            |              |                                                              |                                                              |                            | v      |                                                              |                                     |
| [158 Read N Characters Given Read4 Ⅱ](#158)                  |              |                                                              |                                                              |                            |        |                                                              |                                     |
| [621 Task Scheduler](#621)                                   |              |                                                              |                                                              |                            |        |                                                              |                                     |
| [325 Maximum Size Subarray Sum Equals k](#325)               |              |                                                              |                                                              |                            |        |                                                              | ~ 560                               |
|                                                              |              |                                                              |                                                              |                            |        |                                                              |                                     |
| [243 Shortest Word Distance Ⅰ](#243) ~ [245 Ⅲ](#245)         |              |                                                              |                                                              |                            | v      |                                                              |                                     |
|                                                              |              |                                                              |                                                              |                            |        |                                                              |                                     |
| **Heap**<br />●　O(N) for all arr's heapify<br />●　O(NlogN) if insert one after one<br /> ● O(lgN) for pop() & insert(), 从 n/2 地方开始进行调整 |              |                                                              |                                                              |                            |        |                                                              |                                     |
| [215 Kth largest elem in unsorted array](#215)               |              | Heapify<br />O(N + klgN) -- N for heapify, klgN for pop() k elem | Q-sort<br />O(N)                                             |                            | v      | v                                                            |                                     |
| [378 Kth Smallest Element in a Sorted Matrix](#378)          |              | heap                                                         | m-sort, w/ heap helping manage running idx                   |                            | v      | https://www.bilibili.com/video/av58960675/<br />仍是需要注意實踐的方式還有熟練度<br />v | ~23                                 |
| [240 Search a 2D Matrix II -- Sorted nxn Matrix](#240)       |              | <u>Binary</u> OK!<br />O(m x lg(n) x lg(DIFF))               | D&C <br />O(n)                                               |                            | v      |                                                              | ~74                                 |
| [74 Search a 2D Matrix](#74)                                 |              |                                                              |                                                              |                            | v      | v                                                            | ~240, but A\[i+1][0] > A\[i-1][n-1] |
| [23 Merge K Sorted Lists](#23)                               |              |                                                              |                                                              |                            | v      | v                                                            | ~378                                |
| [692 Top K frequent words](#692)                             |              | heapify                                                      |                                                              |                            | v      |                                                              |                                     |
| [252 Meeting Room](#252)                                     |              |                                                              |                                                              |                            | v      | v                                                            | ~253, 56                            |
| [253 Meeting Room Ⅱ](#253)                                   |              |                                                              |                                                              |                            | v      |                                                              | ~252, 56                            |
| [56 Merge Intervals](#56)                                    |              |                                                              |                                                              |                            |        |                                                              | ~252, 253, 435                      |
| [435 Non-overlapping Intervals](#435)                        |              |                                                              |                                                              |                            |        |                                                              | ~56, 252, 253                       |
| **[282 Expression Add Operators](#282)**                     |              |                                                              |                                                              |                            |        |                                                              |                                     |
| [438. Find All Anagrams in a String](#438)                   |              | 照bucket sort方式编码然后loop找，但發生 Time Limit Exceeded  |                                                              |                            | v      | v                                                            | ~49                                 |
| [173 Binary Search Tree Iterator](#173)                      |              | heapq, easy                                                  |                                                              |                            | v      | v                                                            |                                     |
| [269 Alien Dictionary](#269)                                 |              | [leetcode.jp-269 wwwlink](https://leetcode.jp/leetcode-269-alien-dictionary-%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90/) |                                                              |                            | HARD   |                                                              | ~207, 210                           |



Arrays:

|                                          |                                                              |                                                              |      | status | coded    |        |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- | ------ | -------- | ------ |
| [349 Intersection of Two Arrays](#349)   |                                                              |                                                              |      | v      | v        |        |
| [350 Intersection of Two Arrays Ⅱ](#350) | Two pointers:<br />Time Complexity: O(*n*log*n*+*m*log*m*), where n*n* and m*m* are the lengths of the arrays.<br />Space complexity: \mathcal{O}(1)O(1). We sort the arrays in-place. | Time complexity: \mathcal{O}(n + m)O(*n*+*m*), where n*n* and m*m* are the lengths of the arrays. We iterate through the first, and then through the second array; insert and lookup operations in the hash map take a constant time. <br />Space complexity: \mathcal{O}(\min(n, m))O(min(*n*,*m*)). We use hash map to store numbers (and their counts) from the smaller array. |      | v      | v        |        |
| [896 Monotonic rAray](#896)              |                                                              |                                                              |      | v      |          | too ye |
| [31 Next Permutation](#31)               |                                                              |                                                              |      | v      | Once     |        |
| [825 Friends of Appropriate Ages](#825)  |                                                              |                                                              |      | v      | Abstract |        |
| **TWO WAYS recording**                   |                                                              |                                                              |      |        |          |        |
| [42 Trapping Rain Water](#42)            |                                                              |                                                              |      | v      | v        | ~84    |
| [238 Product of Array Except Self](#238) |                                                              |                                                              |      | v      | v        |        |



## Sliding Window

|                                                              |      |      |      | coded                      | Status |          |
| ------------------------------------------------------------ | ---- | ---- | ---- | -------------------------- | ------ | -------- |
| [209 Minimum Size Subarray Sum](#209)                        |      |      |      | v                          | v      |          |
| [159 Longest Substring with At Most Two Distinct Characters](#159) |      |      |      | v                          | v      | ~340     |
| [340 Longest Substring with At Most k Distinct Characters](#340) |      |      |      | v 比159多了個 k==0 的check | v      | ~159, ~3 |
| [3 Longest Substring Without Repeating Characters](#3)       |      |      |      |                            |        |          |

３３3232222232322

status

Coded 32324

Greedy

|                 |      |      |      |      |      |        |
| --------------- | ---- | ---- | ---- | ---- | ---- | ------ |
| 135 分發糖果    |      |      |      |      |      | Not in |
| 376 搖擺序列    |      |      |      |      |      | Not in |
| 402 移除K個數字 |      |      |      |      |      | Not in |
| 55              |      |      |      |      |      | Not in |
| **45**          |      |      |      |      |      |        |



## Backtracking

|                                                 |      |      |      | status | coded                                                        |      |
| ----------------------------------------------- | ---- | ---- | ---- | ------ | ------------------------------------------------------------ | ---- |
| [78 Subsets](#78)                               |      |      |      | v      | v                                                            |      |
| [90 Subsets Ⅱ](#90)                             |      |      |      | v      | v                                                            |      |
| [40 Combination Sum Ⅱ](#40)                     |      |      |      | v      | v                                                            | ~113 |
| [22 Generate Parentheses](#22)                  |      |      |      | v      | △ 未想出return條件；<br />　 然後item的更新仍該在result更新前 |      |
| [51 N-Queens](#51)                              |      |      |      |        | X                                                            |      |
| Merge                                           |      |      |      |        |                                                              |      |
| [315 Count of Smaller Numbers After Self](#315) |      |      |      |        | X                                                            |      |
| high freq.                                      |      |      |      |        |                                                              |      |
| [46 Permutations](#46)                          |      |      |      | v      | v                                                            |      |
| [47 Permutations Ⅱ](#47)                        |      |      |      | v      | v                                                            |      |
| [88 Merge Sorted Array](#88)                    |      |      |      | v      | v                                                            |      |



D&C

|                                |      |      |      |      |      |      |
| ------------------------------ | ---- | ---- | ---- | ---- | ---- | ---- |
| [125 Valid Palindrome](#125)   |      |      |      | v    |      |      |
| [680 Valid Palindrome Ⅱ](#680) |      |      |      | v    |      |      |
|                                |      |      |      |      |      |      |



## Binary Tree & Graph

A **binary tree** is a data structure in which each node has at most 2 children, which aer referred to as the left and right child respectively.

**Complete Binary Tree** :
Every level, except possibly the last, is completely filled. And all nodes in the last level are as far left as possible.

**Full Tree**
A **full binary tree** (sometimes referred to as a **proper** or **plane** binary tree) is a tree in which every node has either 0 or 2 children.

#### Traversals

```python
class Node(object):
	def __init__(self, value):
		self.value = value
		self.left, self.right = None, None
class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)
	
  def print_tree(self, traversal_type):
    if traversal_type == "preorder":
      return self.preorder_print(tree.root, "")
    elif traversal_type == "inorder":
      return self.inorder_print(tree.root, "")
    elif traversal_type == "postorder":
      return self.postorder_print(tree.root, "")    
    else:
      print("Trav type not supported")
      return False
  def preorder_print(self, start, traversal):
    if start:
      traversal += (str(start.value) + "_")
      traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
		return traversal
  
  def inorder_print(self, start, traversal):
    if start:
      traversal = self.preorder_print(start.left, traversal)
			traversal += (str(start.value) + "_")
			traversal = self.preorder_print(start.right, traversal)
		return traversal
  
  def postorder_print(self, start, traversal):
    if start:
      traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
			traversal += (str(start.value) + "_")     
		return traversal  

  
# 1-2-4-5-3-6-7
# 4-2-5-1-6-3-7
# 
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Nonde(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
```

#### Height

```python
    def height(self, root):
        if not root:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        
        return 1 + max(l, r)
```

#### Size

```python
		def size_(self, root):
			if not root:
				return 0
      return 1 + self.size_(root.left) + self.size_(root.right)
   or 
  	BFS
```



|                                                              |      |                      |                                                              | status   | coded                                        |           |
| ------------------------------------------------------------ | ---- | -------------------- | ------------------------------------------------------------ | -------- | -------------------------------------------- | --------- |
| DFS preorder                                                 |      |                      |                                                              |          |                                              |           |
| [113 Path Sum Ⅱ](#113)                                       |      |                      |                                                              | v        | △ return的時機未抓好，造成items未被pop()足夠 | ~40       |
| [236 Lowest Common Ancestor of a Binary Tree](#236)          |      |                      |                                                              | v        |                                              |           |
| [114 Flatten Binary Tree to Linked List](#114)               |      | 左边先拉平，常规思维 | 右边从底部建上来，酷                                         | v        |                                              |           |
| BFS                                                          |      |                      |                                                              |          |                                              |           |
| [199 Binary Tree Right Side View](#199)                      |      |                      |                                                              |          |                                              |           |
| *HIgh Freq.*                                                 |      |                      |                                                              |          |                                              |           |
| [105 Construct Binary Tree from Preorder and Inorder Traversal](#105) |      |                      |                                                              |          |                                              |           |
| [110 Balanced Binary Tree](#110)                             |      |                      |                                                              |          |                                              |           |
| [111 Minimum Depth of Binary Tree](#111)                     |      |                      |                                                              |          |                                              |           |
| [112 Path Sum](#112)                                         |      |                      |                                                              |          |                                              |           |
| [113 Path Sum Ⅱ](#113) repeated                              |      |                      |                                                              |          |                                              |           |
| [124 Binary Tree Maximum Path Sum](#124)                     |      |                      |                                                              |          |                                              |           |
| [297 Serialize and Deserialize Binary Tree](#297)            |      |                      |                                                              |          |                                              |           |
| GRAPH<br />adjacent matrix & table                           |      |                      |                                                              |          |                                              |           |
| [207 Course Schedule](#207)                                  |      | DFS                  | BFS Topological sorting<br />[leecode.jp link](https://leetcode.jp/leetcode-207-course-schedule%e8%a7%a3%e9%a2%98%e6%80%9d%e8%b7%af%e5%88%86%e6%9e%90/) | v        | v                                            | ~210, 269 |
| High Freq.                                                   |      |                      |                                                              |          |                                              |           |
| [210 Course Schedule Ⅱ](#210)                                |      |                      |                                                              | v        | v                                            |           |
| [269 Alien Dictionary](#269)                                 |      |                      |                                                              | Too HARD |                                              |           |
| [102 Binary Tree Level Order Traversal](#102)                |      |                      |                                                              |          |                                              |           |
| [145 Binary Tree Postorder Traversal](#145)                  |      |                      |                                                              | v        | v                                            |           |
| [958 Completeness of a Binary Tree](#958)                    |      |                      |                                                              | v        |                                              |           |
| [104 Maximum Depth of Binary Tree](#104)                     |      |                      |                                                              | v        | v                                            |           |
| [111 Minimum Depth of Binary Tree](#111)                     |      |                      |                                                              | v        | v                                            |           |



## B-Search & B-Search Tree

<img src="https://tva1.sinaimg.cn/large/006tNbRwgy1gbfy37o6xtj31ds0u04qp.jpg" alt="image-20200131174932656" style="zoom:50%;" />

|                                                              |      |      |      | status      | coded                                            |                                  |
| ------------------------------------------------------------ | ---- | ---- | ---- | ----------- | ------------------------------------------------ | -------------------------------- |
| B-Search<br />1. 如果搭配(l+1, r-1)條件應該要是 l<=r 才對。不然兩個元素時，第二個元素是target就會找不到！<br /> |      |      |      |             |                                                  |                                  |
| [35 Search Insertion Position](#35)                          |      |      |      | v           | v                                                | 邊界條件需要特別思考<br />Not in |
| [34 Search for a Range](#34)                                 |      |      |      | v           | v                                                |                                  |
|                                                              |      |      |      |             |                                                  |                                  |
|                                                              |      |      |      | X　討論複雜 |                                                  |                                  |
| B-Search 模板：https://www.jianshu.com/p/b72c80fdb240<br />https://www.jianshu.com/p/b72c80fdb240 |      |      |      |             |                                                  |                                  |
| [69 Sqrt(x)](#69)                                            |      |      |      | v           | v<br />Template1                                 |                                  |
| [374 Guess Number Higher or Lower](#374)                     |      |      |      | v           | v<br />Tempalte1                                 | Not in                           |
| [33 Search in Rotated Sorted Array](#33)                     |      |      |      | v           | Not yet, should be Template1                     |                                  |
| [278 First Bad Version](#75)                                 |      |      |      | v           | v <br />Template2                                |                                  |
| [162 Find Peak Element](#162)                                |      |      |      | v           | △<br />Template2, 但r值却是设为了 len(nums)-1 ?! |                                  |
| [153 Find Minimum in Rotated Sorted Array](#153)             |      |      |      |             | <br />Template2                                  |                                  |
|                                                              |      |      |      |             |                                                  |                                  |
| B-Search Tree (BST)　<br />左子樹所有節點的值都<=根<br />左右子樹也分別為B-Search Tree<br />等於的情況只能出現在左子樹或右子樹的某一側<br />由於中序是小到大的，所以又叫B-Sort Tree<br />插入 |      |      |      |             |                                                  |                                  |
| [449 Serialize and Deserialize BST](#449)<br />BST的查找跟復原只有前序可以；中序會全向右靠；後序的話根要最後才生出，不合理 |      |      |      |             |                                                  |                                  |
| [315 Count of Smaller Numbers After Self](#315)              |      |      |      | △           |                                                  | Not In                           |
| High Freq.                                                   |      |      |      |             |                                                  |                                  |
| [270 Closest Binary Search Tree Value](#270)                 |      |      |      | v           | v                                                |                                  |



## Hash & String

|                                                              |      |              |                                                              | status | coded |         |
| ------------------------------------------------------------ | ---- | ------------ | ------------------------------------------------------------ | ------ | ----- | ------- |
| Hash <br />如果用array當最基本的hash來排序，複雜度會是<br />O(表長＋n) -- 遍歷表長 + 把elem塞進表；當ｎ遠大於表長時吃香<br />用哈希fn將key轉換為整數再對表長取餘，從而關鍵字值被轉換為哈希表的表長範圍內的整數。<br />衝突就是表長不夠大。<br />拉鏈法來解決衝突，插入是頭插法，所以不需要last指針，也就O(1)就插進去了。<br />找的時候是找hash_key 對應的那條linked-list<br />TABLE_LEN選為質數好，可少衝突 |      |              |                                                              |        |       |         |
| [409. Longest Palindrome](#409)                              |      |              |                                                              | v      | v     | Not in  |
| [290 Word Pattern](#290)                                     |      |              |                                                              | v      | v     | Not in  |
| [49 Group Anagrams](#49)                                     |      | sort(string) | onehot coding string                                         | v      | v     | ~438    |
| [3 Longest Substring Without Repeating Characters](#3)       |      |              |                                                              |        |       |         |
| [187 Repeated DNA Sequences](#187)                           |      |              |                                                              |        |       | No t in |
| [76 [ Minimum Window Substring]](#76)                        |      |              |                                                              |        |       | ~209    |
| [161 One Edit Distance](#161)                                |      |              |                                                              | v      |       |         |
| [415 Add Strings](#415)                                      |      |              | 注意地方：<br />1. # if len(num1) > len(num2)    ## CAUTIOUS!!! SHOULD USE WHILE<br/>        while len(num1) > len(num2) and i < len(num1)-1:<br />2. 最後要的答案反轉跟res在append時的type要是str() | v      | v     |         |
| [71 Simplify Path](#71)                                      |      |              |                                                              | v      |       |         |



## Searching

|                                   |      |      |      | status | coded |        |
| --------------------------------- | ---- | ---- | ---- | ------ | ----- | ------ |
| [200 Number of Islands](#200)     |      |      |      |        |       |        |
| [127 Word Ladder](#127)           |      |      |      |        |       |        |
| [473 Matchsticks to Square](#473) |      |      |      |        |       | Not in |
| [107 Trapping Rain Water Ⅱ](#107) |      |      |      |        |       | Not in |



## Dynamic Programming

|                                                              |      |      |      | status                                          | coded                                                        |                             |
| ------------------------------------------------------------ | ---- | ---- | ---- | ----------------------------------------------- | ------------------------------------------------------------ | --------------------------- |
| [70 Climbing Stairs](#70)                                    |      |      |      | v                                               | v                                                            |                             |
| [198 House Robber](#198)                                     |      |      |      | v                                               | v                                                            | Not in                      |
| [53 Maximum Subarray](#53)                                   |      |      |      | v                                               | v                                                            |                             |
| [322 Coin Change](#322) <br />dp[i]代表金额的最優解，就是最小使用張數 |      |      |      | v                                               | v<br />需要注意dp[i-coin]+1的這個１的位置                    | No t in                     |
| [120 Triangle](#120)                                         |      |      |      |                                                 |                                                              | Not in   ~64                |
| [300 Longest Increasing Subsequence](#300)                   |      |      |      | v<br /> O(nlg(n)) should combine with <a>35</a> | v                                                            |                             |
| [64 Minimum Path Sum](#64)                                   |      |      |      |                                                 | v                                                            | Not in ~120                 |
| [174 Dungeon Game](#174)                                     |      |      |      | 之後看…難                                       |                                                              | Not in                      |
| High Freq.                                                   |      |      |      |                                                 |                                                              |                             |
| [121 Best Time to Buy and Sell Stock](#121)                  |      |      |      |                                                 | v                                                            |                             |
| [122 Best Time to Buy and Sell StockⅡ](#122)                 |      |      |      |                                                 | v                                                            |                             |
| [523 Continuous Subarray Sum](#523)                          |      |      |      | v                                               | v 需考慮k 為０的情況                                         |                             |
| [304 Range Sum Query 2D - Immutable](#304)                   |      |      |      | v                                               | v 要注意m, n代表pre_sum的長度所以要補加１，然後matrix都是拿 m-1, n-1的 |                             |
| [303 Range Suym Query - Immutable](#303)                     |      |      |      | v                                               | v<br />做個pre_sum 就ｏｋ要注意長度需加１                    | Not in, but for prep of 304 |
| [1027 Longest Arithmetic Sequence](#1027)                    |      |      |      | v                                               | v                                                            |                             |



## Complex Data Structure

|                                                         |      |                                     |      | Status | coded |        |
| ------------------------------------------------------- | ---- | ----------------------------------- | ---- | ------ | ----- | ------ |
| [208 Implement Trie(Prefix Tree)](#208)                 |      |                                     |      |        |       |        |
| [211 Add and Search Word - Data Structure Design](#211) |      | Trie Tree                           |      |        |       |        |
| [547 Friend Circles](#547)                              |      | 並查集                              |      |        |       | Not in |
| [307 Range Sum Query - Mutable](#307)                   |      | 線段樹！讓update跟query都可是 lg(n) |      |        |       | Not in |



馬走日

八皇后







### 84 

```java
public int largestRectangleArea(int[] heights) {
    if (heights.length == 0) {
        return 0;
    }
    int[] leftBiggerCount = new int[heights.length];
    for (int i = 0; i < heights.length; i++) {
        int count = 1;
        int index = i - 1;
        while (index >= 0 ＆＆ heights[index] > heights[i]) {
            count += leftBiggerCount[index];
            index -= leftBiggerCount[index];
        }
        leftBiggerCount[i] = count;
    }
    int[] rightBiggerCount = new int[heights.length];
    for (int i = heights.length - 1; i >= 0; i--) {
        int count = 1;
        int index = i + 1;
        while (index < heights.length ＆＆ heights[index] >= heights[i]) {
            count += rightBiggerCount[index];
            index += rightBiggerCount[index];
        }
        rightBiggerCount[i] = count;
    }
    int max = 0;
    for (int i = 0; i < heights.length; i++) {
        max = Math.max(max, (rightBiggerCount[i] + leftBiggerCount[i] - 1) * heights[i]);
    }
    return max;
}

```



##### TLE

```python
'''
heights      [2 1 5 6 2 3]
dis_l        [0 1 0 0 3 0]
dis_r        [0 4 1 0 1 0]

For idx in range(len(heights)):
    (dis_l + 1 + dis_r) * heights[idx]

res   [0 (1+4+1)*1, (0+1+1)*2, 0, (1+1+1)*2, 0]
return max(res)
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        n = len(heights)

        # left[i], right[i] represent how many bars are >= than the current bar

        left = [1] * n		# SHOULD START fr 1 to avoid -1 idx problem for left arr
        right = [1] * n
        max_rect = 0

        # calculate left
        for i in range(0, n):
            j = i - 1
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    j -= left[j]
                else: break

        # calculate right
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else: break

        for i in range(0, n):
            max_rect = max(max_rect, heights[i] * (left[i] + right[i] - 1))

        return max_rect
```



* 

85 

v1 ~v5 

local 

### <a name="22">22</a>

```python
# 2 ==> 4 symbols
# (()), ()()
# ((((, ((()

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        result = []
        self.gen(0, '', "", result, n, n)
        return result
        
    def gen(self, i, symbol, item, result, left, right):
        # if i >= self.n * 2:
        #     return
        item = item + symbol # item.push_back()
        
        if not left and not right:
            result.append(item) # result.push_back(item)
            return

        if left > 0:    # pruning 
            self.gen(i+1, '(', item, result, left-1, right)   
        
        if right > 0 and right > left:
            self.gen(i+1, ')', item, result, left, right-1)
            
```



### <a name="23">23</a>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # val, index 
        # 1, 0
        # 1, 1
        # 2, 2
        if not lists:
            return None
        # if not lists[0]:
        #     return None
        
        l = []  # for heapq
        for i in range(len(lists)):
            if lists[i]:                # CAUTION! for [[],[1]]
                val, idx = lists[i].val, i
                heapq.heappush(l, (val, idx))
            # lists[idx] = lists[idx].next  # CAUTION! 別跟31行重覆了
        
        root = curr = ListNode(-1)
        while True:
            if not l:
                break
            val, idx = heapq.heappop(l)
            # print(val, idx)
            # for update heapq
            lists[idx] = lists[idx].next

            if lists[idx] is not None:
                heapq.heappush(l, (lists[idx].val, idx))
                
            # for Result
            curr.next = ListNode(val)
            curr = curr.next
        
        return root.next
        
```



### <a name="31">31</a>

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #　把頂點前的那個值跟最後的換，然後後半進行排序
        if not nums or not len(nums):
            return nums
        if len(nums) == 1:
            return nums
        
        #    1,2,6,4,2
        # => 1,4,2,2,6 
        replace = len(nums)-2
        while replace >= 0 and nums[replace] >= nums[replace+1]:   # CAUTIOUS! ">="
            replace -= 1

        if replace < 0:  # 5,1,1 # 6,5,4,3,2,1
            # nums = sorted(nums)    # sorted function not in-place
            i = 0
            p, q = i, len(nums)-1-i
            while p < q:
                nums[p], nums[q]= nums[q], nums[p]
                p += 1
                q -= 1
            return
        print(replace)
        
        next_larger = replace + 1
        while  next_larger < len(nums) and nums[next_larger] > nums[replace]:
            next_larger += 1
        next_larger -= 1
        
        print(next_larger)
        nums[replace], nums[next_larger] = nums[next_larger], nums[replace]
        i = 0
        p, q = replace+1, len(nums)-1
        print(nums, p, q)
        while p < q:
            nums[p], nums[q]= nums[q], nums[p]
            p += 1
            q -= 1
        return
        
        
        # return 
```



### <a name="33">33</a>

```c++
class Solution {
public:
	int search(vector<int> nums, int target) {
		//对于特殊情况的判断
		if(nums.size()==0) return -1;
		if(nums.size()==1 && nums[0]==target) return 0;
		if(nums.size()==1 && nums[0]!=target) return -1;
		int index= 0 ; //记录轴点
		int size = nums.size();//记录下初始数组的长度
		for(int i=0;i<nums.size();i++){
			if(nums[i]<nums[i-1]){
				index = i; //找到轴点后结束循环
				break;
			}
			nums.push_back(nums[i]); //在找到轴点之前，将轴点前数字依次放在数组尾部
		}
		int left = index; //left = 轴点
		int right = nums.size()-1; //right = 数组当前长度-1 
		int ans = -1;//ans表示最终的位置
		while(left<=right){
			int mid = (left+right)/2; //计算中点
			if(nums[mid]==target){
				ans = mid; //如果nums[mid] == target 
				break;
			}
			if(nums[mid]<target) left = mid+1; //如果nums[mid]<target 修改left
			if(nums[mid]>target) right = mid-1; //如果 nums[mid]>target 修改 right
			if(nums[right] == target ) ans = right; //如果 nums[right] == target 将 ans修改为right 否则ans为-1
			else ans = -1;
		}
		return ans % size;
	}
};
```



### <a name="34">34</a>

##### Use bisect built-in for 'r' !

```python

from bisect import * # bisect_left() bisect_right()
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r-l)//2
                    # 5 7 7  8 8 10
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        ans_l = l   # == bisect_left(nums, traget)
        # if nums[l] != target:
        #     ans_l = -1
        
        ans_r = bisect_right(nums, target) # SHOULDN'T  - 1
        
        if ans_l == ans_r:
            ans_l = ans_r = -1
        else:
            ans_r -= 1
        return (ans_l, ans_r)
```

```python
def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo
```



##### W/O Bisect

```python
class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        left, right = -1, -1
        l, r = 0, n-1
        while l < r:
            m = (l+r)/2
            if nums[m] < target: l = m+1
            else: r = m
        if nums[l] != target: return -1, -1
        left = l
        l, r = left, n-1
        while l < r:
            m = (l+r)/2+1
            if nums[m] == target: l = m
            else: r = m-1
        right = l
        return left, right
```



### <a name="35">35</a>

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l + r)//2
            
            if target == nums[mid]:
                return mid
            elif target <= nums[mid]:
                r = mid-1
            else: 
                l = mid+1
        # res = l if nums[l]>target else l-1 
        if target > nums[l]:
            res = l+1
        else:
            res = l
        return res    ### 該思考比mid大或小的時候；還有該思考邊界條件時
```



### <a name="42">42</a>

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # l_max =  [0 0 1 1 2 2 2 2 3 3 3 3]
        # r_max =  [3 3 3 3 3 3 3 2 2 2 1 0]
        # min_nbr = min(l_max[i], r_max[i])
        # water[i] = height[i] < min_nbr ? (min_nbr-height[i]) * 1:0
        # return sum(water)
    
        n = len(height)
        l_max = [0] * n
        cur_max = 0
        for i in range(n):
            l_max[i] = cur_max
            cur_max = max(height[i], cur_max)
            
        r_max = [0] * n
        cur_max = 0
        for j in reversed(range(n)):
            r_max[j] = cur_max
            cur_max = max(height[j], cur_max)
            
        
        res = 0
        for k in range(n):
            min_nbr = min(l_max[k], r_max[k])
            res += (min_nbr-height[k])*1 if height[k] < min_nbr else 0
            
        return res
```



### <a name="46">46</a> & <a name="47">47</a>

```python
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        c_map = Counter(nums)
        # 1: 2
        # 2: 1
        keys = sorted(dict(c_map))  #[1, 2]
        arr = []
        counts = []
        for key in keys:
            arr.append(key)     # [1, 2]
            counts.append(c_map[key])   # [2, 1]
        item = [0 for i in range(len(nums))]
        self.result = []
        self.helper(arr, counts, item, 0)
        return self.result
    
    def helper(self, arr, counts, item, level):
        if len(item) == level:
            if item not in self.result:
                self.result.append(item.copy())
            return
        
        for i in range(len(arr)):
            if counts[i] == 0:
                continue
            # item.append(arr[i])
            item[level] = arr[i]
            counts[i] -= 1
            self.helper(arr, counts.copy(), item.copy(), level+1)
            counts[i] += 1
```



### <a name="49">49</a>

```python
class Solution:
    # def __init__(self):
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        # build a one-hot mapping 
        for s in strs:
            onehot = self.chars2onehot(s)
            # if onehot not in d: # unhashable type: 'list' CAUTIOUS! should turn into tuple for hashable
            if tuple(onehot) not in d:
                d[tuple(onehot)] = [s]  # [100101] ==> eat
            else:
                d[tuple(onehot)].append(s)
            # d[onehot] = d.get(onehot, 0) + 1
            # {[1 0 0 0 0 1 0 0 1 0 ]}
        
        ret = []
        for key in d.keys():
            ret.append(d[key])
        
        return ret
        
    def chars2onehot(self, s):
        onehot = [0] * 26
        for c in s:
            onehot[ord(c)-97] += 1  # 97 is ord('a') CAUTIOUS!!
        
        return onehot
```



### <a name="56">56</a>

```python
'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
  *---*
 cur_i cur_j
    *-------*
    tmp_i   cur_j
                   *---*
               tmp_i   tmp_j
                                    *--------*
start i to end j
push (i,j) into priority que, so that the min-heap use i as key
    
while min-heap:
    pop the (i, j) pair and if curr j > than next i of pop() from min-heap, keep poping()
    if j <= next i:
        count += 1
'''
import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        l = []
        intervals = sorted(intervals)
        
        # for idx in range(len(intervals)):
        #     heapq.heappush(l, intervals[idx])         # n*lg(n)
        heapq.heapify(intervals)    # O(n)
        l, h = heapq.heappop(intervals)
        result = []
        while intervals:
            next_int = heapq.heappop(intervals)
            if next_int[0] <= h:        # CAUTIOUS, SHOULD BE '='
                h = max(h, next_int[1])
            else:
                result.append([l, h])          
                l = next_int[0]
                h = next_int[1]
        result.append([l, h])    
        return result
```



### <a name="71">71</a>

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()
        path = [p for p in path.split('/') if p]
        for f in path:
            if f == '.': 
                continue
            elif f == '..': 
                if stack: 
                    stack.pop()
            else: 
                stack.append(f)

        return '/'+'/'.join(stack)

```



### <a name="74">74</a>

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >= 0: # target != curr:
            curr = matrix[i][j]
            print(curr)
            if curr > target:   # 7 > 3
                j = j - 1
            elif curr < target:    # 7 < 13
                i = i + 1
            else:
                return True
            
        return False
```



### <a name ="78">78</a>

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        self.helper(0, nums, [], result)
        
        return result
        
    def helper(self, i, nums, item, result):
        if i >= len(nums):
            return
        
        item += [nums[i]]
        result.append(item)
        self.helper(i+1, nums, item.copy(), result)
        item = item[:-1]
        self.helper(i+1, nums, item.copy(), result)
        
```



### <a name="88">88</a>

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            
        num_zeros = len(nums1) - len(nums2)
        idx_1 = num_zeros - 1
        idx_2 = len(nums2) - 1

        k = -1
        while idx_1 >= 0 and idx_2 >= 0:
            if nums1[idx_1] >= nums2[idx_2]: # CAUTIOUS! case of "="
                nums1[k] = nums1[idx_1]
                idx_1 -= 1
            elif nums1[idx_1] < nums2[idx_2]:
                nums1[k] = nums2[idx_2]            
                idx_2 -= 1
            
            k -= 1
            
        # if idx_2 < 0:
        #     nums1[0:len(nums1)+k] = nums1[:]
        if idx_1 < 0:
            nums1[0:len(nums1)+k+1] = nums2[0:idx_2+1]
            
        
```



### <a name="102">102</a>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        res = []
        while que:
            # node = que.popleft()
            level_length = len(que)
            level_res = []
            for i in range(level_length):
                node = que.popleft()
                level_res.append(node.val)
                if node.left:
                    # level_l.append(node.left)
                    que.append(node.left)
                if node.right:
                    # level_l.append(node.right)
                    que.append(node.right)
            
            res.append(level_res.copy())
        return res
        
```



### <a name="104">104</a>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.height(root)
        
    def height(self, root):
        if not root:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        
        return 1 + max(l, r)
```



### <a name="105"> 105</a>

```python
# preorder: [3,9,20]
# inorder:  [9,3,20]
    3
   / \
  9  20
class Solution(object):
  def buildTree(self, inorder, preorder):
		if not inorder:
      return inorder
    #val = preorder.pop(0)
    #idx = inorder.index(val)	# lg(n)
    #result = node = TreeNode(inorder[idx])
    #result = TreeNode(-1)
    root = self.build(inorder, preorder)#, None, result)
    
    return root
  
  def build(self, inorder, preorder):
    if not node:
      return
    val = inorder.index(preorder.pop(0))
    #result = item
    item = root = TreeNode(val)
    root.left = self.build(inorder[:mid], preorder)
    root.right = self.build(inorder[mid+1:], preorder)
		
    return root

```



### <a name="111">111</a>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        return self.helper(root)
    
    def helper(self, root):
        if not root:
            return 0
        ans = 0
        if root.left and root.right:
            ans = min(self.helper(root.right), self.helper(root.left)) + 1
        else:
            # if not root.left and not root.right:
            #     ans = 0
            # elif (not root.left and root.right) or (root.left and not root.right):
            l = self.helper(root.left)
            r = self.helper(root.right)
            ans = 1 + max(l, r)
        
        return ans

```



### <a name="121">121</a>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[0] = 7
        # dp[1] = prices[1]>prices[0]?diff(prices[1], prices[0]), 0
        # dp[2] = max(prices[2]-curr_min, g_max_profit)
        # curr_min to record minimum
        if not prices:
            return 0
        cur_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            cur_min = min(cur_min, prices[i])
            max_profit = max(max_profit, prices[i]-cur_min)
        
        return max_profit
```



### <a name="122">122</a>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
               if prices[i+1]  > prices[i]:
                    res += prices[i+1] - prices[i]
                    
        return res
            
```



### <a name="145">145</a>

```python
class Solution:
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.helper(root)
        return self.result
    
    def helper(self, node):
        if not node:
            return 
        
        self.helper(node.left)
        self.helper(node.right)
        self.result.append(node.val)
```



### <a name="161">161</a>

```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        '''
        不能使用Counter，因為char之間的順序也要被考慮進來……
        以下的case就會 Failed...
        "teacher"
        "detacher"
        '''
        if s == t:
            return False
        l1, l2 = len(s), len(t)
        if l1 > l2: # force s no longer than t
            return self.isOneEditDistance(t, s)
        if l2 - l1 > 1:
            return False
        for i in xrange(len(s)):
            if s[i] != t[i]:
                if l1 == l2:
                    s = s[:i]+t[i]+s[i+1:]  # replacement
                else:
                    s = s[:i]+t[i]+s[i:]  # insertion
                break
        return s == t or s == t[:-1]

```



### <a name="173">173</a>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.l = []
        self.trvs(root)
        
    def trvs(self, root):
        
        if not root:
            return None
        
        heapq.heappush(self.l, root.val)
        self.trvs(root.left)
        self.trvs(root.right)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return heapq.heappop(self.l)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.l:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```



### <a name="199">199</a>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        que = deque([root])
        res = []
        while que:
            leng_level = len(que)
            level_l = []
            for i in range(leng_level):
                v = que.popleft()
                if not v:
                    continue
                level_l.append(v.val)
                if v.left:
                    que.append(v.left)
                if v.right:
                    que.append(v.right)
            res.append(level_l)
        
        return [item[-1] for item in res]
```



### <a name="207">207</a> TBP

```python
# exmample: 4, [[1,0],[2,0],[3,1],[3,2]]
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        G = [[] for i in range(n)]
        degrees = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degrees[j] += 1    
    
        '''
        0 -> 1 ------> 3
          \        /
            -> 2 --
            idx    0 1 2 3
        degrees = [0 1 1 2]
        G = [[1,2], [3], [3], []]
        
        Q = [0]
            idx
        ''' 
        Q = deque([])
        [Q.append(idx) for idx, degree in enumerate(degrees) if degree == 0]        
        visited = []
        while Q:
            v_idx = Q.popleft()    
            # visited.append[v_idx]
            for j in range(len(G[v_idx])):
                next_v_idx = G[v_idx][j] # 1, then 2
                degrees[next_v_idx] -= 1
                if degrees[next_v_idx] == 0:
                    Q.append(next_v_idx)
        
        return not any(degrees) # check whether any element in degrees is larger than 0
            
```



### <a name="209">209</a>

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        '''
                [2,3,1,2,4,3]
        ps =    [0,2,5,6,8,12,15]    # pre_sum

        curr_idx 0
        result = float('inf')
        if diff  (8-curr_idx) - 7 >= 0 
            result = min(result, 8-curr_idx)
            update curr_idx to index of value 8
        '''
        if not nums:
            return 0
        
        accu = 0
        ps = [0] * (len(nums)+1)
        for i in range(1, len(ps)):
            accu += nums[i-1]
            ps[i] = accu
            
        # ps[-1] = ps[-2] + nums[-1]
        print(ps)
        
        curr_idx = 0
        result = float('inf')
        for k in range(1, len(ps)):
            
            # SHOULD REPLACE THIS W/ B-SEARCH, to search the residual
            # if ps[k]-ps[curr_idx] - s >= 0:
            if ps[k]-ps[curr_idx] - s >= 0:    
                while ps[k]-ps[curr_idx] - s >= 0:
                    curr_idx += 1
                curr_idx -= 1
            
                result = min(result, k-curr_idx)
                # curr_idx = k
        
        if result == float('inf'):
            result = 0
        return result
        
        
            
        
```



### <a name="210">210</a>

```python
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        G = [[] for i in range(n)]
        degrees = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degrees[j] += 1    
    
        '''
        0 -> 1 ------> 3
          \        /
            -> 2 --
            idx    0 1 2 3
        degrees = [0 1 1 2]
        G = [[1,2], [3], [3], []]
        
        Q = [0]
            idx
        ''' 
        Q = deque([])
        [Q.append(idx) for idx, degree in enumerate(degrees) if degree == 0]        
        # visited = []
        result = [] # as a stack
        [result.append(idx) for idx in Q]     # [0], result = Q.copy()
        while Q:
            v_idx = Q.popleft()    
            # visited.append[v_idx]
            
            for j in range(len(G[v_idx])):
                next_v_idx = G[v_idx][j] # 1, then 2
                degrees[next_v_idx] -= 1
                if degrees[next_v_idx] == 0:
                    Q.append(next_v_idx)
                    result.append(next_v_idx)
        if len(result) != numCourses:
            result = list() 
        return result
```



### <a name="215">215</a>

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if not nums:
            return 0
        
        l = [-1*num for num in nums]
        heapq.heapify(l)
 
        for i in range(k-1):
            heapq.heappop(l)
        return heapq.heappop(l) * -1
```



```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq._heapify_max(nums)
        for i in range(k-1):
            heapq._heappop_max(nums)
        return heapq._heappop_max(nums)
```



### <a name="210">210</a>

```python
class Solution:
    def addEdge(self, child, parent, adjList):
		#Creating Adjacency List
        if parent in adjList:
            adjList[parent].append(child)
        else:
            adjList[parent] = [child]
        
    def TopoSort(self, course: int, adjList, visited: List, res: List):
        #print("course: {}, visited: {}, res: {}".format(course, visited, res))
		# Checking if the courses is in the recursion stack. If yes, then exit;
        if visited[course] == 1: res.clear(); return False
		
		#If the course has already been visited, then return
        if visited[course] == 2: return True
        
        visited[course] = 1
        if course in adjList:
            for c in adjList[course]:
                if not self.TopoSort(c, adjList, visited, res): return False
    
        visited[course] = 2
        res.insert(0, course)
        return True
            
                

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        res = []
        visited = [0] * numCourses
        for course in prerequisites:
            c, pre = course
            self.addEdge(c, pre, adjList)
        #print("adjList: ", adjList)
        for course in range(numCourses):
            if visited[course] != 2 :
                if not self.TopoSort(course, adjList, visited, res): break
        return res
        
```



### <a name="252">252</a>

```python
# MORE LIKE [start, end), where [ means close, ( means open
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        heapq.heapify(intervals)
        
        l, h = heapq.heappop(intervals)
        result = []
        while intervals:
            next_ = heapq.heappop(intervals)
            if next_[0] >= h:
                # result.append([l, h]) # NOT USED HERE
                l, h = next_[0], next_[1]
            else:
                return False
                # UPDATE h
                # h = max(h, next_[1])   # NOT USED HERE
        
        return True
        # return result
```



### <a name="253">253</a>

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        intervals = sorted(intervals, key=lambda x:x[0]) # Sort by start value
        heap = []
        for i in intervals:
            if heap and heap[0] <= i[0]:
                # If the new start time is greater than or equal to the exist end time, means the room has been released, replace the previous time with the new ending time
                heapq.heapreplace(heap, i[-1])
            else:
                # The room is still in use, add (push a new end time to min heap) a new room
                heapq.heappush(heap, i[-1])
        return len(heap)
```



### <a name="270">270</a>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return 0
        
        que = deque([root])
        min_g = float('inf')
        res = que[0].val
        
        while que:
            v = que.popleft()
            if abs(v.val - target) < min_g:
                min_g = abs(v.val - target)
                res = v.val
            if v.left:
                que.append(v.left)
            if v.right:
                que.append(v.right)
        return res
            
        
```

O(N)



```phthon
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
```

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200201202254537.png" alt="image-20200201202254537" style="zoom:50%;" />

- Time complexity : O(*H*) since here one goes from root down to a leaf.
- Space complexity : O(1).

### <a name="301">301</a>

```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        lefts_to_remove, rights_to_remove = 0, 0
        lefts, rights = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                lefts += 1
            elif s[i] == ')':
                if lefts > 0:
                    lefts -= 1
                else:
                    rights_to_remove += 1 #if right doesn't have a matching left, it should be removed
        lefts_to_remove = lefts #if we have more lefts than rights, extra lefts should be removed
        
        self.backtracking(0, 0, s, 0, '', ans, lefts_to_remove, rights_to_remove)
        if not ans:
            ans.append('')
        
        return ans
                    
    
    def backtracking(self, lefts, rights, s, ind, cur_str, ans, lefts_to_remove, rights_to_remove):
        if ind == len(s):
            if lefts == rights and lefts_to_remove==0 and rights_to_remove==0 and cur_str not in ans:
                ans.append(cur_str)
            return
        
        if s[ind] == '(':
            if lefts_to_remove > 0:
                self.backtracking(lefts, rights, s, ind+1, cur_str, ans, lefts_to_remove-1, rights_to_remove)
            self.backtracking(lefts+1, rights, s, ind+1, cur_str+'(', ans, lefts_to_remove, rights_to_remove)
            
        elif s[ind] == ')':
            if (lefts==0 or lefts>=rights) and rights_to_remove > 0:
                self.backtracking(lefts, rights, s, ind+1, cur_str, ans, lefts_to_remove, rights_to_remove-1)
            if lefts > rights:
                self.backtracking(lefts, rights+1, s, ind+1, cur_str+')', ans, lefts_to_remove, rights_to_remove)
            
        else:
            self.backtracking(lefts, rights, s, ind+1, cur_str+s[ind], ans, lefts_to_remove, rights_to_remove)
```



### <a name="303">303</a>

```python
# nums    =       [-2  0  3 -5  2 -1]          
# pre_sum  =    [0 -2 -2  1 -4 -2 -3]
class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0] + [0] * len(nums)
        accu = 0
        for idx in range(1, len(self.pre_sum)):
            accu += nums[idx-1]
            self.pre_sum[idx] = accu
						# FOLLOWING IS FASTER THAN PREVIOUS LINE
            self.pre_sum[idx] = self.pre_sum[idx-1] + nums[idx-1]
        # print(self.pre_sum)
            

    def sumRange(self, i: int, j: int) -> int:
            return self.pre_sum[j+1] - self.pre_sum[i]
```

**Complexity analysis**

- Time complexity : O(1)*O*(1) time per query, O(n)*O*(*n*) time pre-computation. Since the cumulative sum is cached, each *sumRange* query can be calculated in O(1)*O*(1) time.
- Space complexity : O(n)*O*(*n*).

### <a name="304">304</a>

```python
'''
A
3 0 1
5 6 3
1 2 0

presum of A
0 0 0 0 
0 3 3 4
0 8    
0 9

For A_presum[2][2] = 3+5+6 = 14 or -1+3+8+6 = 14
                    A[0][0]         -1*p_A[2-1][2-1]
                    A[0][1]         p_A[2][2-1]
                    A[1][0]         p_A[2-1][2]
                                    nums[2-1][2-1]
'''             
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return None
        
        m, n = len(matrix)+1, len(matrix[0])+1   # row and col for pre_sum matrix
        pre_sum = [[0 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                pre_sum[i][j] =  -1*pre_sum[i-1][j-1] + pre_sum[i][j-1] + pre_sum[i-1][j] + matrix[i-1][j-1]
              
        self.pre_sum  = pre_sum

    '''
    For the region (r1, c1) (r2, c2)
        A[row2+1][col2+1] - A[row2+1][col1] - A[row1][col2+1] + A[row1][col1]
    '''
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        A = self.pre_sum
        ans = A[row2+1][col2+1] - A[row2+1][col1] - A[row1][col2+1] + A[row1][col1]
        return ans
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```

- Time complexity : O(1)*O*(1) time per query, O(mn)*O*(*m**n*) time pre-computation. The pre-computation in the constructor takes O(mn)*O*(*m**n*) time. Each *sumRegion* query takes O(1)*O*(1) time.
- Space complexity : O(mn)*O*(*m**n*). The algorithm uses O(mn)*O*(*m**n*) space to store the cumulative region sum.

### <a name="340">340</a>

```python
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # {e:[0, 2], c:[1]}   l=0 r=r2 len=3
        # or
        # {e:2, c:1}
        if k == 0:
            return 0
        
        d = defaultdict(int)   
        j = 0
        max_len = 0
        for idx in range(len(s)):
            if s[idx] not in d:
                d[s[idx]] = 0
            else:
                d[s[idx]] += 1
            while len(d) > k and j < idx:
                if d[s[j]] > 0:
                    d[s[j]] -= 1
                else:
                    del d[s[j]]
                j += 1
            max_len = max(max_len, idx - (j-1))        
        return max_len  
```



### <a name="349">349</a>

##### Naive -- O(mxn)

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # _len = min(len(nums1), len(nums2))
        _len = len(nums1)
        if len(nums2) < len(nums1):
            _len = len(nums2)       # CAUTIOUS!!! should be prior to Line8
            nums1, nums2 = nums2, nums1
            # _len = len(nums2)
            
        result = []
        for i in range(_len):
            # print(i, nums1)
            if nums1[i] in nums2 and nums1[i] not in result:
                result.append(nums1[i])
        return result     
```



##### turn list into set, 'cause set is implemented in hash, thus O(m+n)

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1, set2 = set(nums1), set(nums2)
        
        if len(set2)< len(set1):
            set1, set2 = set2, set1
        res = []
        for item in set1:
            if item in set2:
                res.append(item)
                
        return res
```



### <a name="350">350</a>

```python
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return set.intersection(set(nums1), set(nums2))
        d_a = Counter(nums1)
        # b = Counter(nums2)
        res = []
        for j in range(len(nums2)):
            if d_a.get(nums2[j], 0) != 0:
                d_a[nums2[j]] -= 1
                # res.append(d_a[nums2[j]])
                res.append(nums2[j])
            else:
                d_a[nums2[j]] = 0
        
        return res
```



### <a name="378">378</a>

##### Sol1: Iterate all mxn 2D array 

```python
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: 
            return 0
        if not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        heap_l = []
        for i in range(m):
            for j in range(n):
                heapq.heappush(heap_l, matrix[i][j])    # mxnxlg(mxn)    
                # heapq.heappush
                
        for tmp in range(k-1):
            heapq.heappop(heap_l)
            
        return heapq.heappop(heap_l)
```



##### Sol2: heapq helps manage each row's pointer

```python
import heapq
from collections import deque
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return -1
        if not matrix[0]:
            return -1
        
        m, n = len(matrix), len(matrix[0])
        
        l = []
        for i in range(m):
            heapq.heappush(l, (matrix[i][0], i, 0))	# m x lg(m)
            
        for idx in range(k-1):
            val, i, j = heapq.heappop(l)    # k x lg(m)
            if j < n-1: # n-2
                heapq.heappush(l, (matrix[i][j+1], i, j+1))    # k x lg(m)
        val, i, j = heapq.heappop(l)
        return val
        
```

##### Sol3: Binary 

```python
import heapq
from collections import deque
from bisect import bisect
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return -1
        if not matrix[0]:
            return -1
        
        m, n = len(matrix), len(matrix[0])
        
        lo, hi = matrix[0][0], matrix[m-1][n-1]
        
        while lo < hi:
            mid = (lo + hi)//2
            amount = 0
            for j in range(m):
                amount += bisect(matrix[j], mid)
            print(amount)
            if amount < k:  # No EQUALS!!!
                lo = mid+1
            else: 
                hi = mid
            # amount = bisect()
        return lo
```



### <a name="392">392</a>

```python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        queue = collections.deque(s)
        for c in t:
            if not queue: return True
            if c == queue[0]:
                queue.popleft()
        return not queue
```



### <a name="438">438</a>

##### TLE...

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        p ==> onehot arr
        a b c , [1,1,1,0 0 0... 0], len == 26
        b a c 
        
        
        trvs string s w/ sliding window
        fr idx 0 to idx len(s)-1-len(p) to check
        '''
        
        # result = [-1]   # means p NOT within s
        window = len(p)
        d = {}  # {[1 1 1 0 0 0 ]:
                #     ['abc', 'cba'...]
                # }
        onehot_p = self.onehot2encode(p)
        d[tuple(onehot_p)] = []
        
        for k in range(len(s)-(window-1)):
            pat = s[k:k+window] # CAUTIOUS! k:k+window!!!
            onehot = self.onehot2encode(pat)
            # use onehot as key 
            # if onehot not in d:
            #     # d[onehot_t] = [pat]
            #     d[onehot] = [k]
            if tuple(onehot) in d:
                d[tuple(onehot)].append(k)
        
        ans = d[tuple(onehot_p)]
        # if not ans: # ans is []
        #     ans = [-1]
        return ans
    
    def onehot2encode(self, p):  # bucket sort
        onehot = [0] * 26
        for i in range(len(p)):
            onehot[ord(p[i]) - ord('a')] += 1 
        return onehot
         # [1,1,1,0 0 0... 0]
    
```

##### Sliding Window

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        p ==> onehot arr
        a b c , [1,1,1,0 0 0... 0], len == 26
        b a c 
        
        
        trvs string s w/ sliding window
        fr idx 0 to idx len(s)-1-len(p) to check
        '''
        
        window = len(p)
        d = {}  # {[1 1 1 0 0 0 ]:
                #     ['abc', 'cba'...]
                # }
        onehot_p = self.onehot2encode(p)
        
        onehot_s = [0] * 26
        ans = []
        for k in range(len(s)):
            onehot_s[ord(s[k])-ord('a')] += 1
            if k >= window:
                onehot_s[ord(s[k-window])-ord('a')] -= 1
                
            if onehot_s == onehot_p:
                ans.append(k-window+1)
                       
        return ans
        
        
        '''
        for k in range(len(s)-(window-1)):
            pat = s[k:k+window] # CAUTIOUS! k:k+window!!!
            
            DON'T HAVE TO CALC ENCODING OF EACH P
            onehot = self.onehot2encode(pat)
            # use onehot as key 
            # if onehot not in d:
            #     # d[onehot_t] = [pat]
            #     d[onehot] = [k]
            if tuple(onehot) in d:
                d[tuple(onehot)].append(k)
                        
        ans = d[tuple(onehot_p)]
        # if not ans: # ans is []
        #     ans = [-1]
        return ans
        ''' # TLE
        '''
        lookup = set([]) # to record p already showed up in s 
        ans = []
        for k in range(len(s)-(window-1)):
            pat = s[k:k+window]
            if pat in lookup:
                ans.append(k)
            else:
                # CALCULATE ENBEDDING
                onehot = self.onehot2encode(pat)
                if onehot == onehot_p:
                    ans.append(k)
        return ans
        ''' # STILL TLE
        
        

    
    def onehot2encode(self, p):  # bucket sort
        onehot = [0] * 26
        for i in range(len(p)):
            onehot[ord(p[i]) - ord('a')] += 1 
        return onehot
         # [1,1,1,0 0 0... 0]
    
```



### <a name="523">523</a>

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        1. loop nums
            for start
                for end
                    for btw start end to check the sum
        
            O(n^3) 3 power of n
        2. build a pre_sum , cumulative sum --> cs
            [23, 2, 4,  6   7 ]
          =>[0, 25, 29, 35, 42]  O(n)
        
            for start ()
                for end to len(1, cs)
                    check 
                    cs[end] - cs[start] + nums[i]
        3. pre_sum 
            [23, 2, 4,  6   7 ]
          =>[0, 23, 25, 29, 35, 42]  O(n)  cs
            {
                0:0
                23:1
                25:2
            } ==> {cum: i}
            
            k = 6
            residual = 29 - 6 == > 23 @ cs[1] and check index to know interval > 1,  curr - i > 1 
            then return True!
        '''
        
        pre_sum = [0] + [0] * len(nums)
        cum = 0
        for idx in range(len(nums)):
            cum += nums[idx]
            pre_sum[idx+1] = cum 

        if k == 0:
            '''
            [0 0 0 0 0 0]
          [0 0 0 0 0 0 0]
            '''
            # d = {0:0}
            for idx in range(len(pre_sum)-2):
                if pre_sum[idx] == pre_sum[idx+2]:
                    return True
            return False
            
        # lookup = {0:0}
        lookup = {k:0}
        '''
          [23, 2, 4, 6, 7]
        [0,23, 25, 29, 35, 42 ]  k==6
        lookup {6-23%6:1, 6-25%6:2, }
               {0:0, 1:1, 5:2, 1(HIT!):3(X), 1:4(X), }
                3-1 > 1 ==> True! 
                
          [23, 2, 6, 4, 7]
        [0,23, 25, 31, 35, 42 ]  k==6
        lookup {6-23%6:1, 6-25%6:2, }
               {0:0, 1:1, 5:2, 5:3(X), 1:4(X), }
        '''
        for j in range(1, len(pre_sum)):
            # pre_sum[j]
            # if pre_sum[j] not in lookup:
            #     lookup[pre_sum[j]] = j
            mod = k - pre_sum[j]%k    
            if mod not in lookup:
                lookup[mod] = j
            
            if j - lookup[mod] > 1:
                return True

        return False

```



### <a name="825">825</a>

```python
import collections
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        """
        :type ages: List[int]
        :rtype: int
        """
        cnt = collections.Counter(ages)
        ans = 0
        for age in ages:
            cnt[age] -= 1
            left, right = age // 2 + 8, age
            ans += sum(cnt[age] for age in range(left, right + 1))
            cnt[age] += 1
        return ans
```



### <a name="896">896</a>

```python
class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing
```



### <a name="907">907</a>

```python
'''
heights      [2 1 5 6 2 3]
dis_l        [0 1 0 0 3 0]
dis_r        [0 4 1 0 1 0]

For idx in range(len(heights)):
    (dis_l + 1 + dis_r) * heights[idx]

res   [0 (1+4+1)*1, (0+1+1)*2, 0, (1+1+1)*2, 0]
return max(res)
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        n = len(heights)

        # left[i], right[i] represent how many bars are >= than the current bar

        left = [1] * n
        right = [1] * n
        max_rect = 0

        # calculate left
        for i in range(0, n):
            j = i - 1
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    j -= left[j]
                else: break

        # calculate right
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else: break

        for i in range(0, n):
            max_rect = max(max_rect, heights[i] * (left[i] + right[i] - 1))

        return max_rect
```



### <a name="953">953</a>

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 1. build mapping score for each c in order str
        # 2. assign pointer at head of each of the word in words and check the mapping score relationship
        # 3. empty hel'' < hel'l'
        
        if not words or not order: return False
        score = {'':0}
        for idx in range(len(order)):
            score[order[idx]] = idx+1
            
        n = len(words)
        
        for i in range(len(words)-1):
            # compare word by word
            a, b = words[i], words[i+1]
            _len = min(len(a), len(b))
            for k in range(_len):
                if score[a[k]] < score[b[k]]:
                    break
                elif score[a[k]] == score[b[k]]:
                    continue
                if score[a[k]] > score[b[k]]:    # SERIOUSLY WRONG!!! NOT EACH CHAR, ONLY FIRST CHAR to be compared!!!
                    # print(a[k], b[k])
                    return False
                
            # if len(a) > len(b):   # for [apple, app], but failed when [kuvp, q]
                # return False
            if len(a) > len(b) and a[:_len] == b:
                return False
        return True
```



### <a name="958">958</a>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        have_null = False
        Q = [root]
        
        while Q:
            cur_node = Q.pop(0)
            if not cur_node: 
                have_null = True
                continue
            if have_null: return False
            Q.append(cur_node.left)
            Q.append(cur_node.right)
            
        return True
```



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        res = []
        q = collections.deque([(root, 1)])
        while q:
            node, pos = q.popleft()
            res.append(pos)
            if node.left:
                q.append((node.left, 2 * pos))
            if node.right:
                q.append((node.right, 2 * pos + 1))
            
        return len(res) == res[-1]
```



### <a name="1027">1027</a>

```python
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        # [3,6,9,12,13]
        # when i=1, A[i]=6:
        # dp=[{3:2}]
        # when i=2, A[i]=9:
        # dp=[{3:2}, {6:2, 3:3}]
        # when i=2, A[i]=12:
        # dp=[{3:2}, {6:2, 3:3}, {9:2, 6:2, 3:4}, {10:2, 7:2, 4:2, 1:2}]
        # return max([2,3,4,2])
    
        dp = [dict() for i in range(len(A))]
        max_len = 2
        for i in range(1, len(A)):
            for j in range(i):
                dp[i][A[i] - A[j]] = dp[j].get(A[i] - A[j], 1) + 1   # min length btw 2 items is 2
                max_len = max(max_len, dp[i][A[i] - A[j]])
            # print(dp[i])
        return max_len
    
    
    
        dp = [dict()]
        ret = 2
        for i in range(1, len(A)):
            dp.append({})
            for j in range(i):
                dp[i][A[i] - A[j]] = dp[j].get(A[i] - A[j], 1) + 1
                # ret = max(ret, dp[i][j]);
        # print(dp)
        # print(max([max(i.values()) for i in dp if i.values()]))
        ret = max([max(i.values()) for i in dp if i.values()])
        return ret
```

Time: O(n^2)
Space: O(n^2)

ref : [https://leetcode.flowerplayer.com/2019/04/12/leetcode-907-sum-of-subarray-minimums-%e8%a7%a3%e9%a2%98%e6%80%9d%e8%b7%af%e5%88%86%e6%9e%90/](https://leetcode.flowerplayer.com/2019/04/12/leetcode-907-sum-of-subarray-minimums-解题思路分析/)