# ============================================
# MODULE 7 - SUBTOPIC 5: Tuple Methods
# ============================================

# Tuples have ONLY two methods: count() and index()

# =============================
# 1. count() — COUNT OCCURRENCES
# =============================

# --- Example 1: Basic count ---
numbers = (1, 2, 3, 2, 4, 2, 5, 2)
print("Tuple:", numbers)
print("Count of 2:", numbers.count(2))   # 4
print("Count of 5:", numbers.count(5))   # 1
print("Count of 9:", numbers.count(9))   # 0 (not found)

# --- Example 2: Counting strings ---
colors = ("red", "blue", "red", "green", "red", "blue")
print("\nColors:", colors)
print("Count of 'red':", colors.count("red"))     # 3
print("Count of 'blue':", colors.count("blue"))    # 2
print("Count of 'yellow':", colors.count("yellow"))  # 0

# --- Example 3: Counting in a grades tuple ---
grades = ("A", "B", "A", "C", "B", "A", "B", "A")
print("\nGrades:", grades)
print("Number of A's:", grades.count("A"))   # 4
print("Number of B's:", grades.count("B"))   # 3
print("Number of C's:", grades.count("C"))   # 1

# =============================
# 2. index() — FIND POSITION
# =============================

# --- Example 4: Basic index ---
fruits = ("apple", "banana", "cherry", "date")
print("\nFruits:", fruits)
print("Index of 'banana':", fruits.index("banana"))   # 1
print("Index of 'cherry':", fruits.index("cherry"))    # 2

# --- Example 5: First occurrence only ---
letters = ("a", "b", "c", "b", "d", "b")
print("\nLetters:", letters)
print("Index of 'b':", letters.index("b"))   # 1 (first occurrence)

# --- Example 6: index() with start parameter ---
numbers = (10, 20, 30, 20, 40, 20, 50)
print("\nNumbers:", numbers)
print("First 20 at:", numbers.index(20))        # 1
print("Next 20 after index 2:", numbers.index(20, 2))   # 3
print("Next 20 after index 4:", numbers.index(20, 4))    # 5

# --- Example 7: index() with start and end ---
data = (5, 10, 15, 10, 20, 10, 25)
print("\nData:", data)
print("10 between index 2 and 5:", data.index(10, 2, 5))   # 3

# =============================
# 3. SAFE SEARCH WITH in + index()
# =============================

# --- Example 8: Check before using index ---
fruits = ("apple", "banana", "cherry")
search = "mango"

if search in fruits:
    position = fruits.index(search)
    print(f"\n'{search}' found at index {position}")
else:
    print(f"\n'{search}' is not in the tuple")

# --- Example 9: Safe search for multiple items ---
colors = ("red", "green", "blue", "yellow", "purple")
to_find = ("green", "orange", "purple")

print("\nSearching in colors:")
for item in to_find:
    if item in colors:
        print(f"  '{item}' found at index {colors.index(item)}")
    else:
        print(f"  '{item}' not found")

# =============================
# 4. PRACTICAL EXAMPLES
# =============================

# --- Example 10: Finding most common element ---
votes = ("A", "B", "A", "C", "A", "B", "A", "C", "B", "A")
print("\nVotes:", votes)

candidates = ("A", "B", "C")
for candidate in candidates:
    count = votes.count(candidate)
    print(f"  Candidate {candidate}: {count} votes")

# --- Example 11: Finding all positions of an element ---
data = (5, 10, 5, 20, 5, 30, 5)
target = 5
positions = []

for i in range(len(data)):
    if data[i] == target:
        positions.append(i)

print(f"\n{target} found at positions: {positions}")   # [0, 2, 4, 6]

# ============================================
# TRY IT YOURSELF:
# 1. Count how many times "hello" appears in a tuple
# 2. Find the index of the number 50 in a tuple of numbers
# 3. Safely search for an element using in before index()
# ============================================
