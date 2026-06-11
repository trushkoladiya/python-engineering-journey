# ============================================
# MODULE 11 - SUBTOPIC 3: try-except Basics
# ============================================

# =============================
# 1. BASIC try-except
# =============================

# --- Example 1: Without try-except (would crash) ---
print("=== Basic try-except ===")
print()

# Without handling, this would crash the program:
#   result = 10 / 0   # ZeroDivisionError!

# With try-except, we handle it gracefully:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Program continues normally after the error is handled.")
print()

# =============================
# 2. CATCHING SPECIFIC EXCEPTIONS
# =============================

# --- Example 2: Catching ValueError ---
print("=== Catching Specific Exceptions ===")
print()

user_inputs = ["42", "hello", "3.14", ""]

for value in user_inputs:
    try:
        number = int(value)
        print(f"  '{value}' → converted to int: {number}")
    except ValueError:
        print(f"  '{value}' → not a valid integer!")

print()

# --- Example 3: Catching KeyError ---
print("=== Catching KeyError ===")
print()

student = {"name": "Trush", "grade": "A"}
keys_to_check = ["name", "grade", "age", "school"]

for key in keys_to_check:
    try:
        value = student[key]
        print(f"  student['{key}'] = {value}")
    except KeyError:
        print(f"  student['{key}'] → Key not found!")

print()

# --- Example 4: Catching IndexError ---
print("=== Catching IndexError ===")
print()

scores = [85, 92, 78]

for i in [0, 1, 2, 5, -1, 10]:
    try:
        print(f"  scores[{i}] = {scores[i]}")
    except IndexError:
        print(f"  scores[{i}] → Index out of range!")

print()

# =============================
# 3. WHAT HAPPENS AFTER try-except
# =============================

# --- Example 5: Code after try-except runs normally ---
print("=== Flow After try-except ===")
print()

print("Step 1: Before the try block")

try:
    result = int("not_a_number")
    print("Step 2: This line is SKIPPED because the error happened above")
except ValueError:
    print("Step 2: Error was caught!")

print("Step 3: This ALWAYS runs — the program continues")
print()

# =============================
# 4. ONLY THE FAILING LINE IS SKIPPED
# =============================

# --- Example 6: Lines after the error in try are skipped ---
print("=== Lines After Error are Skipped ===")
print()

try:
    print("  Line 1: This runs")
    print("  Line 2: This runs")
    result = 10 / 0                     # Error here!
    print("  Line 3: This is SKIPPED")  # Never reached
    print("  Line 4: This is SKIPPED")  # Never reached
except ZeroDivisionError:
    print("  Caught the error — jumped to except")

print()

# =============================
# 5. UNMATCHED EXCEPTIONS
# =============================

# --- Example 7: Wrong exception type is NOT caught ---
print("=== Unmatched Exception Type ===")
print()

try:
    # This raises ValueError, but we catch ZeroDivisionError
    try:
        number = int("hello")
    except ZeroDivisionError:
        print("  This will NOT catch a ValueError!")
except ValueError:
    print("  The ValueError was NOT caught by the inner except")
    print("  It bubbled up to the outer except")

print()

# =============================
# 6. PRACTICAL: SAFE NUMBER INPUT
# =============================

# --- Example 8: Building a safe converter function ---
def safe_to_int(text):
    """Try to convert text to int, return None if impossible."""
    try:
        return int(text)
    except ValueError:
        return None


test_values = ["100", "-5", "hello", "3.14", "0", ""]

print("=== Safe Number Converter ===")
print()

for val in test_values:
    result = safe_to_int(val)
    if result is not None:
        print(f"  '{val}' → {result}")
    else:
        print(f"  '{val}' → Cannot convert")

print()

# --- Example 9: Safe file reading ---
def safe_read_file(filename):
    """Try to read a file, return None if it doesn't exist."""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


result = safe_read_file("nonexistent_file.txt")
if result is None:
    print("File not found — handled gracefully!")
else:
    print(f"File content: {result}")

print()

# --- Example 10: Safe division ---
def safe_divide(a, b):
    """Divide a by b, return None if division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


pairs = [(10, 2), (9, 3), (7, 0), (100, 4), (0, 5)]

print("=== Safe Division ===")
print()

for a, b in pairs:
    result = safe_divide(a, b)
    if result is not None:
        print(f"  {a} / {b} = {result}")
    else:
        print(f"  {a} / {b} = Cannot divide by zero!")

# ============================================
# TRY IT YOURSELF:
# 1. Write a try-except that catches TypeError
# 2. Create a safe function that converts to float
# 3. Try catching the wrong exception type — see what happens
# ============================================
