# Class Internals & Memory

Understanding how Python stores object data helps you write more efficient code.

## `__dict__` — Attribute Storage

Every object stores its attributes in a dictionary called `__dict__`:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

buddy = Dog("Buddy", 3)
print(buddy.__dict__)  # {'name': 'Buddy', 'age': 3}
```

- Instance attributes live in `obj.__dict__`
- Class attributes live in `ClassName.__dict__`
- `vars(obj)` is the same as `obj.__dict__`

## `__slots__` — Memory Optimization

By default, every object has a `__dict__` (a full dictionary). For classes with many instances, this wastes memory.

`__slots__` replaces `__dict__` with a fixed set of attributes:

```python
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
p.z = 3  # AttributeError! Can't add new attributes
```

## `__slots__` Benefits

| Feature | Normal Class | Class with `__slots__` |
|---------|-------------|----------------------|
| `__dict__` | Yes | No |
| Memory per instance | Higher | Lower |
| Add attributes at runtime | Yes | No |
| Speed of attribute access | Normal | Slightly faster |

## When to Use `__slots__`

- Creating **millions** of small objects
- Performance-critical code
- You know all attributes in advance

## Key Points

- `__dict__` stores attributes as a dictionary (flexible but uses memory)
- `__slots__` fixes allowed attributes (saves memory, prevents additions)
- `vars(obj)` returns `obj.__dict__`
- Use `__slots__` for high-performance, many-instance scenarios
- Most classes don't need `__slots__` — use it when it matters
