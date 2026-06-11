# Immutability in Practice

**Immutability** means data that **cannot be changed** after creation. Functional programming prefers immutable data because it's safer and more predictable.

## Mutable vs Immutable in Python

| Mutable | Immutable |
|---------|-----------|
| `list` | `tuple` |
| `dict` | `frozenset` |
| `set` | `str`, `int`, `float` |

## Why Immutability Matters

```python
# Mutable — accidental change!
def add_item(items, item):
    items.append(item)    # modifies the ORIGINAL list!
    return items

original = [1, 2, 3]
result = add_item(original, 4)
print(original)   # [1, 2, 3, 4] — CHANGED!

# Immutable approach — safe
def add_item_safe(items, item):
    return items + [item]   # creates a NEW list

original = [1, 2, 3]
result = add_item_safe(original, 4)
print(original)   # [1, 2, 3] — unchanged!
```

## Functional Transformations

Instead of modifying data, create **new versions**:

```python
# Instead of: data.sort()
sorted_data = sorted(data)

# Instead of: data.append(x)
new_data = data + [x]

# Instead of: dict["key"] = value
new_dict = {**old_dict, "key": value}
```

## Key Points

- Immutable data can't be accidentally changed
- Use tuples instead of lists when data shouldn't change
- Create new data instead of modifying existing data
- `frozenset` is an immutable set
- Python strings and numbers are already immutable
