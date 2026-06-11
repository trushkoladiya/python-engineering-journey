# Tuple Methods

Tuples have only **two** built-in methods: `count()` and `index()`. This is because tuples are immutable — there are no methods to add, remove, or change elements.

## `count()` — Count Occurrences

Returns how many times a value appears in the tuple:

```python
numbers = (1, 2, 3, 2, 4, 2, 5)
print(numbers.count(2))   # 3
print(numbers.count(9))   # 0
```

## `index()` — Find Position

Returns the index of the **first** occurrence of a value:

```python
fruits = ("apple", "banana", "cherry", "banana")
print(fruits.index("banana"))    # 1 (first occurrence)
print(fruits.index("cherry"))    # 2
```

If the value is not found, it raises a `ValueError`:

```python
# fruits.index("mango")   # ValueError!
```

## `index()` with Start and End

You can search within a range:

```python
numbers = (10, 20, 30, 20, 40, 20)
print(numbers.index(20))        # 1 (first occurrence)
print(numbers.index(20, 2))     # 3 (search from index 2)
print(numbers.index(20, 4))     # 5 (search from index 4)
```

## Key Points

- Tuples have only **two** methods: `count()` and `index()`
- `count()` returns the number of times a value appears
- `index()` returns the position of the first occurrence
- Always check with `in` before using `index()` to avoid errors
