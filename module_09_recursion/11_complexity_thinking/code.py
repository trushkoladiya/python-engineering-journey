# ============================================
# MODULE 9 - SUBTOPIC 11: Complexity Thinking (Intro)
# ============================================

import time

# =============================
# 1. LINEAR — O(n)
# =============================

# --- Example 1: Factorial — O(n) calls ---
def factorial(n, counter=None):
    if counter is not None: counter[0] += 1
    if n <= 1: return 1
    return n * factorial(n - 1, counter)

print("Linear recursion — O(n):")
for size in [10, 100, 500]:
    count = [0]
    factorial(size, count)
    print(f"  factorial({size:3d}): {count[0]:>4} calls")
print("  Pattern: calls ≈ n (grows linearly)")

# =============================
# 2. EXPONENTIAL — O(2^n)
# =============================

# --- Example 2: Fibonacci — O(2^n) calls ---
def fib_naive(n, counter=None):
    if counter is not None: counter[0] += 1
    if n <= 1: return n
    return fib_naive(n - 1, counter) + fib_naive(n - 2, counter)

print(f"\nExponential recursion — O(2^n):")
for size in [5, 10, 15, 20, 25]:
    count = [0]
    fib_naive(size, count)
    print(f"  fib({size:2d}): {count[0]:>10,} calls")
print("  Pattern: calls roughly double each time!")

# =============================
# 3. LOGARITHMIC — O(log n)
# =============================

# --- Example 3: Fast power — O(log n) calls ---
def fast_power(base, exp, counter=None):
    if counter is not None: counter[0] += 1
    if exp == 0: return 1
    if exp % 2 == 0:
        half = fast_power(base, exp // 2, counter)
        return half * half
    return base * fast_power(base, exp - 1, counter)

print(f"\nLogarithmic recursion — O(log n):")
for size in [10, 100, 1000]:
    count = [0]
    fast_power(2, size, count)
    print(f"  power(2, {size:4d}): {count[0]:>3} calls")
print("  Pattern: calls ≈ log₂(n) (grows very slowly)")

# =============================
# 4. COMPARISON TABLE
# =============================

# --- Example 4: Side-by-side comparison ---
print(f"\n{'='*50}")
print(f"{'n':>5} | {'O(n)':>8} | {'O(2^n)':>12} | {'O(log n)':>8}")
print(f"{'-'*50}")

for n in [5, 10, 15, 20]:
    linear = n
    exponential = 2 ** n
    logarithmic = 0
    temp = n
    while temp > 0:
        logarithmic += 1
        temp //= 2
    print(f"{n:>5} | {linear:>8} | {exponential:>12,} | {logarithmic:>8}")

# =============================
# 5. SPACE COMPLEXITY — STACK USAGE
# =============================

# --- Example 5: Measuring stack depth ---
def measure_depth(n, current_depth=1):
    if n <= 1:
        return current_depth
    return measure_depth(n - 1, current_depth + 1)

print(f"\nStack depth (space usage):")
for n in [5, 10, 50, 100]:
    depth = measure_depth(n)
    print(f"  factorial({n:3d}): {depth:>4} frames on stack")

# --- Example 6: Tail recursion saves stack (conceptually) ---
# In Python it doesn't actually save stack, but the concept matters
def sum_tail(n, acc=0):
    """O(n) stack in Python. In other languages: O(1) stack."""
    if n <= 0: return acc
    return sum_tail(n - 1, acc + n)

def sum_iterative(n):
    """O(1) space — no stack usage."""
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

print(f"\nSpace comparison:")
print(f"  Recursive sum(100): {sum_tail(100)} (uses 100 stack frames)")
print(f"  Iterative sum(100): {sum_iterative(100)} (uses 0 stack frames)")

# =============================
# 6. TIMING DIFFERENT COMPLEXITIES
# =============================

# --- Example 7: Empirical timing ---
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1: return n
    return fib_memo(n - 1) + fib_memo(n - 2)

print(f"\nTiming comparison:")

# O(n) — factorial
start = time.time()
factorial(500)
t_linear = time.time() - start
print(f"  O(n)     factorial(500):   {t_linear:.6f}s")

# O(log n) — fast power
start = time.time()
fast_power(2, 500)
t_log = time.time() - start
print(f"  O(log n) power(2, 500):    {t_log:.6f}s")

# O(2^n) — naive fib
start = time.time()
fib_naive(25)
t_exp = time.time() - start
print(f"  O(2^n)   fib_naive(25):    {t_exp:.4f}s")

# O(n) — memoized fib
fib_memo.cache_clear()
start = time.time()
fib_memo(500)
t_memo = time.time() - start
print(f"  O(n)     fib_memo(500):    {t_memo:.6f}s")

# ============================================
# TRY IT YOURSELF:
# 1. Count calls for different recursion types and compare
# 2. Time factorial for n=100, 500, 1000 and see if it grows linearly
# 3. Compare fib_naive(30) vs fib_memo(30) timing
# ============================================
