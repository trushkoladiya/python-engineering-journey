# Special (Dunder) Methods

Python uses **special methods** (also called "dunder" methods because of the **d**ouble **under**scores) to define how objects behave with built-in operations.

## What are Dunder Methods?

Methods surrounded by double underscores: `__method__`. You've already seen `__init__`. Here are two more essential ones:

## `__str__` — Human-Readable String

Called by `print()` and `str()`. It defines how your object looks when printed:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (age {self.age})"

buddy = Dog("Buddy", 3)
print(buddy)  # "Buddy (age 3)" — instead of <Dog object at 0x...>
```

Without `__str__`, you get an ugly memory address.

## `__repr__` — Developer String

Called by `repr()` and in the Python shell. It should be **unambiguous** and ideally look like valid code:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

buddy = Dog("Buddy", 3)
print(repr(buddy))  # "Dog('Buddy', 3)"
```

## `__str__` vs `__repr__`

| Method | Called By | Purpose | Audience |
|--------|-----------|---------|----------|
| `__str__` | `print()`, `str()` | Readable output | End users |
| `__repr__` | `repr()`, shell | Unambiguous representation | Developers |

> **Tip:** If you define only one, define `__repr__`. Python uses it as a fallback for `__str__`.

## Other Useful Dunder Methods

| Method | What It Does |
|--------|-------------|
| `__len__` | Define `len(obj)` |
| `__add__` | Define `obj + other` |
| `__eq__` | Define `obj == other` |
| `__lt__` | Define `obj < other` |
| `__contains__` | Define `item in obj` |

## Key Points

- Dunder methods customize how objects work with Python's built-in features
- `__str__` → for `print()`, human-readable
- `__repr__` → for debugging, developer-readable
- Define `__repr__` at minimum — it's the fallback
- These methods make your classes feel like native Python types
