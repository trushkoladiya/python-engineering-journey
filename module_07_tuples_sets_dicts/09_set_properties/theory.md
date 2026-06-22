# Set Properties

Sets have three important properties: they are **unordered**, contain **no duplicates**, and are **mutable** (but their elements must be immutable).

## Unordered

Sets do not maintain insertion order:

```python
colors = {"red", "green", "blue"}
print(colors)   # Order may vary each time
```

Because sets are unordered:
- You **cannot** access elements by index
- There is no "first" or "last" element

## No Duplicates

Every element in a set is unique:

```python
numbers = {1, 1, 2, 2, 3}
print(numbers)   # {1, 2, 3}
```

## Mutable (But Elements Must Be Immutable)

You can add or remove elements from a set:

```python
fruits = {"apple", "banana"}
fruits.add("cherry")    # ✅ Works
print(fruits)
```

But elements themselves must be **immutable** (hashable):

```python
# {[1, 2], [3, 4]}     # ❌ Error — lists are mutable
# Sets can contain: int, float, str, bool, tuple
valid = {1, "hello", (1, 2), True, 3.14}
```

## Key Points

- Sets are **unordered** — no indexing
- No duplicate elements allowed
- Sets are **mutable** — you can add/remove elements
- Elements must be **immutable** (numbers, strings, tuples — not lists or dicts)
