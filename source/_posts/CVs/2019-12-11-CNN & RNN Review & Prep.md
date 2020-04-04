---
layout: post
categories: AI
tag: [] 



---



> Two stages: RPN for localization, then classification & bbox regression on proposals
>
> Single shot: classification + bbox regression at one time

### RCNN

- ~2000 forward passes for each image

- Train 3 models seperately

  <img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdd7ffqcltj30pi0ku17e.jpg" alt="image-20200331164611434" style="zoom:50%;" />

- Selective search(texture, adjecent color, and intensity) to clustering pixeles as RPN function, and then feed into AlexNet to extract embeddings. 
- SVM to classify each bbox into categoies.
- linear regression on bbox for tighter bbox.

### SPP Net

1.結合空間金字塔方法實現CNNs的多尺度輸入。
SPP Net的第一個貢獻就是在最後一個卷積層後，接入了金字塔池化層，保證傳到下一層全連線層的輸入固定。
換句話說，在普通的CNN機構中，輸入影象的尺寸往往是固定的（比如224*224畫素），輸出則是一個固定維數的向量。SPP Net在普通的CNN結構中加入了ROI池化層（ROI Pooling），使得網路的輸入影象可以是任意尺寸的，輸出則不變，同樣是一個固定維數的向量。

簡言之，CNN原本只能固定輸入、固定輸出，CNN加上SSP之後，便能任意輸入、固定輸出。神奇吧？

ROI池化層一般跟在卷積層後面，此時網路的輸入可以是任意尺度的，在SPP layer中每一個pooling的filter會根據輸入調整大小，而SPP的輸出則是固定維數的向量，然後給到全連線FC層。
![img](https://tva1.sinaimg.cn/large/00831rSTgy1gdd8d9rgnxj30al0750sy.jpg)
2.只對原圖提取一次卷積特徵
在R-CNN中，每個候選框先resize到統一大小，然後分別作為CNN的輸入，這樣是很低效的。
而SPP Net根據這個缺點做了優化：只對原圖進行一次卷積計算，便得到整張圖的卷積特徵feature map，然後找到每個候選框在feature map上的對映patch，將此patch作為每個候選框的卷積特徵輸入到SPP layer和之後的層，完成特徵提取工作。

如此這般，R-CNN要對每個區域計算卷積，而SPPNet只需要計算一次卷積，從而節省了大量的計算時間，比R-CNN有一百倍左右的提速。

### Fast

- ROI pool to share process

- Search selective algorithm is computed base on the output feature map of the previous step. Then, ROI pooling layer is used to ensure the standard and pre-defined output size.

- These valid outputs are passed to a fully connected layer as inputs. Finally, two output vectors are used to predict the observed object with a softmax classifier and adapt bounding box localisations with a linear regressor.

  ![img](https://tva1.sinaimg.cn/large/00831rSTgy1gddbgk1y3dj30in097my5.jpg)



### Faster RCNN

![image-20200331165148305](https://tva1.sinaimg.cn/large/00831rSTgy1gdd7vl10thj30om0l8q4a.jpg)

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

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdddgum6x0j31jk0esacq.jpg" alt="img" style="zoom:67%;" />

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



### Why ReLU Better than Sigmoid?

- 一方面，ReLU比sigmoid效果好的分析都是基于深度神经网络的前提，比如网络足够深时sigmoid会有明显的梯度消失问题，如果是浅层神经网络的话这些问题并不存在。另一方面，它们的用处不同，sigmoid输出范围是01之间，可以当作概率。深度神经网络中sigmoid可以用作门控单元（比如LSTM的三种门都是sigmoid）或attention（比如SENet中excitation部分），这些ReLU并不能取代。

- 说白了还是具体问题具体分析。如果神经网络是进行二分类，你用relu做输出层激励函数，你的输出是不是很难控制？如果你的神经网络层数很深，你用sigmoid，反向传播过程是不是会有梯度消失？现在sigmoid更多的情况下，在小型神经网络和二分类型的输出层中出现的比较多，relu效果好不代表在任何应用条件下都好

- 隐含层就放心用Relu吧,
  -  relu的好处是可以解决梯度消失问题
  - sigmoid的好处是可以把输入缩放到0--1之前，并且连续没有绝对的好与坏，具体情况具体分析
- sigmoid和tanh的gradient在饱和区域非常平缓，接近于0，很容易造成vanishing gradient的问题，减缓收敛速度。vanishing gradient在网络层数多的时候尤其明显，是加深网络结构的主要障碍之一。
- Relu的另一个优势是在生物上的合理性, with 0s so sparse network，它是单边的，相比sigmoid和tanh，更符合生物神经元的特征。

- Relu的另一个优势是在生物上的合理性，它是单边的，相比sigmoid和tanh，更符合生物神经元的特征。

### Why Non-linear

- or you can just use LR... same meaning.



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

  VGG as e.g.

  | Layer     |                                                              |      |
  | --------- | ------------------------------------------------------------ | ---- |
  | 1-1       | 1 + 1x2^1                                                    | 3    |
  | 1-2       | 1 + 2x2^1                                                    | 5    |
  | Pooling 1 | 1 + 2x2^1 + **2^0**                                          | 6    |
  | 2-1       | 1 + 2x2^1 + **2^0** + 1x2^2                                  | 10   |
  | 2-2       | 1 + 2x2^1 + **2^0** + 2x2^2                                  | 14   |
  | Pooling 2 | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1**                        | 16   |
  | 3-1       | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 1x2^3                | 24   |
  | 3-2       | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 2x2^3                | 32   |
  | 3-3       | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 3x2^3                | 40   |
  | Pooling 3 | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 3x2^3 + **2^2**      | 44   |
  | 4-1       | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 3x2^3 + **2^2** + 1x2^4 | 60   |
  | 4-2       | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 3x2^3 + **2^2** + 2x2^4 | 76   |
  | 4-3       | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 3x2^3 + **2^2 **+ 3x2^4 | 92   |
  | Pooling 4 | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 3x2^3 + **2^2** + 3x2^4 + **2^3** | 100  |
  | 5-1       | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 3x2^3 + **2^2** + 3x2^4 + **2^3** + 1x2^5 | 132  |
  | 5-2       | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 3x2^3 + **2^2** + 3x2^4 + **2^3** + 2x2^5 | 164  |
  | 5-3       | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 3x2^3 + **2^2** + 3x2^4 + **2^3** + 3x2^5 | 196  |
  | Pooling 5 | 1 + 2x2^1 + **2^0** + 2x2^2 + **2^1** + 3x2^3 + **2^2** + 3x2^4 + **2^3** + 3x2^5 + **2^4** | 212  |

  ​	

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



### SVM

- hinge loss

- 分类间隔为1/||w||，||w||代表向量的模

- 当参数C越小时，分类间隔越大，分类错误越多，趋于欠学习

  考虑软间隔的时候，C对优化问题的影响就在于把a的范围从[0，+inf]限制到了[0,C]。C越小，那么a就会越小，目标函数拉格朗日函数导数为0可以求出w=求和ai∗yi∗xi，a变小使得w变小，因此间隔2/||w||变大

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



### Naive Bayes

- 特征变量X的各个维度是类别条件独立随机变量





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



### Reason of LR as Linear

有人說，因為邏輯迴歸不是線性的，這個說法是不對的！因為我們可以把邏輯回歸的模型轉成線性的形式如下：

 

![螢幕快照 2017-12-22 上午12.41.33](https://tva1.sinaimg.cn/large/00831rSTgy1gcx9msq25oj311a0b6411.jpg)

 

主要原因很簡單，因為迴歸分析中 ![Y](https://tva1.sinaimg.cn/large/00831rSTgy1gcx9mt6yxrj300o00n08d.jpg) 是已經觀察到的資料，可是邏輯迴歸中 ![P(https://tva1.sinaimg.cn/large/00831rSTgy1gcx9mo7366j301q00y0fi.jpg)](https://s0.wp.com/latex.php?zoom=2&latex=P%28Y%3D1%7CX%29&bg=ffffff&fg=000&s=0) 是資料裡面無法觀察到的，所以我們就沒辦法用傳統的最小平方法估計，而要採用最大概似法 (Maximum Likelihood Estimation)。至於最大概似法的原理是什麼，可以用下面這張圖很清楚的解釋。

 

### 关于logit 回归和SVM 不正确的是（A） 机器学习 ML模型 中

A. Logit回归本质上是一种根据样本对权值进行极大似然估计的方法，而后验概率正比于先验概率和似然函数的乘积。logit仅仅是最大化似然函数，并没有最大化后验概率，更谈不上最小化后验概率。**A错误**
B. Logit回归的输出就是样本属于正类别的几率，可以计算出概率，正确
C. SVM的目标是找到使得训练数据尽可能分开且分类间隔最大的超平面，应该属于结构风险最小化。
D. SVM可以通过正则化系数控制模型的复杂度，避免过拟合。
@BlackEyes_SGC：**Logit回归目标函数是最小化后验概率，Logit回归可以用于预测事件发生概率的大小，**SVM目标是结构风险最小化，SVM可以有效避免模型过拟合。



![螢幕快照 2017-12-22 上午12.44.31](https://tva1.sinaimg.cn/large/00831rSTgy1gcx9mu07mkj314s0u0tjz.jpg)



### 为什么xgboost要用泰勒展开，优势在哪里？机器学习 ML模型 难

@AntZ：xgboost使用了一阶和二阶偏导, 二阶导数有利于梯度下降的更快更准. 使用泰勒展开取得函数做自变量的二阶导数形式, 可以在不选定损失函数具体形式的情况下, 仅仅依靠输入数据的值就可以进行叶子分裂优化计算, 本质上也就把损失函数的选取和模型算法优化/参数选择分开了. 这种去耦合增加了xgboost的适用性, 使得它按需选取损失函数, 可以用于分类, 也可以用于回归。
————————————————
版权声明：本文为CSDN博主「v_JULY_v」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/v_JULY_v/article/details/78121924 



### L1和L2正则先验分别服从什么分布。机器学习 ML基础 易

- L1和L2正则先验分别服从什么分布，L1是拉普拉斯分布，L2是高斯分布。
- 先验就是优化的起跑线, 有先验的好处就是可以在较小的数据集中有良好的泛化性能，当然这是在先验分布是接近真实分布的情况下得到的了，从信息论的角度看，向系统加入了正确先验这个信息，肯定会提高系统的性能。
  对参数引入高斯正态先验分布相当于L2正则化, 这个大家都熟悉：



### How to choose K for K-Means Clustering

- sqrt(n/2) -- bad
- elbow method - Y-axis means sum(square errors)

https://rpubs.com/skydome20/R-Note9-Clustering

https://www.biaodianfu.com/k-means-choose-k.html



### How to choose K for kNN

- CV error might rise after a specific lowest value of K

如果选择较小的K值，就相当于用较小的领域中的训练实例进行预测，“学习”近似误差会减小，只有与输入实例较近或相似的训练实例才会对预测结果起作用，与此同时带来的问题是“学习”的估计误差会增大，换句话说，K值的减小就意味着整体模型变得复杂，容易发生过拟合；
如果选择较大的K值，就相当于用较大领域中的训练实例进行预测，其优点是可以减少学习的估计误差，但缺点是学习的近似误差会增大。这时候，与输入实例较远（不相似的）训练实例也会对预测器作用，使预测发生错误，且K值的增大就意味着整体的模型变得简单。
K=N，则完全不足取，因为此时无论输入实例是什么，都只是简单的预测它属于在训练实例中最多的累，模型过于简单，忽略了训练实例中大量有用信息。
    在实际应用中，K值一般取一个比较小的数值，例如采用交叉验证法（简单来说，就是一部分样本做训练集，一部分做测试集）来选择最优的K值。

```python
K = 10
batch_size = 16
epochs = 100
error_histories = []
num_val_samples = len(train_data) // K

for i in range(K):
    print('Processing fold #', i)
    val_data = train_data[i*num_val_samples : (i+1)*num_val_samples]
    val_targets = train_targets[i*num_val_samples : (i+1)*num_val_samples]
    
    partial_train_data = np.concatenate( 
                         [train_data[: i*num_val_samples],
                         train_data[(i+1)*num_val_samples :]],
                         axis = 0)
    partial_train_targets = np.concatenate(
                         [train_targets[: i*num_val_samples],
                         train_targets[(i+1)*num_val_samples :]],
                         axis = 0)
    model = build_model()
    history = model.fit(partial_train_data,
                        partial_train_targets,
                        validation_data = (val_data, val_targets),
                        epochs = epochs,
                        batch_size = batch_size,
                        verbose = 1)
    mae_history = history.history['val_mean_absolute_error']
    error_histories.append(mae_history)
    average_error = [ np.mean([x[i] for x in error_histories]) for i in range(epochs)]

fr: 
  https://jason-chen-1992.weebly.com/home/-cross-validation
```



### DBSCAN

Density-based spatial clustering of applications with noise



### 防止过拟合, 

　　过拟合的原因是算法的学习能力过强；一些假设条件（如样本独立同分布）可能是不成立的；训练样本过少不能对整个空间进行分布估计。 
　　处理方法：

早停止：如在训练中多次迭代后发现模型性能没有显著提高就停止训练
数据集扩增：原有数据增加、原有数据加随机噪声、重采样
正则化
交叉验证
特征选择/特征降维
创建一个验证集是最基本的防止过拟合的方法。我们最终训练得到的模型目标是要在验证集上面有好的表现，而不训练集。
正则化可以限制模型的复杂度。

在训练中，我们希望在中间箭头的位置停止训练。而Early stopping就可以实现该功能，这时获得的模型泛化能力较强，还可以得到一个中等大小的w的弗罗贝尼乌斯范数。其与L2正则化相似，选择参数w范数较小的神经网络。

可以用L2正则化代替early stopping。因为只要训练的时间足够长，多试几个lambda。总可以得到比较好的结果。



### Early stopping:

优点：只运行一次梯度下降，我们就可以找出w的较小值，中间值和较大值。而无需尝试L2正则化超级参数lambda的很多值。

缺点：不能独立地处理以上两个问题，使得要考虑的东西变得复杂。举例如下：



一般机器学习的步骤分为以上两步，第一步我们确定一个成本函数J，然后可以用梯度下降等方法去优化它；第二步我们不希望模型发生过拟合，就有正则化等方式去操作，这是一个动态的过程。但是如果采用early stopping，这就相当于用一种方式来控制两个问题的结束，这会使得问题变得复杂。如图一所示，在中间位置时，模型已经停止训练了，而成本函数还没有下降到合适的区域。



### AUC

二階混淆矩陣

有了混淆矩陣，就可以定義**ROC**曲線了。**ROC**曲線將假陽性率（FPR）定義為 X 軸，真陽性率（TPR）定義為 Y 軸。其中：

- TPR：在所有實際為陽性的樣本中，被正確地判斷為陽性的樣本比率。
- FPR：在所有實際為陰性的樣本中，被錯誤地判斷為陽性的樣本比率。
- TPR = TP / (TP + FN)
- FPR = FP / (FP + TN)
- <img src="https://tva1.sinaimg.cn/large/00831rSTgy1gcydclzpf2j30hs0csdgb.jpg" alt="img" style="zoom:50%;" />

### ML Flow

Abstract as math problem -> acquire data, pca ... -> feature selection -> train & optimize model -> analyze model -> deploy (time complexity, resource consumption, stability)



### Linear vs Non-linear classifiers

非线性分类器效果拟合能力较强，不足之处是数据量不足容易过拟合、计算复杂度高、可解释性不好。
常见的线性分类器有：LR,贝叶斯分类，单层感知机、线性回归
常见的非线性分类器：决策树、RF、GBDT、多层感知机
SVM两种都有（看线性核还是高斯核）



### 参数初始化

下面几种方式,随便选一个,结果基本都差不多。但是一定要做。否则可能会减慢收敛速度，影响收敛结果，甚至造成Nan等一系列问题。

下面的n_in为网络的输入大小，n_out为网络的输出大小，n为n_in或(n_in+n_out)*0.5

Xavier初始法论文：http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf

He初始化论文：https://arxiv.org/abs/1502.01852
————————————————
版权声明：本文为CSDN博主「v_JULY_v」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/v_JULY_v/article/details/78121924



### k-d tree



### Ave Pooling

但是average-pooling在全局平均池化操作中应用也比较广，在ResNet和Inception结构中最后一层都使用了平均池化。有的时候在模型接近分类器的末端使用全局平均池化还可以代替Flatten操作，使输入数据变成一位向量。



### Newton's method for Optimization

牛顿法的优缺点总结：

优点：二阶收敛，收敛速度快；

缺点：牛顿法是一种迭代算法，每一步都需要求解目标函数的Hessian矩阵的逆矩阵，计算比较复杂。

什么是拟牛顿法（Quasi-Newton Methods）？机器学习 ML基础 中

@wtq1993，http://blog.csdn.net/wtq1993/article/details/51607040
拟牛顿法是求解非线性优化问题最有效的方法之一，于20世纪50年代由美国Argonne国家实验室的物理学家W.C.Davidon所提出来。Davidon设计的这种算法在当时看来是非线性优化领域最具创造性的发明之一。不久R. Fletcher和M. J. D. Powell证实了这种新的算法远比其他方法快速和可靠，使得非线性优化这门学科在一夜之间突飞猛进。

拟牛顿法的本质思想是改善牛顿法每次需要求解复杂的Hessian矩阵的逆矩阵的缺陷，它使用正定矩阵来近似Hessian矩阵的逆，从而简化了运算的复杂度。拟牛顿法和最速下降法一样只要求每一步迭代时知道目标函数的梯度。通过测量梯度的变化，构造一个目标函数的模型使之足以产生超线性收敛性。这类方法大大优于最速下降法，尤其对于困难的问题。另外，因为拟牛顿法不需要二阶导数的信息，所以有时比牛顿法更为有效。如今，优化软件中包含了大量的拟牛顿算法用来解决无约束，约束，和大规模的优化问题。



### 共轭梯度法？

​    共轭梯度法是介于梯度下降法（最速下降法）与牛顿法之间的一个方法，它仅需利用一阶导数信息，但克服了梯度下降法收敛慢的缺点，又避免了牛顿法需要存储和计算Hessian矩阵并求逆的缺点，共轭梯度法不仅是解决大型线性方程组最有用的方法之一，也是解大型非线性最优化最有效的算法之一。在各种优化算法中，共轭梯度法是非常重要的一种。其优点是所需存储量小，具有逐步收敛性，稳定性高，而且不需要任何外来参数。



### 直觀理解正定、半正定矩陣　positive definite和positive semi-definite:

半正定与正定矩阵同意用半正定矩阵来事例：
首先半正定矩阵定义为: ![[公式]](https://www.zhihu.com/equation?tex=X^TMX+\geq+0)
其中X 是向量，M 是变换矩阵

我们换一个思路看这个问题，矩阵变换中，![[公式]](https://www.zhihu.com/equation?tex=MX)代表对向量 X进行变换，我们假设变换后的向量为Y，记做![[公式]](https://www.zhihu.com/equation?tex=Y%3DMX)。于是半正定矩阵可以写成：
![[公式]](https://www.zhihu.com/equation?tex=X^TY+\geq+0)

这个是不是很熟悉呢？ 他是两个向量的内积。 同时我们也有公式：

![[公式]](https://www.zhihu.com/equation?tex=cos(\theta)+%3D+\frac{X^TY}{||X||*+||Y||})

||X||, ||Y||代表向量 X,Y的长度，![[公式]](https://www.zhihu.com/equation?tex=\theta)是他们之间的夹角。 于是半正定矩阵意味着![[公式]](https://www.zhihu.com/equation?tex=cos(\theta)\geq+0), 这下明白了么？

正定、半正定矩阵的直觉代表一个向量经过它的变化后的向量与其本身的夹角小于等于90度。



### GAN



### Convolutinon 實現

img2col

note: https://zhuanlan.zhihu.com/p/63974249



### 随机森林如何处理缺失值？

方法一（na.roughfix）简单粗暴，对于训练集,同一个class下的数据，如果是分类变量缺失，用众数补上，如果是连续型变量缺失，用中位数补。
方法二（rfImpute）这个方法计算量大，至于比方法一好坏？不好判断。先用na.roughfix补上缺失值，然后构建森林并计算proximity matrix，再回头看缺失值，如果是分类变量，则用没有缺失的观测实例的proximity中的权重进行投票。如果是连续型变量，则用proximity矩阵进行加权平均的方法补缺失值。然后迭代4-6次，这个补缺失值的思想和KNN有些类似12。



### Why Smooth-L1 in Faster & SSD?



### RNN

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdc5yneca2j31400g6di2.jpg" alt="img" style="zoom:67%;" />

### ★ LSTM & GRU

Ref: https://kknews.cc/zh-tw/code/vegon84.html

https://mp.weixin.qq.com/s/aV9Rj-CnJZRXRm0rDOK6gg

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdc37qy1wmj30oo0bbwf7.jpg" alt="img" style="zoom:67%;" />

Ref: https://blog.floydhub.com/long-short-term-memory-from-zero-to-hero-with-pytorch/

神經元數跟參數個數

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gdc734yxpjj307u00kmwy.jpg" alt="img" style="zoom:67%;" />

隱向量長度應該是要比字典短不少，不過例子裡的字在字典裡長度是５，隱向量長度是10，所以　(5+10)x10 + 10 共四個 for３個gates	

Ref: https://www.cnblogs.com/wushaogui/p/9176617.html, https://blog.csdn.net/Hello_word5/article/details/88918075



![img](https://tva1.sinaimg.cn/large/00831rSTgy1gdc7csb4tuj30u01dn0x9.jpg)



### Word Representation to Word Embedding