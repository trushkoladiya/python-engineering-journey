# Function Definition

A **function** is a reusable block of code that performs a specific task. Instead of writing the same code again and again, you write it once inside a function and call it whenever needed.

## The `def` Keyword

Use `def` to define a function:

```python
def greet():
    print("Hello, World!")
```

- `def` — keyword that starts a function definition
- `greet` — the name of the function
- `()` — parentheses (can hold parameters, covered next)
- `:` — colon at the end of the line
- The **indented block** below is the function body

## Function Naming Rules

- Must start with a letter or underscore (`_`)
- Can contain letters, numbers, and underscores
- Cannot be a Python keyword (`if`, `for`, `while`, etc.)
- Use **snake_case** (lowercase with underscores)

```python
# ✅ Good names
def say_hello():
    print("Hello!")

def calculate_total():
    print("Calculating...")

# ❌ Bad names
# def 2fast():      # Cannot start with a number
# def my-func():    # No hyphens allowed
# def for():        # Cannot use a keyword
```

## Function Structure

```python
def function_name():       # Header line
    # Body (indented)
    print("Line 1")
    print("Line 2")
```

The body can contain any code — print statements, variables, conditions, loops, etc.

## Key Points

- Use `def` to create a function
- Function names follow the same rules as variable names
- Use **snake_case** for function names
- The function body must be **indented**
- A function does nothing until it is **called**
