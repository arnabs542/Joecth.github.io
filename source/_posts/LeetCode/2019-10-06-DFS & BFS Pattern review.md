---
layout: post
categories: LC
tag: [Review] 



---



## 111. Minimum Depth of Binary Tree 

Average Rating: 4.71 (14 votes)

Oct. 28, 2018  |  17.4K views

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.

**Example:**

Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its minimum depth = 2.

## Solution

**Tree definition**

First of all, here is the definition of the `TreeNode` which we would use.

<iframe src="https://leetcode.com/playground/42eFhXEs/shared" frameborder="0" width="100%" height="225" name="42eFhXEs" style="box-sizing: border-box;"></iframe>





------

#### Approach 1: Recursion

**Algorithm**

The intuitive approach is to solve the problem by recursion. Here we demonstrate an example with the DFS (Depth First Search) strategy.

<iframe src="https://leetcode.com/playground/RuBTnmW3/shared" frameborder="0" width="100%" height="412" name="RuBTnmW3" style="box-sizing: border-box;"></iframe>

**Complexity analysis**

- Time complexity : we visit each node exactly once, thus the time complexity is \mathcal{O}(N)O(*N*), where N*N* is the number of nodes.

- Space complexity : in the worst case, the tree is completely unbalanced, *e.g.* each node has only one child node, the recursion call would occur N*N* times (the height of the tree), therefore the storage to keep the call stack would be \mathcal{O}(N)O(*N*). But in the best case (the tree is completely balanced), the height of the tree would be \log(N)log(*N*). Therefore, the space complexity in this case would be \mathcal{O}(\log(N))O(log(*N*)).

  

------

#### Approach 2: DFS Iteration

We could also convert the above recursion into iteration, with the help of stack.

> The idea is to visit each leaf with the DFS strategy, while updating the minimum depth when we reach the leaf node.

So we start from a stack which contains the root node and the corresponding depth which is `1`. Then we proceed to the iterations: pop the current node out of the stack and push the child nodes. The minimum depth is updated at each leaf node.

<iframe src="https://leetcode.com/playground/qGDnLgYs/shared" frameborder="0" width="100%" height="500" name="qGDnLgYs" style="box-sizing: border-box;"></iframe>

**Complexity analysis**

- Time complexity : each node is visited exactly once and time complexity is \mathcal{O}(N)O(*N*).

- Space complexity : in the worst case we could keep up to the entire tree, that results in \mathcal{O}(N)O(*N*) space complexity.

  

------

#### Approach 3: BFS Iteration

The drawback of the DFS approach in this case is that all nodes should be visited to ensure that the minimum depth would be found. Therefore, this results in a \mathcal{O}(N)O(*N*) complexity. One way to optimize the complexity is to use the BFS strategy. We iterate the tree level by level, and the first leaf we reach corresponds to the minimum depth. As a result, we do not need to iterate all nodes.

<iframe src="https://leetcode.com/playground/C5HyFNMJ/shared" frameborder="0" width="100%" height="500" name="C5HyFNMJ" style="box-sizing: border-box;"></iframe>

**Complexity analysis**

- Time complexity : in the worst case for a balanced tree we need to visit all nodes level by level up to the tree height, that excludes the bottom level only. This way we visit N/2*N*/2 nodes, and thus the time complexity is \mathcal{O}(N)O(*N*).
- Space complexity : is the same as time complexity here \mathcal{O}(N)O(*N*).

Analysis written by @[liaison](https://leetcode.com/liaison/) and @[andvary](https://leetcode.com/andvary/)

Rate this article: