# Encapsulation

Encapsulation means **controlling access** to an object's data. Instead of letting anyone change attributes directly, you provide controlled ways to read and modify them.

## Why Encapsulation?

Without encapsulation, anyone can set invalid data:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

acc = BankAccount(1000)
acc.balance = -999999  # No protection! Anyone can do this.
```

With encapsulation, you **protect** the data:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private — hidden from outside

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
```

## Access Levels in Python

Python uses **naming conventions** to signal access levels:

| Prefix | Name | Access Level | Example |
|--------|------|-------------|---------|
| (none) | Public | Anyone can access | `self.name` |
| `_` | Protected | "Please don't touch" (convention) | `self._name` |
| `__` | Private | Hard to access from outside | `self.__name` |

### Public Attributes

```python
self.name = "Trush"   # anyone can read and write
```

### Protected Attributes (`_`)

```python
self._name = "Trush"  # convention: "internal use, don't touch directly"
```

> The single underscore is just a **hint** — Python doesn't actually block access.

### Private Attributes (`__`)

```python
self.__name = "Trush"  # Python "mangles" the name to make it hard to access
```

> Python renames `__name` to `_ClassName__name` internally (name mangling).

## Getters and Setters

**Getter** = method to read a private attribute
**Setter** = method to write a private attribute with validation

```python
class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):         # getter
        return self._grade

    def set_grade(self, grade):  # setter with validation
        if grade in ["A", "B", "C", "D", "F"]:
            self._grade = grade
        else:
            print("Invalid grade!")
```

## Key Points

- **Encapsulation** = controlling access to object data
- **Public** (`name`) → accessible everywhere
- **Protected** (`_name`) → "internal use" convention
- **Private** (`__name`) → name-mangled, hard to access outside
- Use **getters/setters** to add validation when reading/writing data
- This protects your objects from invalid states
