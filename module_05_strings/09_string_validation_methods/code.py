# ============================================
# MODULE 5 - SUBTOPIC 9: String Validation Methods
# ============================================

# =============================
# 1. isalpha() — Only Letters?
# =============================

# --- Example 1: Basic isalpha() checks ---
print("--- isalpha() ---")
print("'Hello':", "Hello".isalpha())          # True
print("'Hello1':", "Hello1".isalpha())        # False (digit)
print("'Hello World':", "Hello World".isalpha())  # False (space)
print("'abc':", "abc".isalpha())              # True

# --- Example 2: Validate name input ---
names = ["Trush", "Rahul123", "Priya!", "Dev"]
print()
for name in names:
    if name.isalpha():
        print(name, "→ valid name")
    else:
        print(name, "→ INVALID (not all letters)")

# =============================
# 2. isdigit() — Only Digits?
# =============================

# --- Example 3: Basic isdigit() checks ---
print()
print("--- isdigit() ---")
print("'12345':", "12345".isdigit())       # True
print("'123.45':", "123.45".isdigit())     # False (dot)
print("'12 34':", "12 34".isdigit())       # False (space)
print("'-5':", "-5".isdigit())             # False (minus sign)

# --- Example 4: Check if a string can be an integer ---
values = ["42", "3.14", "100", "abc", "-7", "0"]
print()
for val in values:
    if val.isdigit():
        print(val, "→ is a whole positive number")
    else:
        print(val, "→ NOT a simple digit string")

# =============================
# 3. isalnum() — Letters and Digits Only?
# =============================

# --- Example 5: Basic isalnum() checks ---
print()
print("--- isalnum() ---")
print("'Hello123':", "Hello123".isalnum())    # True
print("'Hello 123':", "Hello 123".isalnum())  # False (space)
print("'Hello!':", "Hello!".isalnum())        # False (!)
print("'abc':", "abc".isalnum())              # True
print("'123':", "123".isalnum())              # True

# --- Example 6: Validate username ---
usernames = ["trush99", "rahul_dev", "priya!", "dev42", "ankit 7"]
print()
for username in usernames:
    if username.isalnum():
        print(username, "→ valid username")
    else:
        print(username, "→ INVALID (special chars or spaces)")

# =============================
# 4. isspace() — Only Whitespace?
# =============================

# --- Example 7: Basic isspace() checks ---
print()
print("--- isspace() ---")
print("'   ':", "   ".isspace())          # True
print("'\\t\\n':", "\t\n".isspace())      # True
print("' a ':", " a ".isspace())          # False
print("'':", "".isspace())                # False (empty!)

# --- Example 8: Check for blank strings ---
strings = ["Hello", "   ", "", "\t", "  hi  ", "\n\n"]
print()
for s in strings:
    if len(s) > 0 and s.isspace():
        print(repr(s), "→ blank (only whitespace)")
    elif len(s) == 0:
        print(repr(s), "→ empty string")
    else:
        print(repr(s), "→ has content")

# =============================
# 5. islower() and isupper()
# =============================

# --- Example 9: islower() checks ---
print()
print("--- islower() ---")
print("'hello':", "hello".islower())       # True
print("'Hello':", "Hello".islower())       # False
print("'hello123':", "hello123".islower()) # True (digits don't matter)

# --- Example 10: isupper() checks ---
print()
print("--- isupper() ---")
print("'HELLO':", "HELLO".isupper())       # True
print("'Hello':", "Hello".isupper())       # False
print("'HELLO123':", "HELLO123".isupper()) # True (digits don't matter)

# --- Example 11: Classify strings by case ---
words = ["hello", "WORLD", "Python", "ABC", "xyz", "123"]
print()
for w in words:
    if w.islower():
        print(w, "→ all lowercase")
    elif w.isupper():
        print(w, "→ ALL UPPERCASE")
    else:
        print(w, "→ mixed or no letters")

# =============================
# 6. EMPTY STRING BEHAVIOR
# =============================

# --- Example 12: Empty strings return False ---
print()
print("--- Empty string checks ---")
empty = ""
print("''.isalpha():", empty.isalpha())     # False
print("''.isdigit():", empty.isdigit())     # False
print("''.isalnum():", empty.isalnum())     # False
print("''.isspace():", empty.isspace())     # False
print("''.islower():", empty.islower())     # False
print("''.isupper():", empty.isupper())     # False

# =============================
# 7. PRACTICAL VALIDATION
# =============================

# --- Example 13: Simple password strength check ---
passwords = ["abc", "ABC123", "hello world", "Pass1234", "12345"]
print()
print("--- Password checks ---")
for pwd in passwords:
    has_upper = False
    has_lower = False
    has_digit = False

    for char in pwd:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit and len(pwd) >= 8:
        print(pwd, "→ STRONG")
    else:
        print(pwd, "→ WEAK")

# --- Example 14: Count character types ---
text = "Hello World 123!"
letters = 0
digits = 0
spaces = 0
others = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1
print()
print("Text:", text)
print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)
print("Other:", others)

# ============================================
# TRY IT YOURSELF:
# 1. Check if "Python3" is all letters (isalpha)
# 2. Validate if "12345" contains only digits
# 3. Write a loop that counts how many uppercase letters are in "Hello World PyThOn"
# ============================================
