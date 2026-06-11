# ============================================
# MODULE 7 - SUBTOPIC 18: Adding & Updating Dictionary Data
# ============================================

# =============================
# 1. ADDING NEW KEY-VALUE PAIRS
# =============================

# --- Example 1: Adding one at a time ---
person = {"name": "Trush"}
print("Before:", person)

person["age"] = 21
person["city"] = "Mumbai"
person["email"] = "trushkoladiya.work@gmail.com"
print("After:", person)

# --- Example 2: Building a dictionary ---
scores = {}
scores["Trush"] = 95
scores["Rahul"] = 87
scores["Charlie"] = 92
print("\nScores:", scores)

# =============================
# 2. UPDATING EXISTING VALUES
# =============================

# --- Example 3: Changing a value ---
person = {"name": "Trush", "age": 21}
print("\nBefore:", person)
person["age"] = 22
print("After:", person)

# --- Example 4: Incrementing a value ---
counter = {"clicks": 10}
counter["clicks"] = counter["clicks"] + 1
print(f"\nClicks: {counter['clicks']}")   # 11

# --- Example 5: Toggle a boolean ---
settings = {"dark_mode": False}
settings["dark_mode"] = not settings["dark_mode"]
print(f"Dark mode: {settings['dark_mode']}")   # True

# =============================
# 3. update() METHOD
# =============================

# --- Example 6: Update with a dictionary ---
person = {"name": "Trush", "age": 21}
person.update({"age": 22, "city": "Mumbai", "email": "trushkoladiya.work@gmail.com"})
print("\nAfter update:", person)

# --- Example 7: Update with keyword arguments ---
config = {"theme": "light", "font_size": 12}
config.update(theme="dark", language="en")
print("Config:", config)

# --- Example 8: Update with list of tuples ---
data = {"a": 1}
data.update([("b", 2), ("c", 3)])
print("From tuples:", data)

# --- Example 9: Merging two dictionaries ---
defaults = {"color": "blue", "size": "medium", "visible": True}
custom = {"color": "red", "size": "large"}
final = {}
final.update(defaults)
final.update(custom)   # Custom overrides defaults
print("\nMerged:", final)

# =============================
# 4. PRACTICAL EXAMPLES
# =============================

# --- Example 10: Building a word counter ---
sentence = "the cat sat on the mat the cat"
word_count = {}

for word in sentence.split():
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print("\nWord counts:", word_count)

# --- Example 11: Accumulating scores ---
results = [("Trush", 90), ("Rahul", 85), ("Trush", 95), ("Rahul", 88)]
totals = {}

for name, score in results:
    if name in totals:
        totals[name] = totals[name] + score
    else:
        totals[name] = score

print("\nTotal scores:", totals)

# ============================================
# TRY IT YOURSELF:
# 1. Create an empty dict and add 3 key-value pairs
# 2. Update an existing value and verify the change
# 3. Use update() to merge two dictionaries
# ============================================
