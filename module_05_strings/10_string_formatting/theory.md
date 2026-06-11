# String Formatting

String formatting lets you embed values inside strings in a clean, readable way.

## f-strings (Modern Python — Recommended)

Put `f` before the string and use `{}` to insert values:

```python
name = "Trush"
age = 21
print(f"My name is {name} and I am {age} years old.")
# My name is Trush and I am 21 years old.
```

You can put **expressions** inside the curly braces:

```python
x = 10
y = 3
print(f"{x} + {y} = {x + y}")   # 10 + 3 = 13
print(f"{x} / {y} = {x / y:.2f}")  # 10 / 3 = 3.33
```

## `format()` Method

An older but still useful approach:

```python
name = "Trush"
age = 21
print("My name is {} and I am {} years old.".format(name, age))
```

You can use numbered placeholders:

```python
print("{0} is {1} years old. {0} likes Python.".format("Trush", 21))
# Trush is 21 years old. Trush likes Python.
```

## Common Formatting Patterns

```python
# Padding with spaces
print(f"{'Hello':>20}")    # Right-align in 20 chars
print(f"{'Hello':<20}")    # Left-align in 20 chars
print(f"{'Hello':^20}")    # Center in 20 chars

# Number formatting
pi = 3.14159
print(f"Pi is {pi:.2f}")   # 3.14 — 2 decimal places
print(f"Pi is {pi:.4f}")   # 3.1416 — 4 decimal places

# Large numbers with separator
big = 1000000
print(f"{big:,}")   # 1,000,000
```

## Key Points

- **f-strings** are the simplest and most recommended way: `f"text {variable}"`
- `format()` method is an older alternative
- Use `:.2f` for decimal places, `:,` for thousands separator
- Use `:<`, `:>`, `:^` for alignment
