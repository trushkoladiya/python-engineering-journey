# ============================================
# MODULE 11 - SUBTOPIC 11: Exception Propagation
# ============================================

import traceback

# =============================
# 1. BASIC PROPAGATION
# =============================

# --- Example 1: Exception bubbles up through calls ---
print("=== Basic Exception Propagation ===")
print()

def level_3():
    """Deepest level — error originates here."""
    print("    level_3: about to raise ValueError")
    return int("hello")   # ValueError!


def level_2():
    """Middle level — doesn't catch, passes through."""
    print("  level_2: calling level_3")
    return level_3()


def level_1():
    """Top level — catches the error."""
    print("level_1: calling level_2")
    try:
        return level_2()
    except ValueError as e:
        print(f"\nlevel_1: caught ValueError that bubbled up: {e}")
        return None


result = level_1()
print(f"Result: {result}")
print()

# =============================
# 2. CATCHING AT DIFFERENT LEVELS
# =============================

# --- Example 2: Where you catch changes the behavior ---
print("=== Catching at Different Levels ===")
print()

def divide(a, b):
    """Lowest level."""
    return a / b


def calculate_ratio(values):
    """Middle level — could catch here."""
    total = sum(values)
    return divide(total, len(values))


def process_report(data):
    """Top level — catches here."""
    try:
        ratio = calculate_ratio(data)
        print(f"  Ratio: {ratio}")
    except ZeroDivisionError:
        print("  Error: no data to calculate ratio (empty list)")


# Normal case
print("  With data:")
process_report([10, 20, 30])

# Error case — empty list → len = 0 → ZeroDivisionError
print("  Without data:")
process_report([])

print()

# --- Example 3: Catching at the middle level instead ---
print("=== Catching at Middle Level ===")
print()

def safe_calculate_ratio(values):
    """Middle level catches the error and provides a default."""
    try:
        total = sum(values)
        return divide(total, len(values))
    except ZeroDivisionError:
        print("  (Middle level handled: returning 0 as default)")
        return 0


def process_report_v2(data):
    """Top level doesn't need to worry about the error."""
    ratio = safe_calculate_ratio(data)
    print(f"  Ratio: {ratio}")


process_report_v2([10, 20, 30])
process_report_v2([])
print()

# =============================
# 3. VISUALIZING THE PROPAGATION PATH
# =============================

# --- Example 4: Tracking the propagation chain ---
print("=== Tracking Propagation ===")
print()

def func_c():
    print("    func_c: raising error")
    raise ValueError("Something went wrong in func_c")


def func_b():
    print("  func_b: calling func_c")
    try:
        func_c()
    except ValueError:
        print("  func_b: caught and re-raising")
        raise   # Re-raise to propagate further


def func_a():
    print("func_a: calling func_b")
    try:
        func_b()
    except ValueError as e:
        print(f"func_a: finally caught: {e}")


func_a()
print()

# =============================
# 4. USING TRACEBACK MODULE
# =============================

# --- Example 5: Capturing the full traceback ---
print("=== Capturing Tracebacks ===")
print()

def inner_function():
    return int("bad_value")


def middle_function():
    return inner_function()


def outer_function():
    return middle_function()


try:
    outer_function()
except ValueError:
    # Get the formatted traceback as a string
    tb = traceback.format_exc()
    print("  Full traceback:")
    for line in tb.strip().split("\n"):
        print(f"    {line}")

print()

# =============================
# 5. PROPAGATION WITH MULTIPLE EXCEPTION TYPES
# =============================

# --- Example 6: Different errors propagate differently ---
print("=== Multiple Exception Types Propagating ===")
print()

def fetch_data(source):
    """Simulate fetching data from different sources."""
    if source == "file":
        raise FileNotFoundError("data.csv not found")
    elif source == "network":
        raise ConnectionError("Network unreachable")
    elif source == "database":
        raise ValueError("Invalid query")
    return {"value": 42}


def process_source(source):
    """Process data from a source."""
    return fetch_data(source)


def run_pipeline(sources):
    """Run the full pipeline, handling errors at top level."""
    for source in sources:
        try:
            data = process_source(source)
            print(f"  '{source}': got {data}")
        except FileNotFoundError as e:
            print(f"  '{source}': File error — {e}")
        except ConnectionError as e:
            print(f"  '{source}': Network error — {e}")
        except ValueError as e:
            print(f"  '{source}': Data error — {e}")


run_pipeline(["file", "network", "database", "memory"])
print()

# =============================
# 6. PRACTICAL: ERROR HANDLING STRATEGY
# =============================

# --- Example 7: Let errors propagate to the right level ---
print("=== Practical: Multi-Layer Application ===")
print()

# Layer 1: Data access (low level)
def read_score(filename):
    """Read a score from a file."""
    with open(filename, "r") as f:
        content = f.read().strip()
    return int(content)   # Might raise ValueError


# Layer 2: Business logic (middle level)
def get_grade(filename):
    """Get a letter grade from a score file."""
    score = read_score(filename)   # Let errors propagate
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


# Layer 3: Application (top level — catches everything)
def display_grade(filename):
    """Display the grade, handling all errors."""
    try:
        grade = get_grade(filename)
        print(f"  '{filename}': Grade = {grade}")
    except FileNotFoundError:
        print(f"  '{filename}': File not found")
    except ValueError:
        print(f"  '{filename}': Invalid score format")


# Create test files
import os

with open("student_a.txt", "w") as f:
    f.write("95")

with open("student_b.txt", "w") as f:
    f.write("not_a_number")

# Test all scenarios
display_grade("student_a.txt")
display_grade("student_b.txt")
display_grade("student_c.txt")   # Doesn't exist

# Cleanup
os.remove("student_a.txt")
os.remove("student_b.txt")

# ============================================
# TRY IT YOURSELF:
# 1. Create 3 nested functions and let an error propagate
# 2. Catch the same error at different levels and observe the difference
# 3. Use traceback.format_exc() to capture error details
# ============================================
