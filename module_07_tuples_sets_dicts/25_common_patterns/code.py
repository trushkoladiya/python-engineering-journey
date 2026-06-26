# ============================================
# MODULE 7 - SUBTOPIC 25: Common Patterns
# ============================================

# =============================
# 1. TUPLE PATTERNS
# =============================

# --- Example 1: Swapping variables ---
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# --- Example 2: Returning multiple values (concept) ---
# When we learn functions later, tuples are used to return multiple values
# For now, we can pack and unpack manually
result = (True, "Success", 200)
status, message, code = result
print(f"\nStatus: {status}, Message: {message}, Code: {code}")

# --- Example 3: Sorting with tuples ---
students = [("Charlie", 78), ("Trush", 95), ("Rahul", 87)]
students.sort(key=lambda x: x[1], reverse=True)
print("\nRanked students:")
for rank, (name, score) in enumerate(students, 1):
    print(f"  {rank}. {name}: {score}")

# =============================
# 2. SET PATTERNS
# =============================

# --- Example 4: Removing duplicates from a list ---
data = [5, 3, 8, 3, 5, 1, 8, 3, 9, 1]
unique = list(set(data))
print(f"\nOriginal: {data}")
print(f"Unique:   {unique}")

# --- Example 5: Preserving order while removing duplicates ---
data = [5, 3, 8, 3, 5, 1, 8, 3, 9, 1]
seen = set()
unique_ordered = []
for item in data:
    if item not in seen:
        seen.add(item)
        unique_ordered.append(item)
print(f"Unique (ordered): {unique_ordered}")

# --- Example 6: Fast membership testing ---
valid_roles = {"admin", "editor", "viewer", "moderator"}
users = [
    ("Trush", "admin"),
    ("Rahul", "guest"),
    ("Charlie", "editor"),
    ("Diana", "hacker"),
]

print("\nAccess check:")
for name, role in users:
    if role in valid_roles:
        print(f"  ✓ {name} ({role}) — access granted")
    else:
        print(f"  ✗ {name} ({role}) — access denied")

# --- Example 7: Finding common and unique elements ---
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

common = set(list_a) & set(list_b)
only_a = set(list_a) - set(list_b)
only_b = set(list_b) - set(list_a)

print(f"\nList A: {list_a}")
print(f"List B: {list_b}")
print(f"Common: {common}")
print(f"Only in A: {only_a}")
print(f"Only in B: {only_b}")

# =============================
# 3. DICTIONARY PATTERNS
# =============================

# --- Example 8: Frequency counting ---
sentence = "the cat sat on the mat the cat ate the rat"
word_freq = {}
for word in sentence.split():
    word_freq[word] = word_freq.get(word, 0) + 1

print(f"\nWord frequency:")
for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{word}': {count}")

# --- Example 9: Grouping data ---
students = [
    ("Trush", "A"), ("Rahul", "B"), ("Charlie", "A"),
    ("Diana", "C"), ("Eve", "B"), ("Frank", "A"),
]

groups = {}
for name, grade in students:
    if grade not in groups:
        groups[grade] = []
    groups[grade].append(name)

print("\nGrouped by grade:")
for grade in sorted(groups):
    print(f"  Grade {grade}: {groups[grade]}")

# --- Example 10: Lookup table ---
status_codes = {
    200: "OK",
    301: "Moved Permanently",
    404: "Not Found",
    500: "Internal Server Error",
}

codes_to_check = [200, 404, 403, 500]
print("\nStatus codes:")
for code in codes_to_check:
    message = status_codes.get(code, "Unknown")
    print(f"  {code}: {message}")

# --- Example 11: Inverting a mapping ---
country_capital = {
    "India": "Delhi",
    "Japan": "Tokyo",
    "France": "Paris",
}
capital_country = {cap: country for country, cap in country_capital.items()}
print(f"\nCapital → Country: {capital_country}")

# =============================
# 4. COMBINING ALL THREE
# =============================

# --- Example 12: Analyzing survey data ---
survey = [
    ("Trush", "Python"),
    ("Rahul", "JavaScript"),
    ("Charlie", "Python"),
    ("Diana", "Java"),
    ("Eve", "Python"),
    ("Frank", "JavaScript"),
    ("Grace", "Java"),
    ("Henry", "Python"),
]

# Count votes (dict)
votes = {}
for name, lang in survey:
    votes[lang] = votes.get(lang, 0) + 1

# Unique languages (set)
unique_langs = set(lang for _, lang in survey)

# Results (tuple unpacking)
print("\n--- Survey Results ---")
print(f"Total responses: {len(survey)}")
print(f"Unique languages: {unique_langs}")
print(f"\nVote counts:")
for lang, count in sorted(votes.items(), key=lambda x: x[1], reverse=True):
    bar = "█" * count
    print(f"  {lang:12s} {bar} ({count})")

# --- Example 13: Simple inventory system ---
inventory = {
    "apple": (2.50, 100),      # (price, quantity)
    "banana": (1.75, 50),
    "cherry": (4.00, 30),
    "date": (6.50, 20),
}

print("\n--- Inventory ---")
print(f"{'Item':10s} {'Price':>8s} {'Qty':>5s} {'Value':>10s}")
print("-" * 35)

total_value = 0
for item, (price, qty) in inventory.items():
    value = price * qty
    total_value = total_value + value
    print(f"{item:10s} ${price:>6.2f} {qty:>5d} ${value:>8.2f}")

print("-" * 35)
print(f"{'Total':10s} {'':>8s} {'':>5s} ${total_value:>8.2f}")

# ============================================
# TRY IT YOURSELF:
# 1. Count the frequency of each character in your name
# 2. Group a list of numbers into "even" and "odd" using a dict
# 3. Remove duplicates from a list while preserving order
# ============================================
