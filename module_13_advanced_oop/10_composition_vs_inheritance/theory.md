# Composition vs Inheritance — Deep Design

Module 12 covered both. Now let's learn **when to choose each** and avoid common pitfalls.

## The Two Relationships

| Approach | Question | Example |
|----------|---------|---------|
| **Inheritance** | "Is it a ___?" | A Dog **is a** Animal |
| **Composition** | "Has it a ___?" | A Car **has a** Engine |

## When Inheritance Goes Wrong

Deep inheritance creates **fragile, tightly-coupled** code:

```python
# BAD — too many levels, hard to change
class Animal:
    ...
class Mammal(Animal):
    ...
class DomesticMammal(Mammal):
    ...
class Dog(DomesticMammal):
    ...
class GoldenRetriever(Dog):
    ...
```

Changing `Animal` can break everything below it.

## Favor Composition

Instead of inheriting behavior, **contain** objects that provide behavior:

```python
# GOOD — flexible and modular
class Engine:
    def start(self): ...

class GPS:
    def navigate(self, dest): ...

class Car:
    def __init__(self):
        self.engine = Engine()   # has-a
        self.gps = GPS()         # has-a
```

## Rules of Thumb

- Use **inheritance** when there's a true "is-a" relationship AND shared behavior
- Use **composition** when you want to combine behaviors from multiple sources
- Use **composition** when the relationship might change
- Prefer **shallow** hierarchies (1–2 levels max)

## Key Points

- **Inheritance** = "is-a" (use sparingly, keep it shallow)
- **Composition** = "has-a" (flexible, modular, preferred)
- Deep inheritance = fragile code
- Composition lets you swap parts easily
- When in doubt, choose composition
