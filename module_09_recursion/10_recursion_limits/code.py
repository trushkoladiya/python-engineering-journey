# ============================================
# MODULE 9 - SUBTOPIC 10: Recursion Limits & Safety
# ============================================

import sys

# =============================
# 1. PYTHON'S RECURSION LIMIT
# =============================

# --- Example 1: Check the default limit ---
print(f"Default recursion limit: {sys.getrecursionlimit()}")

# --- Example 2: What happens when you exceed it ---
def deep_recursion(n):
    if n <= 0:
        return 0
    return 1 + deep_recursion(n - 1)

# This works:
print(f"\ndeep_recursion(500): {deep_recursion(500)}")

# This might fail depending on the limit:
try:
    result = deep_recursion(5000)
    print(f"deep_recursion(5000): {result}")
except RecursionError:
    print("deep_recursion(5000): ❌ RecursionError! Too deep.")

# =============================
# 2. INFINITE RECURSION
# =============================

# --- Example 3: Missing base case ---
def missing_base(n):
    # No base case! Will recurse forever
    return n + missing_base(n - 1)

try:
    missing_base(5)
except RecursionError:
    print("\n❌ missing_base(5): RecursionError — no base case!")

# --- Example 4: Wrong direction ---
def wrong_direction(n):
    if n <= 0: return 0
    return wrong_direction(n + 1)   # Gets BIGGER, never reaches base case

try:
    wrong_direction(5)
except RecursionError:
    print("❌ wrong_direction(5): RecursionError — moves away from base case!")

# --- Example 5: Base case never reached ---
def bad_condition(n):
    if n == 0: return 0   # Only matches exactly 0
    return bad_condition(n - 2)   # 5→3→1→-1→-3... skips 0!

try:
    bad_condition(5)
except RecursionError:
    print("❌ bad_condition(5): RecursionError — base case is skipped!")

# Fixed version:
def good_condition(n):
    if n <= 0: return 0   # Catches 0 AND negatives
    return good_condition(n - 2)

print(f"✓ good_condition(5): {good_condition(5)}")

# =============================
# 3. CHANGING THE RECURSION LIMIT
# =============================

# --- Example 6: Increasing the limit (use carefully!) ---
original_limit = sys.getrecursionlimit()

# Temporarily increase
sys.setrecursionlimit(10000)
print(f"\nNew limit: {sys.getrecursionlimit()}")

result = deep_recursion(5000)
print(f"deep_recursion(5000): {result}")

# Restore original
sys.setrecursionlimit(original_limit)
print(f"Restored limit: {sys.getrecursionlimit()}")

# =============================
# 4. BETTER SOLUTION: CONVERT TO LOOP
# =============================

# --- Example 7: Deep recursion → iterative ---
# Recursive version (limited)
def sum_recursive(n):
    if n <= 0: return 0
    return n + sum_recursive(n - 1)

# Iterative version (unlimited)
def sum_iterative(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

print(f"\nRecursive sum(900): {sum_recursive(900)}")
print(f"Iterative sum(100000): {sum_iterative(100000)}")

# --- Example 8: Recursive → iterative with a stack ---
def flatten_recursive(items):
    if len(items) == 0: return []
    first = items[0]
    rest = flatten_recursive(items[1:])
    if isinstance(first, list):
        return flatten_recursive(first) + rest
    return [first] + rest

def flatten_iterative(items):
    """Uses an explicit stack instead of recursion."""
    stack = list(items)
    result = []
    while stack:
        item = stack.pop(0)
        if isinstance(item, list):
            stack = item + stack   # Push nested items onto front
        else:
            result.append(item)
    return result

nested = [1, [2, [3, 4]], [5, [6]]]
print(f"\nFlatten recursive: {flatten_recursive(nested)}")
print(f"Flatten iterative: {flatten_iterative(nested)}")

# =============================
# 5. SAFETY CHECKLIST
# =============================

# --- Example 9: Safe recursion pattern ---
def safe_recursive(n, max_depth=100, current_depth=0):
    """Recursion with a safety limit."""
    if current_depth >= max_depth:
        print(f"  ⚠️ Safety limit reached at depth {current_depth}")
        return 0
    if n <= 0:
        return 0
    return n + safe_recursive(n - 1, max_depth, current_depth + 1)

print(f"\nSafe recursion:")
print(f"  safe_recursive(50): {safe_recursive(50)}")
print(f"  safe_recursive(200, max_depth=50):", end=" ")
safe_recursive(200, max_depth=50)

# =============================
# 6. SAFETY CHECKLIST SUMMARY
# =============================

print(f"""
╔═══════════════════════════════════════════════╗
║         RECURSION SAFETY CHECKLIST            ║
╠═══════════════════════════════════════════════╣
║  ✓ Does the function have a base case?        ║
║  ✓ Does every call move toward the base?      ║
║  ✓ Is the base case reachable for all inputs? ║
║  ✓ Is the depth reasonable (< 1000)?          ║
║  ✓ For deep problems, use a loop instead?     ║
╚═══════════════════════════════════════════════╝
""")

# ============================================
# TRY IT YOURSELF:
# 1. Write a function with a missing base case, catch the error
# 2. Convert a recursive function to iterative for large inputs
# 3. Add a depth-safety check to a recursive function
# ============================================
