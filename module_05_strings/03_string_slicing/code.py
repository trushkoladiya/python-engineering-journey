# ============================================
# MODULE 5 - SUBTOPIC 3: String Slicing
# ============================================

# =============================
# 1. BASIC SLICING (start:end)
# =============================

# --- Example 1: Extract a portion ---
word = "Python"
print("word[0:3] →", word[0:3])   # Pyt
print("word[2:5] →", word[2:5])   # tho
print("word[0:6] →", word[0:6])   # Python (full string)

# --- Example 2: Remember — end index is EXCLUDED ---
text = "Hello World"
print()
print("text[0:5] →", text[0:5])   # Hello
print("text[6:11] →", text[6:11]) # World

# =============================
# 2. OMITTING START OR END
# =============================

# --- Example 3: Omit start (from beginning) ---
word = "Python"
print()
print("word[:3] →", word[:3])    # Pyt
print("word[:1] →", word[:1])    # P

# --- Example 4: Omit end (to the end) ---
print("word[3:] →", word[3:])    # hon
print("word[1:] →", word[1:])    # ython

# --- Example 5: Omit both (full copy) ---
print("word[:] →", word[:])      # Python

# =============================
# 3. STEP SLICING (start:end:step)
# =============================

# --- Example 6: Every 2nd character ---
word = "Python"
print()
print("word[::2] →", word[::2])     # Pto
print("word[1::2] →", word[1::2])   # yhn

# --- Example 7: Every 3rd character ---
text = "abcdefghijkl"
print("text[::3] →", text[::3])     # adgj

# --- Example 8: Step with start and end ---
numbers = "0123456789"
print()
print("numbers[1:8:2] →", numbers[1:8:2])   # 1357
print("numbers[0:9:3] →", numbers[0:9:3])   # 036

# =============================
# 4. REVERSING A STRING
# =============================

# --- Example 9: Reverse with [::-1] ---
word = "Python"
reversed_word = word[::-1]
print()
print("Original:", word)
print("Reversed:", reversed_word)   # nohtyP

# --- Example 10: Reverse different strings ---
words = ["hello", "world", "racecar", "12345"]
print()
for w in words:
    print(w, "→", w[::-1])

# =============================
# 5. NEGATIVE INDICES IN SLICING
# =============================

# --- Example 11: Negative start and end ---
word = "Python"
print()
print("word[-4:-1] →", word[-4:-1])   # tho
print("word[-3:] →", word[-3:])       # hon
print("word[:-2] →", word[:-2])       # Pyth

# --- Example 12: Getting last N characters ---
text = "Hello World"
print()
print("Last 5:", text[-5:])    # World
print("Last 3:", text[-3:])    # rld
print("Last 1:", text[-1:])    # d

# =============================
# 6. OUT-OF-RANGE SLICING
# =============================

# --- Example 13: Slicing beyond string length ---
word = "Hi"
print()
print("word[0:100] →", word[0:100])   # Hi — no error!
print("word[5:10] →", word[5:10])     # (empty string)
print("word[-100:2] →", word[-100:2]) # Hi

# =============================
# 7. PRACTICAL SLICING PATTERNS
# =============================

# --- Example 14: Extract first and last halves ---
text = "HelloWorld"
mid = len(text) // 2
first_half = text[:mid]
second_half = text[mid:]
print()
print("Full:", text)
print("First half:", first_half)     # Hello
print("Second half:", second_half)   # World

# --- Example 15: Remove first and last characters ---
word = "(Hello)"
without_parens = word[1:-1]
print()
print("Original:", word)
print("Without parens:", without_parens)   # Hello

# --- Example 16: Extract every other character ---
secret = "HXeXlXlXo"
decoded = secret[::2]
print()
print("Encoded:", secret)
print("Decoded:", decoded)   # Hello

# ============================================
# TRY IT YOURSELF:
# 1. Extract the first 3 and last 3 characters of "Programming"
# 2. Reverse the word "desserts" — what word do you get?
# 3. Extract every 3rd character from "abcdefghijklmnop"
# ============================================
