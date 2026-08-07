# ============================================
# MODULE 17 - SUBTOPIC 13: Recursion in DSA
# ============================================

# Using recursion for divide-and-conquer
# and recursive problem solving.

# =============================
# 1. DIVIDE AND CONQUER — FIND MAX
# =============================

print("=== Divide and Conquer — Find Maximum ===")
print()

def find_max(items, start, end):
    """Find maximum using divide and conquer."""
    # Base case: single element
    if start == end:
        return items[start]

    # Divide
    mid = (start + end) // 2
    left_max = find_max(items, start, mid)
    right_max = find_max(items, mid + 1, end)

    # Combine
    return max(left_max, right_max)

data = [34, 67, 12, 89, 45, 23, 78, 56]
result = find_max(data, 0, len(data) - 1)
print(f"  Data: {data}")
print(f"  Max:  {result}")
print()

# =============================
# 2. DIVIDE AND CONQUER — SUM
# =============================

print("=== Divide and Conquer — Sum ===")
print()

def recursive_sum(items, start, end):
    """Sum elements using divide and conquer."""
    if start == end:
        return items[start]

    mid = (start + end) // 2
    left_sum = recursive_sum(items, start, mid)
    right_sum = recursive_sum(items, mid + 1, end)
    return left_sum + right_sum

data = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_sum(data, 0, len(data) - 1)
print(f"  Data: {data}")
print(f"  Sum:  {result} (verify: {sum(data)})")
print()

# =============================
# 3. POWER FUNCTION (FAST EXPONENTIATION)
# =============================

print("=== Fast Exponentiation ===")
print()

def power(base, exp):
    """Calculate base^exp using divide and conquer. O(log n)."""
    if exp == 0:
        return 1
    if exp == 1:
        return base

    # Divide: x^n = (x^(n/2))^2
    half = power(base, exp // 2)

    if exp % 2 == 0:
        return half * half
    else:
        return half * half * base

test_cases = [(2, 10), (3, 5), (5, 3), (2, 20)]
for b, e in test_cases:
    result = power(b, e)
    print(f"  {b}^{e} = {result}")
print()

# Counting multiplications
def power_count(base, exp):
    """Count how many multiplications are needed."""
    if exp == 0 or exp == 1:
        return 0
    half_ops = power_count(base, exp // 2)
    return half_ops + (1 if exp % 2 == 0 else 2)

print("  Multiplications needed:")
for exp in [4, 8, 16, 32, 64, 1000]:
    ops = power_count(2, exp)
    print(f"    2^{exp}: {ops} multiplications (vs {exp - 1} naive)")
print()

# =============================
# 4. GENERATE ALL SUBSETS
# =============================

print("=== Generate All Subsets ===")
print()

def subsets(items):
    """Generate all subsets of a list."""
    if not items:
        return [[]]

    first = items[0]
    rest_subsets = subsets(items[1:])

    # Each subset either includes or excludes 'first'
    with_first = [[first] + s for s in rest_subsets]
    return rest_subsets + with_first

data = [1, 2, 3]
all_subsets = subsets(data)
print(f"  Items: {data}")
print(f"  Subsets ({len(all_subsets)} total):")
for s in all_subsets:
    print(f"    {s}")
print()

# =============================
# 5. GENERATE PERMUTATIONS
# =============================

print("=== Generate Permutations ===")
print()

def permutations(items):
    """Generate all permutations of a list."""
    if len(items) <= 1:
        return [items]

    result = []
    for i in range(len(items)):
        current = items[i]
        remaining = items[:i] + items[i + 1:]
        for perm in permutations(remaining):
            result.append([current] + perm)
    return result

data = [1, 2, 3]
all_perms = permutations(data)
print(f"  Items: {data}")
print(f"  Permutations ({len(all_perms)} total):")
for p in all_perms:
    print(f"    {p}")
print()

# =============================
# 6. TOWER OF HANOI
# =============================

print("=== Tower of Hanoi ===")
print()

def hanoi(n, source, target, auxiliary):
    """Solve Tower of Hanoi with n disks."""
    if n == 1:
        print(f"    Move disk 1 from {source} to {target}")
        return 1

    moves = 0
    moves += hanoi(n - 1, source, auxiliary, target)
    print(f"    Move disk {n} from {source} to {target}")
    moves += 1
    moves += hanoi(n - 1, auxiliary, target, source)
    return moves

print("  3 disks:")
total_moves = hanoi(3, "A", "C", "B")
print(f"  Total moves: {total_moves}")
print()

# The pattern: n disks need 2^n - 1 moves
print("  Moves needed for n disks:")
for n in range(1, 8):
    moves = 2 ** n - 1
    print(f"    {n} disks: {moves} moves")
print()

# =============================
# 7. RECURSIVE BINARY SEARCH
# =============================

print("=== Recursive Binary Search ===")
print()

def binary_search(items, target, left, right, depth=0):
    """Binary search with recursion depth tracking."""
    indent = "    " * depth
    if left > right:
        return -1

    mid = (left + right) // 2
    print(f"  {indent}Checking index {mid}: value={items[mid]}", end="")

    if items[mid] == target:
        print(" ← FOUND!")
        return mid
    elif items[mid] < target:
        print(" → go right")
        return binary_search(items, target, mid + 1, right, depth + 1)
    else:
        print(" → go left")
        return binary_search(items, target, left, mid - 1, depth + 1)

data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"  Data: {data}")
print(f"  Searching for 13:")
result = binary_search(data, 13, 0, len(data) - 1)
print(f"  Found at index: {result}")
print()

# =============================
# 8. RECURSIVE vs ITERATIVE THINKING
# =============================

print("=== When to Use Recursion ===")
print()

approaches = [
    ("Linear search", "Iterative", "Simple loop, no benefit from recursion"),
    ("Binary search", "Both", "Iterative preferred, recursive works"),
    ("Tree traversal", "Recursive", "Natural fit — trees are recursive structures"),
    ("Merge sort", "Recursive", "Divide and conquer is naturally recursive"),
    ("Fibonacci", "Iterative", "Recursive is slow without memoization"),
    ("Subsets/Perms", "Recursive", "Exploring all possibilities"),
]

for problem, preferred, reason in approaches:
    print(f"  {problem:18} → {preferred:10} | {reason}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a recursive function to count the number
#    of digits in a positive integer
# 2. Write a recursive function to check if a list
#    is sorted (compare first two, recurse on rest)
# 3. Generate all binary strings of length n
# ============================================
