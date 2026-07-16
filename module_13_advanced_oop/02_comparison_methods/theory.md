# Comparison Dunder Methods — Deep Dive

In Module 12, you saw `__eq__` and `__lt__`. Now let's cover **all six** comparison operators and learn best practices.

## The Six Comparison Methods

| Method | Operator | Meaning |
|--------|----------|---------|
| `__eq__` | `==` | Equal to |
| `__ne__` | `!=` | Not equal to |
| `__lt__` | `<` | Less than |
| `__gt__` | `>` | Greater than |
| `__le__` | `<=` | Less than or equal |
| `__ge__` | `>=` | Greater than or equal |

## Basic Implementation

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __le__(self, other):
        return self.celsius <= other.celsius

    def __gt__(self, other):
        return self.celsius > other.celsius

    def __ge__(self, other):
        return self.celsius >= other.celsius

    def __ne__(self, other):
        return self.celsius != other.celsius
```

## The `@functools.total_ordering` Shortcut

Implementing all six is tedious. Define just `__eq__` and **one** of `__lt__`, `__gt__`, `__le__`, `__ge__`, and Python fills in the rest:

```python
from functools import total_ordering

@total_ordering
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius
```

Now `>`, `>=`, `<=`, and `!=` all work automatically!

## Type Checking

Always check the type of `other` to avoid errors:

```python
def __eq__(self, other):
    if not isinstance(other, Temperature):
        return NotImplemented
    return self.celsius == other.celsius
```

Returning `NotImplemented` tells Python to try the other object's method instead.

## Key Points

- Six comparison methods: `__eq__`, `__ne__`, `__lt__`, `__gt__`, `__le__`, `__ge__`
- Use `@functools.total_ordering` to only define `__eq__` + one other
- Always check `isinstance` and return `NotImplemented` for wrong types
- Implementing comparisons enables `sorted()` and `min()`/`max()`
