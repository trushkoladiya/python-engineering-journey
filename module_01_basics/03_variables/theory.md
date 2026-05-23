# Variables

## What is a Variable?

A variable is a **name** that stores a **value**. Think of it as a labeled box.

```python
age = 21         # the box "age" now holds 21
name = "Trush"   # the box "name" now holds "Trush"
```

## 1. Variable Creation

- No special keyword needed
- Just use `=` to assign a value

```python
x = 10
message = "hello"
```

## 2. Dynamic Typing

Python figures out the type **automatically**. You don't need to declare it.

```python
x = 10        # Python knows this is an integer
x = "hello"   # Now x is a string — Python is fine with this
```

- A variable can change its type at any time
- This is called **dynamic typing**

## 3. Naming Rules

| Rule | Example | Valid? |
|------|---------|--------|
| Letters, numbers, underscores | `my_var`, `age2` | ✅ |
| Cannot start with a number | `2name` | ❌ |
| No spaces | `my name` | ❌ |
| Case sensitive | `age` ≠ `Age` | ✅ |
| No keywords | `print`, `if` | ❌ |

### Good Naming Practice

```python
user_age = 21       # ✅ clear and descriptive
x = 25              # ❌ unclear — what is x?
```

## 4. Multiple Assignment

You can assign values to multiple variables in one line.

```python
a, b, c = 1, 2, 3
```

You can also give the same value to multiple variables:

```python
x = y = z = 0
```

## Key Points

- Variables store data
- Use `=` to assign
- Python is dynamically typed
- Use clear, descriptive names
- Names are case-sensitive
