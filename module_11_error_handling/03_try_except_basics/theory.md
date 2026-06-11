# try-except Basics

The `try-except` block lets you **catch errors** and handle them instead of crashing.

## Basic Structure

```python
try:
    # Code that might fail
    result = 10 / 0
except:
    # Code that runs if an error occurs
    print("Something went wrong!")
```

**Flow:**
1. Python tries the code in `try`
2. If an error occurs, Python jumps to `except`
3. If no error, `except` is skipped

## Catching Specific Exceptions

Always catch **specific** exception types — this is a best practice.

```python
try:
    number = int("hello")
except ValueError:
    print("That's not a valid number!")
```

If a **different** exception occurs, it is **not caught**:

```python
try:
    number = int("hello")
except ZeroDivisionError:
    print("Division by zero!")
# This will NOT catch the ValueError — the program crashes!
```

## Why Specific Exceptions Matter

Using a bare `except:` catches **everything**, including bugs you didn't expect:

```python
# Bad — hides all errors
try:
    result = my_function()
except:
    pass    # Silently ignores ALL errors — very dangerous!

# Good — catches only what you expect
try:
    result = int(user_input)
except ValueError:
    print("Please enter a number.")
```

## Key Points

- `try` contains code that **might fail**
- `except` handles the error **if it happens**
- Always catch **specific** exception types
- Bare `except:` is dangerous — it hides bugs
