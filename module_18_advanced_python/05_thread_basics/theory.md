# Multithreading — Thread Basics

## What Is a Thread?

A **thread** is a lightweight unit of execution within a program. Multiple threads share the same memory space and can run concurrently.

Think of threads like multiple workers in the same office:
- They share the same desk (memory)
- They can work on different tasks at the same time
- They need to coordinate to avoid conflicts

## Creating Threads

```python
import threading

def say_hello(name):
    print(f"Hello from {name}!")

# Create a thread
t = threading.Thread(target=say_hello, args=("Thread-1",))

# Start the thread
t.start()

# Wait for the thread to finish
t.join()
```

## Thread Lifecycle

1. **Created** — `Thread()` is called
2. **Started** — `.start()` begins execution
3. **Running** — the thread's function executes
4. **Finished** — the function returns

```python
t = threading.Thread(target=my_function)  # Created
t.start()                                   # Started → Running
t.join()                                    # Wait until Finished
```

## Multiple Threads

```python
import threading
import time

def worker(name, duration):
    print(f"{name} starting")
    time.sleep(duration)
    print(f"{name} done")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Worker-{i}", 1))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All workers finished")
```

All three workers run concurrently — the total time is ~1 second, not 3.

## Thread Names and Current Thread

```python
import threading

print(threading.current_thread().name)  # "MainThread"
print(threading.active_count())          # Number of active threads
```

## Key Points

- Threads run concurrently within the same process
- Use `threading.Thread(target=func, args=(...))` to create threads
- `.start()` begins execution, `.join()` waits for completion
- Threads are best for **I/O-bound** tasks (due to the GIL)
- Multiple threads share the same memory — this can cause problems (next subtopic)
