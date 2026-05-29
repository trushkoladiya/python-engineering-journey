# Bitwise Operators

Bitwise operators work on numbers at the **binary (bit) level**. They operate on individual bits (0s and 1s).

## Understanding Binary First

Every number is stored as binary in the computer:

```python
# Decimal → Binary
# 5  → 101
# 3  → 011
# 10 → 1010
```

You can see binary with `bin()` (learned in Module 2):

```python
print(bin(5))    # 0b101
print(bin(10))   # 0b1010
```

## All Bitwise Operators

| Operator | Name | Description |
|----------|------|-------------|
| `&` | AND | 1 if both bits are 1 |
| `\|` | OR | 1 if at least one bit is 1 |
| `^` | XOR | 1 if bits are different |
| `~` | NOT | Flips all bits |
| `<<` | Left shift | Shifts bits left (multiplies by 2) |
| `>>` | Right shift | Shifts bits right (divides by 2) |

## Bitwise AND (`&`)

Each bit is 1 only if **both** corresponding bits are 1.

```python
# 5 = 101
# 3 = 011
# ------
# & = 001 = 1
print(5 & 3)   # 1
```

## Bitwise OR (`|`)

Each bit is 1 if **at least one** corresponding bit is 1.

```python
# 5 = 101
# 3 = 011
# ------
# | = 111 = 7
print(5 | 3)   # 7
```

## Bitwise XOR (`^`)

Each bit is 1 if the bits are **different**.

```python
# 5 = 101
# 3 = 011
# ------
# ^ = 110 = 6
print(5 ^ 3)   # 6
```

## Bitwise NOT (`~`)

Flips all bits. Result is `-(n + 1)`.

```python
print(~5)    # -6
print(~0)    # -1
```

## Left Shift (`<<`) and Right Shift (`>>`)

- `<<` shifts bits left — equivalent to multiplying by 2
- `>>` shifts bits right — equivalent to dividing by 2

```python
print(5 << 1)    # 10  (5 × 2)
print(5 << 2)    # 20  (5 × 4)
print(20 >> 1)   # 10  (20 ÷ 2)
print(20 >> 2)   # 5   (20 ÷ 4)
```

## Key Points

- Bitwise operators work on binary representations
- `&` = AND, `|` = OR, `^` = XOR, `~` = NOT
- `<<` multiplies by powers of 2
- `>>` divides by powers of 2
- These are advanced but useful in certain situations
