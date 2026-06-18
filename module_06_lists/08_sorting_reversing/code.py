# ============================================
# MODULE 6 - SUBTOPIC 8: Sorting & Reversing
# ============================================

# =============================
# 1. SORT() — Sort in place
# =============================

# --- Example 1: Sort numbers ascending ---
nums = [5, 2, 8, 1, 9, 3]
print("Before sort:", nums)
nums.sort()
print("After sort:", nums)   # [1, 2, 3, 5, 8, 9]

# --- Example 2: Sort descending ---
nums = [5, 2, 8, 1, 9, 3]
nums.sort(reverse=True)
print("\nDescending:", nums)   # [9, 8, 5, 3, 2, 1]

# --- Example 3: Sort strings alphabetically ---
fruits = ["cherry", "apple", "banana", "date"]
fruits.sort()
print("\nSorted fruits:", fruits)   # ['apple', 'banana', 'cherry', 'date']

# --- Example 4: sort() returns None ---
nums = [3, 1, 2]
result = nums.sort()
print("\nReturn value:", result)   # None — sort() modifies in place!
print("List is sorted:", nums)    # [1, 2, 3]

# =============================
# 2. SORTED() — Return new list
# =============================

# --- Example 5: sorted() keeps original unchanged ---
original = [5, 2, 8, 1, 9]
new_sorted = sorted(original)
print("\nOriginal:", original)     # [5, 2, 8, 1, 9] — unchanged!
print("Sorted copy:", new_sorted)  # [1, 2, 5, 8, 9]

# --- Example 6: sorted() descending ---
nums = [3, 1, 4, 1, 5]
desc = sorted(nums, reverse=True)
print("\nDescending:", desc)   # [5, 4, 3, 1, 1]

# --- Example 7: sorted() works on any iterable ---
text = "python"
sorted_chars = sorted(text)
print("\nSorted chars:", sorted_chars)   # ['h', 'n', 'o', 'p', 't', 'y']

# =============================
# 3. REVERSE() — Reverse in place
# =============================

# --- Example 8: Basic reverse ---
nums = [1, 2, 3, 4, 5]
print("\nBefore reverse:", nums)
nums.reverse()
print("After reverse:", nums)   # [5, 4, 3, 2, 1]

# --- Example 9: Reverse vs sort(reverse=True) ---
nums = [3, 1, 4, 1, 5]
# reverse() just flips the order:
reversed_list = nums[:]
reversed_list.reverse()
print("\nReversed:", reversed_list)   # [5, 1, 4, 1, 3]

# sort(reverse=True) sorts descending:
sorted_list = nums[:]
sorted_list.sort(reverse=True)
print("Sort desc:", sorted_list)     # [5, 4, 3, 1, 1]
print("Not the same!")

# --- Example 10: Reverse using slicing (creates new list) ---
nums = [1, 2, 3, 4, 5]
reversed_copy = nums[::-1]
print(f"\nOriginal: {nums}")
print(f"Reversed copy: {reversed_copy}")
print(f"Original unchanged: {nums}")

# =============================
# 4. CUSTOM SORTING WITH key
# =============================

# --- Example 11: Sort by string length ---
words = ["banana", "apple", "cherry", "kiwi", "fig"]
words.sort(key=len)
print("\nSorted by length:", words)
# ['fig', 'kiwi', 'apple', 'banana', 'cherry']

# --- Example 12: Sort case-insensitive ---
names = ["trush", "Priya", "Rahul", "dev"]
sorted_names = sorted(names, key=str.lower)
print("Case-insensitive:", sorted_names)
# ['dev', 'Priya', 'Rahul', 'trush']

# --- Example 13: Sort by last character ---
words = ["hello", "world", "alpha", "bravo"]
sorted_words = sorted(words, key=lambda w: w[-1])
print("\nSorted by last char:", sorted_words)

# =============================
# 5. SORTING PRACTICAL PATTERNS
# =============================

# --- Example 14: Sort and find median ---
scores = [85, 92, 78, 96, 88, 70, 91]
sorted_scores = sorted(scores)
mid = len(sorted_scores) // 2
median = sorted_scores[mid]
print(f"\nScores: {scores}")
print(f"Sorted: {sorted_scores}")
print(f"Median: {median}")

# --- Example 15: Get top 3 ---
scores = [78, 92, 85, 97, 88, 65, 91, 73]
top3 = sorted(scores, reverse=True)[:3]
print(f"\nAll scores: {scores}")
print(f"Top 3: {top3}")

# --- Example 16: Sort and check if sorted ---
nums = [1, 3, 2, 5, 4]
sorted_nums = sorted(nums)
is_sorted = nums == sorted_nums
print(f"\n{nums} is sorted? {is_sorted}")

already = [1, 2, 3, 4, 5]
print(f"{already} is sorted? {already == sorted(already)}")

# --- Example 17: Rank items ---
scores = [85, 92, 78, 96, 88]
print("\n--- Rankings ---")
sorted_desc = sorted(scores, reverse=True)
for i in range(len(sorted_desc)):
    print(f"  Rank {i + 1}: {sorted_desc[i]}")

# ============================================
# TRY IT YOURSELF:
# 1. Sort [9, 3, 7, 1, 5] in ascending and descending order
# 2. Sort ["banana", "apple", "fig"] by word length
# 3. Find the top 3 smallest numbers in [45, 12, 89, 23, 67, 5, 34]
# ============================================
