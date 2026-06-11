# Thread Synchronization

## Why Synchronization?

When multiple threads share data, they can interfere with each other. This causes **race conditions** — bugs where the result depends on the timing of thread execution.

```python
# Without synchronization — DANGER!
counter = 0

def increment():
    global counter
    for _ in range(100_000):
        counter += 1  # NOT atomic — can cause wrong results
```

## What Is a Race Condition?

A race condition happens when two threads read and write the same data at the same time:

1. Thread A reads `counter` = 5
2. Thread B reads `counter` = 5
3. Thread A writes `counter` = 6
4. Thread B writes `counter` = 6 ← Should be 7!

The increment is "lost" because both threads read the old value.

## Lock — The Solution

A `Lock` ensures only one thread accesses shared data at a time:

```python
import threading

lock = threading.Lock()
counter = 0

def safe_increment():
    global counter
    for _ in range(100_000):
        lock.acquire()
        counter += 1
        lock.release()
```

Or use `with` for cleaner code:

```python
def safe_increment():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1
```

## Deadlock

A **deadlock** occurs when two threads each wait for a lock the other holds:

- Thread A holds Lock1, waiting for Lock2
- Thread B holds Lock2, waiting for Lock1
- Neither can proceed — the program freezes

**Prevention**: Always acquire locks in the same order.

## Key Points

- **Race condition**: threads interfere with shared data
- **Lock**: ensures only one thread accesses data at a time
- **`with lock:`**: cleanest way to use locks
- **Deadlock**: threads waiting for each other forever — avoid by ordering locks
- **RLock**: a reentrant lock that the same thread can acquire multiple times
