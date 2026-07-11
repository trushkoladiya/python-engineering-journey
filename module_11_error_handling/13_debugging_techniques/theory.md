# Debugging Techniques

When errors occur, Python gives you a **traceback**. Learning to read it is a critical skill.

## Reading a Traceback

A traceback shows the **chain of function calls** that led to the error:

```
Traceback (most recent call last):
  File "app.py", line 15, in main
    result = process(data)
  File "app.py", line 8, in process
    return calculate(value)
  File "app.py", line 3, in calculate
    return 100 / value
ZeroDivisionError: division by zero
```

### How to Read It

1. **Start at the bottom** — the last line shows the **error type and message**
2. **Look at the line above** — shows the **exact line of code** that failed
3. **Read upward** — shows the **call chain** (who called what)

## Key Parts of a Traceback

| Part | Meaning |
|------|---------|
| `File "app.py"` | Which file |
| `line 3` | Which line number |
| `in calculate` | Which function |
| `return 100 / value` | The actual code that failed |
| `ZeroDivisionError: division by zero` | What went wrong |

## Common Debugging Strategies

### 1. Print Debugging
Add `print()` statements to see values at each step:

```python
print(f"DEBUG: value = {value}")
```

### 2. Check Variable Types
Many errors come from unexpected types:

```python
print(f"DEBUG: type = {type(value)}")
```

### 3. Reproduce Minimally
Find the **smallest code** that triggers the error.

## Key Points

- Read tracebacks **bottom to top**
- The last line has the **error type and message**
- The lines above show the **call chain**
- Use `print()` debugging to inspect values
- Always check **types** when debugging TypeError
