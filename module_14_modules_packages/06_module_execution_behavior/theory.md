# Module Execution Behavior: `__name__`

Every Python module has a special variable called `__name__`. Its value changes depending on **how** the module is used.

## The Two Modes

| Mode | `__name__` value |
|------|-----------------|
| Run directly (`python myfile.py`) | `"__main__"` |
| Imported (`import myfile`) | `"myfile"` (the module name) |

## The `if __name__ == "__main__":` Pattern

This is one of the most important patterns in Python:

```python
# calculator.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# This block ONLY runs when the file is executed directly
if __name__ == "__main__":
    print("Testing calculator:")
    print(add(3, 4))       # 7
    print(multiply(5, 6))  # 30
```

**When run directly:** The test code executes.
**When imported:** Only the functions are available — no test output.

## Why This Matters

Without this guard, importing a module would run ALL its code:

```python
# bad_module.py (no guard)
def greet(name):
    return f"Hello, {name}!"

print("This runs on EVERY import!")  # BAD — runs when imported
```

```python
# good_module.py (with guard)
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("This only runs when executed directly")  # GOOD
```

## Key Points

- `__name__` is `"__main__"` when a file is run directly
- `__name__` is the module name when a file is imported
- Use `if __name__ == "__main__":` to guard test/demo code
- This lets a file work both as a module AND as a script
