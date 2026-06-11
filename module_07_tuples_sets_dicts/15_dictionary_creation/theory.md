# Dictionary Creation

A **dictionary** stores data as **key-value pairs**. Each key maps to a value, like a real dictionary maps words to definitions.

## Empty Dictionary

```python
empty = {}
print(empty)        # {}
print(type(empty))  # <class 'dict'>

# Or using dict()
empty2 = dict()
print(empty2)       # {}
```

## Dictionary with Values

```python
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print(person)
# {'name': 'Trush', 'age': 21, 'city': 'Mumbai'}
```

## Using `dict()` Constructor

```python
person = dict(name="Trush", age=21, city="Mumbai")
print(person)
```

## Mixed Value Types

Keys are usually strings, but values can be anything:

```python
data = {
    "name": "Trush",
    "age": 21,
    "scores": [90, 85, 92],
    "active": True,
}
print(data)
```

## Nested Dictionaries

```python
students = {
    "Trush": {"age": 21, "grade": "A"},
    "Rahul": {"age": 21, "grade": "B"},
}
print(students["Trush"])   # {'age': 21, 'grade': 'A'}
```

## Key Points

- Use `{}` or `dict()` to create a dictionary
- Data is stored as `key: value` pairs
- Keys must be **unique** and **immutable** (strings, numbers, tuples)
- Values can be any type
- Dictionaries are **ordered** (Python 3.7+)
