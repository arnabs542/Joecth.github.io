---
layout: post
categories: Graphic
date: 2019-11-06
tag: [Deep-Learning ] 



---



## EGNet Evaluation

![img](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ol6oj5msj307h0b4wfe.jpg)

### **1. GPU 运行时间测试**

| Times                | 1      | 2      | 3      | 4      | 5      | 6      | 7      | 8      | 9      | 10     |
| -------------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| preprocess time / s  | 0.0016 | 0.0016 | 0.0023 | 0.0019 | 0.0016 | 0.0023 | 0.0027 | 0.0028 | 0.0024 | 0.0022 |
| model time / s       | 0.1007 | 0.1011 | 0.0982 | 0.1076 | 0.0945 | 0.0970 | 0.0997 | 0.0948 | 0.1021 | 0.1015 |
| postprocess time / s | 0.0017 | 0.0020 | 0.0021 | 0.0022 | 0.0019 | 0.0019 | 0.0027 | 0.0018 | 0.0021 | 0.0022 |

**preprocessing average time: 0.00214**

**model average time: 0.09972**

**postprocessing average time: 0.00206**



### **2. CPU Time

| Times                | 1      | 2      | 3      | 4      | 5      | 6      | 7      | 8      | 9      | 10     |
| -------------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| preprocess time / s  | 0.0027 | 0.0029 | 0.0017 | 0.0022 | 0.0016 | 0.0017 | 0.0028 | 0.0024 | 0.0031 | 0.0016 |
| model time / s       | 8.9851 | 9.6686 | 8.6931 | 9.7251 | 8.9071 | 8.9628 | 8.9946 | 8.9697 | 8.9452 | 9.0649 |
| postprocess time / s | 0.0017 | 0.0017 | 0.0023 | 0.0017 | 0.0017 | 0.0018 | 0.0017 | 0.0017 | 0.0018 | 0.0016 |

**preprocessing average time: 0.00227**

**model average time: 9.09162**

**postprocessing average time: 0.00177**



3. Results

![img](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ol8on2b6j307h0b4ab1.jpg)

![img](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ol8t9igaj307h0b4wed.jpg)