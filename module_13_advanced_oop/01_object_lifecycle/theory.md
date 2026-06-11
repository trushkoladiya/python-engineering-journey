# Object Lifecycle: `__new__` and `__init__`

In Module 12, you learned `__init__` initializes an object. But there's a step **before** that — `__new__` actually **creates** the object.

## The Two Steps of Object Creation

When you write `obj = MyClass()`, Python does two things:

1. **`__new__`** — creates the object (allocates memory)
2. **`__init__`** — initializes the object (sets attributes)

```python
class Dog:
    def __new__(cls, name):
        print(f"1. __new__: Creating a Dog object")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print(f"2. __init__: Initializing with name='{name}'")
        self.name = name

buddy = Dog("Buddy")
# Output:
# 1. __new__: Creating a Dog object
# 2. __init__: Initializing with name='Buddy'
```

## `__new__` vs `__init__`

| Feature | `__new__` | `__init__` |
|---------|-----------|------------|
| Purpose | Creates the object | Initializes the object |
| First param | `cls` (the class) | `self` (the instance) |
| Returns | The new instance | `None` |
| When called | Before `__init__` | After `__new__` |
| Override? | Rarely | Almost always |

## When to Use `__new__`?

Most of the time, `__init__` is all you need. Use `__new__` for:
- Controlling **how** an object is created
- Implementing patterns like **Singleton** (covered later)
- Subclassing immutable types like `str`, `int`, `tuple`

## `__del__` — Object Destruction

Called when an object is about to be garbage collected:

```python
class Resource:
    def __del__(self):
        print("Resource cleaned up")
```

> **Note:** Don't rely on `__del__` for critical cleanup — use context managers instead (covered later in this module).

## Key Points

- `__new__` creates → `__init__` initializes
- You almost always only need `__init__`
- `__new__` takes `cls`, returns the new instance
- `__init__` takes `self`, returns nothing
- `__del__` runs on garbage collection (unreliable timing)
