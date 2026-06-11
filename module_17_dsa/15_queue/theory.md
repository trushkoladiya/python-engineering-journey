# Queue

## What Is a Queue?

A **queue** is a **FIFO** (First In, First Out) data structure. The first element added is the first one removed.

Think of a line at a store:
- People **join** at the back → `enqueue`
- People **leave** from the front → `dequeue`

## Operations

| Operation | Description | Time |
|-----------|-------------|------|
| enqueue(item) | Add to back | O(1) |
| dequeue() | Remove from front | O(1)* |
| peek() | View front item | O(1) |
| is_empty() | Check if empty | O(1) |

*O(1) with `collections.deque`, O(n) with a list

## Why Not Use a List?

```python
# Using list — removing from front is O(n)!
queue = [1, 2, 3]
queue.pop(0)     # O(n) — shifts all elements

# Using deque — removing from front is O(1)
from collections import deque
queue = deque([1, 2, 3])
queue.popleft()  # O(1) — no shifting needed
```

## Common Applications

- **Task scheduling** — process tasks in order
- **BFS** (Breadth-First Search) — explore graphs level by level
- **Print queue** — documents print in order
- **Message queues** — handle requests in order

## Key Points

- FIFO: First In, First Out
- Use `collections.deque` for efficient queues in Python
- Lists work but are slow for `pop(0)` — O(n) vs O(1)
- Queues are essential for BFS and scheduling
