---
layout: post
categories: AI
tag: [] 



---



> Two stages: RPN for localization, then classification & bbox regression on proposals
>
> Single shot: classification + bbox regression at one time

### Faster RCNN

#### `VGG` backbone

* VGG: Input 224x224, therefore, 224/2^4 = 14, 14x14 for conv-5 (ch-512, same as conv-4),  13 conv, 13 ReLU, 4 Pooling

* Faster RCNN's image size :  ==> 800x600 (image's input by python 's cv2)

  ```
   # reshape network inputs
    net.blobs['data'].reshape(*(blobs['data'].shape))
  ```

  As we can see, the input blob `'data'` is reshaped according to the input image size. Once you `forward` caffe will reshape all consequent blobs according to the input shape；　`*` means convert passed argument from tuple to positional parameters

* RPN: 3x3x512, as each point fuses 3x3 info arounding it. and then calc + & - anchors as well as bbox regression shift, and then calc proposals;

  `ROI Pooling` extract `proposal feature` from `feature map`for FC and softmax

* 9 anchors for each point --> + & -

* TRAINING: 128 + anchors and 128 - anchors
  
  * Suitable Anchors:

![[公式]](https://www.zhihu.com/equation?tex=\text{ceil}(800%2F16)+\times+\text{ceil}(600%2F16)+\times+9%3D50\times38+\times9%3D17100)

> https://github.com/rbgirshick/py-faster-rcnn/tree/master/models/pascal_voc/VGG16/faster_rcnn_end2end



那么为何要在softmax前后都接一个reshape layer？其实只是为了便于softmax分类，至于具体原因这就要从caffe的实现形式说起了。在caffe基本数据结构blob中以如下形式保存数据：

```text
blob=[batch_size, channel，height，width]
```

对应至上面的保存positive/negative anchors的矩阵，其在caffe blob中的存储形式为[1, 2x9, H, W]。而在softmax分类时需要进行positive/negative二分类，所以reshape layer会将其变为[1, 2, 9xH, W]大小，即单独“腾空”出来一个维度以便softmax分类，之后再reshape回复原状。贴一段caffe softmax_loss_layer.cpp的reshape函数的解释，非常精辟：

```cpp
"Number of labels must match number of predictions; "
"e.g., if softmax axis == 1 and prediction shape is (N, C, H, W), "
"label count (number of labels) must be N*H*W, "
"with integer values in {0, 1, ..., C-1}.";
```

* soomth-L1
* ROI pooliing 7x7



#### *for `ZF` backbone *

==> ch-256 before RPN

---

### YOLO v1

* 45FPS

* Can we just out bbox (x,y,w,h) and (c) ? But we found as objected to be detected increase, output dimension of model also increase, not able to be determined.

  ==> YOLO does this by gridding image into grids, within each of which being able to output class and bbox.

* 7x7 grids on image, 30 channels, as No RPN, just use a big net to catch all fishes

* 2 predictor for each cell.

* Q: If class prediction is not sharing, can one cell predict two obj?

  * No. In this way,  how do the two predictor divide their works?
  * Faster RCNN OK because of anhchors and IOU w/ GT, which got introduced in YOLO v2

* Why 2 bounding boxes?

  * Predictor with bigger IOU with GT while training, is responsible for detecting the corresponding object.

* x, y means shift relative to cell's upper-left corner; w, h relative to the whole image

  ![image-20200106075944588](https://tva1.sinaimg.cn/large/006tNbRwly1gamijfkmaej30oy0iy77z.jpg)

* confidence = *Pr(Object) x IOU*,  IOU is calculated during training, Pr(Object) is bool

  So, Pr(Classi|Object) x *Pr(Object) x IOU* , Pr(Classi|Object) is meaningful only when Pr(Object) is not 0.

Ref: https://zhuanlan.zhihu.com/p/37850811

---

### YOLO v2

* input: 416x416 ==> 13 x 13

* No FC (YOLO v1 has FC to turn 1024x7x7 into 30x7x7)

* 5 Anchor, so that **able to predict not only one obj for each cell**, but 5

* BN -- quickly converge, and for regularization

* Fully convolutional network architecture, so any size of image.

* Skipping `reorg` layer --  after conv5-5, making gradient able forward. 

  ![image-20200106111017191](https://tva1.sinaimg.cn/large/006tNbRwly1gamo1nin68j30u60700ul.jpg)

* Prediction: 
  (4 + 1 + num_class) for `each anchor`。Use sigmoid to make value btw 0~1. Use exponential for scaling.

  ![image-20200106112133343](https://tva1.sinaimg.cn/large/006tNbRwly1gamoddpf2zj30um0ta140.jpg)

* anchor with largest IOU (by moving both of anchor and GT_box to upper-left corner) to predict correcponding obj

* Loss: 

  * anchor predicting obj xywh: L2
  * anchor not predicing obj xywh: for correct anchor's xywh
  * anchor predicting obj confidence: IOU btw predicted bbox and GT bbox
  * anchor not predicing obj confidence: for correct anchor's xywh

* Multi-scale:

  [320,320]，[416,416]和[512,512]，==> grids: [10,10], [13,13], [16,16]. 

  During training, every 10 batches, one size btw 320x320 ~ 608x608 is chosen

Ref: https://zhuanlan.zhihu.com/p/40659490

---

### SSD

prototxt: https://github.com/intel/caffe/blob/master/models/intel_optimized_models/ssd/VGGNet/VOC0712/SSD_300x300/deploy.prototxt



* as YOLO, turn `detection` problem into `regression` problem

* as FasterRCNN's anchor, proposed `prior box`,  for each feature map

  ![image-20200106122821151](https://tva1.sinaimg.cn/large/006tNbRwly1gamqauu7ioj30l402smxd.jpg)

  By this formula, Prior Box size could be determined for each feature map together with `aspect ratio`

  m: total feature maps adopted

  * `default box` : abstract concept of `prior box`

  * `prior box`: adopted during training, the actually chosen default box for training

  * for `k default box` on their own feature maps: k x  (c+4) x  m x n

    * for confidence's output: c x k x m x n, 
      c x m x n for each of the k default box 

      if 20 classes, then we have 

    * for localization's output: 4 x k x m x n
      4 x m x n for each of the k default box 

    * All prior box amount: 
      $$
      38x38x4 + 19x19x6 +10x10x6 + 5x5x6 + 3x3x4 +1x1x4 = 8732
      $$
      k x (20+1), if k is 6 for each prior box; thus, 6x21 = 126 kernels
      k x 4, if k is 6 for each prior box; thus, 6x4 = 24 kernels

    * TRAINING to make prior box regress to GT box 

* as FPN, use Pyramidal Feature Hierarchy

* DIDN'T generate RPN, thus speed-up

* VGG-16 as backbone, the final 2 FC were turned into conv layers

* Permute: 32x19x19x24 ==> 32x24x19x19

  Flatten: 32x19x19x24 ==> 32x8664, where 32 is batch_size

  mbox_priorbox -- for training only

  mbox_loc

  mbox_conf

* **Sample augmentation**

* **+/- sampling**

  Match `prior box` and `GT` according to IOU (Jaccard Overlap). 

  \+ prior box  : matching to GT

  \- prior box : not mathcing to GT

  and soft all \- prior boxes according to classificatin loss, to control \+ : \-  is around 1 : 3

* GT : each GT has it mapping anchor. anchors are mapped into original image to match GT box

  <img src="https://tva1.sinaimg.cn/large/006tNbRwly1gams525z5sj30ha0f67ap.jpg" alt="image-20200106133152958" style="zoom:50%;" />

* input 300x300, pooling stride 2, thus conv4_3 length is 38, keep all left equals to 19, and final feature-map's length is 10
* **Loss**
  * loc-loss: smooth-L1 loss as Faster-RCNN
  * conf-loss: softmax loss for each class

![image-20200106115837659](https://tva1.sinaimg.cn/large/006tNbRwly1gampfyf6l8j31200ju46v.jpg)





ref: https://www.cnblogs.com/xuanyuyt/p/7222867.html

---

### FPN -- didn't dig into this too much.



### Focal Loss

### Optimization

* 

### MobileNet

* Explanation:

### MobileNet v2

### ShuffleNet

### 1x1

### ResNet

* To solve what problem?
* Explanation:
* Keywords:
  * Downsampling

### Mask RCNN

### RF (Receptive Field)

* Top-Down (Easy!)
* Bottom Up (Hard..)

### Gradient Vanishing

### Gradient Explosion

ROI Pooling vs ROI Align



------



## Machine Learning

### AdaBoost

* Explanation

  The delta btw y_hat and y will be fed into another weak classifier 

### SVM

**SVM本身是一个二值分类器**

　　SVM算法最初是为二值分类问题设计的，当处理多类问题时，就需要构造合适的多类分类器。

　　目前，构造SVM多类分类器的方法主要有两类

　　（1）直接法，直接在目标函数上进行修改，将多个分类面的参数求解合并到一个最优化问题中，通过求解该最优化问题“一次性”实现多类分类。这种方法看似简单，但其计算复杂度比较高，实现起来比较困难，只适合用于小型问题中；

　　（2）间接法，主要是通过组合多个二分类器来实现多分类器的构造，常见的方法有one-against-one和one-against-all两种。



### DT

smaller entropy means less wrongly classified

* ID3 (granually too small), 

  info gain  = Entropy 

* C4.5, 

* CART (binary tree, generally better than previous twos, needs some pruning sometimes)

  with gini coefficient



## Ensemble

### RF (Random Forest)

### Adaboost

* Bagging

  ​	to decrease variance

* Boosting 

  ​	to decrease bias

  mainly to enhance weak classifier into a strong one. According to the training result from previous classifie, and then train next classifier according to new sample's distribution.

* Adaboost increase wrongly-classifed samples' weights

Ref: https://zhuanlan.zhihu.com/p/37358517

---

used to eliminate the redundant features

### Decision Tree 

copied from : [https://chtseng.wordpress.com/2017/02/10/%E6%B1%BA%E7%AD%96%E6%A8%B9-decision-trees/](https://chtseng.wordpress.com/2017/02/10/決策樹-decision-trees/)

* Entropy definition

![image-20200119192602821](https://tva1.sinaimg.cn/large/006tNbRwly1gb23fhkw46j30l710otgs.jpg)



## **Gini Index (吉尼係數)**

採用GINI Index的代表是CART tree。CART是Classification And Regression Tree的縮寫，從字面上可看出它兼具分類與迴歸兩種功能，同時支援分類(Classification)與數字預測(Regression)，由於不限制應變數與自變數的類型，因此在使用上較具彈性，是目前最為常用的決策樹方法。

GINI係數與INFORMATION GAIN兩者有一個最大的差別：INFORMATION GAIN一次可產生多個不同節點，而GINI係數一次僅能產生兩個，即True或False的Binary分類。

下方一樣以板球為例來說明：（Gini係數公式為p2+q2）

**用性別來分類：** 

![img](https://chtseng.files.wordpress.com/2017/02/3148_gxdl-o-obg.png?w=1140)

Femail節點：十位女性，其中有2位打板球10位不打，Gini係數為
(0.2)2+(0.8)2=0.68

Male節點：20位男性，其中有13位打板球7位不打，Gini係數為
(0.65)2+(0.35)2=0.55

因此以性別分類的Gini係數加權後為：(10/30)*0.68+(20/30)*0.55 = 0.59。

**用班級來分類：**

![img](https://chtseng.files.wordpress.com/2017/02/3148_jsuhhmuveq1.png?w=1140)

  Class IX節點：此班14位同學，其中6位打板球8位不打，因此Gini係數為
(0.43)2+(0.57)2=0.51

  Class X節點：此班16位同學，其中9位打板球7位不打，因此Gini係數為
(0.56)2+(0.44)2=0.51

因此以班級分類的決策樹，其Gini係數加權結果：(14/30)*0.51+(16/30)*0.51 = 0.51。兩樹相互比較，以性別分類的吉尼係數大於以班級分類，因此系統會採用性別來進行節點的分類。

# **決策樹演算法的步驟**

1. **資料設定：**將原始資料分成兩組，一部分為訓練資料，一部分為測試資料
2. **決策樹生成：**使用訓練資料來建立決策樹，而在每一個內部節點，則依據屬性選擇指標 (如：資訊理論(Information Theory)…) 來評估選擇哪個屬性做分支的依據。此又稱節點分割 (Splitting Node)
3. **剪枝：**使用測試資料來進行決策樹修剪，將以上1~3步驟不斷重複進行，直到所有的新產生節點都是樹葉節點為止。

不過決策樹很容易有「Overfitting（過度擬合）」的問題，因為我們如果沒有對樹的成長作限制，演算法最後就會為每個不同特徵值創建新的分類節點，最後將所有資料作到100%正確的分類，因此為了預防Overfitting，我們會採取下列兩種方式：設限及剪枝。

## **設限**

1. Minimum samples for a node split：資料數目不得小於多少才能再產生新節點。
2. Minimum samples for a terminal node (leaf)：要成為葉節點，最少需要多少資料。
3. Maximum depth of tree (vertical depth)：限制樹的高度最多幾層。
4. Maximum number of terminal nodes：限制最終葉節點的數目
5. Maximum features to consider for split：在分離節點時，最多考慮幾種特徵值。

![img](https://chtseng.files.wordpress.com/2017/02/3148_vgszibb2dq.png?w=1140)



![image-20200119194043890](https://tva1.sinaimg.cn/large/006tNbRwly1gb23urtakpj30g410pdkb.jpg)

###  Training Imbalance

* Undersampling
* Oversampling

* SMOTE

### Why Regularization ? example?



### Backward 

------





### Comparison: 

![image-20200119175125694](https://tva1.sinaimg.cn/large/006tNbRwly1gb20p3423tj30kf0b7dhi.jpg)

#### 	Contrastive loss

​		2006, Yann LeCun's paper, mainly adopted for dimension reduction, 即本来相似的样本，在经过降维（特征提取）后，两个样本仍旧相似；而原本不相似的样本，在经过降维后，两个样本仍旧不相似。同样，该损失函数也可以很好的表达成对样本的匹配程度
​		F = kX, as SPRING model

#### 	Triplet loss

​		2015, Google

​		三元组损失：最小化锚点和具有相同的身份的正例之间的距离，并最大化锚点和不同身份的负例之间的距离。 目标： 相同标签的两个示例使其嵌入在嵌入空间中靠近在一起，不同标签的两个示例的嵌入距离要很远 但不希望推动每个标签的训练嵌入到非常小的簇中。 唯一的要求是给出同一类的两个正例和一个负例，负例应该比正例的距离至少远margin。 这与SVM中使用的margin非常相似，这里希望每个类的簇由margin分隔。		

​	**Triplet的选取**

- 如何选择triplet，如何用正负例构建triplet，对模型训练的效率有很大影响。easy negative example比较容易识别，没必要训练，否则会严重降低训练效率。若都采用hard negative example，又可能会影响训练效果。

- Facenet论文中采用了随机的semi-hard negative构建triplet进行训练。

- 基于negative example与anchor和positive距离，分为三类三元组：

- - 容易三元组(easy triplets)：损失为0的三元组，因为d(a,n)>d(a,p)+margin
  - 困难三元组(hard triplets) ：其中负例比正例更靠近锚点，即d(a,n)<d(a,p)
  - 半困难三元组(semi-hard triplets)：其中负例不比正例更接近锚点，但仍有大于0的损失，d(a,p)<d(a,n)<d(a,p)+margin

#### 	Center loss

Center Loss源于深圳先研院乔宇、Yandong Wen等在ECCV 2016上发表的 [A Discriminative Feature Learning Approach for Deep Face Recognition](https://link.zhihu.com/?target=http%3A//ydwen.github.io/papers/WenECCV16.pdf)。
**判别性**

- 深度学习的特征需要具有discriminative(判别性)和泛化能力，以便在没有标签预测的情况下识别新的未见类别，如一个人脸即便没有训练过也能判断类别。判别性同时表征了紧凑的类内差异和可分离的类间差异。
- 判别性特征可以通过最近邻（NN）或k近邻（k-NN）算法进行良好分类，其不一定取决于标签预测。
- 而softmax损失仅鼓励特征的可分离性，所得到的特征对于人脸识别不是足够有效的。
- 对比损失和三元组损失分别构成图像对和三元组的损失函数，然而与原样本相比，训练对或三元组的数量急剧增加，导致了网络收敛缓慢。

**中心损失的定义**

- 中心损失：为每一个类别提供一个类别中心，最小化min-batch中每个样本与该类别中心的距离，即缩小类内距离。
- 有效地表征了深度特征的类内距离，提升深度特征的判别能力，在保持不同类别的特征可分离的同时最小化类内距离是关键。公式如下，c_yi就是第yi个类别的特征中心，xi表示全连接层之前的特征，m表示mini-batch的大小

#### 	ArcFace loss

- 性能高，易于编程实现，复杂性低，训练效率高

- ArcFace直接优化geodesic distance margin(弧度)，因为归一化超球体中的角和弧度的对应。

- 为了性能的稳定，ArcFace不需要与其他loss函数实现联合监督，可以很容易地收敛于任何训练数据集。

- 缺点：W模型很大

  

### GAN 

* metric

### seq2seq

*Ilya Sutskever, Oriol Vinyals, Quoc V. Le, 2014, "Sequence to Sequence Learning with Neural Networks," pp. 3104–311 in NIPS 2014*

Take AlexNet for example, by eliminating softmax, we'll be able to extract a 4096 dimension embedding.

Now, feed the vector into RNN, as what language translation does, it'll generate a output sequence, the CAPTION for the image.

* ##### ImageTOseq

  Image Caption, mean

  *Deep Captioning with Multimodal Recurrent Neural Networks (m-RNN) -- ICLR2015, San Diego*
  *by Junua Mao*

  Meanwhile, Oriol Vinyals, (Andrej, Fei-Fei Li) also acquired the similar conclusion.

After obtaining this vector, decoder part of the network starts its processing with this fixed vector representation and at **each time step of the decoder network it produces outputs**. **Operation stops when a special token** showing the end of the sentence is produced. Distributed representations of the words are used as inputs to the encoder network. At the output side at each time step, a Word is chosen from a specific vocabulary list. At the decoder side, after decoder part a classifier network is used to produce a Word from the output at each time step. **LSTM networks are used in this paper due to their capability of capturing long term relationships**. Paper also shows experiments on machine translation task, which is from English to French. Simulation results reveal that presented approach outperforms existing studies.



### Attention

The Encoder + Decoder mechanism based on RNN (LSTM or GRU). 

For Image caption, it explains different region afftectin the output text series BY

weighing differently in X and therefore extracts important info for model making more precies judgement.

https://zhuanlan.zhihu.com/p/31547842



### Saliency Detection

The region within the image where user most care about.

![image-20200119174713586](/Users/joe/Library/Application Support/typora-user-images/image-20200119174713586.png)





