# Iterable Objects

An **iterable** is any object that can return its elements one at a time. Python has many built-in iterables.

## Built-in Iterables

| Type | Example | Iterable? |
|------|---------|-----------|
| List | `[1, 2, 3]` | ✅ Yes |
| Tuple | `(1, 2, 3)` | ✅ Yes |
| String | `"hello"` | ✅ Yes |
| Set | `{1, 2, 3}` | ✅ Yes |
| Dictionary | `{"a": 1}` | ✅ Yes (over keys) |
| Range | `range(10)` | ✅ Yes |
| File | `open("f.txt")` | ✅ Yes (over lines) |
| Integer | `42` | ❌ No |
| Float | `3.14` | ❌ No |

## How to Check if Something is Iterable

Use `iter()` — if it doesn't raise `TypeError`, it's iterable:

```python
iter([1, 2, 3])   # works — list is iterable
iter(42)           # TypeError — int is NOT iterable
```

Or check using `hasattr`:

```python
hasattr([1, 2, 3], "__iter__")  # True
hasattr(42, "__iter__")         # False
```

## Dictionary Iteration

Dictionaries iterate over **keys** by default:

```python
d = {"name": "Trush", "age": 21}

for key in d:           # keys
for val in d.values():  # values
for k, v in d.items():  # key-value pairs
```

## Key Points

- Most Python containers are iterable
- Numbers and booleans are NOT iterable
- Dictionaries iterate over keys by default
- Use `iter()` or `hasattr(__iter__)` to check iterability
