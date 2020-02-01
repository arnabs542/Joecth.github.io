---
layout: post
categories: LC
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

### M-Sort

Nxlg(N), where lg(N) is height