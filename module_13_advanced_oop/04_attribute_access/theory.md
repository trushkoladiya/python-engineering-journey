# Attribute Access Control

Python lets you customize what happens when attributes are **accessed**, **set**, or **deleted** using special hooks.

## The Four Attribute Hooks

| Method | Called When | Example |
|--------|-----------|---------|
| `__getattr__` | Attribute **not found** normally | `obj.missing_attr` |
| `__getattribute__` | **Every** attribute access | `obj.any_attr` |
| `__setattr__` | Attribute is **set** | `obj.x = 5` |
| `__delattr__` | Attribute is **deleted** | `del obj.x` |

## `__getattr__` — Handle Missing Attributes

Called only when normal lookup **fails**:

```python
class Flexible:
    def __getattr__(self, name):
        return f"'{name}' not found, returning default"

obj = Flexible()
print(obj.anything)  # "'anything' not found, returning default"
```

## `__getattribute__` — Intercept ALL Access

Called on **every** attribute access (be careful — can cause infinite recursion!):

```python
class Logged:
    def __getattribute__(self, name):
        print(f"Accessing: {name}")
        return super().__getattribute__(name)  # MUST call super!
```

## `__setattr__` — Control Setting

Called whenever you do `obj.x = value`:

```python
class Validated:
    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            raise ValueError("Age can't be negative")
        super().__setattr__(name, value)  # MUST call super!
```

## `__delattr__` — Control Deletion

```python
class Protected:
    def __delattr__(self, name):
        if name == "id":
            raise AttributeError("Cannot delete id!")
        super().__delattr__(name)
```

## Key Points

- `__getattr__` → called only for **missing** attributes (safe, common)
- `__getattribute__` → called for **all** access (dangerous, rare)
- `__setattr__` → called on **every** assignment (use `super().__setattr__`)
- `__delattr__` → called on **every** deletion
- Always call `super()` in `__getattribute__`, `__setattr__`, `__delattr__` to avoid infinite recursion
