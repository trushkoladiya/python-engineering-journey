# Type Checking

## 1. `type()` — What Type Is This?

`type()` returns the exact type of a value.

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
print(type(None))     # <class 'NoneType'>
```

### Comparing types

```python
x = 42
print(type(x) == int)    # True
print(type(x) == str)    # False
```

## 2. `isinstance()` — Is This a Type?

`isinstance()` checks if a value **is** a certain type. Returns `True` or `False`.

```python
x = 42
print(isinstance(x, int))    # True
print(isinstance(x, str))    # False
print(isinstance(x, float))  # False
```

### Why `isinstance()` is better

`isinstance()` also recognizes related types:

```python
print(isinstance(True, bool))  # True
print(isinstance(True, int))   # True — bool is a subtype of int!

print(type(True) == int)       # False — type() is strict
```

### Checking multiple types

```python
x = 3.14
print(isinstance(x, (int, float)))  # True — is it int OR float?
```

## Key Points

| Tool | Use For | Example |
|------|---------|---------|
| `type()` | Get exact type | `type(42)` → `<class 'int'>` |
| `isinstance()` | Check if value is a type | `isinstance(42, int)` → `True` |

- Prefer `isinstance()` for checking types
- `type()` for inspecting/debugging
