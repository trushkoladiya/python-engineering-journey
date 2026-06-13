# ============================================
# MODULE 5 - SUBTOPIC 6: String Iteration
# ============================================

# =============================
# 1. FOR LOOP WITH CHARACTERS
# =============================

# --- Example 1: Print each character ---
word = "Python"
print("Characters in", word, ":")
for char in word:
    print(" ", char)

# --- Example 2: Process each character ---
text = "Hello"
print()
for char in text:
    print(char, "→", char * 3)
# H → HHH
# e → eee
# etc.

# =============================
# 2. INDEX-BASED ITERATION
# =============================

# --- Example 3: Using range(len()) ---
word = "Code"
print()
print("Index-based iteration:")
for i in range(len(word)):
    print("  word[" + str(i) + "] =", word[i])

# --- Example 4: Print with position numbers ---
text = "Python"
print()
for i in range(len(text)):
    print("  Position", i + 1, ":", text[i])

# =============================
# 3. WHILE LOOP ITERATION
# =============================

# --- Example 5: Basic while loop ---
word = "Hello"
i = 0
print()
print("Using while loop:")
while i < len(word):
    print(" ", word[i])
    i += 1

# --- Example 6: While loop with step (every other character) ---
text = "abcdefgh"
i = 0
print()
print("Every other character:")
while i < len(text):
    print(" ", text[i])
    i += 2   # skip one character

# =============================
# 4. COUNTING CHARACTERS
# =============================

# --- Example 7: Count specific character ---
text = "mississippi"
count = 0
for char in text:
    if char == "s":
        count += 1
print()
print("Letter 's' in", text, ":", count, "times")   # 4

# --- Example 8: Count vowels ---
text = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print("Vowels in '" + text + "':", vowel_count)   # 3

# --- Example 9: Count uppercase and lowercase ---
text = "Hello World Python"
upper_count = 0
lower_count = 0
space_count = 0
for char in text:
    if char >= "A" and char <= "Z":
        upper_count += 1
    elif char >= "a" and char <= "z":
        lower_count += 1
    elif char == " ":
        space_count += 1
print()
print("Text:", text)
print("Uppercase:", upper_count)
print("Lowercase:", lower_count)
print("Spaces:", space_count)

# =============================
# 5. BUILDING NEW STRINGS
# =============================

# --- Example 10: Build reversed string ---
word = "Python"
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word   # prepend each character
print()
print("Original:", word)
print("Reversed:", reversed_word)

# --- Example 11: Build string with separator ---
word = "Hello"
result = ""
for i in range(len(word)):
    result = result + word[i]
    if i < len(word) - 1:
        result = result + "-"
print("Separated:", result)   # H-e-l-l-o

# --- Example 12: Extract only digits ---
mixed = "abc123def456"
digits = ""
for char in mixed:
    if char >= "0" and char <= "9":
        digits = digits + char
print()
print("Original:", mixed)
print("Digits only:", digits)   # 123456

# =============================
# 6. SEARCHING IN STRINGS
# =============================

# --- Example 13: Find position of first occurrence ---
text = "Hello World"
target = "o"
print()
for i in range(len(text)):
    if text[i] == target:
        print("First '" + target + "' found at index", i)
        break

# --- Example 14: Find all positions of a character ---
text = "banana"
target = "a"
print()
print("Positions of '" + target + "' in", text, ":")
for i in range(len(text)):
    if text[i] == target:
        print("  Index", i)

# =============================
# 7. PRACTICAL PATTERNS
# =============================

# --- Example 15: Check if string has only letters ---
text = "HelloWorld"
all_letters = True
for char in text:
    if not ((char >= "a" and char <= "z") or (char >= "A" and char <= "Z")):
        all_letters = False
        break
print()
print(text, "has only letters?", all_letters)   # True

text2 = "Hello World!"
all_letters = True
for char in text2:
    if not ((char >= "a" and char <= "z") or (char >= "A" and char <= "Z")):
        all_letters = False
        break
print(text2, "has only letters?", all_letters)   # False

# ============================================
# TRY IT YOURSELF:
# 1. Count how many times the letter 'e' appears in "engineering"
# 2. Build a new string from "Hello" with each character doubled: "HHeelllloo"
# 3. Print the characters of "Python" in reverse using a while loop
# ============================================
