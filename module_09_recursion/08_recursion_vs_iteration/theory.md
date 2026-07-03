# Recursion vs Iteration

Every recursive solution can be written as a loop, and vice versa. Knowing **when** to use each is important.

## When Recursion is Better

- **Tree-structured problems**: subsets, permutations, tree traversal
- **Naturally recursive problems**: fractals, divide & conquer
- **Cleaner code**: when the recursive version is simpler to read

## When Loops are Better

- **Simple repetition**: counting, summing, iterating lists
- **Performance matters**: loops avoid stack overhead
- **Deep iteration**: loops don't hit recursion limits

## Converting Recursion to Iteration

Any recursive function can be converted to a loop using a **stack**:

```python
# Recursive
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)

# Iterative equivalent
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

## Key Points

- Recursion: elegant, natural for tree/branching problems
- Iteration: faster, no stack limit, better for simple loops
- If you can write it clearly as a loop, prefer the loop
- If the problem is naturally recursive (trees, backtracking), use recursion
