# ============================================
# MODULE 15 - SUBTOPIC 3: Iterator Protocol
# ============================================

# The iterator protocol is based on two methods:
#   __iter__() — return the iterator
#   __next__() — return the next item

# =============================
# 1. THE PROTOCOL IN ACTION
# =============================

print("=== Iterator Protocol ===")
print()

my_list = [10, 20, 30]

# iter() calls __iter__()
it = iter(my_list)
print(f"  iter({my_list}) = {it}")
print()

# next() calls __next__()
print(f"  next(it) = {next(it)}")   # 10
print(f"  next(it) = {next(it)}")   # 20
print(f"  next(it) = {next(it)}")   # 30
print()

# StopIteration when exhausted
try:
    next(it)
except StopIteration:
    print("  next(it) → StopIteration raised!")
print()

# =============================
# 2. CALLING DUNDER METHODS DIRECTLY
# =============================

print("=== Calling __iter__ and __next__ Directly ===")
print()

# These are equivalent:
data = [100, 200, 300]

# Using built-in functions (preferred)
it1 = iter(data)
print(f"  iter(data):    next() = {next(it1)}")

# Using dunder methods directly (same thing)
it2 = data.__iter__()
print(f"  __iter__():    __next__() = {it2.__next__()}")
print()

print("  → iter() is just a wrapper for __iter__()")
print("  → next() is just a wrapper for __next__()")
print()

# =============================
# 3. StopIteration EXCEPTION
# =============================

print("=== StopIteration Exception ===")
print()

# StopIteration is a normal exception
short_list = [42]
it = iter(short_list)

print(f"  List has 1 item: {short_list}")
print(f"  First next():  {next(it)}")

try:
    value = next(it)
    print(f"  Second next(): {value}")
except StopIteration:
    print("  Second next(): StopIteration! (list exhausted)")
print()

# StopIteration is how for loops know to stop
print("  How for loop uses StopIteration:")
print("    1. Call iter() to get iterator")
print("    2. Call next() in a loop")
print("    3. When StopIteration → break")
print()

# =============================
# 4. SIMULATING A FOR LOOP
# =============================

print("=== Simulating a for Loop ===")
print()

colors = ["red", "green", "blue"]

# This for loop:
print("  for loop:")
for color in colors:
    print(f"    {color}")
print()

# Is equivalent to this:
print("  Manual simulation:")
iterator = iter(colors)
while True:
    try:
        color = next(iterator)
        print(f"    {color}")
    except StopIteration:
        break
print()

# =============================
# 5. ITERATOR RETURNS ITSELF
# =============================

print("=== Iterator Returns Itself ===")
print()

my_list = [1, 2, 3]
it = iter(my_list)

# An iterator's __iter__() returns itself
print(f"  iter(iterator) is iterator: {iter(it) is it}")
print(f"  This means iterators are also iterable!")
print()

# This is why you can use an iterator in a for loop:
it = iter([10, 20, 30])
next(it)   # skip first item

print("  Using iterator in for loop (skipped first):")
for item in it:    # for calls iter(it) which returns it
    print(f"    {item}")
print()

# =============================
# 6. MULTIPLE ITERATORS FROM SAME ITERABLE
# =============================

print("=== Multiple Iterators ===")
print()

data = [1, 2, 3, 4, 5]

# Create two independent iterators
it_a = iter(data)
it_b = iter(data)

print(f"  Iterator A: next() = {next(it_a)}")   # 1
print(f"  Iterator A: next() = {next(it_a)}")   # 2
print(f"  Iterator B: next() = {next(it_b)}")   # 1 (independent!)
print(f"  Iterator A: next() = {next(it_a)}")   # 3
print(f"  Iterator B: next() = {next(it_b)}")   # 2
print()
print("  → Each iterator has its own position")
print()

# =============================
# 7. PROTOCOL WITH DIFFERENT TYPES
# =============================

print("=== Protocol Works Everywhere ===")
print()

# Every iterable follows the same protocol

# String
s_it = iter("AB")
print(f"  String: {next(s_it)}, {next(s_it)}")

# Dict
d_it = iter({"x": 1, "y": 2})
print(f"  Dict keys: {next(d_it)}, {next(d_it)}")

# Range
r_it = iter(range(3))
print(f"  Range: {next(r_it)}, {next(r_it)}, {next(r_it)}")

# Set
set_it = iter({100, 200})
print(f"  Set: {next(set_it)}, {next(set_it)}")
print()

print("  → Same protocol (__iter__ + __next__) for all types!")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Manually iterate over "Hello" using iter() and next()
# 2. Simulate a for loop over range(5) using while + next()
# 3. Create two iterators from the same list — verify independence
# ============================================
