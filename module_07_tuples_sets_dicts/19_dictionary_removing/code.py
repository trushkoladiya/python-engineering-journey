# ============================================
# MODULE 7 - SUBTOPIC 19: Removing Dictionary Elements
# ============================================

# =============================
# 1. pop() — REMOVE BY KEY
# =============================

# --- Example 1: Basic pop ---
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print("Before:", person)

age = person.pop("age")
print(f"Removed age: {age}")
print("After:", person)

# --- Example 2: pop with default value ---
email = person.pop("email", "not found")
print(f"\nEmail: {email}")   # not found (no error!)

# --- Example 3: pop without default raises error if missing ---
# person.pop("phone")   # KeyError: 'phone'
print("pop() without default raises KeyError if key missing")

# =============================
# 2. popitem() — REMOVE LAST ITEM
# =============================

# --- Example 4: Basic popitem ---
data = {"a": 1, "b": 2, "c": 3}
print(f"\nBefore: {data}")

last = data.popitem()
print(f"Removed: {last}")   # ('c', 3)
print(f"After: {data}")

# --- Example 5: Popping multiple items ---
colors = {"red": 1, "green": 2, "blue": 3, "yellow": 4}
print(f"\nOriginal: {colors}")
while len(colors) > 1:
    removed = colors.popitem()
    print(f"  Removed: {removed}")
print(f"Remaining: {colors}")

# =============================
# 3. del — DELETE BY KEY
# =============================

# --- Example 6: Basic del ---
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print(f"\nBefore: {person}")
del person["city"]
print(f"After del city: {person}")

# --- Example 7: del raises error if missing ---
# del person["email"]   # KeyError: 'email'
print("del raises KeyError if key doesn't exist")

# --- Example 8: Safe deletion ---
data = {"x": 10, "y": 20, "z": 30}
key_to_remove = "y"
if key_to_remove in data:
    del data[key_to_remove]
    print(f"\nRemoved '{key_to_remove}':", data)
else:
    print(f"\n'{key_to_remove}' not found")

# =============================
# 4. clear() — REMOVE ALL
# =============================

# --- Example 9: Clear entire dictionary ---
settings = {"theme": "dark", "language": "en", "font_size": 14}
print(f"\nBefore clear: {settings}")
settings.clear()
print(f"After clear: {settings}")
print(f"Length: {len(settings)}")

# =============================
# 5. PRACTICAL EXAMPLES
# =============================

# --- Example 10: Removing specific keys ---
student = {
    "name": "Rahul",
    "age": 20,
    "grade": "A",
    "temporary_id": "T123",
    "notes": "none",
}
keys_to_remove = ["temporary_id", "notes"]

print(f"\nBefore cleanup: {student}")
for key in keys_to_remove:
    student.pop(key, None)   # Safe removal
print(f"After cleanup: {student}")

# --- Example 11: Filtering a dictionary ---
scores = {"Trush": 95, "Rahul": 45, "Charlie": 72, "Diana": 38, "Eve": 88}
print(f"\nAll scores: {scores}")

# Remove students who failed (< 50)
failed = []
for name in scores:
    if scores[name] < 50:
        failed.append(name)

for name in failed:
    scores.pop(name)

print(f"After removing failures: {scores}")

# ============================================
# TRY IT YOURSELF:
# 1. Use pop() to remove and print a value from a dictionary
# 2. Use del to remove a key-value pair
# 3. Clear a dictionary and verify it's empty
# ============================================
