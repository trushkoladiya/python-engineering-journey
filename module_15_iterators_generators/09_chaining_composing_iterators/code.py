# ============================================
# MODULE 15 - SUBTOPIC 9: Chaining & Composing Iterators
# ============================================

# Combine multiple iterators to build
# powerful data processing pipelines.

# =============================
# 1. MANUAL CHAINING
# =============================

print("=== Manual Chaining ===")
print()

def chain_manual(*iterables):
    """Yield items from multiple iterables in sequence."""
    for iterable in iterables:
        for item in iterable:
            yield item

result = list(chain_manual([1, 2, 3], [4, 5], [6, 7, 8, 9]))
print(f"  chain([1,2,3], [4,5], [6,7,8,9]) = {result}")

# Mix different types
mixed = list(chain_manual("AB", [10, 20], (True, False)))
print(f"  chain('AB', [10,20], (True,False)) = {mixed}")
print()

# =============================
# 2. yield from — CLEANER CHAINING
# =============================

print("=== yield from ===")
print()

# yield from delegates to a sub-iterator
def chain_elegant(*iterables):
    """Same as above, but using yield from."""
    for iterable in iterables:
        yield from iterable    # replaces the inner for loop!

result = list(chain_elegant([1, 2], "abc", range(3)))
print(f"  yield from result: {result}")
print()

# --- Compare the two approaches ---
print("  Without yield from:")
print("    for item in iterable:")
print("        yield item")
print()
print("  With yield from:")
print("    yield from iterable")
print("  → Same result, cleaner code!")
print()

# =============================
# 3. yield from WITH GENERATORS
# =============================

print("=== yield from with Generators ===")
print()

def evens(n):
    for i in range(0, n, 2):
        yield i

def odds(n):
    for i in range(1, n, 2):
        yield i

def all_numbers(n):
    """Combine evens and odds using yield from."""
    yield from evens(n)
    yield from odds(n)

print(f"  evens(8): {list(evens(8))}")
print(f"  odds(8):  {list(odds(8))}")
print(f"  all_numbers(8): {list(all_numbers(8))}")
print()

# =============================
# 4. COMPOSING: PIPELINE PATTERN
# =============================

print("=== Composing: Pipeline Pattern ===")
print()

# Step 1: Generate data
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Step 2: Filter
def only_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

# Step 3: Transform
def square(numbers):
    for n in numbers:
        yield n ** 2

# Step 4: Limit
def take(iterable, count):
    for i, item in enumerate(iterable):
        if i >= count:
            return
        yield item

# Build the pipeline: generate → filter → transform → limit
pipeline = take(square(only_even(generate_numbers(20))), 5)
result = list(pipeline)
print(f"  Pipeline: generate(20) → even → square → take(5)")
print(f"  Result: {result}")
print()

# =============================
# 5. itertools MODULE (INTRO)
# =============================

print("=== itertools Module ===")
print()

import itertools

# chain — combine iterables
chained = list(itertools.chain([1, 2], [3, 4], [5, 6]))
print(f"  itertools.chain: {chained}")

# islice — slice an iterator (like list slicing but for iterators)
sliced = list(itertools.islice(range(100), 5))
print(f"  itertools.islice(range(100), 5): {sliced}")

# More islice: start, stop, step
sliced2 = list(itertools.islice(range(100), 10, 20, 3))
print(f"  itertools.islice(range(100), 10, 20, 3): {sliced2}")
print()

# =============================
# 6. itertools — MORE TOOLS
# =============================

print("=== More itertools ===")
print()

# count — infinite counter
counter = itertools.count(10, 5)   # start=10, step=5
first_five = [next(counter) for _ in range(5)]
print(f"  count(10, step=5): {first_five}")

# cycle — infinite cycling
cycler = itertools.cycle(["A", "B", "C"])
cycled = [next(cycler) for _ in range(7)]
print(f"  cycle(['A','B','C']): {cycled}")

# repeat — repeat a value
repeated = list(itertools.repeat("hello", 3))
print(f"  repeat('hello', 3): {repeated}")

# takewhile — take while condition is true
data = [2, 4, 6, 7, 8, 10]
taken = list(itertools.takewhile(lambda x: x % 2 == 0, data))
print(f"  takewhile(even, {data}): {taken}")

# dropwhile — skip while condition is true
dropped = list(itertools.dropwhile(lambda x: x < 5, [1, 3, 5, 2, 7]))
print(f"  dropwhile(<5, [1,3,5,2,7]): {dropped}")
print()

# =============================
# 7. itertools — COMBINATIONS & PERMUTATIONS
# =============================

print("=== Combinations & Permutations ===")
print()

# product — cartesian product
pairs = list(itertools.product("AB", [1, 2]))
print(f"  product('AB', [1,2]): {pairs}")

# permutations
perms = list(itertools.permutations("ABC", 2))
print(f"  permutations('ABC', 2): {perms}")

# combinations
combos = list(itertools.combinations([1, 2, 3, 4], 2))
print(f"  combinations([1,2,3,4], 2): {combos}")
print()

# =============================
# 8. BUILDING A DATA PIPELINE
# =============================

print("=== Real-World Pipeline ===")
print()

# Simulate processing log entries
log_entries = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "INFO: Page loaded",
    "WARNING: Slow query detected",
    "ERROR: Timeout on request",
    "INFO: User logged out",
    "ERROR: File not found",
]

# Pipeline: filter errors → extract messages → uppercase
def filter_level(entries, level):
    for entry in entries:
        if entry.startswith(level):
            yield entry

def extract_message(entries):
    for entry in entries:
        yield entry.split(": ", 1)[1]

def uppercase(items):
    for item in items:
        yield item.upper()

# Compose the pipeline
errors = uppercase(extract_message(filter_level(log_entries, "ERROR")))

print("  Error messages (uppercase):")
for msg in errors:
    print(f"    {msg}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use yield from to combine three generators
# 2. Build a pipeline: generate → filter → transform
# 3. Use itertools.chain and itertools.islice
# ============================================
