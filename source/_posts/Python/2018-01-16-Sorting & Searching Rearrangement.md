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
for i in range(0, len(A)):
	for j in range(0, len(A)-i-1):
  	# val = A[j]
    swapped = False
    if A[j] > A[j+1]:
      # A[j] = A[j+1]
      A[j], A[j+1] = A[j+1], A[j]
    	swapped = True
    
  if swapped == False:
    break
    
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

