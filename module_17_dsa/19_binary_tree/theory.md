# Binary Tree

## What Is a Binary Tree?

A **binary tree** is a data structure where each node has at most **two children** — called **left** and **right**.

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

## Terminology

| Term | Meaning |
|------|---------|
| Root | Top node (1 in the example) |
| Leaf | Node with no children (4, 5, 6) |
| Parent | Node above another node |
| Child | Node below another node |
| Depth | Distance from root to node |
| Height | Distance from node to deepest leaf |

## Node Structure

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

## Tree Traversals

Three ways to visit all nodes:

### Inorder (Left → Root → Right)
Visits nodes in **sorted order** for BSTs.

### Preorder (Root → Left → Right)
Visits root **first** — useful for copying trees.

### Postorder (Left → Right → Root)
Visits root **last** — useful for deleting trees.

```
        1
       / \
      2   3

Inorder:   2, 1, 3
Preorder:  1, 2, 3
Postorder: 2, 3, 1
```

## Key Points

- Binary trees are recursive structures — each subtree is itself a tree
- Traversals are naturally recursive
- Binary Search Trees (BSTs) keep data sorted: left < root < right
- Trees are the foundation for many advanced data structures
