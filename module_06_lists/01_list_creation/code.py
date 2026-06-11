# ============================================
# MODULE 6 - SUBTOPIC 1: List Creation
# ============================================

# =============================
# 1. EMPTY LIST
# =============================

# --- Example 1: Creating an empty list ---
my_list = []
print("Empty list:", my_list)
print("Length:", len(my_list))   # 0
print("Type:", type(my_list))   # <class 'list'>

# --- Example 2: Another way to create an empty list ---
another = list()
print("Also empty:", another)   # []

# =============================
# 2. LIST WITH VALUES
# =============================

# --- Example 3: List of integers ---
numbers = [1, 2, 3, 4, 5]
print("\nNumbers:", numbers)

# --- Example 4: List of strings ---
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# --- Example 5: List of booleans ---
flags = [True, False, True, True]
print("Flags:", flags)

# --- Example 6: List of floats ---
prices = [9.99, 14.50, 3.75, 22.00]
print("Prices:", prices)

# =============================
# 3. MIXED DATA TYPES
# =============================

# --- Example 7: Different types in one list ---
mixed = [42, "hello", 3.14, True, None]
print("\nMixed:", mixed)

# --- Example 8: Show type of each element ---
mixed = [10, "Python", 3.14, False]
for item in mixed:
    print(f"  {item} → {type(item)}")

# =============================
# 4. NESTED LISTS
# =============================

# --- Example 9: List of lists ---
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nNested:", nested)
print("First inner list:", nested[0])    # [1, 2, 3]
print("Second inner list:", nested[1])   # [4, 5, 6]

# --- Example 10: Mixed nesting ---
data = ["Trush", [95, 87, 92], True]
print("\nStudent data:", data)
print("Name:", data[0])
print("Scores:", data[1])

# --- Example 11: Nested with different sizes ---
ragged = [[1], [2, 3], [4, 5, 6]]
print("\nRagged list:", ragged)
for row in ragged:
    print(f"  {row} → length {len(row)}")

# =============================
# 5. CREATING LISTS FROM OTHER TYPES
# =============================

# --- Example 12: From a string ---
chars = list("Hello")
print("\nFrom string:", chars)   # ['H', 'e', 'l', 'l', 'o']

# --- Example 13: From a range ---
nums = list(range(5))
print("From range(5):", nums)   # [0, 1, 2, 3, 4]

nums2 = list(range(1, 11))
print("From range(1,11):", nums2)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums3 = list(range(0, 20, 3))
print("From range(0,20,3):", nums3)   # [0, 3, 6, 9, 12, 15, 18]

# =============================
# 6. SINGLE ELEMENT LISTS
# =============================

# --- Example 14: List with one item ---
single = [42]
print("\nSingle item list:", single)
print("Length:", len(single))   # 1

# --- Example 15: Don't confuse with the value itself ---
value = 42
value_list = [42]
print(f"\n42 is type: {type(value)}")          # <class 'int'>
print(f"[42] is type: {type(value_list)}")     # <class 'list'>
print(f"Are they equal? {value == value_list}")  # False

# =============================
# 7. PRACTICAL CREATION PATTERNS
# =============================

# --- Example 16: Build list with a loop ---
squares = []
for i in range(1, 6):
    squares = squares + [i * i]
print("\nSquares:", squares)   # [1, 4, 9, 16, 25]

# --- Example 17: Build from user-like data ---
names_string = "Trush,Rahul,Priya,Dev"
names_list = names_string.split(",")
print("Names:", names_list)   # ['Trush', 'Rahul', 'Priya', 'Dev']

# ============================================
# TRY IT YOURSELF:
# 1. Create a list of 5 of your favorite foods
# 2. Create a mixed list with your name, age, and a boolean
# 3. Create a list from the string "Python" using list()
# ============================================
