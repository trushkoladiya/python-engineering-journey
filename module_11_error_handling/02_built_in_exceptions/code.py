# ============================================
# MODULE 11 - SUBTOPIC 2: Built-in Exceptions
# ============================================

# Python has many built-in exception types.
# Each one tells you exactly WHAT went wrong.

# =============================
# 1. ValueError
# =============================

# --- Example 1: Wrong value for a function ---
print("=== ValueError ===")

try:
    number = int("hello")
except ValueError as e:
    print(f"int('hello') → ValueError: {e}")

try:
    number = int("3.14")
except ValueError as e:
    print(f"int('3.14') → ValueError: {e}")

try:
    number = float("abc")
except ValueError as e:
    print(f"float('abc') → ValueError: {e}")

print()

# =============================
# 2. TypeError
# =============================

# --- Example 2: Wrong type for an operation ---
print("=== TypeError ===")

try:
    result = "hello" + 5
except TypeError as e:
    print(f"'hello' + 5 → TypeError: {e}")

try:
    result = len(42)
except TypeError as e:
    print(f"len(42) → TypeError: {e}")

try:
    result = "hello" * "world"
except TypeError as e:
    print(f"'hello' * 'world' → TypeError: {e}")

print()

# =============================
# 3. IndexError
# =============================

# --- Example 3: Invalid list/tuple index ---
print("=== IndexError ===")

items = [10, 20, 30]

try:
    value = items[10]
except IndexError as e:
    print(f"items[10] → IndexError: {e}")

try:
    value = items[-10]
except IndexError as e:
    print(f"items[-10] → IndexError: {e}")

# Tuples too
data = (1, 2, 3)
try:
    value = data[5]
except IndexError as e:
    print(f"tuple[5] → IndexError: {e}")

print()

# =============================
# 4. KeyError
# =============================

# --- Example 4: Missing dictionary key ---
print("=== KeyError ===")

person = {"name": "Trush", "age": 21}

try:
    salary = person["salary"]
except KeyError as e:
    print(f"person['salary'] → KeyError: {e}")

# Safe alternative: .get()
salary = person.get("salary", "Not found")
print(f"person.get('salary', 'Not found') → {salary}")

print()

# =============================
# 5. ZeroDivisionError
# =============================

# --- Example 5: Division by zero ---
print("=== ZeroDivisionError ===")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"10 / 0 → ZeroDivisionError: {e}")

try:
    result = 10 // 0
except ZeroDivisionError as e:
    print(f"10 // 0 → ZeroDivisionError: {e}")

try:
    result = 10 % 0
except ZeroDivisionError as e:
    print(f"10 % 0 → ZeroDivisionError: {e}")

print()

# =============================
# 6. FileNotFoundError
# =============================

# --- Example 6: Opening a missing file ---
print("=== FileNotFoundError ===")

try:
    with open("this_file_does_not_exist_xyz.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"open('missing.txt') → FileNotFoundError: {e}")

print()

# =============================
# 7. AttributeError
# =============================

# --- Example 7: Wrong attribute or method ---
print("=== AttributeError ===")

try:
    "hello".append("!")
except AttributeError as e:
    print(f"'hello'.append('!') → AttributeError: {e}")

try:
    numbers = [1, 2, 3]
    numbers.upper()
except AttributeError as e:
    print(f"[1,2,3].upper() → AttributeError: {e}")

print()

# =============================
# 8. NameError
# =============================

# --- Example 8: Undefined variable ---
print("=== NameError ===")

try:
    print(undefined_variable_xyz)
except NameError as e:
    print(f"undefined_variable_xyz → NameError: {e}")

print()

# =============================
# 9. QUICK REFERENCE TABLE
# =============================

# --- Example 9: Summary of all exceptions ---
print("=== Exception Quick Reference ===")
print()

exceptions = [
    ("ValueError",          "Wrong value",           "int('hello')"),
    ("TypeError",           "Wrong type",            "'hello' + 5"),
    ("IndexError",          "Bad index",             "[1,2][10]"),
    ("KeyError",            "Missing dict key",      "d['missing']"),
    ("ZeroDivisionError",   "Divide by zero",        "10 / 0"),
    ("FileNotFoundError",   "File doesn't exist",    "open('?.txt')"),
    ("AttributeError",      "Wrong attribute",       "'str'.append()"),
    ("NameError",           "Undefined variable",    "print(xyz)"),
]

print(f"{'Exception':<22} {'Cause':<22} {'Example'}")
print("-" * 60)
for exc, cause, example in exceptions:
    print(f"{exc:<22} {cause:<22} {example}")

# ============================================
# TRY IT YOURSELF:
# 1. Trigger a ValueError with float()
# 2. Create a TypeError by adding a list to an int
# 3. Use .get() to safely access a missing dict key
# ============================================
