# ============================================
# MODULE 15 - SUBTOPIC 11: Performance & Memory Concepts
# ============================================

# Understanding when to use generators vs lists
# based on memory and speed.

import sys
import time

# =============================
# 1. MEMORY COMPARISON
# =============================

print("=== Memory: List vs Generator ===")
print()

# List: stores ALL values
list_10k = [x for x in range(10_000)]
list_100k = [x for x in range(100_000)]
list_1m = [x for x in range(1_000_000)]

# Generator: stores almost nothing
gen_10k = (x for x in range(10_000))
gen_100k = (x for x in range(100_000))
gen_1m = (x for x in range(1_000_000))

print(f"  {'Items':<12} {'List Size':>12} {'Generator Size':>15}")
print(f"  {'-'*12} {'-'*12} {'-'*15}")
print(f"  {'10,000':<12} {sys.getsizeof(list_10k):>10,} B {sys.getsizeof(gen_10k):>13,} B")
print(f"  {'100,000':<12} {sys.getsizeof(list_100k):>10,} B {sys.getsizeof(gen_100k):>13,} B")
print(f"  {'1,000,000':<12} {sys.getsizeof(list_1m):>10,} B {sys.getsizeof(gen_1m):>13,} B")
print()
print("  → Generator size is CONSTANT regardless of data size!")
print()

# =============================
# 2. RANGE vs LIST OF RANGE
# =============================

print("=== range() vs list(range()) ===")
print()

# range is lazy (like a generator)
r = range(1_000_000)
l = list(range(1_000_000))

print(f"  range(1M) size: {sys.getsizeof(r):>10,} bytes")
print(f"  list(range(1M)) size: {sys.getsizeof(l):>10,} bytes")
print(f"  → range is {sys.getsizeof(l) // sys.getsizeof(r):,}x more memory-efficient!")
print()

# =============================
# 3. SPEED: SUM COMPARISON
# =============================

print("=== Speed: Summing Values ===")
print()

n = 1_000_000

# List
start = time.perf_counter()
total_list = sum([x for x in range(n)])
time_list = time.perf_counter() - start

# Generator
start = time.perf_counter()
total_gen = sum(x for x in range(n))
time_gen = time.perf_counter() - start

# Range (optimized)
start = time.perf_counter()
total_range = sum(range(n))
time_range = time.perf_counter() - start

print(f"  sum([x for x in range(1M)]): {time_list:.4f}s  (list)")
print(f"  sum(x for x in range(1M)):   {time_gen:.4f}s  (generator)")
print(f"  sum(range(1M)):              {time_range:.4f}s  (range)")
print(f"  All equal? {total_list == total_gen == total_range}")
print()

# =============================
# 4. SPEED: EARLY STOPPING
# =============================

print("=== Speed: Early Stopping ===")
print()

# Finding first item > threshold

def find_first_list(data, threshold):
    """Eager approach: create full list first."""
    squared = [x**2 for x in data]
    for val in squared:
        if val > threshold:
            return val
    return None

def find_first_gen(data, threshold):
    """Lazy approach: compute on demand."""
    squared = (x**2 for x in data)
    for val in squared:
        if val > threshold:
            return val
    return None

big_data = range(1_000_000)
threshold = 100

# List approach: computes ALL 1M squares first
start = time.perf_counter()
result_list = find_first_list(big_data, threshold)
time_list = time.perf_counter() - start

# Generator approach: stops as soon as it finds the answer
start = time.perf_counter()
result_gen = find_first_gen(big_data, threshold)
time_gen = time.perf_counter() - start

print(f"  List approach:      {time_list:.6f}s (computed ALL squares)")
print(f"  Generator approach: {time_gen:.6f}s (stopped early!)")
print(f"  Both found: {result_list} == {result_gen}")
if time_list > 0:
    print(f"  Generator was ~{time_list/max(time_gen, 0.000001):.0f}x faster!")
print()

# =============================
# 5. MEMORY: NESTED STRUCTURES
# =============================

print("=== Memory: Practical Example ===")
print()

# Processing "records" — each is a dict

# Eager: all records in memory
def create_records_list(n):
    return [{"id": i, "value": i * 10, "status": "active"} for i in range(n)]

# Lazy: one record at a time
def create_records_gen(n):
    for i in range(n):
        yield {"id": i, "value": i * 10, "status": "active"}

# Compare
n = 100_000
records_list = create_records_list(n)
records_gen = create_records_gen(n)

print(f"  {n:,} records as list: {sys.getsizeof(records_list):>10,} bytes (+ dict contents)")
print(f"  {n:,} records as gen:  {sys.getsizeof(records_gen):>10,} bytes")
print()

# =============================
# 6. TRADE-OFFS SUMMARY
# =============================

print("=== Generator vs List: Trade-offs ===")
print()

print("  ┌──────────────────┬──────────────┬──────────────┐")
print("  │ Feature          │ List         │ Generator    │")
print("  ├──────────────────┼──────────────┼──────────────┤")
print("  │ Memory           │ O(n)         │ O(1)         │")
print("  │ Random access    │ ✅ data[i]   │ ❌ no        │")
print("  │ Multiple passes  │ ✅ yes       │ ❌ exhausts  │")
print("  │ len()            │ ✅ yes       │ ❌ no        │")
print("  │ Early stopping   │ Wasteful     │ ✅ efficient │")
print("  │ Infinite data    │ ❌ impossible│ ✅ yes       │")
print("  │ Slicing          │ ✅ data[2:5] │ Use islice   │")
print("  └──────────────────┴──────────────┴──────────────┘")
print()

# =============================
# 7. PRACTICAL GUIDELINES
# =============================

print("=== Practical Guidelines ===")
print()

print("  Use GENERATORS when:")
print("    • Processing large files line by line")
print("    • Searching for first match in big data")
print("    • Building data transformation pipelines")
print("    • Working with infinite or streaming data")
print("    • Memory is a concern")
print()
print("  Use LISTS when:")
print("    • Data is small (< 10,000 items typically)")
print("    • Need to access items by index")
print("    • Need to sort, reverse, or iterate multiple times")
print("    • Need len() or other list operations")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Compare memory of [x**2 for x in range(1M)] vs (x**2 for ...)
# 2. Time: finding first prime > 10000 with list vs generator
# 3. Profile a data pipeline with generators vs lists
# ============================================
