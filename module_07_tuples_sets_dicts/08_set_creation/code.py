# ============================================
# MODULE 7 - SUBTOPIC 8: Set Creation
# ============================================

# =============================
# 1. EMPTY SET
# =============================

# --- Example 1: Creating an empty set ---
empty = set()
print("Empty set:", empty)
print("Type:", type(empty))   # <class 'set'>
print("Length:", len(empty))  # 0

# --- Example 2: COMMON MISTAKE — {} is a dict, NOT a set ---
not_a_set = {}
print("\n{} is type:", type(not_a_set))   # <class 'dict'>

actual_set = set()
print("set() is type:", type(actual_set))  # <class 'set'>

# =============================
# 2. SET WITH VALUES
# =============================

# --- Example 3: Set of integers ---
numbers = {1, 2, 3, 4, 5}
print("\nNumbers:", numbers)

# --- Example 4: Set of strings ---
fruits = {"apple", "banana", "cherry"}
print("Fruits:", fruits)   # Order may vary!

# --- Example 5: Mixed types ---
mixed = {1, "hello", 3.14, True}
print("Mixed:", mixed)
# Note: True and 1 are considered equal, so only one appears

# =============================
# 3. AUTOMATIC DUPLICATE REMOVAL
# =============================

# --- Example 6: Duplicates are removed ---
numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print("\nWith duplicates removed:", numbers)   # {1, 2, 3, 4}

# --- Example 7: String duplicates ---
letters = {"a", "b", "a", "c", "b", "d", "a"}
print("Unique letters:", letters)

# --- Example 8: How many duplicates were removed? ---
original_data = [5, 3, 8, 3, 5, 1, 8, 3, 5]
unique_data = set(original_data)
removed = len(original_data) - len(unique_data)
print(f"\nOriginal: {original_data} (length {len(original_data)})")
print(f"Unique:   {unique_data} (length {len(unique_data)})")
print(f"Duplicates removed: {removed}")

# =============================
# 4. CREATING SETS FROM OTHER TYPES
# =============================

# --- Example 9: From a list ---
my_list = [10, 20, 30, 20, 10, 40]
my_set = set(my_list)
print(f"\nList: {my_list}")
print(f"Set:  {my_set}")

# --- Example 10: From a string ---
chars = set("hello")
print(f"\nset('hello'): {chars}")   # No duplicate 'l'

word = set("mississippi")
print(f"set('mississippi'): {word}")   # Only unique letters

# --- Example 11: From a tuple ---
my_tuple = (1, 2, 3, 2, 1)
my_set = set(my_tuple)
print(f"\nTuple: {my_tuple}")
print(f"Set:   {my_set}")

# --- Example 12: From a range ---
range_set = set(range(1, 11))
print(f"\nset(range(1,11)): {range_set}")

# =============================
# 5. SETS ARE UNORDERED
# =============================

# --- Example 13: Order is not guaranteed ---
colors = {"red", "green", "blue", "yellow", "purple"}
print("\nColors:", colors)
print("Run this multiple times — the order may change!")

# --- Example 14: No indexing in sets ---
# numbers = {10, 20, 30}
# print(numbers[0])   # TypeError: 'set' object is not subscriptable

# =============================
# 6. PRACTICAL: REMOVING DUPLICATES FROM A LIST
# =============================

# --- Example 15: Quick duplicate removal ---
names = ["Trush", "Rahul", "Trush", "Charlie", "Rahul", "Diana", "Trush"]
unique_names = list(set(names))
print(f"\nOriginal: {names}")
print(f"Unique:   {unique_names}")

# --- Example 16: Counting unique elements ---
grades = ["A", "B", "A", "C", "B", "A", "D", "C", "B"]
unique_grades = set(grades)
print(f"\nAll grades: {grades}")
print(f"Unique grades: {unique_grades}")
print(f"Number of unique grades: {len(unique_grades)}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a set with some duplicate numbers and see what happens
# 2. Convert the string "programming" to a set
# 3. Remove duplicates from a list using set()
# ============================================
