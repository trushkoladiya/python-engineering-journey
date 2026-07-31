# map() — Applying Functions to Iterables

`map()` applies a function to **every item** in an iterable, returning a new iterable of results.

## Basic Syntax

```python
map(function, iterable)
```

It returns a **map object** (lazy iterator), not a list. Convert it with `list()` when needed.

## Simple Examples

```python
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

# Using a named function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
# [2, 4, 6, 8, 10]
```

## map() with Multiple Iterables

```python
a = [1, 2, 3]
b = [10, 20, 30]

sums = list(map(lambda x, y: x + y, a, b))
# [11, 22, 33]
```

## map() vs List Comprehension

```python
# These do the same thing:
result1 = list(map(lambda x: x * 2, numbers))
result2 = [x * 2 for x in numbers]
```

| Feature | map() | List Comprehension |
|---------|-------|--------------------|
| Style | Functional | Pythonic |
| Readability | With named functions | With simple expressions |
| Laziness | Yes (returns iterator) | No (creates list) |

## Key Points

- `map()` transforms every element using a function
- Returns a **lazy iterator** (processes one item at a time)
- Works with lambda or named functions
- Can take multiple iterables
- List comprehensions are often more Pythonic for simple cases
