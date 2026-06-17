# ============================================
# MODULE 6 - SUBTOPIC 5: List Operations
# ============================================

# =============================
# 1. CONCATENATION (+)
# =============================

# --- Example 1: Basic concatenation ---
a = [1, 2, 3]
b = [4, 5, 6]
combined = a + b
print("a + b:", combined)   # [1, 2, 3, 4, 5, 6]

# --- Example 2: Originals unchanged ---
print("a:", a)   # [1, 2, 3] — unchanged
print("b:", b)   # [4, 5, 6] — unchanged

# --- Example 3: Concatenate multiple ---
x = [1]
y = [2]
z = [3]
all_together = x + y + z
print("\nx + y + z:", all_together)   # [1, 2, 3]

# --- Example 4: Concatenate different types ---
nums = [1, 2, 3]
words = ["hello", "world"]
mixed = nums + words
print("Mixed:", mixed)   # [1, 2, 3, 'hello', 'world']

# --- Example 5: Building a list with + ---
result = []
for i in range(5):
    result = result + [i * 10]
print("\nBuilt with +:", result)   # [0, 10, 20, 30, 40]

# =============================
# 2. REPETITION (*)
# =============================

# --- Example 6: Repeat a list ---
zeros = [0] * 5
print("\n[0] * 5:", zeros)   # [0, 0, 0, 0, 0]

# --- Example 7: Repeat a pattern ---
pattern = [1, 2, 3] * 3
print("[1,2,3] * 3:", pattern)   # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# --- Example 8: Initialize a list ---
empty_slots = [None] * 4
print("Slots:", empty_slots)   # [None, None, None, None]

# --- Example 9: Repeat strings ---
dashes = ["-"] * 10
print("Dashes:", dashes)
print("Joined:", "".join(dashes))

# =============================
# 3. MEMBERSHIP (in, not in)
# =============================

# --- Example 10: Check if element exists ---
fruits = ["apple", "banana", "cherry"]
print("\n'banana' in fruits:", "banana" in fruits)     # True
print("'grape' in fruits:", "grape" in fruits)         # False
print("'grape' not in fruits:", "grape" not in fruits) # True

# --- Example 11: Membership with numbers ---
primes = [2, 3, 5, 7, 11, 13]
for num in range(1, 15):
    if num in primes:
        print(f"  {num} is prime")

# --- Example 12: Search in a list ---
colors = ["red", "green", "blue", "yellow"]
search = "blue"
print()
if search in colors:
    print(f"Found '{search}' in the list!")
else:
    print(f"'{search}' not found")

# --- Example 13: Case-sensitive membership ---
names = ["Trush", "Rahul", "Priya"]
print("\n'trush' in names:", "trush" in names)   # False — case matters!
print("'Trush' in names:", "Trush" in names)    # True

# =============================
# 4. LENGTH (len())
# =============================

# --- Example 14: Basic length ---
nums = [10, 20, 30, 40]
print("\nLength:", len(nums))   # 4

# --- Example 15: Empty list length ---
empty = []
print("Empty length:", len(empty))   # 0

# --- Example 16: Nested list length ---
nested = [[1, 2], [3, 4], [5, 6]]
print("Nested length:", len(nested))       # 3 (three inner lists)
print("Inner length:", len(nested[0]))     # 2 (first inner list has 2 items)

# =============================
# 5. COMBINING OPERATIONS
# =============================

# --- Example 17: Add element only if not present ---
shopping = ["milk", "bread", "eggs"]
new_item = "bread"
if new_item not in shopping:
    shopping = shopping + [new_item]
    print(f"Added '{new_item}'")
else:
    print(f"'{new_item}' already in list")
print("Shopping:", shopping)

# --- Example 18: Merge and check length ---
list1 = [1, 2, 3]
list2 = [4, 5]
merged = list1 + list2
print(f"\nMerged {len(list1)} + {len(list2)} = {len(merged)} items")
print("Merged:", merged)

# --- Example 19: Create grid with repetition ---
row = [0] * 5
print("\nRow:", row)
print("Grid (3 rows):")
for i in range(3):
    print(f"  Row {i}: {[0] * 5}")

# ============================================
# TRY IT YOURSELF:
# 1. Concatenate [1, 2] and [3, 4] and print the result
# 2. Create a list of 10 zeros using repetition
# 3. Check if "python" is in ["Python", "Java", "Go"]
# ============================================
