# Call Stack Understanding

Understanding the **call stack** is key to understanding how recursion actually works.

## What is the Call Stack?

Every time a function is called, Python creates a **stack frame** — a block of memory storing:
- The function's local variables
- Where to return after the function finishes

These frames stack on top of each other like a pile of plates.

## Execution Flow

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

factorial(4)
```

The calls stack up, then resolve in reverse (LIFO — Last In, First Out):

```
Call:   factorial(4) → waits for factorial(3)
Call:     factorial(3) → waits for factorial(2)
Call:       factorial(2) → waits for factorial(1)
Call:         factorial(1) → returns 1        ← base case hit
Return:     factorial(2) → returns 2 * 1 = 2
Return:   factorial(3) → returns 3 * 2 = 6
Return: factorial(4) → returns 4 * 6 = 24
```

## Each Call Has Its Own Variables

Every recursive call gets its own copy of local variables:

```python
def show(n):
    print(f"n = {n}")   # Each call has its own 'n'
    if n <= 0:
        return
    show(n - 1)
```

## Key Points

- Each function call creates a new **stack frame**
- Frames are resolved in **reverse order** (LIFO)
- Each call has its own **separate** local variables
- Too many calls = **stack overflow** (RecursionError)
