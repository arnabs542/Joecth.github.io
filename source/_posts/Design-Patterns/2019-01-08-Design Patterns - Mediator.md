---
layout: post
categories: DesignPattern
ag: []
date: 2020-01-08
---



### Mediator Pattern

The mediator allows implitcit interaction btw objects, and therefore decoupling between them, making them independent to each other.

Example: houselord (landlord) vs tenant　，Other example like chatroom

```python
# landlord INTERFACE
class HouseOwner:
  def action(self):
    pass

# tenant IMPL
class HouseRent(HouseOwner):
  def action(self):
    print("Customer here to rent house")
    
# renting/sell IMPL
class HouseSale(HouseOwner):
  def action(self):
    print("To sell/rent house")

# MEDIATOR
class Mediator:
  def handle(self, content):
    pass

# MEDIATOR IMPL
class MediatorImpl(Mediator):
  def __init__(self):
    self.owner1 = HouseRent()
    self.owner2 = HouseSale()
    
  def handle(self, content):
    if "rent" == content:
      self.owner1.action()
    if "sale" == content:
      self.owner2.action()
      
"""
TESTING
"""
mediator = MediatorImpl()

# The mediator helps coordiante btw landlord & tenant
mediator.handle("rent")
mediator.handle("sale")

-----------------------------
Customer here to rent house
To Sell/rent house

```

![image-20200108153907776](https://tva1.sinaimg.cn/large/006tNbRwly1gap722mnbgj30mn06kq3w.jpg)

