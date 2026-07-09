# ============================================
# MODULE 11 - SUBTOPIC 6: Raising Exceptions
# ============================================

# =============================
# 1. BASIC raise
# =============================

# --- Example 1: Raising a ValueError ---
print("=== Basic raise ===")
print()

try:
    raise ValueError("This is a manually raised error")
except ValueError as e:
    print(f"  Caught: {e}")

print()

# --- Example 2: Raising different exception types ---
print("=== Raising Different Types ===")
print()

errors_to_raise = [
    ValueError("Invalid value provided"),
    TypeError("Expected a string, got int"),
    RuntimeError("Something unexpected happened"),
]

for error in errors_to_raise:
    try:
        raise error
    except (ValueError, TypeError, RuntimeError) as e:
        print(f"  {type(e).__name__}: {e}")

print()

# =============================
# 2. RAISE FOR VALIDATION
# =============================

# --- Example 3: Validating function inputs ---
print("=== Raise for Input Validation ===")
print()

def set_age(age):
    """Set age with validation."""
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")
    if age > 150:
        raise ValueError(f"Age seems unrealistic, got {age}")
    return age


test_ages = [25, -5, 200, 0, 100]

for age in test_ages:
    try:
        result = set_age(age)
        print(f"  set_age({age}) → {result} ✓")
    except (ValueError, TypeError) as e:
        print(f"  set_age({age}) → {e} ✗")

print()

# --- Example 4: Validating string inputs ---
print("=== String Validation ===")
print()

def validate_username(username):
    """Validate a username with rules."""
    if not isinstance(username, str):
        raise TypeError("Username must be a string")
    if len(username) < 3:
        raise ValueError("Username must be at least 3 characters")
    if len(username) > 20:
        raise ValueError("Username must be 20 characters or less")
    if " " in username:
        raise ValueError("Username cannot contain spaces")
    return username


test_names = ["trush", "ab", "this_is_a_very_long_username_indeed", "rahul smith", "charlie"]

for name in test_names:
    try:
        result = validate_username(name)
        print(f"  '{name}' → Valid ✓")
    except (ValueError, TypeError) as e:
        print(f"  '{name}' → {e} ✗")

print()

# =============================
# 3. RAISE WITHOUT MESSAGE vs WITH
# =============================

# --- Example 5: Always include messages ---
print("=== Error Messages Matter ===")
print()

# Bad: no message
try:
    raise ValueError
except ValueError as e:
    print(f"  No message: '{e}' (not helpful!)")

# Good: with message
try:
    raise ValueError("Expected positive number, got -3")
except ValueError as e:
    print(f"  With message: '{e}' (much better!)")

print()

# =============================
# 4. RE-RAISING EXCEPTIONS
# =============================

# --- Example 6: Log and re-raise ---
print("=== Re-raising Exceptions ===")
print()

def process_data(data):
    """Process data, log errors, then re-raise."""
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print(f"  [LOG] Failed to process: '{data}'")
        raise   # Re-raise the same exception


test_data = ["42", "hello", "100"]

for data in test_data:
    try:
        result = process_data(data)
        print(f"  process_data('{data}') → {result}")
    except ValueError as e:
        print(f"  Caller caught re-raised error: {e}")

print()

# --- Example 7: Cleanup then re-raise ---
print("=== Cleanup and Re-raise ===")
print()

def read_config(filename):
    """Try to read config, cleanup on error, re-raise."""
    temp_data = {"status": "loading"}

    try:
        with open(filename, "r") as f:
            content = f.read()
        temp_data["status"] = "loaded"
        return content
    except FileNotFoundError:
        temp_data["status"] = "failed"
        print(f"  [CLEANUP] Reset status to '{temp_data['status']}'")
        raise


try:
    config = read_config("nonexistent_config.ini")
except FileNotFoundError:
    print("  Caller: config file not found, using defaults")

print()

# =============================
# 5. PRACTICAL: SAFE CALCULATOR
# =============================

# --- Example 8: Calculator with validation ---
print("=== Safe Calculator ===")
print()

def calculate(a, b, operation):
    """Perform a calculation with input validation."""
    # Validate types
    if not isinstance(a, (int, float)):
        raise TypeError(f"First operand must be a number, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second operand must be a number, got {type(b).__name__}")

    # Validate operation
    valid_ops = ["+", "-", "*", "/"]
    if operation not in valid_ops:
        raise ValueError(f"Invalid operation '{operation}'. Use: {valid_ops}")

    # Perform calculation
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


test_calculations = [
    (10, 5, "+"),
    (10, 5, "-"),
    (10, 5, "*"),
    (10, 5, "/"),
    (10, 0, "/"),
    (10, 5, "%"),
    ("10", 5, "+"),
]

for a, b, op in test_calculations:
    try:
        result = calculate(a, b, op)
        print(f"  calculate({a}, {b}, '{op}') = {result}")
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"  calculate({a}, {b}, '{op}') → {type(e).__name__}: {e}")

# ============================================
# TRY IT YOURSELF:
# 1. Write a function that raises ValueError for empty strings
# 2. Create a validate_email() that checks for '@'
# 3. Use re-raise after logging an error
# ============================================
