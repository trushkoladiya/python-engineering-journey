# ============================================
# MODULE 9 - SUBTOPIC 9: Optimization Techniques
# ============================================

# =============================
# 1. THE PROBLEM — REPEATED WORK
# =============================

# --- Example 1: Counting calls in naive Fibonacci ---
def fib_naive(n, counter):
    counter[0] += 1
    if n <= 1: return n
    return fib_naive(n - 1, counter) + fib_naive(n - 2, counter)

print("Naive Fibonacci — call counts:")
for i in [5, 10, 15, 20, 25]:
    count = [0]
    result = fib_naive(i, count)
    print(f"  fib({i:2d}) = {result:>8d}  |  {count[0]:>10,} calls")

# --- Example 2: Visualizing repeated work ---
def fib_trace(n, depth=0):
    print(f"{'  ' * depth}fib({n})")
    if n <= 1: return n
    return fib_trace(n - 1, depth + 1) + fib_trace(n - 2, depth + 1)

print(f"\nRepeated calls for fib(5):")
fib_trace(5)

# =============================
# 2. MEMOIZATION — MANUAL APPROACH
# =============================

# --- Example 3: Fibonacci with manual memoization ---
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print(f"\nMemoized Fibonacci:")
for i in [10, 20, 50, 100]:
    print(f"  fib({i}) = {fib_memo(i)}")

# --- Example 4: Counting calls WITH memoization ---
def fib_memo_counted(n, memo=None, counter=None):
    if memo is None: memo = {}
    if counter is None: counter = [0]
    counter[0] += 1
    if n in memo: return memo[n], counter[0]
    if n <= 1: return n, counter[0]
    r1, _ = fib_memo_counted(n - 1, memo, counter)
    r2, _ = fib_memo_counted(n - 2, memo, counter)
    memo[n] = r1 + r2
    return memo[n], counter[0]

print(f"\nMemoized Fibonacci — call counts:")
for i in [5, 10, 15, 20, 25]:
    result, calls = fib_memo_counted(i)
    print(f"  fib({i:2d}) = {result:>8d}  |  {calls:>6} calls")

# =============================
# 3. SPEED COMPARISON
# =============================

import time

# --- Example 5: Timing comparison ---
def fib_slow(n):
    if n <= 1: return n
    return fib_slow(n - 1) + fib_slow(n - 2)

def fib_fast(n, memo=None):
    if memo is None: memo = {}
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib_fast(n - 1, memo) + fib_fast(n - 2, memo)
    return memo[n]

print(f"\nSpeed comparison — fib(30):")
start = time.time()
r1 = fib_slow(30)
t1 = time.time() - start

start = time.time()
r2 = fib_fast(30)
t2 = time.time() - start

print(f"  Naive:    {r1} in {t1:.4f}s")
print(f"  Memoized: {r2} in {t2:.6f}s")
print(f"  Speedup:  ~{t1 / max(t2, 0.000001):.0f}x faster!")

# =============================
# 4. USING functools.lru_cache
# =============================

from functools import lru_cache

# --- Example 6: Automatic memoization ---
@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1: return n
    return fib_cached(n - 1) + fib_cached(n - 2)

print(f"\nUsing @lru_cache:")
for i in [50, 100, 200]:
    print(f"  fib({i}) = {fib_cached(i)}")

# Show cache stats
print(f"\nCache info: {fib_cached.cache_info()}")

# =============================
# 5. MEMOIZATION ON OTHER PROBLEMS
# =============================

# --- Example 7: Staircase problem ---
# How many ways to climb n stairs taking 1 or 2 steps at a time?
@lru_cache(maxsize=None)
def climb_stairs(n):
    if n <= 1: return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)

print(f"\nStaircase problem:")
for i in range(1, 11):
    print(f"  {i} stairs: {climb_stairs(i)} ways")

# --- Example 8: Coin change — minimum coins ---
@lru_cache(maxsize=None)
def min_coins(amount, coins=(1, 5, 10, 25)):
    if amount == 0: return 0
    if amount < 0: return float('inf')
    
    best = float('inf')
    for coin in coins:
        result = min_coins(amount - coin, coins)
        if result + 1 < best:
            best = result + 1
    return best

print(f"\nMinimum coins:")
for amount in [11, 30, 47, 63]:
    print(f"  ${amount}: {min_coins(amount)} coins")

# =============================
# 6. BUILD YOUR OWN MEMOIZE DECORATOR
# =============================

# --- Example 9: Generic memoization ---
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def power(base, exp):
    if exp == 0: return 1
    return base * power(base, exp - 1)

print(f"\nMemoized power:")
print(f"  2^20 = {power(2, 20)}")
print(f"  3^10 = {power(3, 10)}")

# ============================================
# TRY IT YOURSELF:
# 1. Add memoization to the staircase problem with 1, 2, or 3 steps
# 2. Time naive vs memoized for fib(35)
# 3. Write a memoized function for unique paths in a grid
# ============================================
