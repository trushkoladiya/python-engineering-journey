# ============================================
# MODULE 6 - SUBTOPIC 7: Searching & Counting
# ============================================

# =============================
# 1. INDEX() — Find position
# =============================

# --- Example 1: Basic index ---
fruits = ["apple", "banana", "cherry", "date"]
print("Index of 'cherry':", fruits.index("cherry"))   # 2
print("Index of 'apple':", fruits.index("apple"))     # 0

# --- Example 2: First occurrence only ---
nums = [10, 20, 30, 20, 40, 20]
print("\nIndex of 20:", nums.index(20))   # 1 (first occurrence)

# --- Example 3: index() with start position ---
nums = [10, 20, 30, 20, 40, 20]
first_pos = nums.index(20)
second_pos = nums.index(20, first_pos + 1)
print(f"\nFirst 20 at index: {first_pos}")    # 1
print(f"Second 20 at index: {second_pos}")   # 3

# --- Example 4: Find all positions ---
nums = [1, 2, 3, 2, 4, 2, 5]
target = 2
print(f"\nAll positions of {target}:")
positions = []
for i in range(len(nums)):
    if nums[i] == target:
        positions.append(i)
print(f"  Positions: {positions}")   # [1, 3, 5]

# =============================
# 2. COUNT() — Count occurrences
# =============================

# --- Example 5: Basic count ---
nums = [1, 2, 3, 2, 4, 2, 5]
print(f"\nCount of 2: {nums.count(2)}")   # 3
print(f"Count of 4: {nums.count(4)}")     # 1
print(f"Count of 9: {nums.count(9)}")     # 0

# --- Example 6: Count strings ---
words = ["hello", "world", "hello", "python", "hello"]
print(f"\nCount of 'hello': {words.count('hello')}")   # 3

# --- Example 7: Count all unique elements ---
data = ["a", "b", "a", "c", "b", "a", "d"]
print(f"\nData: {data}")
counted = []
for item in data:
    if item not in counted:
        print(f"  '{item}' appears {data.count(item)} times")
        counted.append(item)

# =============================
# 3. SAFE SEARCHING
# =============================

# --- Example 8: Check before using index ---
fruits = ["apple", "banana", "cherry"]
target = "grape"

print()
if target in fruits:
    pos = fruits.index(target)
    print(f"'{target}' found at index {pos}")
else:
    print(f"'{target}' not found in the list")

# --- Example 9: Safe search for multiple items ---
inventory = ["pen", "notebook", "eraser", "pencil"]
search_items = ["pen", "marker", "eraser", "stapler"]

print("\n--- Search Results ---")
for item in search_items:
    if item in inventory:
        print(f"  ✓ '{item}' found at index {inventory.index(item)}")
    else:
        print(f"  ✗ '{item}' not in inventory")

# =============================
# 4. FINDING MIN AND MAX POSITION
# =============================

# --- Example 10: Find position of maximum ---
scores = [78, 92, 85, 97, 88]
max_score = max(scores)
max_pos = scores.index(max_score)
print(f"\nScores: {scores}")
print(f"Max score: {max_score} at index {max_pos}")

# --- Example 11: Find position of minimum ---
temps = [72, 68, 75, 65, 70]
min_temp = min(temps)
min_pos = temps.index(min_temp)
print(f"\nTemps: {temps}")
print(f"Min temp: {min_temp} at index {min_pos}")

# =============================
# 5. PRACTICAL PATTERNS
# =============================

# --- Example 12: Find elements that appear more than once ---
data = [1, 2, 3, 2, 4, 3, 5, 1]
duplicates = []
for item in data:
    if data.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
print(f"\nData: {data}")
print(f"Duplicates: {duplicates}")   # [1, 2, 3]

# --- Example 13: Find most common element ---
votes = ["A", "B", "A", "C", "B", "A", "B", "A"]
candidates = []
for v in votes:
    if v not in candidates:
        candidates.append(v)

most_votes = 0
winner = ""
for c in candidates:
    count = votes.count(c)
    print(f"  {c}: {count} votes")
    if count > most_votes:
        most_votes = count
        winner = c

print(f"\nWinner: {winner} with {most_votes} votes")

# --- Example 14: Check if list contains only unique elements ---
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 2, 5]

print()
for test_list in [list1, list2]:
    all_unique = True
    for item in test_list:
        if test_list.count(item) > 1:
            all_unique = False
            break
    if all_unique:
        print(f"{test_list} → all unique")
    else:
        print(f"{test_list} → has duplicates")

# ============================================
# TRY IT YOURSELF:
# 1. Find the index of "Python" in ["Java", "Python", "Go", "Rust"]
# 2. Count how many times 5 appears in [5, 3, 5, 7, 5, 2, 5]
# 3. Find all elements that appear exactly twice in a list
# ============================================
