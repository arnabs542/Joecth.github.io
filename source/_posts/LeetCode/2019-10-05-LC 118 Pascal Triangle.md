---
layout: post
categories: LC
tag: [Michell, TODO, F] 



---





```python
class Solution():

    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            # res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
            res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]

        return res[:numRows]


print(Solution().generate(5))
```

```
   explanation: Any row can be constructed using the offset sum of the previous row. Example:

    1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1
```

