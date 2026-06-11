# Performance & Optimization

Functional programming offers tools for **efficient data processing**. Understanding when to use lazy evaluation and when to avoid unnecessary copies is key.

## Lazy vs Eager Evaluation

| Type | Example | Creates Data |
|------|---------|-------------|
| Eager | `list(...)`, `[...]` | All at once in memory |
| Lazy | `map()`, `filter()`, generators | One at a time, on demand |

```python
# EAGER — creates entire list in memory
squares = [x ** 2 for x in range(1_000_000)]

# LAZY — creates nothing until consumed
squares = (x ** 2 for x in range(1_000_000))
```

## When to Use Lazy Evaluation

- Processing **large datasets** that don't fit in memory
- When you only need **some** of the results
- When **chaining** multiple transformations

## Avoiding Unnecessary Copies

```python
# BAD: creates 3 intermediate lists
step1 = [x for x in data if x > 0]
step2 = [x * 2 for x in step1]
step3 = [str(x) for x in step2]

# GOOD: single pass with generator chain
result = (str(x * 2) for x in data if x > 0)
```

## Key Points

- Use generators and lazy iterators for large data
- Chain `map()` and `filter()` for zero-copy pipelines
- Convert to `list()` only when you need the final result
- `itertools` provides efficient iterator tools
- Profile before optimizing — readability comes first
