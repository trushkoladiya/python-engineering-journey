# Defining Classes and Creating Objects

## Defining a Class

A **class** is a blueprint. You create one using the `class` keyword:

```python
class Dog:
    pass
```

- `class` — keyword to start a class definition
- `Dog` — the class name (use **CamelCase**: capitalize each word)
- `pass` — placeholder for an empty class body

## Class Naming Convention

| Style | Used For | Example |
|-------|----------|---------|
| `CamelCase` | Classes | `Dog`, `BankAccount`, `StudentRecord` |
| `snake_case` | Variables, functions | `my_dog`, `get_name()` |

## Creating Objects (Instantiation)

An **object** is a specific instance made from a class:

```python
class Dog:
    pass

my_dog = Dog()       # Create an object
another_dog = Dog()  # Create another object
```

- `Dog()` — calling the class creates a new object
- Each object is **independent** — they are separate instances

## Adding Data to Objects

You can attach **attributes** (data) to an object using dot notation:

```python
my_dog = Dog()
my_dog.name = "Buddy"
my_dog.age = 3

print(my_dog.name)  # "Buddy"
```

## Multiple Objects from One Class

Each object has its **own** copy of data:

```python
dog1 = Dog()
dog1.name = "Buddy"

dog2 = Dog()
dog2.name = "Max"

print(dog1.name)  # "Buddy"
print(dog2.name)  # "Max"
```

## Checking Object Type

```python
my_dog = Dog()
print(type(my_dog))        # <class '__main__.Dog'>
print(isinstance(my_dog, Dog))  # True
```

## Key Points

- Use `class ClassName:` to define a class (CamelCase)
- Use `ClassName()` to create an object (instantiation)
- Attach attributes with `object.attribute = value`
- Each object is independent — changing one doesn't affect others
- `type()` and `isinstance()` check an object's class
