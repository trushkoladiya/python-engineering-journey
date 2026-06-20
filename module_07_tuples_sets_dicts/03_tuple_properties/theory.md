# Tuple Properties

The most important property of tuples is **immutability** — they cannot be changed after creation.

## Immutability

Once a tuple is created, you **cannot** modify its elements:

```python
colors = ("red", "green", "blue")

# This will cause an ERROR:
# colors[0] = "yellow"   # TypeError!
```

You also **cannot**:
- Add elements
- Remove elements
- Change elements in place

## Why Use Tuples Instead of Lists?

Since tuples can't be changed, they are useful when:
- Data should **not** be modified (e.g., days of the week)
- You want to protect data from accidental changes
- You need a **hashable** type (for dictionary keys or set elements)

## Tuples Are Faster Than Lists

Tuples use less memory and are slightly faster than lists. This is because Python knows the tuple won't change, so it can optimize.

```python
import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(my_list))    # larger
print(sys.getsizeof(my_tuple))   # smaller
```

## Tuples with Mutable Elements

A tuple itself is immutable, but if it contains a **mutable** object (like a list), that object can still be changed:

```python
data = (1, 2, [3, 4])
data[2].append(5)       # This works!
print(data)             # (1, 2, [3, 4, 5])

# But this still fails:
# data[0] = 10          # TypeError!
```

## Key Points

- Tuples are **immutable** — no adding, removing, or changing elements
- Tuples are faster and use less memory than lists
- Use tuples for data that should stay constant
- A tuple can contain mutable objects, but the tuple itself can't be reassigned
