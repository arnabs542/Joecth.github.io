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



### ~~Birthday Chocolate~~

**Sample Input 0**

```
5
1 2 1 3 2
3 2
```

**Sample Output 0**

```
2
```

```python
def birthday(s, d, m):
    if not s or not d or not m:
        return 0
    j = 0
    res = 0
    for i in range(m-1, len(s)):        # use m-1 instead of m to solve m==1 case, where the loop isn't gonna entered
        if sum(s[j:i+1]) == d:
            res += 1
        j += 1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
```



### ~~DivisorSum~~

```python
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        res = 0
        for j in range(1, n+1):
            if n % j == 0:
                res += j

        return res
```



### ~~DivisibleSumPair~~

```python
def divisibleSumPairs(n, k, ar):
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                res += 1
    # print(res)
    return res
```



### ~~Count B-Sort Swapping~~



### Generics

```java
import java.util.*;

class Printer <T> {

    /**
    *    Method Name: printArray
    *    Print each element of the generic array on a new line. Do not return anything.
    *    @param A generic array
    **/
    
    // Write your code here
    public static <E> void printArray(E[] generic){
        for(E element : generic) {
            System.out.println(element); 
        }
    }
}
```



#### ~~BST Height according to Edges~~

```python
    def getHeight(self,root):
        #Write your code here
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
        L = self.getHeight(root.left)
        R = self.getHeight(root.right)

        return max(L, R) + 1
```



### RM Duplicated from Sorted Linked List

```python
    def removeDuplicates(self,head):
        #Write your code here
        dummy = Node("INIT")
        dummy.next = head
        self.helper(head, dummy)
        return dummy.next

    def helper(self, root, prev):
        if not root:
            return
        if prev.data == root.data:
            prev.next = root.next
            self.helper(root.next, prev)
        else:
            self.helper(root.next, root)
```



### IsPrime w/ Input() Parsing

```python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
num = int(input().strip())

arr = []
for i in range(num):
    arr.append(int(input().strip()))
# print('arr: {}'.format(arr))

class Solution:
    def foo(self, arr):
        for i in range(len(arr)):
            if self.isPrime(arr[i]):
                print('Prime')
            else:
                print('Not prime')

    def isPrime(self, n):
        if n <= 1:
            return False
        end = int(math.sqrt(n)) + 1
        for j in range(2, end):
            if  n % j == 0:
                return False
        return True
```



### Day 26 - Nested Logic

```python

actual = list(map(int, input().strip().split()))
expect = list(map(int, input().strip().split()))


class Solution:
    def foo(self, actual, expect):
        da, ma, ya = actual
        de, me, ye = expect
        if ya < ye or da <= de and ma <= me and ya <= ye:
            return 0
        elif ya > ye:
            return 10000
        elif ma > me:
            return 500 * (ma - me) 
        elif da > de:
            return 15 * (da - de)
        else:
            return -1
if __name__ == "__main__":
    sol = Solution()
    print(sol.foo(actual, expect))
```



### Day 27 - Test

```python
def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):
    arr = [5,4,3,2,1]
    @staticmethod
    def get_array():
        # complete this function
        return TestDataUniqueValues.arr

    @staticmethod
    def get_expected_result():
        # complete this function
        return minimum_index(TestDataUniqueValues.arr)

class TestDataExactlyTwoDifferentMinimums(object):
    arr = [5, 4, 3, 2, 2]
    @staticmethod
    def get_array():
        # complete this function
        return TestDataExactlyTwoDifferentMinimums.arr

    @staticmethod
    def get_expected_result():
        # complete this function
        return minimum_index(TestDataExactlyTwoDifferentMinimums.arr)


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
```



### Draw Book

![image-20200317163814705](https://tva1.sinaimg.cn/large/00831rSTgy1gcx0ix4kyej31in0u0djo.jpg)

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gcx0kem3spj313w0880tq.jpg" alt="image-20200317163936950" style="zoom:67%;" />



### Day 28 RegEX, Pattern 

```python
import math
import os
import random
import re
import sys
import heapq

import re
if __name__ == '__main__':
    pattern = re.compile('@gmail.com$')

    N = int(input())
    res = []
    # heapq.heapify(res)

    for N_itr in range(N):
        firstNameEmailID = input().strip().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        # if emailID.split('@')[1].split('.')[0] != 'gmail':
        #     continue
        if not pattern.search(emailID):
            continue
        # heapq.heappush(res, firstName)
        res.append(firstName)
    
    res.sort()
    for j in range(len(res)):
        # print(heapq.heappop(res))
        print(res[j])

```



### Level Order BFS~~