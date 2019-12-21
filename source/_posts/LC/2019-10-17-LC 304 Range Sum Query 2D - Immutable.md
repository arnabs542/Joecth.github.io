---
layout: post
categories: LC
date: 2019-10-17
tag: [TODO, F] 



---



```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
          if matrix is None or not matrix:
              return
          n, m = len(matrix), len(matrix[0])
          self.sums = [ [0 for j in range(m+1)] for i in range(n+1) ]
          for i in range(1, n+1):
              for j in range(1, m+1):
                  self.sums[i][j] = matrix[i-1][j-1] + self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]
    
  

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
          row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
          return self.sums[row2][col2] - self.sums[row2][col1-1] - self.sums[row1-1][col2] + self.sums[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```

["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]

Expected result
[null,8,11,12]

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

self.accu:
[[0, 0, 0, 0, 0, 0], 
 [0, 3, 3, 4, 8, 10], 
 [0, 8, 14, 18, 24, 27], 
 [0, 9, 17, 21, 28, 36], 
 [0, 13, 22, 26, 34, 49], 
 [0, 14, 23, 30, 38, 58]]