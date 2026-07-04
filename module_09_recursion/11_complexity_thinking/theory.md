# Complexity Thinking (Introduction)

Understanding **how fast** a recursive function runs helps you choose the right approach.

## Time Complexity

How many operations does the function perform as input grows?

### Linear Recursion — O(n)
One recursive call per level → n calls total:

```python
def factorial(n):    # O(n) — n calls
    if n <= 1: return 1
    return n * factorial(n - 1)
```

### Exponential Recursion — O(2^n)
Two recursive calls per level → doubles each time:

```python
def fibonacci(n):    # O(2^n) — exponential!
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Space Complexity

How much memory does the recursion use?

- Each call uses a **stack frame**
- Linear recursion: O(n) stack frames
- With memoization: O(n) cache + O(n) stack

## Key Points

- Linear recursion: O(n) time, O(n) space — efficient
- Tree recursion: O(2^n) time — slow without memoization
- Memoization turns O(2^n) → O(n) by caching results
- Always consider: "Can this be done in O(n) with a loop?"
