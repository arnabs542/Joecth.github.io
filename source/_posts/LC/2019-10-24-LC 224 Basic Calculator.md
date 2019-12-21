---
categories: LC
tag: [F, TODO, ComeO] 
date: 2019-10-24




---

```python

class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res = res + sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res = res + sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res = res + sign * num
        return res
```





![image-20191026205957710](https://tva1.sinaimg.cn/large/006y8mN6ly1g8bwh653lkj30ui0o213v.jpg)

![image-20191026211832001](https://tva1.sinaimg.cn/large/006y8mN6ly1g8bx0dz21fj30vy0f2n35.jpg)

![image-20191026211814852](https://tva1.sinaimg.cn/large/006y8mN6ly1g8bx03clc4j30x007wjwk.jpg)