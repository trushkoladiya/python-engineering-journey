# ============================================
# MODULE 17 - SUBTOPIC 2: Complexity Basics
# ============================================

# Complexity = how fast (time) and how much memory (space)
# an algorithm uses as input grows.

import time

# =============================
# 1. O(1) — CONSTANT TIME
# =============================

print("=== O(1) — Constant Time ===")
print()

# The operation takes the SAME time regardless of data size

# Dict lookup — O(1)
phonebook = {"Trush": "555-0001", "Rahul": "555-0002", "Charlie": "555-0003"}
print(f"  phonebook['Rahul'] = {phonebook['Rahul']}")
print("  → Dict lookup is O(1) — instant, no matter how big the dict")
print()

# List index access — O(1)
numbers = [10, 20, 30, 40, 50]
print(f"  numbers[3] = {numbers[3]}")
print("  → Index access is O(1) — jumps directly to position")
print()

# =============================
# 2. O(n) — LINEAR TIME
# =============================

print("=== O(n) — Linear Time ===")
print()

# Time grows proportionally with input size

def find_max(items):
    """Find maximum value — must check every element."""
    maximum = items[0]
    for item in items:        # visits each item once → O(n)
        if item > maximum:
            maximum = item
    return maximum

data = [23, 67, 12, 89, 45, 34, 78]
print(f"  Data: {data}")
print(f"  Max:  {find_max(data)}")
print("  → Checked every element once → O(n)")
print()

# =============================
# 3. O(n²) — QUADRATIC TIME
# =============================

print("=== O(n²) — Quadratic Time ===")
print()

# Nested loops — time grows with the SQUARE of input

def has_duplicates_brute(items):
    """Check for duplicates by comparing every pair."""
    comparisons = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):   # nested loop → O(n²)
            comparisons += 1
            if items[i] == items[j]:
                return True, comparisons
    return False, comparisons

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
found, comps = has_duplicates_brute(test)
print(f"  List of {len(test)} items → {comps} comparisons")

test2 = list(range(20))
found2, comps2 = has_duplicates_brute(test2)
print(f"  List of {len(test2)} items → {comps2} comparisons")
print("  → Double the input, quadruple the work!")
print()

# =============================
# 4. O(n) vs O(n²) — REAL COMPARISON
# =============================

print("=== O(n) vs O(n²) — Speed Comparison ===")
print()

# O(n²) approach: check every pair
def find_pair_sum_brute(numbers, target):
    """Find two numbers that add to target — O(n²)."""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])
    return None

# O(n) approach: use a set for lookups
def find_pair_sum_smart(numbers, target):
    """Find two numbers that add to target — O(n)."""
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:       # set lookup is O(1)
            return (complement, num)
        seen.add(num)
    return None

test_data = list(range(10_000))
target = 19_997   # last two numbers: 9998 + 9999

start = time.time()
result1 = find_pair_sum_brute(test_data, target)
time_brute = time.time() - start

start = time.time()
result2 = find_pair_sum_smart(test_data, target)
time_smart = time.time() - start

print(f"  Looking for pair summing to {target} in {len(test_data):,} items:")
print(f"  Brute force O(n²): {result1} in {time_brute:.4f}s")
print(f"  Smart O(n):        {result2} in {time_smart:.6f}s")
if time_smart > 0:
    print(f"  Smart approach was ~{time_brute / time_smart:.0f}x faster!")
print()

# =============================
# 5. O(log n) — LOGARITHMIC TIME
# =============================

print("=== O(log n) — Logarithmic Time ===")
print()

# Each step HALVES the problem — very efficient
# Binary search is O(log n) — we'll cover it in detail later

def count_halvings(n):
    """Count how many times we can halve n before reaching 1."""
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps

# Notice how slowly steps grow compared to n
for size in [10, 100, 1000, 10_000, 100_000, 1_000_000]:
    steps = count_halvings(size)
    print(f"  n = {size:>10,} → {steps:2} halvings")
print()
print("  → 1 million items needs only ~20 steps!")
print()

# =============================
# 6. SPACE COMPLEXITY
# =============================

print("=== Space Complexity ===")
print()

# O(1) space — uses a fixed amount of extra memory
def sum_list(items):
    """Sum without creating new data. O(1) extra space."""
    total = 0        # just one variable
    for item in items:
        total += item
    return total

print(f"  sum_list O(1) space: {sum_list([1, 2, 3, 4, 5])}")

# O(n) space — creates a new collection proportional to input
def double_all(items):
    """Double every value. O(n) extra space."""
    return [x * 2 for x in items]    # new list of same size

print(f"  double_all O(n) space: {double_all([1, 2, 3, 4, 5])}")
print()

# Trade-off example: speed vs memory
print("  Speed vs Memory Trade-off:")

# Slow but memory-efficient — O(n²) time, O(1) space
def has_dup_slow(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False

# Fast but uses more memory — O(n) time, O(n) space
def has_dup_fast(items):
    seen = set()        # extra memory
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

test = list(range(5000)) + [0]   # duplicate at the end

start = time.time()
has_dup_slow(test)
t1 = time.time() - start

start = time.time()
has_dup_fast(test)
t2 = time.time() - start

print(f"    O(n²) time, O(1) space: {t1:.4f}s")
print(f"    O(n) time,  O(n) space: {t2:.6f}s")
print("    → Trading memory for speed is often worth it!")
print()

# =============================
# 7. IDENTIFYING COMPLEXITY
# =============================

print("=== How to Identify Complexity ===")
print()

# Rule of thumb:
# - No loops → O(1)
# - Single loop → O(n)
# - Nested loops → O(n²)
# - Halving each step → O(log n)
# - Single loop with O(1) lookup → O(n)

examples = [
    ("Dict lookup", "O(1)", "my_dict[key]"),
    ("Single for loop", "O(n)", "for x in list: ..."),
    ("Two nested loops", "O(n²)", "for i: for j: ..."),
    ("Halving loop", "O(log n)", "while n > 1: n //= 2"),
    ("Sort", "O(n log n)", "sorted(list)"),
]

for name, complexity, code in examples:
    print(f"  {name:25} → {complexity:10} | {code}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. What is the time complexity of:
#    - Looking up a key in a dictionary?
#    - Finding the minimum value in an unsorted list?
#    - Checking if a sorted list contains a value (using binary search)?
# 2. Write a function to reverse a list.
#    What is its time and space complexity?
# 3. Which is better for checking membership: list or set? Why?
# ============================================
