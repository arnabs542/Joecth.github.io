---
layout: post
categories: Python
tag: []
date: 2019-02-28

---



```python
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super(MyBook, self).__init__(title, author)
        self.price = price
    def display(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price))
```



BTW, 如果真的想要模擬Java中interface，可定義一個抽象類別，完全沒有實作的方法即可。例如：

```python
import random
from abc import ABCMeta, abstractmethod

class Flyer(metaclass=ABCMeta): # 就像是Java中的interface
    @abstractmethod
    def fly(self):
        pass

class Bird:
    pass
    
class Sparrow(Bird, Flyer):  # 就像Java中繼承Bird類別並實作Flyer介面
    def fly(self):
        print('麻雀飛')

s = Sparrow()
s.fly()
```