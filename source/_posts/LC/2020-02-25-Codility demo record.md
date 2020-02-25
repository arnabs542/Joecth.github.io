---
layout: post
categories: LC
tag: []
date: 2020-02-25
Author: Joe Huang

---





```python
'''
Counter  X
if not ass: return 
if arr[-1] < 1:
    return 1
    
if diff > 1:
    return arr[perv] + 1
    
if i end loops :
    return arr[-1] + 1   or
    return arr[prev] + 1
    
sort
    -2 -1 0 1 2 3 4     5
                      prev    i
                 diff > 1!  
                bk
'''
def solution(A):
    # write your code in Python 3.6
    # pass
    if not A:
        return 1
    if len(A) == 1:
        return 1 if A[0] <= 0 else A[0]+1
        
    arr = sorted(A, key=lambda x: x)
    
    if arr[-1] <= 0:
        return 1
    
    prev = 0
    for i in range(1, len(arr)):    # at least 2 elems here
        if arr[i] <= 0:
            continue
        diff = arr[i] - arr[prev]
        if diff > 1:
            return arr[prev] + 1
        prev = i
    return arr[prev] + 1
```

