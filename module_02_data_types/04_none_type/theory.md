# None Type

## What is `None`?

`None` means **"no value"** or **"nothing"**. It is Python's way of saying empty/absent.

```python
result = None
print(result)       # None
print(type(result)) # <class 'NoneType'>
```

## When is `None` Used?

- When a variable has no value yet
- When something hasn't been assigned
- `print()` actually returns `None`

```python
x = None  # x exists, but has no meaningful value yet

value = print("hello")  # print() returns None
print(value)             # None
```

## Checking for `None`

Use `is` (not `==`) to check for None:

```python
x = None

print(x is None)      # True  ✅ correct way
print(x is not None)  # False
```

## `None` is Falsy

```python
print(bool(None))  # False
```

## Key Points

- `None` means "no value"
- There is only **one** `None` in Python
- Use `is None` to check (not `==`)
- `None` is falsy (`bool(None)` → `False`)
