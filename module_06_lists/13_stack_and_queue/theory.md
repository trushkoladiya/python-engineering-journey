# List as Stack & Queue

Lists can be used to implement common data structures: **stacks** and **queues**.

## Stack (Last In, First Out — LIFO)

A stack works like a pile of plates — the **last** item added is the **first** one removed.

```python
stack = []
stack.append("A")   # push
stack.append("B")   # push
stack.append("C")   # push
print(stack)         # ['A', 'B', 'C']

top = stack.pop()    # pop — removes 'C'
print(top)           # C
print(stack)         # ['A', 'B']
```

- **Push**: `append()` — add to top
- **Pop**: `pop()` — remove from top

## Queue (First In, First Out — FIFO)

A queue works like a line at a store — the **first** person in line is the **first** served.

```python
queue = []
queue.append("A")    # enqueue
queue.append("B")
queue.append("C")

first = queue.pop(0)  # dequeue — removes 'A'
print(first)           # A
```

> **Note**: `pop(0)` on a list is **slow** for large lists. For better performance, use `collections.deque`.

## `collections.deque` (Intro)

A `deque` (double-ended queue) is optimized for adding/removing from both ends:

```python
from collections import deque
queue = deque()
queue.append("A")       # add to right
queue.append("B")
first = queue.popleft()  # remove from left — fast!
print(first)             # A
```

## Key Points

- **Stack**: use `append()` and `pop()` — LIFO
- **Queue**: use `append()` and `pop(0)` — FIFO (slow with lists)
- **deque**: better queue — fast `append()` and `popleft()`
