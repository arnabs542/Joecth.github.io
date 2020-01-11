---
layout: post
categories: DesignPattern
ag: []
date: 2019-10-10
---

### Strategy Pattern

Algorithms Encapisulation for mutual exchange.
For Algorithms Scalibility.

```python
# Abstract
class Strategy:
  def foo(self):
    pass
  
# Implementation
class StrategyImplA(Strategy):
  def foo(self):
    print("Strategy Imp A")
    
class StrategyImplB(Strategy):
  def foo(self):
    print("Strategy Imp B")    

class StrategyImplC(Strategy):
  def foo(self):
    print("Strategy Imp C")

# Stategy Env Encapsulation
class Context:
  def __init__(self, strategy):
    self.strategy = strategy
  
  def do(self):
    self.strategy.foo()
    
# Testing
Context(StrategyImplB()).do()
```



### Factory Pattern 

### (w/o encapsulation, -- Simple Factory Method)

Decoupling instance initialization & usage steps.
Child determines concrete the concrete implementation class.

```python
# Product
class Product:
  def getName(self):
    pass

# Product A
class ProductA(Product):
  def getName(self):
    return "product A"

# Product B
class ProductA(Product):
  def getName(self):
    return "product B"

# Factory to create product
class Factory:
  @staticmethod
  def yield_product(productType):
    if productType == 0:
      p = ProductA()
    elif productType == 1:
      p = ProductB()
    return p

# Testing 
p = Factory.create(0)

```

