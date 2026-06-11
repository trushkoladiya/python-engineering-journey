# filter() — Filtering Data

`filter()` selects elements from an iterable based on a **condition** (a function that returns `True` or `False`).

## Basic Syntax

```python
filter(function, iterable)
```

The function is called a **predicate** — it tests each element and returns `True` to keep it, `False` to discard it.

## Simple Examples

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8]

# Keep numbers greater than 4
big = list(filter(lambda x: x > 4, numbers))
# [5, 6, 7, 8]
```

## Predicate Functions

A **predicate** is a function that returns a boolean:

```python
def is_positive(x):
    return x > 0

data = [-3, -1, 0, 2, 5]
positives = list(filter(is_positive, data))
# [2, 5]
```

## filter() with None

Passing `None` as the function removes all **falsy** values:

```python
data = [0, 1, "", "hello", None, 42, False, True]
truthy = list(filter(None, data))
# [1, 'hello', 42, True]
```

## Key Points

- `filter()` keeps elements where the function returns `True`
- Returns a lazy iterator
- The function used is called a **predicate**
- `filter(None, iterable)` removes falsy values
- List comprehensions with `if` often achieve the same result
