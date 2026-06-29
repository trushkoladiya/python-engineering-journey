# Function Design Principles

Writing functions that work is easy. Writing **good** functions takes practice. Here are key principles.

## Single Responsibility

A function should do **one thing** and do it well:

```python
# ❌ Bad — does too much
def process_student(name, score):
    grade = "A" if score >= 90 else "B" if score >= 80 else "F"
    print(f"{name}: {grade}")
    with open("grades.txt", "a") as f:
        f.write(f"{name},{grade}\n")

# ✅ Good — each function does one thing
def get_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    return "F"

def display_result(name, grade):
    print(f"{name}: {grade}")
```

## Reusability

Write functions that can be used in **multiple situations**:

```python
# ❌ Too specific
def add_5_and_3():
    return 5 + 3

# ✅ Reusable
def add(a, b):
    return a + b
```

## Readability

Use clear names and keep functions short:

```python
# ❌ Unclear
def p(x):
    return x > 0

# ✅ Clear
def is_positive(number):
    return number > 0
```

## Pure vs Impure Functions

A **pure function** always gives the same output for the same input, with no side effects:

```python
# Pure — no side effects
def add(a, b):
    return a + b

# Impure — changes external state
total = 0
def add_to_total(n):
    global total
    total += n
```

## Key Points

- One function = one job (single responsibility)
- Make functions reusable with parameters
- Use descriptive names
- Keep functions short and focused
- Prefer pure functions when possible
