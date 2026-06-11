# Frozen Set

A **frozenset** is an **immutable** version of a set. Once created, you cannot add or remove elements.

## Creating a Frozen Set

```python
fs = frozenset([1, 2, 3, 4, 5])
print(fs)        # frozenset({1, 2, 3, 4, 5})
print(type(fs))  # <class 'frozenset'>
```

## Frozenset is Immutable

```python
fs = frozenset([1, 2, 3])
# fs.add(4)       # AttributeError!
# fs.remove(1)    # AttributeError!
```

## Frozenset Supports Read Operations

All non-modifying set operations work:

```python
fs = frozenset([1, 2, 3, 4, 5])
print(3 in fs)      # True
print(len(fs))       # 5

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(a | b)   # frozenset({1, 2, 3, 4, 5})
print(a & b)   # frozenset({3})
```

## Use Cases

- As **dictionary keys** (regular sets can't be used as keys)
- As **elements of another set**
- When you want to ensure a set is never modified

## Key Points

- `frozenset()` creates an immutable set
- Cannot add, remove, or modify elements
- Supports all read operations and set math
- Can be used as dictionary keys or set elements
