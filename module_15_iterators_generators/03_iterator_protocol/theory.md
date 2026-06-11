# The Iterator Protocol

The **iterator protocol** is the set of rules that makes iteration work in Python. Any object that follows these rules can be used in a `for` loop.

## The Two Required Methods

An iterator must implement:

1. **`__iter__()`** — returns the iterator object itself
2. **`__next__()`** — returns the next item, or raises `StopIteration` when done

```python
my_list = [10, 20, 30]
it = iter(my_list)       # calls my_list.__iter__()

next(it)   # 10          # calls it.__next__()
next(it)   # 20          # calls it.__next__()
next(it)   # 30          # calls it.__next__()
next(it)   # StopIteration!
```

## `iter()` and `next()` Are Wrappers

| Function | Calls |
|----------|-------|
| `iter(obj)` | `obj.__iter__()` |
| `next(it)` | `it.__next__()` |

```python
it = [1, 2, 3].__iter__()   # same as iter([1, 2, 3])
it.__next__()                 # same as next(it) → 1
```

## `StopIteration` — The Signal to Stop

When an iterator has no more items, it raises `StopIteration`:

```python
it = iter([1])
next(it)    # 1
next(it)    # raises StopIteration
```

The `for` loop catches `StopIteration` automatically — that's how it knows when to stop.

## Key Points

- The iterator protocol requires `__iter__()` and `__next__()`
- `iter()` calls `__iter__()`, `next()` calls `__next__()`
- `StopIteration` signals that iteration is complete
- `for` loops handle `StopIteration` automatically
