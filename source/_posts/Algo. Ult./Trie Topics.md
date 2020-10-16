---
layout: post
categories: AlgoUlt.
tag: [] 
date: 2019-09-25
---



## 559 Trie Service

Build tries from a list of <word, freq> pairs. Save top 10 for each node.

### Example

**Example1**

```
Input:  
 <"abc", 2>
 <"ac", 4>
 <"ab", 9>
Output:<a[9,4,2]<b[9,2]<c[2]<>>c[4]<>>> 
Explanation:
			Root
             / 
           a(9,4,2)
          /    \
        b(9,2) c(4)
       /
     c(2)
```

**Example2**

```
Input:  
<"a", 10>
<"c", 41>
<"b", 50>
<"abc", 5>
Output: <a[10,5]<b[5]<c[5]<>>>b[50]<>c[41]<>>
```

```python
Serialize and deserialize a trie (prefix tree, search on internet for more details).

You can specify your own serialization algorithm, the online judge only cares about whether you can successfully deserialize the output from your own serialize function.

You only need to implement these two functions serialize and deserialize. We will run the following code snippet

str = serialize(old_trie)
// str can be any string used to represent this tree
new_trie = deserialize(str)
// The new tree should be identical to the old one
Example
Example 1

Input: <a<b<e<>>c<>d<f<>>>>
Output: <a<b<e<>>c<>d<f<>>>>
Explanation:
The trie is look like this.
     root
      /
     a
   / | \
  b  c  d
 /       \
e         f
Example 2

Input: <a<>>
Output: <a<>>
Notice
You don't have to serialize like the test data, you can design your own format.
```



## 527 Trie Serialization

Serialize and deserialize a trie (prefix tree, search on internet for more details).

You can specify your own serialization algorithm, the online judge only cares about whether you can successfully deserialize the output from your own serialize function.

You only need to implement these two functions `serialize` and `deserialize`. We will run the following code snippet

```cpp
str = serialize(old_trie)
// str can be any string used to represent this tree
new_trie = deserialize(str)
// The new tree should be identical to the old one
```

### Example

**Example 1**

```plain
Input: <a<b<e<>>c<>d<f<>>>>
Output: <a<b<e<>>c<>d<f<>>>>
Explanation:
The trie is look like this.
     root
      /
     a
   / | \
  b  c  d
 /       \
e         f
```

**Example 2**

```plain
Input: <a<>>
Output: <a<>>
```

### Notice

You don't have to serialize like the test data, you can design your own format.

```python
"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
"""
class Solution:

    '''
    @param root: An object of TrieNode, denote the root of the trie.
    This method will be invoked first, you should design your own algorithm 
    to serialize a trie which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # Write your code here
        if root is None:
            return ""

        data = ""
        for key, value in root.children.items():
            data += key + self.serialize(value)

        return "<%s>" % data


    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # Write your code here
        if data is None or len(data) == 0:
            return None

        root = TrieNode()
        current = root
        path =[]
        for c in data:
            if c == '<':
                path.append(current)
            elif c == '>':
                path.pop()
            else:
                current = TrieNode()
                if len(path) == 0:
                    print c, path
                path[-1].children[c] = current

        return root
```

