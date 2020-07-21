---
layout: post
categories: AlgoUlt.
tag: [] 

---



# Fenwick Tree

![image-20200715173319551](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggrsh3fq61j31920lm47i.jpg)

![image-20200715174108116](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggrsp6fuk6j31960mgqeg.jpg)

![image-20200715174924357](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggrsxs6yawj30y60ge7cg.jpg)



```python
class FenwickTree(object):
    def __init__(self, n):
        self.sums_ = [0] * (n+1)
        self.n = n
        
    def update(self, i, delta):
        while i < len(self.sums_):
            self.sums_[i] += delta
            i += self._lowbit(i)
    
    def query(self, i):
        sum_ = 0
        while i > 0:
            sum_ += self.sums_[i]
            i -= self._lowbit(i)
        return sum_
    
    def _lowbit(self, x):
        return x & -x
    

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = FenwickTree(len(nums))
        for i in range(len(nums)):
            self.tree.update(i+1, nums[i])

    def update(self, i: int, val: int) -> None:
        self.tree.update(i+1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.query(j + 1) - self.tree.query(i)
```



## 315.Count of Smaller Numbers After Self

![image-20200718023519761](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggujdp1o3cj319y0n2k4o.jpg)



![image-20200718023609770](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggujeh5tfej31ae0ms12c.jpg)

![image-20200718023824394](/Users/joe/Library/Application Support/typora-user-images/image-20200718023824394.png)

![image-20200718023848244](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggujh9hnupj30xy0kygz9.jpg)



# Segment Tree

- 更直觀且容易理解，但就是代碼長
- binary tree, balanced, so O(logN); not necessary perfect

![image-20200717004335838](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggtajfaf6jj315q0k2ajx.jpg)



![image-20200717004840098](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggtaogby29j31760l4al7.jpg)



![image-20200717005918569](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggtazhqyolj31380i210v.jpg)

![image-20200717010205089](/Users/joe/Library/Application Support/typora-user-images/image-20200717010205089.png)





![image-20200717011114867](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggtbc3bhtbj31720ke13z.jpg)

![image-20200717011201336](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggtbcsjngrj31840mgwq4.jpg)



![image-20200717011546317](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggtbh09kqsj317s0mu7gt.jpg)







# MST

Usually, turn edge list into adj. list

- adj matrix: |V| x |V|
- adj list: |V| + |E|
- edge list: |E|

## Prim

![image-20200715184644350](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggrulfnwylj30gk05ujt1.jpg)



![image-20200715184636907](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggrulc6ffvj30im0b00w3.jpg)



Greedy!



![image-20200715185254214](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggrus16rd6j31dk0ognax.jpg)



![image-20200715185312545](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggrusiuvkpj31iu0q41gm.jpg)



## Kruskal

![image-20200715230409210](/Users/joe/Library/Application Support/typora-user-images/image-20200715230409210.png)

![image-20200715230645534](/Users/joe/Library/Application Support/typora-user-images/image-20200715230645534.png)

