# Multiprocessing

## What Is Multiprocessing?

**Multiprocessing** creates separate **processes**, each with its own Python interpreter and its own GIL. This allows **true parallel execution** on multiple CPU cores.

| Feature | Threading | Multiprocessing |
|---------|-----------|----------------|
| Memory | Shared | Separate per process |
| GIL | Shared (limits parallelism) | Each has its own |
| Best for | I/O-bound tasks | CPU-bound tasks |
| Overhead | Low | Higher (process creation) |

## Creating Processes

```python
from multiprocessing import Process

def worker(name):
    print(f"Hello from {name}")

p = Process(target=worker, args=("Process-1",))
p.start()
p.join()
```

The API is very similar to `threading.Thread`.

## When to Use Multiprocessing

Use multiprocessing when:
- You have **CPU-bound** work (math, data processing, sorting)
- You want to use **multiple CPU cores**
- Threading doesn't give you a speedup (because of the GIL)

## Inter-Process Communication (IPC)

Since processes don't share memory, you need special tools to pass data between them:

```python
from multiprocessing import Queue

q = Queue()
q.put("hello")       # Producer puts data
item = q.get()        # Consumer gets data
```

## Process Pool

For running many tasks across multiple processes:

```python
from multiprocessing import Pool

def square(n):
    return n * n

with Pool(4) as pool:
    results = pool.map(square, [1, 2, 3, 4, 5])
# results = [1, 4, 9, 16, 25]
```

## Key Points

- Each process has its own memory and its own GIL
- Processes achieve **true parallelism** for CPU-bound tasks
- Use `Queue` or `Pipe` for inter-process communication
- `Pool` simplifies running functions across multiple processes
- Higher overhead than threads — use only when needed
