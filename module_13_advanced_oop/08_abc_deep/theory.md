# Abstract Base Classes — Deep Dive

Module 12 introduced `ABC` and `@abstractmethod`. Now let's explore **advanced patterns**: abstract properties, abstract class methods, and designing contracts.

## Review: Basic ABC

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

## Abstract Properties

Combine `@property` with `@abstractmethod`:

```python
class Shape(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

class Circle(Shape):
    @property
    def name(self):
        return "Circle"
```

## Abstract Class Methods

```python
class Serializable(ABC):
    @classmethod
    @abstractmethod
    def from_string(cls, data):
        pass
```

## Designing Contracts

ABCs define a **contract** — "any class that inherits from me MUST implement these methods." This lets you write code that works with **any** conforming class:

```python
def calculate_total_area(shapes):
    # Works with ANY list of Shape subclasses
    return sum(s.area() for s in shapes)
```

## `__subclasshook__` — Custom isinstance

You can make `isinstance()` work even without inheritance:

```python
class Drawable(ABC):
    @classmethod
    def __subclasshook__(cls, C):
        if any("draw" in B.__dict__ for B in C.__mro__):
            return True
        return NotImplemented
```

## Key Points

- `@property` + `@abstractmethod` = abstract property
- `@classmethod` + `@abstractmethod` = abstract class method
- ABCs define **contracts** for consistent interfaces
- `__subclasshook__` enables structural (duck-type) checking
- ABCs are great for framework and library design
