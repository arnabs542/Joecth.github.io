---
layout: post
categories: LC
tag: [D&C] 



---



```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        cur_row, cur_col = 0, n - 1
        while cur_row < m and cur_col >=0:
            val = matrix[cur_row][cur_col]
            if val == target:
                return True
            elif val > target:
                cur_col -= 1
            else:
                cur_row += 1
        return False
```

