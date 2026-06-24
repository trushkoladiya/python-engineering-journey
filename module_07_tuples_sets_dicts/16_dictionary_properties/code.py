# ============================================
# MODULE 7 - SUBTOPIC 16: Dictionary Properties
# ============================================

# =============================
# 1. KEY UNIQUENESS
# =============================

# --- Example 1: Duplicate keys — last value wins ---
data = {"a": 1, "b": 2, "a": 99}
print("Result:", data)   # {'a': 99, 'b': 2}

# --- Example 2: Building shows uniqueness ---
inventory = {}
inventory["apple"] = 5
inventory["banana"] = 3
inventory["apple"] = 10   # Overwrites!
print("\nInventory:", inventory)   # {'apple': 10, 'banana': 3}

# =============================
# 2. KEYS MUST BE IMMUTABLE
# =============================

# --- Example 3: Valid key types ---
valid = {
    "name": "Trush",         # string key ✅
    42: "forty-two",         # int key ✅
    3.14: "pi",              # float key ✅
    (1, 2): "coordinates",   # tuple key ✅
    True: "yes",             # bool key ✅
}
print("\nValid keys dict:", valid)

# --- Example 4: Invalid key types ---
# These will cause errors:
# bad = {[1, 2]: "list key"}       # TypeError: unhashable type: 'list'
# bad = {{1, 2}: "set key"}        # TypeError: unhashable type: 'set'
# bad = {{"a": 1}: "dict key"}     # TypeError: unhashable type: 'dict'
print("Lists, sets, and dicts CANNOT be keys")

# =============================
# 3. MUTABLE STRUCTURE
# =============================

# --- Example 5: Adding, modifying, removing ---
person = {"name": "Trush"}
print("\nOriginal:", person)

person["age"] = 21          # Add
print("After add:", person)

person["name"] = "Rahul"      # Modify
print("After modify:", person)

del person["age"]           # Remove
print("After delete:", person)

# =============================
# 4. ORDERED (PYTHON 3.7+)
# =============================

# --- Example 6: Insertion order preserved ---
d = {}
d["third"] = 3
d["first"] = 1
d["second"] = 2
print("\nOrder preserved:", d)
# {'third': 3, 'first': 1, 'second': 2}

# --- Example 7: Iterating shows insertion order ---
colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
print("\nColors in order:")
for key in colors:
    print(f"  {key}: {colors[key]}")

# =============================
# 5. VALUES CAN BE ANY TYPE
# =============================

# --- Example 8: Diverse value types ---
record = {
    "name": "Charlie",
    "scores": [95, 87, 92],
    "address": {"city": "Mumbai", "zip": "400001"},
    "active": True,
    "notes": None,
}
print("\nRecord:", record)
print("Scores:", record["scores"])
print("City:", record["address"]["city"])

# ============================================
# TRY IT YOURSELF:
# 1. Create a dict with duplicate keys and see what happens
# 2. Try using a list as a key and observe the error
# 3. Add, modify, and delete elements in a dictionary
# ============================================
