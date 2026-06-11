# ============================================
# MODULE 17 - SUBTOPIC 4: Arrays — Advanced Patterns
# ============================================

# Two powerful techniques: two-pointer and sliding window.
# Both turn O(n²) brute-force into O(n) solutions.

# =============================
# 1. TWO-POINTER — PAIR SUM (SORTED)
# =============================

print("=== Two-Pointer: Pair Sum in Sorted List ===")
print()

def two_sum_sorted(numbers, target):
    """Find a pair that sums to target in a sorted list. O(n)."""
    left = 0
    right = len(numbers) - 1

    while left < right:
        current = numbers[left] + numbers[right]
        if current == target:
            return (numbers[left], numbers[right])
        elif current < target:
            left += 1      # need a bigger sum → move left pointer right
        else:
            right -= 1     # need a smaller sum → move right pointer left
    return None

sorted_data = [1, 3, 5, 7, 9, 11, 15, 20]
print(f"  Data: {sorted_data}")

for target in [12, 16, 26, 100]:
    result = two_sum_sorted(sorted_data, target)
    if result:
        print(f"  Target {target}: {result[0]} + {result[1]} = {target}")
    else:
        print(f"  Target {target}: no pair found")
print()

# =============================
# 2. TWO-POINTER — REMOVE DUPLICATES (SORTED)
# =============================

print("=== Two-Pointer: Remove Duplicates from Sorted List ===")
print()

def remove_duplicates(sorted_list):
    """Remove duplicates in-place from sorted list. Returns new length."""
    if not sorted_list:
        return 0

    write = 1    # position to write next unique element
    for read in range(1, len(sorted_list)):
        if sorted_list[read] != sorted_list[write - 1]:
            sorted_list[write] = sorted_list[read]
            write += 1
    return write

data = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5]
print(f"  Before: {data}")
new_length = remove_duplicates(data)
print(f"  After:  {data[:new_length]}")
print(f"  Unique count: {new_length}")
print()

# =============================
# 3. TWO-POINTER — PALINDROME CHECK
# =============================

print("=== Two-Pointer: Palindrome Check ===")
print()

def is_palindrome(text):
    """Check if text is a palindrome using two pointers."""
    clean = text.lower().replace(" ", "")
    left = 0
    right = len(clean) - 1

    while left < right:
        if clean[left] != clean[right]:
            return False
        left += 1
        right -= 1
    return True

test_words = ["racecar", "hello", "madam", "level", "python", "A man a plan a canal Panama"]
for word in test_words:
    result = "✓ palindrome" if is_palindrome(word) else "✗ not palindrome"
    print(f"  '{word}' → {result}")
print()

# =============================
# 4. TWO-POINTER — CONTAINER WITH MOST WATER
# =============================

print("=== Two-Pointer: Container With Most Water ===")
print()

def max_water(heights):
    """Find the maximum area between two lines."""
    left = 0
    right = len(heights) - 1
    max_area = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        max_area = max(max_area, area)

        # Move the shorter line inward
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

bars = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"  Heights: {bars}")
print(f"  Max water area: {max_water(bars)}")
print()

# =============================
# 5. SLIDING WINDOW — MAX SUM OF K ELEMENTS
# =============================

print("=== Sliding Window: Max Sum of K Consecutive Elements ===")
print()

def max_sum_subarray(numbers, k):
    """Find maximum sum of k consecutive elements. O(n)."""
    if len(numbers) < k:
        return None

    # Calculate first window
    window_sum = sum(numbers[:k])
    max_sum = window_sum
    max_start = 0

    # Slide the window
    for i in range(k, len(numbers)):
        window_sum += numbers[i]         # add new element entering window
        window_sum -= numbers[i - k]     # remove element leaving window
        if window_sum > max_sum:
            max_sum = window_sum
            max_start = i - k + 1

    return max_sum, max_start

data = [2, 1, 5, 1, 3, 2, 8, 4, 6]
k = 3
result, start = max_sum_subarray(data, k)
print(f"  Data: {data}")
print(f"  k = {k}")
print(f"  Max sum: {result} (subarray: {data[start:start + k]})")
print()

# Compare with brute force
print("  Why sliding window is better:")
print("    Brute force: recalculate sum for each position → O(n × k)")
print("    Sliding window: reuse previous sum → O(n)")
print()

# =============================
# 6. SLIDING WINDOW — LONGEST SUBSTRING WITHOUT REPEATS
# =============================

print("=== Sliding Window: Longest Substring Without Repeating Characters ===")
print()

def longest_unique_substring(s):
    """Find length of longest substring without repeating characters."""
    seen = {}          # char → last index
    max_length = 0
    start = 0          # window start

    for end in range(len(s)):
        if s[end] in seen and seen[s[end]] >= start:
            start = seen[s[end]] + 1    # move window past the duplicate
        seen[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

test_strings = ["abcabcbb", "bbbbb", "pwwkew", "abcdef"]
for s in test_strings:
    length = longest_unique_substring(s)
    print(f"  '{s}' → longest unique substring length: {length}")
print()

# =============================
# 7. SLIDING WINDOW — AVERAGE OF SUBARRAYS
# =============================

print("=== Sliding Window: Average of All Subarrays ===")
print()

def subarray_averages(numbers, k):
    """Calculate average of all subarrays of size k."""
    if len(numbers) < k:
        return []

    averages = []
    window_sum = sum(numbers[:k])
    averages.append(window_sum / k)

    for i in range(k, len(numbers)):
        window_sum += numbers[i]
        window_sum -= numbers[i - k]
        averages.append(window_sum / k)

    return averages

data = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
avgs = subarray_averages(data, k)
print(f"  Data: {data}")
print(f"  k = {k}")
print(f"  Averages: {[f'{a:.1f}' for a in avgs]}")
print()

# =============================
# 8. COMPARING APPROACHES
# =============================

print("=== Pattern Summary ===")
print()

import time

# Problem: Find if sorted list has two numbers summing to target
size = 50_000
sorted_data = list(range(size))
target = size + size - 3   # near the end

# Brute force O(n²)
start = time.time()
found_brute = None
for i in range(min(len(sorted_data), 1000)):   # limited for speed
    for j in range(i + 1, min(len(sorted_data), 1000)):
        if sorted_data[i] + sorted_data[j] == target:
            found_brute = (sorted_data[i], sorted_data[j])
            break
t_brute = time.time() - start

# Two-pointer O(n)
start = time.time()
found_smart = two_sum_sorted(sorted_data, target)
t_smart = time.time() - start

print(f"  Two-pointer found: {found_smart}")
print(f"  Two-pointer time: {t_smart:.6f}s")
print()

patterns = [
    ("Two-Pointer", "Sorted data, pair problems, palindromes"),
    ("Sliding Window", "Contiguous subarrays, substring problems"),
]
for name, use_case in patterns:
    print(f"  {name}:")
    print(f"    Use when: {use_case}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use two-pointer to find three numbers that sum
#    to a target (sort first, then fix one and two-pointer the rest)
# 2. Use sliding window to find the minimum sum subarray of size k
# 3. Use two-pointer to merge two sorted lists into one sorted list
# ============================================
