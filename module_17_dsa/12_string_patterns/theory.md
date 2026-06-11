# Strings in DSA

## String Problems Are Everywhere

Strings are one of the most common data types in interviews and real-world code. Key patterns:

## 1. Pattern Matching

Finding whether a substring exists in a string:

```python
# Simple: use Python's `in` operator
"hello" in "hello world"    # True

# DSA approach: implement it manually
def find_pattern(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            return i
    return -1
```

## 2. Palindrome Problems

A **palindrome** reads the same forwards and backwards:

```python
def is_palindrome(s):
    return s == s[::-1]

# Or using two pointers (more DSA-oriented):
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

## 3. Frequency-Based Problems

Counting character occurrences to solve problems:

```python
# Are two strings anagrams?
def is_anagram(s1, s2):
    freq = {}
    for c in s1:
        freq[c] = freq.get(c, 0) + 1
    for c in s2:
        freq[c] = freq.get(c, 0) - 1
    return all(v == 0 for v in freq.values())
```

## Key Points

- Strings are immutable in Python — operations create new strings
- Use dictionaries/sets for frequency and lookup problems
- Two-pointer technique works well for palindromes
- Many string problems can be solved with hash maps
