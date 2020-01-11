---
layout: post
categories: DesignPattern
ag: []
date: 2019-10-10
---

### Decoration Pattern

Dynamically add additional duty/functions with it's light-weight characteristic.

```python
# Abstract
class Person:
  def show(self):
    pass

# Implementation
class Man(Person):
  def show(self):
    print("I'm a man")
    
class Decorator(Stage):
  p = None
  def __init__(self, p):
    self.p = p

# Decorating as Actor
class ActorDecorator(Decorator):
  def __init__(self, p):
    self.p = p
    
  def show(self):
    self.p.show()
    print("Besides, I'm a actor!")
    
# Decorating as manager
class ManagerDecorator(Decorator):
  def __init__(self, p):
    self.p = p
    
  def show(self):
    self.p.show()
    print("Besides, I'm a manaer!")

p = Man()
p.show()
p = ActorDecorator(p)
p.show()
```

#### Decorator in Python

```python
def deco_w_template(func):
  def wrapper(self):
    '''
    Wearing template for a specific stage
    '''

    func(self)
@deco_w_template
def stack_imgs_w_template(self):
  self.stack_imag_input()
```



### -------------------------

### Bridge Pattern

![img](https://wenku.baidu.com/content/bdfbea1532687e21af45b307e87101f69f31fb57?m=733a52e18c55a2da23ca8d2474c6063b&type=pic&src=9d099aa89ac3df4848d1bb0577d84a2b.png&token=6f2c8b37d54ffc89fefa2592228ab461)

```python 
# cloth
class Clothing:
  name = ""
  person = None
  
  def __init__(self, name):
    self.name = name
  
  def getName(self):
    return self.name
 
	def setName(self, name):
    self.name = name
    
  def getPerson(self):
    return self.person
	
  def setPerson(self, person):
    self.person = person
    
# Jacket class
class Jacket(Clothing):
  def __init__(self, name):
    self.name = name

# Denim
class Trousser(Clothing):
  def __init__(self, name):
    self.name = name

###############################################
# Person
class Person:
  name = ""
  cloth = None
  
  def __init__(self, name):
    self.name = name
  
  def getName(self):
    return self.name
 
	def setName(self, name):
    self.name = name
    
  def getCloth(self):
    return self.cloth
	
  def setCloth(self, cloth):
    self.cloth = cloth
    
  def dress(self):
    pass
  
# Man
class Man(Person):
  def __init__(self, name):
    self.name = name
	
  def dress(self):
    print(self.name, " Wears ", 
         self.cloth.getName())
    
# Woman
class Woman(Person):
  def __init__(self, name):
    self.name = name
	
  def dressß(self):
    print(self.name, " Wears ", 
         self.cloth.getName())
    
# Testing
lady = Woman('Amy')
lady.setCloth(Jacket('Jacket'))
lady.dress()
lady.setCloth(Trouser('Skirt'))
lady.dress()
```

