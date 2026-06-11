# ============================================
# MODULE 17 - SUBTOPIC 7: Bubble Sort
# ============================================

# Bubble sort: repeatedly swap adjacent elements
# if they're in the wrong order. O(n²).

import time

# =============================
# 1. BASIC BUBBLE SORT
# =============================

print("=== Basic Bubble Sort ===")
print()

def bubble_sort(items):
    """Sort list in-place using bubble sort."""
    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):    # last i elements are already sorted
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break   # optimization: stop if no swaps occurred

data = [64, 34, 25, 12, 22, 11, 90]
print(f"  Before: {data}")
bubble_sort(data)
print(f"  After:  {data}")
print()

# =============================
# 2. VISUALIZING EACH PASS
# =============================

print("=== Bubble Sort — Pass by Pass ===")
print()

def bubble_sort_visual(items):
    """Bubble sort with visualization."""
    n = len(items)
    arr = items.copy()
    print(f"  Start:  {arr}")

    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        sorted_part = arr[n - i:]
        print(f"  Pass {i + 1}: {arr}  (sorted: last {i + 1})")
        if not swapped:
            print("  → No swaps needed, array is sorted!")
            break
    return arr

data = [5, 3, 8, 4, 2]
bubble_sort_visual(data)
print()

# =============================
# 3. COUNTING OPERATIONS
# =============================

print("=== Bubble Sort — Counting Operations ===")
print()

def bubble_sort_count(items):
    """Count comparisons and swaps."""
    arr = items.copy()
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break

    return arr, comparisons, swaps

# Best case: already sorted
best = [1, 2, 3, 4, 5, 6, 7, 8]
_, comps, swps = bubble_sort_count(best)
print(f"  Best case (sorted):   {comps} comparisons, {swps} swaps")

# Worst case: reverse sorted
worst = [8, 7, 6, 5, 4, 3, 2, 1]
_, comps, swps = bubble_sort_count(worst)
print(f"  Worst case (reverse): {comps} comparisons, {swps} swaps")

# Average case: random
import random
avg = random.sample(range(1, 9), 8)
_, comps, swps = bubble_sort_count(avg)
print(f"  Random case:          {comps} comparisons, {swps} swaps")
print()

# =============================
# 4. SORTING DIFFERENT DATA
# =============================

print("=== Sorting Different Data ===")
print()

# Sort strings
words = ["banana", "apple", "cherry", "date", "elderberry"]
print(f"  Words before: {words}")
bubble_sort(words)
print(f"  Words after:  {words}")
print()

# Sort tuples by second element
def bubble_sort_by_key(items, key_func):
    """Bubble sort with custom key."""
    arr = items.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if key_func(arr[j]) > key_func(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

students = [("Trush", 85), ("Rahul", 92), ("Charlie", 78), ("Diana", 95)]
sorted_students = bubble_sort_by_key(students, lambda s: s[1])
print(f"  By grade: {sorted_students}")
print()

# =============================
# 5. PERFORMANCE TEST
# =============================

print("=== Bubble Sort — Performance ===")
print()

for size in [100, 500, 1000, 2000]:
    data = list(range(size, 0, -1))   # worst case
    start = time.time()
    bubble_sort(data)
    elapsed = time.time() - start
    print(f"  Size {size:>5}: {elapsed:.4f}s")

print()
print("  → Doubling size → ~4x slower (O(n²) behavior)")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Modify bubble sort to sort in descending order
# 2. Count how many passes are needed for different inputs
# 3. Sort a list of dictionaries by a specific key
# ============================================
