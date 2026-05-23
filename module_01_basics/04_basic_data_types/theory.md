# Basic Data Types (Intro)

Python has different **types** of data. Here are the 4 basic ones.

## 1. Integer (`int`)

Whole numbers — no decimal point.

```python
age = 21
count = -3
zero = 0
```

## 2. Float (`float`)

Numbers **with** a decimal point.

```python
price = 19.99
temperature = -5.0
pi = 3.14
```

> Even `5.0` is a float, not an integer.

## 3. String (`str`)

Text — wrapped in quotes (single `'` or double `"`).

```python
name = "Trush"
greeting = 'Hello!'
```

- Single or double quotes both work
- Must use the **same** quote to open and close

## 4. Boolean (`bool`)

Only two values: `True` or `False`.

```python
is_student = True
has_license = False
```

- Always capitalized: `True`, not `true`
- Used for yes/no, on/off situations

## Checking the Type

Use `type()` to see what type a value is.

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
```

## Key Points

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42` | Whole number |
| `float` | `3.14` | Decimal number |
| `str` | `"hello"` | Text |
| `bool` | `True` | True or False |

- Use `type()` to check any value's type
- Python assigns the type automatically
