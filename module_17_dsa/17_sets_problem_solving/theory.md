# Sets in Problem Solving

## Sets as a DSA Tool

Sets provide **O(1) average** membership testing and automatically handle uniqueness. They're perfect for specific problem patterns.

## Key Operations

| Operation | Time | Example |
|-----------|------|---------|
| `x in s` | O(1) | Membership check |
| `s.add(x)` | O(1) | Add element |
| `s - t` | O(len(s)) | Difference |
| `s & t` | O(min) | Intersection |
| `s \| t` | O(n+m) | Union |

## Common Patterns

### Removing Duplicates
```python
unique = list(set(items))
```

### Fast Membership Testing
```python
valid = {"a", "b", "c"}
if char in valid:    # O(1) instead of O(n) with a list
    ...
```

### Finding Common/Missing Elements
```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
common = set_a & set_b       # {3, 4}
only_in_a = set_a - set_b    # {1, 2}
```

## Key Points

- Use sets when you need **fast lookup** and **uniqueness**
- Set operations (intersection, union, difference) are powerful tools
- Convert to set for O(1) lookups, then back to list if order matters
- Perfect for "find missing", "find common", "find duplicates" problems
