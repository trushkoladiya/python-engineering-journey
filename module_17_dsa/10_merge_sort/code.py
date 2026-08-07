# ============================================
# MODULE 17 - SUBTOPIC 10: Merge Sort
# ============================================

# Merge sort: divide and conquer approach.
# Always O(n log n) — the first efficient sort we learn.

import time
import random

# =============================
# 1. THE MERGE OPERATION
# =============================

print("=== The Merge Operation ===")
print()

def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

left = [1, 4, 7, 9]
right = [2, 3, 5, 8]
merged = merge(left, right)
print(f"  Left:   {left}")
print(f"  Right:  {right}")
print(f"  Merged: {merged}")
print()

# =============================
# 2. FULL MERGE SORT
# =============================

print("=== Merge Sort ===")
print()

def merge_sort(items):
    """Sort using merge sort (recursive)."""
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

data = [38, 27, 43, 3, 9, 82, 10]
sorted_data = merge_sort(data)
print(f"  Before: {data}")
print(f"  After:  {sorted_data}")
print()

# =============================
# 3. VISUALIZING THE RECURSION
# =============================

print("=== Merge Sort — Visualization ===")
print()

def merge_sort_visual(items, depth=0):
    """Merge sort with step-by-step display."""
    indent = "    " * depth
    print(f"  {indent}split: {items}")

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort_visual(items[:mid], depth + 1)
    right = merge_sort_visual(items[mid:], depth + 1)
    merged = merge(left, right)

    print(f"  {indent}merge: {left} + {right} → {merged}")
    return merged

data = [5, 3, 8, 1, 4]
print("  Tracing merge sort:")
result = merge_sort_visual(data)
print(f"  Final: {result}")
print()

# =============================
# 4. MERGE SORT vs BASIC SORTS
# =============================

print("=== Merge Sort vs Insertion Sort — Speed ===")
print()

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
    t_insertion = time.time() - start

    start = time.time()
    merge_sort(data)
    t_merge = time.time() - start

    speedup = t_insertion / t_merge if t_merge > 0 else float('inf')
    print(f"  Size {size:>6}: Insertion={t_insertion:.4f}s, "
          f"Merge={t_merge:.4f}s ({speedup:.1f}x faster)")

print()
print("  → Merge sort scales MUCH better!")
print()

# =============================
# 5. MERGE SORT WITH CUSTOM KEY
# =============================

print("=== Merge Sort — Custom Key ===")
print()

def merge_key(left, right, key_func):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_key(items, key_func):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort_key(items[:mid], key_func)
    right = merge_sort_key(items[mid:], key_func)
    return merge_key(left, right, key_func)

students = [
    {"name": "Charlie", "grade": 85},
    {"name": "Trush", "grade": 92},
    {"name": "Eve", "grade": 78},
    {"name": "Rahul", "grade": 92},
    {"name": "Diana", "grade": 85},
]

sorted_students = merge_sort_key(students, lambda s: s["grade"])
print("  Sorted by grade (stable — same grades keep original order):")
for s in sorted_students:
    print(f"    {s['name']}: {s['grade']}")
print()

# =============================
# 6. COUNTING OPERATIONS
# =============================

print("=== Merge Sort — Operation Count ===")
print()

merge_count = 0

def merge_counted(left, right):
    global merge_count
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        merge_count += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_counted(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort_counted(items[:mid])
    right = merge_sort_counted(items[mid:])
    return merge_counted(left, right)

for size in [10, 100, 1000, 10000]:
    merge_count = 0
    merge_sort_counted(random.sample(range(size * 10), size))
    # n log n approximation
    import math
    expected = size * math.log2(size) if size > 0 else 0
    print(f"  n={size:>5}: comparisons={merge_count:>7,} "
          f"(n·log₂n ≈ {expected:>10,.0f})")

print()

# ============================================
# TRY IT YOURSELF:
# 1. Implement bottom-up merge sort (iterative, no recursion)
# 2. Count the number of inversions in an array using merge sort
# 3. Merge k sorted lists into one sorted list
# ============================================
