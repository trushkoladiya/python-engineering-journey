# ============================================
# MODULE 17 - SUBTOPIC 5: Linear Search
# ============================================

# Linear search: check each element one by one.
# Works on ANY list — sorted or unsorted.

# =============================
# 1. BASIC LINEAR SEARCH
# =============================

print("=== Basic Linear Search ===")
print()

def linear_search(items, target):
    """Return index of target, or -1 if not found."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

data = [42, 17, 89, 5, 63, 31, 74]
print(f"  Data: {data}")
print(f"  Search 63: index {linear_search(data, 63)}")
print(f"  Search 99: index {linear_search(data, 99)}")
print()

# =============================
# 2. SEARCH WITH STEP COUNTING
# =============================

print("=== Linear Search — Step by Step ===")
print()

def linear_search_steps(items, target):
    """Search and count comparisons made."""
    for i in range(len(items)):
        print(f"    Step {i + 1}: compare items[{i}]={items[i]} with {target}", end="")
        if items[i] == target:
            print(" ← FOUND!")
            return i, i + 1
        print()
    print(f"    Not found after {len(items)} steps")
    return -1, len(items)

data = [10, 25, 7, 43, 18, 56, 32]
print(f"  Data: {data}")
print(f"  Searching for 18:")
idx, steps = linear_search_steps(data, 18)
print(f"  Result: index={idx}, steps={steps}")
print()

# =============================
# 3. SEARCH IN DIFFERENT DATA TYPES
# =============================

print("=== Search in Different Data Types ===")
print()

# Search in strings
def search_char(text, char):
    for i in range(len(text)):
        if text[i] == char:
            return i
    return -1

word = "algorithm"
print(f"  Search 'r' in '{word}': index {search_char(word, 'r')}")
print(f"  Search 'z' in '{word}': index {search_char(word, 'z')}")
print()

# Search in list of dicts
students = [
    {"name": "Trush", "grade": 92},
    {"name": "Rahul", "grade": 85},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 95},
]

def search_by_name(records, name):
    for i, record in enumerate(records):
        if record["name"] == name:
            return record
    return None

result = search_by_name(students, "Charlie")
print(f"  Search student 'Charlie': {result}")

result = search_by_name(students, "Eve")
print(f"  Search student 'Eve': {result}")
print()

# =============================
# 4. FIND FIRST AND LAST OCCURRENCE
# =============================

print("=== First and Last Occurrence ===")
print()

def find_first(items, target):
    """Find first occurrence of target."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

def find_last(items, target):
    """Find last occurrence of target."""
    last_index = -1
    for i in range(len(items)):
        if items[i] == target:
            last_index = i
    return last_index

data = [3, 7, 2, 7, 5, 7, 1, 7, 9]
print(f"  Data: {data}")
print(f"  First 7: index {find_first(data, 7)}")
print(f"  Last 7:  index {find_last(data, 7)}")
print()

# =============================
# 5. SENTINEL LINEAR SEARCH
# =============================

print("=== Sentinel Linear Search ===")
print()

def sentinel_search(items, target):
    """
    Sentinel search: place target at end to avoid
    checking bounds on every iteration.
    """
    n = len(items)
    if n == 0:
        return -1

    last = items[-1]
    items[-1] = target    # sentinel

    i = 0
    while items[i] != target:
        i += 1

    items[-1] = last      # restore original

    if i < n - 1 or items[-1] == target:
        return i
    return -1

data = [15, 28, 4, 37, 52, 11, 43]
print(f"  Data: {data}")
print(f"  Sentinel search for 37: index {sentinel_search(data, 37)}")
print(f"  Sentinel search for 99: index {sentinel_search(data, 99)}")
print("  → Slightly fewer comparisons per iteration")
print()

# =============================
# 6. COMPLEXITY DEMONSTRATION
# =============================

print("=== Linear Search — Complexity ===")
print()

import time

sizes = [1_000, 10_000, 100_000, 1_000_000]

print("  Size        | Time (worst case)")
print("  " + "-" * 35)

for size in sizes:
    data = list(range(size))
    target = size - 1    # worst case: last element

    start = time.time()
    linear_search(data, target)
    elapsed = time.time() - start

    print(f"  {size:>10,} | {elapsed:.6f}s")

print()
print("  → Time grows linearly with size — that's O(n)")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a linear search that returns ALL indices
#    where the target appears
# 2. Write a search that finds the first element
#    greater than a given value
# 3. Search for a substring within a list of strings
# ============================================
