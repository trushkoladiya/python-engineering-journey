# Context Managers — `__enter__` and `__exit__`

Context managers handle **setup and cleanup** automatically using the `with` statement.

## The `with` Statement

You've used `with` for file handling:

```python
with open("file.txt") as f:
    data = f.read()
# File is automatically closed, even if an error occurs
```

Now you can create your **own** context managers.

## How It Works

A context manager needs two methods:
- `__enter__` — runs at the start of `with` (setup)
- `__exit__` — runs at the end of `with` (cleanup)

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"Elapsed: {elapsed:.3f}s")
        return False   # don't suppress exceptions

with Timer():
    # do some work
    total = sum(range(1000000))
```

## `__exit__` Parameters

`__exit__` receives exception info:
- `exc_type` — the exception class (or `None` if no error)
- `exc_val` — the exception instance
- `exc_tb` — the traceback

Return `True` to **suppress** the exception, `False` to **propagate** it.

## When to Use

- **Resource management** — open/close, connect/disconnect
- **Timing** — measure code execution time
- **Temporary state** — change something, then restore it
- **Locking** — acquire/release locks

## Key Points

- `__enter__` = setup (returns the managed object)
- `__exit__` = cleanup (always runs, even on errors)
- Use `with obj:` syntax for automatic cleanup
- Return `True` from `__exit__` to suppress exceptions
- Perfect for any acquire/release pattern
