# ============================================
# MODULE 9 - SUBTOPIC 8: Recursion vs Iteration
# ============================================

# =============================
# 1. SAME PROBLEM, TWO WAYS
# =============================

# --- Example 1: Factorial ---
def factorial_recursive(n):
    if n <= 1: return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print("Factorial comparison:")
print(f"  Recursive: {factorial_recursive(10)}")
print(f"  Iterative: {factorial_iterative(10)}")

# --- Example 2: Sum 1 to n ---
def sum_recursive(n):
    if n <= 0: return 0
    return n + sum_recursive(n - 1)

def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(f"\nSum comparison:")
print(f"  Recursive: {sum_recursive(100)}")
print(f"  Iterative: {sum_iterative(100)}")

# --- Example 3: Fibonacci ---
def fib_recursive(n):
    if n <= 1: return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(f"\nFibonacci(20):")
# Recursive is very slow for large n!
print(f"  Iterative: {fib_iterative(20)}")
print(f"  Recursive: {fib_recursive(20)}")

# =============================
# 2. PERFORMANCE COMPARISON
# =============================

import time

# --- Example 4: Speed test —  Fibonacci ---
def time_it(func, *args):
    start = time.time()
    result = func(*args)
    elapsed = time.time() - start
    return result, elapsed

print(f"\nPerformance: fibonacci(30)")
result_iter, time_iter = time_it(fib_iterative, 30)
result_rec, time_rec = time_it(fib_recursive, 30)
print(f"  Iterative: {result_iter} in {time_iter:.6f}s")
print(f"  Recursive: {result_rec} in {time_rec:.6f}s")
print(f"  Recursive is ~{time_rec / max(time_iter, 0.000001):.0f}x slower!")

# =============================
# 3. WHEN RECURSION IS BETTER
# =============================

# --- Example 5: Tree traversal — recursion is natural ---
# Nested data is naturally recursive
def flatten(items):
    """Recursion is the cleanest way to flatten nested lists."""
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))   # Recursive — clean!
        else:
            result.append(item)
    return result

nested = [1, [2, [3, 4]], [5, [6, [7]]]]
print(f"\nFlatten (recursion wins):")
print(f"  {nested} → {flatten(nested)}")

# --- Example 6: Subsets — recursion is natural ---
def subsets(items, index=0, current=None):
    if current is None: current = []
    if index == len(items):
        return [current[:]]
    # Include and exclude
    result = subsets(items, index + 1, current + [items[index]])
    result += subsets(items, index + 1, current)
    return result

print(f"\nSubsets (recursion wins):")
print(f"  {subsets([1, 2, 3])}")

# =============================
# 4. WHEN LOOPS ARE BETTER
# =============================

# --- Example 7: Simple counting — loop is cleaner ---
# Recursive (over-engineering)
def count_items_recursive(items):
    if len(items) == 0: return 0
    return 1 + count_items_recursive(items[1:])

# Iterative (simple and clear)
def count_items_iterative(items):
    count = 0
    for _ in items:
        count += 1
    return count

data = [1, 2, 3, 4, 5]
print(f"\nCounting (loop wins):")
print(f"  Recursive: {count_items_recursive(data)}")
print(f"  Iterative: {count_items_iterative(data)}")
print(f"  Best: just use len()! → {len(data)}")

# =============================
# 5. CONVERTING RECURSION TO ITERATION
# =============================

# --- Example 8: Manual stack for conversion ---
def reverse_recursive(s):
    if len(s) <= 1: return s
    return reverse_recursive(s[1:]) + s[0]

def reverse_iterative(s):
    """Convert recursive approach to iterative using a stack."""
    stack = list(s)   # Push all characters
    result = ""
    while stack:
        result += stack.pop()   # Pop in reverse order
    return result

print(f"\nReverse conversion:")
print(f"  Recursive: {reverse_recursive('hello')}")
print(f"  Iterative: {reverse_iterative('hello')}")

# --- Example 9: Power — recursive to iterative ---
def power_recursive(base, exp):
    if exp == 0: return 1
    return base * power_recursive(base, exp - 1)

def power_iterative(base, exp):
    result = 1
    for _ in range(exp):
        result = result * base
    return result

print(f"\nPower conversion:")
print(f"  Recursive: 2^10 = {power_recursive(2, 10)}")
print(f"  Iterative: 2^10 = {power_iterative(2, 10)}")

# =============================
# 6. DECISION GUIDE
# =============================

print(f"""
╔═══════════════════════════════════════════════╗
║      RECURSION vs ITERATION GUIDE             ║
╠═══════════════════════════════════════════════╣
║ Use RECURSION when:                           ║
║   • Problem is naturally tree-like            ║
║   • Backtracking is needed                    ║
║   • Code is cleaner recursive                 ║
║   • Depth is bounded                          ║
╠═══════════════════════════════════════════════╣
║ Use ITERATION when:                           ║
║   • Simple linear processing                  ║
║   • Performance is critical                   ║
║   • Deep recursion possible (>1000)           ║
║   • Loop version is equally clear             ║
╚═══════════════════════════════════════════════╝
""")

# ============================================
# TRY IT YOURSELF:
# 1. Convert a recursive string reverse to iterative
# 2. Write both recursive and iterative GCD
# 3. Time your own recursive vs iterative functions
# ============================================
