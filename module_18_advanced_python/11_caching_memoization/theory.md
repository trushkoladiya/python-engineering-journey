# Caching & Memoization

## What Is Caching?

**Caching** means storing the result of an expensive operation so you can reuse it later without recomputing.

```python
# Without caching — recomputes every time
def expensive_operation(n):
    time.sleep(1)  # Simulate slow computation
    return n * n

# With caching — stores result after first call
cache = {}
def cached_operation(n):
    if n not in cache:
        time.sleep(1)
        cache[n] = n * n
    return cache[n]
```

## What Is Memoization?

**Memoization** is a specific type of caching for **function results**. It stores the return value for each unique set of arguments.

## functools.lru_cache

Python provides a built-in decorator for memoization:

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # Instant — results are cached
```

- `maxsize=128` → Cache up to 128 unique argument combinations
- `maxsize=None` → Unlimited cache (use carefully)

## When to Use Caching

| Situation | Use Cache? |
|-----------|-----------|
| Same inputs called repeatedly | ✅ Yes |
| Pure function (no side effects) | ✅ Yes |
| Expensive computation | ✅ Yes |
| Results change over time | ❌ No (stale data) |
| Unique inputs every time | ❌ No (wasted memory) |

## Cache Info

```python
@lru_cache(maxsize=128)
def square(n):
    return n * n

square(5)
square(5)  # From cache
print(square.cache_info())
# CacheInfo(hits=1, misses=1, maxsize=128, currsize=1)
```

## Key Points

- Caching avoids recomputing expensive results
- `@lru_cache` is Python's built-in memoization decorator
- Only works with **hashable** arguments (no lists or dicts)
- Use `cache_info()` to monitor cache effectiveness
- Clear cache with `cache_clear()` when needed
