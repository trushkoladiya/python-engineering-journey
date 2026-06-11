# Copying Lists

Copying lists is tricky because of how Python handles references. Understanding this prevents many bugs.

## Reference vs Copy

When you assign a list to another variable, both point to the **same** list:

```python
a = [1, 2, 3]
b = a           # b is NOT a copy — it's the same list
b[0] = 999
print(a)   # [999, 2, 3] — a changed too!
```

## Shallow Copy Methods

To create an **independent** copy:

```python
original = [1, 2, 3]

# Method 1: Slice
copy1 = original[:]

# Method 2: copy() method
copy2 = original.copy()

# Method 3: list() constructor
copy3 = list(original)
```

All three create a new list with the same values.

## Shallow Copy Limitation

A shallow copy only copies the **outer** list. Inner lists are still shared:

```python
original = [[1, 2], [3, 4]]
copy = original[:]
copy[0][0] = 999
print(original)   # [[999, 2], [3, 4]] — inner list changed!
```

## Deep Copy Concept

To fully copy nested structures, you need a **deep copy**:

```python
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 999
print(original)   # [[1, 2], [3, 4]] — unchanged!
```

## Key Points

- `b = a` creates a **reference** (not a copy)
- `a[:]`, `a.copy()`, `list(a)` create **shallow copies**
- Shallow copies don't copy inner lists (nested data)
- Use `copy.deepcopy()` for fully independent nested copies
