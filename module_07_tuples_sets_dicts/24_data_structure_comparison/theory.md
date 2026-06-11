# Data Structure Comparison & Use Cases

Choosing the right data structure is an important skill. Here's when to use each one.

## List vs Tuple

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | ✅ Yes | ❌ No |
| Speed | Slower | Faster |
| Memory | More | Less |
| Use as dict key | ❌ No | ✅ Yes |

**Use List when**: data changes (shopping cart, to-do items)
**Use Tuple when**: data is fixed (coordinates, RGB colors, days of week)

## Set vs List

| Feature | List | Set |
|---------|------|-----|
| Ordered | ✅ Yes | ❌ No |
| Duplicates | ✅ Allowed | ❌ Removed |
| Indexing | ✅ Yes | ❌ No |
| Lookup speed | Slow | Fast |

**Use List when**: order matters, duplicates needed
**Use Set when**: uniqueness needed, fast lookups

## Dictionary vs List of Tuples

| Feature | Dictionary | List of Tuples |
|---------|-----------|---------------|
| Lookup by key | ✅ Fast | ❌ Slow |
| Ordered | ✅ Yes (3.7+) | ✅ Yes |
| Duplicate keys | ❌ No | ✅ Allowed |

**Use Dict when**: mapping keys to values (name → age)
**Use List of Tuples when**: order matters, duplicate keys possible

## Performance — Lookup Speed

- **List**: checks each element one by one (slow for large data)
- **Set**: uses hashing (very fast lookup)
- **Dictionary**: uses hashing for keys (very fast lookup)

## Key Points

- Lists: ordered, mutable, allow duplicates
- Tuples: ordered, immutable, allow duplicates
- Sets: unordered, mutable, no duplicates
- Dicts: key-value pairs, fast key lookup
- Choose based on your needs: mutability, order, uniqueness, speed
