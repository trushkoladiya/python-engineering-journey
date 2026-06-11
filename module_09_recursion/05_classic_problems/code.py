# ============================================
# MODULE 9 - SUBTOPIC 5: Classic Problems
# ============================================

# =============================
# 1. FACTORIAL
# =============================

def factorial(n):
    """n! = n × (n-1) × ... × 1"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorials:")
for i in range(8):
    print(f"  {i}! = {factorial(i)}")

# =============================
# 2. FIBONACCI
# =============================

def fibonacci(n):
    """F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)"""
    if n <= 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci sequence:")
fib_nums = [fibonacci(i) for i in range(12)]
print(f"  {fib_nums}")

# =============================
# 3. SUM OF NUMBERS
# =============================

def sum_to(n):
    """Sum of 1 + 2 + ... + n"""
    if n <= 0: return 0
    return n + sum_to(n - 1)

print(f"\nSum 1 to 10: {sum_to(10)}")    # 55
print(f"Sum 1 to 100: {sum_to(100)}")    # 5050

# =============================
# 4. POWER CALCULATION
# =============================

# --- Linear version ---
def power(base, exp):
    """base^exp using linear recursion."""
    if exp == 0: return 1
    if exp < 0: return 1 / power(base, -exp)
    return base * power(base, exp - 1)

print(f"\nPower (linear):")
print(f"  2^10 = {power(2, 10)}")
print(f"  3^5 = {power(3, 5)}")
print(f"  5^0 = {power(5, 0)}")
print(f"  2^-3 = {power(2, -3)}")

# --- Fast version (divide and conquer) ---
def fast_power(base, exp):
    """base^exp using O(log n) recursion."""
    if exp == 0: return 1
    if exp < 0: return 1 / fast_power(base, -exp)
    if exp % 2 == 0:
        half = fast_power(base, exp // 2)
        return half * half
    return base * fast_power(base, exp - 1)

print(f"\nPower (fast):")
print(f"  2^10 = {fast_power(2, 10)}")
print(f"  2^20 = {fast_power(2, 20)}")

# =============================
# 5. GCD (Greatest Common Divisor)
# =============================

def gcd(a, b):
    """Euclidean algorithm."""
    if b == 0: return a
    return gcd(b, a % b)

print(f"\nGCD:")
print(f"  gcd(48, 18) = {gcd(48, 18)}")    # 6
print(f"  gcd(100, 75) = {gcd(100, 75)}")  # 25
print(f"  gcd(17, 5) = {gcd(17, 5)}")      # 1

# =============================
# 6. BINARY SEARCH (RECURSIVE)
# =============================

def binary_search(arr, target, low=0, high=None):
    """Find target in sorted list."""
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1   # Not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(f"\nBinary search in {sorted_list}:")
print(f"  Find 23: index {binary_search(sorted_list, 23)}")
print(f"  Find 72: index {binary_search(sorted_list, 72)}")
print(f"  Find 50: index {binary_search(sorted_list, 50)}")

# =============================
# 7. NUMBER BASE CONVERSION
# =============================

def to_binary(n):
    """Convert positive integer to binary string."""
    if n == 0: return "0"
    if n == 1: return "1"
    return to_binary(n // 2) + str(n % 2)

print(f"\nBinary conversion:")
for num in [5, 10, 42, 255]:
    print(f"  {num} → {to_binary(num)}")

# ============================================
# TRY IT YOURSELF:
# 1. Write a recursive function for n-th triangular number
# 2. Write recursive LCM using GCD
# 3. Implement recursive binary search on a list of names
# ============================================
