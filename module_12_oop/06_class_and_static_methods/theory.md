# Class Methods and Static Methods

Beyond instance methods, Python has two other types of methods: **class methods** and **static methods**.

## Class Methods (`@classmethod`)

A class method works with the **class itself**, not a specific object. It uses `cls` instead of `self`:

```python
class Dog:
    count = 0

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    @classmethod
    def get_count(cls):
        return f"Total dogs: {cls.count}"

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(Dog.get_count())  # "Total dogs: 2"
```

- Decorated with `@classmethod`
- First parameter is `cls` (the class, not an object)
- Can access/modify **class attributes** but not instance attributes
- Called on the class: `ClassName.method()`

## Static Methods (`@staticmethod`)

A static method is a **utility function** inside a class. It doesn't access `self` or `cls`:

```python
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(MathHelper.add(3, 5))     # 8
print(MathHelper.is_even(4))    # True
```

- Decorated with `@staticmethod`
- No `self` or `cls` parameter
- Can't access instance or class data
- Just a regular function organized inside a class

## When to Use What?

| Type | Decorator | First Param | Access | Use Case |
|------|-----------|-------------|--------|----------|
| Instance method | (none) | `self` | Object data | Most methods |
| Class method | `@classmethod` | `cls` | Class data | Factory methods, counters |
| Static method | `@staticmethod` | (none) | Nothing | Utility/helper functions |

## Key Points

- **Instance methods** → work with a specific object (`self`)
- **Class methods** → work with the class itself (`cls`)
- **Static methods** → independent helpers, no access to class/object
- Use `@classmethod` and `@staticmethod` decorators
