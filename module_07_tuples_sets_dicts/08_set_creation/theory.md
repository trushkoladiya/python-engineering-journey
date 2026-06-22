# Set Creation

A **set** is an unordered collection of **unique** elements. Sets automatically remove duplicates.

## Empty Set

You **must** use `set()` to create an empty set. `{}` creates an empty **dictionary**, not a set!

```python
empty = set()
print(empty)        # set()
print(type(empty))  # <class 'set'>

# This is a DICTIONARY, not a set!
not_a_set = {}
print(type(not_a_set))  # <class 'dict'>
```

## Set with Values

```python
numbers = {1, 2, 3, 4, 5}
print(numbers)   # {1, 2, 3, 4, 5}

fruits = {"apple", "banana", "cherry"}
print(fruits)    # order may vary!
```

## Automatic Duplicate Removal

Sets automatically remove duplicate values:

```python
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)   # {1, 2, 3, 4}

letters = {"a", "b", "a", "c", "b"}
print(letters)   # {'a', 'b', 'c'}
```

## Creating Sets from Lists

```python
my_list = [1, 2, 2, 3, 3, 4]
my_set = set(my_list)
print(my_set)   # {1, 2, 3, 4}
```

## Creating Sets from Strings

```python
chars = set("hello")
print(chars)   # {'h', 'e', 'l', 'o'}  — no duplicate 'l'
```

## Key Points

- Use `set()` for empty sets (not `{}`)
- Sets are **unordered** — no guaranteed order
- Sets contain only **unique** elements
- Duplicates are automatically removed
- Use `set()` to convert lists or strings to sets
