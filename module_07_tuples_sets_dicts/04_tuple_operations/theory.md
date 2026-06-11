# Tuple Operations

Tuples support several built-in operations for combining, repeating, and checking elements.

## Concatenation (`+`)

Joining two tuples creates a **new** tuple:

```python
a = (1, 2, 3)
b = (4, 5, 6)
result = a + b
print(result)   # (1, 2, 3, 4, 5, 6)
```

## Repetition (`*`)

Repeating a tuple creates a **new** tuple with copies:

```python
t = (1, 2, 3)
result = t * 3
print(result)   # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

## Membership (`in`, `not in`)

Check if an element exists:

```python
fruits = ("apple", "banana", "cherry")
print("apple" in fruits)      # True
print("mango" in fruits)      # False
print("mango" not in fruits)  # True
```

## Length (`len()`)

```python
numbers = (10, 20, 30, 40)
print(len(numbers))   # 4
```

## Min and Max

```python
numbers = (5, 2, 8, 1, 9)
print(min(numbers))   # 1
print(max(numbers))   # 9
```

## Sum

```python
numbers = (10, 20, 30)
print(sum(numbers))   # 60
```

## Key Points

- `+` concatenates tuples (creates a new tuple)
- `*` repeats a tuple
- `in` / `not in` checks membership
- `len()`, `min()`, `max()`, `sum()` work on tuples just like lists
