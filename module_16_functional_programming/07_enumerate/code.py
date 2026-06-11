# ============================================
# MODULE 16 - SUBTOPIC 7: enumerate()
# ============================================

# enumerate() adds an index counter to any iterable.
# Returns (index, value) pairs.

# =============================
# 1. BASIC enumerate()
# =============================

print("=== Basic enumerate() ===")
print()

fruits = ["apple", "banana", "cherry", "date"]

for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")
print()

# =============================
# 2. CUSTOM START INDEX
# =============================

print("=== Custom Start Index ===")
print()

# Start counting from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}. {fruit}")
print()

# Start from any number
menu_items = ["Burger", "Pizza", "Salad", "Pasta"]
for num, item in enumerate(menu_items, start=101):
    print(f"  Item #{num}: {item}")
print()

# =============================
# 3. enumerate() RETURNS AN ITERATOR
# =============================

print("=== enumerate() is Lazy ===")
print()

colors = ["red", "green", "blue"]
enum_obj = enumerate(colors)

print(f"  Type: {type(enum_obj)}")
print(f"  next(): {next(enum_obj)}")
print(f"  next(): {next(enum_obj)}")
print(f"  next(): {next(enum_obj)}")
print()

# Convert to list
enum_list = list(enumerate(["a", "b", "c"]))
print(f"  As list: {enum_list}")
print()

# =============================
# 4. FINDING ITEMS WITH INDEX
# =============================

print("=== Finding Items with Index ===")
print()

scores = [72, 85, 91, 68, 95, 88, 77]

# Find all scores above 85
print("  Scores above 85:")
for i, score in enumerate(scores):
    if score > 85:
        print(f"    Position {i}: {score}")
print()

# Find first occurrence
target = 91
for i, score in enumerate(scores):
    if score == target:
        print(f"  Found {target} at position {i}")
        break
print()

# =============================
# 5. enumerate() WITH STRINGS
# =============================

print("=== enumerate() with Strings ===")
print()

word = "PYTHON"

for i, char in enumerate(word):
    print(f"  Index {i} → '{char}'")
print()

# Find positions of vowels
text = "Hello World"
vowel_positions = [(i, c) for i, c in enumerate(text) if c.lower() in "aeiou"]
print(f"  Text: '{text}'")
print(f"  Vowel positions: {vowel_positions}")
print()

# =============================
# 6. enumerate() WITH DICTIONARIES
# =============================

print("=== enumerate() with Dictionaries ===")
print()

config = {"host": "localhost", "port": 8080, "debug": True}

# Numbering dictionary items
for i, (key, value) in enumerate(config.items(), 1):
    print(f"  {i}. {key} = {value}")
print()

# =============================
# 7. BUILDING INDEXED DATA
# =============================

print("=== Building Indexed Data ===")
print()

names = ["Trush", "Rahul", "Eve", "Charlie"]

# Create a numbered roster
roster = {i: name for i, name in enumerate(names, 1)}
print(f"  Roster: {roster}")
print()

# Create indexed tuples
indexed = list(enumerate(names, start=100))
print(f"  Indexed list: {indexed}")
print()

# =============================
# 8. enumerate() WITH zip()
# =============================

print("=== enumerate() + zip() ===")
print()

students = ["Trush", "Rahul", "Eve"]
subjects = ["Math", "Science", "English"]
scores = [95, 88, 92]

print("  Report Card:")
for i, (student, subject, score) in enumerate(zip(students, subjects, scores), 1):
    print(f"    {i}. {student} — {subject}: {score}")
print()

# =============================
# 9. PRACTICAL: LINE NUMBERING
# =============================

print("=== Practical: Line Numbering ===")
print()

poem = """Roses are red
Violets are blue
Python is great
And so are you"""

lines = poem.strip().split("\n")

print("  Numbered poem:")
for line_num, line in enumerate(lines, 1):
    print(f"    {line_num:2}| {line}")
print()

# =============================
# 10. COMPARING WITH AND WITHOUT enumerate()
# =============================

print("=== With vs Without enumerate() ===")
print()

items = ["alpha", "beta", "gamma", "delta"]

# Without enumerate — manual counter (avoid this)
print("  Without enumerate:")
i = 0
for item in items:
    print(f"    {i}: {item}")
    i += 1
print()

# With enumerate — clean and Pythonic
print("  With enumerate:")
for i, item in enumerate(items):
    print(f"    {i}: {item}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use enumerate to find all positions of a character
#    in a string
# 2. Use enumerate to create a numbered menu from a list
# 3. Combine enumerate with zip to create a formatted
#    table with row numbers
# ============================================
