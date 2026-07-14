# Polymorphism

Polymorphism means **"many forms"** — the same method name behaves **differently** depending on the object calling it.

## Method Overriding (Polymorphism via Inheritance)

Different child classes can have the same method name but **different behavior**:

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Same method name, different results
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # each object decides its own behavior
```

## Why Polymorphism Matters

You can write code that works with **any** object that has the right method, without caring about the specific class:

```python
def make_speak(animal):
    print(animal.speak())  # works with any object that has speak()

make_speak(Dog())   # "Woof!"
make_speak(Cat())   # "Meow!"
```

## Operator Overloading (Intro)

You can define how operators (`+`, `-`, `==`, etc.) work with your objects using special methods:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):         # defines +
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):          # defines ==
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2     # calls __add__
print(p3.x, p3.y)  # 4, 6
```

| Operator | Special Method |
|----------|---------------|
| `+` | `__add__` |
| `-` | `__sub__` |
| `==` | `__eq__` |
| `<` | `__lt__` |
| `len()` | `__len__` |

## Key Points

- **Polymorphism** = same method name, different behavior per class
- Works through **method overriding** in child classes
- Lets you write flexible code that works with any compatible object
- **Operator overloading** lets you use `+`, `==`, etc. with your own objects
- Uses special (dunder) methods like `__add__`, `__eq__`
