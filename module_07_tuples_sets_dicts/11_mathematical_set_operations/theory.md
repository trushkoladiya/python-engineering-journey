# Mathematical Set Operations

Python sets support the same operations you learn in math — **union**, **intersection**, **difference**, and **symmetric difference**.

## Union — All elements from both sets

Combines elements from both sets (no duplicates):

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)          # {1, 2, 3, 4, 5}
print(a.union(b))     # {1, 2, 3, 4, 5}
```

## Intersection — Elements in both sets

Only elements that appear in **both** sets:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)                # {3, 4}
print(a.intersection(b))    # {3, 4}
```

## Difference — Elements in one but not the other

Elements in `a` that are **not** in `b`:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)              # {1, 2}
print(a.difference(b))    # {1, 2}
print(b - a)              # {5, 6}
```

## Symmetric Difference — Elements in either, but not both

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a ^ b)                         # {1, 2, 5, 6}
print(a.symmetric_difference(b))     # {1, 2, 5, 6}
```

## Key Points

| Operation | Operator | Method |
|-----------|----------|--------|
| Union | `\|` | `.union()` |
| Intersection | `&` | `.intersection()` |
| Difference | `-` | `.difference()` |
| Symmetric Difference | `^` | `.symmetric_difference()` |
