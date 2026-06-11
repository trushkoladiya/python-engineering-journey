# ============================================
# MODULE 16 - SUBTOPIC 16: Performance & Optimization
# ============================================

# Functional programming gives us tools for
# efficient data processing — lazy evaluation,
# generators, and avoiding unnecessary copies.

import time
import sys

# =============================
# 1. LAZY vs EAGER EVALUATION
# =============================

print("=== Lazy vs Eager Evaluation ===")
print()

# EAGER: list comprehension creates everything at once
eager_squares = [x ** 2 for x in range(10)]
print(f"  Eager (list): {eager_squares}")
print(f"  Type: {type(eager_squares)}")
print()

# LAZY: generator expression creates nothing until consumed
lazy_squares = (x ** 2 for x in range(10))
print(f"  Lazy (generator): {lazy_squares}")
print(f"  Type: {type(lazy_squares)}")
print(f"  Consumed: {list(lazy_squares)}")
print()

# =============================
# 2. MEMORY COMPARISON
# =============================

print("=== Memory Comparison ===")
print()

# Eager: stores all 100,000 items in memory
eager = [x ** 2 for x in range(100_000)]
eager_size = sys.getsizeof(eager)

# Lazy: stores nothing — generates on demand
lazy = (x ** 2 for x in range(100_000))
lazy_size = sys.getsizeof(lazy)

print(f"  List of 100K squares: {eager_size:,} bytes")
print(f"  Generator of 100K squares: {lazy_size:,} bytes")
print(f"  Memory savings: {eager_size / lazy_size:.0f}x less")
print()

# =============================
# 3. LAZY CHAINING (NO INTERMEDIATE LISTS)
# =============================

print("=== Lazy Chaining ===")
print()

data = range(1, 1_000_001)   # 1 to 1 million

# BAD: creates 3 intermediate lists (lots of memory!)
# step1 = [x for x in data if x % 2 == 0]
# step2 = [x ** 2 for x in step1]
# step3 = [x for x in step2 if x > 1000]

# GOOD: lazy chain — no intermediate lists
step1 = filter(lambda x: x % 2 == 0, data)      # lazy
step2 = map(lambda x: x ** 2, step1)             # lazy
step3 = filter(lambda x: x > 1000, step2)        # lazy

# Only materialize the first 5 results
from itertools import islice
first_5 = list(islice(step3, 5))
print(f"  First 5 results from lazy chain: {first_5}")
print("  (Processed million items without storing them all!)")
print()

# =============================
# 4. EARLY TERMINATION
# =============================

print("=== Early Termination ===")
print()

def expensive_computation(x):
    """Simulate an expensive operation."""
    return x ** 3 + x ** 2 + x + 1

# Using generator + next to find FIRST match
def find_first_above(data, threshold):
    """Find first computed value above threshold."""
    return next(
        (expensive_computation(x) for x in data if expensive_computation(x) > threshold),
        None
    )

# Only processes items until it finds the first match!
result = find_first_above(range(1, 1000), 100)
print(f"  First value > 100: {result}")

# With any() — stops at first True
has_large = any(expensive_computation(x) > 1000 for x in range(1, 1000))
print(f"  Any value > 1000? {has_large}")
print()

# =============================
# 5. TIMING: EAGER vs LAZY
# =============================

print("=== Timing: Eager vs Lazy ===")
print()

n = 500_000

# EAGER: compute all, then take first 10
start = time.perf_counter()
eager_result = [x ** 2 for x in range(n)][:10]
eager_time = time.perf_counter() - start

# LAZY: only compute what we need
start = time.perf_counter()
lazy_gen = (x ** 2 for x in range(n))
lazy_result = [next(lazy_gen) for _ in range(10)]
lazy_time = time.perf_counter() - start

print(f"  Eager (compute all, take 10): {eager_time:.6f}s")
print(f"  Lazy  (compute only 10):      {lazy_time:.6f}s")
print(f"  Results match: {eager_result == lazy_result}")
print()

# =============================
# 6. itertools FOR EFFICIENT PROCESSING
# =============================

print("=== itertools Essentials ===")
print()

from itertools import chain, islice, takewhile, dropwhile, accumulate

# chain — combine multiple iterables without copying
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
combined = list(chain(a, b, c))
print(f"  chain: {combined}")

# islice — take a slice from an iterator
big_range = iter(range(100))
first_5 = list(islice(big_range, 5))
print(f"  islice(range(100), 5): {first_5}")

# takewhile — take while condition is True
nums = [2, 4, 6, 7, 8, 10]
evens = list(takewhile(lambda x: x % 2 == 0, nums))
print(f"  takewhile(even, {nums}): {evens}")

# dropwhile — drop while condition is True
after = list(dropwhile(lambda x: x < 5, [1, 3, 5, 2, 7]))
print(f"  dropwhile(<5, [1,3,5,2,7]): {after}")

# accumulate — running total
data = [1, 2, 3, 4, 5]
running_sum = list(accumulate(data))
print(f"  accumulate({data}): {running_sum}")
print()

# =============================
# 7. GENERATOR PIPELINES
# =============================

print("=== Generator Pipelines ===")
print()

def generate_data(n):
    """Generate n random-like numbers."""
    for i in range(n):
        yield (i * 7 + 3) % 100

def filter_above(threshold, data):
    """Keep values above threshold."""
    for value in data:
        if value > threshold:
            yield value

def transform(factor, data):
    """Multiply each value by factor."""
    for value in data:
        yield value * factor

def take(n, data):
    """Take first n values."""
    count = 0
    for value in data:
        if count >= n:
            break
        yield value
        count += 1

# Build a lazy pipeline
pipeline = take(8,
    transform(2,
        filter_above(50,
            generate_data(1000))))

# Nothing computed until we consume!
result = list(pipeline)
print(f"  Pipeline result: {result}")
print("  (Processed 1000 items lazily, kept only 8)")
print()

# =============================
# 8. AVOID COMMON PERFORMANCE PITFALLS
# =============================

print("=== Common Performance Pitfalls ===")
print()

# PITFALL 1: Repeated list creation in loops
print("  Pitfall 1: Repeated list concatenation")
# BAD:  result = []; for x in data: result = result + [x]
# GOOD: result = []; for x in data: result.append(x)
# BEST: result = [x for x in data]  (if transforming)

# PITFALL 2: Converting to list unnecessarily
print("  Pitfall 2: Unnecessary list conversion")
# BAD:  total = sum(list(filter(lambda x: x > 0, data)))
# GOOD: total = sum(filter(lambda x: x > 0, data))
# (sum() can consume iterators directly!)

# PITFALL 3: Multiple passes over data
print("  Pitfall 3: Multiple passes")
data = range(10000)
# BAD: two passes
# count = len([x for x in data if x > 5000])
# total = sum(x for x in data if x > 5000)
# GOOD: single pass
count = 0
total = 0
for x in data:
    if x > 5000:
        count += 1
        total += x
print(f"  Single pass: count={count}, total={total}")
print()

# =============================
# 9. WHEN TO OPTIMIZE
# =============================

print("=== When to Optimize ===")
print()

print("  ✓ Use lazy evaluation for LARGE datasets")
print("  ✓ Use generators when you might not need ALL results")
print("  ✓ Chain map/filter instead of creating intermediate lists")
print("  ✓ Use itertools for complex iterator operations")
print()
print("  ✗ Don't optimize small datasets (readability first!)")
print("  ✗ Don't make code complex just to avoid a list")
print("  ✗ Don't guess — profile to find real bottlenecks")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Process a range of 1 million numbers lazily —
#    filter, transform, take first 10
# 2. Compare memory usage of a list vs generator
#    for different sizes
# 3. Build a generator pipeline that processes text
#    line by line
# ============================================
