# Recursion Limits & Safety

Python has built-in protection against infinite recursion. Understanding these limits keeps your code safe.

## Python's Recursion Limit

Python defaults to a maximum of **1000** recursive calls:

```python
import sys
print(sys.getrecursionlimit())   # 1000
```

Exceeding this causes a `RecursionError`.

## Stack Overflow

Each recursive call uses memory for a stack frame. Too many calls = out of memory:

```python
def infinite():
    return infinite()   # 💥 RecursionError!
```

## Avoiding Infinite Recursion

1. **Always have a base case**
2. **Ensure progress toward the base case** — the input must get smaller
3. **Test with small inputs first**

```python
# ❌ Bad: n never reaches 0
def bad(n):
    return bad(n + 1)   # Gets BIGGER, never stops

# ✅ Good: n decreases toward base case
def good(n):
    if n <= 0: return 0
    return n + good(n - 1)   # Gets smaller
```

## Key Points

- Python's default limit is ~1000 recursive calls
- `RecursionError` is Python's protection against stack overflow
- You can increase the limit with `sys.setrecursionlimit()` (be careful!)
- Better solution: convert deep recursion to a loop
