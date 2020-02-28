---
layout: post
categories: Python
tag: []
date: 2020-01-15
---



### Finding Pos

```python
import bisect
 
a = [1,4,6,8,12,15,20]
position = bisect.bisect(a,13)
print(position)
 
# 用可变序列内置的insert方法插入
a.insert(position,13)
print(a)

```

输出：

5
[1, 4, 6, 8, 12, 13, 15, 20]



---



### Insert 

```python
import bisect
 
a = [1,4,6,8,12,15,20]
bisect.insort(a,13)
print(a)
```

