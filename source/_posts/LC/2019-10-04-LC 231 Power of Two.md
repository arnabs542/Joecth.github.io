---
layout: post
categories: LC
date: 2019-10-04
tag: [] 

---

```python
def isPowerOfTwo(self, n: int) -> bool:
    tmp = n
date: 2019-10-04
    while tmp:
        if tmp == 1:
            return True
        tmp = tmp / 2
        if tmp < 1 :
            break
    return False
```


```python
def f(self, n):
	return n > 0 and (n & (n-1)) == 0
```

