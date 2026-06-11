# Generator Behavior

Understanding how generators **pause and resume** is key to using them effectively.

## Execution Flow

A generator function doesn't run when you call it. It runs step by step:

```python
def demo():
    print("Before first yield")
    yield 1
    print("Before second yield")
    yield 2
    print("After last yield")

gen = demo()        # nothing printed yet!
next(gen)           # prints "Before first yield", returns 1
next(gen)           # prints "Before second yield", returns 2
next(gen)           # prints "After last yield", raises StopIteration
```

## Pausing and Resuming

At each `yield`:
1. The generator **returns** the yielded value
2. The generator **pauses** — all local variables are preserved
3. On `next()`, the generator **resumes** from exactly where it stopped

## State Preservation

Local variables survive between `yield` calls:

```python
def counter():
    count = 0
    while count < 3:
        count += 1
        yield count   # count is preserved between calls!
```

## Generator Exhaustion

After the function body finishes (no more `yield`), the generator is **exhausted**:
- `next()` raises `StopIteration`
- The generator cannot be restarted
- You must create a new generator to iterate again

## Key Points

- Generator code runs lazily — only when `next()` is called
- Execution pauses at `yield` and resumes on next `next()`
- All local variables are preserved between yields
- Once exhausted, a generator cannot be reused
