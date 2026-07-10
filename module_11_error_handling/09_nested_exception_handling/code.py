# ============================================
# MODULE 11 - SUBTOPIC 9: Nested Exception Handling
# ============================================

import os

# =============================
# 1. BASIC NESTING
# =============================

# --- Example 1: Inner and outer try-except ---
print("=== Basic Nested try-except ===")
print()

try:
    print("  Outer try: starting")
    try:
        print("  Inner try: attempting int('hello')")
        result = int("hello")
    except ValueError:
        print("  Inner except: caught ValueError")
    print("  Outer try: continues after inner block")
except Exception:
    print("  Outer except: this won't run (inner handled it)")

print()

# =============================
# 2. EXCEPTION BUBBLING
# =============================

# --- Example 2: Unhandled inner exception bubbles up ---
print("=== Exception Bubbling ===")
print()

try:
    print("  Outer try: starting")
    try:
        print("  Inner try: attempting 10 / 0")
        result = 10 / 0
    except ValueError:
        # This doesn't match ZeroDivisionError!
        print("  Inner except: caught ValueError (won't happen)")
    print("  This line is skipped — error bubbled up")
except ZeroDivisionError:
    print("  Outer except: caught ZeroDivisionError (bubbled up from inner)")

print()

# =============================
# 3. MULTI-STEP OPERATIONS
# =============================

# --- Example 3: File read + process with nested handling ---
print("=== Multi-Step: File Processing ===")
print()

# Create test files
with open("good_data.txt", "w") as f:
    f.write("42")

with open("bad_data.txt", "w") as f:
    f.write("not_a_number")


def process_file(filename):
    """Read a file and convert its content to a number."""
    print(f"  Processing '{filename}':")

    try:
        # Step 1: Open the file (might fail)
        file = open(filename, "r")

        try:
            # Step 2: Read and convert (might fail differently)
            content = file.read().strip()
            number = int(content)
            print(f"    Success: got number {number}")
            return number

        except ValueError:
            print(f"    Inner error: '{content}' is not a valid number")
            return None

        finally:
            file.close()
            print(f"    Inner finally: file closed")

    except FileNotFoundError:
        print(f"    Outer error: file not found")
        return None


# Test with different files
for filename in ["good_data.txt", "bad_data.txt", "missing.txt"]:
    result = process_file(filename)
    print(f"    Result: {result}")
    print()

# Cleanup
os.remove("good_data.txt")
os.remove("bad_data.txt")

# =============================
# 4. NESTED LOOPS WITH ERROR HANDLING
# =============================

# --- Example 4: Processing a 2D data set ---
print("=== Nested Loops with Error Handling ===")
print()

data_sets = [
    ["10", "20", "30"],
    ["5", "hello", "15"],
    ["8", "0", "12"],
]

print("  Calculating 100 / value for each entry:")
print()

for row_idx, row in enumerate(data_sets):
    print(f"  Row {row_idx}:")
    row_results = []

    for col_idx, value in enumerate(row):
        try:
            number = int(value)
            try:
                result = 100 / number
                row_results.append(result)
                print(f"    [{col_idx}] 100 / {number} = {result:.1f}")
            except ZeroDivisionError:
                print(f"    [{col_idx}] 100 / {number} = Cannot divide by zero!")
        except ValueError:
            print(f"    [{col_idx}] '{value}' is not a number!")

    print(f"    Row results: {row_results}")
    print()

# =============================
# 5. NESTED FUNCTION CALLS
# =============================

# --- Example 5: Errors in called functions ---
print("=== Nested Function Error Handling ===")
print()

def parse_score(text):
    """Parse a score string to int."""
    return int(text)   # Might raise ValueError


def validate_score(score):
    """Check if score is valid."""
    if score < 0 or score > 100:
        raise ValueError(f"Score {score} out of range (0-100)")
    return score


def process_score(text):
    """Parse and validate a score with layered error handling."""
    try:
        # Layer 1: parsing
        try:
            score = parse_score(text)
        except ValueError:
            print(f"    Parse error: '{text}' is not a number")
            return None

        # Layer 2: validation
        try:
            validated = validate_score(score)
        except ValueError as e:
            print(f"    Validation error: {e}")
            return None

        return validated

    except Exception as e:
        # Catch-all for unexpected errors
        print(f"    Unexpected error: {type(e).__name__}: {e}")
        return None


test_scores = ["85", "hello", "150", "-10", "92", "0", "100"]

for text in test_scores:
    result = process_score(text)
    if result is not None:
        print(f"    '{text}' → Score: {result} ✓")

print()

# =============================
# 6. PRACTICAL: BATCH DATA PROCESSOR
# =============================

# --- Example 6: Processing records with nested error handling ---
print("=== Batch Data Processor ===")
print()

records = [
    {"name": "Trush", "scores": ["90", "85", "hello"]},
    {"name": "Rahul", "scores": ["70", "0", "88"]},
    {"scores": ["100", "95"]},                           # Missing name
    {"name": "Dave", "scores": ["80", "92", "76"]},
]

all_results = {}

for idx, record in enumerate(records):
    print(f"  Record {idx + 1}:")

    try:
        # Outer: get the name
        name = record["name"]

        try:
            # Inner: process scores
            valid_scores = []

            for score_str in record["scores"]:
                try:
                    score = int(score_str)
                    if score < 0 or score > 100:
                        print(f"    Skipping invalid score: {score}")
                        continue
                    valid_scores.append(score)
                except ValueError:
                    print(f"    Skipping non-numeric: '{score_str}'")

            if valid_scores:
                avg = sum(valid_scores) / len(valid_scores)
                all_results[name] = avg
                print(f"    {name}: scores={valid_scores}, average={avg:.1f}")
            else:
                print(f"    {name}: no valid scores!")

        except KeyError:
            print(f"    {name}: missing 'scores' field")

    except KeyError:
        print(f"    Record {idx + 1}: missing 'name' field")

    print()

print("  Final Results:")
for name, avg in all_results.items():
    print(f"    {name}: {avg:.1f}")

# ============================================
# TRY IT YOURSELF:
# 1. Write a nested try that handles file open + content parsing
# 2. Create a function with two layers of validation
# 3. Process a list of dicts with nested error handling
# ============================================
