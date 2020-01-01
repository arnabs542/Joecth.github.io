---
layout: post
categories: Python
date: 2018-10-21
tag: [] 



---

### Closure & Non-local vs Global

```python
方法一：创建生成器            

def creatCounter( ):
    def f( ):
        x = 0
        while True:
              x = x +1
              yield x
    
    sum = f( ) 
      
    def  counter( ):
         return next( sum )
 
    return counter


```



这里没有直接调用f( )，即next( f( ) )，而是用定义sum = f( )，即next( sum )，

因为creatCounter( )返回的是counter这个函数，而此时f( )并没有执行并返回一个生成器对象，而执行next（sum）则会执行f( )生成一个新的生成器对象，变向的理解，s1 = f( )，s2 = f( )，但s1 == s2是false（这个变向理解感觉有点牵强）

方法二：创建列表

```python

def creatCounter():
    s = [0]
    def counter():
        s[0] = s[0] + 1
```



```python
def creat_counter():
    i=0
    def counter():
        nonlocal i
        i=i+1
        return i
    return counter
```



![image-20191023164204053](https://tva1.sinaimg.cn/large/006y8mN6gy1g8885skue5j30v30u042e.jpg)



![image-20191023165343479](https://tva1.sinaimg.cn/large/006y8mN6gy1g888hveiitj30dd0v4420.jpg)

![image-20191023165358740](https://tva1.sinaimg.cn/large/006y8mN6gy1g888i4jauxj30db0saq6i.jpg)

Ref:

https://www.jianshu.com/p/703ad1289a00
