---
layout: post
categories: M
tag: []
date: 2020-02-28

---



## 時間數據的特徵工程

可展開成年、月、日、星期幾、週末、月的哪部分，一年當中第幾天、第幾個月、月初還是月末、節日

上中下旬用數字不OK, 所以可用one-hot encoding，用很多個bool表示其中那個用1, 2, 3表示的上中下旬。

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd8c7zt08dj30w20bg75q.jpg" alt="image-20200327114411681" style="zoom:67%;" />



pd.get_dummies 做 one-hot- encoding

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd8cgz308wj314g0iq411.jpg" alt="image-20200327115247759" style="zoom:80%;" />

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd8ccnwq2gj310409k757.jpg" alt="image-20200327114837591" style="zoom:67%;" />

用10個維度表示其中的10年

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd8cbtiq38j310o096aam.jpg" alt="image-20200327114753055" style="zoom:67%;" />





然後整理數據集

Linear regression, 多項式迴歸、嶺迴歸、Lasso regression 需要　X_dummy , with one-hot-encoding, 成72維度

DT、RF不需要 one-hot-encoding，用 X_before_dummy





## 模型

MSE, RMSE, MAbsoluteE, R Square

#### 線性迴歸

![image-20200327120233707](https://tva1.sinaimg.cn/large/00831rSTgy1gd8cqzb6j7j312u0huh1c.jpg)

我們看到的是72維在2D平面的投影

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd8ct2bdltj313m02mdgg.jpg" alt="image-20200327120425110" style="zoom:80%;" />



#### 多項式迴歸

二次、三次

#### 嶺迴歸

- 線性加了L1正則

#### Lasso迴歸

- 線性加了L2正則



#### RF

- bagging 子集建各樹、考慮最大的特徵數，作Cross Validation



## 模型比較

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd8df910hwj31eu0m8n1b.jpg" alt="image-20200327122545346" style="zoom:67%;" />

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd8dfjtqpej315o0gk4cq.jpg" alt="image-20200327122605413" style="zoom:67%;" />