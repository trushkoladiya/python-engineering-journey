# ============================================
# MODULE 9 - SUBTOPIC 13: Common Mistakes & Debugging
# ============================================

# =============================
# 1. MISTAKE: MISSING BASE CASE
# =============================

# --- Example 1: No base case ---
def sum_no_base(n):
    return n + sum_no_base(n - 1)   # Never stops!

try:
    sum_no_base(5)
except RecursionError:
    print("❌ Mistake 1: Missing base case → RecursionError")

# --- Example 2: Fixed ---
def sum_fixed(n):
    if n <= 0: return 0   # ✅ Base case added
    return n + sum_fixed(n - 1)

print(f"✓ Fixed: sum(5) = {sum_fixed(5)}")

# =============================
# 2. MISTAKE: BASE CASE NEVER REACHED
# =============================

# --- Example 3: Wrong direction ---
def wrong_direction(n):
    if n <= 0: return 0
    return wrong_direction(n + 1)   # Gets BIGGER!

try:
    wrong_direction(5)
except RecursionError:
    print(f"\n❌ Mistake 2: n grows instead of shrinking → RecursionError")

# --- Example 4: Skipping the base case ---
def skip_base(n):
    if n == 0: return 0    # Only catches exactly 0
    return skip_base(n - 2)   # 5 → 3 → 1 → -1 → skips 0!

try:
    skip_base(5)
except RecursionError:
    print("❌ Mistake 2b: Base case skipped → RecursionError")

# Fix: use <= instead of ==
def skip_fixed(n):
    if n <= 0: return 0   # ✅ Catches 0 AND negatives
    return skip_fixed(n - 2)

print(f"✓ Fixed: skip(5) = {skip_fixed(5)}")

# =============================
# 3. MISTAKE: FORGETTING TO RETURN
# =============================

# --- Example 5: Missing return ---
def sum_no_return(n):
    if n <= 0: return 0
    sum_no_return(n - 1)   # ❌ Forgot 'return'!

result = sum_no_return(5)
print(f"\n❌ Mistake 3: Missing return → result is {result} (None!)")

# --- Example 6: Fixed ---
def sum_with_return(n):
    if n <= 0: return 0
    return n + sum_with_return(n - 1)   # ✅ return added

print(f"✓ Fixed: sum(5) = {sum_with_return(5)}")

# =============================
# 4. MISTAKE: MODIFYING SHARED STATE
# =============================

# --- Example 7: Shared mutable default ---
def collect_bad(n, result=[]):   # ❌ Shared list!
    if n <= 0: return result
    result.append(n)
    return collect_bad(n - 1, result)

print(f"\n❌ Mistake 4: Mutable default")
print(f"  Call 1: {collect_bad(3)}")
print(f"  Call 2: {collect_bad(3)}")   # Contains data from call 1!

# --- Example 8: Fixed with None ---
def collect_good(n, result=None):
    if result is None: result = []   # ✅ Fresh list each time
    if n <= 0: return result
    result.append(n)
    return collect_good(n - 1, result)

print(f"\n✓ Fixed:")
print(f"  Call 1: {collect_good(3)}")
print(f"  Call 2: {collect_good(3)}")

# =============================
# 5. DEBUGGING: TRACING WITH PRINTS
# =============================

# --- Example 9: Basic trace ---
def factorial_debug(n):
    print(f"  Called factorial({n})")
    if n <= 1:
        print(f"  Base case: returning 1")
        return 1
    result = n * factorial_debug(n - 1)
    print(f"  factorial({n}) = {n} * ... = {result}")
    return result

print(f"\nDebug trace:")
factorial_debug(4)

# --- Example 10: Trace with indentation ---
def debug_trace(func_name):
    """Create a tracing decorator for recursive functions."""
    def decorator(func):
        depth = [0]
        def wrapper(*args):
            indent = "  " * depth[0]
            args_str = ", ".join(str(a) for a in args)
            print(f"{indent}→ {func_name}({args_str})")
            depth[0] += 1
            result = func(*args)
            depth[0] -= 1
            print(f"{indent}← {func_name}({args_str}) = {result}")
            return result
        return wrapper
    return decorator

@debug_trace("fib")
def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)

print(f"\nTraced fibonacci(4):")
fib(4)

# =============================
# 6. DEBUGGING: TEST WITH TINY INPUTS
# =============================

# --- Example 11: Systematic testing ---
def my_sum(items):
    if len(items) == 0: return 0
    return items[0] + my_sum(items[1:])

print(f"\nTest with tiny inputs first:")
print(f"  [] → {my_sum([])}")           # Base case
print(f"  [5] → {my_sum([5])}")         # Single element
print(f"  [1,2] → {my_sum([1, 2])}")   # Two elements
print(f"  [1,2,3] → {my_sum([1, 2, 3])}")   # Normal case

# =============================
# 7. DEBUGGING CHECKLIST
# =============================

print(f"""
╔═══════════════════════════════════════════════╗
║         RECURSION DEBUGGING CHECKLIST         ║
╠═══════════════════════════════════════════════╣
║  1. Is there a base case?                     ║
║  2. Does every path reach the base case?      ║
║  3. Do I RETURN the recursive call?           ║
║  4. Does the input get SMALLER each call?     ║
║  5. Am I using mutable defaults safely?       ║
║  6. Does it work for the smallest input?      ║
║  7. Did I trace it with print statements?     ║
╚═══════════════════════════════════════════════╝
""")

# ============================================
# TRY IT YOURSELF:
# 1. Find and fix the bug in a recursive reverse function
# 2. Add debug tracing to your own recursive function
# 3. Test a recursive function with edge cases: 0, 1, negative
# ============================================
