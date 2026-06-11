# ============================================
# MODULE 6 - SUBTOPIC 15: Common List Patterns
# ============================================

# =============================
# 1. FINDING MAX / MIN
# =============================

# --- Example 1: Using built-in max/min ---
scores = [78, 92, 85, 97, 63, 88]
print(f"Scores: {scores}")
print(f"Max: {max(scores)}")   # 97
print(f"Min: {min(scores)}")   # 63
print(f"Sum: {sum(scores)}")   # 503
print(f"Avg: {sum(scores) / len(scores):.1f}")

# --- Example 2: Find max manually (with position) ---
nums = [45, 12, 89, 23, 67, 89]
max_val = nums[0]
max_idx = 0
for i in range(1, len(nums)):
    if nums[i] > max_val:
        max_val = nums[i]
        max_idx = i
print(f"\nMax {max_val} at index {max_idx}")

# --- Example 3: Find second largest ---
nums = [45, 12, 89, 23, 67, 34]
sorted_nums = sorted(nums, reverse=True)
second = sorted_nums[1]
print(f"\nNums: {nums}")
print(f"Second largest: {second}")   # 67

# =============================
# 2. REMOVING DUPLICATES
# =============================

# --- Example 4: Remove duplicates (preserve order) ---
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique = []
for item in data:
    if item not in unique:
        unique.append(item)
print(f"\nOriginal: {data}")
print(f"Unique: {unique}")

# --- Example 5: Using comprehension-like pattern ---
data = ["apple", "banana", "apple", "cherry", "banana"]
seen = []
unique = []
for item in data:
    if item not in seen:
        seen.append(item)
        unique.append(item)
print(f"\nOriginal: {data}")
print(f"Unique: {unique}")

# =============================
# 3. FREQUENCY COUNTING
# =============================

# --- Example 6: Count each element ---
votes = ["A", "B", "A", "C", "B", "A", "B", "C", "A"]
counted = []
print(f"\nVotes: {votes}")
print("Frequency:")
for item in votes:
    if item not in counted:
        print(f"  {item}: {votes.count(item)}")
        counted.append(item)

# --- Example 7: Find most frequent ---
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
most_freq = data[0]
max_count = 0
counted = []
for item in data:
    if item not in counted:
        c = data.count(item)
        if c > max_count:
            max_count = c
            most_freq = item
        counted.append(item)
print(f"\nData: {data}")
print(f"Most frequent: {most_freq} ({max_count} times)")

# --- Example 8: Group elements by frequency ---
data = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1]
once = []
multiple = []
counted = []
for item in data:
    if item not in counted:
        c = data.count(item)
        if c == 1:
            once.append(item)
        else:
            multiple.append(item)
        counted.append(item)
print(f"\nAppear once: {once}")
print(f"Appear multiple: {multiple}")

# =============================
# 4. TWO-POINTER TECHNIQUE
# =============================

# --- Example 9: Pair elements from both ends ---
nums = [1, 2, 3, 4, 5, 6]
left = 0
right = len(nums) - 1
print(f"\nPairs from ends of {nums}:")
while left < right:
    print(f"  ({nums[left]}, {nums[right]}) → sum = {nums[left] + nums[right]}")
    left += 1
    right -= 1

# --- Example 10: Check if list is a palindrome ---
items = [1, 2, 3, 2, 1]
left = 0
right = len(items) - 1
is_palindrome = True
while left < right:
    if items[left] != items[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print(f"\n{items} is palindrome? {is_palindrome}")   # True

items2 = [1, 2, 3, 4, 5]
left = 0
right = len(items2) - 1
is_palindrome = True
while left < right:
    if items2[left] != items2[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print(f"{items2} is palindrome? {is_palindrome}")   # False

# --- Example 11: Reverse list in place with two pointers ---
nums = [1, 2, 3, 4, 5]
print(f"\nBefore reverse: {nums}")
left = 0
right = len(nums) - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
print(f"After reverse: {nums}")

# =============================
# 5. SLIDING WINDOW (Intro)
# =============================

# --- Example 12: Max sum of 3 consecutive elements ---
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
window_size = 3

max_sum = 0
# Calculate first window
for i in range(window_size):
    max_sum += nums[i]

current_sum = max_sum
for i in range(window_size, len(nums)):
    current_sum = current_sum + nums[i] - nums[i - window_size]
    if current_sum > max_sum:
        max_sum = current_sum

print(f"\nNums: {nums}")
print(f"Max sum of {window_size} consecutive: {max_sum}")   # 33

# --- Example 13: Moving average ---
data = [10, 20, 30, 40, 50, 60, 70]
window = 3
print(f"\nMoving average (window={window}) of {data}:")
for i in range(len(data) - window + 1):
    window_slice = data[i:i + window]
    avg = sum(window_slice) / window
    print(f"  {window_slice} → avg = {avg:.1f}")

# =============================
# 6. FLATTENING NESTED LISTS
# =============================

# --- Example 14: Flatten with comprehension ---
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [item for row in nested for item in row]
print(f"\nNested: {nested}")
print(f"Flat: {flat}")

# --- Example 15: Flatten with loop ---
nested = [["a", "b"], ["c", "d", "e"], ["f"]]
flat = []
for row in nested:
    for item in row:
        flat.append(item)
print(f"\nNested: {nested}")
print(f"Flat: {flat}")

# =============================
# 7. LIST ROTATION
# =============================

# --- Example 16: Rotate left by k positions ---
nums = [1, 2, 3, 4, 5]
k = 2
rotated = nums[k:] + nums[:k]
print(f"\nRotate {nums} left by {k}: {rotated}")   # [3, 4, 5, 1, 2]

# --- Example 17: Rotate right by k positions ---
nums = [1, 2, 3, 4, 5]
k = 2
rotated = nums[-k:] + nums[:-k]
print(f"Rotate {nums} right by {k}: {rotated}")   # [4, 5, 1, 2, 3]

# =============================
# 8. MERGE AND INTERLEAVE
# =============================

# --- Example 18: Merge two sorted lists ---
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
merged = sorted(a + b)
print(f"\nMerge {a} + {b}: {merged}")

# --- Example 19: Interleave two lists ---
a = ["a", "b", "c"]
b = [1, 2, 3]
interleaved = []
for i in range(len(a)):
    interleaved.append(a[i])
    interleaved.append(b[i])
print(f"Interleaved: {interleaved}")   # ['a', 1, 'b', 2, 'c', 3]

# --- Example 20: Partition into even/odd ---
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in nums if n % 2 == 0]
odds = [n for n in nums if n % 2 != 0]
print(f"\nNums: {nums}")
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# ============================================
# TRY IT YOURSELF:
# 1. Find the two largest numbers in a list without sorting
# 2. Check if a list is a palindrome using two pointers
# 3. Flatten [[1,[2,3]],[4,[5,6]]] — hint: you'll need nested loops
# 4. Rotate [10, 20, 30, 40, 50] right by 3 positions
# ============================================
