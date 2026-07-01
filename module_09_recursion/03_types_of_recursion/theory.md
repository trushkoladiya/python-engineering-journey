# Types of Recursion

There are different ways a function can call itself recursively.

## Direct Recursion

A function calls **itself** directly:

```python
def direct(n):
    if n <= 0: return
    direct(n - 1)   # Calls itself
```

## Indirect Recursion

Function A calls function B, and function B calls function A:

```python
def is_even(n):
    if n == 0: return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0: return False
    return is_even(n - 1)
```

## Tail Recursion

The recursive call is the **last** thing the function does — nothing happens after it returns:

```python
# Tail recursive — recursive call is the last operation
def factorial_tail(n, acc=1):
    if n <= 1: return acc
    return factorial_tail(n - 1, acc * n)

# NOT tail recursive — multiplication happens AFTER the call returns
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)   # n * ... happens after return
```

> **Note:** Python does NOT optimize tail recursion (unlike some other languages), but understanding it helps you write better recursive code.

## Key Points

- **Direct**: function calls itself
- **Indirect**: functions call each other in a cycle
- **Tail**: recursive call is the very last operation
- Python doesn't optimize tail recursion, but you can manually convert to loops
