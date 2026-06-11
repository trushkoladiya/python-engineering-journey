# ============================================
# MODULE 15 - SUBTOPIC 13: Debugging Iterators & Generators
# ============================================

# Common pitfalls and how to avoid them.

# =============================
# 1. BUG: EXHAUSTED ITERATOR
# =============================

print("=== Bug #1: Exhausted Iterator ===")
print()

# The most common generator bug!
gen = (x ** 2 for x in range(5))

# First use — works fine
result1 = list(gen)
print(f"  First list(gen): {result1}")

# Second use — EMPTY! Generator is exhausted.
result2 = list(gen)
print(f"  Second list(gen): {result2}")
print("  → Generator was exhausted after first use!")
print()

# FIX: Create a new generator each time
print("  Fix: create new generator for each use:")
result_a = list(x ** 2 for x in range(5))
result_b = list(x ** 2 for x in range(5))
print(f"  First:  {result_a}")
print(f"  Second: {result_b}")
print()

# =============================
# 2. BUG: ACCIDENTAL EXHAUSTION
# =============================

print("=== Bug #2: Accidental Exhaustion ===")
print()

def get_numbers():
    yield 10
    yield 20
    yield 30

# BUG: printing the generator eats it
gen = get_numbers()
print(f"  Debug print: {list(gen)}")   # [10, 20, 30]

# Now the for loop gets nothing!
print("  Trying to iterate:")
count = 0
for num in gen:
    count += 1
    print(f"    {num}")
print(f"  Items found: {count}")
print("  → Zero! The debug print exhausted the generator.")
print()

# FIX: convert to list first, then use the list
print("  Fix: store as list first:")
data = list(get_numbers())
print(f"  Debug: {data}")
for num in data:
    print(f"    {num}")
print()

# =============================
# 3. BUG: FUNCTION vs GENERATOR OBJECT
# =============================

print("=== Bug #3: Function vs Generator Object ===")
print()

def count_to(n):
    for i in range(1, n + 1):
        yield i

# WRONG: assigning the function itself
wrong = count_to
print(f"  wrong = count_to → type: {type(wrong)}")
print(f"  This is the FUNCTION, not a generator!")
print()

# RIGHT: calling the function to create a generator
right = count_to(5)
print(f"  right = count_to(5) → type: {type(right)}")
print(f"  Values: {list(right)}")
print()

# =============================
# 4. BUG: MODIFYING WHILE ITERATING
# =============================

print("=== Bug #4: Modifying While Iterating ===")
print()

# WRONG: removing items during iteration
numbers = [1, 2, 3, 4, 5, 6]
print(f"  Original: {numbers}")
print(f"  Trying to remove even numbers during iteration:")

# This creates subtle bugs — items get skipped!
bad_list = [1, 2, 3, 4, 5, 6]
for num in bad_list:
    if num % 2 == 0:
        bad_list.remove(num)

print(f"  Result (buggy): {bad_list}")
print("  → 4 was skipped!")
print()

# FIX 1: iterate over a copy
print("  Fix 1 — iterate over copy:")
good_list = [1, 2, 3, 4, 5, 6]
for num in good_list[:]:    # [:] makes a copy
    if num % 2 == 0:
        good_list.remove(num)
print(f"  Result: {good_list}")
print()

# FIX 2: use a generator to filter (best approach)
print("  Fix 2 — use generator filter:")
original = [1, 2, 3, 4, 5, 6]
odds_only = [x for x in original if x % 2 != 0]
print(f"  Result: {odds_only}")
print()

# =============================
# 5. BUG: SHARED ITERATOR
# =============================

print("=== Bug #5: Shared Iterator ===")
print()

# WRONG: using same iterator in nested loops
numbers = iter(range(6))

print("  Trying nested loops with SAME iterator:")
for a in numbers:
    for b in numbers:
        print(f"    a={a}, b={b}")
# Not what you expected! The inner loop consumes the iterator.
print("  → Inner loop consumed the shared iterator!")
print()

# FIX: use the iterable (list), not an iterator
print("  Fix — use list (iterable), not iterator:")
numbers_list = list(range(4))
for a in numbers_list:
    for b in numbers_list:
        print(f"    a={a}, b={b}", end="  ")
    print()
print()

# =============================
# 6. BUG: GENERATOR RETURN VALUE
# =============================

print("=== Bug #6: Generator Return Value ===")
print()

# A generator function ALWAYS returns a generator object
# Even if it looks like a normal function!

def maybe_generator(use_yield):
    if use_yield:
        yield 42
    else:
        return 42   # this does NOT return 42 to the caller!

# When yield is present, it's ALWAYS a generator
result = maybe_generator(True)
print(f"  maybe_generator(True): {result}")
print(f"  Type: {type(result)}")
print(f"  Value: {list(result)}")
print()

result = maybe_generator(False)
print(f"  maybe_generator(False): {result}")
print(f"  Type: {type(result)}")
print(f"  Value: {list(result)}")
print("  → Even with 'return 42', it returns a generator (empty one)!")
print()

# =============================
# 7. DEBUGGING TIP: PEEK WITHOUT CONSUMING
# =============================

print("=== Debugging Tip: Peek at a Generator ===")
print()

import itertools

def peek_generator(gen, n=3):
    """Peek at first N items without fully consuming the generator."""
    # Take first N items
    peeked = list(itertools.islice(gen, n))
    # Chain them back with the rest
    restored = itertools.chain(peeked, gen)
    return peeked, restored

gen = (x ** 2 for x in range(10))

# Peek at first 3
peeked, gen = peek_generator(gen, 3)
print(f"  Peeked: {peeked}")

# Continue consuming the rest
remaining = list(gen)
print(f"  Remaining: {remaining}")
print("  → Peeked items + remaining = full sequence!")
print()

# =============================
# 8. DEBUGGING CHECKLIST
# =============================

print("=== Debugging Checklist ===")
print()

print("  When a generator gives unexpected results, check:")
print()
print("  1. ❓ Is it exhausted? (used twice?)")
print("  2. ❓ Did a debug print consume it?")
print("  3. ❓ Are you calling the function? gen() not gen")
print("  4. ❓ Are you modifying data while iterating?")
print("  5. ❓ Are two loops sharing one iterator?")
print("  6. ❓ Is yield present? (makes it a generator)")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a generator, exhaust it, then try to use it again
# 2. Reproduce the "modify while iterating" bug
# 3. Use itertools.islice to peek at a generator
# ============================================
