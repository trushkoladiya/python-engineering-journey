# else and finally Blocks

The `try-except` structure has two optional blocks: `else` and `finally`.

## The `else` Block

Runs **only when NO exception occurs** in `try`.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"Result: {result}")   # Runs because no error happened
```

**Why use `else`?** It keeps the "success" code **separate** from the "risky" code. Only code that might fail goes in `try`.

## The `finally` Block

Runs **always** — whether an exception occurred or not.

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs — cleanup here!")
```

**Common use:** Closing resources, cleaning up temporary data.

## Full Structure

```python
try:
    # Risky code
except SomeException:
    # Handle error
else:
    # Runs if NO error
finally:
    # ALWAYS runs
```

## Execution Flow

| Scenario | try | except | else | finally |
|----------|-----|--------|------|---------|
| No error | ✓ runs | ✗ skipped | ✓ runs | ✓ runs |
| Error occurs | ✓ (partial) | ✓ runs | ✗ skipped | ✓ runs |

## Key Points

- `else` runs only when `try` succeeds — keeps success logic clean
- `finally` always runs — perfect for cleanup
- `finally` runs even if you `return` from inside `try` or `except`
