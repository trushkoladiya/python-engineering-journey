# ============================================
# MODULE 18 - SUBTOPIC 4: GIL (Global Interpreter Lock)
# ============================================

# The GIL allows only ONE thread to run Python code at a time.
# This affects CPU-bound tasks but NOT I/O-bound tasks.

import threading
import time
import sys

# =============================
# 1. WHAT IS THE GIL?
# =============================

print("=== What Is the GIL? ===")
print()

print("  The Global Interpreter Lock (GIL) is a mutex in CPython.")
print("  It ensures only ONE thread executes Python bytecode at a time.")
print("  This is needed because Python's reference counting is not thread-safe.")
print()

# Check Python implementation
print(f"  Python implementation: {sys.implementation.name}")
print(f"  (The GIL is specific to CPython)")
print()

# =============================
# 2. CPU-BOUND TASK: SINGLE THREAD
# =============================

print("=== CPU-Bound: Single Thread ===")
print()

def cpu_task(n):
    """Count up to n — a CPU-bound task."""
    total = 0
    for i in range(n):
        total += i
    return total

COUNT = 10_000_000

start = time.time()
cpu_task(COUNT)
cpu_task(COUNT)
single_time = time.time() - start

print(f"  Two sequential CPU tasks: {single_time:.3f}s")
print()

# =============================
# 3. CPU-BOUND TASK: TWO THREADS
# =============================

print("=== CPU-Bound: Two Threads ===")
print()

start = time.time()

t1 = threading.Thread(target=cpu_task, args=(COUNT,))
t2 = threading.Thread(target=cpu_task, args=(COUNT,))

t1.start()
t2.start()
t1.join()
t2.join()

thread_time = time.time() - start

print(f"  Two threaded CPU tasks: {thread_time:.3f}s")
print(f"  Single thread time:     {single_time:.3f}s")
print()

# With the GIL, threading does NOT speed up CPU-bound tasks
# It may even be SLOWER due to thread switching overhead
if thread_time >= single_time * 0.9:
    print("  → Threads did NOT speed up CPU work (GIL in action)")
else:
    print("  → Some speedup observed (unusual for CPython)")
print()

# =============================
# 4. I/O-BOUND TASK: SINGLE THREAD
# =============================

print("=== I/O-Bound: Single Thread ===")
print()

def io_task(seconds):
    """Simulate I/O by sleeping."""
    time.sleep(seconds)

SLEEP_TIME = 0.5

start = time.time()
io_task(SLEEP_TIME)
io_task(SLEEP_TIME)
single_io_time = time.time() - start

print(f"  Two sequential I/O tasks: {single_io_time:.3f}s")
print()

# =============================
# 5. I/O-BOUND TASK: TWO THREADS
# =============================

print("=== I/O-Bound: Two Threads ===")
print()

start = time.time()

t1 = threading.Thread(target=io_task, args=(SLEEP_TIME,))
t2 = threading.Thread(target=io_task, args=(SLEEP_TIME,))

t1.start()
t2.start()
t1.join()
t2.join()

thread_io_time = time.time() - start

print(f"  Two threaded I/O tasks: {thread_io_time:.3f}s")
print(f"  Single thread time:     {single_io_time:.3f}s")
print()

# The GIL is RELEASED during I/O, so both threads run concurrently
if thread_io_time < single_io_time * 0.8:
    print("  → Threads DID speed up I/O work (GIL released during sleep)")
print()

# =============================
# 6. DEMONSTRATING GIL CONTENTION
# =============================

print("=== GIL Contention ===")
print()

# Multiple threads fighting for the GIL

results = {}

def timed_cpu_task(name, n):
    start = time.time()
    total = 0
    for i in range(n):
        total += i
    elapsed = time.time() - start
    results[name] = elapsed

SMALL_COUNT = 5_000_000

# Run 4 threads
threads = []
for i in range(4):
    t = threading.Thread(target=timed_cpu_task,
                         args=(f"Thread-{i+1}", SMALL_COUNT))
    threads.append(t)

start = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
total_wall = time.time() - start

print("  4 threads doing CPU work:")
for name, elapsed in sorted(results.items()):
    print(f"    {name}: {elapsed:.3f}s")
print(f"  Total wall time: {total_wall:.3f}s")
print()
print("  Each thread takes LONGER because they compete for the GIL")
print()

# =============================
# 7. GIL AND THE SOLUTION: MULTIPROCESSING
# =============================

print("=== Solution for CPU-Bound: Multiprocessing ===")
print()

# Each process has its OWN Python interpreter and its OWN GIL
# So processes can truly run in parallel

print("  For CPU-bound tasks:")
print("    ❌ threading — blocked by GIL")
print("    ✅ multiprocessing — each process has own GIL")
print()
print("  For I/O-bound tasks:")
print("    ✅ threading — GIL released during I/O")
print("    ✅ asyncio — single thread, non-blocking I/O")
print()

# (We'll use multiprocessing in the next subtopic)

# =============================
# 8. GIL SWITCH INTERVAL
# =============================

print("=== GIL Switch Interval ===")
print()

# Python switches the GIL between threads periodically
interval = sys.getswitchinterval()
print(f"  Current GIL switch interval: {interval}s")
print(f"  This is {interval * 1000:.1f}ms")
print()

# The switch interval controls how often Python gives
# other threads a chance to run
# Default is usually 5ms (0.005s)

# You can change it (but usually shouldn't):
# sys.setswitchinterval(0.001)  # 1ms — more switching

# =============================
# 9. SUMMARY TABLE
# =============================

print("=== When Does the GIL Matter? ===")
print()

print("  ┌──────────────┬──────────┬────────────────┐")
print("  │ Task Type    │ Threads  │ Processes       │")
print("  ├──────────────┼──────────┼────────────────┤")
print("  │ CPU-bound    │ NO help  │ TRUE parallelism│")
print("  │ I/O-bound    │ Works!   │ Overkill        │")
print("  │ Mixed        │ Partial  │ Best choice     │")
print("  └──────────────┴──────────┴────────────────┘")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Time a CPU-bound task with 1, 2, and 4 threads
#    — notice that more threads doesn't mean faster
# 2. Time an I/O-bound task (time.sleep) with 1, 2, 4 threads
#    — notice that threads DO help here
# 3. Check sys.getswitchinterval() on your machine
# ============================================
