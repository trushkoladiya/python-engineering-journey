# Exception Object Handling

When you catch an exception, you can **capture it as a variable** to access its details.

## The `as` Keyword

```python
try:
    number = int("hello")
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: invalid literal for int() with base 10: 'hello'
```

The variable `e` holds the **exception object**. You can:
- Print its message
- Check its type
- Store it for logging

## Accessing Exception Details

### The Error Message

```python
except ValueError as e:
    message = str(e)           # Convert to string
    print(f"Message: {message}")
```

### The Exception Type

```python
except Exception as e:
    error_type = type(e).__name__    # e.g., "ValueError"
    print(f"Type: {error_type}")
```

### The Arguments

Every exception stores its arguments in `.args`:

```python
except ValueError as e:
    print(e.args)    # Tuple of arguments: ('invalid literal...',)
```

## Catching a General Exception

You can catch `Exception` to handle **any** error — useful for logging:

```python
try:
    risky_code()
except Exception as e:
    print(f"{type(e).__name__}: {e}")
```

> **Warning:** Only do this when you need to **log everything**. For normal handling, catch specific types.

## Key Points

- Use `as e` to capture the exception object
- `str(e)` gives the error message
- `type(e).__name__` gives the exception class name
- `e.args` gives the raw arguments tuple
- Capture exceptions for logging and debugging
