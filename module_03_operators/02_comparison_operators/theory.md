# Comparison (Relational) Operators

Comparison operators compare two values and return a **boolean** (`True` or `False`).

## All Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `7 > 3` | `True` |
| `<` | Less than | `3 < 7` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `4 <= 5` | `True` |

## How They Work

Comparisons always return `True` or `False`.

```python
print(10 == 10)   # True
print(10 == 5)    # False
print(10 != 5)    # True
```

## Comparing Different Types

```python
print(10 == 10.0)   # True  (Python compares the values)
print(10 > 9.5)     # True
```

## `==` vs `=`

- `=` is **assignment** — it stores a value
- `==` is **comparison** — it checks if two values are equal

```python
x = 10       # assignment: x is now 10
print(x == 10)  # comparison: is x equal to 10? → True
```

## Chained Comparisons

Python allows chaining comparisons — a shorthand for checking ranges.

```python
x = 5
print(1 < x < 10)     # True  (x is between 1 and 10)
print(1 < x < 3)      # False (x is not between 1 and 3)
print(0 <= x <= 5)     # True
```

## Key Points

- Comparisons return `True` or `False`
- `==` checks equality, `=` assigns a value
- You can chain comparisons like `1 < x < 10`
- Python can compare int and float values
