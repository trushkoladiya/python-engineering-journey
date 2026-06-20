# Tuple Creation

A **tuple** is an ordered collection of items, similar to a list — but **immutable** (cannot be changed after creation).

## Empty Tuple

```python
empty = ()
print(empty)       # ()
print(len(empty))  # 0
```

You can also use `tuple()`:

```python
empty = tuple()
print(empty)       # ()
```

## Single-Element Tuple (Important!)

You **must** include a trailing comma to create a single-element tuple:

```python
# This is a tuple
single = (42,)
print(type(single))   # <class 'tuple'>

# This is NOT a tuple — just an integer in parentheses
not_tuple = (42)
print(type(not_tuple))   # <class 'int'>
```

The comma is what makes it a tuple, not the parentheses.

## Multiple Elements

```python
numbers = (1, 2, 3, 4, 5)
print(numbers)   # (1, 2, 3, 4, 5)

fruits = ("apple", "banana", "cherry")
print(fruits)    # ('apple', 'banana', 'cherry')
```

## Mixed Data Types

Tuples can hold different types:

```python
mixed = (42, "hello", 3.14, True)
print(mixed)   # (42, 'hello', 3.14, True)
```

## Nested Tuples

Tuples can contain other tuples:

```python
nested = ((1, 2), (3, 4), (5, 6))
print(nested)      # ((1, 2), (3, 4), (5, 6))
print(nested[0])   # (1, 2)
```

## Creating Tuples from Other Types

```python
from_list = tuple([1, 2, 3])
print(from_list)   # (1, 2, 3)

from_string = tuple("Hello")
print(from_string)   # ('H', 'e', 'l', 'l', 'o')
```

## Key Points

- Use `()` to create a tuple
- A single-element tuple **needs a comma**: `(42,)`
- Tuples can hold any data type
- Tuples are **ordered** — items stay in the order you put them
- Tuples are **immutable** — once created, they cannot be changed
