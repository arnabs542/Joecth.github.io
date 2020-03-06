---
layout: post
categories: Python
tag: []
date: 2020-01-15
---



## Read input from STDIN. Print output to STDOUT*

**Sample Input**

```
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
```

**Sample Output**

```
sam=99912222
Not found
harry=12299933
```

```python
n = int(input())

book = [input().split() for _ in range(n)]  # [[name1, phone1], [name2, phone2]...]
# print(book)
d = {k:v for k, v in book}

while True:
    try:
        name = input()
        # if not name: break
        if name in d:
            print('{}={}'.format(name, d[name]))
        else:
            print('Not found')
    except Exception as e:
        break
```



```python
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # print(apples ,oranges)
    
    aa = map(lambda a, x: a+x, [a]*len(apples), apples)
    oo = map(lambda b, x: b+x, [b]*len(oranges), oranges)

    count_a = 0
    for a in aa:
        if s <= a <= t:
            count_a += 1
    print(count_a)
    count_o = 0
    for o in oo:
        if s <= o <= t:
            count_o += 1
    print(count_o)
```



### GCD  x LCM

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def getTotalX(a, b):
    # Write your code here
    if not a or not b:
        return 0
    def gcd(A):
        '''
        12 16 18 40
        0   4  6  ４
        0.  0. 2  ０
        '''
        # arr = sorted(A, key=lambda x: x)
        # p = arr[0]
        # while p:
        #     prev_p = p
        #     for j in range(len(arr)):
        #         arr[j] = arr[j] % p
        #     for k in range(len(arr)):
        #         if arr[j] != 0:
        #             p =  arr[j]
        #         if p != prev_p:
        #             break
        # return prev_p
        pass

    def find_gcd(a, b):
        if a < b:
            a, b = b, a
        while a:
            # print("a:{}, b:{}".format(a, b))
            r = a % b       # 20 16
            if r == 0:      # 4
                break       
            a, b = b, r                         

        return b

    def GCD(arr):
        if len(arr) == 1:
            return arr[0]
        gcd = find_gcd(arr[0], arr[1])
        for i in range(2, len(arr)):
            gcd = find_gcd(gcd, arr[i])
        return gcd

    def LCM(arr):
        if len(arr) == 1:
            return arr[0]
        def find_lcm(a, b):
            gcd = find_gcd(a, b)
            return a*b/gcd
        lcm = find_lcm(arr[0], arr[1])
        for j in range(2, len(arr)):
            lcm = find_lcm(lcm, arr[j])
        return lcm

    gcd = GCD(b)
    # print('GCD: {}'.format(gcd))
    lcm = LCM(a)
    # print('LCM: {}'.format(lcm))
    n = int(gcd/lcm)
    res = 0
    for k in range(1, n+1):
        if gcd % (k*lcm) == 0:
            res += 1
    return res

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

```



### ~~Exceptions - String to Integer~~

```python
import sys


S = input().strip()

try:
    print(int(S))
except:
    print('Bad String')
```

