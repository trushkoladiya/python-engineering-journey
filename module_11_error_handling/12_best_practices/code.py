# ============================================
# MODULE 11 - SUBTOPIC 12: Best Practices
# ============================================

import os

# =============================
# 1. SPECIFIC vs BROAD EXCEPTIONS
# =============================

# --- Example 1: Bad — bare except ---
print("=== Rule 1: No Bare except ===")
print()

# BAD: bare except catches everything — even KeyboardInterrupt!
print("  BAD approach (bare except):")
try:
    result = 10 / 0
except:
    print("    Something went wrong (but what? we don't know!)")

# GOOD: specific except
print("  GOOD approach (specific except):")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("    Cannot divide by zero — clear and specific!")

print()

# --- Example 2: Catching too broadly ---
print("=== Rule 2: Don't Catch Too Broadly ===")
print()

# BAD: Exception catches bugs you didn't intend
print("  BAD: catching Exception hides bugs")
data = {"name": "Trush"}

try:
    # Typo: 'nme' instead of 'name' — this is a BUG
    value = data["nme"]
    result = int(value)
except Exception:
    print("    'Something failed' — but was it ValueError or KeyError?")
    print("    We can't tell! The KeyError bug is hidden.")

# GOOD: catch only what you expect
print("  GOOD: catching specific types reveals bugs")
try:
    value = data["name"]
    result = int(value)
except ValueError:
    print("    Value is not a number")
except KeyError as e:
    print(f"    Missing key: {e} — now we can see the bug!")

print()

# =============================
# 2. DON'T SILENCE ERRORS
# =============================

# --- Example 3: Silent pass vs proper handling ---
print("=== Rule 3: Don't Silence Errors ===")
print()

scores_text = ["90", "hello", "85", "", "70"]

# BAD: silently ignore errors
print("  BAD: silent pass")
bad_scores = []
for text in scores_text:
    try:
        bad_scores.append(int(text))
    except ValueError:
        pass   # Error disappears — no way to know what happened

print(f"    Got {len(bad_scores)} scores (2 silently dropped, no warning!)")

# GOOD: log the error
print("  GOOD: log the error")
good_scores = []
skipped = []
for text in scores_text:
    try:
        good_scores.append(int(text))
    except ValueError:
        skipped.append(text)
        print(f"    Warning: skipped invalid value '{text}'")

print(f"    Got {len(good_scores)} scores, skipped {len(skipped)}")

print()

# =============================
# 3. SMALL TRY BLOCKS
# =============================

# --- Example 4: Too much in try vs focused try ---
print("=== Rule 6: Keep try Blocks Small ===")
print()

# BAD: everything in one big try
print("  BAD: big try block")
data_dict = {"value": "42", "multiplier": "3"}

try:
    raw_value = data_dict["value"]
    number = int(raw_value)
    multiplier = int(data_dict["multiplier"])
    result = number * multiplier
    doubled = result * 2
    print(f"    Result: {doubled}")
except ValueError:
    print("    A number conversion failed — but which one?")
except KeyError:
    print("    A key was missing — but which one?")

# GOOD: separate try blocks for separate operations
print("  GOOD: focused try blocks")

try:
    raw_value = data_dict["value"]
except KeyError:
    print("    Missing 'value' key")
    raw_value = "0"

try:
    number = int(raw_value)
except ValueError:
    print(f"    '{raw_value}' is not a valid number")
    number = 0

try:
    multiplier = int(data_dict.get("multiplier", "1"))
except ValueError:
    print("    Invalid multiplier")
    multiplier = 1

result = number * multiplier * 2
print(f"    Result: {result}")

print()

# =============================
# 4. USE 'with' FOR RESOURCES
# =============================

# --- Example 5: Manual cleanup vs 'with' ---
print("=== Rule 5: Use 'with' for Resources ===")
print()

# Create a test file
with open("best_practice_test.txt", "w") as f:
    f.write("hello world")

# BAD: manual file handling
print("  BAD: manual open/close")
f = None
try:
    f = open("best_practice_test.txt", "r")
    content = f.read()
    print(f"    Read: '{content}'")
finally:
    if f:
        f.close()
        print("    Manually closed file")

# GOOD: 'with' handles cleanup automatically
print("  GOOD: 'with' statement")
try:
    with open("best_practice_test.txt", "r") as f:
        content = f.read()
        print(f"    Read: '{content}'")
    print("    File automatically closed!")
except FileNotFoundError:
    print("    File not found")

os.remove("best_practice_test.txt")
print()

# =============================
# 5. HANDLE ONLY EXPECTED ERRORS
# =============================

# --- Example 6: Let unexpected errors propagate ---
print("=== Rule 4: Handle Only Expected Errors ===")
print()

def parse_config_value(text):
    """Parse a config value — only handle what we expect."""
    try:
        return int(text)
    except ValueError:
        # We EXPECT this might not be an integer
        try:
            return float(text)
        except ValueError:
            # We EXPECT this might not be a float either
            return text   # Return as string


test_values = ["42", "3.14", "hello", "True", "-7"]

for val in test_values:
    result = parse_config_value(val)
    print(f"  '{val}' → {result} (type: {type(result).__name__})")

print()

# =============================
# 6. PRACTICAL: WELL-STRUCTURED ERROR HANDLING
# =============================

# --- Example 7: Complete example following all best practices ---
print("=== Complete Best Practice Example ===")
print()

def process_student_file(filename):
    """
    Read student scores from a file.
    Each line: name,score
    Returns list of (name, score) tuples.
    """
    results = []
    warnings = []

    # Rule 5: Use 'with' for file handling
    # Rule 4: Only handle expected errors
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"  Error: '{filename}' not found")
        return [], ["File not found"]

    for line_num, line in enumerate(lines, 1):
        line = line.strip()

        # Skip empty lines (not an error)
        if not line:
            continue

        # Rule 6: Small, focused try block
        parts = line.split(",")
        if len(parts) != 2:
            # Rule 3: Don't silence — log it
            warnings.append(f"Line {line_num}: bad format '{line}'")
            continue

        name = parts[0].strip()

        # Rule 2: Catch specific exceptions
        try:
            score = int(parts[1].strip())
        except ValueError:
            warnings.append(f"Line {line_num}: invalid score for {name}")
            continue

        # Validation (not an exception — just logic)
        if score < 0 or score > 100:
            warnings.append(f"Line {line_num}: score {score} out of range for {name}")
            continue

        results.append((name, score))

    return results, warnings


# Create test data
with open("students.csv", "w") as f:
    f.write("Trush,95\n")
    f.write("Rahul,hello\n")
    f.write("Carol,87\n")
    f.write("bad line without comma\n")
    f.write("Dave,-5\n")
    f.write("Eve,92\n")
    f.write("\n")
    f.write("Frank,78\n")

# Process
students, warns = process_student_file("students.csv")

print("  Results:")
for name, score in students:
    print(f"    {name}: {score}")

if warns:
    print()
    print("  Warnings:")
    for w in warns:
        print(f"    ⚠ {w}")

print()
print(f"  Summary: {len(students)} valid, {len(warns)} warnings")

# Cleanup
os.remove("students.csv")

# ============================================
# TRY IT YOURSELF:
# 1. Refactor some old code to follow these best practices
# 2. Replace bare except with specific exceptions
# 3. Add proper error messages instead of silent pass
# ============================================
