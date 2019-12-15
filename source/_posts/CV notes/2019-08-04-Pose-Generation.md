---
layout: post
categories:  [Deep-Learning, AI]

---

(NOT MY NOTE, ref from colleaque's)
### Deformable GANs for Pose-based Human Image Generation.

https://github.com/AliaksandrSiarohin/pose-gan.  cvpr2018

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6hp3mtcvuj30rp0aq42d.jpg)





![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6hp4oxs5gj30gd0adwh2.jpg)



### Progressive Pose Attention for Person Image Generation

https://github.com/tengteng95/Pose-Transfer.  cvpr2019, 

![整体流程图](https://tva1.sinaimg.cn/large/006y8mN6ly1g6gthtcaz5j30o70b2wfd.jpg)

整体结构中含有多个Pose  Attentional Block，其作用是对输入的image pathway和pose pathway按照Pose Mask进行更新，图中Mt即为Pose Mask，它引导网络将图片中人物的不同的部分按照目标姿态进行像素块迁移。

将最后一个Block中Image Pathway的数据经过解码网络，即得到了最终的生成图像。

### Unsupervised Person Image Generation with Semantic Parsing Transformation

https://github.com/SijieSong/person_generation_spt. cvpr2019

只有测试代码，测试输入还需要semantic parsing

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6lf6q884ej311s0mb0vb.jpg)  



###Dense Intrinsic Appearance Flow for Human Pose Transfer

https://github.com/ly015/intrinsic_flow      cvpr2019

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6m4tdrihzj31dk0lsgrt.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6m4v9xer1j31bg0j40u9.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6m4vecqfjj30o407udg5.jpg)

###Disentangled Person Image Generation

https://github.com/charliememory/Disentangled-Person-Image-Generation cvpr2018

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6m4zyq9zhj31pa0n076v.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6m4xvk2woj31l00l8di5.jpg)

