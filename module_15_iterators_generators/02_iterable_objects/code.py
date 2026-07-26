# ============================================
# MODULE 15 - SUBTOPIC 2: Iterable Objects
# ============================================

# Python has many built-in iterable types.
# Let's explore each one.

# =============================
# 1. LISTS ARE ITERABLE
# =============================

print("=== Lists ===")
print()

fruits = ["apple", "banana", "cherry"]
it = iter(fruits)

print(f"  List: {fruits}")
print(f"  next() = '{next(it)}'")
print(f"  next() = '{next(it)}'")
print(f"  next() = '{next(it)}'")
print()

# =============================
# 2. STRINGS ARE ITERABLE
# =============================

print("=== Strings ===")
print()

word = "Python"
it = iter(word)

print(f"  String: '{word}'")
print(f"  Characters: ", end="")
for ch in word:
    print(f"'{ch}' ", end="")
print()
print()

# =============================
# 3. TUPLES ARE ITERABLE
# =============================

print("=== Tuples ===")
print()

coords = (10, 20, 30)
it = iter(coords)

print(f"  Tuple: {coords}")
print(f"  next() = {next(it)}")
print(f"  next() = {next(it)}")
print(f"  next() = {next(it)}")
print()

# =============================
# 4. SETS ARE ITERABLE
# =============================

print("=== Sets ===")
print()

colors = {"red", "green", "blue"}
print(f"  Set: {colors}")
print(f"  Items (order may vary):")
for color in colors:
    print(f"    {color}")
print()

# =============================
# 5. DICTIONARIES ARE ITERABLE
# =============================

print("=== Dictionaries ===")
print()

person = {"name": "Trush", "age": 21, "city": "NYC"}

# Default: iterates over KEYS
print("  Iterating over keys (default):")
for key in person:
    print(f"    {key}")
print()

# Iterating over values
print("  Iterating over values:")
for val in person.values():
    print(f"    {val}")
print()

# Iterating over key-value pairs
print("  Iterating over items (key, value):")
for key, val in person.items():
    print(f"    {key} = {val}")
print()

# =============================
# 6. RANGE IS ITERABLE
# =============================

print("=== Range ===")
print()

r = range(5)
it = iter(r)

print(f"  range(5) is iterable:")
print(f"  next() = {next(it)}")
print(f"  next() = {next(it)}")
print(f"  next() = {next(it)}")
print()

# Range can be iterated multiple times (unlike iterators!)
print("  Range can be iterated multiple times:")
for i in r:
    print(f"    {i}", end=" ")
print()
for i in r:
    print(f"    {i}", end=" ")
print()
print()

# =============================
# 7. CHECKING ITERABILITY
# =============================

print("=== Checking Iterability ===")
print()

# Method 1: Try iter()
def check_iterable(obj, name):
    try:
        iter(obj)
        return f"  {name:15s} → ✅ Iterable"
    except TypeError:
        return f"  {name:15s} → ❌ Not iterable"

objects = [
    ([1, 2, 3], "list"),
    ((1, 2), "tuple"),
    ("hello", "string"),
    ({1, 2}, "set"),
    ({"a": 1}, "dict"),
    (range(5), "range"),
    (42, "int"),
    (3.14, "float"),
    (True, "bool"),
    (None, "None"),
]

for obj, name in objects:
    print(check_iterable(obj, name))
print()

# Method 2: hasattr check
print("  Using hasattr('__iter__'):")
print(f"    [1,2,3] has __iter__? {hasattr([1,2,3], '__iter__')}")
print(f"    42 has __iter__?      {hasattr(42, '__iter__')}")
print(f"    'hi' has __iter__?    {hasattr('hi', '__iter__')}")
print()

# =============================
# 8. ITERABLE vs ITERATOR DISTINCTION
# =============================

print("=== Iterable vs Iterator ===")
print()

my_list = [10, 20, 30]

# The LIST is the iterable
# The ITERATOR is what you get from iter()
iterator1 = iter(my_list)
iterator2 = iter(my_list)

print(f"  Same list, two different iterators:")
print(f"  iterator1: next() = {next(iterator1)}")
print(f"  iterator2: next() = {next(iterator2)}")
print(f"  iterator1: next() = {next(iterator1)}")
print(f"  iterator2: next() = {next(iterator2)}")
print()

# Each iterator has its OWN position
print("  → Each iterator tracks its own position!")
print("  → The iterable (list) stays unchanged")
print()

# An iterator IS also iterable (iter() on an iterator returns itself)
it = iter([1, 2, 3])
print(f"  iter(iterator) is iterator: {iter(it) is it}")
print("  → An iterator returns itself from iter()")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create iterators from a tuple and a set
# 2. Iterate over a dict using .items()
# 3. Check if range(10) is iterable using both methods
# ============================================
