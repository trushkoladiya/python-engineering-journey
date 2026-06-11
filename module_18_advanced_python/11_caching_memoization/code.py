# ============================================
# MODULE 18 - SUBTOPIC 11: Caching & Memoization
# ============================================

# Store results of expensive operations to avoid recomputing them.

from functools import lru_cache, cache
import time

# =============================
# 1. THE PROBLEM: REPEATED EXPENSIVE WORK
# =============================

print("=== The Problem: Repeated Work ===")
print()

call_count = 0

def expensive_square(n):
    global call_count
    call_count += 1
    time.sleep(0.1)  # Simulate expensive computation
    return n * n

# Without caching — every call recomputes
call_count = 0
start = time.time()
for _ in range(5):
    expensive_square(42)  # Same argument, recomputed 5 times!
elapsed = time.time() - start

print(f"  Without cache: {call_count} function calls, {elapsed:.2f}s")
print()

# =============================
# 2. MANUAL CACHING
# =============================

print("=== Manual Caching ===")
print()

manual_cache = {}
manual_calls = 0

def cached_square(n):
    global manual_calls
    if n in manual_cache:
        return manual_cache[n]
    manual_calls += 1
    time.sleep(0.1)
    result = n * n
    manual_cache[n] = result
    return result

manual_calls = 0
start = time.time()
for _ in range(5):
    cached_square(42)  # Only computed ONCE
elapsed = time.time() - start

print(f"  With cache: {manual_calls} computation(s), {elapsed:.2f}s")
print(f"  Cache contents: {manual_cache}")
print()

# =============================
# 3. @lru_cache — BUILT-IN MEMOIZATION
# =============================

print("=== @lru_cache ===")
print()

@lru_cache(maxsize=128)
def fibonacci(n):
    """Compute the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Without caching, fibonacci(35) would take seconds
# With caching, it's instant!

start = time.time()
result = fibonacci(100)
elapsed = time.time() - start

print(f"  fibonacci(100) = {result}")
print(f"  Time: {elapsed:.6f}s")
print(f"  Cache info: {fibonacci.cache_info()}")
print()

# =============================
# 4. CACHE INFO AND MANAGEMENT
# =============================

print("=== Cache Info ===")
print()

@lru_cache(maxsize=32)
def compute(x, y):
    return x ** y

# Make some calls
results = [compute(2, i) for i in range(10)]
results += [compute(2, i) for i in range(10)]  # These hit cache

info = compute.cache_info()
print(f"  Hits: {info.hits}")       # Times result was found in cache
print(f"  Misses: {info.misses}")   # Times result was computed
print(f"  Max size: {info.maxsize}")
print(f"  Current size: {info.currsize}")
print()

# Clear the cache
compute.cache_clear()
print(f"  After clear: {compute.cache_info()}")
print()

# =============================
# 5. @cache (PYTHON 3.9+) — UNLIMITED CACHE
# =============================

print("=== @cache (Unlimited) ===")
print()

@cache
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"  factorial(10) = {factorial(10)}")
print(f"  factorial(20) = {factorial(20)}")
print(f"  Cache info: {factorial.cache_info()}")
print()

# @cache is shorthand for @lru_cache(maxsize=None)
# It caches everything — use when you know inputs are bounded

factorial.cache_clear()

# =============================
# 6. FIBONACCI: CACHED vs UNCACHED
# =============================

print("=== Fibonacci: Cached vs Uncached ===")
print()

def fib_slow(n):
    """Uncached fibonacci — exponentially slow."""
    if n < 2:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

@lru_cache(maxsize=None)
def fib_fast(n):
    """Cached fibonacci — linear time."""
    if n < 2:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)

# Uncached — slow even for n=30
start = time.time()
result_slow = fib_slow(30)
slow_time = time.time() - start
print(f"  fib_slow(30) = {result_slow} in {slow_time:.4f}s")

# Cached — instant even for n=500
fib_fast.cache_clear()
start = time.time()
result_fast = fib_fast(300)
fast_time = time.time() - start
print(f"  fib_fast(300) = {result_fast}")
print(f"  Time: {fast_time:.6f}s")
print()

fib_fast.cache_clear()

# =============================
# 7. CACHING WITH A TTL (TIME-TO-LIVE)
# =============================

print("=== Manual Cache with TTL ===")
print()

class TTLCache:
    """A simple cache with time-to-live expiration."""

    def __init__(self, ttl_seconds):
        self._cache = {}
        self._ttl = ttl_seconds

    def get(self, key):
        if key in self._cache:
            value, timestamp = self._cache[key]
            if time.time() - timestamp < self._ttl:
                return value
            else:
                del self._cache[key]  # Expired
        return None

    def set(self, key, value):
        self._cache[key] = (value, time.time())

    def __repr__(self):
        return f"TTLCache(ttl={self._ttl}, size={len(self._cache)})"

# Usage
ttl_cache = TTLCache(ttl_seconds=1)
ttl_cache.set("user_123", {"name": "Trush", "score": 95})

print(f"  Immediate get: {ttl_cache.get('user_123')}")
time.sleep(0.5)
print(f"  After 0.5s: {ttl_cache.get('user_123')}")
time.sleep(0.6)
print(f"  After 1.1s (expired): {ttl_cache.get('user_123')}")
print()

# =============================
# 8. CACHING DECORATOR (CUSTOM)
# =============================

print("=== Custom Caching Decorator ===")
print()

def memoize(func):
    """A custom memoization decorator."""
    memo = {}

    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]

    wrapper.cache = memo
    wrapper.cache_clear = lambda: memo.clear()
    return wrapper

@memoize
def power(base, exp):
    print(f"    Computing {base}^{exp}")
    return base ** exp

print(f"  power(2, 10) = {power(2, 10)}")  # Computes
print(f"  power(2, 10) = {power(2, 10)}")  # From cache
print(f"  power(3, 5) = {power(3, 5)}")    # Computes
print(f"  Cache: {power.cache}")
print()

# =============================
# 9. PRACTICAL: CACHING API RESPONSES
# =============================

print("=== Practical: Caching API Responses ===")
print()

class APIClient:
    """Simulated API client with caching."""

    def __init__(self):
        self._cache = {}
        self._call_count = 0

    def get_user(self, user_id):
        if user_id in self._cache:
            print(f"    Cache hit for user {user_id}")
            return self._cache[user_id]

        # Simulate API call
        self._call_count += 1
        print(f"    API call for user {user_id}")
        time.sleep(0.1)
        user = {"id": user_id, "name": f"User_{user_id}", "active": True}
        self._cache[user_id] = user
        return user

client = APIClient()

# First calls — hit the API
for uid in [101, 102, 103, 101, 102, 101]:
    user = client.get_user(uid)

print(f"\n  Total API calls: {client._call_count}")
print(f"  Cache size: {len(client._cache)}")
print()

# =============================
# 10. WHEN NOT TO CACHE
# =============================

print("=== When NOT to Cache ===")
print()

warnings = [
    "Results change over time (live data, random values)",
    "Arguments are never repeated (unique inputs each time)",
    "Memory is limited (cache grows unbounded)",
    "Function has side effects (files, databases, network)",
    "Arguments are unhashable (lists, dicts as arguments)",
]

for i, warning in enumerate(warnings, 1):
    print(f"  {i}. Don't cache when: {warning}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Add @lru_cache to a recursive factorial function
#    and compare speed with/without caching
# 2. Build a TTLCache that also tracks hit/miss counts
# 3. Create a memoized function that computes
#    the number of ways to climb N stairs (1 or 2 at a time)
# ============================================
