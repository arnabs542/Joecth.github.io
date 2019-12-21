---


date: 2019-10-03
layout: post
categories: LC
tag: [Michelle, TODO] 


---

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res, i, j, s = [], len(a)-1, len(b)-1, 0
        while i >=0 or j >= 0 or s:
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1
            res.append(str(s % 2))
            s /= 2
        res_str = ''.join(res[::-1])
        return res_str
```

```python
def addBinary(self, a, b):
    res, carry = '', 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        curval = ) + (j >= 0 and b[j] == '1')
        carry, rem = divmod(curval + carry, 2)
        res = `rem` + res
        i -= 1
        j -= 1
    return res
```

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, carry, val = '', 0, 0
        
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i< len(b):
                val += int(b[-(i+1)])
            carry, val = val//2, val%2
            result += str(val)
        if carry:
            result += str(1)
        return result[::-1]
            
```

![image-20191003140722662](https://tva1.sinaimg.cn/large/006y8mN6ly1g7kzb2nyk1j30pg0dwjti.jpg)