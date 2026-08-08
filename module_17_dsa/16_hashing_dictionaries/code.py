# ============================================
# MODULE 17 - SUBTOPIC 16: Hashing & Dictionaries in DSA
# ============================================

# Dictionaries provide O(1) lookup — the most powerful
# tool in your DSA toolkit.

import time

# =============================
# 1. FREQUENCY COUNTING
# =============================

print("=== Frequency Counting ===")
print()

def count_frequency(items):
    """Count frequency of each item. O(n)."""
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Word frequency
text = "to be or not to be that is the question to be"
words = text.split()
word_freq = count_frequency(words)

print(f"  Text: '{text}'")
print("  Word frequencies:")
for word, count in sorted(word_freq.items(), key=lambda x: -x[1]):
    bar = "█" * count
    print(f"    {word:10} {count} {bar}")
print()

# =============================
# 2. TWO SUM PROBLEM
# =============================

print("=== Two Sum Problem ===")
print()

def two_sum(numbers, target):
    """Find indices of two numbers that add to target. O(n)."""
    seen = {}   # value → index
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

data = [2, 7, 11, 15]
target = 9
result = two_sum(data, target)
print(f"  Data: {data}, target: {target}")
print(f"  Indices: {result} → {data[result[0]]} + {data[result[1]]} = {target}")
print()

data = [3, 2, 4, 1, 5]
target = 6
result = two_sum(data, target)
print(f"  Data: {data}, target: {target}")
print(f"  Indices: {result} → {data[result[0]]} + {data[result[1]]} = {target}")
print()

# =============================
# 3. DUPLICATE DETECTION
# =============================

print("=== Duplicate Detection ===")
print()

def find_duplicates(items):
    """Find all duplicate items. O(n)."""
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return [item for item, count in freq.items() if count > 1]

data = [1, 3, 5, 3, 7, 1, 9, 5, 5]
dupes = find_duplicates(data)
print(f"  Data: {data}")
print(f"  Duplicates: {dupes}")
print()

# First duplicate
def first_duplicate(items):
    """Find the first duplicate value. O(n)."""
    seen = set()
    for item in items:
        if item in seen:
            return item
        seen.add(item)
    return None

data = [5, 3, 4, 2, 3, 5, 1]
print(f"  Data: {data}")
print(f"  First duplicate: {first_duplicate(data)}")
print()

# =============================
# 4. GROUPING DATA
# =============================

print("=== Grouping Data with Dicts ===")
print()

def group_by(items, key_func):
    """Group items by a key function."""
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

students = [
    {"name": "Trush", "grade": "A"},
    {"name": "Rahul", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "C"},
    {"name": "Eve", "grade": "B"},
    {"name": "Frank", "grade": "A"},
]

by_grade = group_by(students, lambda s: s["grade"])
for grade, group in sorted(by_grade.items()):
    names = [s["name"] for s in group]
    print(f"  Grade {grade}: {', '.join(names)}")
print()

# =============================
# 5. ISOMORPHIC STRINGS
# =============================

print("=== Isomorphic Strings ===")
print()

def is_isomorphic(s1, s2):
    """Check if two strings have the same character pattern."""
    if len(s1) != len(s2):
        return False

    map_s1 = {}
    map_s2 = {}

    for c1, c2 in zip(s1, s2):
        if c1 in map_s1 and map_s1[c1] != c2:
            return False
        if c2 in map_s2 and map_s2[c2] != c1:
            return False
        map_s1[c1] = c2
        map_s2[c2] = c1

    return True

pairs = [("egg", "add"), ("foo", "bar"), ("paper", "title"), ("ab", "aa")]
for s1, s2 in pairs:
    result = "✓" if is_isomorphic(s1, s2) else "✗"
    print(f"  {result} '{s1}' ~ '{s2}'")
print()

# =============================
# 6. SUBARRAY SUM EQUALS K
# =============================

print("=== Subarray Sum Equals K ===")
print()

def count_subarrays_sum(nums, k):
    """Count subarrays that sum to k using prefix sum + hash map."""
    count = 0
    prefix_sum = 0
    prefix_counts = {0: 1}   # empty subarray has sum 0

    for num in nums:
        prefix_sum += num
        # If (prefix_sum - k) exists, there's a subarray summing to k
        if prefix_sum - k in prefix_counts:
            count += prefix_counts[prefix_sum - k]
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

    return count

data = [1, 1, 1]
k = 2
print(f"  Data: {data}, k: {k}")
print(f"  Subarrays summing to {k}: {count_subarrays_sum(data, k)}")

data = [1, 2, 3, -1, 2]
k = 4
print(f"  Data: {data}, k: {k}")
print(f"  Subarrays summing to {k}: {count_subarrays_sum(data, k)}")
print()

# =============================
# 7. DICT vs LIST LOOKUP SPEED
# =============================

print("=== Dict vs List — Lookup Speed ===")
print()

size = 100_000

# Build data
items_list = list(range(size))
items_dict = {i: True for i in range(size)}

# Search for last element
target = size - 1

start = time.time()
_ = target in items_list
t_list = time.time() - start

start = time.time()
_ = target in items_dict
t_dict = time.time() - start

print(f"  Search for {target:,} in {size:,} items:")
print(f"    List: {t_list:.6f}s")
print(f"    Dict: {t_dict:.8f}s")
if t_dict > 0:
    print(f"    Dict is ~{t_list / t_dict:,.0f}x faster!")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Find the longest consecutive sequence in a list
#    (e.g., [100, 4, 200, 1, 3, 2] → [1, 2, 3, 4] → length 4)
# 2. Given a list of integers, find all pairs
#    with a given difference k
# 3. Build a simple phone book using a dictionary
# ============================================
