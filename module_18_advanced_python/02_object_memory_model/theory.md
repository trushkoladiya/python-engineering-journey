# Object Memory Model

## How Python Stores Objects in Memory

Every value in Python is an **object** stored in memory. When you write `x = 42`, Python:

1. Creates an integer object `42` in memory
2. Creates a name `x` that **references** (points to) that object

```python
x = 42
y = x  # y points to the SAME object as x
```

`x` and `y` are not separate copies — they both reference the **same** object.

## id() — Finding an Object's Memory Address

```python
x = 42
y = x
print(id(x))  # e.g., 140234567890
print(id(y))  # Same number — same object!

z = 42
print(id(z))  # May also be the same (Python reuses small integers)
```

## Reference Counting

Python tracks how many names point to each object. This count is called the **reference count**.

```python
import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # Shows reference count (usually 2+)

b = a  # Reference count increases
print(sys.getrefcount(a))  # Now higher

del b  # Reference count decreases
print(sys.getrefcount(a))  # Back down
```

When the reference count reaches **0**, Python deletes the object and frees the memory.

## Garbage Collection

Sometimes objects reference **each other** in a cycle:

```python
a = []
b = []
a.append(b)  # a references b
b.append(a)  # b references a
```

Even after `del a` and `del b`, the reference count never reaches 0 because they point to each other. Python's **garbage collector** detects these cycles and cleans them up.

```python
import gc
gc.collect()  # Manually trigger garbage collection
```

## is vs ==

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True — same VALUE
print(a is b)  # False — different OBJECTS in memory
```

- `==` compares **values**
- `is` compares **identity** (same object in memory)

## Key Points

- Variables are **names** that reference objects in memory
- `id()` shows an object's memory address
- Python uses **reference counting** to manage memory
- **Garbage collection** handles circular references
- `is` checks identity, `==` checks equality
