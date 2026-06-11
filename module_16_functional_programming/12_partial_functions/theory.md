# Partial Functions — `functools.partial`

`functools.partial` lets you **pre-fill some arguments** of a function, creating a new, simpler function.

## Basic Syntax

```python
from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)    # pre-fill a=2
print(double(5))   # multiply(2, 5) → 10
```

## How It Works

`partial(func, arg1, arg2, ...)` creates a new function where the first arguments are already set:

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))   # 25
print(cube(5))     # 125
```

## Practical Uses

```python
# Pre-configure a formatter
format_price = partial("{:.2f}".format)
print(format_price(9.9))    # "9.90"

# Pre-configure a sort
from functools import partial

sort_desc = partial(sorted, reverse=True)
print(sort_desc([3, 1, 4]))   # [4, 3, 1]
```

## Key Points

- `partial` "freezes" some arguments of a function
- Creates a new callable with fewer required arguments
- Useful for creating specialized versions of general functions
- Often cleaner than lambda for simple argument binding
- Import from `functools`
