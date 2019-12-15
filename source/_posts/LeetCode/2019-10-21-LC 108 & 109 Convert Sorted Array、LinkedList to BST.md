---
layout: post
categories: LC
tag: [Michelle, TODO] 



---


### 108
```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums)//2
        print(mid)
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return node
```

### 109
```python
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        tree = []
        while head:
            tree.append(head.val)
            head = head.next
        root = self.constructTree(tree)        
        return root
    
    def constructTree(self, tree):
        if not tree:
            return
        mid = len(tree)//2
        root = TreeNode(tree[mid])
        root.left = self.constructTree(tree[:mid])
        root.right = self.constructTree(tree[mid+1:])
        return root
```

```python
def sortedListToBST(self, head):
    if not head:
        return 
    if not head.next:
        return TreeNode(head.val)
    # here we get the middle point,
    # even case, like '1234', slow points to '2',
    # '3' is root, '12' belongs to left, '4' is right
    # odd case, like '12345', slow points to '2', '12'
    # belongs to left, '3' is root, '45' belongs to right
    slow, fast = head, head.next.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # tmp points to root
    tmp = slow.next
    # cut down the left child
    slow.next = None
    root = TreeNode(tmp.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(tmp.next)
    return root

```