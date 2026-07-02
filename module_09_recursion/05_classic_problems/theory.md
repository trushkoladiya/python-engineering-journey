# Classic Problems

These fundamental problems build your recursive thinking muscles.

## Factorial

`n! = n × (n-1) × ... × 1`, with `0! = 1`

```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)
```

## Fibonacci

Each number is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8, 13...

```python
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Sum of Numbers

```python
def sum_to(n):
    if n <= 0: return 0
    return n + sum_to(n - 1)
```

## Power Calculation

```python
def power(base, exp):
    if exp == 0: return 1
    return base * power(base, exp - 1)
```

## Key Points

- These are the "building blocks" of recursive thinking
- Each follows the same pattern: base case + recursive case
- Practice these until they feel natural
