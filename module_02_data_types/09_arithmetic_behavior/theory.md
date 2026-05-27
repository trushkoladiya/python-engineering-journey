# Basic Arithmetic Behavior with Types

## 1. Type Promotion

When you mix `int` and `float` in math, Python **promotes** the result to `float`.

```python
print(5 + 2.0)     # 7.0  (int + float → float)
print(10 * 1.5)    # 15.0 (int * float → float)
print(type(5 + 2.0))  # <class 'float'>
```

**Rule**: `int` + `float` → always `float`

## 2. Division Types

Python has three division operators:

| Operator | Name | Result |
|----------|------|--------|
| `/` | True division | Always returns float |
| `//` | Floor division | Returns int (rounds down) |
| `%` | Modulo | Returns remainder |

```python
print(7 / 2)    # 3.5  (true division — always float)
print(7 // 2)   # 3    (floor division — rounds down)
print(7 % 2)    # 1    (remainder)
```

### Floor division rounds **down** (toward negative infinity)

```python
print(7 // 2)     # 3
print(-7 // 2)    # -4  (not -3!)
```

### True division always returns float

```python
print(10 / 2)     # 5.0  (even if it divides evenly)
print(type(10/2)) # <class 'float'>
```

## 3. Mixed Operations

```python
x = 10 + 3.0   # float
y = 5 * 2      # int
z = 5 / 1      # float (division always returns float)
```

## Key Points

- `int` + `float` → `float` (type promotion)
- `/` always returns `float`
- `//` returns floor (rounded down integer)
- `%` returns the remainder
- Floor division rounds toward negative infinity
