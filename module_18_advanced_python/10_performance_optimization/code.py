# ============================================
# MODULE 18 - SUBTOPIC 10: Performance Optimization
# ============================================

# Find bottlenecks, measure performance, and optimize
# the parts that matter most.

import time
import timeit
import cProfile
import io
import pstats

# =============================
# 1. BASIC TIMING
# =============================

print("=== Basic Timing with time.time() ===")
print()

def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

def fast_sum(n):
    return sum(range(n))

n = 1_000_000

start = time.time()
slow_sum(n)
slow_time = time.time() - start

start = time.time()
fast_sum(n)
fast_time = time.time() - start

print(f"  Manual loop: {slow_time:.4f}s")
print(f"  Built-in sum: {fast_time:.4f}s")
print(f"  Speedup: {slow_time / fast_time:.1f}x")
print()

# =============================
# 2. timeit FOR MICRO-BENCHMARKS
# =============================

print("=== timeit — Precise Micro-Benchmarks ===")
print()

# timeit runs code many times for accurate measurement

# Method 1: String concatenation with +
t1 = timeit.timeit(
    '"-".join([str(i) for i in range(100)])',
    number=10_000
)

# Method 2: String concatenation with join
t2 = timeit.timeit(
    'result = ""; [result := result + "-" + str(i) for i in range(100)]',
    number=10_000
)

print(f"  join():        {t1:.4f}s (10,000 runs)")
print(f"  concatenation: {t2:.4f}s (10,000 runs)")
print()

# =============================
# 3. COMPARING APPROACHES WITH timeit
# =============================

print("=== Comparing Approaches ===")
print()

# List comprehension vs loop with append
t_comp = timeit.timeit(
    '[x**2 for x in range(1000)]',
    number=5000
)

t_loop = timeit.timeit('''
result = []
for x in range(1000):
    result.append(x**2)
''', number=5000)

t_map = timeit.timeit(
    'list(map(lambda x: x**2, range(1000)))',
    number=5000
)

print(f"  List comprehension: {t_comp:.4f}s")
print(f"  Loop + append:      {t_loop:.4f}s")
print(f"  map + lambda:       {t_map:.4f}s")
print()

# =============================
# 4. PROFILING WITH cProfile
# =============================

print("=== Profiling with cProfile ===")
print()

def find_primes(limit):
    """Find all primes up to limit."""
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes

def is_prime(n):
    """Check if n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Capture profile output
profiler = cProfile.Profile()
profiler.enable()
result = find_primes(5000)
profiler.disable()

# Print profile results
stream = io.StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 functions
print(stream.getvalue())

print(f"  Found {len(result)} primes up to 5000")
print()

# =============================
# 5. OPTIMIZATION: BUILT-IN FUNCTIONS
# =============================

print("=== Built-in Functions Are Faster ===")
print()

data = list(range(100_000))

# Finding max — manual vs built-in
start = time.time()
manual_max = data[0]
for x in data:
    if x > manual_max:
        manual_max = x
manual_time = time.time() - start

start = time.time()
builtin_max = max(data)
builtin_time = time.time() - start

print(f"  Manual max: {manual_time:.6f}s → {manual_max}")
print(f"  Built-in max: {builtin_time:.6f}s → {builtin_max}")
print()

# =============================
# 6. OPTIMIZATION: DATA STRUCTURE CHOICE
# =============================

print("=== Right Data Structure Matters ===")
print()

import random

# Membership test: list vs set
test_data = list(range(100_000))
test_set = set(test_data)
search_items = [random.randint(0, 200_000) for _ in range(1000)]

# List lookup
start = time.time()
list_found = sum(1 for item in search_items if item in test_data)
list_time = time.time() - start

# Set lookup
start = time.time()
set_found = sum(1 for item in search_items if item in test_set)
set_time = time.time() - start

print(f"  List lookup (1000 searches): {list_time:.4f}s")
print(f"  Set lookup (1000 searches):  {set_time:.6f}s")
if set_time > 0:
    print(f"  Set is {list_time / set_time:.0f}x faster!")
print()

# =============================
# 7. OPTIMIZATION: AVOID REPEATED WORK
# =============================

print("=== Avoid Repeated Computation ===")
print()

# Bad: recomputing length each iteration
def bad_average(data):
    total = 0
    for i in range(len(data)):
        total += data[i]
    return total / len(data)

# Good: compute once, reuse
def good_average(data):
    n = len(data)
    total = sum(data)
    return total / n

data = list(range(100_000))

t_bad = timeit.timeit(lambda: bad_average(data), number=100)
t_good = timeit.timeit(lambda: good_average(data), number=100)

print(f"  Bad approach:  {t_bad:.4f}s")
print(f"  Good approach: {t_good:.4f}s")
print()

# =============================
# 8. OPTIMIZATION: STRING BUILDING
# =============================

print("=== String Building: join vs concatenation ===")
print()

n = 10_000

# Bad: string concatenation in a loop
t_concat = timeit.timeit('''
result = ""
for i in range(1000):
    result += str(i)
''', number=500)

# Good: build list then join
t_join = timeit.timeit('''
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)
''', number=500)

# Best: join with comprehension
t_comp = timeit.timeit(
    '"".join(str(i) for i in range(1000))',
    number=500
)

print(f"  String +=:       {t_concat:.4f}s")
print(f"  List + join:     {t_join:.4f}s")
print(f"  Join + genexpr:  {t_comp:.4f}s")
print()

# =============================
# 9. OPTIMIZATION: LOCAL VARIABLES
# =============================

print("=== Local Variables Are Faster ===")
print()

import math

# Global access (slower)
def global_sqrt(data):
    return [math.sqrt(x) for x in data]

# Local access (faster)
def local_sqrt(data):
    sqrt = math.sqrt  # Cache the function locally
    return [sqrt(x) for x in data]

data = list(range(1, 50_001))

t_global = timeit.timeit(lambda: global_sqrt(data), number=50)
t_local = timeit.timeit(lambda: local_sqrt(data), number=50)

print(f"  Global lookup: {t_global:.4f}s")
print(f"  Local lookup:  {t_local:.4f}s")
print()

# Python looks up local variables faster than global/module ones

# =============================
# 10. OPTIMIZATION SUMMARY
# =============================

print("=== Optimization Summary ===")
print()

tips = [
    ("Measure first", "Use timeit, cProfile before optimizing"),
    ("Built-in functions", "sum(), max(), min(), sorted() are C-speed"),
    ("Right data structure", "set for lookups, dict for key-value"),
    ("List comprehensions", "Faster than loop + append"),
    ("join() for strings", "Never concatenate in a loop"),
    ("Local variable cache", "Assign frequently-used functions locally"),
    ("Avoid repeated work", "Compute once, use many times"),
    ("Generator expressions", "Save memory for large data"),
]

for technique, description in tips:
    print(f"  • {technique:25s} → {description}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Profile a function of your own with cProfile
# 2. Compare dict lookup vs list lookup for 10,000 items
# 3. Use timeit to compare three ways of filtering a list:
#    loop, list comprehension, and filter()
# ============================================
