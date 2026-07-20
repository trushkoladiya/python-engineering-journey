# Advanced Class Patterns

These engineering-level patterns make your classes more powerful and elegant.

## Fluent Interface (Method Chaining)

Methods return `self` so you can chain calls:

```python
class Query:
    def __init__(self):
        self.filters = []

    def where(self, condition):
        self.filters.append(condition)
        return self     # return self for chaining!

    def limit(self, n):
        self._limit = n
        return self

q = Query().where("age > 18").where("active = True").limit(10)
```

**Key:** each method returns `self`.

## Immutable Objects

Objects whose state **cannot change** after creation. Safer, simpler, and thread-safe.

Using `__setattr__` to prevent modification:

```python
class Point:
    def __init__(self, x, y):
        super().__setattr__("x", x)
        super().__setattr__("y", y)

    def __setattr__(self, name, value):
        raise AttributeError("Point is immutable")
```

Or using `__slots__` + frozen logic.

## Named Tuple Alternative

For simple immutable data, `collections.namedtuple` is even easier:

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
# p.x = 3  → AttributeError
```

## Key Points

- **Fluent interfaces** = return `self` from methods for chaining
- **Immutable objects** = block `__setattr__` after `__init__`
- `namedtuple` is a quick way to create immutable data objects
- Immutable objects are safer and easier to reason about
- Choose the right pattern for your use case
