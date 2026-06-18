# List Iteration

There are several ways to loop through a list in Python.

## Looping with `for`

The simplest way — iterate over each element:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## Using Index with `range()`

Access both the index and the element:

```python
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
```

## `enumerate()` — Index + Value Together

The cleanest way to get both index and value:

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

You can set a custom start number:

```python
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```

## Key Points

- `for item in list` — simple iteration
- `for i in range(len(list))` — when you need the index
- `for i, item in enumerate(list)` — best of both worlds
- `enumerate(list, start=1)` — start counting from 1
