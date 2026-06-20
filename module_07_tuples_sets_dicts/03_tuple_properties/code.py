# ============================================
# MODULE 7 - SUBTOPIC 3: Tuple Properties
# ============================================

# =============================
# 1. IMMUTABILITY
# =============================

# --- Example 1: Tuples cannot be modified ---
colors = ("red", "green", "blue")
print("Tuple:", colors)

# Trying to change an element causes an error:
# Uncomment the line below to see the error:
# colors[0] = "yellow"   # TypeError: 'tuple' object does not support item assignment

# --- Example 2: Cannot add or remove elements ---
numbers = (1, 2, 3)
# numbers.append(4)    # AttributeError: 'tuple' has no attribute 'append'
# numbers.remove(1)    # AttributeError: 'tuple' has no attribute 'remove'
# del numbers[0]       # TypeError: 'tuple' object doesn't support item deletion
print("Numbers (unchanged):", numbers)

# --- Example 3: Comparison with lists ---
my_list = [1, 2, 3]
my_list[0] = 99        # ✅ Works — lists are mutable
print("\nList after change:", my_list)

my_tuple = (1, 2, 3)
# my_tuple[0] = 99     # ❌ Error — tuples are immutable
print("Tuple (can't change):", my_tuple)

# =============================
# 2. WORKAROUND: CREATING A NEW TUPLE
# =============================

# --- Example 4: "Change" by creating a new tuple ---
original = (1, 2, 3, 4, 5)
# To "change" index 2, create a new tuple
new_tuple = original[:2] + (99,) + original[3:]
print("\nOriginal:", original)       # (1, 2, 3, 4, 5)
print("New tuple:", new_tuple)       # (1, 2, 99, 4, 5)

# --- Example 5: "Add" by concatenation ---
base = (1, 2, 3)
extended = base + (4, 5)
print("\nBase:", base)
print("Extended:", extended)   # (1, 2, 3, 4, 5)

# =============================
# 3. TUPLES ARE FASTER AND SMALLER
# =============================

# --- Example 6: Size comparison ---
import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

list_size = sys.getsizeof(my_list)
tuple_size = sys.getsizeof(my_tuple)

print(f"\nList size:  {list_size} bytes")
print(f"Tuple size: {tuple_size} bytes")
print(f"Tuple is {list_size - tuple_size} bytes smaller")

# =============================
# 4. TUPLES WITH MUTABLE ELEMENTS
# =============================

# --- Example 7: Tuple containing a list ---
data = (1, 2, [3, 4])
print("\nBefore:", data)

# The list inside the tuple CAN be changed
data[2].append(5)
print("After append:", data)   # (1, 2, [3, 4, 5])

data[2][0] = 99
print("After modify:", data)   # (1, 2, [99, 4, 5])

# But the tuple element itself cannot be reassigned:
# data[2] = [10, 20]   # TypeError!

# --- Example 8: Proving the tuple reference didn't change ---
data = (1, 2, [3, 4])
print(f"\nID of list inside tuple: {id(data[2])}")
data[2].append(5)
print(f"ID after append:         {id(data[2])}")   # Same ID!
print("The list object itself didn't change — only its contents did")

# =============================
# 5. TUPLES ARE HASHABLE (when all elements are immutable)
# =============================

# --- Example 9: Tuples can be used as dictionary keys ---
locations = {}
locations[(40, 74)] = "New York"
locations[(51, 0)] = "London"
print("\nLocations:", locations)
print("At (40, 74):", locations[(40, 74)])

# --- Example 10: Tuples can be added to sets ---
point_set = set()
point_set.add((1, 2))
point_set.add((3, 4))
point_set.add((1, 2))   # duplicate — won't be added
print("\nPoint set:", point_set)   # {(1, 2), (3, 4)}

# Lists cannot be used as keys or in sets:
# locations[[40, 74]] = "New York"   # TypeError: unhashable type: 'list'

# ============================================
# TRY IT YOURSELF:
# 1. Try modifying a tuple and observe the error
# 2. Create a new tuple by combining slices of an existing tuple
# 3. Compare the size of a list and a tuple with the same elements
# ============================================
