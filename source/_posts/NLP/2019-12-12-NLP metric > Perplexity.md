---
layout: post
categories: NLP, AI
date: 2019-12-12
tag: [] 




---



from : [https://blog.csdn.net/index20001/article/details/78884646](https://blog.csdn.net/index20001/article/details/78884646)

# 语言模型评价指标Perplexity

原创[Joy_Shen](https://me.csdn.net/index20001) 发布于2017-12-24 13:33:02 阅读数 26576 收藏

展开

语言模型（Language Model，LM），给出一句话的前k个词，希望它可以预测第k+1个词是什么，即给出一个第k+1个词可能出现的概率的分布p(xk+1|x1,x2,...,xk)。

在报告里听到用PPL衡量语言模型收敛情况，于是从公式角度来理解一下该指标的意义。

## Perplexity定义

PPL是用在自然语言处理领域（NLP）中，衡量语言模型好坏的指标。它主要是根据每个词来估计一句话出现的概率，并用句子长度作normalize，公式为

![img](https://img-blog.csdn.net/20171224134258243)

S代表sentence，N是句子长度，p(wi)是第i个词的概率。第一个词就是 p(w1|w0)，而w0是START，表示句子的起始，是个占位符。

这个式子可以这样理解，PPL越小，p(wi)则越大，一句我们期望的sentence出现的概率就越高。

还有人说，Perplexity可以认为是average branch factor（平均分支系数），即预测下一个词时可以有多少种选择。别人在作报告时说模型的PPL下降到90，可以直观地理解为，在模型生成一句话时下一个词有90个合理选择，可选词数越少，我们大致认为模型越准确。这样也能解释，为什么PPL越小，模型越好。