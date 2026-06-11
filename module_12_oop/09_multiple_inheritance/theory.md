# Multiple Inheritance and MRO

Python allows a class to inherit from **more than one** parent class. This is called **multiple inheritance**.

## Basic Multiple Inheritance

```python
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimmable):  # inherits from BOTH
    def quack(self):
        return "Quack!"

duck = Duck()
duck.fly()    # from Flyable
duck.swim()   # from Swimmable
duck.quack()  # its own
```

## Method Resolution Order (MRO)

When multiple parents have the **same method**, Python uses **MRO** to decide which one to call. The order is:

1. The child class itself
2. First parent (left to right)
3. Second parent
4. ... and so on

```python
class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A, B):   # A comes before B
    pass

obj = C()
obj.greet()  # "Hello from A" — A is checked first
```

## Checking MRO

```python
print(C.__mro__)
# (<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>)
```

## When to Use Multiple Inheritance

- Use it to **combine behaviors** (mixins)
- Keep parent classes **focused on one thing**
- Avoid complex inheritance chains — they get confusing

## Key Points

- `class Child(Parent1, Parent2):` — inherits from multiple parents
- MRO determines which method gets called (left to right)
- Use `ClassName.__mro__` to see the resolution order
- Keep it simple — prefer single inheritance when possible
- Multiple inheritance is best for combining small, focused behaviors
