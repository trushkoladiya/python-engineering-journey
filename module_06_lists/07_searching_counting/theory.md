# Searching & Counting

Lists have built-in methods to find elements and count occurrences.

## `index()` — Find Position of an Element

```python
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.index("banana"))   # 1 — first occurrence
print(fruits.index("cherry"))   # 2
```

If the element is **not found**, `index()` raises a `ValueError`:

```python
# fruits.index("grape")   # ❌ ValueError
```

## `count()` — Count Occurrences

```python
nums = [1, 2, 3, 2, 4, 2, 5]
print(nums.count(2))   # 3
print(nums.count(7))   # 0 — not found
```

## Checking Existence Safely

Always check with `in` before using `index()`:

```python
fruits = ["apple", "banana", "cherry"]
target = "grape"

if target in fruits:
    pos = fruits.index(target)
    print(f"Found at index {pos}")
else:
    print(f"'{target}' not found")
```

## Key Points

- `index(value)` returns the index of the first occurrence
- `count(value)` returns how many times it appears
- `index()` raises `ValueError` if not found — use `in` first to be safe
