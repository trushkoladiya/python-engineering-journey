# ============================================
# MODULE 11 - SUBTOPIC 5: else and finally Blocks
# ============================================

# =============================
# 1. THE else BLOCK
# =============================

# 'else' runs ONLY when try succeeds (no exception).

# --- Example 1: else with successful try ---
print("=== else Block ===")
print()

# Case 1: No error → else runs
print("  Case 1: No error")
try:
    result = 100 / 5
except ZeroDivisionError:
    print("    except: division by zero!")
else:
    print(f"    else: result = {result}")

print()

# Case 2: Error occurs → else is skipped
print("  Case 2: Error occurs")
try:
    result = 100 / 0
except ZeroDivisionError:
    print("    except: division by zero!")
else:
    print(f"    else: result = {result}")   # This is SKIPPED

print()

# --- Example 2: Why else is useful ---
print("=== Why Use else? ===")
print()

# Without else — extra code in try block
# (Bad: if print crashes, we'd catch the wrong error)
# try:
#     number = int("42")
#     print(f"Result: {number * 2}")  # This could also raise errors!
# except ValueError:
#     print("Not a number!")

# With else — only risky code in try
values = ["42", "hello", "7"]

for val in values:
    try:
        number = int(val)
    except ValueError:
        print(f"  '{val}' → Not a valid number")
    else:
        # Only runs if int() succeeded
        doubled = number * 2
        print(f"  '{val}' → Doubled: {doubled}")

print()

# =============================
# 2. THE finally BLOCK
# =============================

# 'finally' ALWAYS runs — error or no error.

# --- Example 3: finally always executes ---
print("=== finally Block ===")
print()

# Case 1: No error
print("  Case 1: No error")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("    except: error!")
finally:
    print("    finally: this ALWAYS runs")

print()

# Case 2: Error occurs
print("  Case 2: Error occurs")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("    except: division by zero!")
finally:
    print("    finally: this ALWAYS runs")

print()

# --- Example 4: finally for cleanup ---
print("=== finally for Cleanup ===")
print()

import os

# Create a temporary file
temp_file = "temp_data.txt"

try:
    with open(temp_file, "w") as f:
        f.write("temporary data")
    print(f"  Created '{temp_file}'")

    # Simulate some processing
    with open(temp_file, "r") as f:
        data = f.read()
    print(f"  Read data: '{data}'")

except IOError as e:
    print(f"  File error: {e}")
finally:
    # Always clean up the temp file
    if os.path.exists(temp_file):
        os.remove(temp_file)
        print(f"  Cleaned up '{temp_file}' (finally block)")

print()

# =============================
# 3. FULL STRUCTURE: try-except-else-finally
# =============================

# --- Example 5: All four blocks together ---
print("=== Full try-except-else-finally ===")
print()

test_cases = [("10", "5"), ("10", "0"), ("10", "abc")]

for a_str, b_str in test_cases:
    print(f"  Dividing '{a_str}' by '{b_str}':")
    try:
        a = int(a_str)
        b = int(b_str)
        result = a / b
    except ValueError:
        print(f"    except: invalid number!")
    except ZeroDivisionError:
        print(f"    except: can't divide by zero!")
    else:
        print(f"    else: {a} / {b} = {result}")
    finally:
        print(f"    finally: done processing this pair")
    print()

# =============================
# 4. finally RUNS EVEN WITH return
# =============================

# --- Example 6: finally with return ---
print("=== finally with return ===")
print()

def divide_safe(a, b):
    """Demonstrates that finally runs even when returning."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("    except: caught division by zero")
        return None
    else:
        print(f"    else: division successful")
        return result
    finally:
        # This prints BEFORE the function actually returns
        print("    finally: cleanup complete")


print("  divide_safe(10, 2):")
answer = divide_safe(10, 2)
print(f"    returned: {answer}")
print()

print("  divide_safe(10, 0):")
answer = divide_safe(10, 0)
print(f"    returned: {answer}")
print()

# =============================
# 5. PRACTICAL: SAFE FILE PROCESSOR
# =============================

# --- Example 7: Processing a file with full error handling ---
print("=== Practical: Safe File Processor ===")
print()

def process_number_file(filename):
    """Read numbers from a file and calculate their sum."""
    total = 0
    count = 0

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(f"  File '{filename}' not found!")
        return None
    else:
        # File opened successfully
        try:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        number = float(line)
                        total += number
                        count += 1
                    except ValueError:
                        print(f"  Skipping invalid line: '{line}'")
        finally:
            file.close()
            print(f"  File closed (finally)")

    return total, count


# Create test file
with open("numbers.txt", "w") as f:
    f.write("10\n20\nhello\n30\n")

result = process_number_file("numbers.txt")
if result:
    total, count = result
    print(f"  Sum: {total}, Count: {count}")

print()

result = process_number_file("nonexistent.txt")
print()

# Cleanup
os.remove("numbers.txt")

# ============================================
# TRY IT YOURSELF:
# 1. Write a try-except-else to convert and double a number
# 2. Use finally to print "Done!" after any operation
# 3. Write a function that uses all four blocks
# ============================================
