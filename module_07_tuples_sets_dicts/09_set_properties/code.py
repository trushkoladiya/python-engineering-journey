# ============================================
# MODULE 7 - SUBTOPIC 9: Set Properties
# ============================================

# =============================
# 1. UNORDERED
# =============================

# --- Example 1: Sets don't maintain order ---
colors = {"red", "green", "blue", "yellow"}
print("Colors:", colors)   # Order may vary!

# --- Example 2: Cannot use indexing ---
numbers = {10, 20, 30}
# print(numbers[0])   # TypeError: 'set' object is not subscriptable
# print(numbers[-1])  # TypeError!
print("Cannot index sets — they are unordered")

# --- Example 3: Converting to list for ordered access ---
my_set = {50, 10, 30, 20, 40}
my_list = sorted(my_set)   # Convert to sorted list
print(f"\nSet: {my_set}")
print(f"Sorted list: {my_list}")
print(f"First (sorted): {my_list[0]}")

# =============================
# 2. NO DUPLICATES
# =============================

# --- Example 4: Duplicates are automatically removed ---
numbers = {1, 2, 3, 2, 1, 4, 3, 5}
print(f"\nSet with no duplicates: {numbers}")

# --- Example 5: True and 1 are considered equal ---
mixed = {1, True, 0, False}
print(f"{{1, True, 0, False}} becomes: {mixed}")
# True == 1 and False == 0, so only one of each appears

# --- Example 6: Case sensitivity matters ---
names = {"Trush", "trush", "TRUSH"}
print(f"\nDifferent cases: {names}")   # All three are unique
print(f"Length: {len(names)}")

# =============================
# 3. MUTABLE — CAN ADD AND REMOVE
# =============================

# --- Example 7: Adding elements ---
fruits = {"apple", "banana"}
print(f"\nBefore add: {fruits}")

fruits.add("cherry")
print(f"After add: {fruits}")

# --- Example 8: Removing elements ---
fruits.discard("banana")
print(f"After remove: {fruits}")

# --- Example 9: Adding duplicates has no effect ---
numbers = {1, 2, 3}
print(f"\nBefore: {numbers}")
numbers.add(2)   # Already exists
numbers.add(3)   # Already exists
print(f"After adding 2 and 3 again: {numbers}")   # Unchanged

# =============================
# 4. ELEMENTS MUST BE IMMUTABLE
# =============================

# --- Example 10: Valid set elements ---
valid = {42, 3.14, "hello", True, (1, 2, 3)}
print(f"\nValid set: {valid}")

# --- Example 11: Invalid elements (lists, dicts, sets) ---
# These will cause errors:
# bad = {[1, 2]}        # TypeError: unhashable type: 'list'
# bad = {{1, 2}}        # TypeError: unhashable type: 'set'
# bad = {{"a": 1}}      # TypeError: unhashable type: 'dict'
print("Lists, sets, and dicts CANNOT be set elements")

# --- Example 12: Tuples can be set elements (because they're immutable) ---
coordinates = {(0, 0), (1, 2), (3, 4), (1, 2)}
print(f"\nCoordinate set: {coordinates}")   # Duplicate (1,2) removed
print(f"Length: {len(coordinates)}")

# =============================
# 5. COMPARING SET vs LIST vs TUPLE
# =============================

# --- Example 13: Quick comparison ---
my_list = [1, 2, 3, 2, 1]     # Ordered, duplicates OK, mutable
my_tuple = (1, 2, 3, 2, 1)    # Ordered, duplicates OK, immutable
my_set = {1, 2, 3, 2, 1}      # Unordered, no duplicates, mutable

print(f"\nList:  {my_list}  (length {len(my_list)})")
print(f"Tuple: {my_tuple} (length {len(my_tuple)})")
print(f"Set:   {my_set}   (length {len(my_set)})")

# --- Example 14: Checking membership is faster in sets ---
big_list = list(range(10000))
big_set = set(range(10000))

# Both work, but set lookup is much faster for large data
print(f"\n9999 in list: {9999 in big_list}")
print(f"9999 in set:  {9999 in big_set}")

# ============================================
# TRY IT YOURSELF:
# 1. Try adding a list to a set and observe the error
# 2. Create a set with True, 1, False, 0 and see the result
# 3. Compare the length of a list and set with the same values
# ============================================
