# Identity Operators

Identity operators check whether two variables refer to the **same object in memory** — not just the same value.

## The Two Identity Operators

| Operator | Meaning | Returns |
|----------|---------|---------|
| `is` | Same object | `True` if same identity |
| `is not` | Different object | `True` if different identity |

## `is` vs `==`

This is a very important distinction:

- `==` checks if the **values** are equal
- `is` checks if they are the **exact same object** in memory

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)    # True  — same values
print(a is b)    # False — different objects in memory
```

## When `is` Returns True

When two variables point to the **same object**:

```python
a = [1, 2, 3]
b = a            # b points to the same object as a

print(a is b)    # True — same object
print(a == b)    # True — same values too
```

## Checking with `id()`

`id()` shows the memory address (learned in Module 2). Same `id` = same object.

```python
a = [1, 2, 3]
b = a
print(id(a) == id(b))   # True — same object
```

## `is not`

Checks if two variables are **not** the same object:

```python
x = [1, 2]
y = [1, 2]
print(x is not y)   # True — different objects
```

## Common Use: Checking for None

The most common use of `is` is checking for `None`:

```python
result = None
print(result is None)       # True
print(result is not None)   # False
```

Always use `is` (not `==`) when checking for `None`.

## Key Points

- `is` checks identity (same object), `==` checks equality (same value)
- Use `id()` to verify object identity
- Always use `is` when checking for `None`
- `is not` checks that objects are different
