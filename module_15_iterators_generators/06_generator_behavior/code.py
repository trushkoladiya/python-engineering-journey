# ============================================
# MODULE 15 - SUBTOPIC 6: Generator Behavior
# ============================================

# Generators pause at yield and resume on next().
# Understanding this flow is essential.

# =============================
# 1. STEP-BY-STEP EXECUTION
# =============================

print("=== Step-by-Step Execution ===")
print()

def demo_generator():
    print("    → Step 1: Before first yield")
    yield "A"
    print("    → Step 2: Between yields")
    yield "B"
    print("    → Step 3: Before last yield")
    yield "C"
    print("    → Step 4: After last yield (function ends)")

gen = demo_generator()
print("  Generator created — nothing runs yet!")
print()

print("  Calling next() #1:")
val = next(gen)
print(f"    Got: '{val}'")
print()

print("  Calling next() #2:")
val = next(gen)
print(f"    Got: '{val}'")
print()

print("  Calling next() #3:")
val = next(gen)
print(f"    Got: '{val}'")
print()

print("  Calling next() #4 (exhausted):")
try:
    next(gen)
except StopIteration:
    print("    StopIteration raised!")
print()

# =============================
# 2. STATE PRESERVATION
# =============================

print("=== State Preservation ===")
print()

def accumulator():
    """Shows that local variables survive between yields."""
    total = 0
    for i in range(1, 6):
        total += i
        yield f"Added {i}, total = {total}"

gen = accumulator()
for msg in gen:
    print(f"  {msg}")
print()

# total was preserved across all yields!

# =============================
# 3. GENERATOR EXHAUSTION
# =============================

print("=== Generator Exhaustion ===")
print()

def small_gen():
    yield "first"
    yield "second"

gen = small_gen()

# Consume all values
print(f"  next() = '{next(gen)}'")
print(f"  next() = '{next(gen)}'")

# Now it's exhausted
print(f"  Exhausted? Trying next()...")
try:
    next(gen)
except StopIteration:
    print("  StopIteration — generator is done!")
print()

# Can't restart — must create a new one
print("  Creating a new generator:")
gen2 = small_gen()
print(f"  next() = '{next(gen2)}'")
print()

# =============================
# 4. for LOOP HANDLES EXHAUSTION
# =============================

print("=== for Loop Handles Exhaustion ===")
print()

def three_items():
    yield "apple"
    yield "banana"
    yield "cherry"

# for loop automatically handles StopIteration
print("  for loop (no StopIteration error):")
for item in three_items():
    print(f"    {item}")
print()

# =============================
# 5. GENERATOR WITH COMPLEX STATE
# =============================

print("=== Complex State Tracking ===")
print()

def running_average():
    """Yields running average of numbers 1 to 10."""
    total = 0
    count = 0
    for num in range(1, 11):
        total += num
        count += 1
        avg = total / count
        yield f"After {count} numbers: sum={total}, avg={avg:.2f}"

for report in running_average():
    print(f"  {report}")
print()

# =============================
# 6. YIELDING FROM MULTIPLE SOURCES
# =============================

print("=== Yielding from Multiple Sources ===")
print()

def multi_source():
    """Yields from different data sources."""
    # From a list
    for item in [1, 2, 3]:
        yield f"list: {item}"

    # From a string
    for ch in "AB":
        yield f"string: {ch}"

    # Computed values
    for i in range(3):
        yield f"computed: {i ** 2}"

for item in multi_source():
    print(f"  {item}")
print()

# =============================
# 7. GENERATOR WITH return
# =============================

print("=== Generator with return (early exit) ===")
print()

def until_negative(numbers):
    """Yield numbers until a negative is found."""
    for n in numbers:
        if n < 0:
            return   # stops the generator (same as raising StopIteration)
        yield n

data = [5, 3, 8, -1, 9, 2]
print(f"  Data: {data}")
print(f"  until_negative: {list(until_negative(data))}")
print()

# return in a generator = StopIteration
# (return with a value sets StopIteration.value, rarely used)

# =============================
# 8. NESTED GENERATORS
# =============================

print("=== Nested Generator Calls ===")
print()

def doubles(n):
    for i in range(1, n + 1):
        yield i * 2

def triples(n):
    for i in range(1, n + 1):
        yield i * 3

def doubles_and_triples(n):
    """Yield from two other generators."""
    for val in doubles(n):
        yield f"double: {val}"
    for val in triples(n):
        yield f"triple: {val}"

print("  doubles_and_triples(3):")
for item in doubles_and_triples(3):
    print(f"    {item}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a generator that prints a message before/after each yield
# 2. Track how many values a generator has produced using internal state
# 3. Create a generator that yields until a condition is met (use return)
# ============================================
