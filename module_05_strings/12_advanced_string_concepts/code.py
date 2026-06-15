# ============================================
# MODULE 5 - SUBTOPIC 12: Advanced String Concepts
# ============================================

# =============================
# 1. STRING COMPARISON (LEXICOGRAPHIC)
# =============================

# --- Example 1: Basic comparisons ---
print("--- String Comparison ---")
print("'apple' < 'banana':", "apple" < "banana")     # True
print("'apple' < 'apricot':", "apple" < "apricot")   # True
print("'cat' == 'cat':", "cat" == "cat")              # True
print("'cat' > 'bat':", "cat" > "bat")                # True

# --- Example 2: Case matters in comparison ---
print()
print("'A' < 'a':", "A" < "a")        # True (65 < 97)
print("'Z' < 'a':", "Z" < "a")        # True (90 < 97)
print("'Apple' < 'apple':", "Apple" < "apple")  # True

# --- Example 3: Comparing words ---
words = ["banana", "apple", "cherry", "date"]
print()
print("Words:", words)
# Find the smallest (alphabetically first)
smallest = words[0]
for word in words:
    if word < smallest:
        smallest = word
print("First alphabetically:", smallest)   # apple

# --- Example 4: Sorting comparison ---
words = ["banana", "Apple", "cherry", "apple"]
print()
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if words[i] > words[j]:
            print(f"'{words[i]}' comes after '{words[j]}'")

# =============================
# 2. ord() — CHARACTER TO NUMBER
# =============================

# --- Example 5: Basic ord() ---
print()
print("--- ord() ---")
print("ord('A'):", ord("A"))    # 65
print("ord('B'):", ord("B"))    # 66
print("ord('Z'):", ord("Z"))    # 90
print("ord('a'):", ord("a"))    # 97
print("ord('z'):", ord("z"))    # 122
print("ord('0'):", ord("0"))    # 48
print("ord('9'):", ord("9"))    # 57
print("ord(' '):", ord(" "))    # 32

# --- Example 6: Show codes for a word ---
word = "Hello"
print()
print(f"Character codes for '{word}':")
for char in word:
    print(f"  '{char}' → {ord(char)}")

# --- Example 7: Why 'A' < 'a' ---
print()
print(f"'A' has code {ord('A')}, 'a' has code {ord('a')}")
print(f"Since {ord('A')} < {ord('a')}, 'A' < 'a' is True")

# =============================
# 3. chr() — NUMBER TO CHARACTER
# =============================

# --- Example 8: Basic chr() ---
print()
print("--- chr() ---")
print("chr(65):", chr(65))     # A
print("chr(97):", chr(97))     # a
print("chr(48):", chr(48))     # 0
print("chr(32):", chr(32))     # (space)

# --- Example 9: Print the alphabet using chr() ---
print()
print("Uppercase alphabet:")
alphabet = ""
for code in range(65, 91):   # A=65 to Z=90
    alphabet = alphabet + chr(code)
print(alphabet)

print()
print("Lowercase alphabet:")
alphabet = ""
for code in range(97, 123):   # a=97 to z=122
    alphabet = alphabet + chr(code)
print(alphabet)

# --- Example 10: Print digits using chr() ---
print()
print("Digits:")
for code in range(48, 58):   # '0'=48 to '9'=57
    print(chr(code), end=" ")
print()

# =============================
# 4. ASCII TABLE (PARTIAL)
# =============================

# --- Example 11: ASCII table for printable characters ---
print()
print("--- Partial ASCII Table ---")
print(f"{'Code':<6} {'Char':<6} {'Code':<6} {'Char':<6}")
print("-" * 24)
for i in range(32, 48):
    j = i + 48
    if j <= 126:
        print(f"{i:<6} {chr(i):<6} {j:<6} {chr(j):<6}")
    else:
        print(f"{i:<6} {chr(i):<6}")

# =============================
# 5. PRACTICAL USES
# =============================

# --- Example 12: Simple Caesar cipher (shift by 1) ---
text = "HELLO"
shifted = ""
for char in text:
    new_code = ord(char) + 1
    shifted = shifted + chr(new_code)
print()
print("Original:", text)
print("Shifted by 1:", shifted)   # IFMMP

# --- Example 13: Decode it back ---
decoded = ""
for char in shifted:
    original_code = ord(char) - 1
    decoded = decoded + chr(original_code)
print("Decoded:", decoded)   # HELLO

# --- Example 14: Check if character is uppercase using ord ---
text = "Hello World"
print()
print(f"Uppercase chars in '{text}':")
for char in text:
    if ord(char) >= 65 and ord(char) <= 90:
        print(f"  '{char}' (code {ord(char)})")

# --- Example 15: Distance between characters ---
char1 = "A"
char2 = "Z"
distance = ord(char2) - ord(char1)
print()
print(f"Distance from '{char1}' to '{char2}': {distance}")   # 25

# =============================
# 6. UNICODE
# =============================

# --- Example 16: Unicode escape sequences ---
print()
print("--- Unicode ---")
print("Heart:", "\u2764")
print("Star:", "\u2605")
print("Smiley:", "\u263A")
print("Check:", "\u2713")
print("Cross:", "\u2717")

# --- Example 17: Unicode characters are just strings ---
heart = "\u2764"
print()
print("Type:", type(heart))
print("Length:", len(heart))     # 1 — it's just one character
print("Code:", ord(heart))      # 10084

# --- Example 18: Emoji (wider Unicode) ---
print()
print("Python \u2764 Unicode")

# ============================================
# TRY IT YOURSELF:
# 1. Find the ord() values for all characters in your name
# 2. Print the uppercase alphabet backwards using chr() and a loop
# 3. Create a simple cipher that shifts each letter by 3
# ============================================
