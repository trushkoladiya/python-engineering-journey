# Linked List

## What Is a Linked List?

A **linked list** is a sequence of **nodes**, where each node contains:
- **Data** — the value stored
- **Next** — a reference (pointer) to the next node

Unlike lists/arrays, linked list elements are **not stored in contiguous memory**. Each node points to the next one.

```
[10 | →] → [20 | →] → [30 | →] → None
```

## Why Use Linked Lists?

| Operation | Array/List | Linked List |
|-----------|-----------|-------------|
| Access by index | O(1) | O(n) |
| Insert at beginning | O(n) | O(1) |
| Insert at end | O(1)* | O(n)** |
| Delete from beginning | O(n) | O(1) |

*Amortized for Python lists. **O(1) if you track the tail.

Linked lists excel at **frequent insertions/deletions** at the beginning.

## Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Types

- **Singly linked list** — each node points to the next
- **Doubly linked list** — each node points to next AND previous
- **Circular linked list** — last node points back to first

## Key Points

- Nodes are connected via references, not indices
- O(1) insertion/deletion at head
- O(n) access by position (must traverse)
- Foundation for more complex structures (stacks, queues, graphs)
