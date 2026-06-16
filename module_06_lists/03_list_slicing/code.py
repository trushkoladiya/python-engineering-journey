# ============================================
# MODULE 6 - SUBTOPIC 3: List Slicing
# ============================================

# =============================
# 1. BASIC SLICING (start:end)
# =============================

# --- Example 1: Extract a portion ---
nums = [10, 20, 30, 40, 50]
print("nums[1:4]:", nums[1:4])   # [20, 30, 40]
print("nums[0:3]:", nums[0:3])   # [10, 20, 30]
print("nums[2:5]:", nums[2:5])   # [30, 40, 50]

# --- Example 2: Slicing strings list ---
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("\nFirst 3 fruits:", fruits[0:3])
print("Last 2 fruits:", fruits[3:5])

# =============================
# 2. OMITTING START OR END
# =============================

# --- Example 3: Omit start ---
nums = [10, 20, 30, 40, 50]
print("\nnums[:3]:", nums[:3])    # [10, 20, 30]
print("nums[:1]:", nums[:1])    # [10]

# --- Example 4: Omit end ---
print("nums[2:]:", nums[2:])    # [30, 40, 50]
print("nums[4:]:", nums[4:])    # [50]

# --- Example 5: Omit both (full copy) ---
print("nums[:]:", nums[:])      # [10, 20, 30, 40, 50]

# =============================
# 3. NEGATIVE INDICES IN SLICING
# =============================

# --- Example 6: Negative start and end ---
nums = [10, 20, 30, 40, 50]
print("\nnums[-3:]:", nums[-3:])      # [30, 40, 50] — last 3
print("nums[-4:-1]:", nums[-4:-1])  # [20, 30, 40]
print("nums[:-2]:", nums[:-2])      # [10, 20, 30]

# --- Example 7: Getting last N elements ---
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nLast 3:", data[-3:])   # [8, 9, 10]
print("Last 5:", data[-5:])    # [6, 7, 8, 9, 10]

# =============================
# 4. STEP SLICING
# =============================

# --- Example 8: Every 2nd element ---
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nEvery 2nd:", nums[::2])      # [0, 2, 4, 6, 8]
print("Every 2nd from 1:", nums[1::2])  # [1, 3, 5, 7, 9]

# --- Example 9: Every 3rd element ---
print("Every 3rd:", nums[::3])      # [0, 3, 6, 9]

# --- Example 10: Step with start and end ---
print("nums[1:8:2]:", nums[1:8:2])   # [1, 3, 5, 7]

# =============================
# 5. REVERSING A LIST
# =============================

# --- Example 11: Reverse with [::-1] ---
nums = [1, 2, 3, 4, 5]
reversed_nums = nums[::-1]
print("\nOriginal:", nums)
print("Reversed:", reversed_nums)   # [5, 4, 3, 2, 1]

# --- Example 12: Reverse strings list ---
words = ["Hello", "World", "Python"]
print("Reversed words:", words[::-1])   # ['Python', 'World', 'Hello']

# =============================
# 6. COPYING WITH SLICING
# =============================

# --- Example 13: Slice copy vs direct assignment ---
original = [1, 2, 3, 4, 5]
copy = original[:]       # creates a separate copy
reference = original     # points to the SAME list

original[0] = 999
print("\nAfter changing original[0] to 999:")
print("Original:", original)    # [999, 2, 3, 4, 5]
print("Copy:", copy)            # [1, 2, 3, 4, 5]  ← unchanged!
print("Reference:", reference)  # [999, 2, 3, 4, 5] ← also changed!

# =============================
# 7. SLICE ASSIGNMENT
# =============================

# --- Example 14: Replace a section of a list ---
nums = [1, 2, 3, 4, 5]
nums[1:4] = [20, 30, 40]
print("\nAfter slice assignment:", nums)   # [1, 20, 30, 40, 5]

# --- Example 15: Replace with different length ---
nums = [1, 2, 3, 4, 5]
nums[1:4] = [99]
print("Replace 3 with 1:", nums)   # [1, 99, 5]

# --- Example 16: Insert with slice ---
nums = [1, 2, 5, 6]
nums[2:2] = [3, 4]    # insert at index 2
print("After insert:", nums)   # [1, 2, 3, 4, 5, 6]

# =============================
# 8. PRACTICAL PATTERNS
# =============================

# --- Example 17: Split list into halves ---
data = [1, 2, 3, 4, 5, 6, 7, 8]
mid = len(data) // 2
first_half = data[:mid]
second_half = data[mid:]
print(f"\nFull: {data}")
print(f"First half: {first_half}")
print(f"Second half: {second_half}")

# --- Example 18: Remove first and last ---
items = [0, 1, 2, 3, 4, 5, 0]
middle = items[1:-1]
print(f"\nFull: {items}")
print(f"Without first and last: {middle}")

# --- Example 19: Out-of-range slicing is safe ---
small = [1, 2, 3]
print(f"\nsmall[0:100]: {small[0:100]}")   # [1, 2, 3] — no error
print(f"small[10:20]: {small[10:20]}")     # [] — empty list

# ============================================
# TRY IT YOURSELF:
# 1. Extract the first 3 and last 3 elements of [1,2,3,4,5,6,7,8,9,10]
# 2. Reverse the list ["a", "b", "c", "d"] using slicing
# 3. Get every 3rd element from list(range(20))
# ============================================
