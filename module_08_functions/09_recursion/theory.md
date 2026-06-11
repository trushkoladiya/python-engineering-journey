# Recursion (Introduction)

A **recursive function** is a function that **calls itself**. It's a different way to repeat operations.

## Basic Concept

A recursive function needs two parts:
1. **Base case** — when to stop
2. **Recursive case** — the function calls itself with a simpler input

```python
def countdown(n):
    if n <= 0:           # Base case
        print("Go!")
        return
    print(n)
    countdown(n - 1)    # Recursive case

countdown(3)
# 3
# 2
# 1
# Go!
```

## Classic Example: Factorial

`5! = 5 × 4 × 3 × 2 × 1 = 120`

```python
def factorial(n):
    if n <= 1:           # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case

print(factorial(5))   # 120
```

## How It Works (Call Stack)

Each recursive call is placed on a "stack":

```
factorial(5) → 5 * factorial(4)
                   4 * factorial(3)
                       3 * factorial(2)
                           2 * factorial(1)
                               returns 1    ← base case
                           returns 2
                       returns 6
                   returns 24
               returns 120
```

## Key Points

- A recursive function calls itself
- Always needs a **base case** to stop
- Without a base case, you get infinite recursion (crash!)
- Each call uses memory (call stack)
- For beginners: loops are usually simpler; recursion is powerful for certain problems
