# Raising Exceptions

You can **manually raise** exceptions using the `raise` keyword.

## The `raise` Keyword

```python
raise ValueError("Age cannot be negative")
```

This **immediately stops** execution and creates an exception, just like Python does internally.

## Why Raise Exceptions?

When your code detects an **invalid situation**, you should signal it clearly:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age
```

Without `raise`, you might return `None` or a magic value — which hides bugs.

## Raising with a Message

Always include a **descriptive message**:

```python
# Bad — no message
raise ValueError

# Good — clear message
raise ValueError("Expected a positive number, got -5")
```

## Re-raising Exceptions

Inside `except`, you can use bare `raise` to **re-raise** the caught exception:

```python
try:
    result = risky_operation()
except ValueError:
    print("Logging the error...")
    raise   # Re-raise the same exception
```

This is useful when you want to **log** or do cleanup, then let the error propagate.

## Key Points

- `raise` creates an exception manually
- Always include a **clear error message**
- Use `raise` to enforce **rules and constraints** in your code
- Bare `raise` in `except` re-raises the current exception
