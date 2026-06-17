# List Operations

Python provides several built-in operations for lists, similar to strings.

## Concatenation (`+`)

Join two lists together:

```python
a = [1, 2, 3]
b = [4, 5, 6]
result = a + b
print(result)   # [1, 2, 3, 4, 5, 6]
```

## Repetition (`*`)

Repeat a list:

```python
zeros = [0] * 5
print(zeros)   # [0, 0, 0, 0, 0]

pattern = [1, 2] * 3
print(pattern)   # [1, 2, 1, 2, 1, 2]
```

## Membership (`in`, `not in`)

Check if an element exists in a list:

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("grape" in fruits)       # False
print("grape" not in fruits)   # True
```

## Length (`len()`)

Get the number of elements:

```python
nums = [10, 20, 30, 40]
print(len(nums))   # 4
```

## Key Points

- `+` joins two lists into a new list
- `*` repeats a list
- `in` / `not in` checks if an element exists
- `len()` returns the number of elements
