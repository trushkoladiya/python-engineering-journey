# Custom Exceptions

You can create your **own exception types** to describe errors specific to your program.

## Why Custom Exceptions?

Built-in exceptions like `ValueError` are generic. Custom exceptions make your errors **specific and meaningful**:

```python
# Generic — what value was invalid?
raise ValueError("Invalid input")

# Specific — immediately clear what went wrong
raise InvalidAgeError("Age must be between 0 and 150")
```

## Creating a Custom Exception

A custom exception is a simple class that **inherits from `Exception`**:

```python
class InvalidAgeError(Exception):
    pass
```

> **Note:** This uses a `class` definition. You'll learn classes fully in Module 12. For now, just follow this **pattern** — it's a one-line template.

## Using a Custom Exception

```python
class NegativeNumberError(Exception):
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError(f"Cannot take square root of {n}")
    return n ** 0.5
```

## Custom Exception with a Message

The `Exception` base class already handles messages for you:

```python
class InvalidEmailError(Exception):
    pass

raise InvalidEmailError("Email must contain '@'")
```

You catch them just like built-in exceptions:

```python
try:
    raise InvalidEmailError("missing @")
except InvalidEmailError as e:
    print(f"Email error: {e}")
```

## Naming Convention

Custom exceptions should:
- End with `Error` (e.g., `InvalidAgeError`, `InsufficientFundsError`)
- Be descriptive of the specific problem

## Key Points

- Custom exceptions are classes that inherit from `Exception`
- They make your error messages **specific and clear**
- Follow the pattern: `class MyError(Exception): pass`
- Catch them just like any other exception
- Full OOP details come in Module 12 — for now, just use the pattern
