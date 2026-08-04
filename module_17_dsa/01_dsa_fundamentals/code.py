# ============================================
# MODULE 17 - SUBTOPIC 1: DSA Fundamentals
# ============================================

# DSA = Data Structures + Algorithms
# Data Structure = how you ORGANIZE data
# Algorithm = how you PROCESS data

# =============================
# 1. DATA STRUCTURES YOU ALREADY KNOW
# =============================

print("=== Data Structures You Already Know ===")
print()

# List — ordered, mutable
names = ["Trush", "Rahul", "Charlie"]
print(f"  List: {names}")

# Dict — key-value pairs, fast lookup
ages = {"Trush": 21, "Rahul": 25, "Charlie": 35}
print(f"  Dict: {ages}")

# Set — unique items, fast membership check
unique_numbers = {3, 1, 4, 1, 5, 9}
print(f"  Set: {unique_numbers}")

# Tuple — ordered, immutable
point = (10, 20)
print(f"  Tuple: {point}")
print()

# =============================
# 2. ALGORITHMS YOU ALREADY USE
# =============================

print("=== Algorithms You Already Use ===")
print()

# Algorithm 1: Finding the maximum
numbers = [34, 12, 89, 45, 67, 23]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(f"  Numbers: {numbers}")
print(f"  Largest: {largest}")
print()

# Algorithm 2: Counting occurrences
text = "hello world hello python hello"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"  Text: '{text}'")
print(f"  Word counts: {word_count}")
print()

# =============================
# 3. CHOOSING THE RIGHT STRUCTURE
# =============================

print("=== Choosing the Right Structure ===")
print()

# Problem: Check if a value exists in a collection

import time

# Using a LIST — must check each element
big_list = list(range(100_000))
start = time.time()
result = 99_999 in big_list
list_time = time.time() - start
print(f"  Search in list: {result} (took {list_time:.6f}s)")

# Using a SET — instant lookup
big_set = set(range(100_000))
start = time.time()
result = 99_999 in big_set
set_time = time.time() - start
print(f"  Search in set:  {result} (took {set_time:.6f}s)")

if list_time > 0 and set_time > 0:
    print(f"  Set was roughly {list_time / set_time:.0f}x faster!")
else:
    print("  Set is dramatically faster for lookups!")
print()

# =============================
# 4. WHAT MAKES AN ALGORITHM GOOD?
# =============================

print("=== What Makes an Algorithm Good? ===")
print()

# Two ways to sum numbers from 1 to N

# Method 1: Loop (slow for huge N)
def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Method 2: Formula (instant for any N)
def sum_formula(n):
    return n * (n + 1) // 2

n = 1_000_000

start = time.time()
result1 = sum_loop(n)
time1 = time.time() - start

start = time.time()
result2 = sum_formula(n)
time2 = time.time() - start

print(f"  Sum 1 to {n:,}:")
print(f"    Loop:    {result1:,} (took {time1:.6f}s)")
print(f"    Formula: {result2:,} (took {time2:.6f}s)")
print(f"    Both correct: {result1 == result2}")
print()

# =============================
# 5. THE DSA MINDSET
# =============================

print("=== The DSA Mindset ===")
print()

# Problem: Find duplicate values in a list

items = [4, 2, 7, 2, 9, 4, 1, 7, 3]

# Approach 1: Brute force — check every pair (slow)
duplicates_v1 = []
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i] == items[j] and items[i] not in duplicates_v1:
            duplicates_v1.append(items[i])

print(f"  Items: {items}")
print(f"  Duplicates (brute force): {duplicates_v1}")

# Approach 2: Use a set to track seen items (fast)
seen = set()
duplicates_v2 = set()
for item in items:
    if item in seen:
        duplicates_v2.add(item)
    seen.add(item)

print(f"  Duplicates (set-based):   {sorted(duplicates_v2)}")
print()

# The set-based approach is smarter:
# - It scans the list ONCE
# - Uses a set for instant lookups
# - This is DSA thinking!

# =============================
# 6. ORGANIZING DATA FOR A TASK
# =============================

print("=== Organizing Data For a Task ===")
print()

# Task: Build a contact lookup system

# Bad: searching a list of tuples
contacts_list = [
    ("Trush", "555-0001"),
    ("Rahul", "555-0002"),
    ("Charlie", "555-0003"),
    ("Diana", "555-0004"),
]

# To find Rahul, we must scan the list
def find_in_list(name, contacts):
    for n, phone in contacts:
        if n == name:
            return phone
    return None

print(f"  List search for Rahul: {find_in_list('Rahul', contacts_list)}")

# Better: use a dictionary for direct lookup
contacts_dict = {name: phone for name, phone in contacts_list}

print(f"  Dict lookup for Rahul: {contacts_dict['Rahul']}")
print()

# The dict is the RIGHT structure for lookups
# The list is the RIGHT structure for ordered sequences
# Choosing correctly = DSA thinking

# ============================================
# TRY IT YOURSELF:
# 1. Find the second largest number in a list
#    without using sort()
# 2. Count how many unique words are in a sentence
#    (hint: which data structure makes this trivial?)
# 3. Compare the speed of checking membership in
#    a list vs a set with 1 million elements
# ============================================
