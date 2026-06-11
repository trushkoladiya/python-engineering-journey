# ============================================
# MODULE 11 - SUBTOPIC 4: Multiple Exception Handling
# ============================================

# =============================
# 1. MULTIPLE except BLOCKS
# =============================

# --- Example 1: Different handling for different errors ---
print("=== Multiple except Blocks ===")
print()

test_inputs = ["10", "0", "hello", "3.14"]

for user_input in test_inputs:
    print(f"  Input: '{user_input}'")
    try:
        number = int(user_input)
        result = 100 / number
        print(f"    100 / {number} = {result}")
    except ValueError:
        print(f"    → ValueError: not a valid integer")
    except ZeroDivisionError:
        print(f"    → ZeroDivisionError: cannot divide by zero")

print()

# --- Example 2: Multiple errors from different operations ---
print("=== Different Operations, Different Errors ===")
print()

data = {"scores": [85, 92, 78]}

test_cases = [
    ("scores", 0),    # Works fine
    ("scores", 10),   # IndexError
    ("grades", 0),    # KeyError
]

for key, index in test_cases:
    print(f"  data['{key}'][{index}]:")
    try:
        value = data[key][index]
        print(f"    → {value}")
    except KeyError:
        print(f"    → KeyError: key '{key}' not found")
    except IndexError:
        print(f"    → IndexError: index {index} out of range")

print()

# =============================
# 2. TUPLE-BASED HANDLING
# =============================

# --- Example 3: Same handler for multiple exceptions ---
print("=== Tuple-Based Exception Handling ===")
print()

test_values = ["42", "hello", "0"]

for val in test_values:
    print(f"  Processing '{val}':")
    try:
        number = int(val)
        result = 100 / number
        print(f"    → Result: {result}")
    except (ValueError, ZeroDivisionError):
        print(f"    → Number error occurred!")

print()

# --- Example 4: Tuple with 'as' to see the actual error ---
print("=== Tuple with Error Message ===")
print()

risky_operations = [
    lambda: int("hello"),          # ValueError
    lambda: 10 / 0,               # ZeroDivisionError
    lambda: [1, 2][10],           # IndexError
]

labels = ["int('hello')", "10 / 0", "[1,2][10]"]

for label, operation in zip(labels, risky_operations):
    try:
        operation()
    except (ValueError, ZeroDivisionError, IndexError) as e:
        error_type = type(e).__name__
        print(f"  {label} → {error_type}: {e}")

print()

# =============================
# 3. ORDER MATTERS
# =============================

# --- Example 5: Specific before general ---
print("=== Exception Order Matters ===")
print()

# FileNotFoundError is a subtype of OSError
# If we catch OSError first, FileNotFoundError is also caught by it

# Correct order: specific first
try:
    with open("nonexistent_xyz.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("  Specific: FileNotFoundError caught (correct!)")
except OSError:
    print("  General: OSError caught")

print()

# =============================
# 4. PRACTICAL: SAFE DATA PROCESSOR
# =============================

# --- Example 6: Processing a list of mixed data ---
print("=== Safe Data Processor ===")
print()

raw_data = [
    {"name": "Trush", "score": "95"},
    {"name": "Rahul", "score": "hello"},
    {"name": "Carol", "score": "0"},
    {"name": "Dave"},                       # Missing 'score' key
]

results = []

for record in raw_data:
    try:
        name = record["name"]
        score = int(record["score"])
        percentage = 100 / score * score    # Just to test division
        results.append((name, score))
        print(f"  ✓ {name}: score = {score}")
    except KeyError:
        print(f"  ✗ {record.get('name', '?')}: missing 'score' field")
    except ValueError:
        print(f"  ✗ {record['name']}: score is not a number")
    except ZeroDivisionError:
        print(f"  ✗ {record['name']}: score cannot be zero")

print(f"\n  Successfully processed: {len(results)} out of {len(raw_data)}")
print()

# --- Example 7: Multiple except with file operations ---
print("=== File Processing with Multiple Handlers ===")
print()

filenames = ["test_data.txt", "nonexistent.txt"]

# Create a test file first
with open("test_data.txt", "w") as f:
    f.write("42\nhello\n0\n")

for filename in filenames:
    print(f"  Processing '{filename}':")
    try:
        with open(filename, "r") as f:
            for line_num, line in enumerate(f, 1):
                value = int(line.strip())
                result = 100 / value
                print(f"    Line {line_num}: 100 / {value} = {result}")
    except FileNotFoundError:
        print(f"    → File not found!")
    except ValueError:
        print(f"    → Invalid number in file at line {line_num}")
    except ZeroDivisionError:
        print(f"    → Division by zero at line {line_num}")
    print()

# Clean up test file
import os
os.remove("test_data.txt")

# ============================================
# TRY IT YOURSELF:
# 1. Write a try with 3 different except blocks
# 2. Use tuple-based handling for ValueError and TypeError
# 3. Process a dictionary with potential KeyError and TypeError
# ============================================
