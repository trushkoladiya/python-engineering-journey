# Nested Exception Handling

You can put `try-except` blocks **inside other `try-except` blocks** for layered error handling.

## Basic Nesting

```python
try:
    # Outer operation
    try:
        # Inner operation
        result = int("hello")
    except ValueError:
        print("Inner: caught ValueError")
except Exception:
    print("Outer: caught something else")
```

## Why Use Nesting?

When you have **multiple steps** and each can fail differently:

```python
try:
    file = open("data.txt", "r")
    try:
        content = file.read()
        number = int(content)
    except ValueError:
        print("File content is not a number")
    finally:
        file.close()
except FileNotFoundError:
    print("File not found")
```

- **Outer `try`** handles the file opening
- **Inner `try`** handles the file content processing
- **Inner `finally`** ensures the file is always closed

## How Exceptions Bubble Up

If an inner `except` **doesn't catch** the error, it moves to the outer `try-except`:

```python
try:
    try:
        result = 10 / 0
    except ValueError:     # Doesn't match ZeroDivisionError!
        print("Inner: ValueError")
except ZeroDivisionError:
    print("Outer: caught the ZeroDivisionError")
```

## Key Points

- Use nested `try-except` for **multi-step operations**
- Inner uncaught exceptions **bubble up** to outer handlers
- Use inner `finally` for cleanup of inner resources
- Don't nest too deeply — it becomes hard to read
