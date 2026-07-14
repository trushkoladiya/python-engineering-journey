# Abstraction and Abstract Base Classes

Abstraction means **hiding complex details** and showing only what's necessary. You define **what** a class should do, without specifying **how**.

## The Concept

Think of a TV remote:
- You press "volume up" → volume increases
- You don't need to know the internal circuitry
- The **interface** (buttons) hides the **implementation** (electronics)

## Abstract Base Classes (ABC)

An **abstract class** defines methods that child classes **must** implement. You can't create objects from an abstract class directly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass       # no implementation — children MUST provide it

    @abstractmethod
    def perimeter(self):
        pass
```

- `ABC` — base class for abstract classes (from the `abc` module)
- `@abstractmethod` — marks a method as "must implement"
- You **cannot** create an instance of `Shape` directly

## Implementing an Abstract Class

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):              # MUST implement
        return self.width * self.height

    def perimeter(self):         # MUST implement
        return 2 * (self.width + self.height)
```

If you forget to implement an abstract method, Python raises a `TypeError`.

## Why Use Abstraction?

- **Enforces a contract** — all children must have certain methods
- **Prevents mistakes** — can't forget to implement required methods
- **Clean design** — defines a clear interface

## Key Points

- **Abstraction** = hide details, show only the interface
- Use `from abc import ABC, abstractmethod`
- Abstract classes **cannot be instantiated**
- Child classes **must implement** all abstract methods
- This ensures a consistent interface across related classes
