# reduce() — Aggregation Operations

`reduce()` takes an iterable and **reduces** it to a single value by applying a function cumulatively.

## Import

Unlike `map()` and `filter()`, `reduce()` must be imported:

```python
from functools import reduce
```

## How It Works

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
# Step by step:
# a=1, b=2 → 3
# a=3, b=3 → 6
# a=6, b=4 → 10
# a=10, b=5 → 15
```

The function takes **two arguments**:
- `a` = the accumulated result so far
- `b` = the next element

## With Initial Value

You can provide a starting value as the third argument:

```python
total = reduce(lambda a, b: a + b, numbers, 100)
# Starts at 100 instead of the first element
# Result: 115
```

## Common Uses

```python
# Product of all numbers
product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
# 120

# Find maximum
biggest = reduce(lambda a, b: a if a > b else b, [3, 1, 4, 1, 5])
# 5

# Flatten lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda a, b: a + b, nested)
# [1, 2, 3, 4, 5, 6]
```

## Key Points

- `reduce()` combines all elements into a single result
- Must import from `functools`
- Takes a two-argument function
- Optional third argument sets the initial value
- For simple sums/products, `sum()` and `math.prod()` are clearer
