# Assertions

The `assert` statement is a **debugging tool** that checks if a condition is true. If the condition is false, it raises an `AssertionError`.

## Basic Syntax

```python
assert condition, "Error message"
```

If `condition` is `False`, Python raises:
```
AssertionError: Error message
```

If `condition` is `True`, nothing happens — the program continues.

## Simple Examples

```python
age = 25
assert age > 0, "Age must be positive"        # Passes — no error

age = -5
assert age > 0, "Age must be positive"        # Fails — AssertionError!
```

## When to Use assert

| Use `assert` for... | Use `raise` for... |
|---------------------|--------------------|
| Internal checks (debugging) | User input validation |
| Checking your own code's logic | Expected runtime errors |
| Conditions that should **never** be false | Conditions that **might** be false |

### Good uses:
```python
# Checking function preconditions during development
assert len(items) > 0, "List should never be empty here"
assert result >= 0, "Result should never be negative"
```

### Bad uses:
```python
# Don't use assert for user input — it can be disabled!
assert user_input != "", "Enter a value"   # Bad!
```

## Important: assert Can Be Disabled

Python can skip all `assert` statements when run with the `-O` flag:
```
python -O script.py    # All asserts are ignored!
```

This is why **assert should never be used for input validation** — only for internal debugging checks.

## Key Points

- `assert condition, "message"` checks a condition
- Raises `AssertionError` if the condition is `False`
- Use for **debugging and internal checks** only
- Never use for **user input validation** — use `raise` instead
- Assertions can be disabled with `python -O`
