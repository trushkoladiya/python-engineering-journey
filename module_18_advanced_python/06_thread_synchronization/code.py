# ============================================
# MODULE 18 - SUBTOPIC 6: Thread Synchronization
# ============================================

# When threads share data, you need synchronization
# to prevent race conditions and data corruption.

import threading
import time

# =============================
# 1. THE RACE CONDITION PROBLEM
# =============================

print("=== Race Condition Demo ===")
print()

# Shared variable WITHOUT protection
counter = 0

def unsafe_increment(n):
    global counter
    for _ in range(n):
        counter += 1  # NOT atomic!

# Reset and test
counter = 0
N = 100_000

threads = [
    threading.Thread(target=unsafe_increment, args=(N,)),
    threading.Thread(target=unsafe_increment, args=(N,)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"  Expected: {N * 2:,}")
print(f"  Got:      {counter:,}")
print(f"  Lost:     {N * 2 - counter:,} increments")
print(f"  Race condition: {counter != N * 2}")
print()

# counter += 1 is NOT a single operation:
# 1. Read counter
# 2. Add 1
# 3. Write counter
# Threads can interleave between these steps!

# =============================
# 2. FIXING WITH Lock
# =============================

print("=== Fixed with Lock ===")
print()

lock = threading.Lock()
safe_counter = 0

def safe_increment(n):
    global safe_counter
    for _ in range(n):
        lock.acquire()    # Only one thread can enter
        safe_counter += 1
        lock.release()    # Let other threads in

safe_counter = 0

threads = [
    threading.Thread(target=safe_increment, args=(N,)),
    threading.Thread(target=safe_increment, args=(N,)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"  Expected: {N * 2:,}")
print(f"  Got:      {safe_counter:,}")
print(f"  Correct:  {safe_counter == N * 2}")
print()

# =============================
# 3. USING Lock WITH context manager
# =============================

print("=== Lock with 'with' Statement ===")
print()

lock2 = threading.Lock()
balance = 1000

def withdraw(amount, name):
    global balance
    with lock2:  # Automatically acquire and release
        if balance >= amount:
            time.sleep(0.01)  # Simulate processing
            balance -= amount
            print(f"  {name} withdrew ${amount}. Balance: ${balance}")
        else:
            print(f"  {name} — insufficient funds! Balance: ${balance}")

threads = [
    threading.Thread(target=withdraw, args=(600, "Trush")),
    threading.Thread(target=withdraw, args=(600, "Rahul")),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"  Final balance: ${balance}")
print()

# Without the lock, both could pass the balance check
# and withdraw, leaving a negative balance!

# =============================
# 4. RLock (Reentrant Lock)
# =============================

print("=== RLock (Reentrant Lock) ===")
print()

# A regular Lock CANNOT be acquired twice by the same thread
# An RLock CAN — useful for recursive or nested locking

rlock = threading.RLock()

def outer():
    with rlock:
        print("  Outer lock acquired")
        inner()  # Calls another function that also needs the lock

def inner():
    with rlock:  # Same thread can acquire again
        print("  Inner lock acquired (same thread)")

outer()
print()

# With a regular Lock, this would DEADLOCK
# because the thread would wait for itself

# =============================
# 5. MULTIPLE LOCKS AND DEADLOCK
# =============================

print("=== Deadlock Example (Avoided) ===")
print()

# Deadlock: Thread A holds Lock1 and waits for Lock2
#           Thread B holds Lock2 and waits for Lock1
# Both wait forever!

lock_a = threading.Lock()
lock_b = threading.Lock()

def task_1():
    with lock_a:
        print("  Task 1: got lock_a")
        time.sleep(0.1)
        with lock_b:  # Waits for lock_b
            print("  Task 1: got lock_b")

def task_2():
    # SAFE: acquire locks in SAME order as task_1
    with lock_a:  # Same order prevents deadlock
        print("  Task 2: got lock_a")
        time.sleep(0.1)
        with lock_b:
            print("  Task 2: got lock_b")

# This is SAFE because both tasks acquire locks in the same order
t1 = threading.Thread(target=task_1)
t2 = threading.Thread(target=task_2)
t1.start()
t2.start()
t1.join()
t2.join()
print()

# Rule: Always acquire multiple locks in a consistent order!

# =============================
# 6. Event — SIGNALING BETWEEN THREADS
# =============================

print("=== Event — Thread Signaling ===")
print()

event = threading.Event()

def waiter(name):
    print(f"  {name} waiting for signal...")
    event.wait()  # Block until event is set
    print(f"  {name} received signal!")

def signaler():
    time.sleep(0.3)
    print("  Signaler: sending signal!")
    event.set()  # Wake up all waiting threads

threads = [
    threading.Thread(target=waiter, args=("Waiter-1",)),
    threading.Thread(target=waiter, args=("Waiter-2",)),
    threading.Thread(target=signaler),
]

for t in threads:
    t.start()
for t in threads:
    t.join()
print()

# =============================
# 7. Semaphore — LIMITING CONCURRENT ACCESS
# =============================

print("=== Semaphore — Limiting Concurrent Access ===")
print()

# A semaphore allows up to N threads to access a resource
semaphore = threading.Semaphore(2)  # Max 2 concurrent

def limited_resource(worker_id):
    with semaphore:
        print(f"  Worker-{worker_id} accessing resource")
        time.sleep(0.2)
        print(f"  Worker-{worker_id} releasing resource")

threads = []
for i in range(5):
    t = threading.Thread(target=limited_resource, args=(i + 1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print()

# Only 2 workers access the resource at the same time

# =============================
# 8. PRACTICAL: THREAD-SAFE COUNTER CLASS
# =============================

print("=== Practical: Thread-Safe Counter ===")
print()

class ThreadSafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()

    def increment(self, amount=1):
        with self._lock:
            self._count += amount

    def decrement(self, amount=1):
        with self._lock:
            self._count -= amount

    @property
    def value(self):
        with self._lock:
            return self._count

counter_obj = ThreadSafeCounter()

def add_many(n):
    for _ in range(n):
        counter_obj.increment()

# 4 threads, each incrementing 50,000 times
threads = []
PER_THREAD = 50_000

for _ in range(4):
    t = threading.Thread(target=add_many, args=(PER_THREAD,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"  Expected: {PER_THREAD * 4:,}")
print(f"  Got:      {counter_obj.value:,}")
print(f"  Correct:  {counter_obj.value == PER_THREAD * 4}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a race condition with a shared list
#    (append from multiple threads) and fix it
# 2. Use an Event to coordinate a producer and consumer
# 3. Use a Semaphore to limit database connections to 3
# ============================================
