# ============================================
# MODULE 6 - SUBTOPIC 6: List Methods (Core)
# ============================================

# =============================
# 1. APPEND() — Add one item to the end
# =============================

# --- Example 1: Basic append ---
fruits = ["apple", "banana"]
print("Before:", fruits)
fruits.append("cherry")
print("After append:", fruits)   # ['apple', 'banana', 'cherry']

# --- Example 2: Append in a loop ---
squares = []
for i in range(1, 6):
    squares.append(i * i)
print("\nSquares:", squares)   # [1, 4, 9, 16, 25]

# --- Example 3: Append vs concatenation ---
nums = [1, 2, 3]
nums.append(4)          # ✅ modifies in place, efficient
# nums = nums + [4]     # also works, but creates new list
print("After append:", nums)

# --- Example 4: Append adds ONE item (even if it's a list) ---
a = [1, 2, 3]
a.append([4, 5])
print("\nAppend a list:", a)   # [1, 2, 3, [4, 5]] — nested!

# =============================
# 2. EXTEND() — Add multiple items
# =============================

# --- Example 5: Basic extend ---
a = [1, 2, 3]
a.extend([4, 5, 6])
print("\nAfter extend:", a)   # [1, 2, 3, 4, 5, 6]

# --- Example 6: Extend from a string ---
letters = ["a", "b"]
letters.extend("cde")
print("Extend from string:", letters)   # ['a', 'b', 'c', 'd', 'e']

# --- Example 7: Append vs Extend comparison ---
list1 = [1, 2, 3]
list1.append([4, 5])
print("\nappend([4,5]):", list1)    # [1, 2, 3, [4, 5]]

list2 = [1, 2, 3]
list2.extend([4, 5])
print("extend([4,5]):", list2)     # [1, 2, 3, 4, 5]

# =============================
# 3. INSERT() — Add at specific position
# =============================

# --- Example 8: Insert at beginning ---
nums = [2, 3, 4]
nums.insert(0, 1)
print("\nInsert at 0:", nums)   # [1, 2, 3, 4]

# --- Example 9: Insert in the middle ---
fruits = ["apple", "cherry", "date"]
fruits.insert(1, "banana")
print("Insert at 1:", fruits)   # ['apple', 'banana', 'cherry', 'date']

# --- Example 10: Insert at the end (same as append) ---
nums = [1, 2, 3]
nums.insert(len(nums), 4)
print("Insert at end:", nums)   # [1, 2, 3, 4]

# =============================
# 4. REMOVE() — Remove by value
# =============================

# --- Example 11: Remove first occurrence ---
nums = [1, 2, 3, 2, 1]
print("\nBefore:", nums)
nums.remove(2)
print("After remove(2):", nums)   # [1, 3, 2, 1] — only first 2

# --- Example 12: Safe removal (check first) ---
colors = ["red", "green", "blue"]
target = "yellow"
if target in colors:
    colors.remove(target)
    print(f"Removed '{target}'")
else:
    print(f"'{target}' not found in list")

# --- Example 13: Remove all occurrences ---
nums = [1, 2, 3, 2, 4, 2, 5]
print("\nBefore:", nums)
while 2 in nums:
    nums.remove(2)
print("After removing all 2s:", nums)   # [1, 3, 4, 5]

# =============================
# 5. POP() — Remove by index and return
# =============================

# --- Example 14: Pop last item (default) ---
fruits = ["apple", "banana", "cherry"]
last = fruits.pop()
print(f"\nPopped: '{last}'")
print("Remaining:", fruits)   # ['apple', 'banana']

# --- Example 15: Pop at specific index ---
nums = [10, 20, 30, 40, 50]
second = nums.pop(1)
print(f"\nPopped index 1: {second}")
print("Remaining:", nums)   # [10, 30, 40, 50]

# --- Example 16: Pop first item ---
items = ["a", "b", "c"]
first = items.pop(0)
print(f"\nPopped first: '{first}'")
print("Remaining:", items)   # ['b', 'c']

# --- Example 17: Pop until empty ---
stack = [1, 2, 3, 4, 5]
print("\nPopping all:")
while len(stack) > 0:
    item = stack.pop()
    print(f"  Popped: {item}, remaining: {stack}")

# =============================
# 6. CLEAR() — Remove all items
# =============================

# --- Example 18: Clear a list ---
data = [1, 2, 3, 4, 5]
print("\nBefore clear:", data)
data.clear()
print("After clear:", data)   # []
print("Length:", len(data))   # 0

# =============================
# 7. DEL STATEMENT
# =============================

# --- Example 19: Delete by index ---
nums = [10, 20, 30, 40, 50]
print("\nBefore del:", nums)
del nums[2]
print("After del [2]:", nums)   # [10, 20, 40, 50]

# --- Example 20: Delete a slice ---
nums = [1, 2, 3, 4, 5, 6, 7]
del nums[2:5]
print("After del [2:5]:", nums)   # [1, 2, 6, 7]

# =============================
# 8. PRACTICAL PATTERNS
# =============================

# --- Example 21: Build a filtered list ---
all_nums = [1, -2, 3, -4, 5, -6, 7]
positives = []
for num in all_nums:
    if num > 0:
        positives.append(num)
print(f"\nAll: {all_nums}")
print(f"Positives: {positives}")

# --- Example 22: Collect unique items ---
items = ["a", "b", "a", "c", "b", "d"]
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
print(f"\nOriginal: {items}")
print(f"Unique: {unique}")

# ============================================
# TRY IT YOURSELF:
# 1. Start with an empty list, append 5 numbers, then pop the last
# 2. Insert "start" at the beginning of ["middle", "end"]
# 3. Remove all occurrences of 0 from [0, 1, 0, 2, 0, 3]
# ============================================
