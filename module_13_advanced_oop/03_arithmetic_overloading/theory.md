# Arithmetic Operator Overloading — Deep Dive

Module 12 introduced `__add__` and `__sub__`. Now let's cover the **full set** of arithmetic operators and learn about **reflected** operators.

## Full Arithmetic Methods

| Method | Operator | Example |
|--------|----------|---------|
| `__add__` | `+` | `a + b` |
| `__sub__` | `-` | `a - b` |
| `__mul__` | `*` | `a * b` |
| `__truediv__` | `/` | `a / b` |
| `__floordiv__` | `//` | `a // b` |
| `__mod__` | `%` | `a % b` |
| `__pow__` | `**` | `a ** b` |
| `__neg__` | `-a` | Unary minus |
| `__abs__` | `abs(a)` | Absolute value |

## Reflected (Right-side) Operators

When `a + b` fails on `a`, Python tries `b.__radd__(a)`:

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):           # Money + something
        if isinstance(other, (int, float)):
            return Money(self.amount + other)
        return NotImplemented

    def __radd__(self, other):          # something + Money
        return self.__add__(other)

m = Money(100)
result = 50 + m   # int.__add__ fails → calls m.__radd__(50)
```

## In-Place Operators

Methods like `__iadd__` handle `+=`:

```python
def __iadd__(self, other):    # +=
    self.amount += other.amount
    return self
```

## Key Points

- Each arithmetic operator has a corresponding dunder method
- **Reflected** operators (`__radd__`, etc.) handle right-side operations
- **In-place** operators (`__iadd__`, etc.) handle `+=`, `-=`, etc.
- Always check types and return `NotImplemented` for unsupported types
- Implement `__neg__` and `__abs__` for unary operations
