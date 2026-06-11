# ============================================
# MODULE 11 - SUBTOPIC 8: Exception Object Handling
# ============================================

# =============================
# 1. CAPTURING WITH 'as'
# =============================

# --- Example 1: Basic exception capture ---
print("=== Capturing Exception with 'as' ===")
print()

try:
    number = int("hello")
except ValueError as e:
    print(f"  Error message: {e}")
    print(f"  Error type:    {type(e).__name__}")
    print(f"  Error args:    {e.args}")

print()

# --- Example 2: Different exceptions, same pattern ---
print("=== Capturing Different Exception Types ===")
print()

errors = [
    lambda: 10 / 0,
    lambda: int("abc"),
    lambda: [1, 2][10],
    lambda: {"a": 1}["z"],
]

labels = ["10 / 0", "int('abc')", "[1,2][10]", "dict['z']"]

for label, trigger in zip(labels, errors):
    try:
        trigger()
    except Exception as e:
        print(f"  {label}:")
        print(f"    Type:    {type(e).__name__}")
        print(f"    Message: {e}")
        print(f"    Args:    {e.args}")
        print()

# =============================
# 2. USING str() AND repr()
# =============================

# --- Example 3: String representations ---
print("=== str() vs repr() ===")
print()

try:
    value = int("not_a_number")
except ValueError as e:
    print(f"  str(e):  {str(e)}")        # Human-readable message
    print(f"  repr(e): {repr(e)}")       # Detailed representation

print()

try:
    data = {"name": "Trush"}
    value = data["age"]
except KeyError as e:
    print(f"  str(e):  {str(e)}")        # Just the key
    print(f"  repr(e): {repr(e)}")       # KeyError('age')

print()

# =============================
# 3. ACCESSING .args
# =============================

# --- Example 4: The args tuple ---
print("=== Exception .args ===")
print()

# Single argument
try:
    raise ValueError("bad value")
except ValueError as e:
    print(f"  Single arg: {e.args}")      # ('bad value',)
    print(f"  First arg:  {e.args[0]}")

print()

# Multiple arguments (less common but possible)
try:
    raise ValueError("bad value", 42, "extra info")
except ValueError as e:
    print(f"  Multiple args: {e.args}")
    for i, arg in enumerate(e.args):
        print(f"    args[{i}] = {arg}")

print()

# =============================
# 4. LOGGING ERRORS
# =============================

# --- Example 5: Building an error log ---
print("=== Error Logging ===")
print()

error_log = []

test_operations = [
    ("Convert 'hello'", lambda: int("hello")),
    ("Divide by zero",  lambda: 10 / 0),
    ("Bad index",       lambda: [1, 2][10]),
    ("Convert '42'",    lambda: int("42")),         # This succeeds
    ("Missing key",     lambda: {"a": 1}["b"]),
]

for description, operation in test_operations:
    try:
        result = operation()
        print(f"  ✓ {description}: success (result={result})")
    except Exception as e:
        error_entry = {
            "operation": description,
            "error_type": type(e).__name__,
            "message": str(e),
        }
        error_log.append(error_entry)
        print(f"  ✗ {description}: {type(e).__name__}")

print()
print(f"  Total errors logged: {len(error_log)}")
print()

# Display the log
print("  Error Log:")
for i, entry in enumerate(error_log, 1):
    print(f"    {i}. [{entry['error_type']}] {entry['operation']}: {entry['message']}")

print()

# =============================
# 5. CONDITIONAL HANDLING BASED ON ERROR
# =============================

# --- Example 6: Different responses based on error content ---
print("=== Conditional Error Handling ===")
print()

def convert_value(text):
    """Convert text to a number with detailed error info."""
    try:
        # Try int first
        return int(text)
    except ValueError as e:
        error_msg = str(e)
        if "invalid literal" in error_msg:
            print(f"    '{text}' is not a number at all")
        return None


test_values = ["42", "hello", "3.14", "", "  "]

for val in test_values:
    result = convert_value(val)
    if result is not None:
        print(f"    '{val}' → {result}")

print()

# =============================
# 6. PRACTICAL: ERROR REPORT GENERATOR
# =============================

# --- Example 7: Generating a formatted error report ---
print("=== Error Report Generator ===")
print()

def process_student_scores(students):
    """Process scores and generate an error report."""
    results = []
    errors = []

    for name, score_str in students:
        try:
            score = int(score_str)
            if score < 0 or score > 100:
                raise ValueError(f"Score out of range: {score}")
            results.append((name, score))
        except ValueError as e:
            errors.append({
                "student": name,
                "input": score_str,
                "error_type": type(e).__name__,
                "error_message": str(e),
            })

    return results, errors


students = [
    ("Trush", "95"),
    ("Rahul", "hello"),
    ("Carol", "87"),
    ("Dave", "-5"),
    ("Eve", "110"),
    ("Frank", "73"),
]

valid, error_report = process_student_scores(students)

print("  Valid Scores:")
for name, score in valid:
    print(f"    {name}: {score}")

print()
print("  Error Report:")
for err in error_report:
    print(f"    Student: {err['student']}")
    print(f"      Input:   '{err['input']}'")
    print(f"      Error:   {err['error_type']}: {err['error_message']}")
    print()

print(f"  Summary: {len(valid)} valid, {len(error_report)} errors")

# ============================================
# TRY IT YOURSELF:
# 1. Capture an exception and print its type and message
# 2. Build an error log from a list of operations
# 3. Use e.args to access multiple error arguments
# ============================================
