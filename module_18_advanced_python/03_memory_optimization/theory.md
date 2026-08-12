# Memory Optimization

## Why Optimize Memory?

When your program handles large data, memory usage matters. Python provides ways to reduce memory footprint and handle data more efficiently.

## Object Reuse: Python's Built-in Optimizations

Python automatically reuses certain objects:

```python
# Small integers (-5 to 256) are cached
a = 100
b = 100
print(a is b)  # True — same object reused

# Short strings are interned
x = "hello"
y = "hello"
print(x is y)  # True — same object reused
```

## __slots__ — Reducing Object Memory

By default, Python objects store attributes in a `__dict__` (a dictionary). This is flexible but uses extra memory.

```python
# Without __slots__ — uses more memory
class PointRegular:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# With __slots__ — uses less memory
class PointOptimized:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

`__slots__` tells Python exactly which attributes to expect, so it skips creating a `__dict__`.

## sys.getsizeof() — Measuring Object Size

```python
import sys

print(sys.getsizeof([]))          # Empty list
print(sys.getsizeof([1, 2, 3]))   # List with items
print(sys.getsizeof({}))          # Empty dict
print(sys.getsizeof("hello"))     # String
```

## Generators for Memory Efficiency

Instead of building a whole list in memory, generators produce values one at a time:

```python
# List — stores ALL values in memory
big_list = [x * x for x in range(1_000_000)]

# Generator — produces values on demand
big_gen = (x * x for x in range(1_000_000))
```

The generator uses almost no memory compared to the list.

## Key Points

- Python reuses small integers and interned strings automatically
- `__slots__` reduces memory for objects with fixed attributes
- `sys.getsizeof()` measures an object's memory usage
- Generators are memory-efficient alternatives to lists
- Choose the right data structure for your data size
