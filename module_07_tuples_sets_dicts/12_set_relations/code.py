# ============================================
# MODULE 7 - SUBTOPIC 12: Set Relations
# ============================================

# =============================
# 1. SUBSET — issubset() / <=
# =============================

# --- Example 1: Basic subset check ---
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(f"a = {a}")
print(f"b = {b}")
print(f"a.issubset(b): {a.issubset(b)}")   # True
print(f"b.issubset(a): {b.issubset(a)}")   # False

# --- Example 2: Using <= operator ---
print(f"\na <= b: {a <= b}")   # True
print(f"b <= a: {b <= a}")     # False

# --- Example 3: A set is always a subset of itself ---
x = {1, 2, 3}
print(f"\nx.issubset(x): {x.issubset(x)}")   # True

# --- Example 4: Empty set is subset of everything ---
empty = set()
any_set = {1, 2, 3}
print(f"\nempty.issubset(any_set): {empty.issubset(any_set)}")   # True

# --- Example 5: Practical — checking permissions ---
required = {"read", "write"}
user_perms = {"read", "write", "execute", "admin"}
has_access = required.issubset(user_perms)
print(f"\nRequired: {required}")
print(f"User has: {user_perms}")
print(f"Access granted: {has_access}")   # True

# =============================
# 2. SUPERSET — issuperset() / >=
# =============================

# --- Example 6: Basic superset check ---
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(f"\nb.issuperset(a): {b.issuperset(a)}")   # True
print(f"a.issuperset(b): {a.issuperset(b)}")       # False

# --- Example 7: Using >= operator ---
print(f"b >= a: {b >= a}")   # True
print(f"a >= b: {a >= b}")   # False

# --- Example 8: Practical — checking if store has all items ---
store_inventory = {"bread", "milk", "eggs", "butter", "cheese", "juice"}
shopping_list = {"bread", "milk", "eggs"}
can_buy_all = store_inventory.issuperset(shopping_list)
print(f"\nStore has: {store_inventory}")
print(f"Need:     {shopping_list}")
print(f"Can buy everything: {can_buy_all}")   # True

# =============================
# 3. DISJOINT — isdisjoint()
# =============================

# --- Example 9: Sets with no common elements ---
a = {1, 2, 3}
b = {4, 5, 6}
print(f"\na = {a}")
print(f"b = {b}")
print(f"a.isdisjoint(b): {a.isdisjoint(b)}")   # True

# --- Example 10: Sets with common elements ---
c = {3, 4, 5}
print(f"\na = {a}")
print(f"c = {c}")
print(f"a.isdisjoint(c): {a.isdisjoint(c)}")   # False — 3 is common

# --- Example 11: Practical — checking for conflicts ---
team_a = {"Trush", "Rahul", "Charlie"}
team_b = {"David", "Eve", "Frank"}
team_c = {"Charlie", "Grace", "Eve"}

print(f"\nTeam A and B have no overlap: {team_a.isdisjoint(team_b)}")   # True
print(f"Team A and C have no overlap: {team_a.isdisjoint(team_c)}")     # False
print(f"Team B and C have no overlap: {team_b.isdisjoint(team_c)}")     # False

# =============================
# 4. STRICT SUBSET AND SUPERSET
# =============================

# --- Example 12: Strict subset (proper subset) ---
a = {1, 2, 3}
b = {1, 2, 3, 4}
c = {1, 2, 3}

# < means strict subset (not equal to the superset)
print(f"\na < b: {a < b}")   # True — a is smaller and contained in b
print(f"a < c: {a < c}")     # False — they are equal

# <= includes the case where sets are equal
print(f"a <= c: {a <= c}")   # True

# --- Example 13: Strict superset ---
print(f"\nb > a: {b > a}")   # True
print(f"c > a: {c > a}")     # False — equal, not strictly greater

# =============================
# 5. COMBINING RELATION CHECKS
# =============================

# --- Example 14: Analyzing two sets ---
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print(f"\nset1 = {set1}")
print(f"set2 = {set2}")
print(f"Subset:   {set1.issubset(set2)}")
print(f"Superset: {set2.issuperset(set1)}")
print(f"Disjoint: {set1.isdisjoint(set2)}")
print(f"Equal:    {set1 == set2}")

# --- Example 15: Practical — course prerequisites ---
completed = {"Math 101", "English 101", "CS 101", "Physics 101"}
required_for_cs201 = {"Math 101", "CS 101"}
required_for_cs301 = {"CS 201", "Math 201"}

print(f"\nCompleted: {completed}")
print(f"CS 201 requires: {required_for_cs201}")
print(f"Can take CS 201: {required_for_cs201.issubset(completed)}")   # True

print(f"CS 301 requires: {required_for_cs301}")
print(f"Can take CS 301: {required_for_cs301.issubset(completed)}")   # False

# ============================================
# TRY IT YOURSELF:
# 1. Check if {1, 2} is a subset of {1, 2, 3, 4, 5}
# 2. Check if two sets of colors have any overlap
# 3. Verify if your skills are a superset of job requirements
# ============================================
