# ============================================
# MODULE 7 - SUBTOPIC 11: Mathematical Set Operations
# ============================================

# =============================
# 1. UNION — ALL ELEMENTS FROM BOTH
# =============================

# --- Example 1: Basic union ---
a = {1, 2, 3}
b = {3, 4, 5}
print("a:", a)
print("b:", b)
print("a | b:", a | b)           # {1, 2, 3, 4, 5}
print("a.union(b):", a.union(b)) # {1, 2, 3, 4, 5}

# --- Example 2: Union of string sets ---
python_devs = {"Trush", "Rahul", "Charlie"}
java_devs = {"Charlie", "David", "Eve"}
all_devs = python_devs | java_devs
print(f"\nPython devs: {python_devs}")
print(f"Java devs:   {java_devs}")
print(f"All devs:    {all_devs}")

# --- Example 3: Union of multiple sets ---
a = {1, 2}
b = {2, 3}
c = {3, 4}
all_together = a | b | c
print(f"\na | b | c: {all_together}")   # {1, 2, 3, 4}

# =============================
# 2. INTERSECTION — ELEMENTS IN BOTH
# =============================

# --- Example 4: Basic intersection ---
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(f"\na: {a}")
print(f"b: {b}")
print(f"a & b: {a & b}")                       # {3, 4, 5}
print(f"a.intersection(b): {a.intersection(b)}")

# --- Example 5: Finding common friends ---
trush_friends = {"Rahul", "Charlie", "David", "Eve"}
rahul_friends = {"Charlie", "Eve", "Frank", "Grace"}
common = trush_friends & rahul_friends
print(f"\nTrush's friends: {trush_friends}")
print(f"Rahul's friends:   {rahul_friends}")
print(f"Common friends:  {common}")

# --- Example 6: No common elements ---
x = {1, 2, 3}
y = {4, 5, 6}
print(f"\n{x} & {y}: {x & y}")   # set() — empty set

# =============================
# 3. DIFFERENCE — IN ONE BUT NOT OTHER
# =============================

# --- Example 7: Basic difference ---
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(f"\na - b: {a - b}")   # {1, 2} — in a but not in b
print(f"b - a: {b - a}")     # {6, 7} — in b but not in a

# --- Example 8: Items only in first set ---
all_students = {"Trush", "Rahul", "Charlie", "David", "Eve"}
passed = {"Trush", "Charlie", "Eve"}
failed = all_students - passed
print(f"\nAll students: {all_students}")
print(f"Passed:       {passed}")
print(f"Failed:       {failed}")

# --- Example 9: Using difference() method ---
have = {"pen", "pencil", "eraser", "ruler"}
need = {"pen", "notebook", "calculator", "ruler"}
already_have = have - need
still_need = need - have
print(f"\nAlready have: {already_have}")
print(f"Still need:   {still_need}")

# =============================
# 4. SYMMETRIC DIFFERENCE — IN EITHER BUT NOT BOTH
# =============================

# --- Example 10: Basic symmetric difference ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"\na ^ b: {a ^ b}")   # {1, 2, 5, 6}
print(f"a.symmetric_difference(b): {a.symmetric_difference(b)}")

# --- Example 11: Practical — find unique skills ---
trush_skills = {"Python", "SQL", "HTML"}
rahul_skills = {"SQL", "JavaScript", "HTML"}
unique_skills = trush_skills ^ rahul_skills
print(f"\nTrush's skills: {trush_skills}")
print(f"Rahul's skills:   {rahul_skills}")
print(f"Unique to one:  {unique_skills}")   # Skills only one person has

# =============================
# 5. COMPARING ALL OPERATIONS
# =============================

# --- Example 12: Visual comparison ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"\na = {a}")
print(f"b = {b}")
print(f"Union (a | b):                {a | b}")         # {1, 2, 3, 4, 5, 6}
print(f"Intersection (a & b):         {a & b}")         # {3, 4}
print(f"Difference (a - b):           {a - b}")         # {1, 2}
print(f"Difference (b - a):           {b - a}")         # {5, 6}
print(f"Symmetric Difference (a ^ b): {a ^ b}")         # {1, 2, 5, 6}

# =============================
# 6. PRACTICAL: REAL-WORLD EXAMPLE
# =============================

# --- Example 13: Comparing inventory ---
store_a = {"apple", "banana", "cherry", "date", "elderberry"}
store_b = {"banana", "date", "fig", "grape", "honeydew"}

print("\n--- Store Comparison ---")
print(f"Both sell:       {store_a & store_b}")
print(f"Only Store A:    {store_a - store_b}")
print(f"Only Store B:    {store_b - store_a}")
print(f"All products:    {store_a | store_b}")
print(f"Exclusive items: {store_a ^ store_b}")

# ============================================
# TRY IT YOURSELF:
# 1. Create two sets of your hobbies and a friend's hobbies
# 2. Find common hobbies (intersection)
# 3. Find hobbies only you have (difference)
# ============================================
