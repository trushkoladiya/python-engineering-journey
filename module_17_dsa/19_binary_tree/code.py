# ============================================
# MODULE 17 - SUBTOPIC 19: Binary Tree
# ============================================

# Binary tree: each node has at most two children.
# Traversals: inorder, preorder, postorder.

from collections import deque

# =============================
# 1. TREE NODE
# =============================

print("=== Tree Node ===")
print()

class TreeNode:
    """A node in a binary tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.data})"

# Build a tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("  Tree built:")
print("        1")
print("       / \\")
print("      2   3")
print("     / \\   \\")
print("    4   5   6")
print()

# =============================
# 2. TREE TRAVERSALS
# =============================

print("=== Tree Traversals ===")
print()

def inorder(node):
    """Left → Root → Right."""
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)

def preorder(node):
    """Root → Left → Right."""
    if node is None:
        return []
    return [node.data] + preorder(node.left) + preorder(node.right)

def postorder(node):
    """Left → Right → Root."""
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.data]

print(f"  Inorder   (L-Root-R): {inorder(root)}")
print(f"  Preorder  (Root-L-R): {preorder(root)}")
print(f"  Postorder (L-R-Root): {postorder(root)}")
print()

# =============================
# 3. LEVEL ORDER TRAVERSAL (BFS)
# =============================

print("=== Level Order Traversal (BFS) ===")
print()

def level_order(root):
    """Visit nodes level by level using a queue."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

print(f"  Level order: {level_order(root)}")
print()

# Level by level (grouped)
def level_order_grouped(root):
    """Return nodes grouped by level."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

levels = level_order_grouped(root)
for i, level in enumerate(levels):
    print(f"  Level {i}: {level}")
print()

# =============================
# 4. TREE PROPERTIES
# =============================

print("=== Tree Properties ===")
print()

def tree_height(node):
    """Calculate height of tree."""
    if node is None:
        return -1    # or 0, depending on convention
    left_height = tree_height(node.left)
    right_height = tree_height(node.right)
    return 1 + max(left_height, right_height)

def count_nodes(node):
    """Count total nodes."""
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def count_leaves(node):
    """Count leaf nodes."""
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

print(f"  Height: {tree_height(root)}")
print(f"  Total nodes: {count_nodes(root)}")
print(f"  Leaf nodes: {count_leaves(root)}")
print()

# =============================
# 5. BINARY SEARCH TREE (BST)
# =============================

print("=== Binary Search Tree ===")
print()

class BST:
    """Binary Search Tree — left < root < right."""

    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert value into BST."""
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def search(self, data):
        """Search for value. O(log n) average."""
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def inorder(self):
        """Return sorted elements."""
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.data] + self._inorder(node.right)

bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]
for val in values:
    bst.insert(val)

print(f"  Inserted: {values}")
print(f"  Inorder (sorted): {bst.inorder()}")
print(f"  Search 40: {bst.search(40)}")
print(f"  Search 55: {bst.search(55)}")
print()

# BST structure:
#        50
#       /  \
#      30   70
#     / \  / \
#    20 40 60 80
print("  BST structure:")
print("        50")
print("       /  \\")
print("      30   70")
print("     / \\ / \\")
print("    20 40 60 80")
print()

# =============================
# 6. TREE PROBLEMS
# =============================

print("=== Tree Problems ===")
print()

# Maximum value in tree
def max_value(node):
    if node is None:
        return float('-inf')
    return max(node.data, max_value(node.left), max_value(node.right))

print(f"  Max value in tree: {max_value(root)}")

# Sum of all nodes
def tree_sum(node):
    if node is None:
        return 0
    return node.data + tree_sum(node.left) + tree_sum(node.right)

print(f"  Sum of all nodes: {tree_sum(root)}")

# Check if tree contains a value
def tree_contains(node, target):
    if node is None:
        return False
    if node.data == target:
        return True
    return tree_contains(node.left, target) or tree_contains(node.right, target)

print(f"  Contains 5: {tree_contains(root, 5)}")
print(f"  Contains 9: {tree_contains(root, 9)}")
print()

# =============================
# 7. INVERT (MIRROR) A TREE
# =============================

print("=== Invert Binary Tree ===")
print()

def invert_tree(node):
    """Swap left and right children at every node."""
    if node is None:
        return None
    node.left, node.right = node.right, node.left
    invert_tree(node.left)
    invert_tree(node.right)
    return node

# Build a new tree for inversion
mirror_root = TreeNode(1)
mirror_root.left = TreeNode(2)
mirror_root.right = TreeNode(3)
mirror_root.left.left = TreeNode(4)
mirror_root.left.right = TreeNode(5)

print(f"  Before: {level_order(mirror_root)}")
invert_tree(mirror_root)
print(f"  After:  {level_order(mirror_root)}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a function to find the minimum depth
#    of a binary tree
# 2. Check if two binary trees are identical
# 3. Find the lowest common ancestor of two nodes
#    in a BST
# ============================================
