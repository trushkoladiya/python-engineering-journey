# ============================================
# MODULE 16 - SUBTOPIC 11: Immutability in Practice
# ============================================

# Immutability = data that can't change after creation.
# Functional programming prefers creating NEW data over modifying existing data.

# =============================
# 1. THE MUTATION PROBLEM
# =============================

print("=== The Mutation Problem ===")
print()

# Dangerous: function modifies the original list!
def add_item_bad(items, item):
    """This MODIFIES the original list — side effect!"""
    items.append(item)
    return items

original = [1, 2, 3]
result = add_item_bad(original, 4)
print(f"  original after add_item_bad: {original}")   # [1, 2, 3, 4] — CHANGED!
print(f"  result: {result}")
print(f"  original is result: {original is result}")   # True — same object!
print()

# Safe: function creates a NEW list
def add_item_safe(items, item):
    """This creates a NEW list — no side effect."""
    return items + [item]

original2 = [1, 2, 3]
result2 = add_item_safe(original2, 4)
print(f"  original after add_item_safe: {original2}")  # [1, 2, 3] — unchanged!
print(f"  result: {result2}")
print(f"  original is result: {original2 is result2}")  # False — different objects
print()

# =============================
# 2. TUPLES INSTEAD OF LISTS
# =============================

print("=== Tuples for Immutability ===")
print()

# Use tuples when data shouldn't change
point = (3, 5)
print(f"  point: {point}")

# Can't modify a tuple
try:
    point[0] = 10
except TypeError as e:
    print(f"  Can't modify tuple: {e}")

# Create a NEW tuple instead
new_point = (10, point[1])
print(f"  new_point: {new_point}")
print(f"  original point: {point}")   # unchanged
print()

# Tuple unpacking for "updates"
x, y = point
updated = (x + 1, y + 1)
print(f"  Shifted point: {updated}")
print()

# =============================
# 3. FROZENSET
# =============================

print("=== Frozenset — Immutable Set ===")
print()

# Regular set — mutable
mutable_tags = {"python", "code", "tutorial"}
mutable_tags.add("new")
print(f"  Mutable set after add: {mutable_tags}")

# Frozenset — immutable
frozen_tags = frozenset({"python", "code", "tutorial"})
print(f"  Frozenset: {frozen_tags}")

try:
    frozen_tags.add("new")
except AttributeError as e:
    print(f"  Can't modify frozenset: {e}")

# Create new frozenset with added element
new_tags = frozen_tags | frozenset({"new"})
print(f"  Original frozenset: {frozen_tags}")
print(f"  New frozenset: {new_tags}")
print()

# Frozensets can be dictionary keys (mutable sets can't!)
permissions = {
    frozenset({"read"}): "Viewer",
    frozenset({"read", "write"}): "Editor",
    frozenset({"read", "write", "admin"}): "Admin",
}
user_perms = frozenset({"read", "write"})
print(f"  Role: {permissions[user_perms]}")
print()

# =============================
# 4. IMMUTABLE DICTIONARY UPDATES
# =============================

print("=== Immutable Dictionary Updates ===")
print()

# Mutable approach — modifies in place
person = {"name": "Trush", "age": 21}
person["age"] = 31   # mutates!
print(f"  Mutable update: {person}")

# Immutable approach — create new dict
person = {"name": "Trush", "age": 21}
updated_person = {**person, "age": 31}
print(f"  Original: {person}")
print(f"  Updated:  {updated_person}")
print()

# Adding new keys immutably
with_city = {**person, "city": "NYC"}
print(f"  With city: {with_city}")
print(f"  Original still: {person}")
print()

# =============================
# 5. FUNCTIONAL LIST OPERATIONS
# =============================

print("=== Functional List Operations ===")
print()

data = [5, 3, 8, 1, 9, 2, 7]

# Instead of data.sort() — use sorted()
sorted_data = sorted(data)
print(f"  Original: {data}")
print(f"  Sorted (new): {sorted_data}")

# Instead of data.reverse() — use reversed()
reversed_data = list(reversed(data))
print(f"  Reversed (new): {reversed_data}")
print(f"  Original still: {data}")
print()

# Instead of data.append(x) — use concatenation
with_new = data + [10]
print(f"  With 10 appended (new): {with_new}")
print(f"  Original still: {data}")
print()

# =============================
# 6. FUNCTIONAL DATA PROCESSING
# =============================

print("=== Functional Data Processing ===")
print()

# Process without mutating original
records = [
    {"name": "Trush", "score": 85},
    {"name": "Rahul", "score": 92},
    {"name": "Eve", "score": 78},
]

# Add grades WITHOUT modifying original records
def add_grade(record):
    """Return a NEW record with a grade added."""
    grade = "A" if record["score"] >= 90 else ("B" if record["score"] >= 80 else "C")
    return {**record, "grade": grade}

graded = list(map(add_grade, records))

print("  Original records:")
for r in records:
    print(f"    {r}")
print()
print("  Graded records (new):")
for r in graded:
    print(f"    {r}")
print()

# =============================
# 7. BUILDING UP DATA FUNCTIONALLY
# =============================

print("=== Building Data Functionally ===")
print()

from functools import reduce

# Build a configuration dict step by step
defaults = {"theme": "light", "language": "en", "font_size": 14}
user_prefs = {"theme": "dark", "font_size": 16}
overrides = {"debug": True}

# Merge immutably using reduce
configs = [defaults, user_prefs, overrides]
final_config = reduce(lambda a, b: {**a, **b}, configs)

print(f"  Defaults:   {defaults}")
print(f"  User prefs: {user_prefs}")
print(f"  Overrides:  {overrides}")
print(f"  Final:      {final_config}")
print()

# =============================
# 8. NAMED TUPLES FOR IMMUTABLE RECORDS
# =============================

print("=== Named Tuples for Immutable Records ===")
print()

from collections import namedtuple

# Define an immutable record type
Point = namedtuple("Point", ["x", "y"])

p = Point(3, 5)
print(f"  Point: {p}")
print(f"  x={p.x}, y={p.y}")

# Can't modify!
try:
    p.x = 10
except AttributeError as e:
    print(f"  Can't modify: {e}")

# Create a new point with _replace
moved = p._replace(x=10)
print(f"  Original: {p}")
print(f"  Moved: {moved}")
print()

# =============================
# 9. COMPARING APPROACHES
# =============================

print("=== Mutable vs Immutable Summary ===")
print()

print("  MUTABLE (Imperative):")
print("    list.append(x)      — modifies in place")
print("    dict[key] = value   — modifies in place")
print("    list.sort()         — modifies in place")
print()
print("  IMMUTABLE (Functional):")
print("    list + [x]          — creates new list")
print("    {**dict, key: val}  — creates new dict")
print("    sorted(list)        — creates new list")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a function that "updates" a tuple-based record
#    by creating a new tuple
# 2. Process a list of dicts without modifying originals
# 3. Build a config system using immutable dict merging
# ============================================
