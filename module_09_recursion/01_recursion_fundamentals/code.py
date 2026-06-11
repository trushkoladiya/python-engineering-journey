# ============================================
# MODULE 9 - SUBTOPIC 1: Recursion Fundamentals
# ============================================
# Building on Module 8's intro — now we go deeper.

# =============================
# 1. THE RECURSIVE THINKING PATTERN
# =============================

# --- Example 1: Sum from 1 to n ---
# Think: sum(5) = 5 + sum(4) = 5 + 4 + sum(3) = ...
def sum_to(n):
    if n <= 0:       # Base case
        return 0
    return n + sum_to(n - 1)   # n + answer for smaller problem

print("sum_to(5):", sum_to(5))     # 15
print("sum_to(10):", sum_to(10))   # 55

# --- Example 2: Count digits in a number ---
# Think: digits(12345) = 1 + digits(1234)
def count_digits(n):
    n = abs(n)   # Handle negative
    if n < 10:   # Base case: single digit
        return 1
    return 1 + count_digits(n // 10)

print(f"\nDigits in 12345: {count_digits(12345)}")   # 5
print(f"Digits in 7: {count_digits(7)}")             # 1
print(f"Digits in 100: {count_digits(100)}")         # 3

# =============================
# 2. BASE CASE — THE FOUNDATION
# =============================

# --- Example 3: What makes a good base case ---
def power(base, exp):
    # Base case: anything to the power of 0 is 1
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(f"\n2^5 = {power(2, 5)}")    # 32
print(f"3^4 = {power(3, 4)}")      # 81
print(f"10^0 = {power(10, 0)}")    # 1

# --- Example 4: Multiple base cases ---
def fibonacci(n):
    if n == 0: return 0    # Base case 1
    if n == 1: return 1    # Base case 2
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci sequence:")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}")

# =============================
# 3. RECURSIVE CASE — BREAKING DOWN
# =============================

# --- Example 5: String length without len() ---
def string_length(s):
    if s == "":        # Base case: empty string has length 0
        return 0
    return 1 + string_length(s[1:])   # 1 + length of remaining

print(f"\nLength of 'hello': {string_length('hello')}")
print(f"Length of '': {string_length('')}")
print(f"Length of 'Python': {string_length('Python')}")

# --- Example 6: Multiply using addition only ---
def multiply(a, b):
    if b == 0:          # Base case
        return 0
    if b < 0:           # Handle negative
        return -multiply(a, -b)
    return a + multiply(a, b - 1)   # a * b = a + a*(b-1)

print(f"\n3 * 4 = {multiply(3, 4)}")
print(f"5 * 0 = {multiply(5, 0)}")
print(f"7 * 3 = {multiply(7, 3)}")

# =============================
# 4. THE KEY QUESTION
# =============================

# The secret to writing recursive functions:
# "If I already had the answer for a SMALLER input,
#  how would I use it to build the FULL answer?"

# --- Example 7: Sum of digits ---
# If I know sum_digits(1234) = 10, then sum_digits(12345) = 5 + 10
def sum_digits(n):
    n = abs(n)
    if n < 10:         # Single digit — return it
        return n
    return (n % 10) + sum_digits(n // 10)   # Last digit + sum of rest

print(f"\nSum of digits of 12345: {sum_digits(12345)}")   # 15
print(f"Sum of digits of 999: {sum_digits(999)}")         # 27
print(f"Sum of digits of 7: {sum_digits(7)}")             # 7

# --- Example 8: Check if a number exists in a list ---
def contains(items, target):
    if len(items) == 0:         # Base case: empty list
        return False
    if items[0] == target:      # Found it!
        return True
    return contains(items[1:], target)   # Check the rest

data = [3, 7, 1, 9, 4]
print(f"\n{data} contains 9: {contains(data, 9)}")
print(f"{data} contains 5: {contains(data, 5)}")

# ============================================
# TRY IT YOURSELF:
# 1. Write a recursive function to find the product of 1 to n
# 2. Write a recursive function to count occurrences of a char in a string
# 3. Write a recursive function to check if a number is even
#    (subtract 2 until you reach 0 or 1)
# ============================================
