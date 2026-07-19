# Design Patterns — Introduction

Design patterns are **proven solutions** to common problems. Here are three fundamental patterns.

## 1. Singleton Pattern

Ensures only **one instance** of a class exists:

```python
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = Database()
db2 = Database()
print(db1 is db2)  # True — same object!
```

**Use when:** you need exactly one instance (config, logger, connection pool).

## 2. Factory Pattern

A method that **creates objects** without exposing the creation logic:

```python
class Animal:
    @staticmethod
    def create(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        raise ValueError(f"Unknown: {animal_type}")
```

**Use when:** creation logic is complex or you want to decouple creation from usage.

## 3. Strategy Pattern

Lets you **swap algorithms** at runtime by passing different strategy objects:

```python
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)
```

**Use when:** you need different behaviors that can be changed at runtime.

## Key Points

- **Singleton** = one instance only → global resources
- **Factory** = creates objects → decouples creation from usage
- **Strategy** = swappable behavior → flexibility at runtime
- Patterns are **tools**, not rules — use when they solve a real problem
- Don't over-apply patterns — keep it simple when possible
