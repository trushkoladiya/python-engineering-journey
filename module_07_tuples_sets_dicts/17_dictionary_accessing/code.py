# ============================================
# MODULE 7 - SUBTOPIC 17: Accessing Dictionary Data
# ============================================

# =============================
# 1. USING KEYS (SQUARE BRACKETS)
# =============================

# --- Example 1: Basic access ---
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# --- Example 2: Number keys ---
squares = {1: 1, 2: 4, 3: 9, 4: 16}
print(f"\n3 squared = {squares[3]}")

# --- Example 3: KeyError when key is missing ---
# Uncomment to see the error:
# print(person["email"])   # KeyError: 'email'
print("\nMissing key would cause KeyError!")

# =============================
# 2. get() — SAFE ACCESS
# =============================

# --- Example 4: get() returns None if missing ---
person = {"name": "Trush", "age": 21}
print("\nget('name'):", person.get("name"))      # Trush
print("get('email'):", person.get("email"))      # None

# --- Example 5: get() with default value ---
print("\nget with default:", person.get("email", "not provided"))
print("get age:", person.get("age", 0))          # 25 (key exists)

# --- Example 6: Comparing [] vs get() ---
config = {"theme": "dark", "language": "en"}
# Using [] — crashes if missing
# font = config["font_size"]   # KeyError!

# Using get() — safe
font = config.get("font_size", 14)
print(f"\nFont size: {font}")   # 14 (default)

# =============================
# 3. HANDLING MISSING KEYS
# =============================

# --- Example 7: Check with 'in' before accessing ---
person = {"name": "Trush", "age": 21}
if "email" in person:
    print(f"\nEmail: {person['email']}")
else:
    print("\nNo email found")

# --- Example 8: Safe access pattern ---
settings = {"volume": 80, "brightness": 60}
keys_to_check = ["volume", "brightness", "contrast", "bass"]

print("\nSettings:")
for key in keys_to_check:
    value = settings.get(key, "not set")
    print(f"  {key}: {value}")

# --- Example 9: Building a safe lookup ---
prices = {"apple": 2.50, "banana": 1.75, "cherry": 4.00}
items = ["apple", "mango", "cherry", "grape"]

print("\nPrice list:")
for item in items:
    price = prices.get(item)
    if price is not None:
        print(f"  {item}: ${price:.2f}")
    else:
        print(f"  {item}: not available")

# =============================
# 4. ACCESSING NESTED DATA
# =============================

# --- Example 10: Nested dictionary access ---
students = {
    "Trush": {"age": 21, "grade": "A", "scores": [95, 88, 92]},
    "Rahul": {"age": 21, "grade": "B", "scores": [82, 79, 85]},
}

print(f"\nTrush's grade: {students['Trush']['grade']}")
print(f"Rahul's scores: {students['Rahul']['scores']}")
print(f"Trush's first score: {students['Trush']['scores'][0]}")

# --- Example 11: Safe nested access ---
data = {"user": {"name": "Trush", "settings": {"theme": "dark"}}}
theme = data.get("user", {}).get("settings", {}).get("theme", "light")
print(f"\nTheme: {theme}")

# ============================================
# TRY IT YOURSELF:
# 1. Access values from a dictionary using both [] and get()
# 2. Try accessing a missing key with get() and a default value
# 3. Check if a key exists before accessing it
# ============================================
