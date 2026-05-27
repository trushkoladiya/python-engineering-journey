# Type Conversion (Advanced View)

## Beyond Basic Casting

Module 1 covered `int()`, `float()`, `str()`, `bool()`. Here we go deeper.

## 1. Explicit Casting Between Types

### int ↔ float

```python
print(int(3.99))     # 3 (truncates, does NOT round)
print(float(5))      # 5.0
```

### float → int (rounding)

```python
print(round(3.5))    # 4
print(round(3.14))   # 3
print(round(2.675, 2))  # 2.67 (precision issues!)
```

### str ↔ numbers

```python
print(int("42"))       # 42
print(float("3.14"))   # 3.14
print(str(100))        # "100"
print(str(3.14))       # "3.14"
```

## 2. Chained Conversion

Sometimes you need two steps:

```python
text = "3.14"
# int(text)  ❌ Error — can't go directly
result = int(float(text))  # ✅ first float, then int
print(result)  # 3
```

## 3. Errors During Conversion

Not all conversions work:

```python
# int("hello")    ❌ ValueError
# int("")         ❌ ValueError
# float("abc")    ❌ ValueError
```

### What does work:

```python
int("  42  ")    # 42 — strips whitespace automatically
float("  3.14 ") # 3.14
```

## 4. `ord()` and `chr()` — Character Conversions

```python
print(ord("A"))   # 65 — character to number
print(chr(65))    # A  — number to character
print(ord("a"))   # 97
print(chr(97))    # a
```

## Key Points

- `int()` truncates, `round()` rounds
- Chained conversion: `int(float("3.14"))`
- Invalid conversions raise `ValueError`
- `ord()` / `chr()` convert between characters and numbers
