# ============================================
# MODULE 17 - SUBTOPIC 11: Quick Sort
# ============================================

# Quick sort: choose pivot, partition, recurse.
# Average O(n log n), in-place.

import time
import random

# =============================
# 1. BASIC PARTITION
# =============================

print("=== The Partition Operation ===")
print()

def partition(arr, low, high):
    """Partition array around pivot (last element)."""
    pivot = arr[high]
    i = low - 1    # index of smaller element boundary

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Demonstrate partition
data = [8, 3, 1, 5, 9, 2, 7]
print(f"  Before partition: {data}")
print(f"  Pivot: {data[-1]}")
pivot_idx = partition(data, 0, len(data) - 1)
print(f"  After partition:  {data}")
print(f"  Pivot position:   {pivot_idx}")
print(f"  Left of pivot:  {data[:pivot_idx]} (all ≤ {data[pivot_idx]})")
print(f"  Right of pivot: {data[pivot_idx + 1:]} (all > {data[pivot_idx]})")
print()

# =============================
# 2. FULL QUICK SORT
# =============================

print("=== Quick Sort ===")
print()

def quick_sort(arr, low=0, high=None):
    """Sort array in-place using quick sort."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)     # sort left
        quick_sort(arr, pivot_idx + 1, high)    # sort right

data = [10, 7, 8, 9, 1, 5]
print(f"  Before: {data}")
quick_sort(data)
print(f"  After:  {data}")
print()

# =============================
# 3. SIMPLE VERSION (EASIER TO UNDERSTAND)
# =============================

print("=== Quick Sort — Simple Version ===")
print()

def quick_sort_simple(items):
    """Quick sort using list comprehensions (not in-place)."""
    if len(items) <= 1:
        return items

    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    middle = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]

    return quick_sort_simple(left) + middle + quick_sort_simple(right)

data = [3, 6, 8, 10, 1, 2, 1]
result = quick_sort_simple(data)
print(f"  Before: {data}")
print(f"  After:  {result}")
print("  (This version is clearer but uses O(n) extra space)")
print()

# =============================
# 4. VISUALIZING QUICK SORT
# =============================

print("=== Quick Sort — Visualization ===")
print()

def quick_sort_visual(items, depth=0):
    """Quick sort with step-by-step display."""
    indent = "    " * depth

    if len(items) <= 1:
        return items

    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    middle = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]

    print(f"  {indent}list={items}, pivot={pivot}")
    print(f"  {indent}  left={left}, middle={middle}, right={right}")

    sorted_left = quick_sort_visual(left, depth + 1)
    sorted_right = quick_sort_visual(right, depth + 1)

    result = sorted_left + middle + sorted_right
    return result

data = [5, 3, 8, 1, 9, 2]
print("  Tracing quick sort:")
result = quick_sort_visual(data)
print(f"  Final: {result}")
print()

# =============================
# 5. PIVOT STRATEGIES
# =============================

print("=== Pivot Strategies ===")
print()

def partition_median_of_three(arr, low, high):
    """Choose pivot as median of first, middle, last."""
    mid = (low + high) // 2

    # Sort low, mid, high
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    # Place median at high-1 position as pivot
    arr[mid], arr[high] = arr[high], arr[mid]
    return partition(arr, low, high)

# Show why pivot choice matters
print("  Bad pivot (always min or max):")
print("    → Each partition only removes 1 element → O(n²)")
print()
print("  Good pivot (near median):")
print("    → Each partition splits roughly in half → O(n log n)")
print()

# =============================
# 6. SPEED COMPARISON
# =============================

print("=== Quick Sort vs Merge Sort vs Insertion Sort ===")
print()

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    return merge(merge_sort(items[:mid]), merge_sort(items[mid:]))

def insertion_sort(items):
    arr = items.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

for size in [1000, 5000, 10000]:
    data = random.sample(range(size * 10), size)

    start = time.time()
    insertion_sort(data)
    t_ins = time.time() - start

    start = time.time()
    merge_sort(data)
    t_merge = time.time() - start

    start = time.time()
    quick_sort_simple(data)
    t_quick = time.time() - start

    print(f"  Size {size:>6}: Insertion={t_ins:.4f}s, "
          f"Merge={t_merge:.4f}s, Quick={t_quick:.4f}s")

print()

# =============================
# 7. PYTHON'S BUILT-IN SORT
# =============================

print("=== Python's Built-in Sort (Timsort) ===")
print()

# Python uses Timsort — a hybrid of merge sort and insertion sort
# It's always O(n log n) and optimized for real-world data

size = 100_000
data = random.sample(range(size * 10), size)

start = time.time()
sorted_data = sorted(data)
t_builtin = time.time() - start

print(f"  Python sorted() on {size:,} items: {t_builtin:.4f}s")
print("  → Always use sorted() in production code!")
print("  → Learn these algorithms to understand HOW sorting works")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Implement quick sort with random pivot selection
# 2. Find the k-th smallest element using partition
#    (quick select algorithm)
# 3. Compare all sorting algorithms on sorted, reverse,
#    and random data
# ============================================
