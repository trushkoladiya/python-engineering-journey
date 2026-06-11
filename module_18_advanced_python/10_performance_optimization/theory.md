# Performance Optimization

## Why Optimize?

Code that works is great. Code that works **fast** is better. Performance optimization means making your code run faster or use less resources without changing what it does.

## Step 1: Measure First

**Never optimize blindly.** Always measure to find the bottleneck.

```python
import time

start = time.time()
# ... your code ...
elapsed = time.time() - start
print(f"Took {elapsed:.4f}s")
```

## Profiling with cProfile

```python
import cProfile

def my_function():
    total = sum(range(1_000_000))
    return total

cProfile.run('my_function()')
```

This shows how much time each function call takes — helping you find the slow parts.

## timeit for Micro-Benchmarks

```python
import timeit

# Time a small piece of code
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Took {t:.4f}s for 10000 runs")
```

## Common Optimization Techniques

| Technique | Example |
|-----------|---------|
| Use built-in functions | `sum()` instead of manual loop |
| Choose right data structure | `set` for lookups instead of `list` |
| Avoid repeated computation | Cache results |
| Reduce function calls | Inline simple operations |
| Use list comprehension | Faster than `append` in a loop |

## Key Principle

> "Premature optimization is the root of all evil." — Donald Knuth

1. **Make it work** first
2. **Make it right** (clean, readable)
3. **Make it fast** (only if needed, and only the slow parts)

## Key Points

- Always **measure** before optimizing
- Use `time.time()`, `timeit`, or `cProfile` to find bottlenecks
- Optimize the **slowest part** first — it has the most impact
- Built-in functions are usually faster than manual Python loops
- The right data structure makes more difference than clever tricks
