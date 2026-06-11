# Decorators (Introduction)

A **decorator** is a function that takes another function and extends its behavior — without modifying the original function.

## What is a Decorator?

A decorator **wraps** a function to add extra behavior before or after it runs:

```python
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper
```

## The `@decorator` Syntax

Instead of manually wrapping, use the `@` syntax:

```python
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before the function
# Hello!
# After the function
```

This is the same as writing:

```python
say_hello = my_decorator(say_hello)
```

## Decorators with Arguments

To decorate functions that take parameters, use `*args` and `**kwargs`:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
```

## Common Use Cases

- Logging (print when a function is called)
- Timing (measure how long a function takes)
- Validation (check inputs before running)

## Key Points

- A decorator wraps a function to add behavior
- Use `@decorator_name` above a function definition
- The decorator takes a function and returns a new function
- Use `*args, **kwargs` to handle any parameters
- Advanced decorators (parameterized, stacking, class-based) are covered in Module 13
