# Instance Methods

Methods are **functions that belong to a class**. Instance methods operate on a specific object's data.

## What is an Instance Method?

An instance method is a function defined inside a class that uses `self` to access the object's data:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def get_info(self):
        return f"{self.name}, age {self.age}"

buddy = Dog("Buddy", 3)
print(buddy.bark())      # "Buddy says: Woof!"
print(buddy.get_info())  # "Buddy, age 3"
```

## The `self` Parameter

- `self` is the **first parameter** of every instance method
- It refers to the **specific object** calling the method
- Python passes it automatically — you don't provide it when calling

```python
buddy.bark()   # Python translates this to: Dog.bark(buddy)
```

## Methods That Modify the Object

Methods can **change** the object's attributes:

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0
```

## Methods That Return Values

Methods can **return** computed results:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

## Methods Calling Other Methods

Methods can call other methods using `self`:

```python
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, n):
        self.value += n

    def double(self):
        self.add(self.value)  # calls another method
```

## Key Points

- Instance methods are functions defined inside a class
- Always include `self` as the first parameter
- Use `self.attribute` to access/modify the object's data
- Methods can return values, modify data, or call other methods
- Call with `object.method()` — Python passes `self` automatically
