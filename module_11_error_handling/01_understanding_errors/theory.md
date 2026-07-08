# Understanding Errors

Every programmer encounters errors. Understanding the **types** of errors helps you fix them faster.

## Three Types of Errors

### 1. Syntax Errors

The code **breaks Python's grammar rules**. Python catches these **before** running.

```python
# Missing colon
if True
    print("hello")
# SyntaxError: expected ':'
```

```python
# Unclosed parenthesis
print("hello"
# SyntaxError: unexpected EOF
```

### 2. Runtime Errors (Exceptions)

The code is valid Python, but something **goes wrong during execution**.

```python
result = 10 / 0         # ZeroDivisionError
name = int("hello")     # ValueError
```

These are called **exceptions** — Python "raises" them when it can't continue.

### 3. Logical Errors

The code runs **without crashing**, but gives the **wrong result**.

```python
# Bug: should be (a + b) / 2, not a + b / 2
average = 10 + 20 / 2   # Gives 20.0, not 15.0
```

Python can't detect logical errors — only **you** can, by testing your code.

## Syntax Errors vs Exceptions

| Feature | Syntax Error | Exception |
|---------|-------------|-----------|
| When caught | Before running | During running |
| Can you handle it? | No — must fix the code | Yes — with `try/except` |
| Example | `if True` (no colon) | `10 / 0` |

## Key Points

- **Syntax errors** = bad grammar → fix the code
- **Runtime errors** = exceptions → can be handled
- **Logical errors** = wrong results → test your code
- This module focuses on **runtime errors (exceptions)**
