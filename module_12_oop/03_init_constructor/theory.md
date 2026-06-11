# The `__init__` Method (Constructor)

Adding attributes *after* creating an object is messy. The `__init__` method lets you set up attributes **automatically** when an object is created.

## What is `__init__`?

`__init__` is a **special method** (called a constructor) that runs automatically when you create an object:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

buddy = Dog("Buddy", 3)  # __init__ runs automatically
print(buddy.name)  # "Buddy"
```

## Understanding `self`

`self` refers to the **specific object being created**:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name   # attach 'name' to THIS object
        self.age = age     # attach 'age' to THIS object
```

- `self` is always the **first parameter** of `__init__`
- You don't pass it when creating an object — Python does it automatically
- `self.name = name` means "save the `name` argument as this object's attribute"

## Default Values

You can give parameters default values:

```python
class Dog:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

puppy = Dog("Max")       # age defaults to 1
old_dog = Dog("Rex", 10) # age is 10
```

## Setting Up Computed Attributes

`__init__` can set attributes that aren't parameters:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height  # computed in __init__
```

## Key Points

- `__init__` runs **automatically** when you create an object
- `self` = the object being created
- Use `self.attribute = value` to save data on the object
- You can use default values for optional parameters
- `__init__` replaces manually adding attributes after creation
