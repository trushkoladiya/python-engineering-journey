# Metaclasses — Introduction

In Python, **everything is an object** — including classes themselves. A **metaclass** is the "class of a class."

## Classes Are Objects

When you write `class Dog: pass`, Python creates a **class object** called `Dog`. This object is created by a metaclass.

```python
class Dog:
    pass

print(type(Dog))    # <class 'type'>
print(type(42))     # <class 'int'>
```

- `type(42)` → `int` (42 is an instance of int)
- `type(Dog)` → `type` (Dog is an instance of type)

So `type` is the **default metaclass** — the class that creates other classes.

## Creating Classes with `type()`

You can create classes dynamically using `type()`:

```python
# Normal way:
class Dog:
    species = "Canis familiaris"
    def bark(self):
        return "Woof!"

# Equivalent using type():
Dog = type("Dog", (), {
    "species": "Canis familiaris",
    "bark": lambda self: "Woof!"
})
```

`type(name, bases, dict)`:
- `name` — class name
- `bases` — parent classes (tuple)
- `dict` — class attributes/methods

## Custom Metaclass (Basic)

A metaclass is a class that inherits from `type`:

```python
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Creating class: {name}")
        return super().__new__(mcs, name, bases, namespace)

class Dog(metaclass=MyMeta):
    pass
# Output: Creating class: Dog
```

## When to Use Metaclasses?

Almost never! They're for:
- Frameworks (Django, SQLAlchemy use them internally)
- Enforcing class conventions
- Auto-registering classes

> "If you're wondering whether you need metaclasses, you don't." — Most Python developers

## Key Points

- Classes are instances of `type` (the default metaclass)
- `type(name, bases, dict)` creates classes dynamically
- Custom metaclasses inherit from `type`
- Metaclasses control **class creation**, not instance creation
- Use sparingly — they add complexity
