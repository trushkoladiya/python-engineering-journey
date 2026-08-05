# ============================================
# MODULE 17 - SUBTOPIC 6: Binary Search
# ============================================

# Binary search: find a target in SORTED data by halving
# the search space each step. O(log n).

import time

# =============================
# 1. ITERATIVE BINARY SEARCH
# =============================

print("=== Iterative Binary Search ===")
print()

def binary_search(items, target):
    """Find target in sorted list. Returns index or -1."""
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1      # search right half
        else:
            right = mid - 1     # search left half
    return -1

data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(f"  Sorted data: {data}")
print(f"  Search 23: index {binary_search(data, 23)}")
print(f"  Search 50: index {binary_search(data, 50)}")
print()

# =============================
# 2. STEP-BY-STEP VISUALIZATION
# =============================

print("=== Binary Search — Step by Step ===")
print()

def binary_search_verbose(items, target):
    """Binary search with step-by-step output."""
    left = 0
    right = len(items) - 1
    step = 0

    while left <= right:
        step += 1
        mid = (left + right) // 2
        print(f"    Step {step}: left={left}, right={right}, mid={mid}, "
              f"items[mid]={items[mid]}", end="")

        if items[mid] == target:
            print(" ← FOUND!")
            return mid, step
        elif items[mid] < target:
            print(f" → {items[mid]} < {target}, go RIGHT")
            left = mid + 1
        else:
            print(f" → {items[mid]} > {target}, go LEFT")
            right = mid - 1

    print(f"    Not found after {step} steps")
    return -1, step

data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
print(f"  Data: {data}")
print(f"  Searching for 21:")
idx, steps = binary_search_verbose(data, 21)
print(f"  Result: index={idx}, steps={steps}")
print()

print(f"  Searching for 14 (not present):")
idx, steps = binary_search_verbose(data, 14)
print(f"  Result: index={idx}, steps={steps}")
print()

# =============================
# 3. RECURSIVE BINARY SEARCH
# =============================

print("=== Recursive Binary Search ===")
print()

def binary_search_recursive(items, target, left, right):
    """Binary search using recursion."""
    if left > right:
        return -1

    mid = (left + right) // 2
    if items[mid] == target:
        return mid
    elif items[mid] < target:
        return binary_search_recursive(items, target, mid + 1, right)
    else:
        return binary_search_recursive(items, target, left, mid - 1)

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"  Data: {data}")
print(f"  Recursive search for 60: index {binary_search_recursive(data, 60, 0, len(data) - 1)}")
print(f"  Recursive search for 45: index {binary_search_recursive(data, 45, 0, len(data) - 1)}")
print()

# =============================
# 4. LINEAR vs BINARY SEARCH — SPEED
# =============================

print("=== Linear vs Binary Search — Speed Comparison ===")
print()

def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]

print("  Size          | Linear (s)   | Binary (s)   | Speedup")
print("  " + "-" * 60)

for size in sizes:
    data = list(range(size))
    target = size - 1   # worst case for linear

    start = time.time()
    linear_search(data, target)
    t_linear = time.time() - start

    start = time.time()
    binary_search(data, target)
    t_binary = time.time() - start

    speedup = t_linear / t_binary if t_binary > 0 else float('inf')
    print(f"  {size:>12,} | {t_linear:.6f}     | {t_binary:.8f}  | ~{speedup:,.0f}x")

print()

# =============================
# 5. FIND INSERTION POINT
# =============================

print("=== Binary Search — Find Insertion Point ===")
print()

def find_insert_position(sorted_list, target):
    """Find where target should be inserted to keep list sorted."""
    left = 0
    right = len(sorted_list)

    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

data = [10, 20, 30, 40, 50]
print(f"  Data: {data}")

for value in [5, 25, 35, 55]:
    pos = find_insert_position(data, value)
    print(f"  Insert {value} at index {pos} → {data[:pos] + [value] + data[pos:]}")
print()

# =============================
# 6. FIND FIRST AND LAST OCCURRENCE
# =============================

print("=== Binary Search — First and Last Occurrence ===")
print()

def find_first_occurrence(sorted_list, target):
    """Find the first occurrence of target in sorted list."""
    left, right = 0, len(sorted_list) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            result = mid
            right = mid - 1    # keep searching LEFT for earlier occurrence
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def find_last_occurrence(sorted_list, target):
    """Find the last occurrence of target in sorted list."""
    left, right = 0, len(sorted_list) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            result = mid
            left = mid + 1     # keep searching RIGHT for later occurrence
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

data = [1, 2, 3, 3, 3, 3, 4, 5, 6]
target = 3
first = find_first_occurrence(data, target)
last = find_last_occurrence(data, target)
count = last - first + 1 if first != -1 else 0

print(f"  Data: {data}")
print(f"  Target: {target}")
print(f"  First at: {first}")
print(f"  Last at:  {last}")
print(f"  Count:    {count}")
print()

# =============================
# 7. SEARCH IN ROTATED SORTED ARRAY
# =============================

print("=== Binary Search — Rotated Sorted Array ===")
print()

def search_rotated(nums, target):
    """Search in a sorted array that has been rotated."""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Original sorted: [1,2,3,4,5,6,7] → rotated at index 3
rotated = [4, 5, 6, 7, 1, 2, 3]
print(f"  Rotated array: {rotated}")
print(f"  Search 6: index {search_rotated(rotated, 6)}")
print(f"  Search 2: index {search_rotated(rotated, 2)}")
print(f"  Search 9: index {search_rotated(rotated, 9)}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use binary search to find the square root
#    of a number (integer part only)
# 2. Count how many times a number appears in a
#    sorted list using binary search (not linear scan)
# 3. Find the peak element in a list where elements
#    first increase then decrease
# ============================================
