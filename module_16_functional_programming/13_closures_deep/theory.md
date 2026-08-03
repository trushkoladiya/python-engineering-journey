# Closures (Deep Use)

A **closure** is a function that **remembers** variables from its enclosing scope, even after that scope has finished executing.

## How Closures Work

```python
def make_counter():
    count = 0              # enclosed variable
    def counter():
        nonlocal count
        count += 1
        return count
    return counter         # returned function "remembers" count

c = make_counter()
print(c())   # 1
print(c())   # 2
print(c())   # 3
```

The inner function `counter` **captures** the variable `count` from `make_counter`'s scope. Even after `make_counter()` finishes, `count` lives on inside the closure.

## Closure vs Regular Function

| Feature | Regular Function | Closure |
|---------|-----------------|---------|
| State | Stateless | Carries captured state |
| Memory | No persistent variables | Remembers enclosing scope |
| Use case | Simple computation | Persistent state, factories |

## The `nonlocal` Keyword

To **modify** a captured variable (not just read it), use `nonlocal`:

```python
def make_accumulator():
    total = 0
    def add(amount):
        nonlocal total     # allows modification
        total += amount
        return total
    return add
```

## Practical Patterns

```python
# Logger with context
def make_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

debug = make_logger("DEBUG")
debug("Starting process")   # [DEBUG] Starting process
```

## Key Points

- A closure captures variables from its enclosing scope
- The captured variables persist even after the outer function returns
- Use `nonlocal` to modify captured variables
- Closures are used for state, factories, and callbacks
- Every closure has a `__closure__` attribute
