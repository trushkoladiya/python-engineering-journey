# ============================================
# MODULE 17 - SUBTOPIC 8: Selection Sort
# ============================================

# Selection sort: find the minimum, place it in position.
# Always O(n²), but makes fewer swaps than bubble sort.

import time

# =============================
# 1. BASIC SELECTION SORT
# =============================

print("=== Basic Selection Sort ===")
print()

def selection_sort(items):
    """Sort list in-place using selection sort."""
    n = len(items)
    for i in range(n):
        # Find minimum in unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j
        # Swap minimum with first unsorted position
        items[i], items[min_idx] = items[min_idx], items[i]

data = [64, 25, 12, 22, 11]
print(f"  Before: {data}")
selection_sort(data)
print(f"  After:  {data}")
print()

# =============================
# 2. VISUALIZING EACH PASS
# =============================

print("=== Selection Sort — Pass by Pass ===")
print()

def selection_sort_visual(items):
    """Selection sort with visualization."""
    arr = items.copy()
    n = len(arr)
    print(f"  Start: {arr}")

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print(f"  Pass {i + 1}: {arr}  (placed {arr[i]} at index {i})")

    return arr

data = [29, 10, 14, 37, 13]
selection_sort_visual(data)
print()

# =============================
# 3. COUNTING OPERATIONS
# =============================

print("=== Selection Sort — Counting Operations ===")
print()

def selection_sort_count(items):
    """Count comparisons and swaps."""
    arr = items.copy()
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return arr, comparisons, swaps

# Always same comparisons, regardless of input order
sorted_data = [1, 2, 3, 4, 5, 6, 7, 8]
_, comps1, swps1 = selection_sort_count(sorted_data)
print(f"  Already sorted: {comps1} comparisons, {swps1} swaps")

reverse_data = [8, 7, 6, 5, 4, 3, 2, 1]
_, comps2, swps2 = selection_sort_count(reverse_data)
print(f"  Reverse sorted: {comps2} comparisons, {swps2} swaps")

print(f"  → Same comparisons ({comps1}), but swaps differ")
print(f"  → Selection sort always does n(n-1)/2 comparisons")
print()

# =============================
# 4. FINDING K SMALLEST ELEMENTS
# =============================

print("=== Selection Sort — Finding K Smallest ===")
print()

def k_smallest(items, k):
    """Find k smallest elements using partial selection sort."""
    arr = items.copy()
    n = len(arr)
    result = []

    for i in range(min(k, n)):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        result.append(arr[i])

    return result

data = [45, 12, 78, 3, 67, 23, 56, 8, 91, 34]
print(f"  Data: {data}")
print(f"  3 smallest: {k_smallest(data, 3)}")
print(f"  5 smallest: {k_smallest(data, 5)}")
print("  → We only need k passes instead of n!")
print()

# =============================
# 5. SORT BY CUSTOM KEY
# =============================

print("=== Selection Sort — Custom Key ===")
print()

def selection_sort_key(items, key_func):
    """Selection sort with custom comparison key."""
    arr = items.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if key_func(arr[j]) < key_func(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Sort strings by length
words = ["banana", "pie", "strawberry", "kiwi", "apple"]
sorted_words = selection_sort_key(words, key_func=len)
print(f"  Words by length: {sorted_words}")

# Sort dicts by value
scores = [
    {"name": "Trush", "score": 85},
    {"name": "Rahul", "score": 92},
    {"name": "Charlie", "score": 78},
]
sorted_scores = selection_sort_key(scores, key_func=lambda s: s["score"])
print(f"  By score: {[(s['name'], s['score']) for s in sorted_scores]}")
print()

# =============================
# 6. PERFORMANCE
# =============================

print("=== Selection Sort — Performance ===")
print()

for size in [100, 500, 1000, 2000]:
    data = list(range(size, 0, -1))
    start = time.time()
    selection_sort(data)
    elapsed = time.time() - start
    print(f"  Size {size:>5}: {elapsed:.4f}s")

print()
print("  → Always O(n²) — no best case optimization")
print("  → But fewer swaps than bubble sort")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Modify selection sort to sort in descending order
# 2. Find the k-th largest element without fully sorting
# 3. Compare swap counts between bubble sort and selection sort
# ============================================
