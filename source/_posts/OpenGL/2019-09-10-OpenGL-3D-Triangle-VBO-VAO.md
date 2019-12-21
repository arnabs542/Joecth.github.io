---
layout: "post"
category: "OpenGL"
date: 2019-09-10
---
### 3D 2D

All 3D space concepts in OpenGL.

3D coordinates (camera) --> 2D plane --> colored pixels.

***2D坐标和像素也是不同的，2D坐标精确表示一个点在2D空间中的位置，而2D像素是这个点的近似值，2D像素受到你的屏幕/窗口分辨率的限制。***

### Shader 

-- program that GPU runs

有些着色器允许开发者自己配置，这就允许我们用自己写的着色器来替换默认的。这样我们就可以更细致地控制图形渲染管线中的特定部分了，而且因为它们运行在GPU上，所以它们可以给我们节约宝贵的CPU时间。OpenGL着色器是用OpenGL着色器语言(OpenGL Shading Language, GLSL)写成的，在下一节中我们再花更多时间研究它。

![image-20190917220604821](https://tva1.sinaimg.cn/large/006y8mN6ly1g72v7ypj0gj30uk0ian1n.jpg)

CPU --> GPU

必用的 ：Vertex Shader, Fragment Shader

#### Geometry Shader

可以偷補插點

#### Vertex

我们以数组的形式传递3个3D坐标作为图形渲染管线的输入，用来表示一个三角形，这个数组叫做顶点数据(Vertex Data)；顶点数据是一系列顶点的集合。一个顶点(Vertex)是一个3D坐标的数据的集合。而顶点数据是用顶点属性(Vertex Attribute)表示的，它可以包含任何我们想用的数据，但是简单起见，我们还是假定每个顶点只由一个3D位置和一些颜色值、UV组成。

***为了让OpenGL知道我们的坐标和颜色值构成的到底是什么，OpenGL需要你去指定这些数据所表示的渲染类型。我们是希望把这些数据渲染成一系列的点？一系列的三角形？还是仅仅是一个长长的线？做出的这些提示叫做图元(Primitive)，任何一个绘制指令的调用都将把图元传递给OpenGL。这是其中的几个：GL_POINTS、GL_TRIANGLES、GL_LINE_STRIP。***

### ---------

VertexShader -> Rasterization -> FragmentShader

### Normalized Device Coordinates (NDC)

![image-20190919100557092](https://tva1.sinaimg.cn/large/006y8mN6ly1g74lnj2v91j30wq0i0dv3.jpg)

### Vertex Data

![image-20190919102118610](https://tva1.sinaimg.cn/large/006y8mN6ly1g74m3bcwprj30uq0f4gss.jpg)

f: means 法向量

![image-20190919102416139](https://tva1.sinaimg.cn/large/006y8mN6ly1g74m6drrucj31b30u0wyu.jpg)   (in Blender)

![image-20190919102343448](https://tva1.sinaimg.cn/large/006y8mN6ly1g74m5tdw1hj30xi0j2jzt.jpg)

![image-20190919102545255](https://tva1.sinaimg.cn/large/006y8mN6ly1g74m7xnz39j31c40q4dp7.jpg)

三角化

![image-20190919102640344](https://tva1.sinaimg.cn/large/006y8mN6ly1g74m927ogwj30kk0diwfb.jpg)



### VBO & VAO

![image-20190919153900923](https://tva1.sinaimg.cn/large/006y8mN6ly1g74v9xvqztj30x60hedpb.jpg)

### UV

![image-20190919154317764](https://tva1.sinaimg.cn/large/006y8mN6ly1g74vebr40mj30h80c2447.jpg)

### -----------

### EBO

![image-20190919155433545](https://tva1.sinaimg.cn/large/006y8mN6ly1g74vtx1bshj30w60i4mzf.jpg)

### VAO

一個物件一個VAO

```c++
unsigned int VAO;
glGenVertexArrays(1, &VAO);

--------P.S.--------------------
unsigned int VAO[10]; //  一次可造多個 array
glGenVertexArrays(10, VAO);
--------P.S.--------------------
  
glBindVertexArray(VAO);

unsigned int VBO;
glBindBuffer(GL_ARRAY_BUFFER, VBO);
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);


```

![image-20190919162325003](https://tva1.sinaimg.cn/large/006y8mN6ly1g74wk2zb4dj30i304j41v.jpg)