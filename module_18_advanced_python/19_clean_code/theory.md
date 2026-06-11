# Clean Code & Architecture

## What Is Clean Code?

Clean code is code that is **easy to read**, **easy to change**, and **easy to understand** — even months later or by someone else.

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." — Martin Fowler

## Readability Rules

### 1. Meaningful Names
```python
# Bad
x = 3600
d = {}
def f(l):
    return [i for i in l if i > 0]

# Good
SECONDS_PER_HOUR = 3600
user_scores = {}
def get_positive_numbers(numbers):
    return [n for n in numbers if n > 0]
```

### 2. Small Functions (Do One Thing)
```python
# Bad — does too many things
def process_user(data):
    # validate, transform, save, send email, log...

# Good — each function does one thing
def validate_user(data): ...
def transform_user(data): ...
def save_user(user): ...
```

### 3. Avoid Deep Nesting
```python
# Bad — deeply nested
if user:
    if user.active:
        if user.has_permission:
            process(user)

# Good — early returns
if not user:
    return
if not user.active:
    return
if not user.has_permission:
    return
process(user)
```

## Project Structure

```
my_project/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   ├── services/
│   └── utils/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

## SOLID Principles (Simplified)

| Principle | Meaning |
|-----------|---------|
| **S**ingle Responsibility | Each class/function does ONE thing |
| **O**pen/Closed | Open for extension, closed for modification |
| **D**on't Repeat Yourself | Avoid duplicate code |

## Key Points

- Write code for **humans**, not just computers
- Use descriptive names for everything
- Keep functions small and focused
- Reduce nesting with early returns
- Organize code into logical modules and packages
- Follow DRY — Don't Repeat Yourself
