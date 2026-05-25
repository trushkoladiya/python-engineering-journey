# Numbers (Numeric Types)

Python has three numeric types: `int`, `float`, and `complex`.

## 1. Integer (`int`)

Whole numbers — positive, negative, or zero. No size limit in Python.

```python
x = 42
y = -100
big = 999999999999999999999  # Python handles huge numbers
```

### Underscores for readability

```python
population = 1_000_000_000  # same as 1000000000
print(population)           # 1000000000
```

## 2. Float (`float`)

Numbers with a decimal point.

```python
price = 19.99
temperature = -5.0
```

### Precision behavior

Floats are **not perfectly accurate** — this is normal in all programming languages.

```python
print(0.1 + 0.2)  # 0.30000000000000004 (not exactly 0.3)
```

### Scientific notation

```python
x = 1e3    # 1000.0
y = 2.5e-4 # 0.00025
```

## 3. Complex Numbers (`complex`)

Numbers with a real and imaginary part. Written with `j`.

```python
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
```

You won't use these often, but Python supports them natively.

## Key Points

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42`, `-5` | Whole numbers, unlimited size |
| `float` | `3.14`, `1e3` | Decimal numbers, slight imprecision |
| `complex` | `3+4j` | Real + imaginary part |

- Use `_` in large numbers for readability
- Float math can have tiny precision errors
- Python integers have no size limit
