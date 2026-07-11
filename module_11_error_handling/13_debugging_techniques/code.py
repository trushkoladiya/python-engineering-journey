# ============================================
# MODULE 11 - SUBTOPIC 13: Debugging Techniques
# ============================================

import traceback

# =============================
# 1. READING TRACEBACKS
# =============================

# --- Example 1: Understanding a traceback ---
print("=== Reading a Traceback ===")
print()

def calculate_average(numbers):
    """Calculate average of numbers."""
    total = sum(numbers)
    return total / len(numbers)


def process_scores(scores):
    """Process a list of scores."""
    return calculate_average(scores)


def generate_report(data):
    """Generate a report from data."""
    return process_scores(data)


# Trigger an error and capture the traceback
try:
    generate_report([])   # Empty list → ZeroDivisionError
except ZeroDivisionError:
    tb = traceback.format_exc()
    print("  Full traceback:")
    for line in tb.strip().split("\n"):
        print(f"    {line}")
    print()
    print("  How to read this (bottom to top):")
    print("    1. Bottom: 'ZeroDivisionError: division by zero'")
    print("    2. Above:  'return total / len(numbers)' — the failing line")
    print("    3. Above:  in 'calculate_average' — the function")
    print("    4. Above:  called from 'process_scores'")
    print("    5. Top:    called from 'generate_report'")

print()

# =============================
# 2. PRINT DEBUGGING
# =============================

# --- Example 2: Using print() to find bugs ---
print("=== Print Debugging ===")
print()

def buggy_average(text_scores):
    """Calculate average — but has a bug!"""
    total = 0
    count = 0

    for score_text in text_scores:
        # DEBUG: see what we're processing
        print(f"    DEBUG: processing '{score_text}' (type: {type(score_text).__name__})")

        score = int(score_text)

        # DEBUG: see the converted value
        print(f"    DEBUG: converted to {score}")

        total += score
        count += 1

    # DEBUG: check values before division
    print(f"    DEBUG: total={total}, count={count}")

    return total / count


try:
    scores = ["90", "85", "78"]
    result = buggy_average(scores)
    print(f"    Result: {result}")
except Exception as e:
    print(f"    Error: {type(e).__name__}: {e}")

print()

# --- Example 3: Finding a type bug ---
print("=== Finding Type Bugs ===")
print()

def concatenate_items(items):
    """Join items into a string — type bug possible."""
    result = ""
    for item in items:
        # DEBUG: check type before concatenation
        print(f"    DEBUG: item={item}, type={type(item).__name__}")

        try:
            result += str(item) + ", "
        except TypeError as e:
            print(f"    DEBUG: TypeError at item={item}: {e}")
            continue

    return result.rstrip(", ")


data = ["Trush", 42, True, [1, 2], "Rahul"]
print(f"    Result: {concatenate_items(data)}")
print()

# =============================
# 3. CHECKING VARIABLE STATE
# =============================

# --- Example 4: Debug function that shows variable info ---
print("=== Variable State Inspection ===")
print()

def debug_var(name, value):
    """Print debug info about a variable."""
    print(f"    [{name}] value={value!r}, type={type(value).__name__}, ", end="")
    if isinstance(value, (str, list, tuple, dict, set)):
        print(f"len={len(value)}")
    elif isinstance(value, (int, float)):
        print(f"is_zero={value == 0}")
    else:
        print()


# Use it to inspect variables
data = {"name": "Trush", "scores": [90, 85, 78], "grade": "A"}

debug_var("data", data)
debug_var("name", data["name"])
debug_var("scores", data["scores"])
debug_var("first_score", data["scores"][0])
debug_var("grade", data["grade"])

print()

# =============================
# 4. ISOLATING THE BUG
# =============================

# --- Example 5: Narrowing down the problem ---
print("=== Isolating Bugs ===")
print()

def process_records(records):
    """Process records — has a bug somewhere."""
    results = []

    for i, record in enumerate(records):
        print(f"    Processing record {i}: {record}")

        try:
            # Step 1: Extract name
            name = record["name"]
            print(f"      Step 1 OK: name = '{name}'")

            # Step 2: Extract and convert score
            score_text = record["score"]
            print(f"      Step 2 OK: score_text = '{score_text}'")

            score = int(score_text)
            print(f"      Step 3 OK: score = {score}")

            # Step 4: Calculate percentage
            percentage = score / record.get("max_score", 100) * 100
            print(f"      Step 4 OK: percentage = {percentage}%")

            results.append((name, percentage))

        except (KeyError, ValueError, ZeroDivisionError) as e:
            print(f"      FAILED at: {type(e).__name__}: {e}")

    return results


test_records = [
    {"name": "Trush", "score": "90", "max_score": 100},
    {"name": "Rahul", "score": "hello"},                       # ValueError
    {"name": "Carol", "score": "80", "max_score": 0},        # ZeroDivisionError
    {"score": "70"},                                          # KeyError
]

results = process_records(test_records)
print()
print(f"    Successful: {results}")
print()

# =============================
# 5. COMMON BUG PATTERNS
# =============================

# --- Example 6: Off-by-one errors ---
print("=== Common Bug: Off-by-One ===")
print()

items = ["a", "b", "c", "d", "e"]

# Bug: using <= instead of <
print("  Bug (IndexError on last iteration):")
try:
    for i in range(len(items) + 1):   # Goes one too far!
        print(f"    items[{i}] = {items[i]}")
except IndexError as e:
    print(f"    IndexError at i={i}: {e}")

print()

# Fix
print("  Fix:")
for i in range(len(items)):
    print(f"    items[{i}] = {items[i]}")

print()

# --- Example 7: Mutable default argument bug ---
print("=== Common Bug: Mutable Default ===")
print()

# BUG: mutable default argument is shared between calls!
def add_item_buggy(item, items=[]):
    items.append(item)
    return items

result1 = add_item_buggy("apple")
print(f"  Call 1: {result1}")        # ['apple']
result2 = add_item_buggy("banana")
print(f"  Call 2: {result2}")        # ['apple', 'banana'] — BUG!

print()

# FIX: use None as default
def add_item_fixed(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

result1 = add_item_fixed("apple")
print(f"  Call 1: {result1}")        # ['apple']
result2 = add_item_fixed("banana")
print(f"  Call 2: {result2}")        # ['banana'] — Correct!

print()

# =============================
# 6. PRACTICAL: DEBUG HELPER
# =============================

# --- Example 8: A reusable debug wrapper ---
print("=== Practical: Debug Wrapper ===")
print()

def debug_call(func, *args, **kwargs):
    """Call a function with debug output."""
    func_name = func.__name__
    print(f"  Calling {func_name}({args}, {kwargs})")

    try:
        result = func(*args, **kwargs)
        print(f"  → Returned: {result!r} (type: {type(result).__name__})")
        return result
    except Exception as e:
        print(f"  → Raised {type(e).__name__}: {e}")
        tb_lines = traceback.format_exc().strip().split("\n")
        # Show just the relevant lines
        print(f"  → Location: {tb_lines[-2].strip()}")
        return None


# Use it
debug_call(int, "42")
debug_call(int, "hello")
debug_call(sorted, [3, 1, 2])
debug_call(lambda x: 100 / x, 0)

# ============================================
# TRY IT YOURSELF:
# 1. Trigger an error and read the traceback bottom-to-top
# 2. Add print debugging to find a bug in your own code
# 3. Use the debug_var function to inspect your variables
# ============================================
