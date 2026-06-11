# Advanced Parameters

Python provides flexible ways to handle any number of arguments.

## `*args` — Variable Positional Arguments

Accept **any number** of positional arguments:

```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2))           # 3
print(add_all(1, 2, 3, 4, 5)) # 15
```

Inside the function, `args` is a **tuple**.

## `**kwargs` — Variable Keyword Arguments

Accept **any number** of keyword arguments:

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Trush", age=21, city="Mumbai")
```

Inside the function, `kwargs` is a **dictionary**.

## Keyword-Only Arguments

Arguments after `*` must be passed by name:

```python
def greet(name, *, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Trush")                     # Hello, Trush!
greet("Rahul", greeting="Hi")       # Hi, Rahul!
# greet("Rahul", "Hi")              # ❌ Error!
```

## Mutable Default Argument Problem

Never use a mutable object (like a list) as a default value:

```python
# ❌ BAD — the list is shared between calls!
def add_item_bad(item, items=[]):
    items.append(item)
    return items

# ✅ GOOD — use None as default
def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## Key Points

- `*args` collects extra positional arguments into a tuple
- `**kwargs` collects extra keyword arguments into a dict
- Arguments after `*` are keyword-only
- Never use mutable objects as default parameter values
