# Dynamic Programming (Intro)

## What Is Dynamic Programming?

**Dynamic Programming (DP)** solves complex problems by breaking them into **overlapping subproblems** and storing results to avoid redundant computation.

## The Two Key Properties

### 1. Overlapping Subproblems
The same subproblem is solved **multiple times**. Example: Fibonacci.

```
fib(5) = fib(4) + fib(3)
fib(4) = fib(3) + fib(2)
fib(3) = fib(2) + fib(1)
```
Notice `fib(3)` is computed **twice**!

### 2. Optimal Substructure
The optimal solution contains optimal solutions to its subproblems.

## Two Approaches

### Memoization (Top-Down)
Solve recursively, but **cache** results:

```python
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

### Tabulation (Bottom-Up)
Build a table from the smallest subproblem up:

```python
def fib(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]
```

## Why It Matters

| Approach | Fibonacci(40) |
|----------|-------------|
| Naive recursion | ~1 billion calls |
| DP (memoization) | 40 calls |

## Key Points

- DP = recursion + memoization (or bottom-up tabulation)
- Look for overlapping subproblems and optimal substructure
- Two approaches: top-down (memoization) and bottom-up (tabulation)
- Transforms exponential solutions into polynomial ones
