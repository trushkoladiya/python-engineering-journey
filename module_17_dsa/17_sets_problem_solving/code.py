# ============================================
# MODULE 17 - SUBTOPIC 17: Sets in Problem Solving
# ============================================

# Sets: O(1) membership testing, uniqueness,
# and powerful set operations for DSA problems.

import time

# =============================
# 1. REMOVING DUPLICATES
# =============================

print("=== Removing Duplicates ===")
print()

# Simple dedup
data = [4, 2, 7, 2, 9, 4, 1, 7, 3, 1]
unique = list(set(data))
print(f"  Data:   {data}")
print(f"  Unique: {unique}")
print()

# Preserve order while removing duplicates
def unique_ordered(items):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

ordered_unique = unique_ordered(data)
print(f"  Unique (ordered): {ordered_unique}")
print()

# =============================
# 2. FAST MEMBERSHIP TESTING
# =============================

print("=== Fast Membership Testing ===")
print()

# Valid usernames
valid_users = {"trush", "rahul", "charlie", "diana", "eve"}

login_attempts = ["trush", "frank", "rahul", "hacker", "charlie"]
for user in login_attempts:
    status = "✓ allowed" if user in valid_users else "✗ denied"
    print(f"  {user:10} → {status}")
print()

# Speed comparison
size = 500_000
data_list = list(range(size))
data_set = set(range(size))
target = size - 1

start = time.time()
_ = target in data_list
t_list = time.time() - start

start = time.time()
_ = target in data_set
t_set = time.time() - start

print(f"  Checking membership in {size:,} items:")
print(f"    List: {t_list:.6f}s")
print(f"    Set:  {t_set:.8f}s")
print()

# =============================
# 3. SET OPERATIONS FOR PROBLEMS
# =============================

print("=== Set Operations ===")
print()

skills_trush = {"Python", "JavaScript", "SQL", "Docker"}
skills_rahul = {"Python", "Java", "SQL", "Kubernetes"}

print(f"  Trush: {skills_trush}")
print(f"  Rahul:   {skills_rahul}")
print()

# Common skills (intersection)
common = skills_trush & skills_rahul
print(f"  Common skills: {common}")

# Trush only (difference)
trush_only = skills_trush - skills_rahul
print(f"  Only Trush: {trush_only}")

# Rahul only
rahul_only = skills_rahul - skills_trush
print(f"  Only Rahul: {rahul_only}")

# All skills combined (union)
all_skills = skills_trush | skills_rahul
print(f"  All skills: {all_skills}")

# Skills unique to each (symmetric difference)
unique_each = skills_trush ^ skills_rahul
print(f"  Unique to each: {unique_each}")
print()

# =============================
# 4. FIND MISSING NUMBER
# =============================

print("=== Find Missing Number ===")
print()

def find_missing(nums, n):
    """Find missing number in range [0, n]."""
    full_set = set(range(n + 1))
    nums_set = set(nums)
    missing = full_set - nums_set
    return missing

# Numbers 0-9, some missing
data = [0, 1, 2, 4, 5, 7, 8, 9]
missing = find_missing(data, 9)
print(f"  Data (should be 0-9): {data}")
print(f"  Missing: {missing}")
print()

# =============================
# 5. LONGEST CONSECUTIVE SEQUENCE
# =============================

print("=== Longest Consecutive Sequence ===")
print()

def longest_consecutive(nums):
    """Find length of longest consecutive sequence. O(n)."""
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting from the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length

data = [100, 4, 200, 1, 3, 2]
result = longest_consecutive(data)
print(f"  Data: {data}")
print(f"  Longest consecutive: {result} (sequence: 1,2,3,4)")
print()

data = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
result = longest_consecutive(data)
print(f"  Data: {data}")
print(f"  Longest consecutive: {result}")
print()

# =============================
# 6. INTERSECTION OF MULTIPLE LISTS
# =============================

print("=== Intersection of Multiple Lists ===")
print()

def intersection_all(*lists):
    """Find elements common to ALL lists."""
    if not lists:
        return set()
    result = set(lists[0])
    for lst in lists[1:]:
        result &= set(lst)
    return result

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [4, 5, 6, 7, 8]

common = intersection_all(list1, list2, list3)
print(f"  List 1: {list1}")
print(f"  List 2: {list2}")
print(f"  List 3: {list3}")
print(f"  Common: {common}")
print()

# =============================
# 7. VOWEL COUNTING WITH SETS
# =============================

print("=== Vowel Counting ===")
print()

vowels = set("aeiouAEIOU")

def analyze_text(text):
    """Analyze text using set operations."""
    chars = set(text.lower()) - {" "}
    text_vowels = chars & set("aeiou")
    text_consonants = chars - set("aeiou") - set("0123456789")
    vowel_count = sum(1 for c in text if c.lower() in set("aeiou"))

    return {
        "unique_chars": len(chars),
        "vowels_used": text_vowels,
        "consonants_used": text_consonants,
        "vowel_count": vowel_count,
    }

text = "Hello World Python Programming"
analysis = analyze_text(text)
print(f"  Text: '{text}'")
print(f"  Unique characters: {analysis['unique_chars']}")
print(f"  Vowels used: {analysis['vowels_used']}")
print(f"  Consonants used: {analysis['consonants_used']}")
print(f"  Total vowel count: {analysis['vowel_count']}")
print()

# =============================
# 8. HAPPY NUMBER
# =============================

print("=== Happy Number ===")
print()

def is_happy(n):
    """
    A happy number: sum of squares of digits eventually reaches 1.
    Use a set to detect cycles.
    """
    seen = set()
    while n != 1:
        if n in seen:
            return False    # cycle detected!
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return True

for num in range(1, 21):
    if is_happy(num):
        print(f"  {num} is a happy number ☺")

print()

# ============================================
# TRY IT YOURSELF:
# 1. Given two lists, find elements that appear
#    in one but not the other
# 2. Check if one list is a subset of another
# 3. Find the first repeating element in a list
#    using a set
# ============================================
