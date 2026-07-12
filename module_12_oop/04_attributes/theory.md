# Instance Attributes vs Class Attributes

There are two kinds of attributes in Python classes:
- **Instance attributes** — unique to each object
- **Class attributes** — shared by ALL objects of that class

## Instance Attributes

Defined inside `__init__` using `self.attribute`. Each object gets its **own copy**:

```python
class Dog:
    def __init__(self, name):
        self.name = name   # instance attribute — different for each dog

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(dog1.name)  # "Buddy"
print(dog2.name)  # "Max"
```

## Class Attributes

Defined **directly inside the class** (outside `__init__`). Shared by **all** objects:

```python
class Dog:
    species = "Canis familiaris"  # class attribute — same for ALL dogs

    def __init__(self, name):
        self.name = name          # instance attribute — unique per dog

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(dog1.species)  # "Canis familiaris"
print(dog2.species)  # "Canis familiaris" — same!
```

## Key Difference

| Feature | Instance Attribute | Class Attribute |
|---------|-------------------|-----------------|
| Defined in | `__init__` with `self.` | Directly in class body |
| Belongs to | One specific object | The class (shared) |
| Changing it | Affects only that object | Affects all objects |
| Use case | Data unique to each object | Data common to all objects |

## Dynamic Attribute Assignment

You can add new attributes to an object **at any time**:

```python
dog = Dog("Buddy")
dog.color = "golden"   # new attribute added dynamically
```

This only affects **that specific object**, not the class or other objects.

## Key Points

- **Instance attributes** (`self.x` in `__init__`) → unique per object
- **Class attributes** (in class body) → shared by all objects
- Class attributes are useful for constants or counters
- You can add attributes dynamically, but `__init__` is preferred
