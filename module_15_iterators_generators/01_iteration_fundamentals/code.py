# ============================================
# MODULE 15 - SUBTOPIC 1: Iteration Fundamentals
# ============================================

# You've used for loops since Module 4.
# Now let's see how iteration ACTUALLY works.

# =============================
# 1. ITERABLE vs ITERATOR
# =============================

print("=== Iterable vs Iterator ===")
print()

# An ITERABLE is something you can loop over
my_list = [10, 20, 30]
my_string = "abc"
my_tuple = (1, 2, 3)

# An ITERATOR is created FROM an iterable using iter()
my_iterator = iter(my_list)

print(f"  my_list (iterable): {my_list}")
print(f"  my_iterator: {my_iterator}")
print(f"  type(my_list): {type(my_list)}")
print(f"  type(my_iterator): {type(my_iterator)}")
print()

# =============================
# 2. USING next() TO GET ITEMS
# =============================

print("=== Using next() ===")
print()

# Create an iterator
numbers = [100, 200, 300, 400]
it = iter(numbers)

# Get items one at a time with next()
print(f"  next(it) = {next(it)}")   # 100
print(f"  next(it) = {next(it)}")   # 200
print(f"  next(it) = {next(it)}")   # 300
print(f"  next(it) = {next(it)}")   # 400
print()

# What happens when there are no more items?
try:
    next(it)
except StopIteration:
    print("  next(it) → StopIteration! (no more items)")
print()

# =============================
# 3. HOW for LOOPS ACTUALLY WORK
# =============================

print("=== How 'for' Loops Actually Work ===")
print()

# When you write this:
print("  Normal for loop:")
for x in [1, 2, 3]:
    print(f"    {x}")
print()

# Python actually does this:
print("  What Python does behind the scenes:")
iterator = iter([1, 2, 3])
while True:
    try:
        x = next(iterator)
        print(f"    {x}")
    except StopIteration:
        break
print()

# =============================
# 4. ITERATING OVER DIFFERENT TYPES
# =============================

print("=== Iterating Over Different Types ===")
print()

# --- Strings ---
string_iter = iter("Hello")
print(f"  String iterator:")
print(f"    next() = '{next(string_iter)}'")
print(f"    next() = '{next(string_iter)}'")
print(f"    next() = '{next(string_iter)}'")
print()

# --- Tuples ---
tuple_iter = iter((10, 20, 30))
print(f"  Tuple iterator:")
print(f"    next() = {next(tuple_iter)}")
print(f"    next() = {next(tuple_iter)}")
print()

# --- Sets ---
set_iter = iter({"a", "b", "c"})
print(f"  Set iterator:")
print(f"    next() = '{next(set_iter)}'")
print()

# --- Dictionaries (iterates over keys) ---
dict_iter = iter({"name": "Trush", "age": 21})
print(f"  Dict iterator (keys):")
print(f"    next() = '{next(dict_iter)}'")
print(f"    next() = '{next(dict_iter)}'")
print()

# =============================
# 5. ITERATORS ARE ONE-WAY
# =============================

print("=== Iterators Are One-Way ===")
print()

# Once you go forward, you can't go back!
it = iter([1, 2, 3])
print(f"  next(it) = {next(it)}")   # 1
print(f"  next(it) = {next(it)}")   # 2
# Can't go back to 1 — it's gone!
print(f"  next(it) = {next(it)}")   # 3
print("  → Can't rewind! Iterator moves forward only.")
print()

# To start over, create a NEW iterator
it2 = iter([1, 2, 3])
print(f"  New iterator: next() = {next(it2)}")
print("  → Create a new iterator to start over")
print()

# =============================
# 6. next() WITH DEFAULT VALUE
# =============================

print("=== next() with Default Value ===")
print()

# You can provide a default to avoid StopIteration
it = iter([10, 20])
print(f"  next(it) = {next(it)}")          # 10
print(f"  next(it) = {next(it)}")          # 20
print(f"  next(it, 'DONE') = {next(it, 'DONE')}")   # 'DONE' (no error!)
print(f"  next(it, -1) = {next(it, -1)}")            # -1
print("  → Default value prevents StopIteration error")
print()

# =============================
# 7. CHECKING IF SOMETHING IS ITERABLE
# =============================

print("=== Checking Iterability ===")
print()

def is_iterable(obj):
    """Check if an object is iterable."""
    try:
        iter(obj)
        return True
    except TypeError:
        return False

test_objects = [
    ([1, 2, 3], "list"),
    ("hello", "string"),
    (42, "integer"),
    (3.14, "float"),
    ({"a": 1}, "dict"),
    (range(5), "range"),
    (True, "bool"),
]

for obj, name in test_objects:
    print(f"  {name:10s} → iterable? {is_iterable(obj)}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create an iterator from a string and call next() 3 times
# 2. Try next() on an exhausted iterator — catch StopIteration
# 3. Use next() with a default value on an empty iterator
# ============================================
