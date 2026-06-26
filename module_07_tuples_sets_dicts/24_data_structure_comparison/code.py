# ============================================
# MODULE 7 - SUBTOPIC 24: Data Structure Comparison
# ============================================

# =============================
# 1. LIST vs TUPLE
# =============================

# --- Example 1: Mutability difference ---
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[0] = 99     # ✅ Works
# my_tuple[0] = 99  # ❌ TypeError

print("List (mutable):", my_list)
print("Tuple (immutable):", my_tuple)

# --- Example 2: Memory comparison ---
import sys
list_size = sys.getsizeof([1, 2, 3, 4, 5])
tuple_size = sys.getsizeof((1, 2, 3, 4, 5))
print(f"\nList size:  {list_size} bytes")
print(f"Tuple size: {tuple_size} bytes")
print(f"Tuple saves {list_size - tuple_size} bytes")

# --- Example 3: When to use which ---
# List: data that changes
shopping = ["milk", "bread", "eggs"]
shopping.append("butter")
print(f"\nShopping (list): {shopping}")

# Tuple: data that stays fixed
coordinates = (28.6139, 77.2090)
print(f"Location (tuple): {coordinates}")

# =============================
# 2. SET vs LIST
# =============================

# --- Example 4: Duplicates ---
list_with_dupes = [1, 2, 2, 3, 3, 3]
set_no_dupes = {1, 2, 2, 3, 3, 3}
print(f"\nList: {list_with_dupes} (length {len(list_with_dupes)})")
print(f"Set:  {set_no_dupes} (length {len(set_no_dupes)})")

# --- Example 5: Order and indexing ---
my_list = [30, 10, 20]
print(f"\nList[0]: {my_list[0]}")   # ✅ Indexing works
# my_set = {30, 10, 20}
# print(my_set[0])   # ❌ TypeError

# --- Example 6: Lookup speed comparison ---
big_list = list(range(100000))
big_set = set(range(100000))

# Both find the element, but set is MUCH faster
print(f"\n99999 in list: {99999 in big_list}")
print(f"99999 in set:  {99999 in big_set}")
print("(Set lookup is near-instant, list is slow for large data)")

# =============================
# 3. DICT vs LIST OF TUPLES
# =============================

# --- Example 7: Dictionary — fast key lookup ---
ages_dict = {"Trush": 21, "Rahul": 30, "Charlie": 28}
print(f"\nDict lookup - Trush's age: {ages_dict['Trush']}")   # Instant

# --- Example 8: List of tuples — sequential search ---
ages_list = [("Trush", 21), ("Rahul", 30), ("Charlie", 28)]
# To find Trush, must loop through:
for name, age in ages_list:
    if name == "Trush":
        print(f"List search - Trush's age: {age}")
        break

# --- Example 9: Dict doesn't allow duplicate keys ---
data = {"a": 1, "a": 2}
print(f"\nDict duplicate keys: {data}")   # {'a': 2}

# List of tuples allows "duplicate keys"
data_list = [("a", 1), ("a", 2)]
print(f"Tuple list duplicates: {data_list}")   # Both kept!

# =============================
# 4. WHEN TO USE WHAT — SUMMARY
# =============================

# --- Example 10: Practical decisions ---
print("\n--- When to Use What ---")
print("  List:  ordered collection, may have duplicates, data changes")
print("  Tuple: ordered collection, data never changes, used as dict keys")
print("  Set:   unique elements, fast lookup, order doesn't matter")
print("  Dict:  key-value mapping, fast lookup by key")

# --- Example 11: Real-world scenarios ---
# ✅ List: student names in enrollment order
enrolled = ["Trush", "Rahul", "Charlie", "Trush"]
print(f"\nEnrolled: {enrolled}")

# ✅ Tuple: fixed configuration
screen_size = (1920, 1080)
print(f"Screen: {screen_size}")

# ✅ Set: unique tags
tags = {"python", "coding", "tutorial", "python"}
print(f"Tags: {tags}")

# ✅ Dict: storing structured data
user = {"name": "Trush", "age": 21, "active": True}
print(f"User: {user}")

# =============================
# 5. CONVERSION BETWEEN TYPES
# =============================

# --- Example 12: Converting between structures ---
original_list = [1, 2, 3, 2, 1, 4]

as_tuple = tuple(original_list)
as_set = set(original_list)
back_to_list = list(as_set)

print(f"\nList:      {original_list}")
print(f"As tuple:  {as_tuple}")
print(f"As set:    {as_set}")
print(f"Back to list: {back_to_list}")

# ============================================
# TRY IT YOURSELF:
# 1. Compare memory of a list vs tuple with 10 elements
# 2. Check lookup speed: find an element in a list vs set
# 3. Decide the best structure for: student grades, unique IDs, config
# ============================================
