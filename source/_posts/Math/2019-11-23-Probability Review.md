---
layout: post
categories: Probability
date: 2019-11-23
tag: [] 


---





### Calc

假设每个靶中率都是相同的，一个人每个都去射，发现连续射 30 个能中的probability是 93.6%， 那么请问连续射 10次能中的概率是多少？

Ans: 
$$
(p^{30})^{1/3} = (6.4％)^{1/3}
$$



### 中央極限定理

![image-20191208222151340](https://tva1.sinaimg.cn/large/006tNbRwly1g9pohhkh7lj318s0owaql.jpg)

![image-20191208235851948](https://tva1.sinaimg.cn/large/006tNbRwly1g9prafd63wj310i0hannw.jpg)

<img src="https://tva1.sinaimg.cn/large/006tNbRwly1g9prfrtf57j30we0actm4.jpg" alt="image-20191209000154339" style="zoom:50%;" />

![image-20191209001233563](https://tva1.sinaimg.cn/large/006tNbRwly1g9pronm5amj30t20ly4jg.jpg)

http://onlinestatbook.com/stat_sim/sampling_dist/index.html

[https://www.zhihu.com/question/22913867](https://www.zhihu.com/question/22913867)

![image-20191209001955240](https://tva1.sinaimg.cn/large/006tNbRwly1g9prwbrwlij318p0u010k.jpg)

![image-20191209002030933](https://tva1.sinaimg.cn/large/006tNbRwly1g9prwxvy3oj31840u0qal.jpg)

我们让中心极限定理发挥作用。现在我们抽取1000组，每组**50**个。
我们把每组的平均值都算出来。

```text
samples = []
samples_mean = []
samples_std = []

for i in range(0, 1000):
    sample = []
    for j in range(0, 50):
        sample.append(random_data[int(np.random.random() * len(random_data))])
    sample_np = np.array(sample)
    samples_mean.append(sample_np.mean())
    samples_std.append(sample_np.std())
    samples.append(sample_np)

samples_mean_np = np.array(samples_mean)
samples_std_np = np.array(samples_std)

print samples_mean_np
```

这一共1000个平均值大概是这样的：**[3.44, 3.42, 3.22, 3.2, 2.94 … 4.08, 3.74]** （我肯定不会把1000个数字都写完，又没有稿费可以骗）

然后，我们把这1000个数字用直方图画出来：

![img](https://pic3.zhimg.com/80/v2-3d1871cc5a1bbfdd5610b0c070d0a032_hd.png)

TADA! 完美地形成了正态分布。

结果打印如下：

平均值：**3.48494**
标准差：**0.23506.  (1.7079/sqrt(50))**

#### 实际应用

在实际生活当中，我们不能知道我们想要研究的对象的平均值，标准差之类的统计参数。中心极限定理在理论上保证了我们可以用只抽样一部分的方法，达到推测研究对象统计参数的目的。
在上文的例子中，掷骰子这一行为的理论平均值3.5是我们通过数学定理计算出来的。而我们在实际模拟中，计算出来的样本平均值的平均值（3.48494）确实已经和理论值非常接近了。

```text
import numpy as np 
random_data = np.random.randint(1, 7, 10000)
print random_data.mean() # 打印平均值
print random_data.std()  # 打印标准差
```

生成出来的平均值：**3.4927***（每次重新生成都会略有不同）*
生成出来的标准差：**1.7079**

平均值接近3.5很好理解。 因为每次

### 大數定理

Connect **Expectation of Probabilty** to **Mean in Statistics**.

![v2-670e93df4d2c25f52dc407073e017d03_hd](https://tva1.sinaimg.cn/large/006tNbRwly1g9psliag72j30f00pu3zv.jpg)

[https://www.zhihu.com/question/19911209/answer/245487255](https://www.zhihu.com/question/19911209/answer/245487255)

**切比雪夫大数定律**   
在用标准差估计精度的时候用到，类似6sigma那个规律。   
 由切比雪夫不等式P{|X-EX|<ε}>=1-DX/ε^2    
可以导出区间(x± k σ)下的概率. K=2时. x± 2σ. 75%；K=3，89%；K=4，94%    
切比雪夫大数定律是切比雪夫不等式的推论。   

**伯努利大数定律**   
证明了在多次相同的条件的重复试验中，频率有越接近一稳定值的趋势。   

也告诉了我们当实验次数很大时，可以用事件发生的频率来代替事件的概率。   

**辛钦大数定律**    
需要独立同分布的条件。 切比雪夫大数定律只需相互独立分布。   
　   
**中心极限定理**   
说明的是在一定条件下，大量独立随机变量的平均数是以正态分布为极限的。   
 而大数定律只是揭示了大量随机变量的平均结果，但没有涉及到随机变量的分布的问题。    

**列维-林德伯格定理**   
是中心极限定理的一种，就是独立同分布的中心极限定理   
其他中心极限定理还有一个特例棣莫夫-拉普拉斯定理   

**棣莫弗—拉普拉斯定理**   
证明的是二项分布的极限分布是正态分布，也告诉了我们实际问题时可以用大样本近似处理。



### 貝氏

### Pearson’s correlation coefficient

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdamsiqi39j307a03a3yi.jpg" alt="img" style="zoom:50%;" />

correlation coefficient(*ρ*，有的時候會用*r*來表示)會落在-1到1之間: -1≤*ρ*≤1，*μx*和*μy* 分別代表變數*x*和*y*的平均數。

看公式會很沒有感覺，對於懂得人會覺得簡單，對於不懂的人會覺得是天書。

為什麼這樣設計會稱為相關係數勒，其實相關係數公式等於:

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdamss07xmj30dp064dgk.jpg" alt="img" style="zoom:50%;" />

### selection bias

只聽信某人的話或是相信綴學就是像Steve Jobbs, Bill Gate 那樣

**Selection bias** is the **bias** introduced by the **selection** of individuals, groups or data for analysis in such a way that proper randomization is not achieved, thereby ensuring that the sample obtained is not representative of the population intended to be analyzed. It is sometimes referred to as the **selection** effect.



### example of a dataset with a non -Gaussian distribtion?

Here are sample time series for two measured variables: one is Gaussian-distributed (top), and the other is not (bottom).

![img](https://tva1.sinaimg.cn/large/00831rSTgy1gdanj3szc4j30gq07yq3z.jpg)

On the right, I tallied the measurements in a histogram. This can help us check if a variable is Gaussian or not.

Non-Gaussian distributed time series data arise when the mean or noise statistics vary with time.

If the mean varies with time, the variable could be non-stationary / time-varying (its trend changes with time), auto- or cross-correlated (it changes depending on its previous value or the values of other variables), or its value is computed from the values of other Gaussian variables but in a nonlinear way.

I hope this helps.



