---
layout: post
categories: Python
tag: []
date: 2019-01-15
---



ref: [https://medium.com/bryanyang0528/python-setter-%E5%92%8C-getter-6c08a9d37d46](https://medium.com/bryanyang0528/python-setter-和-getter-6c08a9d37d46)

简言之：

obj.attribute_1 可以拿到 物件的 attribute；但也易被改掉。
為了不讓使用者輕易能改掉 attribute, 所以以下滑線開頭的私有屬性，但這樣就無法無法被obj直接使用，得透過oop的set&get方法。
為了讓它可以用一樣的語法被拿出使用，所以用 `property`，將method變成屬性在作使用；同時，為了讓它可以用一樣的語法被設值，所以用`setter`，將關鍵字加在要變成屬性化的method上面，然後在method裡面去改私有屬性。