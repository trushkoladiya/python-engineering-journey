# ============================================
# MODULE 17 - SUBTOPIC 25: Problem Solving Patterns
# ============================================

# Engineering thinking: how to approach DSA problems.
# Recognize patterns, start brute force, optimize.

import time

# =============================
# 1. THE FRAMEWORK: BRUTE FORCE → OPTIMIZE
# =============================

print("=== Framework: Brute Force → Optimize ===")
print()

# Problem: Find two numbers in a list that sum to a target

# Step 1: BRUTE FORCE — check every pair
def two_sum_brute(nums, target):
    """O(n²) — check every pair."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

# Step 2: OPTIMIZE — use hash map for O(1) lookups
def two_sum_optimal(nums, target):
    """O(n) — use hash map."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

data = list(range(10_000))
target = 19_997

start = time.time()
result1 = two_sum_brute(data, target)
t1 = time.time() - start

start = time.time()
result2 = two_sum_optimal(data, target)
t2 = time.time() - start

print(f"  Problem: Two Sum (n={len(data):,})")
print(f"  Brute force O(n²): {result1} in {t1:.4f}s")
print(f"  Optimized O(n):    {result2} in {t2:.6f}s")
print()

# =============================
# 2. PATTERN: HASH MAP FOR FAST LOOKUP
# =============================

print("=== Pattern: Hash Map for Fast Lookup ===")
print()

# Problem: Find the first pair with a given difference
def pair_with_diff_brute(nums, k):
    """O(n²)"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                return (nums[i], nums[j])
    return None

def pair_with_diff_optimal(nums, k):
    """O(n) using set."""
    num_set = set(nums)
    for num in nums:
        if num + k in num_set:
            return (num, num + k)
    return None

data = [1, 8, 3, 11, 7, 2, 15]
k = 4
print(f"  Data: {data}, difference: {k}")
print(f"  Brute: {pair_with_diff_brute(data, k)}")
print(f"  Optimal: {pair_with_diff_optimal(data, k)}")
print("  → When you need lookup, think: hash map or set")
print()

# =============================
# 3. PATTERN: SORT FIRST
# =============================

print("=== Pattern: Sort First ===")
print()

# Problem: Find the closest pair of numbers
def closest_pair_brute(nums):
    """O(n²) — check every pair."""
    min_diff = float('inf')
    pair = None
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            diff = abs(nums[i] - nums[j])
            if diff < min_diff:
                min_diff = diff
                pair = (nums[i], nums[j])
    return pair, min_diff

def closest_pair_sorted(nums):
    """O(n log n) — sort, then check adjacent."""
    sorted_nums = sorted(nums)
    min_diff = float('inf')
    pair = None
    for i in range(len(sorted_nums) - 1):
        diff = sorted_nums[i + 1] - sorted_nums[i]
        if diff < min_diff:
            min_diff = diff
            pair = (sorted_nums[i], sorted_nums[i + 1])
    return pair, min_diff

data = [23, 45, 12, 67, 89, 11, 44, 90]
pair1, diff1 = closest_pair_brute(data)
pair2, diff2 = closest_pair_sorted(data)
print(f"  Data: {data}")
print(f"  Brute O(n²): pair={pair1}, diff={diff1}")
print(f"  Sorted O(n log n): pair={pair2}, diff={diff2}")
print("  → Sorting often reduces the problem complexity")
print()

# =============================
# 4. PATTERN: SLIDING WINDOW
# =============================

print("=== Pattern: Sliding Window ===")
print()

# Problem: Maximum average subarray of size k
def max_avg_brute(nums, k):
    """O(n*k)"""
    max_avg = float('-inf')
    for i in range(len(nums) - k + 1):
        avg = sum(nums[i:i + k]) / k
        max_avg = max(max_avg, avg)
    return max_avg

def max_avg_window(nums, k):
    """O(n) sliding window."""
    window = sum(nums[:k])
    max_sum = window

    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        max_sum = max(max_sum, window)

    return max_sum / k

data = [1, 12, -5, -6, 50, 3]
k = 4
print(f"  Data: {data}, k={k}")
print(f"  Brute: {max_avg_brute(data, k):.2f}")
print(f"  Window: {max_avg_window(data, k):.2f}")
print("  → Contiguous subarray → think sliding window")
print()

# =============================
# 5. PATTERN: TWO POINTERS
# =============================

print("=== Pattern: Two Pointers ===")
print()

# Problem: Is there a triplet that sums to zero?
def three_sum_brute(nums):
    """O(n³)"""
    result = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    return [list(t) for t in result]

def three_sum_optimal(nums):
    """O(n²) — sort + two pointers."""
    nums = sorted(nums)
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue    # skip duplicates

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

data = [-1, 0, 1, 2, -1, -4]
result = three_sum_optimal(data)
print(f"  Data: {data}")
print(f"  Triplets summing to 0: {result}")
print("  → Sorted data + pair finding → two pointers")
print()

# =============================
# 6. PATTERN: FREQUENCY MAP
# =============================

print("=== Pattern: Frequency Map ===")
print()

# Problem: Find the majority element (appears > n/2 times)
def majority_brute(nums):
    """O(n²)"""
    for num in nums:
        count = sum(1 for x in nums if x == num)
        if count > len(nums) // 2:
            return num
    return None

def majority_optimal(nums):
    """O(n) — Boyer-Moore voting algorithm."""
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate

data = [3, 2, 3, 3, 1, 3, 3, 2]
print(f"  Data: {data}")
print(f"  Majority element: {majority_optimal(data)}")
print("  → Counting/frequency → think hash map or specialized algorithm")
print()

# =============================
# 7. CHOOSING THE RIGHT APPROACH
# =============================

print("=== Decision Guide ===")
print()

guide = [
    ("Need fast lookup?", "→ Use hash map (dict) or set"),
    ("Data is sorted?", "→ Use binary search or two pointers"),
    ("Contiguous subarray?", "→ Use sliding window"),
    ("All combinations?", "→ Use backtracking"),
    ("Optimal from subproblems?", "→ Use dynamic programming"),
    ("Local choice = global?", "→ Use greedy"),
    ("Tree/graph exploration?", "→ Use DFS or BFS"),
    ("Need ordering?", "→ Sort first, then solve"),
]

for question, answer in guide:
    print(f"  {question:30} {answer}")
print()

# =============================
# 8. COMPLETE EXAMPLE: OPTIMIZE STEP BY STEP
# =============================

print("=== Complete Example: Step-by-Step Optimization ===")
print()

# Problem: Find if array has two elements with diff = k

data = list(range(5000))
k = 4999

# V1: Brute force O(n²)
start = time.time()
found_v1 = None
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if abs(data[i] - data[j]) == k:
            found_v1 = (data[i], data[j])
            break
    if found_v1:
        break
t1 = time.time() - start

# V2: Sort + two pointers O(n log n)
start = time.time()
sorted_data = sorted(data)
found_v2 = None
i, j = 0, 1
while j < len(sorted_data):
    diff = sorted_data[j] - sorted_data[i]
    if diff == k:
        found_v2 = (sorted_data[i], sorted_data[j])
        break
    elif diff < k:
        j += 1
    else:
        i += 1
t2 = time.time() - start

# V3: Hash set O(n)
start = time.time()
data_set = set(data)
found_v3 = None
for num in data:
    if num + k in data_set:
        found_v3 = (num, num + k)
        break
t3 = time.time() - start

print(f"  n={len(data):,}, k={k}")
print(f"  V1 O(n²):      {found_v1} in {t1:.4f}s")
print(f"  V2 O(n log n):  {found_v2} in {t2:.6f}s")
print(f"  V3 O(n):        {found_v3} in {t3:.6f}s")
print()
print("  → Each optimization used a different pattern!")
print("  → V1: brute force → V2: sort + two pointers → V3: hash set")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Given a list, find the subarray with the
#    largest sum (try brute force, then Kadane's algorithm)
# 2. Find all anagrams of a pattern in a text
#    (hint: sliding window + frequency map)
# 3. Optimize: given a sorted matrix, find a target
#    (try brute force, then use the sorted property)
# ============================================
