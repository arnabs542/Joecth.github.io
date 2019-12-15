---
layout: post
categories: [Deep-Learning, AI]
---
Deeplearning.ai_Course4.md

<h1 align="center">目标检测</h1>
目标检测是计算机视觉领域中一个新兴的应用方向，其任务是对输入图像进行分类的同时，检测图像中是否包含某些目标，并对他们准确定位并标识。

## 目标定位

定位分类问题不仅要求判断出图片中物体的种类，还要在图片中标记出它的具体位置，用**边框（Bounding Box，或者称包围盒）**把物体圈起来。一般来说，定位分类问题通常只有一个较大的对象位于图片中间位置；而在目标检测问题中，图片可以含有多个对象，甚至单张图片中会有多个不同分类的对象。

为了定位图片中汽车的位置，可以让神经网络多输出 4 个数字，标记为 $b\_x$、$b\_y$、$b\_h$、$b\_w$。将图片左上角标记为 (0, 0)，右下角标记为 (1, 1)，则有：

* 红色方框的中心点：($b\_x$，$b\_y$)
* 边界框的高度：$b\_h$
* 边界框的宽度：$b\_w$

因此，训练集不仅包含对象分类标签，还包含表示边界框的四个数字。定义目标标签 Y 如下：

$$\left[\begin{matrix}P\_c\\\ b\_x\\\ b\_y\\\ b\_h\\\ b\_w\\\ c\_1\\\ c\_2\\\ c\_3\end{matrix}\right]$$

则有：

$$P\_c=1, Y = \left[\begin{matrix}1\\\ b\_x\\\ b\_y\\\ b\_h\\\ b\_w\\\ c\_1\\\ c\_2\\\ c\_3\end{matrix}\right]
$$

其中，$c\_n$表示存在第 $n$个种类的概率；如果 $P\_c=0$，表示没有检测到目标，则输出标签后面的 7 个参数都是无效的，可以忽略（用 ? 来表示）。

$$P\_c=0, Y = \left[\begin{matrix}0\\\ ?\\\ ?\\\ ?\\\ ?\\\ ?\\\ ?\\\ ?\end{matrix}\right]$$

损失函数可以表示为 $L(\hat y, y)$，如果使用平方误差形式，对于不同的 $P\_c$有不同的损失函数（注意下标 $i$指标签的第 $i$个值）：

1. $P\_c=1$，即$y\_1=1$：

    $L(\hat y,y)=(\hat y\_1-y\_1)^2+(\hat y\_2-y\_2)^2+\cdots+(\hat y\_8-y\_8)^2$

2. $P\_c=0$，即$y\_1=0$：

    $L(\hat y,y)=(\hat y\_1-y\_1)^2$

除了使用平方误差，也可以使用逻辑回归损失函数，类标签 $c\_1,c\_2,c\_3$ 也可以通过 softmax 输出。相比较而言，平方误差已经能够取得比较好的效果。

## 特征点检测

神经网络可以像标识目标的中心点位置那样，通过输出图片上的特征点，来实现对目标特征的识别。在标签中，这些特征点以多个二维坐标的形式表示。

通过检测人脸特征点可以进行情绪分类与判断，或者应用于 AR 领域等等。也可以透过检测姿态特征点来进行人体姿态检测。

## 目标检测

想要实现目标检测，可以采用**基于滑动窗口的目标检测（Sliding Windows Detection）**算法。该算法的步骤如下：

1. 训练集上搜集相应的各种目标图片和非目标图片，样本图片要求尺寸较小，相应目标居于图片中心位置并基本占据整张图片。
2. 使用训练集构建 CNN 模型，使得模型有较高的识别率。
3. 选择大小适宜的窗口与合适的固定步幅，对测试图片进行从左到右、从上倒下的滑动遍历。每个窗口区域使用已经训练好的 CNN 模型进行识别判断。
4. 可以选择更大的窗口，然后重复第三步的操作。

![Sliding-windows-detection](https://tva1.sinaimg.cn/large/006y8mN6ly1g7himisg18j30oy0ahjxj.jpg)

滑动窗口目标检测的**优点**是原理简单，且不需要人为选定目标区域；**缺点**是需要人为直观设定滑动窗口的大小和步幅。滑动窗口过小或过大，步幅过大均会降低目标检测的正确率。另外，每次滑动都要进行一次 CNN 网络计算，如果滑动窗口和步幅较小，计算成本往往很大。

所以，滑动窗口目标检测算法虽然简单，但是性能不佳，效率较低。

## 基于卷积的滑动窗口实现

相比从较大图片多次截取，在卷积层上应用滑动窗口目标检测算法可以提高运行速度。所要做的仅是将全连接层换成卷积层，即使用与上一层尺寸一致的滤波器进行卷积运算。

![Convolution-implementation-of-sliding-windows](https://tva1.sinaimg.cn/large/006y8mN6ly1g7himfw9zbj30pu0dgafa.jpg)

如图，对于 16x16x3 的图片，步长为 2，CNN 网络得到的输出层为 2x2x4。其中，2x2 表示共有 4 个窗口结果。对于更复杂的 28x28x3 的图片，得到的输出层为 8x8x4，共 64 个窗口结果。最大池化层的宽高和步长相等。

运行速度提高的原理：在滑动窗口的过程中，需要重复进行 CNN 正向计算。因此，不需要将输入图片分割成多个子集，分别执行向前传播，而是将它们作为一张图片输入给卷积网络进行一次 CNN 正向计算。这样，公共区域的计算可以共享，以降低运算成本。

相关论文：[Sermanet et al., 2014. OverFeat: Integrated Recognition, Localization and Detection using Convolutional Networks](https://arxiv.org/pdf/1312.6229.pdf)

## 边框预测

在上述算法中，边框的位置可能无法完美覆盖目标，或者大小不合适，或者最准确的边框并非正方形，而是长方形。

**YOLO（You Only Look Once）算法**可以用于得到更精确的边框。YOLO 算法将原始图片划分为 n×n 网格，并将[目标定位](http://kyonhuang.top/Andrew-Ng-Deep-Learning-notes/#/Convolutional_Neural_Networks/%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B?id=%e7%9b%ae%e6%a0%87%e5%ae%9a%e4%bd%8d)一节中提到的图像分类和目标定位算法，逐一应用在每个网格中，每个网格都有标签如：

$$\left[\begin{matrix}P\_c\\\ b\_x\\\ b\_y\\\ b\_h\\\ b\_w\\\ c\_1\\\ c\_2\\\ c\_3\end{matrix}\right]$$

若某个目标的中点落在某个网格，则该网格负责检测该对象。

![Bounding-Box-Predictions](https://tva1.sinaimg.cn/large/006y8mN6ly1g7himdh2caj318n0l4nb2.jpg)

如上面的示例中，如果将输入的图片划分为 3×3 的网格、需要检测的目标有 3 类，则每一网格部分图片的标签会是一个 8 维的列矩阵，最终输出的就是大小为 3×3×8 的结果。要得到这个结果，就要训练一个输入大小为 100×100×3，输出大小为 3×3×8 的 CNN。在实践中，可能使用更为精细的 19×19 网格，则两个目标的中点在同一个网格的概率更小。

YOLO 算法的优点：

1. 和图像分类和目标定位算法类似，显式输出边框坐标和大小，不会受到滑窗分类器的步长大小限制。
2. 仍然只进行一次 CNN 正向计算，效率很高，甚至可以达到实时识别。

如何编码边框 $b\_x$、$b\_y$、$b\_h$、$b\_w$？YOLO 算法设 $b\_x$、$b\_y$、$b\_h$、$b\_w$ 的值是相对于网格长的比例。则 $b\_x$、$b\_y$ 在 0 到 1 之间，而 $b\_h$、$b\_w$ 可以大于 1。当然，也有其他参数化的形式，且效果可能更好。这里只是给出一个通用的表示方法。

相关论文：[Redmon et al., 2015. You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/pdf/1506.02640.pdf)。Ng 认为该论文较难理解。

## 交互比

**交互比（IoU, Intersection Over Union）**函数用于评价对象检测算法，它计算预测边框和实际边框交集（I）与并集（U）之比：

$$IoU = \frac{I}{U}$$

IoU 的值在 0～1 之间，且越接近 1 表示目标的定位越准确。IoU 大于等于 0.5 时，一般可以认为预测边框是正确的，当然也可以更加严格地要求一个更高的阈值。

## 非极大值抑制

YOLO 算法中，可能有很多网格检测到同一目标。**非极大值抑制（Non-max Suppression）**会通过清理检测结果，找到每个目标中点所位于的网格，确保算法对每个目标只检测一次。

进行非极大值抑制的步骤如下：

1. 将包含目标中心坐标的可信度 $P\_c$ 小于阈值（例如 0.6）的网格丢弃；
2. 选取拥有最大 $P\_c$ 的网格；
3. 分别计算该网格和其他所有网格的 IoU，将 IoU 超过预设阈值的网格丢弃；
4. 重复第 2~3 步，直到不存在未处理的网格。

上述步骤适用于单类别目标检测。进行多个类别目标检测时，对于每个类别，应该单独做一次非极大值抑制。

## Anchor Boxes

到目前为止，我们讨论的情况都是一个网格只检测一个对象。如果要将算法运用在多目标检测上，需要用到 Anchor Boxes。一个网格的标签中将包含多个 Anchor Box，相当于存在多个用以标识不同目标的边框。

![Overlapping-objects](https://tva1.sinaimg.cn/large/006y8mN6ly1g7him3m8zxj30p20bqjw9.jpg)

在上图示例中，我们希望同时检测人和汽车。因此，每个网格的的标签中含有两个 Anchor Box。输出的标签结果大小从 3×3×8 变为 3×3×16。若两个 $P\_c$ 都大于预设阈值，则说明检测到了两个目标。

在单目标检测中，图像中的目标被分配给了包含该目标中点的那个网格；引入 Anchor Box 进行多目标检测时，图像中的目标则被分配到了包含该目标中点的那个网格以及具有最高 IoU 值的该网格的 Anchor Box。

Anchor Boxes 也有局限性，对于同一网格有三个及以上目标，或者两个目标的 Anchor Box 高度重合的情况处理不好。

Anchor Box 的形状一般通过人工选取。高级一点的方法是用 k-means 将两类对象形状聚类，选择最具代表性的 Anchor Box。

如果对以上内容不是很理解，在“3.9 YOLO 算法”一节中视频的第 5 分钟，有一个更为直观的示例。

## R-CNN 

前面介绍的滑动窗口目标检测算法对一些明显没有目标的区域也进行了扫描，这降低了算法的运行效率。为了解决这个问题，**R-CNN（Region CNN，带区域的 CNN）**被提出。通过对输入图片运行**图像分割算法**，在不同的色块上找出**候选区域（Region Proposal）**，就只需要在这些区域上运行分类器。

![R-CNN](https://tva1.sinaimg.cn/large/006y8mN6ly1g7him6eqfhj30p607o0zs.jpg)

R-CNN 的缺点是运行速度很慢，所以有一系列后续研究工作改进。例如 Fast R-CNN（与基于卷积的滑动窗口实现相似，但得到候选区域的聚类步骤依然很慢）、Faster R-CNN（使用卷积对图片进行分割）。不过大多数时候还是比 YOLO 算法慢。

相关论文：

* R-CNN：[Girshik et al., 2013. Rich feature hierarchies for accurate object detection and semantic segmentation](https://arxiv.org/pdf/1311.2524.pdf)
* Fast R-CNN：[Girshik, 2015. Fast R-CNN](https://arxiv.org/pdf/1504.08083.pdf)
* Faster R-CNN：[Ren et al., 2016. Faster R-CNN: Towards real-time object detection with region proposal networks](https://arxiv.org/pdf/1506.01497v3.pdf)

## --------------------

<h1 align="center">特殊应用：人脸识别和神经风格转换</h1>
## 人脸识别

**人脸验证（Face Verification）**和**人脸识别（Face Recognition）**的区别：

* 人脸验证：一般指一个一对一问题，只需要验证输入的人脸图像是否与某个已知的身份信息对应；
* 人脸识别：一个更为复杂的一对多问题，需要验证输入的人脸图像是否与多个已知身份信息中的某一个匹配。

一般来说，由于需要匹配的身份信息更多导致错误率增加，人脸识别比人脸验证更难一些。

### One-Shot 学习

人脸识别所面临的一个挑战是要求系统只采集某人的一个面部样本，就能快速准确地识别出这个人，即只用一个训练样本来获得准确的预测结果。这被称为**One-Shot 学习**。

有一种方法是假设数据库中存有 N 个人的身份信息，对于每张输入图像，用 Softmax 输出 N+1 种标签，分别对应每个人以及都不是。然而这种方法的实际效果很差，因为过小的训练集不足以训练出一个稳健的神经网络；并且如果有新的身份信息入库，需要重新训练神经网络，不够灵活。

因此，我们通过学习一个 Similarity 函数来实现 One-Shot 学习过程。Similarity 函数定义了输入的两幅图像的差异度，其公式如下：

$$Similarity  = d(img1, img2)$$

可以设置一个超参数 $τ$ 作为阈值，作为判断两幅图片是否为同一个人的依据。

### Siamese 网络

实现 Similarity 函数的一种方式是使用**Siamese 网络**，它是一种对两个不同输入运行相同的卷积网络，然后对它们的结果进行比较的神经网络。

![Siamese](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hiofwbebj30ni0bewg1.jpg)

如上图示例，将图片 $x^{(1)}$、$x^{(2)}$ 分别输入两个相同的卷积网络中，经过全连接层后不再进行 Softmax，而是得到特征向量 $f(x^{(1)})$、$f(x^{(2)})$。这时，Similarity 函数就被定义为两个特征向量之差的 L2 范数：

$$d(x^{(1)}, x^{(2)}) = ||f(x^{(1)}) - f(x^{(2)})||^2\_2$$

相关论文：[Taigman et al., 2014, DeepFace closing the gap to human level performance](http://www.cs.wayne.edu/~mdong/taigman_cvpr14.pdf)

### Triplet 损失

**Triplet 损失函数**用于训练出合适的参数，以获得高质量的人脸图像编码。“Triplet”一词来源于训练这个神经网络需要大量包含 Anchor（靶目标）、Positive（正例）、Negative（反例）的图片组，其中 Anchor 和 Positive 需要是同一个人的人脸图像。

![Training-set-using-triplet-loss](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hiodz3jsj30fs0bz77i.jpg)

对于这三张图片，应该有：

$$||f(A) - f(P)||^2\_2 + \alpha \le ||f(A) - f(N)||^2\_2$$

其中，$\alpha$ 被称为**间隔（margin）**，用于确保 $f()$ 不会总是输出零向量（或者一个恒定的值）。

Triplet 损失函数的定义：

$$L(A, P, N) = max(||f(A) - f(P)||^2\_2 - ||f(A) - f(N)||^2\_2 + \alpha, 0)$$

其中，因为 $||f(A) - f(P)||^2\_2 - ||f(A) - f(N)||^2\_2 + \alpha$ 的值需要小于等于 0，因此取它和 0 的更大值。

对于大小为 $m$ 的训练集，代价函数为：

$$J = \sum^m\_{i=1}L(A^{(i)}, P^{(i)}, N^{(i)})$$

通过梯度下降最小化代价函数。

在选择训练样本时，随机选择容易使 Anchor 和 Positive 极为接近，而 Anchor 和 Negative 相差较大，以致训练出来的模型容易抓不到关键的区别。因此，最好的做法是人为增加 Anchor 和 Positive 的区别，缩小 Anchor 和 Negative 的区别，促使模型去学习不同人脸之间的关键差异。

相关论文：[Schroff et al., 2015,  FaceNet: A unified embedding for face recognition and clustering](https://arxiv.org/pdf/1503.03832.pdf)

### 二分类结构

除了 Triplet 损失函数，二分类结构也可用于学习参数以解决人脸识别问题。其做法是输入一对图片，将两个 Siamese 网络产生的特征向量输入至同一个 Sigmoid 单元，输出 1 则表示是识别为同一人，输出 0 则表示识别为不同的人。

Sigmoid 单元对应的表达式为：

$$\hat y = \sigma (\sum^K\_{k=1}w\_k|f(x^{(i)})\_{k} - x^{(j)})\_{k}| + b)$$

其中，$w\_k$ 和 $b$ 都是通过梯度下降算法迭代训练得到的参数。上述计算表达式也可以用另一种表达式代替：

$$\hat y = \sigma (\sum^K\_{k=1}w\_k
\frac{(f(x^{(i)})\_k - f(x^{(j)})\_k)^2}{f(x^{(i)})\_k + f(x^{(j)})\_k} + b)$$

其中，$\frac{(f(x^{(i)})\_k - f(x^{(j)})\_k)^2}{f(x^{(i)})\_k + f(x^{(j)})\_k}$ 被称为 $\chi$ 方相似度。

无论是对于使用 Triplet 损失函数的网络，还是二分类结构，为了减少计算量，可以提前计算好编码输出 $f(x)$ 并保存。这样就不必存储原始图片，并且每次进行人脸识别时只需要计算测试图片的编码输出。

## 神经风格迁移

**神经风格迁移（Neural style transfer）**将参考风格图像的风格“迁移”到另外一张内容图像中，生成具有其特色的图像。

![Neural-style-transfer](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hioa4airj30pq0btk2v.jpg)

### 深度卷积网络在学什么？

想要理解如何实现神经风格转换，首先要理解在输入图像数据后，一个深度卷积网络从中都学到了些什么。我们借助可视化来做到这一点。

![Visualizing-deep-layers](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hio81mcsj30ok0d7wpn.jpg)

我们通过遍历所有的训练样本，找出使该层激活函数输出最大的 9 块图像区域。可以看出，浅层的隐藏层通常检测出的是原始图像的边缘、颜色、阴影等简单信息。随着层数的增加，隐藏单元能捕捉的区域更大，学习到的特征也由从边缘到纹理再到具体物体，变得更加复杂。

相关论文：[Zeiler and Fergus., 2013, Visualizing and understanding convolutional networks](https://arxiv.org/pdf/1311.2901.pdf)

### 代价函数

神经风格迁移生成图片 G 的代价函数如下：

$$J(G) = \alpha \cdot J\_{content}(C, G) + \beta \cdot J\_{style}(S, G)$$

其中，$\alpha$、$\beta$ 是用于控制相似度比重的超参数。

神经风格迁移的算法步骤如下：

1. 随机生成图片 G 的所有像素点；
2. 使用梯度下降算法使代价函数最小化，以不断修正 G 的所有像素点。

相关论文：[Gatys al., 2015. A neural algorithm of artistic style](https://arxiv.org/pdf/1508.06576v2.pdf)

#### 内容代价函数

上述代价函数包含一个内容代价部分和风格代价部分。我们先来讨论内容代价函数 $J\_{content}(C, G)$，它表示内容图片 C 和生成图片 G 之间的相似度。

$J\_{content}(C, G)$ 的计算过程如下：

* 使用一个预训练好的 CNN（例如 VGG）；
* 选择一个隐藏层 $l$ 来计算内容代价。$l$ 太小则内容图片和生成图片像素级别相似，$l$ 太大则可能只有具体物体级别的相似。因此，$l$ 一般选一个中间层；
* 设 $a^{(C)[l]}$、$a^{(G)[l]}$ 为 C 和 G 在 $l$ 层的激活，则有：

$$J\_{content}(C, G) = \frac{1}{2}||(a^{(C)[l]} - a^{(G)[l]})||^2$$

$a^{(C)[l]}$ 和 $a^{(G)[l]}$ 越相似，则 $J\_{content}(C, G)$ 越小。

#### 风格代价函数

![Intuition-about-style-of-an-image](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hio60a4bj30a50g07a6.jpg)

每个通道提取图片的特征不同，比如标为红色的通道提取的是图片的垂直纹理特征，标为黄色的通道提取的是图片的橙色背景特征。那么计算这两个通道的相关性，相关性的大小，即表示原始图片既包含了垂直纹理也包含了该橙色背景的可能性大小。通过 CNN，“风格”被定义为同一个隐藏层不同通道之间激活值的相关系数，因其反映了原始图片特征间的相互关系。

对于风格图像 S，选定网络中的第 $l$ 层，则相关系数以一个 gram 矩阵的形式表示：

$$G^{\[l](S)}\_{kk'} = \sum^{n^{[l]}\_H}\_{i=1} \sum^{n^{[l]}\_W}\_{j=1} a^{\[l](S)}\_{ijk} a^{\[l](S)}\_{ijk'}$$

其中，$i$ 和 $j$ 为第 $l$ 层的高度和宽度；$k$ 和 $k'$ 为选定的通道，其范围为 $1$ 到 $n\_C^{[l]}$；$a^{\[l](S)}\_{ijk}$ 为激活。

同理，对于生成图像 G，有：

$$G^{\[l](G)}\_{kk'} = \sum^{n^{[l]}\_H}\_{i=1} \sum^{n^{[l]}\_W}\_{j=1} a^{\[l](G)}\_{ijk} a^{\[l](G)}\_{ijk'}$$

因此，第 $l$ 层的风格代价函数为：

$$J^{[l]}\_{style}(S, G) = \frac{1}{(2n^{[l]}\_Hn^{[l]}\_Wn^{[l]}\_C)^2} \sum\_k \sum\_{k'}(G^{\[l](S)}\_{kk'} - G^{\[l](G)}\_{kk'})^2$$

如果对各层都使用风格代价函数，效果会更好。因此有：

$$J\_{style}(S, G) = \sum\_l \lambda^{[l]} J^{[l]}\_{style}(S, G)$$

其中，$lambda$ 是用于设置不同层所占权重的超参数。

### 推广至一维和三维

之前我们处理的都是二维图片，实际上卷积也可以延伸到一维和三维数据。我们举两个示例来说明。

![1D-3D-Convolution](https://tva1.sinaimg.cn/large/006y8mN6ly1g7hio1u4fij30lb06qgmr.jpg)

EKG 数据（心电图）是由时间序列对应的每个瞬间的电压组成，是一维数据。一般来说我们会用 RNN（循环神经网络）来处理，不过如果用卷积处理，则有：

* 输入时间序列维度：14 x 1
* 滤波器尺寸：5 x 1，滤波器个数：16
* 输出时间序列维度：10 x 16

而对于三维图片的示例，有

* 输入 3D 图片维度：14 x 14 x 14 x 1
* 滤波器尺寸：5 x 5 x 5 x 1，滤波器个数：16
* 输出 3D 图片维度：10 x 10 x 10 x 16