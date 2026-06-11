# any() and all() — Boolean Aggregation

`any()` and `all()` check conditions across an entire iterable.

## any()

Returns `True` if **at least one** element is truthy:

```python
numbers = [0, 0, 0, 1, 0]
print(any(numbers))   # True (1 is truthy)

empty = [0, 0, 0]
print(any(empty))     # False (nothing truthy)
```

## all()

Returns `True` if **every** element is truthy:

```python
numbers = [1, 2, 3, 4]
print(all(numbers))   # True (all truthy)

mixed = [1, 2, 0, 4]
print(all(mixed))     # False (0 is falsy)
```

## With Conditions (Generator Expression)

```python
ages = [18, 25, 16, 30]

# Are ALL adults?
all_adults = all(age >= 18 for age in ages)   # False

# Is ANY person a minor?
has_minor = any(age < 18 for age in ages)     # True
```

## Truth Table

| Function | Empty Iterable | All True | Some True | All False |
|----------|---------------|----------|-----------|-----------|
| `any()` | `False` | `True` | `True` | `False` |
| `all()` | `True` | `True` | `False` | `False` |

## Key Points

- `any()` = "is there at least one True?" (logical OR across items)
- `all()` = "are they all True?" (logical AND across items)
- Both work with generator expressions for condition checking
- Both short-circuit (stop early when answer is determined)
