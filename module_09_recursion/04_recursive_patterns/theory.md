# Basic Recursive Patterns

Recursive functions follow two main patterns based on how many recursive calls they make.

## Linear Recursion

Makes **one** recursive call per function invocation. The call chain forms a straight line.

```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)   # ONE call
```

## Binary / Tree Recursion

Makes **two or more** recursive calls. The call chain branches like a tree.

```python
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # TWO calls
```

## Comparison

| Pattern | Calls per level | Growth | Example |
|---------|----------------|--------|---------|
| Linear | 1 | n calls total | factorial, sum |
| Binary/Tree | 2+ | Exponential | fibonacci, subsets |

## Key Points

- Linear recursion: one call → simple chain → efficient
- Tree recursion: multiple calls → branching → can be slow
- Tree recursion often has repeated work (fibonacci computes the same values many times)
- Memoization can fix the repeated work problem (covered later)
