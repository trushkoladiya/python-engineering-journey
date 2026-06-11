# ============================================
# MODULE 18 - SUBTOPIC 9: Concurrent Execution Patterns
# ============================================

# Choosing the right concurrency model and using
# concurrent.futures for a unified interface.

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures import as_completed
import threading
import time
import os

# =============================
# 1. ThreadPoolExecutor BASICS
# =============================

print("=== ThreadPoolExecutor Basics ===")
print()

def download_page(url):
    """Simulate downloading a page."""
    time.sleep(0.2)
    return f"Content from {url} ({len(url) * 50} bytes)"

urls = [
    "example.com/home",
    "example.com/about",
    "example.com/products",
    "example.com/contact",
    "example.com/blog",
]

start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(download_page, urls))
elapsed = time.time() - start

for result in results:
    print(f"  {result}")
print(f"  Time: {elapsed:.3f}s (sequential would be ~{len(urls) * 0.2:.1f}s)")
print()

# =============================
# 2. submit() AND Future OBJECTS
# =============================

print("=== submit() and Future Objects ===")
print()

def compute(n):
    time.sleep(0.1 * n)
    return n * n

with ThreadPoolExecutor(max_workers=4) as executor:
    # submit() returns a Future object
    future1 = executor.submit(compute, 3)
    future2 = executor.submit(compute, 5)
    future3 = executor.submit(compute, 2)

    print(f"  future1 done? {future1.done()}")
    print(f"  future2 done? {future2.done()}")

    # .result() blocks until the task completes
    print(f"  future3 result: {future3.result()}")
    print(f"  future1 result: {future1.result()}")
    print(f"  future2 result: {future2.result()}")
print()

# =============================
# 3. as_completed() — RESULTS AS THEY FINISH
# =============================

print("=== as_completed() — Process Results As They Arrive ===")
print()

def process_item(item, delay):
    time.sleep(delay)
    return f"Processed '{item}' in {delay}s"

tasks = [
    ("apple", 0.3),
    ("banana", 0.1),
    ("cherry", 0.4),
    ("date", 0.2),
    ("elderberry", 0.15),
]

with ThreadPoolExecutor(max_workers=4) as executor:
    # Map futures to their task names for identification
    future_to_name = {
        executor.submit(process_item, name, delay): name
        for name, delay in tasks
    }

    # Results come in as tasks complete (not submission order)
    for future in as_completed(future_to_name):
        name = future_to_name[future]
        try:
            result = future.result()
            print(f"  ✓ {result}")
        except Exception as e:
            print(f"  ✗ {name} failed: {e}")
print()

# =============================
# 4. EXCEPTION HANDLING IN FUTURES
# =============================

print("=== Exception Handling in Futures ===")
print()

def risky_task(n):
    if n == 3:
        raise ValueError(f"Task {n} encountered an error!")
    time.sleep(0.1)
    return n * 10

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(risky_task, i): i for i in range(1, 6)}

    for future in as_completed(futures):
        task_id = futures[future]
        try:
            result = future.result()
            print(f"  Task {task_id}: result = {result}")
        except ValueError as e:
            print(f"  Task {task_id}: ERROR — {e}")
print()

# =============================
# 5. ProcessPoolExecutor FOR CPU WORK
# =============================

print("=== ProcessPoolExecutor for CPU Work ===")
print()

def cpu_intensive(n):
    """A CPU-bound task."""
    total = 0
    for i in range(n):
        total += i * i
    return total

if __name__ == "__main__":
    COUNT = 2_000_000

    # Sequential
    start = time.time()
    sequential_results = [cpu_intensive(COUNT) for _ in range(4)]
    seq_time = time.time() - start
    print(f"  Sequential (4 tasks): {seq_time:.3f}s")

    # Process pool
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        parallel_results = list(executor.map(cpu_intensive, [COUNT] * 4))
    proc_time = time.time() - start
    print(f"  ProcessPool (4 tasks): {proc_time:.3f}s")

    # Thread pool (for comparison — GIL limits this)
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        thread_results = list(executor.map(cpu_intensive, [COUNT] * 4))
    thread_time = time.time() - start
    print(f"  ThreadPool (4 tasks): {thread_time:.3f}s")

    print()
    print(f"  Process speedup over sequential: {seq_time / proc_time:.1f}x")
    print(f"  Thread speedup over sequential: {seq_time / thread_time:.1f}x")
    print(f"  (Threads limited by GIL for CPU work)")
    print()

    # =============================
    # 6. PATTERN: MAP-REDUCE WITH POOL
    # =============================

    print("=== Pattern: Map-Reduce ===")
    print()

    def count_letters(text):
        """Count letters in a text chunk."""
        counts = {}
        for char in text.lower():
            if char.isalpha():
                counts[char] = counts.get(char, 0) + 1
        return counts

    def merge_counts(counts_list):
        """Merge multiple count dictionaries."""
        merged = {}
        for counts in counts_list:
            for key, value in counts.items():
                merged[key] = merged.get(key, 0) + value
        return merged

    # Split text into chunks
    text = "Python is an amazing programming language for learning"
    words = text.split()
    chunks = [" ".join(words[i:i+3]) for i in range(0, len(words), 3)]

    print(f"  Text: '{text}'")
    print(f"  Chunks: {chunks}")

    # Map phase: count letters in each chunk (parallel)
    with ProcessPoolExecutor(max_workers=2) as executor:
        chunk_counts = list(executor.map(count_letters, chunks))

    # Reduce phase: merge all counts
    final_counts = merge_counts(chunk_counts)
    sorted_counts = dict(sorted(final_counts.items(), key=lambda x: -x[1]))

    print(f"  Top 5 letters: {dict(list(sorted_counts.items())[:5])}")
    print()

    # =============================
    # 7. PATTERN: TIMEOUT ON FUTURES
    # =============================

    print("=== Pattern: Timeout on Futures ===")
    print()

    def slow_task(task_id):
        time.sleep(task_id * 0.3)
        return f"Task {task_id} complete"

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(slow_task, i): i for i in range(1, 5)}

        for future in as_completed(futures, timeout=1.0):
            task_id = futures[future]
            print(f"  Completed: Task {task_id} → {future.result()}")

    print()

    # =============================
    # 8. PATTERN: BATCH PROCESSING
    # =============================

    print("=== Pattern: Batch Processing ===")
    print()

    def process_batch(batch):
        """Process a batch of items."""
        results = []
        for item in batch:
            results.append(item ** 2)
        time.sleep(0.1)  # Simulate work
        return results

    # Split data into batches
    data = list(range(1, 21))
    batch_size = 5
    batches = [data[i:i+batch_size] for i in range(0, len(data), batch_size)]

    print(f"  Data: {data}")
    print(f"  Batches: {batches}")

    with ThreadPoolExecutor(max_workers=len(batches)) as executor:
        batch_results = list(executor.map(process_batch, batches))

    # Flatten results
    all_results = [item for batch in batch_results for item in batch]
    print(f"  Results: {all_results}")
    print()

    # =============================
    # 9. DECISION CHEAT SHEET
    # =============================

    print("=== Concurrency Decision Cheat Sheet ===")
    print()

    print("  ┌─────────────────────────┬────────────────────────────┐")
    print("  │ Scenario                │ Best Choice                │")
    print("  ├─────────────────────────┼────────────────────────────┤")
    print("  │ Download 10 files       │ ThreadPoolExecutor         │")
    print("  │ Download 1000 URLs      │ asyncio                    │")
    print("  │ Process images          │ ProcessPoolExecutor        │")
    print("  │ Compute statistics      │ ProcessPoolExecutor        │")
    print("  │ Chat server             │ asyncio                    │")
    print("  │ Database queries        │ ThreadPoolExecutor         │")
    print("  │ Machine learning        │ ProcessPoolExecutor        │")
    print("  │ Web scraping            │ asyncio or ThreadPool      │")
    print("  └─────────────────────────┴────────────────────────────┘")
    print()

    # ============================================
    # TRY IT YOURSELF:
    # 1. Use ThreadPoolExecutor to simulate downloading
    #    20 URLs concurrently with max 5 workers
    # 2. Use ProcessPoolExecutor to compute prime numbers
    #    in parallel
    # 3. Use as_completed() to show a progress indicator
    #    as tasks complete
    # ============================================
