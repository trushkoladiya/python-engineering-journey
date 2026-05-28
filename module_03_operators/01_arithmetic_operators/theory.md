# Arithmetic Operators

Arithmetic operators perform math operations on numbers.

## All Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `3 * 7` | `21` |
| `/` | Division | `15 / 4` | `3.75` |
| `//` | Floor Division | `15 // 4` | `3` |
| `%` | Modulus | `15 % 4` | `3` |
| `**` | Exponentiation | `2 ** 3` | `8` |

## Division vs Floor Division

- `/` always returns a **float** — even when dividing evenly
- `//` returns the **whole part** (rounds down to the nearest integer)

```python
print(10 / 2)    # 5.0  (float!)
print(10 // 2)   # 5    (int)
print(7 / 2)     # 3.5
print(7 // 2)    # 3    (rounds down)
```

## Modulus (Remainder)

`%` gives the **remainder** after division.

```python
print(10 % 3)   # 1  (10 ÷ 3 = 3 remainder 1)
print(20 % 5)   # 0  (no remainder — divides evenly)
```

## Exponentiation

`**` raises a number to a power.

```python
print(2 ** 3)    # 8   (2 × 2 × 2)
print(5 ** 2)    # 25  (5 × 5)
print(9 ** 0.5)  # 3.0 (square root of 9)
```

## Operator Precedence (Order of Execution)

Python follows standard math order:

1. `**` — exponentiation (highest)
2. `*`, `/`, `//`, `%` — multiplication, division
3. `+`, `-` — addition, subtraction (lowest)

Use **parentheses** `()` to control the order.

```python
print(2 + 3 * 4)     # 14  (multiplication first)
print((2 + 3) * 4)   # 20  (parentheses first)
```

## Key Points

- `/` always returns a float
- `//` rounds down to the nearest whole number
- `%` gives the remainder
- `**` is exponentiation
- Use `()` to control order of operations
