# Binary & Base Representations

## Number Bases

We normally use **base 10** (decimal). Python can also show numbers in other bases.

## 1. Binary — `bin()` (Base 2)

Uses only digits `0` and `1`. Prefix: `0b`

```python
print(bin(10))   # 0b1010
print(bin(255))  # 0b11111111
```

## 2. Octal — `oct()` (Base 8)

Uses digits `0–7`. Prefix: `0o`

```python
print(oct(10))   # 0o12
print(oct(255))  # 0o377
```

## 3. Hexadecimal — `hex()` (Base 16)

Uses digits `0–9` and letters `a–f`. Prefix: `0x`

```python
print(hex(10))   # 0xa
print(hex(255))  # 0xff
```

## 4. Converting Back to Decimal

Use `int()` with the base:

```python
print(int("1010", 2))    # 10  (binary to decimal)
print(int("12", 8))      # 10  (octal to decimal)
print(int("a", 16))      # 10  (hex to decimal)
```

## 5. Writing Numbers in Other Bases

```python
x = 0b1010   # binary literal → 10
y = 0o12     # octal literal → 10
z = 0xa      # hex literal → 10
print(x, y, z)  # 10 10 10
```

## Key Points

| Function | Base | Prefix | Example |
|----------|------|--------|---------|
| `bin()` | 2 | `0b` | `bin(10)` → `0b1010` |
| `oct()` | 8 | `0o` | `oct(10)` → `0o12` |
| `hex()` | 16 | `0x` | `hex(10)` → `0xa` |

- Use `int(string, base)` to convert back to decimal
