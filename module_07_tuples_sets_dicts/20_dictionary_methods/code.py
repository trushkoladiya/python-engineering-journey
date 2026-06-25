# ============================================
# MODULE 7 - SUBTOPIC 20: Dictionary Methods
# ============================================

# =============================
# 1. keys() — GET ALL KEYS
# =============================

# --- Example 1: Basic keys ---
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print("Keys:", person.keys())

# --- Example 2: Convert to list ---
keys_list = list(person.keys())
print("Keys list:", keys_list)
print("First key:", keys_list[0])

# --- Example 3: Check if key exists ---
if "name" in person.keys():
    print("\n'name' is a key ✓")
# Same as: if "name" in person:

# =============================
# 2. values() — GET ALL VALUES
# =============================

# --- Example 4: Basic values ---
scores = {"Trush": 95, "Rahul": 87, "Charlie": 92}
print("\nValues:", scores.values())

# --- Example 5: Operations on values ---
values = list(scores.values())
print("Max score:", max(values))
print("Min score:", min(values))
print("Average:", sum(values) / len(values))

# --- Example 6: Check if value exists ---
if 95 in scores.values():
    print("Someone scored 95 ✓")

# =============================
# 3. items() — GET KEY-VALUE PAIRS
# =============================

# --- Example 7: Basic items ---
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print("\nItems:", person.items())

# --- Example 8: Items are tuples ---
items_list = list(person.items())
print("First item:", items_list[0])        # ('name', 'Trush')
print("Type:", type(items_list[0]))        # <class 'tuple'>

# --- Example 9: Unpacking items ---
for key, value in person.items():
    print(f"  {key}: {value}")

# =============================
# 4. PRACTICAL EXAMPLES
# =============================

# --- Example 10: Finding key with max value ---
scores = {"Trush": 95, "Rahul": 87, "Charlie": 92, "Diana": 98}
best_name = ""
best_score = 0

for name, score in scores.items():
    if score > best_score:
        best_score = score
        best_name = name

print(f"\nBest: {best_name} with {best_score}")

# --- Example 11: Inverting a dictionary ---
original = {"a": 1, "b": 2, "c": 3}
inverted = {}
for key, value in original.items():
    inverted[value] = key

print(f"\nOriginal: {original}")
print(f"Inverted: {inverted}")

# --- Example 12: Formatting output ---
menu = {"burger": 8.99, "pizza": 12.50, "salad": 6.75, "drink": 2.50}
print("\n--- MENU ---")
for item, price in menu.items():
    print(f"  {item:10s} ${price:.2f}")
print(f"{'':10s} --------")
print(f"  {'Total':10s} ${sum(menu.values()):.2f}")

# ============================================
# TRY IT YOURSELF:
# 1. Get all keys from a dictionary and print them
# 2. Find the sum of all values in a dictionary
# 3. Use items() to print formatted key-value pairs
# ============================================
