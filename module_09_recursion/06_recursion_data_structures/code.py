# ============================================
# MODULE 9 - SUBTOPIC 6: Recursion with Data Structures
# ============================================

# =============================
# 1. STRINGS — REVERSE
# =============================

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print("String reversal:")
print(f"  'hello' → '{reverse_string('hello')}'")
print(f"  'Python' → '{reverse_string('Python')}'")
print(f"  'a' → '{reverse_string('a')}'")

# =============================
# 2. STRINGS — PALINDROME
# =============================

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(f"\nPalindrome check:")
for word in ["racecar", "hello", "madam", "A man a plan a canal Panama"]:
    print(f"  '{word}': {is_palindrome(word)}")

# =============================
# 3. STRINGS — COUNT CHARACTER
# =============================

def count_char(s, ch):
    if len(s) == 0:
        return 0
    match = 1 if s[0] == ch else 0
    return match + count_char(s[1:], ch)

print(f"\nCount characters:")
print(f"  'mississippi' has {count_char('mississippi', 's')} s's")
print(f"  'hello world' has {count_char('hello world', 'l')} l's")

# =============================
# 4. STRINGS — REMOVE CHARACTER
# =============================

def remove_char(s, ch):
    if len(s) == 0:
        return ""
    if s[0] == ch:
        return remove_char(s[1:], ch)
    return s[0] + remove_char(s[1:], ch)

print(f"\nRemove character:")
print(f"  remove 'l' from 'hello': '{remove_char('hello', 'l')}'")
print(f"  remove 'a' from 'banana': '{remove_char('banana', 'a')}'")

# =============================
# 5. LISTS — SUM
# =============================

def list_sum(items):
    if len(items) == 0:
        return 0
    return items[0] + list_sum(items[1:])

print(f"\nList sum:")
print(f"  sum([1,2,3,4,5]) = {list_sum([1, 2, 3, 4, 5])}")
print(f"  sum([10,20,30]) = {list_sum([10, 20, 30])}")

# =============================
# 6. LISTS — MAX ELEMENT
# =============================

def list_max(items):
    if len(items) == 1:
        return items[0]
    rest_max = list_max(items[1:])
    return items[0] if items[0] > rest_max else rest_max

print(f"\nList max:")
print(f"  max([3,7,2,9,4]) = {list_max([3, 7, 2, 9, 4])}")
print(f"  max([1]) = {list_max([1])}")

# =============================
# 7. LISTS — FLATTEN NESTED LIST
# =============================

def flatten(items):
    if len(items) == 0:
        return []
    first = items[0]
    rest = flatten(items[1:])
    if isinstance(first, list):
        return flatten(first) + rest
    return [first] + rest

print(f"\nFlatten nested list:")
nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"  {nested} → {flatten(nested)}")

deeper = [[1, [2]], [3, [4, [5]]]]
print(f"  {deeper} → {flatten(deeper)}")

# =============================
# 8. LISTS — FILTER RECURSIVELY
# =============================

def filter_positive(items):
    if len(items) == 0:
        return []
    rest = filter_positive(items[1:])
    if items[0] > 0:
        return [items[0]] + rest
    return rest

print(f"\nFilter positive:")
data = [-3, 5, -1, 8, 0, -2, 7]
print(f"  {data} → {filter_positive(data)}")

# =============================
# 9. LISTS — RECURSIVE MAP
# =============================

def recursive_map(items, func):
    if len(items) == 0:
        return []
    return [func(items[0])] + recursive_map(items[1:], func)

print(f"\nRecursive map:")
nums = [1, 2, 3, 4, 5]
print(f"  square: {recursive_map(nums, lambda x: x**2)}")
print(f"  double: {recursive_map(nums, lambda x: x*2)}")

# ============================================
# TRY IT YOURSELF:
# 1. Write a recursive function to count words in a string
# 2. Write a recursive function to find min in a list
# 3. Write a recursive function to check if a list is sorted
# ============================================
