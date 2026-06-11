# ============================================
# MODULE 17 - SUBTOPIC 9: Insertion Sort
# ============================================

# Insertion sort: build sorted portion one element at a time.
# Best basic sort for nearly sorted data.

import time
import random

# =============================
# 1. BASIC INSERTION SORT
# =============================

print("=== Basic Insertion Sort ===")
print()

def insertion_sort(items):
    """Sort list in-place using insertion sort."""
    for i in range(1, len(items)):
        key = items[i]          # element to insert
        j = i - 1
        # Shift elements right until we find the correct position
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key     # insert element

data = [12, 11, 13, 5, 6]
print(f"  Before: {data}")
insertion_sort(data)
print(f"  After:  {data}")
print()

# =============================
# 2. VISUALIZING EACH STEP
# =============================

print("=== Insertion Sort — Step by Step ===")
print()

def insertion_sort_visual(items):
    """Insertion sort with step-by-step display."""
    arr = items.copy()
    print(f"  Start: {arr}")

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"  Step {i}: {arr}  (inserted {key} at index {j + 1})")

    return arr

data = [7, 3, 5, 1, 9, 2]
insertion_sort_visual(data)
print()

# =============================
# 3. WHY INSERTION SORT SHINES ON NEARLY SORTED DATA
# =============================

print("=== Nearly Sorted Data — Insertion Sort Advantage ===")
print()

def insertion_sort_count(items):
    """Count comparisons and shifts."""
    arr = items.copy()
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        if j >= 0:
            comparisons += 1    # final comparison that ended the while

    return arr, comparisons, shifts

# Already sorted
sorted_data = list(range(1, 21))
_, comps, shifts = insertion_sort_count(sorted_data)
print(f"  Already sorted (20 items): {comps} comparisons, {shifts} shifts")

# Nearly sorted (just a few out of place)
nearly = list(range(1, 21))
nearly[5], nearly[6] = nearly[6], nearly[5]   # swap two adjacent
_, comps, shifts = insertion_sort_count(nearly)
print(f"  Nearly sorted (20 items):  {comps} comparisons, {shifts} shifts")

# Reverse sorted (worst case)
reverse = list(range(20, 0, -1))
_, comps, shifts = insertion_sort_count(reverse)
print(f"  Reverse sorted (20 items): {comps} comparisons, {shifts} shifts")

print("  → Nearly sorted data needs very few operations!")
print()

# =============================
# 4. COMPARING ALL THREE BASIC SORTS
# =============================

print("=== Bubble vs Selection vs Insertion — Speed Test ===")
print()

def bubble_sort(items):
    arr = items.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(items):
    arr = items.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort_copy(items):
    arr = items.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

size = 2000

# Random data
random_data = random.sample(range(size * 10), size)

print(f"  Testing with {size} random elements:")
for name, sort_func in [("Bubble", bubble_sort), ("Selection", selection_sort), ("Insertion", insertion_sort_copy)]:
    start = time.time()
    sort_func(random_data)
    elapsed = time.time() - start
    print(f"    {name:12}: {elapsed:.4f}s")
print()

# Nearly sorted data
nearly_sorted = list(range(size))
# Swap 10 random pairs
for _ in range(10):
    i, j = random.randint(0, size - 1), random.randint(0, size - 1)
    nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]

print(f"  Testing with {size} nearly sorted elements:")
for name, sort_func in [("Bubble", bubble_sort), ("Selection", selection_sort), ("Insertion", insertion_sort_copy)]:
    start = time.time()
    sort_func(nearly_sorted)
    elapsed = time.time() - start
    print(f"    {name:12}: {elapsed:.4f}s")
print()
print("  → Insertion sort wins on nearly sorted data!")
print()

# =============================
# 5. SORT STABILITY DEMONSTRATION
# =============================

print("=== Sort Stability ===")
print()

# Stable sort: equal elements keep their original order
students = [
    ("Charlie", 85),
    ("Trush", 92),
    ("Rahul", 85),
    ("Diana", 92),
]

def insertion_sort_key(items, key_func):
    """Stable insertion sort with custom key."""
    arr = items.copy()
    for i in range(1, len(arr)):
        key_val = arr[i]
        j = i - 1
        while j >= 0 and key_func(arr[j]) > key_func(key_val):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_val
    return arr

sorted_students = insertion_sort_key(students, lambda s: s[1])
print("  Sorted by grade (stable — same grades keep original order):")
for name, grade in sorted_students:
    print(f"    {name}: {grade}")
print()

# =============================
# 6. BINARY INSERTION SORT
# =============================

print("=== Binary Insertion Sort ===")
print()

def binary_insertion_sort(items):
    """Use binary search to find insertion position."""
    arr = items.copy()
    for i in range(1, len(arr)):
        key = arr[i]

        # Binary search for position
        left, right = 0, i
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= key:
                left = mid + 1
            else:
                right = mid

        # Shift elements right
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = key

    return arr

data = [38, 27, 43, 3, 9, 82, 10]
result = binary_insertion_sort(data)
print(f"  Before: {data}")
print(f"  After:  {result}")
print("  → Fewer comparisons, but same number of shifts")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Modify insertion sort to sort in descending order
# 2. Sort a list of strings using insertion sort
# 3. Time all three basic sorts on already-sorted,
#    reverse-sorted, and random data — which wins each?
# ============================================
