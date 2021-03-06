---
layout: post
# title:  "Face-Keypoint-Detection"
date: 2019-09-06
# date:   2019-09-25 22:16:11 +0800
categories: [Deep-Learning, AI]
---
Ref from: https://niuyuanyuanna.github.io/2018/11/08/computer_version/face-keypoint-detection/

# 人脸关键点检测

关于人脸识别和表情分类的一些[论文](https://zhuanlan.zhihu.com/p/31638581)

## 人脸关键点检测介绍

人脸关键点检测也称为人脸关键点检测、定位或者人脸对齐，是指给定人脸图像，定位出人脸面部的关键区域位置，包括眉毛、眼睛、鼻子、嘴巴、脸部轮廓等。

关键点的集合称作形状(shape)，形状包含了关键点的位置信息，而这个位置信息一般可以用两种形式表示，第一种是关键点的位置相对于整张图像，第二种是关键点的位置相对于人脸框(标识出人脸在整个图像中的位置)。把第一种形状称作绝对形状，它的取值一般介于 [0∼h][0∼h]或[0∼w][0∼w]，第二种形状我们称作相对形状，它的取值一般介于 0 到 1。这两种形状可以通过人脸框转换。

### 分类

人脸关键点检测分为三种：

- 基于ASM(Active Shape Model)和AAM (Active Appearnce Model) 的传统方法、参数化方法
- 基于CSR(Cascaded Shape Regression)的方法、非参数化方法
- 基于深度学习、非参数化方法

基于参数化形状模型的方法可依据其外观模型的不同，可进一步分为，基于局部的方法和基于全局的方法；对于非参数化进一步可分为基于样例的方法、基于图模型的方法、基于级联回归的方法和基于深度学习的方法。

### 人脸关键点评价标准

目前主要的衡量标准是算法所获取的关键点位置与真实关键点位置之间的偏差。在评价偏差时，由于不同人脸图像的实际大小难免会有所差异，为便于在同样的尺度下比较算法性能，需要采用一定的数据归一化策略。 目前主流的方法是基于两眼间的距离进行人脸大小的标准化：
$$
ex=∣∣x^−xGT∣∣DIODex=DIOD∣∣x^−xGT∣∣
$$
其中分子DIODDIOD表示估计值与真实值的欧式距离，分母∣∣x^−xGT∣∣∣∣x^−xGT∣∣表示双眼距离，即两眼中心的欧式距离。也有采用边界框对角线作为归一化因子来评价偏差。

### 人脸常用数据库

数据库可以分为两类：主动式捕获的数据和被动式捕获的数据。主动式捕获的数据是在实验室里，对光照变化、遮挡、头部姿态和面部表情可控的情况下，对固定人员进行照片采集。被动式捕获的数据则是在社交网站等一些环境不可控的条件下采集而得。

- 主动式数据

1. CMU Multi-PIE：在2004年10月至2005年3月的四次会议中收集的，支持在姿态、光照和表情变化条件下识别人脸的算法的开发。 该数据库包含337个主题和超过750,000个305GB数据的图像。 共记录了六种不同的表情：中性，微笑，惊奇，斜视，厌恶和尖叫。 在15个视图和19个不同照明条件下记录受试者，这个数据库的一个子集被标记为68点或39点。
2. XM2VTS：收集了295人的2360个彩色图像，声音文件和3D人脸模型，这2360个彩色图像标有68个关键点。
3. AR：包含超过4000个彩色图像，对应126人（70名男性和56名女性）的脸部。图像是在可控的条件下，以不同的面部表情，光照条件和遮挡（太阳镜和围巾）拍摄的。Ding and Martinez手动为每张脸部图像标注了130个关键点。
4. IMM：包含240张40个人的彩色图像（7名女性和33名男性）。 每张图像都对眉毛、眼睛、鼻子、嘴巴和下巴进行标注，共计58个标记点。
5. MUCT：由276个人的3755张图像组成，每张图像有76个关键点。 这个数据库中的面孔在不同的光照、不同的年龄和不同的种族的条件下拍摄。
6. PUT：采集了部分光照条件可控的100个人，且沿着俯仰角和偏航角旋转的9971张高分辨率图像（2048×1536），每张图像都标有30个关键点。

- 被动式数据

1. BioID：记录在室内实验室环境中，但使用“真实世界”的条件。 该数据库包含23个主题的1521个灰度人脸图像，每张图像标记20个关键点。
2. LFW：包含从网上收集的5724个人的13,233幅面部图像，其中1680人在数据集中有两张或更多的照片。虽然，这个数据库没有提供标记点，但可以从其余网站上获取。
3. AFLW(Annotated Facial Landmarks in the Wild) ：是一个大规模、多视角和真实环境下的人脸数据库。图像是从图片分享网站Flickr上收集，该数据库共包含25,993张图像，每张图像标有21个关键点。
4. LFPW(Labeled Face Parts in the Wild)：由1400个面部图像（1100作为训练集，其他300个图像作为测试集）组成。所有数据均从google, Flickr和Yahoo上获取，每张图像标记35个关键点，但在文献中，通常采用29个关键点。
5. AFW(Annotated Faces in the Wild)：包含205个图像，特点是：背景高度混乱，人脸比例和姿势都有很大的变化，每张图像均有6个关键点和边界框。
6. 300-W(300 Faces in-the-Wild Challenge)：一个混合数据库，由多个已发布数据库（LFPW，Helen，AFW和XM2VTS）的面部图像和一个新收集的数据库IBUG组成。 所有这些图像都重新标注了68个关键点。

### 算法

#### ASM检测方法

ASM(Active Shape Model)是由Cootes于1995年提出的经典的人脸关键点检测算法，主动形状模型即通过形状模型对目标物体进行抽象，ASM是一种基于点分布模型（Point Distribution Model, PDM）的算法。在PDM中，外形相似的物体，例如人脸、人手、心脏、肺部等的几何形状可以通过若干关键点（landmarks）的坐标依次串联形成一个形状向量来表示。ASM算法需要通过人工标定的方法先标定训练集，经过训练获得形状模型，再通过关键点的匹配实现特定物体的匹配。

其检测过程主要分为两步：

- 训练
  - 图像预处理：
    - 搜集n个训练样本（n=400）， 手动标记脸部关键点；
    - 将训练集中关键点的坐标串成特征向量
    - 对形状进行归一化和对齐（对齐采用Procrustes方法）
    - 对齐后的形状特征做PCA处理
  - 为关键点构建局部特征（在每次迭代搜索过程中每个关键点可以寻找新的位置）：
    - 局部特征一般用梯度特征，以防光照变化
    - 有的方法沿着边缘的法线方向提取，有的方法在关键点附近的矩形区域提取
- 搜索
  - 计算眼睛（或者眼睛和嘴巴）的位置，做简单的尺度和旋转变化，对齐人脸
  - 在对齐后的各个点附近搜索，匹配每个局部关键点（常采用马氏距离），得到初步形状
  - 用平均人脸（形状模型）修正匹配结果
  - 迭代直到收敛

优点：模型简单直接，架构清晰明确，易于理解和应用，而且对轮廓形状有着较强的约束

缺点：其近似于穷举搜索的关键点定位方式在一定程度上限制了其运算效率

#### AAM

AAM（Active Appearance Models）。1998年，Cootes对ASM进行改进，不仅采用形状约束，而且又加入整个脸部区域的纹理特征，提出了AAM算法[2]。AAM于ASM一样，主要分为两个阶段，模型建立阶段和模型匹配阶段。其中模型建立阶段包括对训练样本分别建立形状模型(Shape Model)和纹理模型(Texture Model)，然后将两个模型进行结合，形成AAM模型。

#### CPR

2010年，Dollar提出CPR（Cascaded Pose Regression, 级联姿势回归），CPR通过一系列回归器将一个指定的初始预测值逐步细化，每一个回归器都依靠前一个回归器的输出来执行简单的图像操作，整个系统可自动的从训练样本中学习。
人脸关键点检测的目的是估计向量

S=(x1,x2,⋅⋅⋅,xk,⋅⋅⋅,xK)∈R2KS=(x1,x2,⋅⋅⋅,xk,⋅⋅⋅,xK)∈R2K

其中K表示关键点的个数，由于每个关键点有横纵两个坐标，所以S的长度为2K。CPR检测一共有T个阶段，在每个阶段中首先进行特征提取，得到

ft=ϕ(I,St)ft=ϕ(I,St)

这里特征使用的是shape-indexed features，也可以使用诸如HOG、SIFT等人工设计的特征，或者其他可学习特征（learning based features），然后通过训练得到的回归器rtrt来估计增量ΔSΔS( update vector)

ΔS=rt(ϕ(I,St))ΔS=rt(ϕ(I,St))

把ΔSΔS加到前一个阶段的SS上得到新的SS，这样通过不断的迭代即可以得到最终的S(shape)。

St+1=St+ΔSSt+1=St+ΔS

#### DCNN

2013 年，Sun 等人 首次将 CNN 应用到人脸关键点检测，提出一种级联的 CNN（拥有三个层级）——DCNN(Deep Convolutional Network)，此种方法属于级联回归方法。作者通过精心设计拥有三个层级的级联卷积神经网络，不仅改善初始不当导致陷入局部最优的问题，而且借助于 CNN 强大的特征提取能力，获得更为精准的关键点检测。

[![img](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/06230452.png)](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/06230452.png)

如上图所示，DCNN由三个level构成。level-1是3个CNN网络；level-2是10个CNN块构成，每个关键点采用两个CNN；level-3结构类似于level-2，都为10个CNN。

Level-1的三个CNN分别为 F1（Face 1）、EN1（Eye，Nose）、NM1（Nose，Mouth）。F1 输入尺寸为 39*39，输出 5 个关键点的坐标；EN1 输入尺寸为 39*31，输出是 3 个关键点的坐标；NM11 输入尺寸为 39*31，输出是 3 个关键点；Level-1 的输出为三个 CNN 输出取平均。

Level-2，由 10 个 CNN 构成，输入尺寸均为 15*15，每两个组成一对，一对 CNN 对一个关键点进行预测，预测结果同样是采取平均。

Level-3 与 Level-2 一样，由 10 个 CNN 构成，输入尺寸均为 15*15，每两个组成一对。Level-2 和 Level-3 是对 Level-1 得到的粗定位进行微调，得到精细的关键点定位。

Level-1 之所以比 Level-2 和 Level-3 的输入要大，是因为作者认为，由于人脸检测器的原因，边界框的相对位置可能会在大范围内变化，再加上面部姿态的变化，最终导致输入图像的多样性，因此在 Level-1 应该需要有足够大的输入尺寸。Level-1 与 Level-2 和 Level-3 还有一点不同之处在于，Level-1 采用的是局部权值共享（Lcally Sharing Weights），作者认为传统的全局权值共享是考虑到，某一特征可能在图像中任何位置出现，所以采用全局权值共享。然而，对于类似人脸这样具有固定空间结构的图像而言，全局权值共享就不奏效了。因为眼睛就是在上面，鼻子就是在中间，嘴巴就是在下面的。所以作者采用局部权值共享，通过实验证明了局部权值共享给网络带来性能提升。

DCNN 采用级联回归的思想，从粗到精的逐步得到精确的关键点位置，不仅设计了三级级联的卷积神经网络，还引入局部权值共享机制，从而提升网络的定位性能。最终在数据集 BioID 和 LFPW 上均获得当时最优结果。速度方面，采用 3.3GHz 的 CPU，每 0.12 秒检测一张图片的 5 个关键点。

#### Face++ DCNN

2013 年，Face++在 DCNN 模型上进行改进，提出从粗到精的人脸关键点检测算法，实现了 68 个人脸关键点的高精度定位。该算法将人脸关键点分为内部关键点和轮廓关键点，内部关键点包含眉毛、眼睛、鼻子、嘴巴共计 51 个关键点，轮廓关键点包含 17 个关键点。

针对内部关键点和外部关键点，该算法并行的采用两个级联的 CNN 进行关键点检测，网络结构如图所示：

[![img](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/92897228.jpg)](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/92897228.jpg)

针对内部 51 个关键点，采用四个层级的级联网络进行检测。其中，Level-1 主要作用是获得面部器官的边界框；Level-2 的输出是 51 个关键点预测位置，这里起到一个粗定位作用，目的是为了给 Level-3 进行初始化；Level-3 会依据不同器官进行从粗到精的定位；Level-4 的输入是将 Level-3 的输出进行一定的旋转，最终将 51 个关键点的位置进行输出。针对外部 17 个关键点，仅采用两个层级的级联网络进行检测。Level-1 与内部关键点检测的作用一样，主要是获得轮廓的 bounding box；Level-2 直接预测 17 个关键点，没有从粗到精定位的过程，因为轮廓关键点的区域较大，若加上 Level-3 和 Level-4，会比较耗时间。最终面部 68 个关键点由两个级联 CNN 的输出进行叠加得到。

算法创新点：

1. 把人脸的关键点定位问题，划分为内部关键点和轮廓关键点分开预测，有效的避免了 loss 不均衡问题
2. 在内部关键点检测部分，并采用 DCNN 的方法，将每个关键点采用两个 CNN 进行预测，而是每个器官采用一个 CNN 进行预测，从而减少计算量
3. 相比于 DCNN，没有直接采用人脸检测器返回的结果作为输入，而是增加一个边界框检测层（Level-1），可以大大提高关键点粗定位网络的精度。

#### TCDNN

2014 年，Zhang 等人将 MTL（Multi-Task Learning）应用到人脸关键点检测中，提出 TCDCN（Tasks-Constrained Deep Convolutional Network）。作者认为，在进行人脸关键点检测任务时，结合一些辅助信息可以帮助更好的定位关键点，这些信息如，性别、是否带眼镜、是否微笑和脸部的姿势等等。作者将人脸关键点检测（5 个关键点）与性别、是否带眼镜、是否微笑及脸部的姿势这四个子任务结合起来构成一个多任务学习模型，模型框架如图所示。

[![img](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/15813947.jpg)](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/15813947.jpg)

网络输入为40×40的灰度图，通过CNN后得到2×2×64的特征图，再通过一层含有100个神经元的全连接层输出最终提取到的共享特征。该特征为所有任务共享，对于关键点检测问题，就采用线性回归模型；对于分类问题，就采用逻辑回归。

在传统 MLT 中，各任务重要程度是一致的，其目标方程如下：

arg⁡min⁡∑t−1T∑i=1Nℓ(yit,f(xit;wt))+Φ(wt){wt}argmint−1∑Ti=1∑Nℓ(yit,f(xit;wt))+Φ(wt){wt}t=1T

其中，

- f(xit;wt)f(xit;wt)表示输入矩阵xitxit与权值矩阵$ \mathbf{w}^t$运算后得到的输出
- ℓ(.)ℓ(.)表示损失函数
- Φ(wt)Φ(wt)表示正则化

对于各任务 t 而言，其重要性是相同的，但是在多任务学习中，往往不同任务的学习难易程度不同，若采用相同的损失权重，会导致学习任务难以收敛。文章针对多任务学习中，不同学习难度问题进行了优化，提出带权值的目标函数：

wr,{wa}  ∑i=1Nℓ(yit,f(xit;wt))+∑i=1N∑a∈Aλaℓ(yia,f(xia;wa))argminwr,{wa}a∈A  i=1∑Nℓ(yit,f(xit;wt))+i=1∑Na∈A∑λaℓ(yia,f(xia;wa))

式中前一项为人脸关键点检测的损失函数，第二项表示其他任务的损失函数，λaλa为任务aa的重要程度。在论文中，四个子任务分别为：性别、是否带眼镜、微笑、脸部姿势，因此，优化目标函数为：

wr,{wa}  12∑i=1N∥(yit,f(xit;wt)∥2+∑i=1N∑a∈Aλayialog⁡(p(yia∣xia;wa))+∑t=1T∥wa∥22argminwr,{wa}a∈A  21i=1∑N∥(yit,f(xit;wt)∥2+i=1∑Na∈A∑λayialog(p(yia∣xia;wa))+t=1∑T∥wa∥22

分类任务采用交叉熵损失函数。

针对多任务学习的另外一个问题——各任务收敛速度不同，本文提出一种新的提前停止（Early Stopping）方法。当某个子任务达到最好表现以后，这个子任务就对主任务已经没有帮助，就可以停止这个任务。

TCDCN 采用多任务学习方法对人脸关键点进行检测，针对多任务学习在人脸关键点检测任务中的两个主要问题：不同任务学习难易程度不同以及不同任务收敛速度不同，分别提出了新目标函数和提前停止策略加以改进，最终在 AFLW 和 AFW 数据集上获得领先的结果。同时对比于级联 CNN 方法，在 Intel Core i5 cpu 上，级联 CNN 需要 0.12s，而 TCDCN 仅需要 17ms，速度提升七倍有余。

#### MTCNN

2016 年，Zhang 等人提出一种多任务级联卷积神经网络（MTCNN, Multi-task Cascaded Convolutional Networks）用以同时处理人脸检测和人脸关键点定位问题。作者认为人脸检测和人脸关键点检测两个任务之间往往存在着潜在的联系，然而大多数方法都未将两个任务有效的结合起来，本文为了充分利用两任务之间潜在的联系，提出一种多任务级联的人脸检测框架，将人脸检测和人脸关键点检测同时进行。

MTCNN 包含三个级联的多任务卷积神经网络，分别是 Proposal Network (P-Net)、Refine Network (R-Net)、Output Network (O-Net)，每个多任务卷积神经网络均有三个学习任务，分别是人脸分类、边框回归和关键点定位。网络结构如图所示：

[![img](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/14009657.jpg)](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/14009657.jpg)

MTCNN 实现人脸检测和关键点定位分为三个阶段。首先由 P-Net 获得了人脸区域的候选窗口和边界框的回归向量，并用该边界框做回归，对候选窗口进行校准，然后通过非极大值抑制（NMS）来合并高度重叠的候选框。然后将 P-Net 得出的候选框作为输入，输入到 R-Net，R-Net 同样通过边界框回归和 NMS 来去掉那些 false-positive 区域，得到更为准确的候选框；最后，利用 O-Net 输出 5 个关键点的位置。

在具体训练过程中，作者就多任务学习的损失函数计算方式进行相应改进。在多任务学习中，当不同类型的训练图像输入到网络时，有些任务是不进行学习的，因此相应的损失应为 0。例如，当训练图像为背景（Non-face）时，边界框和关键点的 loss 应为 0，文中提供计算公式自动确定 loss 的选取，公式为：

min⁡∑i=1N∑j∈{det,box,landmark}αjβijLijmini=1∑Nj∈{det,box,landmark}∑αjβijLij

其中

- αjαj表示第jj个任务的重要程度，在P-Net中，αdet=1αdet=1，αbox=0.5αbox=0.5，αlandmark=0.5αlandmark=0.5；在R-Net中αdet=1αdet=1，αbox=0.5αbox=0.5，αlandmark=1αlandmark=1。在R-Net中将$\alpha_{landmark} $增大，因为需要对关键点进行检测，所以相应增大任务重要性
- βij∈(0,1)βij∈(0,1)作为样本类型指示器

为了提升网络性能，需要挑选出困难样本（Hard Sample），传统方法是通过研究训练好的模型进行挑选，而本文提出一种能在训练过程在线挑选困难样本的方法。在 mini-batch 中，对每个样本的损失进行排序，挑选前 70% 较大的损失对应的样本作为困难样本，同时在反向传播时，忽略那 30% 的样本，因为那 30% 样本对更新作用不大。

#### TCNN

TCNN（Tweaked Convolutional Neural Networks）2016 年，Wu 等人研究了 CNN 在人脸关键点定位任务中到底学习到的是什么样的特征，在采用 GMM（Gaussian Mixture Model, 混合高斯模型）对不同层的特征进行聚类分析，发现网络进行的是层次的，由粗到精的特征定位，越深层提取到的特征越能反应出人脸关键点的位置。针对这一发现，提出了 TCNN（Tweaked Convolutional Neural Networks），其网络结构如图所示：

[![img](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/89918024.jpg)](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/89918024.jpg)

左边为Vanilla CNN，针对 FC5FC5得到的特征进行 K 个类别聚类，将训练图像按照所分类别进行划分，用以训练所对应的 FC6KFC6K。测试时，图片首先经过 Vanilla CNN 提取特征，即 FC5FC5的输出。将 FC5FC5输出的特征与 K 个聚类中心进行比较，将 FC5FC5输出的特征划分至相应的类别中，然后选择与之相应的 FC6FC6进行连接，最终得到输出。

作者对 Vanilla CNN 中间各层特征进行聚类分析，并统计出关键点在各层之间的变化程度。越深层提取到的特征越紧密，因此越深层提取到的特征越能反应出人脸关键点的位置。作者在采用 K=64 时，对所划分簇的样本进行平均后绘图如下：

[![img](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/62921355.jpg)](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/62921355.jpg)

从图上可发现，每一个簇的样本反应了头部的某种姿态，甚至出现了表情和性别的差异。因此可推知，人脸关键点的位置常常和人脸的属性相关联。因此为了得到更准确的关键点定位，作者使用具有相似特征的图片训练对应的回归器，最终在人脸关键点检测数据集 AFLW,AFW 和 300W 上均获得当时最佳效果。

## DAN

### 主要内容

DAN是一种人脸对齐的方法，采用级联神经网络结构，充分利用人脸的全局信息，而不是局部信息，避免局部最小化。

1. 参考CSR框架，通过前向传播提取特征，训练前向传播的backbone网络得到关键点位的偏差，替代CSR中的回归器
2. 用级联结构来实现CSR中的迭代
3. 利用人脸所有信息T(I)T(I)、H(I)H(I)、F(I)F(I)作为输入，得到关键点偏差
4. 构造级联网络结构
5. 分级训练网络，每一级网络loss不收敛后再训练下一级网络

### 网络结构

2017 年，Kowalski 等人提出一种新的级联深度神经网络——DAN（Deep Alignment Network），以往级联神经网络输入的是图像的某一部分，与以往不同，DAN 各阶段网络的输入均为整张图片。当网络均采用整张图片作为输入时，DAN 可以有效的克服头部姿态以及初始化带来的问题，从而得到更好的检测效果。之所以 DAN 能将整张图片作为输入，是因为其加入了关键点热图（Landmark Heatmaps），关键点热图的使用是本文的主要创新点。DAN 基本框架如图所示：

[![img](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/55049944.jpg)](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/55049944.jpg)

DAN 包含多个阶段，每一个阶段含三个输入和一个输出，输入分别是被矫正过的图片、关键点热图和由全连接层生成的特征图，输出是面部形状（Face Shape）。其中，CONNECTION LAYER 的作用是将本阶段得输出进行一系列变换，生成下一阶段所需要的三个输入，具体操作如下图所示：

[![img](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/83789038.jpg)](https://github.com/niuyuanyuanna/BlogImages/raw/master/computerVersion/83789038.jpg)

第一阶段的输入仅有原始图片和 S0S0。面部关键点的初始化即为 S0S0，是由所有关键点取平均得到，第一阶段输出 S1S1。对于第二阶段， S1S1经第一阶段的 CONNECTION LAYERS 进行转换，分别得到转换后图片 T2(I)T2(I)、 S1S1所对应的热图 H2H2和第一阶段 fc1fc1层输出，这三个正是第二阶段的输入。如此周而复始，直到最后一个阶段输出 SNSN。

DAN 要做的“IMAGE TRANSFORM“，就是图片矫正， DAN 对姿态变换具有很好的适应能力，或许就得益于这个“IMAGE TRANSFORM“。StSt公式为：

St=Tt−1(Tt(St−1)+ΔSt)St=Tt−1(Tt(St−1)+ΔSt)

Feed forward NN网络参数为：

|  Name  |  Shape-in  | Shape-out  |  Kernel   |
| :----: | :--------: | :--------: | :-------: |
| conv1a | 112×112×1  | 112×112×64 |  3×3×1,1  |
| conv1b | 112×112×64 | 112×112×64 | 3×3×64,1  |
| pool1  | 112×112×64 |  56×56×64  |  2×2×1,2  |
| conv2a |  56×56×64  | 56×56×128  | 3×3×64,1  |
| conv2b | 56×56×128  | 56×56×128  | 3×3×128,1 |
| pool2  | 56×56×128  | 28×28×128  |  2×2×1,2  |
| conv3a | 28×28×128  | 28×28×256  | 3×3×128,1 |
| conv3b | 28×28×256  | 28×28×256  | 3×3×256,1 |
| pool3  | 28×28×256  | 14×14×256  |  2×2×1,2  |
| conv4a | 14×14×256  | 14×14×512  | 3×3×256,1 |
| conv4b | 14×14×512  | 14×14×512  | 3×3×512,1 |
| pool4  | 14×14×512  |  7×7×512   |  2×2×1,2  |
|  fc1   |  7×7×512   |  1×1×256   |     -     |
|  fc2   |  1×1×256   |  1×1×136   |     -     |

Feed Forward NN的输入是经过“IMAGE TRANSFORM“之后得到的偏移量ΔStΔSt，它是在新特征空间下的偏移量，在经过偏移后再经过反变换Tt−1(⋅)Tt−1(⋅)，将其还原到原始空间。

关键点热度图的计算就是一个中心衰减，关键点处值最大，越远则值越小，公式如下：

H(x,y)=11+Si∈Tt(St−1)  ∥(x,y)−Si∥H(x,y)=1+minSi∈Tt(St−1)  ∥(x,y)−Si∥1

从fc1fc1层生成特种图的目的是人为给 CNN 增加上一阶段信息。总而言之，DAN 是一个级联思想的关键点检测方法，通过引入关键点热图作为补充，DAN 可以从整张图片进行提取特征，从而获得更为精确的定位。

## EmotionalDAN

Author: NYY

Link: http://yoursite.com/2018/11/08/computer_version/face-keypoint-detection/

Copyright Notice: All articles in this blog are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)unless stating additionally.