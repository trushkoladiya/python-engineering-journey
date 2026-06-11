# ============================================
# MODULE 18 - SUBTOPIC 5: Thread Basics
# ============================================

# Threads let you run multiple tasks concurrently.
# Best for I/O-bound work (file reading, network, sleeping).

import threading
import time

# =============================
# 1. CREATING A SIMPLE THREAD
# =============================

print("=== Creating a Simple Thread ===")
print()

def greet(name):
    print(f"  Hello from {name}!")

# Create and start a thread
t = threading.Thread(target=greet, args=("Thread-1",))
t.start()
t.join()  # Wait for the thread to finish
print()

# =============================
# 2. THREAD vs MAIN THREAD
# =============================

print("=== Main Thread vs Child Thread ===")
print()

def show_thread_info():
    current = threading.current_thread()
    print(f"  Inside thread: {current.name}")

# Main thread info
print(f"  Main thread: {threading.current_thread().name}")

# Child thread
t = threading.Thread(target=show_thread_info, name="MyWorker")
t.start()
t.join()
print()

# =============================
# 3. MULTIPLE THREADS
# =============================

print("=== Running Multiple Threads ===")
print()

def worker(worker_id, duration):
    print(f"  Worker-{worker_id} starting (will take {duration}s)")
    time.sleep(duration)
    print(f"  Worker-{worker_id} finished")

# Create 4 threads with different durations
threads = []
durations = [0.3, 0.1, 0.4, 0.2]

start = time.time()

for i, dur in enumerate(durations):
    t = threading.Thread(target=worker, args=(i + 1, dur))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

elapsed = time.time() - start
print(f"  All workers done in {elapsed:.3f}s")
print(f"  (Sequential would take {sum(durations):.1f}s)")
print()

# =============================
# 4. THREAD WITH RETURN VALUES
# =============================

print("=== Getting Results from Threads ===")
print()

# Threads don't return values directly.
# Use a shared data structure to collect results.

results = {}

def compute_square(n):
    time.sleep(0.1)  # Simulate work
    results[n] = n * n

threads = []
for num in [2, 5, 8, 11, 14]:
    t = threading.Thread(target=compute_square, args=(num,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"  Results: {results}")
print()

# =============================
# 5. THREAD LIFECYCLE
# =============================

print("=== Thread Lifecycle ===")
print()

def lifecycle_demo():
    time.sleep(0.2)

t = threading.Thread(target=lifecycle_demo, name="LifecycleThread")

print(f"  Before start: alive={t.is_alive()}")

t.start()
print(f"  After start:  alive={t.is_alive()}")

t.join()
print(f"  After join:   alive={t.is_alive()}")
print()

# =============================
# 6. DAEMON THREADS
# =============================

print("=== Daemon Threads ===")
print()

# A daemon thread runs in the background.
# It is killed when the main thread exits.
# Non-daemon threads keep the program alive until they finish.

def background_task():
    for i in range(3):
        print(f"  Background: tick {i + 1}")
        time.sleep(0.1)

# Daemon thread
daemon = threading.Thread(target=background_task, daemon=True)
daemon.start()

# Non-daemon — we wait for it
time.sleep(0.35)  # Let daemon run a bit
print(f"  Daemon alive: {daemon.is_alive()}")
print()

# If we exit without join(), daemon is killed automatically
# For non-daemon threads, Python waits for them

# =============================
# 7. THREAD COUNT AND ENUMERATION
# =============================

print("=== Active Threads ===")
print()

def sleeper(seconds):
    time.sleep(seconds)

# Create a few threads
active_threads = []
for i in range(3):
    t = threading.Thread(target=sleeper, args=(0.5,),
                         name=f"Sleeper-{i+1}")
    active_threads.append(t)
    t.start()

print(f"  Active thread count: {threading.active_count()}")
print(f"  Active threads:")
for t in threading.enumerate():
    print(f"    - {t.name} (daemon={t.daemon})")
print()

for t in active_threads:
    t.join()

print(f"  After join, active count: {threading.active_count()}")
print()

# =============================
# 8. PASSING KEYWORD ARGUMENTS
# =============================

print("=== Thread with kwargs ===")
print()

def describe_person(name, age, city="Unknown"):
    print(f"  {name}, age {age}, from {city}")

t = threading.Thread(
    target=describe_person,
    args=("Trush", 21),
    kwargs={"city": "New York"}
)
t.start()
t.join()
print()

# =============================
# 9. PRACTICAL: CONCURRENT FILE SIMULATION
# =============================

print("=== Practical: Simulating Concurrent Downloads ===")
print()

def download_file(filename, size_mb):
    """Simulate downloading a file."""
    print(f"  Downloading {filename} ({size_mb}MB)...")
    time.sleep(size_mb * 0.1)  # Simulate download time
    print(f"  ✓ {filename} complete")

files = [
    ("report.pdf", 2),
    ("photo.jpg", 1),
    ("video.mp4", 5),
    ("data.csv", 3),
    ("readme.txt", 0.5),
]

# Sequential download
start = time.time()
for name, size in files:
    download_file(name, size)
seq_time = time.time() - start

print(f"\n  Sequential time: {seq_time:.3f}s")
print()

# Concurrent download
start = time.time()
threads = []
for name, size in files:
    t = threading.Thread(target=download_file, args=(name, size))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
conc_time = time.time() - start

print(f"\n  Concurrent time: {conc_time:.3f}s")
print(f"  Speedup: {seq_time / conc_time:.1f}x faster")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create 5 threads that each print a countdown
#    from 3 to 1 with their thread name
# 2. Simulate 10 concurrent API calls (use time.sleep)
#    and compare with sequential execution
# 3. Use daemon threads and observe what happens
#    when the main thread ends early
# ============================================
