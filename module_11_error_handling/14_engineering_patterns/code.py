# ============================================
# MODULE 11 - SUBTOPIC 14: Engineering-Level Patterns
# ============================================

import os

# =============================
# 1. FAIL-SAFE WITH DEFAULTS
# =============================

# --- Example 1: Default values on failure ---
print("=== Fail-Safe: Default Values ===")
print()

def safe_get(data, key, default=None):
    """Get a value from a dict, return default if missing."""
    try:
        return data[key]
    except (KeyError, TypeError):
        return default


config = {"host": "localhost", "port": "8080", "debug": "true"}

# Get existing and missing keys safely
settings = {
    "host": safe_get(config, "host", "0.0.0.0"),
    "port": int(safe_get(config, "port", "3000")),
    "debug": safe_get(config, "debug", "false") == "true",
    "timeout": int(safe_get(config, "timeout", "30")),   # Missing → default
}

for key, value in settings.items():
    print(f"  {key}: {value}")

print()

# --- Example 2: Safe type conversion with defaults ---
print("=== Safe Type Conversion ===")
print()

def safe_int(value, default=0):
    """Convert to int safely."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def safe_float(value, default=0.0):
    """Convert to float safely."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


test_values = ["42", "3.14", "hello", None, "", "100"]

print(f"  {'Value':<10} {'safe_int':<12} {'safe_float':<12}")
print(f"  {'-'*10} {'-'*12} {'-'*12}")

for val in test_values:
    i = safe_int(val)
    f = safe_float(val)
    print(f"  {str(val):<10} {i:<12} {f:<12.2f}")

print()

# =============================
# 2. RETRY PATTERN
# =============================

# --- Example 3: Retry on failure ---
print("=== Retry Pattern ===")
print()

def retry(operation, max_attempts=3, operation_name="operation"):
    """Retry an operation up to max_attempts times."""
    last_error = None

    for attempt in range(1, max_attempts + 1):
        try:
            result = operation()
            print(f"  Attempt {attempt}: {operation_name} succeeded!")
            return result
        except Exception as e:
            last_error = e
            print(f"  Attempt {attempt}: {operation_name} failed — {e}")

    print(f"  All {max_attempts} attempts failed!")
    raise last_error


# Simulate a flaky operation (fails first 2 times)
attempt_counter = {"count": 0}

def flaky_operation():
    attempt_counter["count"] += 1
    if attempt_counter["count"] < 3:
        raise ConnectionError("Server unavailable")
    return {"status": "ok", "data": [1, 2, 3]}


try:
    result = retry(flaky_operation, max_attempts=5, operation_name="fetch_data")
    print(f"  Result: {result}")
except ConnectionError:
    print("  Gave up after all retries")

print()

# =============================
# 3. GRACEFUL DEGRADATION
# =============================

# --- Example 4: System that keeps working despite partial failures ---
print("=== Graceful Degradation ===")
print()

# Create some test files
for name, content in [("data_a.txt", "100"), ("data_c.txt", "300")]:
    with open(name, "w") as f:
        f.write(content)


def load_all_sources(filenames):
    """Load data from multiple files — skip failures."""
    loaded = {}
    failed = []

    for filename in filenames:
        try:
            with open(filename, "r") as f:
                content = f.read().strip()
            loaded[filename] = int(content)
        except FileNotFoundError:
            failed.append((filename, "not found"))
        except ValueError:
            failed.append((filename, "invalid content"))

    return loaded, failed


files = ["data_a.txt", "data_b.txt", "data_c.txt", "data_d.txt"]
data, failures = load_all_sources(files)

print("  Loaded:")
for name, value in data.items():
    print(f"    {name}: {value}")

print("  Failed (gracefully skipped):")
for name, reason in failures:
    print(f"    {name}: {reason}")

print(f"\n  System continues with {len(data)}/{len(files)} sources!")

# Cleanup
for f in ["data_a.txt", "data_c.txt"]:
    os.remove(f)

print()

# =============================
# 4. INPUT VALIDATION PATTERN
# =============================

# --- Example 5: Validate early, process later ---
print("=== Input Validation Pattern ===")
print()

def validate_order(quantity, price, customer_name):
    """Validate all inputs before processing."""
    errors = []

    if not isinstance(customer_name, str) or not customer_name.strip():
        errors.append("Customer name is required")
    if not isinstance(quantity, int) or quantity < 1:
        errors.append(f"Quantity must be a positive integer, got {quantity}")
    if not isinstance(price, (int, float)) or price <= 0:
        errors.append(f"Price must be positive, got {price}")

    if errors:
        raise ValueError("Validation failed:\n  " + "\n  ".join(errors))

    return {
        "customer": customer_name.strip(),
        "quantity": quantity,
        "price": price,
        "total": quantity * price,
    }


test_orders = [
    (5, 9.99, "Trush"),
    (-1, 9.99, "Rahul"),
    (3, 0, ""),
    (2, 15.50, "Carol"),
]

for qty, price, name in test_orders:
    try:
        order = validate_order(qty, price, name)
        print(f"  ✓ Order: {order['customer']} — {order['quantity']}x ${order['price']:.2f} = ${order['total']:.2f}")
    except ValueError as e:
        print(f"  ✗ {e}")
    print()

# =============================
# 5. LBYL vs EAFP
# =============================

# --- Example 6: Comparing both approaches ---
print("=== LBYL vs EAFP ===")
print()

data = {"users": {"trush": {"age": 21}, "rahul": {"age": 25}}}

# LBYL — Look Before You Leap
print("  LBYL approach:")
username = "charlie"
if "users" in data:
    if username in data["users"]:
        if "age" in data["users"][username]:
            print(f"    {username}'s age: {data['users'][username]['age']}")
        else:
            print(f"    {username}: age not found")
    else:
        print(f"    {username}: user not found")

print()

# EAFP — Easier to Ask Forgiveness than Permission (Pythonic!)
print("  EAFP approach:")
try:
    age = data["users"][username]["age"]
    print(f"    {username}'s age: {age}")
except KeyError:
    print(f"    {username}: not found")

print()

# With existing user
print("  EAFP with existing user:")
try:
    age = data["users"]["trush"]["age"]
    print(f"    trush's age: {age}")
except KeyError:
    print(f"    trush: not found")

print()

# =============================
# 6. PRACTICAL: ROBUST DATA PIPELINE
# =============================

# --- Example 7: Complete pipeline with all patterns ---
print("=== Robust Data Pipeline ===")
print()

def read_data_file(filename):
    """Step 1: Read raw data with retry."""
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return None


def parse_records(lines):
    """Step 2: Parse lines into records, skip bad ones."""
    records = []
    errors = []

    for i, line in enumerate(lines, 1):
        parts = line.strip().split(",")
        if len(parts) != 3:
            errors.append(f"Line {i}: wrong format")
            continue

        name = parts[0].strip()
        try:
            score = int(parts[1].strip())
            max_score = int(parts[2].strip())
        except ValueError:
            errors.append(f"Line {i}: invalid numbers")
            continue

        records.append({"name": name, "score": score, "max": max_score})

    return records, errors


def calculate_results(records):
    """Step 3: Calculate percentages, handle division errors."""
    results = []

    for record in records:
        try:
            percentage = (record["score"] / record["max"]) * 100
            results.append({
                "name": record["name"],
                "percentage": round(percentage, 1),
                "grade": "Pass" if percentage >= 60 else "Fail",
            })
        except ZeroDivisionError:
            results.append({
                "name": record["name"],
                "percentage": 0,
                "grade": "Error: max_score is 0",
            })

    return results


def generate_report(results, parse_errors):
    """Step 4: Generate final report."""
    print("  ╔══════════════════════════════════════╗")
    print("  ║         STUDENT REPORT CARD          ║")
    print("  ╠══════════════════════════════════════╣")

    for r in results:
        status = r["grade"]
        print(f"  ║  {r['name']:<12} {r['percentage']:>6.1f}%  {status:<10}  ║")

    print("  ╠══════════════════════════════════════╣")
    print(f"  ║  Processed: {len(results):<3}  Errors: {len(parse_errors):<3}          ║")
    print("  ╚══════════════════════════════════════╝")

    if parse_errors:
        print()
        print("  Parse Warnings:")
        for err in parse_errors:
            print(f"    ⚠ {err}")


# Create test data
with open("pipeline_data.csv", "w") as f:
    f.write("Trush,90,100\n")
    f.write("Rahul,75,100\n")
    f.write("Carol,bad,100\n")
    f.write("Dave,50,100\n")
    f.write("Eve,80,0\n")
    f.write("bad line\n")
    f.write("Frank,95,100\n")

# Run the pipeline
print("  Running pipeline...")
print()

lines = read_data_file("pipeline_data.csv")
if lines is None:
    print("  Pipeline aborted: data file not found")
else:
    records, parse_errors = parse_records(lines)
    results = calculate_results(records)
    generate_report(results, parse_errors)

# Cleanup
os.remove("pipeline_data.csv")

# ============================================
# TRY IT YOURSELF:
# 1. Add a retry mechanism to a file reading function
# 2. Build a validator that collects all errors before raising
# 3. Create a data pipeline with graceful degradation
# ============================================
