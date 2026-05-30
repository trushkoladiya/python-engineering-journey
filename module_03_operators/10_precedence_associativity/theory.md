# Operator Precedence & Associativity (Deep)

When an expression has multiple operators, Python needs to decide **which operator runs first**. This is called **precedence**. When operators have the **same precedence**, **associativity** decides the direction.

## Full Precedence Table (High → Low)

| Priority | Operator | Description |
|----------|----------|-------------|
| 1 (highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `~`, `+x`, `-x` | Bitwise NOT, unary plus/minus |
| 4 | `*`, `/`, `//`, `%` | Multiplication, division, modulus |
| 5 | `+`, `-` | Addition, subtraction |
| 6 | `<<`, `>>` | Bitwise shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `in` | Comparisons |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 (lowest) | `or` | Logical OR |

## Associativity

When two operators have the **same precedence**, Python evaluates:

- **Left to right** (most operators)
- **Right to left** (only `**` and assignment `=`)

```python
# Left to right
print(10 - 5 + 3)     # 8  → (10 - 5) + 3

# Right to left (exponentiation)
print(2 ** 3 ** 2)     # 512 → 2 ** (3 ** 2) = 2 ** 9
```

## Parentheses Always Win

When in doubt, use parentheses. They make code clearer and override all precedence rules.

```python
print(2 + 3 * 4)       # 14 — multiplication first
print((2 + 3) * 4)     # 20 — parentheses first
```

## Mixing Logical and Comparison

```python
x = 5
# not > and > or (precedence order)
print(not x > 10 and x < 20)    # True
# Step 1: x > 10 → False
# Step 2: not False → True
# Step 3: x < 20 → True
# Step 4: True and True → True
```

## Key Points

- Parentheses `()` always have highest priority
- `**` is right-to-left, most others are left-to-right
- `not` > `and` > `or` for logical operators
- When in doubt, use parentheses for clarity
