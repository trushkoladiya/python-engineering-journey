# Security Basics

## Why Security Matters

Even a small Python script can have security vulnerabilities. Understanding common risks helps you write code that's harder to exploit.

## Never Trust User Input

The #1 rule of security: **treat all external input as potentially dangerous**.

```python
# DANGEROUS — user input executed as code
user_input = input("Enter expression: ")
eval(user_input)  # User could type: __import__('os').system('rm -rf /')

# SAFE — validate and restrict input
allowed_operators = set("0123456789+-*/ .()")
if all(c in allowed_operators for c in user_input):
    result = eval(user_input)
```

## Common Vulnerabilities

### 1. Code Injection
```python
# DANGEROUS
eval(user_input)
exec(user_input)

# SAFE — never eval/exec untrusted input
```

### 2. Path Traversal
```python
# DANGEROUS — user could request "../../etc/passwd"
filename = user_input
with open(f"/data/{filename}") as f:
    print(f.read())

# SAFE — validate the path
import os
safe_path = os.path.realpath(os.path.join("/data", filename))
if not safe_path.startswith("/data/"):
    raise ValueError("Invalid path!")
```

### 3. Pickle Deserialization
```python
# DANGEROUS — pickle can execute arbitrary code
import pickle
data = pickle.loads(untrusted_bytes)  # NEVER do this!

# SAFE — use JSON for untrusted data
import json
data = json.loads(untrusted_string)
```

## Input Validation

```python
def validate_age(value):
    if not isinstance(value, int):
        raise TypeError("Age must be an integer")
    if not 0 <= value <= 150:
        raise ValueError("Age must be between 0 and 150")
    return value
```

## Key Points

- **Never** use `eval()` or `exec()` with untrusted input
- **Never** unpickle data from untrusted sources
- **Always** validate and sanitize user input
- **Always** check file paths to prevent directory traversal
- Use **JSON** instead of **pickle** for external data
- Apply the **principle of least privilege** — don't give more access than needed
