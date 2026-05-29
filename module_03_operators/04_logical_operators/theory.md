# Logical Operators

Logical operators combine **boolean expressions** and return `True` or `False`.

## The Three Logical Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both must be True | `True and True` | `True` |
| `or` | At least one True | `True or False` | `True` |
| `not` | Reverses the value | `not True` | `False` |

## `and` — Both Must Be True

Returns `True` only if **both** sides are `True`.

```python
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False
```

## `or` — At Least One True

Returns `True` if **at least one** side is `True`.

```python
print(True or False)    # True
print(False or False)   # False
print(True or True)     # True
```

## `not` — Reverse

Flips `True` to `False` and vice versa.

```python
print(not True)    # False
print(not False)   # True
```

## Combining with Comparisons

```python
age = 21
print(age > 18 and age < 30)   # True (both conditions are true)
print(age < 18 or age > 60)    # False (neither is true)
```

## Short-Circuit Evaluation

Python stops evaluating as soon as it knows the result:

- **`and`** — if the first value is `False`, Python skips the second (result is already `False`)
- **`or`** — if the first value is `True`, Python skips the second (result is already `True`)

```python
print(False and "anything")   # False — didn't even check "anything"
print(True or "anything")    # True  — didn't even check "anything"
```

## Key Points

- `and` — both must be True
- `or` — at least one must be True
- `not` — flips the boolean
- Python uses short-circuit evaluation for efficiency
