# List Creation

A **list** is an ordered collection of items. Lists are one of the most important data types in Python.

## Empty List

```python
my_list = []
print(my_list)      # []
print(len(my_list)) # 0
```

## List with Values

```python
numbers = [1, 2, 3, 4, 5]
print(numbers)   # [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "cherry"]
print(fruits)    # ['apple', 'banana', 'cherry']
```

## Mixed Data Types

A list can hold **different types** of values:

```python
mixed = [42, "hello", 3.14, True]
print(mixed)   # [42, 'hello', 3.14, True]
```

## Nested Lists (Intro)

A list can contain **other lists**:

```python
nested = [[1, 2], [3, 4], [5, 6]]
print(nested)       # [[1, 2], [3, 4], [5, 6]]
print(nested[0])    # [1, 2]
```

## Creating Lists from Strings

You can use `list()` to convert a string into a list of characters:

```python
chars = list("Hello")
print(chars)   # ['H', 'e', 'l', 'l', 'o']
```

## Key Points

- Use `[]` to create a list
- Lists can hold any data type — numbers, strings, booleans, even other lists
- Lists are **ordered** — items stay in the order you put them
- Use `list()` to convert other sequences to lists
