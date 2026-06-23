# ============================================
# MODULE 7 - SUBTOPIC 14: Frozen Set
# ============================================

# =============================
# 1. CREATING A FROZENSET
# =============================

# --- Example 1: From a list ---
fs = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", fs)
print("Type:", type(fs))

# --- Example 2: From a set ---
regular = {10, 20, 30}
frozen = frozenset(regular)
print("\nFrom set:", frozen)

# --- Example 3: From a string ---
chars = frozenset("hello")
print("From string:", chars)

# --- Example 4: Empty frozenset ---
empty = frozenset()
print("Empty:", empty)

# =============================
# 2. FROZENSET IS IMMUTABLE
# =============================

# --- Example 5: Cannot modify ---
fs = frozenset([1, 2, 3])
# fs.add(4)      # AttributeError
# fs.remove(1)   # AttributeError
# fs.discard(1)  # AttributeError
# fs.pop()       # AttributeError
print("\nFrozensets cannot be modified!")

# =============================
# 3. READ OPERATIONS WORK
# =============================

# --- Example 6: Membership ---
fs = frozenset([1, 2, 3, 4, 5])
print("\n3 in fs:", 3 in fs)
print("9 in fs:", 9 in fs)
print("Length:", len(fs))

# --- Example 7: Iteration ---
colors = frozenset(["red", "green", "blue"])
print("\nColors:")
for color in colors:
    print(f"  - {color}")

# --- Example 8: Set math with frozensets ---
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(f"\na | b: {a | b}")
print(f"a & b: {a & b}")
print(f"a - b: {a - b}")
print(f"a ^ b: {a ^ b}")

# =============================
# 4. USE AS DICTIONARY KEYS
# =============================

# --- Example 9: Frozenset as dict key ---
permissions = {
    frozenset(["read"]): "viewer",
    frozenset(["read", "write"]): "editor",
    frozenset(["read", "write", "admin"]): "admin",
}

user_perms = frozenset(["read", "write"])
print(f"\nUser role: {permissions[user_perms]}")

# =============================
# 5. USE AS SET ELEMENTS
# =============================

# --- Example 10: Frozenset inside a set ---
groups = set()
groups.add(frozenset([1, 2, 3]))
groups.add(frozenset([4, 5, 6]))
groups.add(frozenset([1, 2, 3]))   # duplicate
print(f"\nGroups: {groups}")
print(f"Count: {len(groups)}")   # 2

# ============================================
# TRY IT YOURSELF:
# 1. Create a frozenset and try to add an element
# 2. Use frozensets as keys in a dictionary
# 3. Find the union of two frozensets
# ============================================
