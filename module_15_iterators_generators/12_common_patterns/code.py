# ============================================
# MODULE 15 - SUBTOPIC 12: Common Patterns
# ============================================

# Real-world iterator/generator patterns
# used in engineering-level code.

import itertools

# =============================
# 1. INFINITE SEQUENCES
# =============================

print("=== Infinite Sequences ===")
print()

def fibonacci():
    """Infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take first 15
fibs = list(itertools.islice(fibonacci(), 15))
print(f"  First 15 Fibonacci: {fibs}")
print()

def primes():
    """Infinite prime number generator."""
    yield 2
    candidate = 3
    while True:
        is_prime = True
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            yield candidate
        candidate += 2

first_primes = list(itertools.islice(primes(), 15))
print(f"  First 15 primes: {first_primes}")
print()

# =============================
# 2. DATA PIPELINE
# =============================

print("=== Data Pipeline ===")
print()

# Simulate raw data
raw_records = [
    "  Trush, 95  ",
    "  Rahul, invalid  ",
    "  Charlie, 87  ",
    "  , 100  ",
    "  Diana, 92  ",
    "  Eve, -5  ",
    "  Frank, 78  ",
]

# Step 1: Clean
def clean(records):
    for record in records:
        yield record.strip()

# Step 2: Parse
def parse(records):
    for record in records:
        parts = record.split(",")
        if len(parts) == 2:
            name = parts[0].strip()
            score_str = parts[1].strip()
            try:
                score = int(score_str)
                yield {"name": name, "score": score}
            except ValueError:
                continue   # skip invalid scores

# Step 3: Validate
def validate(records):
    for record in records:
        if record["name"] and 0 <= record["score"] <= 100:
            yield record

# Step 4: Transform
def add_grade(records):
    for record in records:
        score = record["score"]
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "D"
        record["grade"] = grade
        yield record

# Build pipeline
pipeline = add_grade(validate(parse(clean(raw_records))))

print("  Pipeline: clean → parse → validate → grade")
print("  Results:")
for student in pipeline:
    print(f"    {student['name']:10s} score={student['score']} grade={student['grade']}")
print()

# =============================
# 3. BATCHING
# =============================

print("=== Batching ===")
print()

def batches(iterable, size):
    """Group items into fixed-size batches."""
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:   # yield remaining items
        yield batch

data = list(range(1, 18))
print(f"  Data: {data}")
print(f"  Batches of 5:")
for batch in batches(data, 5):
    print(f"    {batch}")
print()

# =============================
# 4. SLIDING WINDOW
# =============================

print("=== Sliding Window ===")
print()

def sliding_window(iterable, size):
    """Yield overlapping windows of fixed size."""
    from collections import deque
    window = deque(maxlen=size)
    for item in iterable:
        window.append(item)
        if len(window) == size:
            yield list(window)

temps = [20, 22, 19, 23, 25, 21, 24, 26, 22]
print(f"  Temperatures: {temps}")
print(f"  3-day moving windows:")
for window in sliding_window(temps, 3):
    avg = sum(window) / len(window)
    print(f"    {window} → avg = {avg:.1f}")
print()

# =============================
# 5. FLATTENING NESTED DATA
# =============================

print("=== Flattening ===")
print()

def flatten(nested):
    """Flatten arbitrarily nested lists."""
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3], [4, [5, 6]], [7, [8, [9]]]]
print(f"  Nested: {nested}")
print(f"  Flat:   {list(flatten(nested))}")
print()

# =============================
# 6. UNIQUE ITEMS (ORDER PRESERVED)
# =============================

print("=== Unique Items (Ordered) ===")
print()

def unique(iterable):
    """Yield unique items preserving order."""
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"  Input:  {data}")
print(f"  Unique: {list(unique(data))}")
print()

# =============================
# 7. PAIRWISE ITERATION
# =============================

print("=== Pairwise Iteration ===")
print()

def pairwise(iterable):
    """Yield consecutive pairs: (a,b), (b,c), (c,d)..."""
    it = iter(iterable)
    prev = next(it)
    for current in it:
        yield prev, current
        prev = current

data = [10, 20, 15, 30, 25]
print(f"  Data: {data}")
print(f"  Consecutive differences:")
for a, b in pairwise(data):
    diff = b - a
    direction = "↑" if diff > 0 else "↓"
    print(f"    {a} → {b}: {direction} {abs(diff)}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create an infinite sequence of triangle numbers
# 2. Build a pipeline that processes a list of strings
# 3. Create a batching generator for database inserts
# ============================================
