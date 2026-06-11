# ============================================
# MODULE 5 - SUBTOPIC 2: String Indexing
# ============================================

# =============================
# 1. POSITIVE INDEXING
# =============================

# --- Example 1: Accessing characters by position ---
word = "Python"
print("Full word:", word)
print("Index 0:", word[0])   # P
print("Index 1:", word[1])   # y
print("Index 2:", word[2])   # t
print("Index 3:", word[3])   # h
print("Index 4:", word[4])   # o
print("Index 5:", word[5])   # n

# --- Example 2: First character of different strings ---
name = "Trush"
city = "Mumbai"
print()
print("First letter of", name, "is", name[0])   # T
print("First letter of", city, "is", city[0])    # M

# =============================
# 2. NEGATIVE INDEXING
# =============================

# --- Example 3: Counting from the end ---
word = "Python"
print()
print("Last character:", word[-1])         # n
print("Second from last:", word[-2])       # o
print("Third from last:", word[-3])        # h
print("First character:", word[-6])        # P

# --- Example 4: Getting last letter of any word ---
animal = "elephant"
print()
print("Last letter of", animal, "is", animal[-1])   # t

fruit = "banana"
print("Last letter of", fruit, "is", fruit[-1])     # a

# =============================
# 3. POSITIVE VS NEGATIVE INDEXING
# =============================

# --- Example 5: Same character, different index ---
text = "Hello"
# Positive:  H(0)  e(1)  l(2)  l(3)  o(4)
# Negative:  H(-5) e(-4) l(-3) l(-2) o(-1)

print()
print("text[0] ==", text[0], "  text[-5] ==", text[-5])   # H == H
print("text[4] ==", text[4], "  text[-1] ==", text[-1])   # o == o
print("Same?", text[0] == text[-5])   # True

# =============================
# 4. ACCESSING CHARACTERS WITH LOOPS
# =============================

# --- Example 6: Print each character with its index ---
word = "Code"
print()
print("Characters in", word, ":")
for i in range(len(word)):
    print("  Index", i, "→", word[i])

# --- Example 7: Print each character with negative index ---
word = "Hi!"
print()
print("Negative indexing for", word, ":")
for i in range(1, len(word) + 1):
    print("  Index", -i, "→", word[-i])

# =============================
# 5. FIRST AND LAST CHARACTERS
# =============================

# --- Example 8: Getting first and last ---
words = ["Python", "Java", "Go", "Rust"]
print()
for w in words:
    print(w, "→ first:", w[0], ", last:", w[-1])

# --- Example 9: Check if first and last are the same ---
test_words = ["level", "hello", "madam", "world"]
print()
for w in test_words:
    if w[0] == w[-1]:
        print(w, "→ first and last letter are the SAME")
    else:
        print(w, "→ first and last letter are DIFFERENT")

# =============================
# 6. INDEX SAFETY
# =============================

# --- Example 10: Safe index check ---
text = "Hi"
index = 5
print()
if index < len(text):
    print("Character at index", index, ":", text[index])
else:
    print("Index", index, "is out of range for", text, "(length", len(text), ")")

# --- Example 11: Safe access with condition ---
text = "Python"
for i in range(8):  # intentionally going beyond length
    if i < len(text):
        print("Index", i, "→", text[i])
    else:
        print("Index", i, "→ OUT OF RANGE")

# ============================================
# TRY IT YOURSELF:
# 1. Create a string and print its first, middle, and last character
# 2. Print all characters of a string in reverse using negative indexing
# 3. Check if the second character equals the second-to-last character
# ============================================
