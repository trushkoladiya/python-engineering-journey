# ============================================
# MODULE 11 - SUBTOPIC 10: Assertions
# ============================================

# =============================
# 1. BASIC ASSERT
# =============================

# --- Example 1: Simple assertions ---
print("=== Basic assert ===")
print()

# Assertion that passes — nothing happens
x = 10
assert x > 0, "x must be positive"
print(f"  x = {x}: assert x > 0 passed ✓")

# Assertion that passes
name = "Trush"
assert len(name) > 0, "Name cannot be empty"
print(f"  name = '{name}': assert len(name) > 0 passed ✓")

# Assertion that passes
items = [1, 2, 3]
assert len(items) == 3, "Expected 3 items"
print(f"  items has {len(items)} elements: assertion passed ✓")

print()

# =============================
# 2. FAILING ASSERTIONS
# =============================

# --- Example 2: Catching a failed assertion ---
print("=== Failing Assertions ===")
print()

try:
    age = -5
    assert age > 0, f"Age must be positive, got {age}"
except AssertionError as e:
    print(f"  AssertionError: {e}")

try:
    score = 150
    assert 0 <= score <= 100, f"Score must be 0-100, got {score}"
except AssertionError as e:
    print(f"  AssertionError: {e}")

try:
    data = []
    assert len(data) > 0, "Data list must not be empty"
except AssertionError as e:
    print(f"  AssertionError: {e}")

print()

# =============================
# 3. ASSERT IN FUNCTIONS
# =============================

# --- Example 3: Precondition checks ---
print("=== Assert for Preconditions ===")
print()

def calculate_average(numbers):
    """Calculate average — asserts list is not empty."""
    assert len(numbers) > 0, "Cannot calculate average of empty list"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    return sum(numbers) / len(numbers)


# Valid input
try:
    result = calculate_average([10, 20, 30])
    print(f"  average([10, 20, 30]) = {result}")
except AssertionError as e:
    print(f"  AssertionError: {e}")

# Empty list
try:
    result = calculate_average([])
    print(f"  average([]) = {result}")
except AssertionError as e:
    print(f"  AssertionError: {e}")

print()

# --- Example 4: Post-condition checks ---
print("=== Assert for Post-conditions ===")
print()

def normalize_scores(scores, max_score):
    """Normalize scores to 0-1 range."""
    assert max_score > 0, "Max score must be positive"

    normalized = [s / max_score for s in scores]

    # Post-condition: all values should be between 0 and 1
    for val in normalized:
        assert 0 <= val <= 1, f"Normalized value {val} out of range!"

    return normalized


try:
    result = normalize_scores([80, 90, 100], 100)
    print(f"  Normalized [80, 90, 100]: {result}")
except AssertionError as e:
    print(f"  AssertionError: {e}")

# Score higher than max — post-condition fails
try:
    result = normalize_scores([80, 90, 120], 100)
    print(f"  Normalized: {result}")
except AssertionError as e:
    print(f"  AssertionError: {e}")

print()

# =============================
# 4. ASSERT vs RAISE
# =============================

# --- Example 5: When to use which ---
print("=== assert vs raise ===")
print()

# BAD: Using assert for user input (can be disabled with python -O!)
def bad_validate(user_input):
    assert user_input != "", "Input cannot be empty"
    return user_input


# GOOD: Using raise for user input
def good_validate(user_input):
    if user_input == "":
        raise ValueError("Input cannot be empty")
    return user_input


# GOOD: Using assert for internal logic checks
def process_data(data):
    # This should never happen if our code is correct
    assert isinstance(data, list), f"Internal error: expected list, got {type(data).__name__}"

    result = [x * 2 for x in data]

    # Sanity check: result should be same length
    assert len(result) == len(data), "Internal error: result length mismatch"

    return result


print("  assert → for internal debugging checks")
print("  raise  → for user input validation")
print()

# Demonstrate both
try:
    good_validate("")
except ValueError as e:
    print(f"  raise caught: {e}")

try:
    bad_validate("")
except AssertionError as e:
    print(f"  assert caught: {e}")

print()

# =============================
# 5. PRACTICAL: TESTING WITH ASSERT
# =============================

# --- Example 6: Simple test suite using assert ---
print("=== Simple Tests with assert ===")
print()

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0


# Test suite
tests_passed = 0
tests_failed = 0

test_cases = [
    ("add(2, 3) == 5",        lambda: add(2, 3) == 5),
    ("add(-1, 1) == 0",       lambda: add(-1, 1) == 0),
    ("multiply(3, 4) == 12",  lambda: multiply(3, 4) == 12),
    ("multiply(0, 5) == 0",   lambda: multiply(0, 5) == 0),
    ("is_even(4) == True",    lambda: is_even(4) == True),
    ("is_even(7) == False",   lambda: is_even(7) == False),
    ("add(2, 2) == 5",        lambda: add(2, 2) == 5),    # This will fail!
]

for description, test_func in test_cases:
    try:
        assert test_func(), f"Test failed: {description}"
        print(f"  ✓ {description}")
        tests_passed += 1
    except AssertionError:
        print(f"  ✗ {description}")
        tests_failed += 1

print()
print(f"  Results: {tests_passed} passed, {tests_failed} failed")

# ============================================
# TRY IT YOURSELF:
# 1. Use assert to check that a list is sorted
# 2. Write a function with pre-condition and post-condition asserts
# 3. Create a small test suite for a function you wrote earlier
# ============================================
