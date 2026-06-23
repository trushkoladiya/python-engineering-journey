# ============================================
# MODULE 7 - SUBTOPIC 13: Set Membership & Iteration
# ============================================

# =============================
# 1. MEMBERSHIP — in / not in
# =============================

# --- Example 1: Basic membership check ---
fruits = {"apple", "banana", "cherry", "date"}
print("'apple' in fruits:", "apple" in fruits)       # True
print("'mango' in fruits:", "mango" in fruits)        # False
print("'mango' not in fruits:", "mango" not in fruits)  # True

# --- Example 2: Using membership in conditions ---
valid_colors = {"red", "green", "blue", "yellow", "purple"}
chosen = "green"

if chosen in valid_colors:
    print(f"\n'{chosen}' is a valid color ✓")
else:
    print(f"\n'{chosen}' is NOT a valid color ✗")

# --- Example 3: Checking multiple items ---
required_skills = {"Python", "SQL", "Git"}
my_skills = {"Python", "JavaScript", "Git", "Docker"}

print("\nSkill check:")
for skill in required_skills:
    if skill in my_skills:
        print(f"  ✓ {skill}")
    else:
        print(f"  ✗ {skill} (missing!)")

# =============================
# 2. LOOPING THROUGH SETS
# =============================

# --- Example 4: Basic for loop ---
colors = {"red", "green", "blue", "yellow"}
print("\nColors:")
for color in colors:
    print(f"  - {color}")

# --- Example 5: Looping with action ---
numbers = {10, 20, 30, 40, 50}
total = 0
for num in numbers:
    total = total + num
print(f"\nSum of {numbers}: {total}")

# --- Example 6: Building a new collection from a set ---
words = {"hello", "world", "python", "code"}
upper_words = []
for word in words:
    upper_words.append(word.upper())
print(f"\nOriginal: {words}")
print(f"Uppercase: {upper_words}")

# =============================
# 3. LOOPING WITH ENUMERATE
# =============================

# --- Example 7: Enumerate with set ---
fruits = {"apple", "banana", "cherry", "date"}
print("\nFruits (numbered):")
for i, fruit in enumerate(fruits):
    print(f"  {i + 1}. {fruit}")

# --- Example 8: Enumerate starting from 1 ---
animals = {"cat", "dog", "bird", "fish"}
print("\nAnimals:")
for i, animal in enumerate(animals, start=1):
    print(f"  {i}. {animal}")

# =============================
# 4. FILTERING WHILE ITERATING
# =============================

# --- Example 9: Collecting elements that match a condition ---
numbers = {15, 8, 23, 4, 17, 42, 6, 31}
big_numbers = set()
small_numbers = set()

for num in numbers:
    if num >= 20:
        big_numbers.add(num)
    else:
        small_numbers.add(num)

print(f"\nAll: {numbers}")
print(f"Big (≥20):  {big_numbers}")
print(f"Small (<20): {small_numbers}")

# --- Example 10: Finding items in common ---
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [5, 6, 7, 8, 9, 10]

set_a = set(list_a)
common = []
for item in list_b:
    if item in set_a:   # Fast lookup in set!
        common.append(item)

print(f"\nList A: {list_a}")
print(f"List B: {list_b}")
print(f"Common: {common}")

# =============================
# 5. PRACTICAL EXAMPLES
# =============================

# --- Example 11: Unique visitor tracking ---
visitors = set()
page_views = ["Trush", "Rahul", "Trush", "Charlie", "Rahul", "Diana", "Trush"]

print("\nTracking visitors:")
for visitor in page_views:
    if visitor not in visitors:
        print(f"  New visitor: {visitor}")
        visitors.add(visitor)
    else:
        print(f"  Returning:   {visitor}")

print(f"Total unique visitors: {len(visitors)}")

# --- Example 12: Sorted iteration ---
scores = {88, 95, 72, 85, 91, 78}
print(f"\nScores (sorted):")
for score in sorted(scores):
    print(f"  {score}")

print(f"\nScores (sorted descending):")
for score in sorted(scores, reverse=True):
    print(f"  {score}")

# ============================================
# TRY IT YOURSELF:
# 1. Check if "Python" is in a set of programming languages
# 2. Loop through a set of numbers and print only even ones
# 3. Track unique words in a sentence using a set
# ============================================
