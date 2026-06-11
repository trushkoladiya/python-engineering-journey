# ============================================
# MODULE 11 - SUBTOPIC 1: Understanding Errors
# ============================================

# =============================
# 1. SYNTAX ERRORS
# =============================

# Syntax errors happen BEFORE the program runs.
# Python reads your code and finds grammar mistakes.

# --- Example 1: Demonstrating a syntax error message ---
# The following would cause a SyntaxError if uncommented:
# if True
#     print("missing colon")

# We can show what the error looks like using a string:
print("Example of a SyntaxError message:")
print("  SyntaxError: expected ':'")
print("  This happens when you forget a colon after if/for/def/etc.")
print()

# =============================
# 2. RUNTIME ERRORS (EXCEPTIONS)
# =============================

# Runtime errors happen DURING execution.
# The code is valid Python, but something goes wrong.

# --- Example 2: Common runtime errors (shown safely) ---
print("Common runtime errors:")
print()

# ZeroDivisionError
print("  ZeroDivisionError:")
print("    Caused by: 10 / 0")
print("    Happens when you divide by zero")
print()

# ValueError
print("  ValueError:")
print("    Caused by: int('hello')")
print("    Happens when a value has the wrong type for an operation")
print()

# TypeError
print("  TypeError:")
print("    Caused by: 'hello' + 5")
print("    Happens when you mix incompatible types")
print()

# IndexError
print("  IndexError:")
print("    Caused by: [1, 2, 3][10]")
print("    Happens when you access an index that doesn't exist")
print()

# KeyError
print("  KeyError:")
print("    Caused by: {'a': 1}['z']")
print("    Happens when you access a dict key that doesn't exist")
print()

# =============================
# 3. SEEING REAL ERRORS
# =============================

# --- Example 3: Triggering and observing a real error ---
# Let's intentionally trigger an error to see the message.
# We use try/except here just to catch it — you'll learn this fully in subtopic 3.

print("--- Live error demonstration ---")
print()

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught ZeroDivisionError: {e}")

# ValueError
try:
    number = int("hello")
except ValueError as e:
    print(f"Caught ValueError: {e}")

# IndexError
try:
    items = [10, 20, 30]
    value = items[100]
except IndexError as e:
    print(f"Caught IndexError: {e}")

# KeyError
try:
    data = {"name": "Trush", "age": 21}
    value = data["salary"]
except KeyError as e:
    print(f"Caught KeyError: {e}")

print()

# =============================
# 4. LOGICAL ERRORS
# =============================

# Logical errors are the trickiest — no crash, just wrong results.

# --- Example 4: A logical error ---
print("--- Logical error example ---")
print()

a = 10
b = 20

# Bug: operator precedence — division happens before addition
wrong_average = a + b / 2
print(f"Wrong average of {a} and {b}: {wrong_average}")   # 20.0

# Fix: use parentheses
correct_average = (a + b) / 2
print(f"Correct average of {a} and {b}: {correct_average}")  # 15.0
print()

# --- Example 5: Another logical error ---
# Off-by-one error in a loop
print("--- Off-by-one logical error ---")
numbers = [10, 20, 30, 40, 50]

# Bug: range stops one short
print("Wrong (skips last element):")
for i in range(len(numbers) - 1):   # Goes 0 to 3, misses index 4
    print(f"  {numbers[i]}", end="")
print()

# Fix
print("Correct (all elements):")
for i in range(len(numbers)):        # Goes 0 to 4
    print(f"  {numbers[i]}", end="")
print()
print()

# =============================
# 5. IDENTIFYING ERROR TYPES
# =============================

# --- Example 6: Quick reference ---
print("--- Error Type Quick Reference ---")
print()

error_types = [
    ("Syntax Error",  "Code has bad grammar",      "if True  (no colon)"),
    ("Runtime Error", "Crashes during execution",   "10 / 0"),
    ("Logical Error", "Runs but gives wrong result", "a + b / 2 vs (a+b) / 2"),
]

print(f"{'Type':<16} {'Description':<30} {'Example'}")
print("-" * 70)
for error_type, desc, example in error_types:
    print(f"{error_type:<16} {desc:<30} {example}")

# ============================================
# TRY IT YOURSELF:
# 1. Think of a logical error you might make
# 2. Try uncommenting a syntax error to see it
# 3. Run this file and read each error message
# ============================================
