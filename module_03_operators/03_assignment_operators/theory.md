# Assignment Operators

Assignment operators store values in variables. You already know `=`, but Python has shorthand operators too.

## 1. Basic Assignment (`=`)

```python
x = 10       # x now holds 10
name = "Trush" # name now holds "Trush"
```

## 2. Multiple Assignment

Assign several variables in one line:

```python
a, b, c = 1, 2, 3
```

Same value to multiple variables:

```python
x = y = z = 0
```

## 3. Augmented Assignment Operators

These combine an operation with assignment — a shorthand.

| Operator | Meaning | Same As |
|----------|---------|---------|
| `+=` | Add and assign | `x = x + 5` |
| `-=` | Subtract and assign | `x = x - 5` |
| `*=` | Multiply and assign | `x = x * 5` |
| `/=` | Divide and assign | `x = x / 5` |
| `//=` | Floor divide and assign | `x = x // 5` |
| `%=` | Modulus and assign | `x = x % 5` |
| `**=` | Exponent and assign | `x = x ** 5` |

### How it works

```python
score = 100
score += 10    # same as: score = score + 10
print(score)   # 110

score -= 20    # same as: score = score - 20
print(score)   # 90
```

## Why Use Augmented Assignment?

- Shorter to write
- Easier to read
- Does the same thing as the long form

```python
# Long way
x = x + 1

# Short way (same result)
x += 1
```

## Key Points

- `=` assigns a value
- `+=`, `-=`, `*=`, etc. are shortcuts
- Multiple assignment lets you set several variables at once
