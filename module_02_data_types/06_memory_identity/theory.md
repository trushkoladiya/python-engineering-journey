# Memory & Identity Basics

## 1. Object Identity — `id()`

Every object in Python has a unique **identity number** (like an address).

```python
x = 42
print(id(x))  # some number like 140234567890
```

Two variables pointing to the **same object** have the same `id`.

```python
a = "hello"
b = a
print(id(a) == id(b))  # True — same object
```

## 2. `is` vs `==`

| Operator | Checks | Meaning |
|----------|--------|---------|
| `==` | Equality | Same value? |
| `is` | Identity | Same object in memory? |

```python
a = "hello"
b = "hello"
print(a == b)  # True — same value
print(a is b)  # True — Python reuses small strings
```

## 3. Mutable vs Immutable (Intro)

| Type | Mutable? | Can Change? |
|------|----------|-------------|
| `int` | Immutable | No |
| `float` | Immutable | No |
| `str` | Immutable | No |
| `bool` | Immutable | No |
| `list` | Mutable | Yes |

> You'll learn about mutable types (lists, dicts) in later modules.

For immutable types, "changing" actually creates a **new** object:

```python
x = 10
print(id(x))
x = 20       # new object created
print(id(x)) # different id!
```

## Key Points

- `id()` gives the memory identity of an object
- `is` checks same object, `==` checks same value
- All types you've learned so far are immutable
- Reassigning creates a new object
