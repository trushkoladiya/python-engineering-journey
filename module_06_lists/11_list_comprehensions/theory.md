# List Comprehensions

List comprehensions let you create lists in **one line** — clean, readable, and Pythonic.

## Basic List Comprehension

```python
# Traditional way:
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension way:
squares = [x ** 2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]
```

The syntax: `[expression for item in iterable]`

## Conditional List Comprehension

Add an `if` to filter elements:

```python
# Only even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8]
```

The syntax: `[expression for item in iterable if condition]`

## With `if-else`

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)   # ['even', 'odd', 'even', 'odd', 'even']
```

Note: `if-else` goes **before** `for`, but filter `if` goes **after** `for`.

## Nested List Comprehension (Intro)

```python
# Create a 3x3 matrix
matrix = [[0 for col in range(3)] for row in range(3)]
print(matrix)   # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

## Key Points

- `[expr for item in iterable]` — basic comprehension
- `[expr for item in iterable if cond]` — with filter
- `[a if cond else b for item in iterable]` — with if-else
- Replaces simple `for` + `append` patterns
- More readable for simple transformations
