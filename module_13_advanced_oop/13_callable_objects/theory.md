# Callable Objects — `__call__`

The `__call__` method lets you make an object **behave like a function**. You can "call" the object with parentheses: `obj()`.

## Basic `__call__`

```python
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"

hello = Greeter("Hello")
print(hello("Trush"))   # "Hello, Trush!"
print(hello("Rahul"))     # "Hello, Rahul!"
```

`hello("Trush")` calls `hello.__call__("Trush")`.

## Why Use `__call__`?

Callable objects can **maintain state** between calls, unlike regular functions:

```python
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

## Checking if Something is Callable

```python
print(callable(hello))     # True — has __call__
print(callable(42))        # False — no __call__
print(callable(print))     # True — functions are callable
```

## Use Cases

- **Stateful functions** — functions that remember data between calls
- **Configurable functions** — set up once, call many times
- **Replacing closures** — when you need more structure than a nested function

## Key Points

- `__call__` lets objects be called like functions: `obj()`
- Callable objects can have state (attributes)
- `callable(obj)` checks if an object has `__call__`
- Great for configurable or stateful function-like objects
