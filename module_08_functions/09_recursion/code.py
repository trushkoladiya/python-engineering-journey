# ============================================
# MODULE 8 - SUBTOPIC 9: Recursion (Introduction)
# ============================================

# =============================
# 1. BASIC RECURSION
# =============================

# --- Example 1: Countdown ---
def countdown(n):
    if n <= 0:           # Base case — stop here
        print("  Go!")
        return
    print(f"  {n}...")
    countdown(n - 1)    # Recursive call — closer to base case

print("Countdown:")
countdown(5)

# --- Example 2: Count up using recursion ---
def count_up(current, target):
    if current > target:   # Base case
        return
    print(f"  {current}")
    count_up(current + 1, target)   # Recursive call

print("\nCount up:")
count_up(1, 5)

# =============================
# 2. FACTORIAL
# =============================

# --- Example 3: Factorial function ---
def factorial(n):
    if n <= 1:           # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case

print(f"\nFactorials:")
print(f"  1! = {factorial(1)}")
print(f"  3! = {factorial(3)}")
print(f"  5! = {factorial(5)}")
print(f"  7! = {factorial(7)}")

# --- Example 4: Tracing factorial ---
def factorial_trace(n, depth=0):
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")
    
    if n <= 1:
        print(f"{indent}→ returns 1 (base case)")
        return 1
    
    result = n * factorial_trace(n - 1, depth + 1)
    print(f"{indent}→ returns {result}")
    return result

print(f"\nTracing factorial(4):")
answer = factorial_trace(4)
print(f"Answer: {answer}")

# =============================
# 3. SUM OF NUMBERS
# =============================

# --- Example 5: Sum using recursion ---
def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

print(f"\nSum 1 to 5: {recursive_sum(5)}")    # 15
print(f"Sum 1 to 10: {recursive_sum(10)}")    # 55

# --- Example 6: Sum of a list ---
def list_sum(items):
    if len(items) == 0:   # Base case — empty list
        return 0
    return items[0] + list_sum(items[1:])   # First + sum of rest

numbers = [3, 7, 2, 8, 5]
print(f"\nSum of {numbers}: {list_sum(numbers)}")

# =============================
# 4. FIBONACCI
# =============================

# --- Example 7: Fibonacci sequence ---
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci sequence:")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}")

# =============================
# 5. STRING RECURSION
# =============================

# --- Example 8: Reverse a string ---
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(f"\nReverse 'hello': {reverse_string('hello')}")
print(f"Reverse 'Python': {reverse_string('Python')}")

# --- Example 9: Check palindrome ---
def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(f"\n'racecar' palindrome? {is_palindrome('racecar')}")
print(f"'hello' palindrome? {is_palindrome('hello')}")
print(f"'madam' palindrome? {is_palindrome('madam')}")

# =============================
# 6. BASE CASE IS ESSENTIAL
# =============================

# --- Example 10: What happens without a base case ---
# DON'T RUN THIS — it would crash with RecursionError!
# def infinite():
#     return infinite()   # No base case — infinite recursion!

# --- Example 11: Python has a recursion limit ---
import sys
print(f"\nPython recursion limit: {sys.getrecursionlimit()}")

# =============================
# 7. RECURSION vs LOOPS
# =============================

# --- Example 12: Same problem, two approaches ---
# Loop version
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Recursive version
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print(f"\nLoop factorial(6): {factorial_loop(6)}")
print(f"Recursive factorial(6): {factorial_recursive(6)}")

# ============================================
# TRY IT YOURSELF:
# 1. Write a recursive function that sums digits of a number
# 2. Write a recursive countdown that prints even numbers only
# 3. Write a recursive function to find the length of a list
# ============================================
