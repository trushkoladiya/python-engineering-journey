# Lambda Functions

A **lambda** is a small, anonymous (unnamed) function written in a single line.

## Syntax

```python
lambda parameters: expression
```

It's equivalent to a one-line function:

```python
# Regular function
def double(x):
    return x * 2

# Lambda equivalent
double = lambda x: x * 2
```

## Single-Expression Functions

Lambdas can only have **one expression** — no statements, no loops, no multi-line logic:

```python
square = lambda x: x * x
add = lambda a, b: a + b

print(square(5))    # 25
print(add(3, 4))    # 7
```

## Common Use Cases

Lambdas are most useful as short, throwaway functions:

```python
# Sorting by custom key
names = ["Charlie", "Trush", "Rahul"]
names.sort(key=lambda x: len(x))
print(names)   # ['Trush', 'Rahul', 'Charlie']

# Sorting tuples by second element
students = [("Trush", 85), ("Rahul", 92), ("Charlie", 78)]
students.sort(key=lambda x: x[1])
```

## Key Points

- `lambda` creates a small, unnamed function
- Can only have **one expression** (no statements)
- Useful for short, simple operations
- Often used with `sort()`, `sorted()`, `map()`, `filter()`
- For complex logic, use a regular `def` function instead
