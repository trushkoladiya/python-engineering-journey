# ============================================
# MODULE 15 - SUBTOPIC 10: Lazy Evaluation Patterns
# ============================================

# Lazy evaluation = compute values only when needed.
# Generators enable this naturally.

import os
import tempfile

# =============================
# 1. EAGER vs LAZY
# =============================

print("=== Eager vs Lazy ===")
print()

# EAGER: compute everything upfront
eager = [x ** 2 for x in range(10)]
print(f"  Eager (list): {eager}")
print(f"  Type: {type(eager)}")
print(f"  All values computed immediately!")
print()

# LAZY: compute one at a time
lazy = (x ** 2 for x in range(10))
print(f"  Lazy (generator): {lazy}")
print(f"  Type: {type(lazy)}")
print(f"  Values computed on demand!")
print()

# =============================
# 2. EARLY STOPPING
# =============================

print("=== Early Stopping ===")
print()

def expensive_computation(n):
    """Simulate an expensive operation."""
    for i in range(n):
        # Imagine each yield takes a long time
        yield i ** 2 + i * 3 + 1

# Eager: computes ALL 1000 values
all_values = [x for x in expensive_computation(1000)]

# Lazy: only computes what we need
gen = expensive_computation(1000)
first_value = next(gen)
print(f"  Lazy: only computed 1 value = {first_value}")
print(f"  (Saved computing 999 unnecessary values!)")
print()

# Find first value > 100
gen = expensive_computation(1000)
for val in gen:
    if val > 100:
        print(f"  First value > 100: {val}")
        break   # stops computing! Remaining 900+ values never computed
print()

# =============================
# 3. PROCESSING LARGE FILES
# =============================

print("=== Processing Large Files ===")
print()

# Create a sample "large" file
temp_dir = tempfile.mkdtemp()
large_file = os.path.join(temp_dir, "large_data.txt")

with open(large_file, "w") as f:
    for i in range(1000):
        level = "ERROR" if i % 100 == 0 else "INFO"
        f.write(f"{level}: Event {i} occurred\n")

# LAZY file reader — only one line in memory at a time
def read_lines(filename):
    """Lazily read lines from a file."""
    with open(filename) as f:
        for line in f:
            yield line.strip()

# LAZY filter — doesn't load entire file
def find_errors(lines):
    """Filter only error lines."""
    for line in lines:
        if line.startswith("ERROR"):
            yield line

# Process: read → filter (only errors loaded, rest skipped)
errors = list(find_errors(read_lines(large_file)))
print(f"  File has 1000 lines")
print(f"  Found {len(errors)} errors (only these were kept in memory)")
print(f"  First error: '{errors[0]}'")
print()

# =============================
# 4. STREAMING DATA PATTERN
# =============================

print("=== Streaming Data Pattern ===")
print()

def data_stream():
    """Simulate a data stream (like sensor readings)."""
    import random
    reading_id = 0
    while True:
        reading_id += 1
        value = random.uniform(20.0, 30.0)
        yield {"id": reading_id, "temp": round(value, 1)}

# Process stream — take only what we need
stream = data_stream()
print("  First 5 readings from infinite stream:")
for _ in range(5):
    reading = next(stream)
    print(f"    Reading #{reading['id']}: {reading['temp']}°C")
print()

# Filter stream for high temperatures
def high_temp_alerts(stream, threshold):
    """Yield only readings above threshold."""
    for reading in stream:
        if reading["temp"] > threshold:
            yield reading

alerts = high_temp_alerts(data_stream(), 28.0)
print("  First 3 high-temp alerts (>28°C):")
for _ in range(3):
    alert = next(alerts)
    print(f"    Alert! Reading #{alert['id']}: {alert['temp']}°C")
print()

# =============================
# 5. LAZY TRANSFORMATION PIPELINE
# =============================

print("=== Lazy Transformation Pipeline ===")
print()

# Each step processes ONE item at a time
# Memory usage stays constant regardless of data size

def numbers(n):
    """Generate numbers 1 to n."""
    for i in range(1, n + 1):
        yield i

def doubled(iterable):
    """Double each value."""
    for x in iterable:
        yield x * 2

def as_string(iterable):
    """Convert to formatted strings."""
    for x in iterable:
        yield f"[{x:>4d}]"

# Pipeline: numbers → double → format
pipeline = as_string(doubled(numbers(8)))

print("  Pipeline: numbers(8) → doubled → as_string")
print(f"  Result: {' '.join(pipeline)}")
print()

# =============================
# 6. LAZY vs EAGER — PRACTICAL CHOICE
# =============================

print("=== When to Use Lazy vs Eager ===")
print()

# Create a sample CSV-like file
csv_file = os.path.join(temp_dir, "sales.csv")
with open(csv_file, "w") as f:
    f.write("product,price,quantity\n")
    import random
    products = ["Widget", "Gadget", "Gizmo", "Doohickey"]
    for _ in range(500):
        p = random.choice(products)
        price = round(random.uniform(5.0, 50.0), 2)
        qty = random.randint(1, 20)
        f.write(f"{p},{price},{qty}\n")

# LAZY approach: process one row at a time
def parse_csv_lazy(filename):
    with open(filename) as f:
        header = next(f).strip().split(",")
        for line in f:
            values = line.strip().split(",")
            yield dict(zip(header, values))

def calculate_revenue_lazy(rows):
    for row in rows:
        revenue = float(row["price"]) * int(row["quantity"])
        yield revenue

# Calculate total revenue lazily
total = sum(calculate_revenue_lazy(parse_csv_lazy(csv_file)))
print(f"  Total revenue (lazy): ${total:,.2f}")

# Get top revenue (lazy — can stop early if needed)
gen = calculate_revenue_lazy(parse_csv_lazy(csv_file))
first_5 = [next(gen) for _ in range(5)]
print(f"  First 5 revenues: {[f'${r:.2f}' for r in first_5]}")
print()

# Cleanup
import shutil
shutil.rmtree(temp_dir)

# =============================
# 7. SUMMARY
# =============================

print("=== Lazy Evaluation Summary ===")
print()
print("  Use LAZY (generators) when:")
print("    • Data is too large for memory")
print("    • You might stop early (search, find first)")
print("    • Processing streams of data")
print("    • Building multi-step pipelines")
print()
print("  Use EAGER (lists) when:")
print("    • You need random access (indexing)")
print("    • You need to iterate multiple times")
print("    • Data is small and fits in memory")
print("    • You need len(), sorting, etc.")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a generator that reads a file line by line
# 2. Build a 3-step lazy pipeline for data processing
# 3. Compare memory usage of a list vs generator for 1M items
# ============================================
