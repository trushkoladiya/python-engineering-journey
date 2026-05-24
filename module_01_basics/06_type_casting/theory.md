# Type Casting

## What is Type Casting?

Type casting means **converting** a value from one type to another.

## 1. Casting Functions

| Function | What it does | Example |
|----------|-------------|---------|
| `int()` | Converts to integer | `int("10")` → `10` |
| `float()` | Converts to float | `float("3.14")` → `3.14` |
| `str()` | Converts to string | `str(42)` → `"42"` |
| `bool()` | Converts to boolean | `bool(1)` → `True` |

## 2. Explicit Casting (You Do It)

```python
age = int("21")        # String to Integer
text = str(100)        # Integer to String
price = float("19.99") # String to Float
x = float(5)           # Integer to Float → 5.0
```

## 3. Implicit Casting (Python Does It)

```python
result = 5 + 2.0   # int + float → float
print(result)       # 7.0
```

## 4. What `bool()` Returns

- Zero / empty = `False`
- Everything else = `True`

```python
bool(0)     # False
bool(1)     # True
bool("")    # False
bool("hi")  # True
```

## Key Points

- Use `int()`, `float()`, `str()`, `bool()` to convert types
- `int("3.14")` fails — use `float()` first
- Empty/zero values are `False`, everything else is `True`
