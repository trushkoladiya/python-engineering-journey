# Membership Operators

Membership operators check if a value **exists inside** a sequence (like a string, list, tuple, set, or dictionary).

## The Two Membership Operators

| Operator | Meaning | Returns |
|----------|---------|---------|
| `in` | Value is found | `True` if value is present |
| `not in` | Value is not found | `True` if value is absent |

## Using `in` with Strings

Check if a character or substring exists in a string:

```python
message = "Hello World"
print("Hello" in message)    # True
print("hello" in message)    # False (case-sensitive!)
print("xyz" in message)      # False
```

## Using `in` with Lists

```python
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)       # True
print(10 in numbers)      # False
```

## Using `not in`

```python
fruits = ["apple", "banana", "cherry"]
print("mango" not in fruits)    # True  (mango is not there)
print("apple" not in fruits)    # False (apple IS there)
```

## Using `in` with Tuples

```python
colors = ("red", "green", "blue")
print("red" in colors)     # True
print("yellow" in colors)  # False
```

## Using `in` with Dictionaries

With dictionaries, `in` checks the **keys** (not values):

```python
person = {"name": "Trush", "age": 21}
print("name" in person)     # True  (checks keys)
print("Trush" in person)    # False (doesn't check values)
```

## Key Points

- `in` checks if a value exists in a sequence
- `not in` checks if a value does NOT exist
- Works with strings, lists, tuples, sets, and dictionaries
- Case-sensitive for strings
- For dictionaries, checks **keys** only
