# ============================================
# MODULE 17 - SUBTOPIC 24: Complexity Analysis (Deeper)
# ============================================

# Going beyond basic Big-O: best/average/worst case,
# amortized analysis, and auxiliary space.

import time
import random
import math

# =============================
# 1. BEST, AVERAGE, WORST CASE
# =============================

print("=== Best, Average, Worst Case ===")
print()

def linear_search_counted(items, target):
    """Linear search with step counting."""
    for i in range(len(items)):
        if items[i] == target:
            return i, i + 1    # index, steps
    return -1, len(items)

data = list(range(1000))

# Best case: target is first
_, steps_best = linear_search_counted(data, 0)
print(f"  Linear search (n=1000):")
print(f"    Best case (first):  {steps_best} steps")

# Average case: target in middle
_, steps_avg = linear_search_counted(data, 500)
print(f"    Average case (mid):  {steps_avg} steps")

# Worst case: target is last
_, steps_worst = linear_search_counted(data, 999)
print(f"    Worst case (last):  {steps_worst} steps")
print()

# =============================
# 2. INSERTION SORT — CASE ANALYSIS
# =============================

print("=== Insertion Sort — Case Analysis ===")
print()

def insertion_sort_count(items):
    """Count comparisons for insertion sort."""
    arr = items[:]
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        if j >= 0:
            comparisons += 1
    return comparisons

n = 500

# Best: already sorted → O(n)
best = list(range(n))
comps_best = insertion_sort_count(best)

# Worst: reverse sorted → O(n²)
worst = list(range(n, 0, -1))
comps_worst = insertion_sort_count(worst)

# Average: random → O(n²)
avg = random.sample(range(n * 10), n)
comps_avg = insertion_sort_count(avg)

print(f"  Insertion sort (n={n}):")
print(f"    Best  (sorted):  {comps_best:>8,} comparisons  ≈ O(n)")
print(f"    Average (random): {comps_avg:>8,} comparisons  ≈ O(n²)")
print(f"    Worst  (reverse): {comps_worst:>8,} comparisons  ≈ O(n²)")
print(f"    n²/2 = {n*n//2:>8,} (theoretical average)")
print()

# =============================
# 3. AMORTIZED ANALYSIS — LIST APPEND
# =============================

print("=== Amortized Analysis — List Append ===")
print()

# Python's list.append() is O(1) amortized
# It occasionally needs to resize the internal array

import sys

sizes = []
lst = []
for i in range(100):
    lst.append(i)
    sizes.append(sys.getsizeof(lst))

# Show size jumps (when resizing happens)
print("  List size in memory as elements are added:")
prev_size = 0
for i in range(0, 100, 10):
    size = sizes[i]
    resized = " ← resized!" if size != prev_size and i > 0 else ""
    print(f"    {i+1:3} elements: {size} bytes{resized}")
    prev_size = size
print()
print("  → Append is O(1) amortized: fast most times,")
print("    occasionally O(n) when resizing, but averages to O(1)")
print()

# =============================
# 4. AUXILIARY SPACE
# =============================

print("=== Auxiliary Space ===")
print()

# O(1) auxiliary — in-place
def reverse_in_place(items):
    """Reverse using O(1) extra space."""
    left, right = 0, len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1

# O(n) auxiliary — new list
def reverse_copy(items):
    """Reverse using O(n) extra space."""
    return items[::-1]

data = [1, 2, 3, 4, 5]
print(f"  reverse_in_place: O(1) aux space (modifies original)")
print(f"  reverse_copy:     O(n) aux space (creates new list)")
print()

# Compare sorting space usage
print("  Sorting algorithms — space complexity:")
algorithms = [
    ("Bubble sort", "O(1)", "In-place swaps"),
    ("Selection sort", "O(1)", "In-place swaps"),
    ("Insertion sort", "O(1)", "In-place shifts"),
    ("Merge sort", "O(n)", "Creates temp arrays during merge"),
    ("Quick sort", "O(log n)", "Recursion stack depth"),
    ("Python sorted()", "O(n)", "Timsort uses temp storage"),
]

for name, space, note in algorithms:
    print(f"    {name:18} {space:10} — {note}")
print()

# =============================
# 5. GROWTH RATE COMPARISON
# =============================

print("=== Growth Rate Comparison ===")
print()

print("  Operations for different n values:")
print(f"  {'n':>10} | {'O(1)':>10} | {'O(log n)':>10} | {'O(n)':>10} | "
      f"{'O(n log n)':>12} | {'O(n²)':>12} | {'O(2ⁿ)':>15}")
print("  " + "-" * 90)

for n in [10, 100, 1000, 10_000, 100_000]:
    log_n = int(math.log2(n)) if n > 0 else 0
    n_log_n = n * log_n
    n_sq = n * n
    two_n = "overflow" if n > 30 else str(2 ** n)

    print(f"  {n:>10,} | {1:>10} | {log_n:>10} | {n:>10,} | "
          f"{n_log_n:>12,} | {n_sq:>12,} | {two_n:>15}")
print()

# =============================
# 6. MEASURING REAL PERFORMANCE
# =============================

print("=== Measuring Real Performance ===")
print()

def measure_growth(func, sizes, setup):
    """Measure how time grows with input size."""
    times = []
    for size in sizes:
        data = setup(size)
        start = time.time()
        func(data)
        elapsed = time.time() - start
        times.append(elapsed)
    return times

# O(n) — linear
def sum_list(items):
    total = 0
    for x in items:
        total += x
    return total

# O(n²) — quadratic
def has_dup_brute(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False

sizes = [1000, 2000, 4000, 8000]

print("  O(n) — summing list:")
times_linear = measure_growth(sum_list, sizes, lambda n: list(range(n)))
for size, t in zip(sizes, times_linear):
    print(f"    n={size:>5}: {t:.6f}s")
print(f"    Ratio (8000/1000): {times_linear[-1]/times_linear[0]:.1f}x "
      f"(expected ~8x for O(n))")
print()

print("  O(n²) — brute force duplicates:")
times_quad = measure_growth(has_dup_brute, sizes, lambda n: list(range(n)))
for size, t in zip(sizes, times_quad):
    print(f"    n={size:>5}: {t:.4f}s")
if times_quad[0] > 0:
    print(f"    Ratio (8000/1000): {times_quad[-1]/times_quad[0]:.1f}x "
          f"(expected ~64x for O(n²))")
print()

# =============================
# 7. COMPLEXITY CHEAT SHEET
# =============================

print("=== Algorithm Complexity Cheat Sheet ===")
print()

print(f"  {'Algorithm':<25} | {'Time (avg)':<12} | {'Time (worst)':<12} | {'Space':<8}")
print("  " + "-" * 65)

algorithms = [
    ("Linear Search", "O(n)", "O(n)", "O(1)"),
    ("Binary Search", "O(log n)", "O(log n)", "O(1)"),
    ("Bubble Sort", "O(n²)", "O(n²)", "O(1)"),
    ("Selection Sort", "O(n²)", "O(n²)", "O(1)"),
    ("Insertion Sort", "O(n²)", "O(n²)", "O(1)"),
    ("Merge Sort", "O(n log n)", "O(n log n)", "O(n)"),
    ("Quick Sort", "O(n log n)", "O(n²)", "O(log n)"),
    ("Dict Lookup", "O(1)", "O(n)", "O(n)"),
    ("Set Lookup", "O(1)", "O(n)", "O(n)"),
    ("BFS/DFS", "O(V+E)", "O(V+E)", "O(V)"),
]

for name, time_avg, time_worst, space in algorithms:
    print(f"  {name:<25} | {time_avg:<12} | {time_worst:<12} | {space:<8}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Measure the growth rate of Python's sorted()
#    and verify it's O(n log n)
# 2. Compare set.add() vs list.append() for
#    10,000, 100,000, and 1,000,000 operations
# 3. Write a function and analyze its complexity
#    in terms of both time and space
# ============================================
