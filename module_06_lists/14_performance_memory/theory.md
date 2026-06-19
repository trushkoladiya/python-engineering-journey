# Performance & Memory Concepts

Understanding **when** lists are fast and when they're slow helps you write better programs.

## Time Complexity (Basic Intuition)

Different list operations have different speeds:

| Operation | Speed | Why |
|-----------|-------|-----|
| `append()` | Fast | Adds to end |
| `pop()` | Fast | Removes from end |
| `list[i]` | Fast | Direct index access |
| `pop(0)` | Slow | Must shift all elements |
| `insert(0, x)` | Slow | Must shift all elements |
| `x in list` | Slow | Must check every element |
| `remove(x)` | Slow | Must find + shift |

## When Lists Are Efficient

- Accessing elements by index → **fast**
- Adding/removing at the **end** → **fast**
- Iterating through all elements → **good**

## When Lists Are Slow

- Adding/removing at the **beginning** → **slow** (use `deque` instead)
- Checking membership (`in`) → **slow** for large lists (use `set` later)
- Searching for elements → **slow** (consider sorted lists)

## Practical Tip

```python
# ❌ Slow: building with insert at beginning
result = []
for i in range(5):
    result.insert(0, i)   # shifts all elements every time

# ✅ Fast: build normally, then reverse
result = []
for i in range(5):
    result.append(i)
result.reverse()
```

## Key Points

- `append()` and `pop()` are fast (end of list)
- `insert(0, x)` and `pop(0)` are slow (beginning of list)
- `in` checks every element — slow for large lists
- Build at the end and reverse, instead of inserting at the beginning
