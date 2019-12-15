---
layout: post
categories: NLP, AI
tag: [] 




---





### LSTM Brief.

LSTM是SimpleRNN的变体，它解决了梯度消失的问题。怎么解决的那？

LSTM增加了一个可以相隔多个timesteps来传递信息的方法。想想有一个传送带在你处理sequences时一起运转。每个时间节点的信息都可以放到传送带上，或者从传送带上拿下来，当然你也可以更新传送带上的信息。这样就保存了很久之前的信息，防止了信息的丢失。我们把SimpleRNN中的矩阵记为`Wo Uo bo`，LSTM的结构图如下：

![img](https://pic4.zhimg.com/80/v2-31da92629c2ddbb0a3971d18f1592b03_hd.jpg)



我们在SimpleRNN基础上，增加一条传送带（adding a carry track）用来传递信息。传送带上每个时刻的状态我们记为：`c t` c是carry的意思。

显然，当前时刻的输出就应该收到三个信息的影响





------

### Hamming Distance

在[資訊理論](https://zh.wikipedia.org/wiki/信息论)中，兩個等長[字符串](https://zh.wikipedia.org/wiki/字符串)之間的**漢明距離**（英語：Hamming distance）是兩個字符串對應位置的不同字符的個數。換句話說，它就是將一個字符串變換成另外一個字符串所需要*替換*的字符個數。

**[漢明重量](https://zh.wikipedia.org/wiki/汉明重量)**是字符串相對於同樣長度的零字符串的漢明距離，也就是說，它是字符串中非零的元素個數：對於[二進位](https://zh.wikipedia.org/wiki/二进制)[字符串](https://zh.wikipedia.org/wiki/字符串)來說，就是1的個數，所以11101的漢明重量是4。



例如：

- **1011101**與**1001001**之間的漢明距離是2。
- **2143896**與**2233796**之間的漢明距離是3。
- "**toned**"與"**roses**"之間的漢明距離是3。

------



### Hamming Loss

Hamming Loss 是用来计算多标签分类(Multi-label classification)模型精度的。

HammingLoss=1N∑i=1NXOR(Yi,j,Pi,j)LHammingLoss=1N∑i=1NXOR(Yi,j,Pi,j)L

NN是样本的数量，LL是标签的个数，Yi,jYi,j是第ii个预测结果中第jj个分量的真实值，Pi,jPi,j是第ii个预测结果中第jj个分量的预测值，XORXOR是抑或，XOR(0,1)=XOR(1,0)=1XOR(0,1)=XOR(1,0)=1，XOR(0,0)=XOR(1,1)=0XOR(0,0)=XOR(1,1)=0。

例子：三个样本

Y1=(0,1,1,1,0),P1=(1,1,1,0,0)Y1=(0,1,1,1,0),P1=(1,1,1,0,0)

Y2=(1,0,0,1,1),P2=(1,0,0,0,1)Y2=(1,0,0,1,1),P2=(1,0,0,0,1)

Y3=(1,1,0,0,0),P3=(1,0,1,0,1)Y3=(1,1,0,0,0),P3=(1,0,1,0,1)
$$
HammingLoss=\frac{1}{3}×\frac{2+1+3}{5}=0.4
$$
