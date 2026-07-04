# Common Mistakes & Debugging

Recursion bugs can be tricky. Here are the most common mistakes and how to fix them.

## Typical Errors

### 1. Missing Base Case
```python
# ❌ No base case — infinite recursion
def bad(n):
    return n + bad(n - 1)

# ✅ Fixed
def good(n):
    if n <= 0: return 0
    return n + good(n - 1)
```

### 2. Incorrect Recursive Step
```python
# ❌ Moving away from base case
def bad(n):
    if n <= 0: return 0
    return bad(n + 1)   # Gets bigger!

# ✅ Fixed
def good(n):
    if n <= 0: return 0
    return good(n - 1)   # Gets smaller
```

### 3. Not Returning the Recursive Call
```python
# ❌ Missing return
def bad(n):
    if n <= 0: return 0
    bad(n - 1)   # Result is lost!

# ✅ Fixed
def good(n):
    if n <= 0: return 0
    return good(n - 1)
```

## Debugging Techniques

1. **Add print statements** to trace calls
2. **Use indentation** to show depth
3. **Test with tiny inputs** first (n=1, n=2, n=3)
4. **Draw the call tree** on paper

## Key Points

- Always check: Do I have a base case? Does it get reached?
- Always check: Am I returning the recursive result?
- Debug by tracing with prints
- Start with the smallest possible input
