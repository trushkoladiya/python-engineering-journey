# Dictionary Properties

Dictionaries have several important properties to understand.

## Key Uniqueness

Each key can only appear **once**. If you use the same key twice, the last value wins:

```python
data = {"a": 1, "a": 2}
print(data)   # {'a': 2}
```

## Keys Must Be Immutable

Keys must be **hashable** (immutable) types:

```python
# ✅ Valid keys: strings, numbers, tuples
valid = {"name": 1, 42: 2, (1, 2): 3}

# ❌ Invalid keys: lists, dicts, sets
# invalid = {[1, 2]: "value"}   # TypeError!
```

## Mutable Structure

You can add, modify, and remove key-value pairs:

```python
person = {"name": "Trush"}
person["age"] = 21        # Add
person["name"] = "Rahul"    # Modify
del person["age"]         # Remove
```

## Ordered (Python 3.7+)

Dictionaries maintain **insertion order**:

```python
d = {"c": 3, "a": 1, "b": 2}
print(d)   # {'c': 3, 'a': 1, 'b': 2} — order preserved
```

## Key Points

- Keys must be unique — duplicates overwrite
- Keys must be immutable (str, int, float, tuple)
- Values can be any type
- Dicts are mutable — you can change them
- Order is preserved (Python 3.7+)
