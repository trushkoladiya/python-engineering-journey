# ============================================
# MODULE 17 - SUBTOPIC 12: Strings in DSA
# ============================================

# String problems: pattern matching, palindromes,
# frequency analysis, and character manipulation.

# =============================
# 1. PATTERN MATCHING (BRUTE FORCE)
# =============================

print("=== Pattern Matching — Brute Force ===")
print()

def find_pattern(text, pattern):
    """Find first occurrence of pattern in text."""
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1

text = "hello world, hello python"
print(f"  Text: '{text}'")
print(f"  Find 'world': index {find_pattern(text, 'world')}")
print(f"  Find 'python': index {find_pattern(text, 'python')}")
print(f"  Find 'java': index {find_pattern(text, 'java')}")
print()

# Find ALL occurrences
def find_all_patterns(text, pattern):
    """Find all occurrences of pattern in text."""
    positions = []
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            positions.append(i)
    return positions

positions = find_all_patterns(text, "hello")
print(f"  All 'hello' positions: {positions}")
print()

# =============================
# 2. PALINDROME CHECKING
# =============================

print("=== Palindrome Problems ===")
print()

def is_palindrome(s):
    """Check if string is a palindrome (two-pointer)."""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Simple palindromes
words = ["racecar", "hello", "madam", "level", "world", "noon"]
for word in words:
    result = "✓" if is_palindrome(word) else "✗"
    print(f"  {result} '{word}'")
print()

# Palindrome with cleaning (ignore case and non-alphanumeric)
def is_palindrome_clean(s):
    """Check palindrome ignoring case and non-alphanumeric chars."""
    clean = ""
    for char in s.lower():
        if char.isalnum():
            clean += char
    return is_palindrome(clean)

phrases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "Was it a car or a cat I saw?",
]
for phrase in phrases:
    result = "✓" if is_palindrome_clean(phrase) else "✗"
    print(f"  {result} '{phrase}'")
print()

# =============================
# 3. LONGEST PALINDROMIC SUBSTRING
# =============================

print("=== Longest Palindromic Substring ===")
print()

def longest_palindrome(s):
    """Find the longest palindromic substring."""
    if not s:
        return ""

    start = 0
    max_length = 1

    def expand_from_center(left, right):
        """Expand outward while characters match."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1

    for i in range(len(s)):
        # Odd length palindromes
        left1, len1 = expand_from_center(i, i)
        # Even length palindromes
        left2, len2 = expand_from_center(i, i + 1)

        if len1 > max_length:
            start = left1
            max_length = len1
        if len2 > max_length:
            start = left2
            max_length = len2

    return s[start:start + max_length]

test_strings = ["babad", "cbbd", "racecarxyz", "abacaba"]
for s in test_strings:
    result = longest_palindrome(s)
    print(f"  '{s}' → longest palindrome: '{result}'")
print()

# =============================
# 4. ANAGRAM CHECKING
# =============================

print("=== Anagram Detection ===")
print()

def is_anagram(s1, s2):
    """Check if two strings are anagrams using frequency count."""
    if len(s1) != len(s2):
        return False

    freq = {}
    for char in s1:
        freq[char] = freq.get(char, 0) + 1
    for char in s2:
        freq[char] = freq.get(char, 0) - 1

    return all(count == 0 for count in freq.values())

pairs = [
    ("listen", "silent"),
    ("hello", "world"),
    ("anagram", "nagaram"),
    ("rat", "car"),
]

for s1, s2 in pairs:
    result = "✓ anagram" if is_anagram(s1, s2) else "✗ not anagram"
    print(f"  '{s1}' & '{s2}': {result}")
print()

# Group anagrams
def group_anagrams(words):
    """Group words that are anagrams of each other."""
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = group_anagrams(words)
print(f"  Words: {words}")
print(f"  Anagram groups: {groups}")
print()

# =============================
# 5. CHARACTER FREQUENCY
# =============================

print("=== Character Frequency Problems ===")
print()

def first_unique_char(s):
    """Find first non-repeating character."""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for i, char in enumerate(s):
        if freq[char] == 1:
            return i, char
    return -1, None

test_strings = ["leetcode", "loveleetcode", "aabb"]
for s in test_strings:
    idx, char = first_unique_char(s)
    if idx != -1:
        print(f"  '{s}' → first unique: '{char}' at index {idx}")
    else:
        print(f"  '{s}' → no unique character")
print()

# Most frequent character
def most_frequent(s):
    """Find the most frequent character."""
    freq = {}
    for char in s:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    if not freq:
        return None, 0
    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]

text = "engineering excellence"
char, count = most_frequent(text)
print(f"  '{text}'")
print(f"  Most frequent: '{char}' ({count} times)")
print()

# =============================
# 6. STRING COMPRESSION
# =============================

print("=== String Compression ===")
print()

def compress(s):
    """Compress string: 'aabcccccaaa' → 'a2b1c5a3'."""
    if not s:
        return ""

    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i - 1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")

    compressed = "".join(result)
    # Only return compressed if it's shorter
    return compressed if len(compressed) < len(s) else s

test_strings = ["aabcccccaaa", "abc", "aabbcc", "aaaaaaa"]
for s in test_strings:
    print(f"  '{s}' → '{compress(s)}'")
print()

# =============================
# 7. STRING REVERSAL VARIANTS
# =============================

print("=== String Reversal Variants ===")
print()

# Reverse words in a sentence
def reverse_words(sentence):
    """Reverse the order of words."""
    words = sentence.split()
    return " ".join(reversed(words))

text = "hello beautiful world"
print(f"  '{text}' → '{reverse_words(text)}'")

# Reverse each word individually
def reverse_each_word(sentence):
    words = sentence.split()
    return " ".join(word[::-1] for word in words)

print(f"  Reverse each word: '{reverse_each_word(text)}'")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Check if one string is a rotation of another
#    (hint: concatenate s with itself and search)
# 2. Find the longest common prefix of a list of strings
# 3. Check if a string has all unique characters
#    (without using a set)
# ============================================
