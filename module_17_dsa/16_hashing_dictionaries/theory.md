# Hashing & Dictionaries in DSA

## What Is Hashing?

**Hashing** converts a key into an index using a **hash function**. This enables **O(1) average** lookup, insertion, and deletion.

Python's `dict` and `set` use hashing internally.

## How Dictionaries Work

```
Key → hash(key) → index → value

"Trush" → hash("Trush") → 42 → "555-0001"
```

The hash function converts the key to a number, which maps to a position in an internal array.

## Why O(1)?

- Direct jump to position (no scanning)
- Like knowing exactly which shelf a book is on

## DSA Applications

### Frequency Counting

```python
def count_freq(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq
```

### Duplicate Detection

```python
def has_duplicates(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False
```

## Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Lookup | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case is rare — happens with many hash collisions.

## Key Points

- Hashing gives O(1) average-case operations
- Python dicts and sets are hash tables
- Use dicts for frequency, grouping, and lookup problems
- When you need fast "have I seen this?" → use a set
