# ============================================
# MODULE 18 - SUBTOPIC 7: Multiprocessing
# ============================================

# Multiprocessing creates separate processes with their own GIL.
# This achieves TRUE parallel execution for CPU-bound tasks.

from multiprocessing import Process, Queue, Pool, current_process
import time
import os

# =============================
# 1. CREATING A PROCESS
# =============================

def greet(name):
    pid = os.getpid()
    print(f"  Hello from {name} (PID: {pid})")

if __name__ == "__main__":
    # All multiprocessing code must be inside if __name__ == "__main__"
    # This prevents infinite process spawning on some platforms

    print("=== Creating a Process ===")
    print()
    print(f"  Main process PID: {os.getpid()}")

    p = Process(target=greet, args=("Process-1",))
    p.start()
    p.join()
    print()

    # =============================
    # 2. MULTIPLE PROCESSES
    # =============================

    print("=== Multiple Processes ===")
    print()

    def worker(worker_id, duration):
        pid = os.getpid()
        print(f"  Worker-{worker_id} (PID: {pid}) starting")
        # Simulate CPU work
        total = 0
        for i in range(int(duration * 1_000_000)):
            total += i
        print(f"  Worker-{worker_id} finished")

    processes = []
    start = time.time()

    for i in range(4):
        p = Process(target=worker, args=(i + 1, 1))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    elapsed = time.time() - start
    print(f"  4 processes completed in {elapsed:.3f}s")
    print()

    # =============================
    # 3. CPU-BOUND: PROCESS vs SEQUENTIAL
    # =============================

    print("=== CPU-Bound: Processes vs Sequential ===")
    print()

    def cpu_work(n):
        """A CPU-intensive task."""
        total = 0
        for i in range(n):
            total += i * i
        return total

    COUNT = 5_000_000

    # Sequential
    start = time.time()
    cpu_work(COUNT)
    cpu_work(COUNT)
    seq_time = time.time() - start
    print(f"  Sequential (2 tasks): {seq_time:.3f}s")

    # Parallel with processes
    start = time.time()
    p1 = Process(target=cpu_work, args=(COUNT,))
    p2 = Process(target=cpu_work, args=(COUNT,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    par_time = time.time() - start
    print(f"  Parallel (2 processes): {par_time:.3f}s")

    if par_time < seq_time:
        print(f"  Speedup: {seq_time / par_time:.1f}x faster!")
    print()

    # =============================
    # 4. QUEUE — INTER-PROCESS COMMUNICATION
    # =============================

    print("=== Queue: Inter-Process Communication ===")
    print()

    def producer(queue, items):
        for item in items:
            queue.put(item)
            print(f"  Produced: {item}")
        queue.put(None)  # Sentinel to signal "done"

    def consumer(queue):
        results = []
        while True:
            item = queue.get()
            if item is None:
                break
            results.append(item * 2)
            print(f"  Consumed: {item} → {item * 2}")
        return results

    q = Queue()

    prod = Process(target=producer, args=(q, [1, 2, 3, 4, 5]))
    cons = Process(target=consumer, args=(q,))

    prod.start()
    cons.start()
    prod.join()
    cons.join()
    print()

    # =============================
    # 5. POOL — EASY PARALLEL MAP
    # =============================

    print("=== Pool: Parallel Map ===")
    print()

    def square(n):
        return n * n

    with Pool(processes=4) as pool:
        numbers = list(range(1, 11))
        results = pool.map(square, numbers)
        print(f"  Numbers: {numbers}")
        print(f"  Squares: {results}")
    print()

    # =============================
    # 6. POOL WITH COMPLEX FUNCTIONS
    # =============================

    print("=== Pool: Processing Data ===")
    print()

    def process_item(item):
        """Simulate processing an item."""
        time.sleep(0.1)  # Simulate work
        return {"original": item, "processed": item.upper(), "length": len(item)}

    items = ["apple", "banana", "cherry", "date", "elderberry",
             "fig", "grape", "honeydew"]

    start = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(process_item, items)
    elapsed = time.time() - start

    for r in results:
        print(f"  {r['original']:>12} → {r['processed']:<12} (len: {r['length']})")

    print(f"  Processed {len(items)} items in {elapsed:.3f}s")
    print(f"  (Sequential would take ~{len(items) * 0.1:.1f}s)")
    print()

    # =============================
    # 7. POOL WITH starmap (MULTIPLE ARGUMENTS)
    # =============================

    print("=== Pool: starmap (Multiple Args) ===")
    print()

    def add(a, b):
        return a + b

    pairs = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]

    with Pool(processes=2) as pool:
        results = pool.starmap(add, pairs)
        print(f"  Pairs: {pairs}")
        print(f"  Sums:  {results}")
    print()

    # =============================
    # 8. PROCESS INFORMATION
    # =============================

    print("=== Process Information ===")
    print()

    def show_info():
        proc = current_process()
        print(f"  Name: {proc.name}")
        print(f"  PID: {os.getpid()}")
        print(f"  Parent PID: {os.getppid()}")

    print("  Main process:")
    print(f"  PID: {os.getpid()}")
    print()

    print("  Child process:")
    p = Process(target=show_info, name="InfoWorker")
    p.start()
    p.join()
    print()

    # =============================
    # 9. WHEN TO USE WHAT
    # =============================

    print("=== When to Use What ===")
    print()

    print("  ┌──────────────────┬────────────────────────┐")
    print("  │ Situation        │ Best Tool              │")
    print("  ├──────────────────┼────────────────────────┤")
    print("  │ CPU-bound work   │ multiprocessing / Pool │")
    print("  │ I/O-bound work   │ threading / asyncio    │")
    print("  │ Simple parallel  │ Pool.map()             │")
    print("  │ Shared state     │ Queue / Manager        │")
    print("  │ Many I/O tasks   │ asyncio                │")
    print("  └──────────────────┴────────────────────────┘")
    print()

    # ============================================
    # TRY IT YOURSELF:
    # 1. Use Pool.map() to compute factorials of 1-20
    # 2. Create a producer-consumer pipeline with Queue
    # 3. Compare execution time of a CPU-heavy task
    #    using threading vs multiprocessing
    # ============================================
