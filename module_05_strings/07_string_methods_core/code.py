# ============================================
# MODULE 5 - SUBTOPIC 7: String Methods (Core)
# ============================================

# =============================
# 1. CASE METHODS
# =============================

# --- Example 1: lower() — all lowercase ---
text = "Hello World"
print("lower():", text.lower())   # hello world

# --- Example 2: upper() — all uppercase ---
text = "Hello World"
print("upper():", text.upper())   # HELLO WORLD

# --- Example 3: title() — capitalize each word ---
text = "hello world python"
print("title():", text.title())   # Hello World Python

# --- Example 4: capitalize() — capitalize first letter only ---
text = "hello world python"
print("capitalize():", text.capitalize())   # Hello world python

# --- Example 5: Case methods return NEW strings ---
original = "Python"
lower_version = original.lower()
print()
print("Original:", original)        # Python (unchanged!)
print("Lowercase:", lower_version)  # python (new string)

# --- Example 6: Case-insensitive comparison ---
user_input = "YES"
if user_input.lower() == "yes":
    print("User said yes!")

# =============================
# 2. TRIMMING METHODS
# =============================

# --- Example 7: strip() — remove whitespace from both sides ---
text = "   Hello World   "
print()
print("Before strip: '" + text + "'")
print("After strip:  '" + text.strip() + "'")

# --- Example 8: lstrip() — remove from left only ---
text = "   Hello   "
print()
print("lstrip(): '" + text.lstrip() + "'")   # "Hello   "

# --- Example 9: rstrip() — remove from right only ---
text = "   Hello   "
print("rstrip(): '" + text.rstrip() + "'")   # "   Hello"

# --- Example 10: Stripping newlines and tabs ---
messy = "\n\t  Hello World  \n\t"
print()
print("Messy: repr →", repr(messy))
print("Clean:", messy.strip())

# --- Example 11: Stripping specific characters ---
text = "***Hello***"
print()
print("Strip stars:", text.strip("*"))    # Hello
print("Lstrip stars:", text.lstrip("*"))  # Hello***
print("Rstrip stars:", text.rstrip("*"))  # ***Hello

# =============================
# 3. SEARCHING METHODS
# =============================

# --- Example 12: find() — returns index of first occurrence ---
text = "Hello World"
print()
print("find('World'):", text.find("World"))     # 6
print("find('o'):", text.find("o"))             # 4
print("find('Python'):", text.find("Python"))   # -1 (not found)

# --- Example 13: rfind() — returns index of LAST occurrence ---
text = "banana"
print()
print("find('a'):", text.find("a"))     # 1 (first 'a')
print("rfind('a'):", text.rfind("a"))   # 5 (last 'a')

# --- Example 14: find() with start position ---
text = "Hello World Hello"
print()
print("find('Hello'):", text.find("Hello"))        # 0
print("find('Hello', 1):", text.find("Hello", 1))  # 12 (skip first)

# --- Example 15: index() — like find() but raises error ---
text = "Hello World"
print()
print("index('World'):", text.index("World"))   # 6
# Uncomment to see the error:
# print(text.index("Python"))   # ValueError!

# --- Example 16: Safe searching pattern ---
text = "Python programming"
search = "gram"
pos = text.find(search)
if pos != -1:
    print("'" + search + "' found at index", pos)
else:
    print("'" + search + "' not found")

# =============================
# 4. COUNTING METHOD
# =============================

# --- Example 17: count() — how many times substring appears ---
text = "banana"
print()
print("count('a'):", text.count("a"))    # 3
print("count('na'):", text.count("na"))  # 2
print("count('x'):", text.count("x"))    # 0

# --- Example 18: Counting in a sentence ---
sentence = "the cat sat on the mat"
print()
print("'the' appears:", sentence.count("the"), "times")   # 2
print("'at' appears:", sentence.count("at"), "times")     # 3

# --- Example 19: Count with range ---
text = "abababab"
print()
print("count('ab'):", text.count("ab"))          # 4
print("count('ab', 2):", text.count("ab", 2))    # 3 (from index 2)
print("count('ab', 2, 6):", text.count("ab", 2, 6))  # 2 (index 2 to 5)

# =============================
# 5. COMBINING METHODS
# =============================

# --- Example 20: Clean and compare user input ---
raw_input = "  Python  "
cleaned = raw_input.strip().lower()
print()
print("Raw: '" + raw_input + "'")
print("Cleaned: '" + cleaned + "'")
print("Is python?", cleaned == "python")   # True

# --- Example 21: Find all positions of a character using find() ---
text = "mississippi"
char = "s"
print()
print("All positions of '" + char + "' in", text, ":")
pos = text.find(char)
while pos != -1:
    print("  Index", pos)
    pos = text.find(char, pos + 1)

# ============================================
# TRY IT YOURSELF:
# 1. Take "  HELLO world  " and make it "hello world" (strip + lower)
# 2. Count how many times "is" appears in "this is what it is"
# 3. Find the position of "Python" in "I love Python programming"
# ============================================
