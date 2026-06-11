# Stack

## What Is a Stack?

A **stack** is a **LIFO** (Last In, First Out) data structure. The last element added is the first one removed.

Think of a stack of plates:
- You **add** plates on top → `push`
- You **remove** from the top → `pop`
- You can only see the **top** → `peek`

## Operations

| Operation | Description | Time |
|-----------|-------------|------|
| push(item) | Add to top | O(1) |
| pop() | Remove from top | O(1) |
| peek() | View top without removing | O(1) |
| is_empty() | Check if stack is empty | O(1) |

## Implementation in Python

```python
# Using a list (simplest)
stack = []
stack.append(1)    # push
stack.append(2)    # push
top = stack.pop()  # pop → 2

# Using a custom class
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()
```

## Common Applications

- **Undo/Redo** functionality
- **Balanced parentheses** checking
- **Function call stack** (how Python tracks function calls)
- **Expression evaluation**
- **Backtracking algorithms**

## Key Points

- LIFO: Last In, First Out
- All operations are O(1)
- Python lists work as stacks (use `append` and `pop`)
- Stacks appear everywhere in programming
