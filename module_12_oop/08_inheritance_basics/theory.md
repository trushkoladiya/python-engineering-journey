# Inheritance — Basics

Inheritance lets you create a **new class** based on an **existing class**. The new class gets all the attributes and methods of the parent class.

## The Idea

Instead of writing the same code twice, you **reuse** it:

```python
# Parent class (base class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Child class (derived class) — inherits from Animal
class Dog(Animal):
    def fetch(self):
        return f"{self.name} fetches the ball!"
```

- `Dog` **inherits** everything from `Animal`
- `Dog` can also add **its own** methods

## How to Inherit

Put the parent class name in parentheses:

```python
class Child(Parent):
    pass
```

## What Gets Inherited?

The child class gets:
- All **attributes** from the parent
- All **methods** from the parent
- The child can **add** new methods
- The child can **override** parent methods (change behavior)

## Using `super()`

To call the parent's `__init__` from the child:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # call parent's __init__
        self.breed = breed             # add new attribute
```

`super()` gives you access to the parent class's methods.

## Method Overriding

A child class can **replace** a parent method with its own version:

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):          # overrides Animal.speak()
        return "Woof!"
```

## Key Points

- **Inheritance** = child class gets parent's attributes and methods
- Syntax: `class Child(Parent):`
- Use `super().__init__()` to call parent's constructor
- Child can **add** new methods and attributes
- Child can **override** parent methods
- This promotes **code reuse** — don't repeat yourself (DRY)
