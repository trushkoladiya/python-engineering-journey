# Multiple Exception Handling

Sometimes code can raise **different types** of errors. You can handle each one separately.

## Multiple except Blocks

Each `except` catches a **different** exception type:

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
```

**Python checks `except` blocks from top to bottom** and runs the **first one** that matches.

## Tuple-Based Exception Handling

Handle **multiple exceptions the same way** by using a tuple:

```python
try:
    # some risky code
    result = int("hello") / 0
except (ValueError, ZeroDivisionError):
    print("A number error occurred!")
```

This catches **either** `ValueError` **or** `ZeroDivisionError` with the same handler.

## When to Use Each

| Approach | Use When |
|----------|----------|
| Multiple `except` blocks | You need **different handling** for each error |
| Tuple `except` | You want the **same handling** for several errors |

## Key Points

- Use multiple `except` blocks for **different responses** to different errors
- Use a **tuple** `(Error1, Error2)` when you want the **same response**
- Order matters — put **specific** exceptions before **general** ones
- Only **one** `except` block runs per error
