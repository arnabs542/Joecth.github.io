---
layout: post
categories: Python
tag: []
date: 2018-01-16
---

### I-Sort

Used when playing pokers

```python
arr
for i in range(1, len(A)):
  val = A[i]
  j = i-1
  while j>=0 and A[j]>val:
    A[j+1] = A[j]
    j -= 1
  A[j+1] = val  
```

O(n), O(n^2) Worst when inversed sorted.

### B-Sort

```python
def b_sort(A=[4,3,2,1]):
    for i in range(0, len(A)):
        swapped = False
        for j in range(0, len(A)-i-1):
            if A[j] > A[j+1]:
                # A[j] = A[j+1]
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
    
        if swapped == False:
            break
b_sort() 

---
final_count = 0
for i in range(0, n):
    round_count = 0
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            round_count += 1
            a[j], a[j+1] = a[j+1], a[j]

    if round_count == 0:
        break
    final_count += round_count
```

O(n), O(n^2) Worst when inversed sorted.

### S-Sort

```python
for i in range(0, len(A)):
  min_idx = i
  for j in range(1, len(A)):
    if A[j] < A[min_idx]:
      min_idx = j
  A[i], A[min_idx] = A[min_idx], A[i]
```

O(n^2), O(n^2)



![image-20200116202922983](https://tva1.sinaimg.cn/large/006tNbRwly1gayoeij9eoj31620h8wpf.jpg)



### H-sort, Heap-sort

```python
# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  
# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
# This code is contributed by Mohit Kumra 
```

![image-20200116210706828](https://tva1.sinaimg.cn/large/006tNbRwly1gayphqqjdqj311w0tkgso.jpg)

---



### Heap

```python
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

```

copied fr: https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html

Also, 

https://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html

### Q-Sort

```python
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
```



```python
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

def quicksort(data, left, right): # 輸入資料，和從兩邊開始的位置
    if left >= right :            # 如果左邊大於右邊，就跳出function
        return

    i = left                      # 左邊的代理人
    j = right                     # 右邊的代理人
    key = data[left]                 # 基準點

    while i != j:                  
        while data[j] > key and i < j:   # 從右邊開始找，找比基準點小的值
            j -= 1
        while data[i] <= key and i < j:  # 從左邊開始找，找比基準點大的值
            i += 1
        if i < j:                        # 當左右代理人沒有相遇時，互換值
            data[i], data[j] = data[j], data[i] 

    # 將基準點歸換至代理人相遇點
    data[left] = data[i] 
    data[i] = key

    quicksort(data, left, i-1)   # 繼續處理較小部分的子循環
    quicksort(data, i+1, right)  # 繼續處理較大部分的子循環

quicksort(data, 0, len(data)-1)
print(data)
```



### Q-Select

```python
class Solution:
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        
        # Time complexity : O(N)
        # Space complexity : O(1)
        
        dist = lambda x : points[x][0]**2 + points[x][1]**2
        
        def quickselect(l, r, K):
            
            while l < r :
                
                # To avoid the worst case
                i = random.randint(l, r)
                points[i], points[l] = points[l], points[i]
                
                mid = partition(l, r)
                
                if K > mid :
                    l = mid+1
                elif K < mid :
                    r = mid-1
                else :
                    break
            
        def partition(l, r):
            
            i = l # start index
            pivot = dist(i)
            
            l += 1
            
            while True :
                
                while l<r and dist(l)<pivot:
                    l+=1
                    
                while l<=r and dist(r)>=pivot:
                    r-=1
                    
                if l>=r:
                    break
                
                points[l], points[r] = points[r], points[l]
                
            points[r], points[i] = points[i], points[r]
            return r
            
        quickselect(0, len(points)-1, K)
        return points[:K]
    
```

The worst-case time taken by a randomized quick-select is not O(n). It is O(n^2).
{The worst case is when you want to select the minimum element and your pivot at every stage happens to be the last element in the list at that stage.Comment if you didn't get this.}

However the expected time taken by a randomized quick-select is O(n).
I hope you understand the difference.

4.7k views · [View Upvoters](https://www.quora.com/How-is-time-taken-by-a-randomized-quick-select-algorithm-in-O-n#)





### M-Sort

Nxlg(N), where lg(N) is height

```python
# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
```



### Rehash

> 1)![img](https://tva1.sinaimg.cn/large/00831rSTgy1gcsoq9faroj30z80kadlq.jpg)

fr: https://blog.csdn.net/dalong3976/article/details/83934609



>  HashMap的容量为什么是2的n次幂，和这个(n - 1) & hash的计算方法有着千丝万缕的关系，符号&是按位与的计算，这是位运算，计算机能直接运算，特别高效，按位与&的计算方法是，只有当对应位置的数据都为1时，运算结果也为1，当HashMap的容量是2的n次幂时，(n-1)的2进制也就是1111111***111这样形式的，这样与添加元素的hash值进行位运算时，能够充分的散列，使得添加的元素均匀分布在HashMap的每个位置上，减少hash碰撞，下面举例进行说明。
>
>   当HashMap的容量是16时，它的二进制是10000，(n-1)的二进制是01111，与hash值得计算结果如下：
>
> 
>
> 上面四种情况我们可以看出，不同的hash值，和(n-1)进行位运算后，能够得出不同的值，使得添加的元素能够均匀分布在集合中不同的位置上，避免hash碰撞。
>
>   下面就来看一下HashMap的容量不是2的n次幂的情况，当容量为10时，二进制为01010，(n-1)的二进制是01001，向里面添加同样的元素，结果为：
>
> 
>
> 可以看出，有三个不同的元素进过&运算得出了同样的结果，严重的hash碰撞了。
>
> 终上所述，HashMap计算添加元素的位置时，使用的位运算，这是特别高效的运算；另外，HashMap的初始容量是2的n次幂，扩容也是2倍的形式进行扩容，是因为容量是2的n次幂，可以使得添加的元素均匀分布在HashMap中的数组上，减少hash碰撞，避免形成链表的结构，使得查询效率降低！
> ————————————————
> 版权声明：本文为CSDN博主「猿人小郑」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
> 原文链接：https://blog.csdn.net/Apeopl/article/details/88935422

fr: https://blog.csdn.net/Apeopl/article/details/88935422?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task





## B Tree & B+ Tree

### ● B Tree - Balance Tree

indexing for binary search in b-tree

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd48nzmag6j317o0n87i9.jpg" alt="image-20200323223850264" style="zoom:67%;" />

Ref https://www.bilibili.com/video/BV1p7411k7nU?from=search&seid=14903204102279559784

根滿了，根要拆

根沒滿要先走到葉

​	葉沒滿，就直接插入

​	葉滿了，就拆分葉



### ● B+

a variation of B tree in which all of the values are stored in the leaf nodes. 

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd4wyavvudj30wq0no410.jpg" alt="image-20200324123910488" style="zoom:67%;" />



<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd4x00n4irj30wa0o00vc.jpg" alt="image-20200324124051188" style="zoom:67%;" />





![image-20200324124439801](https://tva1.sinaimg.cn/large/00831rSTgy1gd4x3uxztjj30vs0lewia.jpg)

- value of B trees are ordered from least to greatest, the keys in the internalnodes contain the smallest values from each of its children starting form the second one



<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd4xb27uakj30o80lawhk.jpg" alt="image-20200324125126983" style="zoom:67%;" />



<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd4xebkh46j30wa0kwwje.jpg" alt="image-20200324125436567" style="zoom:67%;" />

ref: https://www.youtube.com/watch?v=49P_GDeMDRo











![image-20200323225728609](https://tva1.sinaimg.cn/large/00831rSTgy1gd497dfsn8j310i0b0t9d.jpg)



![image-20200323230114499](https://tva1.sinaimg.cn/large/00831rSTgy1gd49b4ahnxj31ng0u0u0u.jpg)

<img src="https://tva1.sinaimg.cn/large/00831rSTgy1gd4w3w9wtxj30q407wq3e.jpg" alt="image-20200324120956031" style="zoom:67%;" />