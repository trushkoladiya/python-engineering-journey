# ============================================
# MODULE 5 - SUBTOPIC 4: String Immutability
# ============================================

# =============================
# 1. STRINGS CANNOT BE CHANGED
# =============================

# --- Example 1: Trying to modify a character (causes error) ---
word = "Hello"
# Uncomment the next line to see the error:
# word[0] = "J"   # TypeError: 'str' object does not support item assignment
print("Original word:", word)

# --- Example 2: We can READ characters, but not WRITE them ---
text = "Python"
print()
print("Reading is fine:", text[0], text[1], text[2])
# But this would fail:
# text[0] = "p"   # ❌ Not allowed!

# =============================
# 2. CREATING NEW STRINGS
# =============================

# --- Example 3: Replace first character ---
word = "Hello"
new_word = "J" + word[1:]
print()
print("Old:", word)        # Hello (unchanged!)
print("New:", new_word)    # Jello

# --- Example 4: Replace a character in the middle ---
name = "Trush"
# Change 'u' (index 2) to 'a'
new_name = name[:2] + "a" + name[3:]
print()
print("Old:", name)        # Trush
print("New:", new_name)    # Trash

# --- Example 5: Replace last character ---
word = "cart"
new_word = word[:-1] + "e"
print()
print("Old:", word)        # cart
print("New:", new_word)    # care

# =============================
# 3. REASSIGNMENT VS MODIFICATION
# =============================

# --- Example 6: Reassignment is fine ---
text = "Hello"
print()
print("Before:", text)     # Hello
text = "World"             # ✅ This is reassignment, not modification
print("After:", text)      # World

# --- Example 7: Variable points to a NEW string ---
greeting = "Good morning"
print()
print("Original:", greeting)
greeting = "Good evening"   # ✅ New string assigned to same variable
print("Updated:", greeting)

# =============================
# 4. BUILDING NEW STRINGS
# =============================

# --- Example 8: Build a string character by character ---
original = "Hello"
result = ""
for char in original:
    result = result + char + "-"
print()
print("Spaced out:", result)   # H-e-l-l-o-

# --- Example 9: Replace all occurrences manually ---
text = "banana"
new_text = ""
for char in text:
    if char == "a":
        new_text = new_text + "@"
    else:
        new_text = new_text + char
print()
print("Original:", text)     # banana
print("Modified:", new_text) # b@n@n@

# --- Example 10: Remove a character by skipping it ---
text = "Hello World"
# Remove all spaces
no_spaces = ""
for char in text:
    if char != " ":
        no_spaces = no_spaces + char
print()
print("With spaces:", text)         # Hello World
print("Without spaces:", no_spaces) # HelloWorld

# =============================
# 5. PROOF THAT ORIGINALS DON'T CHANGE
# =============================

# --- Example 11: Original is always preserved ---
original = "Python"
upper_version = original[:1] + "YTHON"
reversed_version = original[::-1]
print()
print("Original:", original)          # Python
print("Upper version:", upper_version) # PYTHON
print("Reversed:", reversed_version)   # nohtyP
print("Original again:", original)     # Python — still unchanged!

# --- Example 12: Multiple "modifications" ---
word = "cat"
print()
print("Start:", word)
word1 = "b" + word[1:]      # bat
word2 = word[0] + "o" + word[2:]  # cot
word3 = word[:2] + "r"      # car
print("Change c→b:", word1)
print("Change a→o:", word2)
print("Change t→r:", word3)
print("Original:", word)     # cat — never changed!

# ============================================
# TRY IT YOURSELF:
# 1. Take the string "python" and create a new string "Python" (capitalize first letter)
# 2. Take "Hello World" and create "Hello_World" (replace space with underscore)
# 3. Take "abcdef" and create "abcXef" (replace 'd' with 'X')
# ============================================
