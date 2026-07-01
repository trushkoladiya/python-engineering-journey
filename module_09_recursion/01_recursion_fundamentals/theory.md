# Recursion Fundamentals (Deep Dive)

In Module 8, we learned the basics of recursion. Now we go deeper — understanding **how** and **why** recursion works.

## The Recursive Thinking Pattern

Recursion solves a problem by:
1. **Breaking it** into a smaller version of the same problem
2. **Solving** the smallest version directly (base case)
3. **Combining** the results back up

```python
def sum_to(n):
    if n <= 0:           # Base case: smallest problem
        return 0
    return n + sum_to(n - 1)   # Break into smaller problem
```

Think of it like Russian nesting dolls — each doll contains a smaller one until you reach the smallest.

## Structure of a Recursive Function

Every recursive function has exactly **two parts**:

```python
def recursive_function(input):
    # 1. BASE CASE — when to stop
    if input is the simplest case:
        return simple answer

    # 2. RECURSIVE CASE — break down and self-call
    return combine(input, recursive_function(smaller_input))
```

## Multiple Base Cases

Some problems need more than one base case:

```python
def fibonacci(n):
    if n == 0: return 0    # Base case 1
    if n == 1: return 1    # Base case 2
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Key Points

- Recursion = solving a problem by solving smaller versions of itself
- Every recursive function needs: base case + recursive case
- The recursive call must move **toward** the base case
- Think: "If I had the answer for a smaller input, how do I build the full answer?"
