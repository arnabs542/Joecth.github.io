---
layout: post
categories: [Deep-Learning, AI]
date: 2018-07-15
---
### More Edge Detection

![image-20190930131327684](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hgvsxddgj30oc13o1kx.jpg)

### FC![image-20190930131559243](/Users/joe/Library/Application Support/typora-user-images/image-20190930131559243.png)

### ResNet

![image-20190930132251760](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hh5larukj31540u0u0x.jpg)

![image-20190930132333911](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hh6b4jv8j30u00znnpd.jpg)

### 1X1

![image-20190930132631493](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hh9e9z08j30vm0sukhp.jpg)

![image-20190930132651113](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hh9q42hqj31320ps1kx.jpg)

![image-20190930132738243](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hhajkqtsj30u00wl7wh.jpg)

### Inception

![image-20190930133434192](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hhhrhpwsj30u00vohdt.jpg)

![image-20190930133601668](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hhja5itdj30wi0u01kx.jpg)

“事 实 上 ， 如 果 你 读 过 论 文 的 原 文 ， 你 就 会 发 现 ， 这 里 其 实 还 有 一 些 分 支 ， 我 现 在 把 它 们 加 上 去 。 所 以 这 些 分 支 有 什  么 用 呢 ？ 在 网 络 的 最 后 几 层 ， 通 常 称 为 金 连 接 层 ， 在 它 之 后 是 一 个 s 。 ftmax 层 （ 编 号 1 ） 来 做 出 预 测 ， 这 些 分 支  （ 编 号 2 ） 所 做 的 就 是 通 过 隐 藏 层 （ 编 号 引 来 做 出 预 氵 则 ， 所 以 这 其 实 是 一 个 s 。 ftmax 输 出 （ 编 号 2 ） ， 这 （ 编 号  1 ） 也 是 。 是 另 一 条 分 支 （ 编 号 4 ） ， 它 也 包 含 了 一 个 隐 藏 层 ， 通 过 一 些 全 连 接 层 ， 然 后 有 一 个 so 代 max 来 预  测 ， 输 出 结 果 的 标 签 。  你 应 该 把 它 看 做 Incepti 。 n 网 络 的 一 个 细 节 ， 它 确 保 了 即 便 是 隐 藏 单 元 和 中 间 层 （ 编 号 5 ） 也 参 与 了 特 征 计 算 ， 它  们 也 能 预 测 图 片 的 分 类 。 它 在 Inception 网 络 中 ， 起 到 一 种 调 整 的 效 果 ， 并 且 能 防 止 网 络 发 生 过 拟 合 。  ”




### 迁移学习

在“搭建机器学习项目”课程中，[迁移学习](http://kyonhuang.top/Andrew-Ng-Deep-Learning-notes/#/Structuring_Machine_Learning_Projects/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%EF%BC%88ML%EF%BC%89%E7%AD%96%E7%95%A5%EF%BC%882%EF%BC%89?id=%e8%bf%81%e7%a7%bb%e5%ad%a6%e4%b9%a0)已经被提到过。计算机视觉是一个经常用到迁移学习的领域。在搭建计算机视觉的应用时，相比于从头训练权重，下载别人已经训练好的网络结构的权重，用其做**预训练**，然后转换到自己感兴趣的任务上，有助于加速开发。

对于已训练好的卷积神经网络，可以将所有层都看作是**冻结的**，只需要训练与你的 Softmax 层有关的参数即可。大多数深度学习框架都允许用户指定是否训练特定层的权重。

而冻结的层由于不需要改变和训练，可以看作一个固定函数。可以将这个固定函数存入硬盘，以便后续使用，而不必每次再使用训练集进行训练了。

上述的做法适用于你只有一个较小的数据集。如果你有一个更大的数据集，应该冻结更少的层，然后训练后面的层。越多的数据意味着冻结越少的层，训练更多的层。如果有一个极大的数据集，你可以将开源的网络和它的权重整个当作初始化（代替随机初始化），然后训练整个网络。

### 数据扩增

计算机视觉领域的应用都需要大量的数据。当数据不够时，**数据扩增（Data Augmentation）**就有帮助。常用的数据扩增包括镜像翻转、随机裁剪、色彩转换。

其中，色彩转换是对图片的 RGB 通道数值进行随意增加或者减少，改变图片色调。另外，**PCA 颜色增强**指更有针对性地对图片的 RGB 通道进行主成分分析（Principles Components Analysis，PCA），对主要的通道颜色进行增加或减少，可以采用高斯扰动做法来增加有效的样本数量。具体的 PCA 颜色增强做法可以查阅 AlexNet 的相关论文或者开源代码。

在构建大型神经网络的时候，数据扩增和模型训练可以由两个或多个不同的线程并行来实现。

### 计算机视觉现状

通常，学习算法有两种知识来源：

* 被标记的数据
* 手工工程

**手工工程（Hand-engineering，又称 hacks）**指精心设计的特性、网络体系结构或是系统的其他组件。手工工程是一项非常重要也比较困难的工作。在数据量不多的情况下，手工工程是获得良好表现的最佳方式。正因为数据量不能满足需要，历史上计算机视觉领域更多地依赖于手工工程。近几年数据量急剧增加，因此手工工程量大幅减少。

另外，在模型研究或者竞赛方面，有一些方法能够有助于提升神经网络模型的性能：

* 集成（Ensembling）：独立地训练几个神经网络，并平均输出它们的输出
* Multi-crop at test time：将数据扩增应用到测试集，对结果进行平均

但是由于这些方法计算和内存成本较大，一般不适用于构建实际的生产项目。

