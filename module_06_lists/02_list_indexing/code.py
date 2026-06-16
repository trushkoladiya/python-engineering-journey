# ============================================
# MODULE 6 - SUBTOPIC 2: List Indexing
# ============================================

# =============================
# 1. POSITIVE INDEXING
# =============================

# --- Example 1: Access elements by position ---
fruits = ["apple", "banana", "cherry", "date"]
print("fruits[0]:", fruits[0])   # apple
print("fruits[1]:", fruits[1])   # banana
print("fruits[2]:", fruits[2])   # cherry
print("fruits[3]:", fruits[3])   # date

# --- Example 2: Index positions ---
colors = ["red", "green", "blue", "yellow", "purple"]
print("\nAll colors with indices:")
for i in range(len(colors)):
    print(f"  Index {i} → {colors[i]}")

# =============================
# 2. NEGATIVE INDEXING
# =============================

# --- Example 3: Counting from the end ---
fruits = ["apple", "banana", "cherry", "date"]
print("\nNegative indexing:")
print("fruits[-1]:", fruits[-1])   # date
print("fruits[-2]:", fruits[-2])   # cherry
print("fruits[-3]:", fruits[-3])   # banana
print("fruits[-4]:", fruits[-4])   # apple

# --- Example 4: Last element of any list ---
numbers = [10, 20, 30, 40, 50]
print("\nLast element:", numbers[-1])   # 50

names = ["Trush", "Rahul"]
print("Last name:", names[-1])   # Rahul

# =============================
# 3. POSITIVE VS NEGATIVE
# =============================

# --- Example 5: Same element, different index ---
letters = ["a", "b", "c", "d", "e"]
print("\nComparing indices:")
print(f"letters[0] = {letters[0]}, letters[-5] = {letters[-5]}")   # a
print(f"letters[4] = {letters[4]}, letters[-1] = {letters[-1]}")   # e
print(f"Same? {letters[0] == letters[-5]}")   # True

# =============================
# 4. ACCESSING NESTED ELEMENTS
# =============================

# --- Example 6: Nested list indexing ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nNested list:")
print("matrix[0]:", matrix[0])       # [1, 2, 3]
print("matrix[0][0]:", matrix[0][0]) # 1
print("matrix[1][2]:", matrix[1][2]) # 6
print("matrix[2][-1]:", matrix[2][-1]) # 9

# --- Example 7: Mixed nested ---
student = ["Trush", [90, 85, 95]]
print(f"\nName: {student[0]}")
print(f"First score: {student[1][0]}")
print(f"Last score: {student[1][-1]}")

# =============================
# 5. SAFE INDEXING
# =============================

# --- Example 8: Check index before access ---
items = ["a", "b", "c"]
index = 5
if index < len(items):
    print(f"\nItem at {index}: {items[index]}")
else:
    print(f"\nIndex {index} is out of range (list has {len(items)} items)")

# --- Example 9: Safe access in a loop ---
data = [10, 20, 30]
print("\nSafe access:")
for i in range(5):
    if i < len(data):
        print(f"  Index {i} → {data[i]}")
    else:
        print(f"  Index {i} → OUT OF RANGE")

# =============================
# 6. PRACTICAL PATTERNS
# =============================

# --- Example 10: First, middle, last ---
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]
print(f"\nFirst: {first}, Middle: {middle}, Last: {last}")

# --- Example 11: Swap first and last ---
items = [1, 2, 3, 4, 5]
print("\nBefore swap:", items)
temp = items[0]
items[0] = items[-1]
items[-1] = temp
print("After swap:", items)   # [5, 2, 3, 4, 1]

# ============================================
# TRY IT YOURSELF:
# 1. Create a list and print its first and last elements
# 2. Access the middle element of a 7-item list
# 3. Create a nested list and access an inner element
# ============================================
