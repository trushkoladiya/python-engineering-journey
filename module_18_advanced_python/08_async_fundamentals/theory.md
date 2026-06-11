# Asynchronous Programming

## What Is Async Programming?

Async programming lets you run multiple I/O tasks **concurrently** using a **single thread**. Instead of waiting for each task to finish, the program can start other tasks while waiting.

Think of it like a chef:
- **Synchronous**: Cook one dish at a time. Wait for water to boil before doing anything else.
- **Asynchronous**: Start boiling water, chop vegetables while waiting, check the oven — all at the same time.

## async and await

```python
import asyncio

async def fetch_data(name, seconds):
    print(f"{name}: starting")
    await asyncio.sleep(seconds)  # Non-blocking wait
    print(f"{name}: done")
    return f"{name} result"

async def main():
    # Run two tasks concurrently
    results = await asyncio.gather(
        fetch_data("Task-1", 2),
        fetch_data("Task-2", 1),
    )
    print(results)

asyncio.run(main())
```

- `async def` defines a **coroutine** (an async function)
- `await` pauses the coroutine and lets other tasks run
- `asyncio.run()` starts the event loop

## The Event Loop

The **event loop** is the engine that manages async tasks:

1. It runs a coroutine until it hits `await`
2. While that coroutine waits, it runs another coroutine
3. When the waited task completes, it resumes the original coroutine

```
Event Loop:
  → Run Task A until it awaits
  → Run Task B until it awaits
  → Task A's await completes → resume Task A
  → Task B's await completes → resume Task B
```

## asyncio.gather() vs asyncio.create_task()

```python
# gather — run multiple coroutines and collect results
results = await asyncio.gather(coro1(), coro2(), coro3())

# create_task — schedule a coroutine to run
task = asyncio.create_task(coro1())
# ... do other work ...
result = await task
```

## When to Use Async

| Use Async | Don't Use Async |
|-----------|----------------|
| Network requests | CPU-heavy math |
| File I/O | Simple scripts |
| Database queries | Already-fast code |
| Web servers | Blocking C libraries |

## Key Points

- `async def` creates a coroutine
- `await` yields control to the event loop
- `asyncio.run()` starts the event loop from synchronous code
- `asyncio.gather()` runs multiple coroutines concurrently
- Async is for **I/O-bound** tasks, not CPU-bound
