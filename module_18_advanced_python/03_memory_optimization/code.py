# ============================================
# MODULE 18 - SUBTOPIC 3: Memory Optimization
# ============================================

# Techniques to reduce memory usage in Python programs.

import sys

# =============================
# 1. MEASURING OBJECT SIZE
# =============================

print("=== Measuring Object Size with sys.getsizeof() ===")
print()

# Basic types
print(f"  int (0):          {sys.getsizeof(0)} bytes")
print(f"  int (42):         {sys.getsizeof(42)} bytes")
print(f"  int (10**100):    {sys.getsizeof(10**100)} bytes")
print(f"  float (3.14):     {sys.getsizeof(3.14)} bytes")
print(f"  bool (True):      {sys.getsizeof(True)} bytes")
print(f"  str (''):         {sys.getsizeof('')} bytes")
print(f"  str ('hello'):    {sys.getsizeof('hello')} bytes")
print(f"  None:             {sys.getsizeof(None)} bytes")
print()

# Collections
print(f"  list []:          {sys.getsizeof([])} bytes")
print(f"  list [1,2,3]:     {sys.getsizeof([1, 2, 3])} bytes")
print(f"  tuple ():         {sys.getsizeof(())} bytes")
print(f"  tuple (1,2,3):    {sys.getsizeof((1, 2, 3))} bytes")
print(f"  dict {{}}:          {sys.getsizeof({})} bytes")
print(f"  set set():        {sys.getsizeof(set())} bytes")
print()

# =============================
# 2. LIST vs TUPLE MEMORY
# =============================

print("=== List vs Tuple Memory ===")
print()

items_list = [1, 2, 3, 4, 5]
items_tuple = (1, 2, 3, 4, 5)

print(f"  List [1..5]:  {sys.getsizeof(items_list)} bytes")
print(f"  Tuple (1..5): {sys.getsizeof(items_tuple)} bytes")
print(f"  Tuples use less memory because they are immutable")
print()

# =============================
# 3. __slots__ FOR CLASSES
# =============================

print("=== __slots__ Memory Savings ===")
print()

# Regular class — each instance gets a __dict__
class PointRegular:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Slotted class — no __dict__, fixed attributes
class PointSlotted:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

regular = PointRegular(1, 2)
slotted = PointSlotted(1, 2)

regular_size = sys.getsizeof(regular) + sys.getsizeof(regular.__dict__)
slotted_size = sys.getsizeof(slotted)

print(f"  Regular point size: {regular_size} bytes (object + __dict__)")
print(f"  Slotted point size: {slotted_size} bytes")
print(f"  Has __dict__: regular={hasattr(regular, '__dict__')}, "
      f"slotted={hasattr(slotted, '__dict__')}")
print()

# With thousands of objects, the savings add up!

# =============================
# 4. __slots__ COMPARISON AT SCALE
# =============================

print("=== __slots__ at Scale ===")
print()

# Create many regular objects
regular_objects = [PointRegular(i, i * 2) for i in range(10_000)]

# Create many slotted objects
slotted_objects = [PointSlotted(i, i * 2) for i in range(10_000)]

# Estimate total memory
regular_total = sum(
    sys.getsizeof(obj) + sys.getsizeof(obj.__dict__)
    for obj in regular_objects
)
slotted_total = sum(
    sys.getsizeof(obj) for obj in slotted_objects
)

print(f"  10,000 regular objects: ~{regular_total:,} bytes")
print(f"  10,000 slotted objects: ~{slotted_total:,} bytes")
print(f"  Savings: ~{regular_total - slotted_total:,} bytes")
print()

del regular_objects, slotted_objects  # Free memory

# =============================
# 5. GENERATOR vs LIST MEMORY
# =============================

print("=== Generator vs List Memory ===")
print()

# List — stores all values
big_list = [x * x for x in range(10_000)]
print(f"  List of 10,000 squares: {sys.getsizeof(big_list):,} bytes")

# Generator — stores almost nothing
big_gen = (x * x for x in range(10_000))
print(f"  Generator of 10,000 squares: {sys.getsizeof(big_gen)} bytes")
print()

# The generator is tiny because it computes values on demand
# instead of storing them all in memory

del big_list

# =============================
# 6. STRING INTERNING
# =============================

print("=== String Interning ===")
print()

# Python automatically interns some strings
a = "hello"
b = "hello"
print(f"  'hello' is 'hello': {a is b}")  # True — same object

# Manual interning with sys.intern()
s1 = sys.intern("a long string for interning example")
s2 = sys.intern("a long string for interning example")
print(f"  Manually interned: {s1 is s2}")  # True
print()

# Interning saves memory when the same string appears many times

# =============================
# 7. CHOOSING EFFICIENT DATA STRUCTURES
# =============================

print("=== Choosing Efficient Data Structures ===")
print()

# Example: Storing 10,000 boolean flags

# Method 1: List of bools
bool_list = [True] * 10_000
print(f"  List of 10,000 bools: {sys.getsizeof(bool_list):,} bytes")

# Method 2: Using a set of indices (sparse representation)
true_indices = set(range(10_000))
print(f"  Set of 10,000 indices: {sys.getsizeof(true_indices):,} bytes")

# Method 3: Bytearray (1 byte per flag)
bool_bytes = bytearray([1] * 10_000)
print(f"  Bytearray of 10,000: {sys.getsizeof(bool_bytes):,} bytes")
print()

# The best choice depends on your usage pattern!

# =============================
# 8. DICT KEY SHARING
# =============================

print("=== Dict Key Sharing (Python Optimization) ===")
print()

# Python optimizes dicts for instances of the same class
# Instances share the key structure, saving memory

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

p1 = Person("Trush", 21, "NYC")
p2 = Person("Rahul", 25, "LA")

# Both instances share the same key layout internally
print(f"  p1.__dict__: {p1.__dict__}")
print(f"  p2.__dict__: {p2.__dict__}")
print(f"  p1 dict size: {sys.getsizeof(p1.__dict__)} bytes")
print(f"  p2 dict size: {sys.getsizeof(p2.__dict__)} bytes")
print()

# =============================
# 9. AVOIDING UNNECESSARY COPIES
# =============================

print("=== Avoiding Unnecessary Copies ===")
print()

import copy

original = list(range(1000))

# These create copies (use memory):
slice_copy = original[:]           # Full slice copy
list_copy = list(original)         # list() copy
method_copy = original.copy()      # .copy() method
deep_copy = copy.deepcopy(original)  # Deep copy

print(f"  Original:   {sys.getsizeof(original):,} bytes")
print(f"  Slice copy: {sys.getsizeof(slice_copy):,} bytes")
print(f"  list() copy: {sys.getsizeof(list_copy):,} bytes")
print(f"  .copy():    {sys.getsizeof(method_copy):,} bytes")
print()

# Tip: Don't copy data unless you need to modify it independently
# Use the original reference when you only need to read

# =============================
# 10. MEMORY TIPS SUMMARY
# =============================

print("=== Memory Optimization Tips ===")
print()

tips = [
    "Use tuples instead of lists for fixed data",
    "Use __slots__ for classes with many instances",
    "Use generators instead of lists for large sequences",
    "Use sys.getsizeof() to measure object sizes",
    "Avoid unnecessary copies of large data",
    "Use sets for membership checks (not lists)",
    "Use sys.intern() for frequently repeated strings",
    "Choose the right data structure for your problem",
]

for i, tip in enumerate(tips, 1):
    print(f"  {i}. {tip}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Compare memory usage of a list vs generator
#    for range(1_000_000)
# 2. Create a class with __slots__ and measure the
#    memory difference with 100,000 instances
# 3. Use sys.getsizeof() to find which collection
#    type uses the least memory for 1000 integers
# ============================================
