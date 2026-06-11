# ============================================
# MODULE 6 - SUBTOPIC 4: List Mutability
# ============================================

# =============================
# 1. MODIFYING ELEMENTS
# =============================

# --- Example 1: Change a single element ---
fruits = ["apple", "banana", "cherry"]
print("Before:", fruits)
fruits[1] = "blueberry"
print("After:", fruits)   # ['apple', 'blueberry', 'cherry']

# --- Example 2: Change first and last ---
numbers = [10, 20, 30, 40, 50]
print("\nBefore:", numbers)
numbers[0] = 100
numbers[-1] = 500
print("After:", numbers)   # [100, 20, 30, 40, 500]

# --- Example 3: Update using current value ---
scores = [80, 90, 70]
print("\nBefore:", scores)
scores[2] = scores[2] + 10   # add 10 to the third score
print("After:", scores)   # [80, 90, 80]

# =============================
# 2. UPDATING WITH LOOPS
# =============================

# --- Example 4: Double every element ---
nums = [1, 2, 3, 4, 5]
print("\nBefore doubling:", nums)
for i in range(len(nums)):
    nums[i] = nums[i] * 2
print("After doubling:", nums)   # [2, 4, 6, 8, 10]

# --- Example 5: Capitalize all strings ---
words = ["hello", "world", "python"]
print("\nBefore:", words)
for i in range(len(words)):
    words[i] = words[i].upper()
print("After:", words)   # ['HELLO', 'WORLD', 'PYTHON']

# =============================
# 3. DIFFERENCE FROM STRINGS
# =============================

# --- Example 6: Strings are immutable ---
word = "Hello"
# word[0] = "J"   # ❌ This would cause TypeError
print("\nString 'Hello' cannot be changed in place")

# --- Example 7: Lists ARE mutable ---
letters = list("Hello")   # ['H', 'e', 'l', 'l', 'o']
print("List from string:", letters)
letters[0] = "J"
print("After change:", letters)   # ['J', 'e', 'l', 'l', 'o']
print("Joined back:", "".join(letters))   # Jello

# --- Example 8: Side-by-side comparison ---
print("\n--- Mutable vs Immutable ---")
# String: must create a new string
original_str = "Cat"
new_str = "B" + original_str[1:]
print(f"String: '{original_str}' → '{new_str}' (new string created)")

# List: change in place
original_list = ["C", "a", "t"]
original_list[0] = "B"
print(f"List: changed in place → {original_list}")

# =============================
# 4. SLICE MODIFICATION
# =============================

# --- Example 9: Replace a section ---
nums = [1, 2, 3, 4, 5]
print("\nBefore:", nums)
nums[1:3] = [20, 30]
print("After nums[1:3] = [20, 30]:", nums)   # [1, 20, 30, 4, 5]

# --- Example 10: Replace with fewer elements ---
nums = [1, 2, 3, 4, 5]
nums[1:4] = [99]
print("\nReplace 3 elements with 1:", nums)   # [1, 99, 5]

# --- Example 11: Replace with more elements ---
nums = [1, 2, 3]
nums[1:2] = [20, 21, 22]
print("Replace 1 element with 3:", nums)   # [1, 20, 21, 22, 3]

# --- Example 12: Delete elements with empty slice ---
nums = [1, 2, 3, 4, 5]
nums[1:3] = []   # remove index 1 and 2
print("After deleting [1:3]:", nums)   # [1, 4, 5]

# =============================
# 5. MUTATION AWARENESS
# =============================

# --- Example 13: Variables point to the same list ---
a = [1, 2, 3]
b = a           # b points to the SAME list
b[0] = 999
print("\na:", a)   # [999, 2, 3] ← a also changed!
print("b:", b)     # [999, 2, 3]

# --- Example 14: Use [:] to make a separate copy ---
a = [1, 2, 3]
b = a[:]        # b is a NEW list (copy)
b[0] = 999
print("\na:", a)   # [1, 2, 3] ← unchanged!
print("b:", b)     # [999, 2, 3]

# --- Example 15: Checking if same object ---
a = [1, 2, 3]
b = a
c = a[:]
print(f"\na is b: {a is b}")   # True — same object
print(f"a is c: {a is c}")     # False — different object
print(f"a == c: {a == c}")     # True — same values

# ============================================
# TRY IT YOURSELF:
# 1. Create a list [1, 2, 3] and change the second element to 99
# 2. Create a list of 5 words and uppercase all of them using a loop
# 3. Observe what happens when you assign b = a and modify b
# ============================================
