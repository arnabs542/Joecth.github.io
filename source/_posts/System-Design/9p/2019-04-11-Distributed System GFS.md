---
layout: post
categories: SystemDesign
tag: []
date: 2019-04-11
---



# General

- GFS Client
- Heart Beat



> GFS 采用的是 Master-slave 的架构。他的一些基本设计原理，如 chunk 的设计（对应文件系统中的 block）和普通文件系统是相通的。整套系统的设计是基于一些合理假设的（这些假设都是Google从大量工程实践中总结出来的），其中一条假设就是：“We expect a few million files, each typically 100MB or larger in size"。如果实在需要存很多小文件的话， 其实可以将这些小文件打包成一个大文件然后再存储，只要记录下每个小文件在文件内部的起始字节和大小就行了。

### 

## 要解決的問題

- Storage不够、QPS太大的問題

- Google 很多小計算機建DFS

  ＶＳ

  SUN大型、貴的（大家買不起），09年被Oracle收了

- GFS、BigTable、MapReduce

# GFS

## Scenario

- 作為一個文件系統，一定要提供兩種常用的操作：寫跟讀
  - 寫：要文件名、內容
  - 讀：文件名，返回文件內容

### 需求1: 總存储量有多大?

- 比如 > 1000T，才會上分布式；機器數也是越大越好

### 需求2: 多台機器，越多越好



## Service

- 如圖書館要有Server、Client。

  GFS提供的一個就是讀取，另一個是寫入的服務

### Q: 多台Server間怎溝通？

#### 	P2P 

平級溝通

- 優：一台掛了還可以工作，沒有單點故障問題
- 缺：但，大家平級，要常通信保持一致性。
- p2p的通信一般是比較難寫的，直覺就是。



#### (V) Master vs Slaves

老大一致對外，對內分配幹活

- 優: 數據易**保持一致性**。就老大分配

- 缺：有單點大哥master掛了，整個系統不work的問題

- 這是GFS最終的選擇，他是後端的服務，不是前端的，所以掛個一分鐘不會怎樣，就如果master掛了，把master重啟就好了。

  

> ##### 单选题]大家猜猜GFS会用哪种设计模式？
>
> A.社会主义 P2P23.06% 选择
>
> B.资本主义 Master Slave76.94% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是A
>
> **正确答案:**B
>
> **解析:**
>
> Master Slave的优势是：
> 设计简单
> 数据很容易保持一致



## Storage

### Q: 大文件存在哪？

- 當然是disk，10PB只有disk可以，內存不可能啦

- 如何存到這個文件系統裡？
  - 怎麼設計GFS?
  - 怎麼存？如果總量 < 100G？

> ##### [单选题]在 GFS 中，大文件存在哪儿？
>
> A.内存中，读写快！5.03% 选择
>
> B.硬盘中，超大空间！94.97% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B



### Q: Metadata存哪？

- metadata元數據常常被無意識訪問到, 怎麼存好？一般打開文件夾就被動看到了

> ##### [单选题]Meta Data应该怎样储存？
>
> **A.所有文件的Meta Data 全放磁盘开头83.51% 选择**
>
> B.每个文件的Meta Data都和它的内容放在一起16.49% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A
>
> **正确答案:**A
>
> **解析:**
>
> 全放磁盘开头可以减少磁盘的寻轨时间

理由跟硬盤的結構有關，機械硬盤的磁頭到軌道有尋軌時間的，一般磁頭跳到要找的位置要10ms

如果是選B，磁頭就要一直跳，100個文件就要10ms*100就一秒了。

A可以一次全讀出去。



- 文件內容怎麼放呢？在磁盤中也有兩種方式：就是要不要把每個文件拆成各小塊交錯放呢？

> ##### [单选题]文件内容应怎样储存？
>
> A.文件整体存储，所有文件连在一起21.44% 选择
>
> B.将每个文件等分成很多小块后再存78.56% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 等分成很多小块后存储可以方便文件的修改操作

如果選A的話，當2號文件是10KB這麼大，寫入後變100KB了，怎麼寫？還得把2號先砍了，再往後找一個夠100KB大小的空間寫進去。

選B的話，文件本來就是一小塊一小塊了，**後面要增加90KB的文件就順勢往後寫就OK了**。



一個硬盤就是一個非常大的array；

一般NTFS(win)、XFS(linux)的文件系統裡的默認Block是　***4KB***

- 本來的100G如果變成了100TB會遇到什麼問題？

  - Block的數量會超多。要拿來儲存block的空間就已經非常大了！

    - 100x1024G = 100x 1024x1024M = 100x1024x1024x1024KB = 25x1024x1024x1024 **blocks**

  - 怎麼改進？ ==> 增加Block的大小。可能就是變成64MB，然後把這個改名叫**Chunk**

    - 優：Reduce size of Metadata，就是筆數變少了
    - 劣：浪費了些小空間，如果我要存的就是個小文章４MB，那也要拿64MB去存，60MB就變成了磁盤碎片浪費了。但就這樣吧。。

       結論：Z > B . 

> - 对于这个trade off，我感觉十分牵强啊。增加chunk size是为了减少meta data 的数量，但是试想，如果存的文件全是非常非常小，都是几百kb或者几mb的，那这样岂不是更浪费空间，造成大量碎片？
>   - 这个在GFS的paper里面有解释，***GFS的设计是基于一些假设的（这些假设都是Google从大量工程实践中总结出来的***），其中一条假设就是：“We expect a few million files, each typically 100MB or larger in size"。这是其一。另外，如果实在需要存很多小文件的话， 其实可以将这些小文件打包成一个大文件然后再存储，只要记录下每个小文件在文件内部的起始字节和大小就行了。
> - 如果在写新文件时发现之前预先留给metadata的空间被用完了怎么办呢？
>   - 这时候应该就写不进去了 生产环境应该及时关注磁盘容量告警



### Q: 100G on 普通的OS怎存?

![image-20200822205723260](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzvx48y5vj30vc0g6dhp.jpg)

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzvxy7io1j30c607edgd.jpg" alt="image-20200822205814035" style="zoom: 33%;" />



1. 因为比较小，預設就是4KB，一般就是照block傳就好了
2. 如果再大一點怎辦？如果再按block算，就會有很多很多個block，去尋執很麻煩，不然我們就by chunk
3. 如果100P就要上多台機子了，P = 1000T



當然指的不是一個，而是很多個文件啦

![image-20200822205929382](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzvz8ufr8j31160hwtb8.jpg)



### Q: 100P, 真的很大怎存？

上分布式



## Scale

![image-20200822210535805](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzw5mlv1rj317o0l441y.jpg)



### Q: 10PB存得下嗎？需要多台電腦 Master-Slave工作模式。

- 現在一台服務器現在最多插10個硬盤，一個硬盤撐死就100TB，這樣也就才0.1P，這樣如此的電腦至少要來100台共同工作才能做得了10PB的事

> ##### [单选题]在 GFS 中 Master 和 Slave 分别存什么数据？
>
> A.Master 存 Metadata，Slave 存实际的文件内容96.81% 选择
>
> B.Master 存实际的文件内容，Slave 存 Metadata3.19% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A

Master存了所有的chunk該在哪台小弟的info

***所以就是slave就是chunk server***

> [单选题]GFS Master 是否有必要存储每个 chunk 在 Slave Server 上的 Offset?
>
> 你的选择:B
>
> A:有必要
>
> B:没有必要
>
> 答对了，您选择的答案是B

這樣可減輕master壓力；而且slave裡面可以自己調整位置不用通跟master通信。



*１chunk = **64MB need 64B的metadata(經驗值)**, 10PB needs 10G metadata, 存內存都可以！*

> - 如果master 挂了 只能恢复master ？ 不能promote slave server 变成master？
>   - GFS 里的 Master 的概念和 MySQL 里的 MasterSlave 的概念不同。GFS 里的 Master 只负责管理，不负责数据存储。MySQL 里的 Master Slave 都只负责数据存储不负责管理。要注意区分。



### Q: 每台 chunk 的Offset偏移量可否不在Master上？

![image-20200822210804854](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzw87abomj31660k07ei.jpg)



### Q: Master 存10P文件的metadata要多少容量？

1 chunk = 64MB needs 64B. (经验值) 10P needs 10G





# One Workable Sol!

## 寫

### 架構 & Q: 一個chunk怎麼寫入server的?

這個還沒有做scale

![image-20200822211653883](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzwhdnk3dj312y0is11s.jpg)

#### Q: 寫入怎麼寫好？一次vs多次

> ##### [单选题]怎么将文件写入GFS?
>
> A.将文件整体一次性写入3.39% 选择
>
> B.将文件拆分成块多次写入96.61% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 不同的块有可能放到不同的Chunk Server，并且分块后方便重传



#### Q: 從哪續傳好? 當多次寫時每份大小？就Chunk，也是傳輸size

如果斷開了，可以從哪斷開的從哪續傳

> ##### [单选题]GFS Client 将文件拆分为多大进行传输比较合适？
>
> A.64k6.92% 选择
>
> B.1M5.73% 选择
>
> **C.64M83.89% 选择**
>
> D.1G3.46% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是C
>
> **正确答案:**C
>
> **解析:**
>
> 64M 是一个 chunk 的大小。GFS 是按照 chunk 为单位进行存储的，所以 64M 为一组比较合适。

傳輸單位也就是chunk。



> ##### [单选题]GFS中每一个Chunk怎么写入Server？
>
> A.把文件传给master，让Master处理所有的事情6.81% 选择
>
> B.仅让Master分配Chunk Server，然后直接把Chunk传给相应的Chunk Server93.19% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> ***避免Master成为瓶颈***

master的硬盤有限，網路也是有限的，自己會卡死，分下去給小弟們，讓client間也不會排隊



#### Q: 要修改一個 .mp4 怎辦？

1. 先刪掉 /gfs/home/xxx.mp4
2. 重把整個文件寫一份

##### 結論就: 別update!



### 總結: 

***Master要存所有的metadata,  chunkserver存真正的大data 讀要找到對應的chunkserver，寫時要找到空閒的chunkserver；***

- **寫入是每次找老大問，老大分配空間，自己去找小弟寫**
- **讀出是問老大拿到chunklist，然後去問小弟拿到chunk就ok**

> - 請問gfs讀取file的話, client會從master得到一個chunk list, 那我並行讀取每個chunk,還是一個一個循序讀取chunk? 有什麼比較快的讀取方法嗎?
>   - GFS中，Chunk分散储存在若干个Chunk Server中，读取的时候Client可以从不同的Chunk Server同时读取Chunk，相当于有一个并行的效果
> - The client is the end user side, or another proxy? I don't think the end user client should worry about which chunk server to write in.
>   - The "client" mentioned here is a library that is linked to the end user's application, serving as an ***abstraction layer between the application and the underlying GFS***.
> - client读取档案时，master server是给他一个chunk list，那client写入档案时，master是给他一个chunk list让他依次写入，还是一个写完master再告知下一个chunk该分配到那个chunk server?
>   - 给一个 chunk list 让他依次写入。否则 master 和 client 之间通信太多很负累，也没啥意义。
> - client 定义是什么 ？是end user吗？ 还是只是gfs 跟外界的一个interface？
>   - gfs 和外界的一个 interface。



## 讀

#### Q: 一次 or 多次？

#### Q: Client 怎知 xxx.mp4 被切成了多少塊？

每個chunk知道在哪個server，所以一個file知道分別位在哪些server

### 架構

![image-20200822212139023](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzwmbpejsj314w0k6424.jpg)

## SCALE --  in One Workable Sol

### Master 做的事

#### Q: Master Task:

- 存儲各個文件數據的 metadata
- 存儲 Map
  - 讀取時找到對應的 Chunk Server, 
  - 寫入時分配空閒三 Chunk Server

#### Q: 單master夠嗎？

- 90%很好了一般都是這樣；大不了就是 Paxos Alg. 的多Master，再多也受不了會有延遲

##### Double Master

- Paper: Apache Hadoop Goes Realtime at Facebook

##### Multi Master

- Paper: Paxos Algorithm



#### Q: 怎麼看資料有掛了

- CHECKSUM, md5  哈希，原串發生變化，哈希值就巨大變化，一旦不同，就是原數據必毀

  <img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gdtqklpedij31260tun45.jpg" alt="image-20200414235740148" style="zoom: 25%;" />

  

- 也可以用 XOR作checksum, 

- 也可以用SHA1, SHA256, SHA512

- Read More: https://en.wikipedia.org/wiki/Checksum

##### Checksum 

- size: 也就 4Bytes
- 時機

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200822213411583.png" alt="image-20200822213411583" style="zoom: 50%;" />

> ##### [单选题]什么时候写入 checksum? 如上圖
>
> A.每个一段时间遍历所有数据计算 checksum 并写入3.32% 选择
>
> B.每个 chunk 在写入的时候计算 checksum 并记录在 chunk 的末尾39.40% 选择
>
> C.每个 chunk 在写入的时候计算 checksum 并集中记录在当前的 Slave 上36.58% 选择
>
> D.每个 chunk 在写入的时候计算 checksum 并集中记录在 Master 上20.70% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B



> ##### [单选题]一般来说什么时候检查 checksum？
>
> A.每次读取 chunk 的时候重新计算并对比以前的 checksum90.56% 选择
>
> B.周期性的遍历所有数据检查 checksum9.44% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是A
>
> **正确答案:**A

而且還可以再週期性地檢查；是根據業務調整。



#### 問題集

> - master down了重启， 是通过读log来恢复吗
>   - 是的，但是一般会定期制作一个checkpoint，挂掉之后只需要从上一个checkpoint开始重放log就行了，不需要每次都从头开始。
> - master down了之后怎么恢复？
>   - master down了之后重启就好
> - 老师请问还有其他的加密算法么？还是只能用这个MD5
>   - 有啊，网上搜一大堆。比如 sha1 sha2, sha256.
> - Check Sum 检查一位错误的例子，如果刚好有两个数据发生改变，是有可能导致xor结果不变的吧。这种情况我们就不知道有文件损坏了？
>   - 是的。check sum 本来就是 false positive 的。你说的这种情况出现概率是很低的。系统设计的领域里面有很多允许 false postive 或者 false negative 的情况，如 BloomFilter 就是一个例子。这些场景下，我们都不能保证 100% work，但是高概率是有效的。这个系统设计区别于算法设计的很大的不同，要注意体会这个地方。





## 更多 Q&A

#### How to avoid data loss when a Chunk Server is down/fail? 

​	Ans: replica 作備份

> ​	[单选题]GFS的Replica怎么存放？
>
> 1.三个备份都放在一个地方（加州）0.97% 选择
>
> 2.三个备份放在三个相隔较远的地方（加州，滨州，纽约州）9.99% 选择
>
> 3.两个备份相对比较近，另一个放在较远的地方（2个加州，1个滨州）89.04% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是3
>
> **正确答案:**3
>
> **解析:**
>
> 两个备份较近，保证出错时快速恢复，一个较远，保证安全性



#### How to recover when a chunk is broken?

讓Master 幫, Master知道他所有的小弟在哪，

1. 

##### 架構

![image-20200822213644383](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzx20e5tfj31120nwgor.jpg)



#### 

#### 如何知道有個小弟完全掛了？==> 心跳，小弟自報

> ##### [单选题]心跳（Heartbeat）机制怎么设计？
>
> A.Master 轮询 Chunk Server13.62% 选择
>
> B.Chunk Server 主动向 Master 汇报86.38% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B
>
> **解析:**
>
> 主动汇报可以减少通信次数，就一次，不然要兩次。



## Scale 再更多 Q&A

#### Q: 寫到一台server安全嗎？

![image-20200822214053264](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzx6c0e7bj31180i8n17.jpg)

#### Q: 解決客戶端瓶頸，不然client分別去寫他太累了

##### 讓隊長去! 寫怎麼寫？client 把chunk一次傳給三個小弟作replica後，client會變成瓶頸…

隊長再去寫給另兩個人

> ##### [单选题]如何解决 client 传输 replica chunk 的问题？
>
> A.client 将 chunk 传给 master，由 master 去纷发到 3 台 chunk server6.24% 选择
>
> B.client 将 chunk 传给其中一台 chunk server，然后由这台 chunk server 再传给另外的 2 台63.29% 选择
>
> C.client 将 chunk 传给其中一台 chunk server，另外的两个 chunk server 空了再慢慢传30.47% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是B
>
> **正确答案:**B

內網自己傳肯定快得多

![image-20200822214408981](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzx9qdmg2j311a0isadu.jpg)



#### Q: 怎麼選隊長？

1. 可找最近的 (快)
2. 找現在沒在幹活的 (平衡)

> ##### [多选题]下列哪些因素是我们挑选 chunk server 队长时所需要考虑的
>
> A.机器的繁忙程度38.48% 选择
>
> B.距离的远近36.78% 选择
>
> C.剩余存储空间的大小13.27% 选择
>
> D.CPU 的个数11.47% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTQxNzAwNjYyNTQzIiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjEwODgiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxMiAwYTUxMiA1MTIgMCAxIDAgMCAxMDI0QTUxMiA1MTIgMCAwIDAgNTEyIDB6IG0xNjUuOTUyIDYzNy43NmwxNS4wNCAxNC45NzZhMjguNDE2IDI4LjQxNiAwIDEgMS00MC4yNTYgNDAuMjU2bC0xNC45NzYtMTUuMDRMNTA5LjUwNCA1NDkuNzYgMzcxLjIgNjg4YTI4LjQxNiAyOC40MTYgMCAxIDEtNDAuMjU2LTQwLjI1NmwxMzguMzA0LTEzOC4yNC0xMjMuMi0xMjMuMi0xNS4xMDQtMTUuMTA0YTI4LjU0NCAyOC41NDQgMCAwIDEgMC00MC4yNTYgMjguNTQ0IDI4LjU0NCAwIDAgMSA0MC4yNTYgMGwxNS4wNCAxNS4xMDRMNTA5LjQ0IDQ2OS4yNDhsMTQzLjIzMi0xNDMuMjk2YTI4LjQxNiAyOC40MTYgMCAxIDEgNDAuMjU2IDQwLjI1Nkw1NDkuNzYgNTA5LjUwNGwxMjguMTkyIDEyOC4yNTZ6IiBmaWxsPSIjRjY1RTVFIiBwLWlkPSIxMDg5Ij48L3BhdGg+PC9zdmc+)答错了，您选择的答案是B
>
> **正确答案:**AB

> ##### [单选题]每次找的 chunk server 队长是一样的么？
>
> A.是1.55% 选择
>
> B.不是20.48% 选择
>
> C.不一定77.97% 选择
>
> ![img](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTM0MTgxMjgxODM5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjM3NjIiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTUxOC4xMiA1MTYuMTZtLTQ5MCAwYTQ5MCA0OTAgMCAxIDAgOTgwIDAgNDkwIDQ5MCAwIDEgMC05ODAgMFoiIGZpbGw9IiM1NkI0MzIiIHAtaWQ9IjM3NjMiPjwvcGF0aD48cGF0aCBkPSJNMzkzLjIxMzYxOSA2NjQuMzM1NDk1bTI4LjI4NDI3MS0yOC4yODQyNzFsMjk2Ljk4NDg0OS0yOTYuOTg0ODQ4cTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBsMCAwcTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDJsLTI5Ni45ODQ4NDggMjk2Ljk4NDg0OHEtMjguMjg0MjcxIDI4LjI4NDI3MS01Ni41Njg1NDMgMGwwIDBxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDJaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY0Ij48L3BhdGg+PHBhdGggZD0iTTI4OS40Njk4NCA0NTIuODQ3ODgzbTI4LjI4NDI3MSAyOC4yODQyNzFsMTU1LjU2MzQ5MiAxNTUuNTYzNDkycTI4LjI4NDI3MSAyOC4yODQyNzEgMCA1Ni41Njg1NDNsMCAwcS0yOC4yODQyNzEgMjguMjg0MjcxLTU2LjU2ODU0MyAwbC0xNTUuNTYzNDkxLTE1NS41NjM0OTJxLTI4LjI4NDI3MS0yOC4yODQyNzEgMC01Ni41Njg1NDNsMCAwcTI4LjI4NDI3MS0yOC4yODQyNzEgNTYuNTY4NTQyIDBaIiBmaWxsPSIjRkZGRkZGIiBwLWlkPSIzNzY1Ij48L3BhdGg+PC9zdmc+)答对了，您选择的答案是C
>
> **正确答案:**C



#### Q: 解決 Chunk Server Failure

如果有人掛了，隊長知道了，它會跟master說不要再讓哪台能「被」分配東西了

![image-20200822214605591](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzxbqyp6oj313q0kmq6f.jpg)



- 如果沒寫上就一直試，如果太多次，就算了吧大家都完了，都掛了也不大可能

![image-20200822214620405](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzxbzzrrhj31320jyac9.jpg)



## 總結

![image-20200822214743151](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghzxdft2fmj30yy0u079h.jpg)

## GFS Problem

https://www.jiuzhang.com/qa/627/

> - **设计一个只读的lookup service. 后台的数据是10 billion个key-value pair, 服务形式是接受用户输入的key，返回对应的value。**
> **已知每个key的size是0.1kB，每个value的size是1kB。要求系统qps >= 5000，latency < 200ms.**
>   
>   - key: 100; value: 1000個ascii字
>   - server性能参数需要自己问，我当时只问了这些，可能有需要的但是没有问到的……
>     commodity server
>     8X CPU cores on each server
>   32G memory
>     6T disk
>
>   使用任意数量的server，设计这个service。
>
>   就不发我的解法了，真的很渣……=。=|||
>
>   - 我总结了SG_SWE_GM以及其他同学的解答，在此基础上我的想法如下，有问题的地方还请老师同学指正，
>   
>     => total key size ~ 10 billion * 0.1kB = 1T		==> 40台*32G 查起來就是很快
>   => total value size ~ 10 billion * 1kB = 10T
>     所以每台服务器用两块硬盘，共12T。数据结构用SSTable就好了。
>
>     充分利用内存，本来我想用binary search tree做index，但是仔细想想这个服务是只读的，而且硬盘存储键值对用的是SSTable是有序的，key和value长度又是固定的，所以直接把key以有序的方式存在内存就好了，查询的时候对key进行binary search，然后用key在内存中的offset来计算键值对在硬盘中的offset。1T/32G = 31.25. 所以一共需要32台服务器的内存分担key index。前面加一个master负责管理consistent hasing。lg(32G) = 35, 平均查询一个key就算18次内存访问，大约才1800ns，在ms这个量级上可以忽略。
>
>     每一次request，在硬盘上读取1kB value的时间：***10ms(disk seek)*** + 4ms(rotation delay for 7200rpm) + 1kB/1MB * ***30ms(reading 1kB sequentially from disk)*** = 14ms. 目前一台server能处理的的QPS: 1000ms/14ms = 71, 总的QPS: 71 * 32 = 2272。距离要求还有两倍多的差距。所以我们可以给每台server装上6个6T硬盘，组成3套数据硬盘，3套硬盘可以并行处理3个请求，这样也算是稍微利用了一下8X的多核CPU。这时QPS即为2272 * 3=6816.
>
>     延迟：
>   
>     1. master内存查找consistent hashing map的时间：忽略
>     2. master与slave的round trip delay：1 round trip in the same data center is 1ms.
>   3. slave内存index查询时间：忽略
>     4. slave硬盘读取时间：14ms
>   
>     so total latency is 15ms。

- 企業現在一般怎麼配server?
  - 16G、32G、64G、256G、1T、3T，一般不會直接用
  - Disk: 
- 300ms是在尋道
- 0.5 m 是round trip在同個data center間，比在硬盤上找還是快多了
- ***30ms(reading 1kB sequentially from disk)***
  - 是因為硬盤估計每秒可讀30MB的數據，所以1MB就是30ms；這個讀了１kB的話就0.03 ms跟disk seek比起來可以不計。
- QPS on 1 server : 1s/10ms 次（一秒一台可以100次。） * 2disk = 200次
- 5000個QPS/200就需要25台服務器





#### Latency: 

1. 找到key : 硬盤中作二分查找，每次的主要的是找的時間。
2. 讀到value很小，每次的可以忽略

- Sol1.

<img src="/Users/joe/Library/Application Support/typora-user-images/image-20200412220508731.png" alt="image-20200412220508731" style="zoom:50%;" />

- [ ] 分析：log該以2為底，所以就變30 * 10ms(每動一次就要10ms) 就是 300ms, 超過題目規定的200ms，找到key的工作只能在硬盤上做，而且單個硬盤不能並行執行，所以一次query 至少要300ms了，一個硬盤１秒內只能做三次，兩個只能做六次，所以要5000QPS要至少約1000台服務器。這跟他給出的25台差很多！
- [ ] 我們最希望減少的就是300ms的***查詢時間***；***而我們未用上他的內存***，一台有32G，***40***台就有超1TB，就跟所有的數據key量一樣了，所以提示了可以在內存作操作，把所有key都存過去。如果內存中有個內存到硬盤位置的映射的話…！
- [ ] 一個key 0.1kB , 一個position 8Byte，所以一筆仍是0.1kB, 10個billion也是用1TB的內存。所以40台的內存並一起變一個大內存裡直接二分查找就快，每次的時間比硬盤的10ms少到幾乎可不計。
- [ ] 內存去對應硬盤的position。
- [ ] 硬盤二分查找每次要花10ms (disk seek)，但內存不用時間。雖一樣是花30次。所以300ms就省了。所以整體10ms + 0.5ms 就10.5ms。
- [ ] 現在已有40台機器，每台有兩個硬盤，而且每台機器的硬盤可以存下全量的數據 ( 就key啦，就 1T而已)，就是說整體的數據一共有40份拷貝，每個硬盤要花約10ms查找一次，一台可以200次操作(一台有兩顆disk)，40台可以並行作，所以就是**8000QPS > 5000QPS!**
- [ ] 總結：一共４０台機器，內存就是４０台合併起來當一大塊用，內存大小是１TB；它存放的是key到硬盤中position的數據。每台兩個硬盤，硬盤中存的是全量的數據，一次查找的過程就是，首先通過整體的內存找到在硬盤上的某個位置，均衡負載到40台的某個機器上，讀它的key, value，因為在內存查的時間可以不計，所以最後的延遲就在disk seek時間10ms還有整體在網路上傳輸的0.5ms。

> - key 1T value 10T 机器6T 为啥一台机器的硬盘可以存下全部的信息？
>   - key 1T + value 10T = 11T
>     一块硬盘6T，一台机器两块硬盘即可存下
> - 为什么一个硬盘能存全量数据？一个硬盘是6TB，key加value需要11TB。如果是两块硬盘存下所有数据，那应该就是100次，为什么是100*2？
>   - 是2块硬盘存下所有数据，每块存一半。100 * 2 的意思是，你有 2 块一瓶，一块硬盘能够提供 100 IOPS，两块就是 200 IOPS，因为你可以并发嘛。
> - 请问，内存是在不同的40台机器上，如何垮机器二分查找呢？机器间通信延迟怎么可以忽略呢？
>   - 40台机器的内存合并起来看成一个大内存。打个比方，一次查找时可以先去编号20的机器上看，如果大了，再去10号机器上看，如果大了，再去5号机器上看。。。。依次类推。40台机器接在一个交换机（switch）上，通信延迟可以做到很低，如果再配合内核旁路，两台机器内存到内存的延迟最低可以做到接近纳秒级别



## GFS QA

- 硬盤的一個block默認就4KB, as an array in disk
- Checksum ，也紀錄下和, 可用md5算hash
  - 可能會有False Positive, 比如 1,4 两个数据，check sum = 5，但是 2 + 3 也是 5。所以 check sum 相同不能证明数据一定没有发生变化。但是 check sum 不同就表示原始数据肯定发生了变化。因此 check sum 是存在 False Positive 但不存在 False Negative 的。