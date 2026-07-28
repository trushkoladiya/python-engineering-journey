# Generator Expressions

Generator expressions are a compact way to create generators — similar to list comprehensions, but lazy.

## Syntax

```python
# List comprehension (eager — creates entire list in memory)
squares_list = [x**2 for x in range(5)]

# Generator expression (lazy — produces values on demand)
squares_gen = (x**2 for x in range(5))
```

The only difference is **parentheses `()`** instead of brackets `[]`.

## List Comprehension vs Generator Expression

| Feature | List Comprehension | Generator Expression |
|---------|-------------------|---------------------|
| Syntax | `[expr for x in iter]` | `(expr for x in iter)` |
| Returns | A list | A generator object |
| Memory | All values at once | One value at a time |
| Reusable | Yes (it's a list) | No (exhausts after one pass) |

## When to Use Which

```python
# Use list comprehension when you need ALL values
data = [x**2 for x in range(10)]   # need to access by index

# Use generator expression when you just iterate
total = sum(x**2 for x in range(10))   # only need the sum
```

## Passing to Functions

You can pass a generator expression directly to functions:

```python
# No extra parentheses needed inside a function call
sum(x**2 for x in range(10))
max(len(w) for w in words)
```

## Key Points

- Generator expressions use `()` instead of `[]`
- They are lazy — values are produced on demand
- Use them when you only need to iterate once
- Perfect for passing to `sum()`, `max()`, `min()`, etc.
- More memory-efficient than list comprehensions for large data
