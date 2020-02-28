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

