# ============================================
# MODULE 17 - SUBTOPIC 3: Arrays & List-Based Problems — Core Patterns
# ============================================

# In Python, "arrays" are lists.
# Core patterns: traversal, searching, basic sorting concepts.

# =============================
# 1. FORWARD TRAVERSAL
# =============================

print("=== Forward Traversal ===")
print()

numbers = [10, 25, 30, 45, 50, 15]

# Simple traversal
print("  All elements:")
for num in numbers:
    print(f"    {num}")
print()

# Traversal with index
print("  With index:")
for i in range(len(numbers)):
    print(f"    Index {i}: {numbers[i]}")
print()

# Using enumerate (cleaner)
print("  Using enumerate:")
for i, num in enumerate(numbers):
    print(f"    [{i}] = {num}")
print()

# =============================
# 2. REVERSE TRAVERSAL
# =============================

print("=== Reverse Traversal ===")
print()

# Method 1: reversed range
print("  Reverse with range:")
for i in range(len(numbers) - 1, -1, -1):
    print(f"    Index {i}: {numbers[i]}")
print()

# Method 2: reversed()
print("  Reverse with reversed():")
for num in reversed(numbers):
    print(f"    {num}")
print()

# =============================
# 3. LINEAR SEARCH
# =============================

print("=== Linear Search ===")
print()

def linear_search(items, target):
    """Search for target in items. Return index or -1."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

data = [64, 34, 25, 12, 22, 11, 90]
print(f"  Data: {data}")

# Search for existing element
target = 22
result = linear_search(data, target)
print(f"  Search for {target}: found at index {result}")

# Search for missing element
target = 50
result = linear_search(data, target)
print(f"  Search for {target}: {'not found' if result == -1 else f'index {result}'}")
print()

# =============================
# 4. LINEAR SEARCH — COUNT STEPS
# =============================

print("=== Linear Search — Counting Steps ===")
print()

def linear_search_verbose(items, target):
    """Search with step counting."""
    steps = 0
    for i in range(len(items)):
        steps += 1
        if items[i] == target:
            return i, steps
    return -1, steps

data = [5, 13, 27, 8, 42, 19, 35, 61, 3, 50]
print(f"  Data: {data}")
print(f"  Length: {len(data)}")
print()

# Best case: target is first element
idx, steps = linear_search_verbose(data, 5)
print(f"  Search for 5 (first):  index={idx}, steps={steps}  ← best case")

# Worst case: target is last element
idx, steps = linear_search_verbose(data, 50)
print(f"  Search for 50 (last):  index={idx}, steps={steps} ← worst case")

# Average case
idx, steps = linear_search_verbose(data, 42)
print(f"  Search for 42 (middle): index={idx}, steps={steps}  ← typical case")
print()

# =============================
# 5. FIND ALL OCCURRENCES
# =============================

print("=== Find All Occurrences ===")
print()

def find_all(items, target):
    """Find all indices where target appears."""
    indices = []
    for i in range(len(items)):
        if items[i] == target:
            indices.append(i)
    return indices

data = [3, 7, 3, 1, 5, 3, 9, 3]
target = 3
result = find_all(data, target)
print(f"  Data: {data}")
print(f"  All positions of {target}: {result}")
print(f"  Count: {len(result)}")
print()

# =============================
# 6. FINDING MIN AND MAX
# =============================

print("=== Finding Min and Max ===")
print()

def find_min_max(items):
    """Find minimum and maximum in one pass."""
    if not items:
        return None, None
    minimum = items[0]
    maximum = items[0]
    for item in items[1:]:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
    return minimum, maximum

data = [34, 12, 89, 45, 67, 23, 56]
min_val, max_val = find_min_max(data)
print(f"  Data: {data}")
print(f"  Min: {min_val}, Max: {max_val}")
print()

# =============================
# 7. COMPUTING RUNNING SUM
# =============================

print("=== Running Sum (Prefix Sum) ===")
print()

def running_sum(items):
    """Compute running sum of a list."""
    result = []
    total = 0
    for item in items:
        total += item
        result.append(total)
    return result

data = [1, 2, 3, 4, 5]
prefix = running_sum(data)
print(f"  Data:        {data}")
print(f"  Running sum: {prefix}")
print(f"  → Each value is the sum of all elements up to that point")
print()

# =============================
# 8. REVERSING A LIST (IN-PLACE)
# =============================

print("=== Reversing a List In-Place ===")
print()

def reverse_list(items):
    """Reverse a list using two pointers."""
    left = 0
    right = len(items) - 1
    while left < right:
        # Swap elements
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1

data = [1, 2, 3, 4, 5]
print(f"  Before: {data}")
reverse_list(data)
print(f"  After:  {data}")
print(f"  → O(n) time, O(1) space — no extra list created")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a function to find the second largest
#    element in a list (without sorting)
# 2. Write a function that counts how many elements
#    are greater than the average
# 3. Write a function to rotate a list left by k positions
# ============================================
