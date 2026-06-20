# ============================================
# MODULE 7 - SUBTOPIC 2: Tuple Access
# ============================================

# =============================
# 1. POSITIVE INDEXING
# =============================

# --- Example 1: Basic positive indexing ---
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("Index 0:", fruits[0])   # apple
print("Index 1:", fruits[1])   # banana
print("Index 4:", fruits[4])   # elderberry

# --- Example 2: First and last with positive index ---
numbers = (10, 20, 30, 40, 50)
print("\nFirst:", numbers[0])    # 10
print("Last:", numbers[4])      # 50

# =============================
# 2. NEGATIVE INDEXING
# =============================

# --- Example 3: Negative indexing ---
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("\nLast:", fruits[-1])      # elderberry
print("Second last:", fruits[-2])   # date
print("First:", fruits[-5])      # apple

# --- Example 4: Comparing positive and negative ---
colors = ("red", "green", "blue", "yellow")
print(f"\ncolors[0] = {colors[0]}, colors[-4] = {colors[-4]}")   # same
print(f"colors[3] = {colors[3]}, colors[-1] = {colors[-1]}")     # same

# =============================
# 3. SLICING
# =============================

# --- Example 5: Basic slicing ---
numbers = (10, 20, 30, 40, 50, 60)
print("\nnumbers[1:4]:", numbers[1:4])   # (20, 30, 40)
print("numbers[:3]:", numbers[:3])       # (10, 20, 30)
print("numbers[3:]:", numbers[3:])       # (40, 50, 60)

# --- Example 6: Full slice (copy) ---
copy = numbers[:]
print("Full copy:", copy)   # (10, 20, 30, 40, 50, 60)

# --- Example 7: Negative slicing ---
print("\nnumbers[-3:]:", numbers[-3:])     # (40, 50, 60)
print("numbers[:-2]:", numbers[:-2])       # (10, 20, 30, 40)

# =============================
# 4. STEP SLICING
# =============================

# --- Example 8: Every 2nd element ---
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("\nEvery 2nd:", numbers[::2])    # (0, 2, 4, 6, 8)
print("Every 3rd:", numbers[::3])      # (0, 3, 6, 9)

# --- Example 9: Step with start ---
print("From index 1, step 2:", numbers[1::2])   # (1, 3, 5, 7, 9)

# --- Example 10: Reversing a tuple ---
original = (1, 2, 3, 4, 5)
reversed_tuple = original[::-1]
print("\nOriginal:", original)
print("Reversed:", reversed_tuple)   # (5, 4, 3, 2, 1)

# =============================
# 5. ACCESSING NESTED TUPLES
# =============================

# --- Example 11: Nested tuple access ---
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("\nRow 0:", matrix[0])        # (1, 2, 3)
print("Row 1, Col 2:", matrix[1][2])   # 6
print("Row 2, Col 0:", matrix[2][0])   # 7

# --- Example 12: Mixed nested tuple ---
student = ("Trush", (95, 87, 92), "A")
print("\nName:", student[0])
print("Second score:", student[1][1])   # 87
print("Grade:", student[2])

# --- Example 13: Iterating with index ---
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
for i in range(len(weekdays)):
    print(f"  Index {i}: {weekdays[i]}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a tuple of 5 numbers and print the middle element
# 2. Slice a tuple to get only the last 3 elements
# 3. Reverse a tuple using slicing
# ============================================
