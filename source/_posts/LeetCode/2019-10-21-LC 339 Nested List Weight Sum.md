---
categories: LC
tag: [F, DFS] 



---



```python
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        counter = 0
        queue = [(1, e) for e in nestedList]
        while queue:
            weight, e = queue.pop(0)
            if e.isInteger():
                counter += e.getInteger()*weight
            else:
                for child_list in e.getList():
                    queue.append((weight+1, child_list))
                
        return counter
```

