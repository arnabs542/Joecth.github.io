---
layout: post
categories: LC
tag: [Fu, TODO, F] 


---



```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        if not grid[0]:
            return 0
        
        land = 0
        overlap = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    land +=1
                    if r < len(grid)-1 and grid[r+1][c] == 1:
                        overlap += 1
                    if c < len(grid[0])-1 and grid[r][c+1] == 1:
                        overlap += 1
                        
        print(land)
        return 4* land - 2* overlap
```

