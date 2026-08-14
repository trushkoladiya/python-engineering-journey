# Concurrent Execution Patterns

## Thread vs Process vs Async — When to Use Which?

Python offers three concurrency models. Choosing the right one is critical.

## Quick Comparison

| Model | Best For | GIL Issue? | Shared Memory? |
|-------|----------|-----------|----------------|
| Threading | I/O-bound tasks | Yes (but GIL released during I/O) | Yes |
| Multiprocessing | CPU-bound tasks | No (each process has own GIL) | No |
| Async/Await | Many I/O tasks | No (single thread) | Yes |

## Decision Guide

```
Is your task CPU-bound or I/O-bound?

CPU-bound → Use multiprocessing
    ├── Need shared state? → Use multiprocessing.Queue or Manager
    └── Simple parallel map? → Use Pool.map()

I/O-bound → How many concurrent tasks?
    ├── Few tasks (< 20) → threading is fine
    └── Many tasks (100+) → asyncio is better
```

## concurrent.futures — Unified Interface

The `concurrent.futures` module provides a **single API** for both threads and processes:

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Thread pool (I/O-bound)
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(io_function, items)

# Process pool (CPU-bound)
with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(cpu_function, items)
```

Same interface — just swap the executor class!

## Future Objects

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    future = executor.submit(my_function, arg1, arg2)
    result = future.result()  # Block until done
```

A `Future` represents a task that will complete in the future. You can check if it's done, get its result, or handle exceptions.

## Key Points

- Use **threading** for simple I/O-bound concurrency
- Use **multiprocessing** for CPU-bound parallelism
- Use **asyncio** for many concurrent I/O operations
- `concurrent.futures` gives a unified API for both threads and processes
- `Future` objects let you submit tasks and collect results later
