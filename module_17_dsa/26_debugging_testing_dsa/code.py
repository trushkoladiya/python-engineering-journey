# ============================================
# MODULE 17 - SUBTOPIC 26: Debugging & Testing DSA Code
# ============================================

# Techniques for finding and preventing bugs in
# algorithm implementations.

import random

# =============================
# 1. DRY RUN — TRACE BY HAND
# =============================

print("=== Dry Run — Tracing an Algorithm ===")
print()

def binary_search_traced(items, target):
    """Binary search with detailed trace output."""
    left = 0
    right = len(items) - 1
    step = 0

    print(f"  Searching for {target} in {items}")
    while left <= right:
        step += 1
        mid = (left + right) // 2
        print(f"    Step {step}: left={left}, right={right}, "
              f"mid={mid}, items[mid]={items[mid]}", end="")

        if items[mid] == target:
            print(f" → FOUND at index {mid}")
            return mid
        elif items[mid] < target:
            print(f" → {items[mid]} < {target}, go RIGHT")
            left = mid + 1
        else:
            print(f" → {items[mid]} > {target}, go LEFT")
            right = mid - 1

    print(f"    Not found after {step} steps")
    return -1

binary_search_traced([1, 3, 5, 7, 9, 11, 13], 7)
print()

# =============================
# 2. EDGE CASE TESTING
# =============================

print("=== Edge Case Testing ===")
print()

def binary_search(items, target):
    """Standard binary search."""
    left, right = 0, len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Edge case tests
edge_cases = [
    ("Empty list", [], 5, -1),
    ("Single element (found)", [5], 5, 0),
    ("Single element (not found)", [5], 3, -1),
    ("First element", [1, 3, 5, 7], 1, 0),
    ("Last element", [1, 3, 5, 7], 7, 3),
    ("Middle element", [1, 3, 5, 7, 9], 5, 2),
    ("Not present (too small)", [1, 3, 5, 7], 0, -1),
    ("Not present (too large)", [1, 3, 5, 7], 8, -1),
    ("Not present (between)", [1, 3, 5, 7], 4, -1),
    ("Two elements", [1, 3], 1, 0),
    ("Negative numbers", [-5, -3, -1, 0, 2], -3, 1),
]

all_passed = True
for name, data, target, expected in edge_cases:
    result = binary_search(data, target)
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} {name:35} → got {result}, expected {expected}")

print(f"\n  {'All tests passed!' if all_passed else 'Some tests FAILED!'}")
print()

# =============================
# 3. ASSERT-BASED TESTING
# =============================

print("=== Assert-Based Testing ===")
print()

def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

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

# Test with assertions
try:
    assert merge_sort([]) == [], "Empty list"
    assert merge_sort([1]) == [1], "Single element"
    assert merge_sort([2, 1]) == [1, 2], "Two elements"
    assert merge_sort([3, 1, 2]) == [1, 2, 3], "Three elements"
    assert merge_sort([5, 5, 5]) == [5, 5, 5], "All same"
    assert merge_sort([1, 2, 3]) == [1, 2, 3], "Already sorted"
    assert merge_sort([3, 2, 1]) == [1, 2, 3], "Reverse sorted"
    assert merge_sort([-3, 1, -1, 2]) == [-3, -1, 1, 2], "Negative numbers"
    print("  ✓ All merge_sort assertions passed!")
except AssertionError as e:
    print(f"  ✗ Failed: {e}")
print()

# =============================
# 4. TESTING AGAINST BRUTE FORCE
# =============================

print("=== Testing Against Brute Force ===")
print()

def two_sum_brute(nums, target):
    """Known correct O(n²) solution."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_optimal(nums, target):
    """Optimized O(n) solution — is it correct?"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

# Random testing: compare optimal vs brute force
print("  Comparing optimal vs brute force (100 random tests):")
failures = 0
for _ in range(100):
    size = random.randint(2, 20)
    nums = [random.randint(-50, 50) for _ in range(size)]
    target = random.randint(-100, 100)

    brute = two_sum_brute(nums, target)
    optimal = two_sum_optimal(nums, target)

    # Both should agree on whether a solution exists
    brute_exists = brute is not None
    optimal_exists = optimal is not None

    if brute_exists != optimal_exists:
        failures += 1
        print(f"    ✗ Mismatch: nums={nums}, target={target}")
        print(f"      Brute: {brute}, Optimal: {optimal}")

    # If both found a solution, verify correctness
    if brute_exists and optimal_exists:
        if nums[optimal[0]] + nums[optimal[1]] != target:
            failures += 1
            print(f"    ✗ Wrong answer: nums={nums}, target={target}")

if failures == 0:
    print("  ✓ All 100 random tests passed!")
else:
    print(f"  ✗ {failures} tests failed!")
print()

# =============================
# 5. COMMON BUG PATTERNS
# =============================

print("=== Common Bug Patterns in DSA ===")
print()

# Bug 1: Off-by-one error
print("  Bug 1: Off-by-one errors")
print("    WRONG: for i in range(len(arr)):  # when you need len-1")
print("    RIGHT: for i in range(len(arr) - 1):  # for adjacent pairs")
print()

# Bug 2: Integer overflow in mid calculation
print("  Bug 2: Mid calculation")
print("    RISKY:  mid = (left + right) // 2  # can overflow in some languages")
print("    SAFER:  mid = left + (right - left) // 2")
print("    (Python handles big integers natively, but good habit)")
print()

# Bug 3: Modifying list while iterating
print("  Bug 3: Modifying while iterating")
data = [1, 2, 3, 4, 5]
# WRONG way:
# for item in data:
#     if item % 2 == 0:
#         data.remove(item)   # skips elements!

# RIGHT way:
filtered = [item for item in data if item % 2 != 0]
print(f"    Remove evens from {data}: {filtered}")
print()

# =============================
# 6. DEBUGGING WITH PRINT STATEMENTS
# =============================

print("=== Strategic Print Debugging ===")
print()

def find_peak(nums, debug=False):
    """Find a peak element (greater than neighbors)."""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if debug:
            print(f"    left={left}, right={right}, mid={mid}, "
                  f"nums[mid]={nums[mid]}, nums[mid+1]={nums[mid+1]}")

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
            if debug:
                print(f"    → going right")
        else:
            right = mid
            if debug:
                print(f"    → going left")

    if debug:
        print(f"    → peak at index {left}: value={nums[left]}")
    return left

data = [1, 3, 5, 7, 6, 4, 2]
print(f"  Finding peak in {data}:")
peak = find_peak(data, debug=True)
print(f"  Peak: index={peak}, value={data[peak]}")
print()

# =============================
# 7. COMPREHENSIVE TEST FUNCTION
# =============================

print("=== Building a Test Framework ===")
print()

def run_tests(func, test_cases, func_name="function"):
    """Run multiple test cases and report results."""
    passed = 0
    failed = 0

    for inputs, expected in test_cases:
        if isinstance(inputs, tuple):
            result = func(*inputs)
        else:
            result = func(inputs)

        if result == expected:
            passed += 1
        else:
            failed += 1
            print(f"  ✗ {func_name}({inputs}) = {result}, expected {expected}")

    total = passed + failed
    print(f"  {func_name}: {passed}/{total} tests passed")
    return failed == 0

# Test binary search
binary_search_tests = [
    (([1, 3, 5, 7, 9], 5), 2),
    (([1, 3, 5, 7, 9], 1), 0),
    (([1, 3, 5, 7, 9], 9), 4),
    (([1, 3, 5, 7, 9], 4), -1),
    (([], 5), -1),
    (([5], 5), 0),
    (([5], 3), -1),
]

run_tests(binary_search, binary_search_tests, "binary_search")
print()

# Test merge sort
merge_sort_tests = [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, 5, 5], [5, 5, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
]

run_tests(merge_sort, merge_sort_tests, "merge_sort")
print()

# =============================
# 8. DEBUGGING CHECKLIST
# =============================

print("=== DSA Debugging Checklist ===")
print()

checklist = [
    "1. Does it handle empty input?",
    "2. Does it handle single-element input?",
    "3. Are loop bounds correct? (off-by-one?)",
    "4. Does it handle duplicates?",
    "5. Does it handle negative numbers?",
    "6. Does it handle already-sorted input?",
    "7. Does it handle reverse-sorted input?",
    "8. Does the base case in recursion terminate?",
    "9. Is the return value correct for all paths?",
    "10. Did you test against a brute-force solution?",
]

for item in checklist:
    print(f"  □ {item}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a bug intentionally in binary search
#    (e.g., use < instead of <=), then debug it
# 2. Write a comprehensive test suite for your
#    own sorting algorithm implementation
# 3. Use random testing to verify that your
#    optimized solution matches brute force
# ============================================
