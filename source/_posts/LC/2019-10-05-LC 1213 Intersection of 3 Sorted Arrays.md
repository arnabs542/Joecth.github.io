---
layout: post
categories: LC
date: 2019-10-05
tag: [Contest] 



---



```python
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = list(set(arr1) & set(arr2) & set(arr3))
        res.sort()
        return res
```

![image-20191006001702675](https://tva1.sinaimg.cn/large/006y8mN6ly1g7ns65cka1j30ki0dqmyy.jpg)