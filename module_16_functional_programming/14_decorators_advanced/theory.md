# Decorators (Advanced Usage)

You learned basic decorators in Module 8 and advanced ones in Module 13. Now we'll use them in a **functional programming** context.

## Quick Recap

A decorator wraps a function to add behavior:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # do something before
        result = func(*args, **kwargs)
        # do something after
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}!"
```

## Multiple Decorators (Stacking)

Decorators apply **bottom to top**:

```python
@decorator_a
@decorator_b
def my_func():
    pass

# Same as: my_func = decorator_a(decorator_b(my_func))
```

## Parameterized Decorators

A decorator that takes arguments needs **three levels** of nesting:

```python
def repeat(n):
    def decorator(func):
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

## Preserving Function Identity

Use `functools.wraps` to keep the original function's name and docstring:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Key Points

- Stacking decorators applies them bottom to top
- Parameterized decorators need an extra level of nesting
- Always use `@wraps(func)` to preserve function identity
- Decorators are higher-order functions in disguise
