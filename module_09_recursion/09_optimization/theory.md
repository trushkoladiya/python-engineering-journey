# Optimization Techniques

Naive recursion can be very slow. **Memoization** fixes this by remembering previous results.

## The Problem: Overlapping Subproblems

In tree recursion, the same calculations are repeated many times:

```
fibonacci(5)
├── fibonacci(4)
│   ├── fibonacci(3)     ← computed here
│   └── fibonacci(2)     ← computed here
└── fibonacci(3)         ← computed AGAIN!
    └── fibonacci(2)     ← computed AGAIN!
```

## Memoization (Caching Results)

Store results in a dictionary — if we've already computed something, return the stored result:

```python
def fibonacci(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```

This turns exponential time into **linear** time!

## The Impact

| n | Without memo | With memo |
|---|-------------|-----------|
| 10 | 177 calls | 19 calls |
| 20 | 21,891 calls | 39 calls |
| 30 | 2,692,537 calls | 59 calls |

## Key Points

- Overlapping subproblems = same computation done multiple times
- Memoization = store results to avoid recomputation
- Turns exponential → linear for many problems
- Python's `functools.lru_cache` does this automatically
