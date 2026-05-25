# Boolean Type

## What is a Boolean?

A boolean has only two values: `True` or `False`.

```python
is_active = True
is_deleted = False
```

> Always capitalized: `True` and `False` — not `true` / `false`.

## 1. Truthy vs Falsy Values

Every value in Python can be treated as `True` or `False`.

### Falsy values (treated as `False`):

| Value | Type |
|-------|------|
| `False` | bool |
| `0` | int |
| `0.0` | float |
| `""` | str (empty) |
| `None` | NoneType |

### Truthy values (treated as `True`):

Everything else — any non-zero number, any non-empty string, etc.

```python
print(bool(0))       # False
print(bool(42))      # True
print(bool(""))      # False
print(bool("hello")) # True
```

## 2. Boolean Operations Preview

You can combine booleans with `and`, `or`, `not`.

```python
print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
```

> These will be covered in depth in Module 3 (Operators).

## 3. Booleans are Numbers

In Python, `True` is `1` and `False` is `0`.

```python
print(True + True)   # 2
print(True + 5)      # 6
print(False + 10)    # 10
```

## Key Points

- Only two values: `True` and `False`
- Zero/empty = Falsy, everything else = Truthy
- `bool()` converts any value to True/False
- `True` equals `1`, `False` equals `0`
