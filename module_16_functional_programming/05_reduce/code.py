# ============================================
# MODULE 16 - SUBTOPIC 5: reduce()
# ============================================

# reduce() takes an iterable and combines all elements
# into a single value using a function.

from functools import reduce

# =============================
# 1. BASIC reduce()
# =============================

print("=== Basic reduce() ===")
print()

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda a, b: a + b, numbers)
print(f"  numbers: {numbers}")
print(f"  sum (reduce): {total}")
print(f"  sum (built-in): {sum(numbers)}")
print()

# =============================
# 2. HOW reduce() WORKS STEP BY STEP
# =============================

print("=== Step-by-Step Trace ===")
print()

def add_with_trace(a, b):
    """Add with tracing to see how reduce works."""
    result = a + b
    print(f"    a={a}, b={b} → {result}")
    return result

print("  reduce(add, [1, 2, 3, 4, 5]):")
result = reduce(add_with_trace, [1, 2, 3, 4, 5])
print(f"  Final result: {result}")
print()

# =============================
# 3. PRODUCT OF NUMBERS
# =============================

print("=== Product of Numbers ===")
print()

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)
print(f"  numbers: {numbers}")
print(f"  product: {product}")   # 120
print()

# Factorial using reduce
import math
n = 6
factorial = reduce(lambda a, b: a * b, range(1, n + 1))
print(f"  {n}! = {factorial}")
print(f"  math.factorial({n}) = {math.factorial(n)}")
print()

# =============================
# 4. WITH INITIAL VALUE
# =============================

print("=== reduce() with Initial Value ===")
print()

numbers = [1, 2, 3, 4, 5]

# Without initial value: starts with first element
total1 = reduce(lambda a, b: a + b, numbers)
print(f"  Without initial: {total1}")

# With initial value of 100
total2 = reduce(lambda a, b: a + b, numbers, 100)
print(f"  With initial 100: {total2}")
print()

# Initial value is important for empty iterables
empty_sum = reduce(lambda a, b: a + b, [], 0)
print(f"  Empty list with initial 0: {empty_sum}")
print()

# =============================
# 5. FINDING MAX AND MIN
# =============================

print("=== Max and Min with reduce() ===")
print()

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

maximum = reduce(lambda a, b: a if a > b else b, data)
minimum = reduce(lambda a, b: a if a < b else b, data)

print(f"  data: {data}")
print(f"  max (reduce): {maximum}")
print(f"  min (reduce): {minimum}")
print(f"  max (built-in): {max(data)}")
print(f"  min (built-in): {min(data)}")
print()

# =============================
# 6. STRING CONCATENATION
# =============================

print("=== String Operations ===")
print()

words = ["Python", "is", "awesome"]

# Join words with spaces
sentence = reduce(lambda a, b: a + " " + b, words)
print(f"  words: {words}")
print(f"  sentence: '{sentence}'")
print()

# Same with str.join (usually better)
sentence2 = " ".join(words)
print(f"  str.join: '{sentence2}'")
print()

# =============================
# 7. FLATTENING NESTED LISTS
# =============================

print("=== Flattening Nested Lists ===")
print()

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = reduce(lambda a, b: a + b, nested)
print(f"  nested: {nested}")
print(f"  flat:   {flat}")
print()

# With initial empty list
nested2 = [[10, 20], [30], [40, 50, 60]]
flat2 = reduce(lambda a, b: a + b, nested2, [])
print(f"  nested: {nested2}")
print(f"  flat:   {flat2}")
print()

# =============================
# 8. BUILDING DICTIONARIES
# =============================

print("=== Building Data with reduce() ===")
print()

# Count character frequencies
text = "hello world"

def count_chars(acc, char):
    """Accumulate character counts in a dictionary."""
    if char != " ":
        acc[char] = acc.get(char, 0) + 1
    return acc

freq = reduce(count_chars, text, {})
print(f"  text: '{text}'")
print(f"  frequency: {freq}")
print()

# =============================
# 9. reduce() WITH NAMED FUNCTIONS
# =============================

print("=== reduce() with Named Functions ===")
print()

def merge_dicts(a, b):
    """Merge two dictionaries into one."""
    result = {**a, **b}
    return result

dicts = [
    {"name": "Trush"},
    {"age": 21},
    {"city": "NYC"},
    {"role": "Engineer"},
]

merged = reduce(merge_dicts, dicts)
print(f"  Separate dicts: {dicts}")
print(f"  Merged: {merged}")
print()

# =============================
# 10. PRACTICAL: PIPELINE WITH reduce()
# =============================

print("=== Pipeline with reduce() ===")
print()

# Apply a series of transformations to a value
def apply_func(value, func):
    return func(value)

transformations = [
    lambda x: x * 2,        # double
    lambda x: x + 10,       # add 10
    lambda x: x ** 2,       # square
    lambda x: x - 100,      # subtract 100
]

start = 5
result = reduce(apply_func, transformations, start)

# Trace it manually:
print(f"  Start: {start}")
print(f"  × 2  → {start * 2}")
print(f"  + 10 → {start * 2 + 10}")
print(f"  ** 2 → {(start * 2 + 10) ** 2}")
print(f"  - 100→ {(start * 2 + 10) ** 2 - 100}")
print(f"  reduce result: {result}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use reduce to find the longest string in a list
# 2. Use reduce to compute the GCD of a list of numbers
# 3. Use reduce to build a sentence from a list of words
#    with proper capitalization
# ============================================
