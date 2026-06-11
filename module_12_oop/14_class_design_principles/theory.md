# Class Design Principles

Good classes aren't just about making code work — they're about making code **maintainable**, **reusable**, and **clear**.

## Single Responsibility Principle (SRP)

A class should do **one thing well**. If a class handles too many concerns, split it up.

### ❌ Bad: One class doing everything

```python
class UserManager:
    def create_user(self, name): ...
    def save_to_database(self, user): ...
    def send_email(self, user): ...
    def generate_report(self): ...
```

### ✅ Good: Each class has one job

```python
class User:
    def __init__(self, name): ...

class UserDatabase:
    def save(self, user): ...

class EmailService:
    def send_welcome(self, user): ...
```

## Keep Classes Focused

Ask: **"Can I describe this class in one sentence without using 'and'?"**

- ✅ `BankAccount` manages a single account's balance
- ❌ `BankAccount` manages balance **and** sends notifications **and** generates reports

## Favor Composition Over Inheritance

Instead of deep inheritance chains, **compose** objects:

```python
# Prefer this (composition):
class Car:
    def __init__(self):
        self.engine = Engine()
        self.gps = GPS()

# Over this (deep inheritance):
class Car(Vehicle, Machine, GPS, Engine):  # confusing!
    pass
```

## Keep `__init__` Simple

Initialize attributes, don't do heavy work:

```python
# Good
def __init__(self, name):
    self.name = name
    self.items = []

# Bad — too much logic in __init__
def __init__(self, filepath):
    self.data = open(filepath).read()  # file I/O in constructor!
```

## Key Principles Summary

| Principle | Rule |
|-----------|------|
| Single Responsibility | One class = one job |
| Clean Names | Class name should describe its purpose |
| Small Methods | Each method does one thing |
| Composition > Inheritance | Combine objects instead of deep hierarchies |
| Simple `__init__` | Initialize, don't compute |
| Encapsulate | Hide internal details |

## Key Points

- A well-designed class is **focused**, **simple**, and **reusable**
- One class = one responsibility
- Prefer composition over deep inheritance
- Keep methods small and focused
- Name classes and methods clearly
