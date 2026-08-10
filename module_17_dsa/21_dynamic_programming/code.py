# ============================================
# MODULE 17 - SUBTOPIC 21: Dynamic Programming (Intro)
# ============================================

# Dynamic Programming: solve complex problems by caching
# solutions to overlapping subproblems.

import time

# =============================
# 1. THE PROBLEM: FIBONACCI WITHOUT DP
# =============================

print("=== Fibonacci — Without DP (Slow) ===")
print()

def fib_naive(n):
    """Naive recursive Fibonacci. O(2^n) — exponential!"""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# Small values are fine
for n in [5, 10, 15]:
    start = time.time()
    result = fib_naive(n)
    elapsed = time.time() - start
    print(f"  fib({n}) = {result} ({elapsed:.6f}s)")

# n=35 is already slow!
start = time.time()
result = fib_naive(30)
elapsed = time.time() - start
print(f"  fib(30) = {result} ({elapsed:.4f}s)")
print("  → Gets exponentially slower!")
print()

# =============================
# 2. MEMOIZATION (TOP-DOWN)
# =============================

print("=== Fibonacci — Memoization (Top-Down) ===")
print()

def fib_memo(n, memo=None):
    """Fibonacci with memoization. O(n)."""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

for n in [10, 30, 50, 100]:
    start = time.time()
    result = fib_memo(n)
    elapsed = time.time() - start
    print(f"  fib({n}) = {result} ({elapsed:.8f}s)")
print("  → Instant, even for n=100!")
print()

# =============================
# 3. TABULATION (BOTTOM-UP)
# =============================

print("=== Fibonacci — Tabulation (Bottom-Up) ===")
print()

def fib_tab(n):
    """Fibonacci with tabulation. O(n) time, O(n) space."""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

for n in [10, 30, 50, 100]:
    print(f"  fib({n}) = {fib_tab(n)}")
print()

# Space-optimized version
def fib_optimized(n):
    """Fibonacci with O(1) space."""
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

print("  Space-optimized:")
for n in [10, 50, 100]:
    print(f"  fib({n}) = {fib_optimized(n)}")
print()

# =============================
# 4. CLIMBING STAIRS
# =============================

print("=== Climbing Stairs Problem ===")
print()

def climb_stairs(n):
    """
    How many ways to climb n stairs, taking 1 or 2 steps at a time?
    This IS the Fibonacci sequence!
    """
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

for n in range(1, 8):
    print(f"  {n} stairs: {climb_stairs(n)} ways")
print()

# =============================
# 5. COIN CHANGE
# =============================

print("=== Coin Change Problem ===")
print()

def min_coins(coins, amount):
    """
    Find minimum number of coins to make the amount.
    dp[i] = minimum coins needed for amount i.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0    # 0 coins needed for amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 5, 10, 25]
for amount in [11, 15, 30, 47]:
    result = min_coins(coins, amount)
    print(f"  Amount {amount} with coins {coins}: {result} coins")
print()

# =============================
# 6. LONGEST COMMON SUBSEQUENCE
# =============================

print("=== Longest Common Subsequence (LCS) ===")
print()

def lcs(s1, s2):
    """Find length of longest common subsequence."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

pairs = [
    ("ABCBDAB", "BDCAB"),
    ("AGGTAB", "GXTXAYB"),
    ("hello", "halo"),
]

for s1, s2 in pairs:
    result = lcs(s1, s2)
    print(f"  LCS('{s1}', '{s2}') = {result}")
print()

# =============================
# 7. 0/1 KNAPSACK (INTRO)
# =============================

print("=== 0/1 Knapsack Problem ===")
print()

def knapsack(weights, values, capacity):
    """
    Maximize value within weight capacity.
    Each item can be included or excluded.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i - 1][w]

            # Take item i (if it fits)
            if weights[i - 1] <= w:
                take = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], take)

    return dp[n][capacity]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

result = knapsack(weights, values, capacity)
print(f"  Items: weight={weights}, value={values}")
print(f"  Capacity: {capacity}")
print(f"  Max value: {result}")
print()

# =============================
# 8. DP THINKING PATTERN
# =============================

print("=== DP Thinking Pattern ===")
print()

print("  Steps to solve a DP problem:")
print("  1. Identify the subproblem (what changes?)")
print("  2. Write the recurrence relation")
print("  3. Identify base cases")
print("  4. Decide: top-down (memo) or bottom-up (table)")
print("  5. Optimize space if possible")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Solve the "house robber" problem: maximize sum
#    from a list without picking two adjacent numbers
# 2. Find minimum number of operations to convert
#    one string to another (edit distance)
# 3. Count the number of unique paths in a grid
#    from top-left to bottom-right
# ============================================
