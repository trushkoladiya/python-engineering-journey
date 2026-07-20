# Advanced Decorators

Module 8 introduced basic decorators. Now let's cover **advanced patterns**: parameterized decorators, stacking, `functools.wraps`, and class-based decorators.

## Review: Basic Decorator

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")
```

## `functools.wraps` — Preserving Metadata

Without `wraps`, the decorated function loses its name and docstring:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)          # preserves func's name, docstring, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Parameterized Decorators

A decorator that **takes arguments** needs an extra layer:

```python
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")
```

## Stacking Decorators

Multiple decorators are applied **bottom-up**:

```python
@decorator_a
@decorator_b
def func():
    pass
# Same as: func = decorator_a(decorator_b(func))
```

## Class-Based Decorators

Use `__call__` to make a class work as a decorator:

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)
```

## Key Points

- Use `@wraps(func)` to preserve function metadata
- Parameterized decorators need three nested levels
- Decorators stack bottom-up
- Class-based decorators use `__call__` (good for stateful decorators)
- `@staticmethod`, `@classmethod`, `@property` are built-in decorators
