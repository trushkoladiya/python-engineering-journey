# GIL (Global Interpreter Lock)

## What Is the GIL?

The **Global Interpreter Lock (GIL)** is a mechanism in CPython (the standard Python implementation) that allows **only one thread to execute Python bytecode at a time**.

Even if your computer has 8 CPU cores, a multithreaded Python program can only run **one thread's Python code** at any moment.

## Why Does the GIL Exist?

Python's memory management (reference counting) is **not thread-safe**. If two threads modified an object's reference count at the same time, memory could be corrupted.

The GIL is a simple solution: **lock everything** so only one thread runs Python code at a time.

## CPU-Bound vs I/O-Bound Tasks

The GIL matters most for **CPU-bound** tasks:

| Task Type | Example | GIL Impact |
|-----------|---------|------------|
| CPU-bound | Math, sorting, processing | GIL blocks parallelism |
| I/O-bound | Reading files, network requests, waiting | GIL released during wait |

```python
# CPU-bound: the GIL prevents true parallelism
# Two threads doing math won't be faster than one

# I/O-bound: the GIL is released while waiting
# Two threads downloading files CAN run concurrently
```

## When the GIL Is Released

The GIL is released during:
- File I/O (reading/writing files)
- Network I/O (HTTP requests, sockets)
- `time.sleep()` calls
- Certain C extension operations

This is why **multithreading works well for I/O tasks** even with the GIL.

## Working Around the GIL

| Approach | Best For |
|----------|---------|
| Threading | I/O-bound tasks (GIL released during I/O) |
| Multiprocessing | CPU-bound tasks (each process has its own GIL) |
| Async/Await | I/O-bound tasks (single thread, no GIL issue) |

## Key Points

- The GIL allows only one thread to execute Python bytecode at a time
- It exists to protect Python's memory management
- **I/O-bound** tasks work fine with threads (GIL is released during I/O)
- **CPU-bound** tasks need multiprocessing to achieve true parallelism
- The GIL is specific to CPython — other implementations (PyPy, Jython) may differ
