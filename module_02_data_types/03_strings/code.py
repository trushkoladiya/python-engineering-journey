# ============================================
# MODULE 2 - SUBTOPIC 3: Strings (Deep Foundation)
# ============================================

# --- Example 1: Creating strings ---
s1 = 'single quotes'
s2 = "double quotes"
s3 = '''triple single
for multi-line'''
s4 = """triple double
also multi-line"""
print(s1)
print(s2)
print(s3)
print(s4)

# --- Example 2: Quotes inside strings ---
msg1 = "It's a great day"       # single quote inside double
msg2 = 'Trush said "hello"'     # double quote inside single
msg3 = "He said \"goodbye\""    # escape quote with backslash
print(msg1)
print(msg2)
print(msg3)

# --- Example 3: Positive indexing ---
word = "Python"
print(word[0])  # P
print(word[1])  # y
print(word[2])  # t
print(word[5])  # n (last character)

# --- Example 4: Negative indexing ---
word = "Python"
print(word[-1])  # n (last)
print(word[-2])  # o (second from last)
print(word[-6])  # P (first — same as word[0])

# --- Example 5: Slicing basics ---
text = "Hello World"
print(text[0:5])   # Hello (index 0 to 4)
print(text[6:11])  # World (index 6 to 10)
print(text[6:])    # World (index 6 to end)
print(text[:5])    # Hello (start to index 4)

# --- Example 6: Slicing with step ---
text = "abcdefgh"
print(text[::2])    # aceg  (every 2nd character)
print(text[1::2])   # bdfh  (every 2nd, starting from index 1)
print(text[::3])    # adg   (every 3rd character)

# --- Example 7: Reversing a string ---
name = "Trush"
print(name[::-1])  # hsurT

# --- Example 8: Immutability ---
greeting = "Hello"
# greeting[0] = "J"   # ❌ TypeError: strings are immutable
# Instead, create a new string:
new_greeting = "J" + greeting[1:]
print(new_greeting)  # Jello

# --- Example 9: Concatenation ---
first = "Hello"
second = "World"
result = first + " " + second
print(result)  # Hello World

# --- Example 10: Repetition ---
line = "-" * 30
print(line)        # ------------------------------
star = "⭐ " * 5
print(star)        # ⭐ ⭐ ⭐ ⭐ ⭐

# --- Example 11: String length ---
message = "Hello World"
print(len(message))  # 11 (spaces count!)
print(len(""))       # 0 (empty string)
print(len("abc"))    # 3

# --- Example 12: Basic string methods ---
msg = "Hello World"
print(msg.upper())              # HELLO WORLD
print(msg.lower())              # hello world
print(msg.title())              # Hello World
print(msg.replace("World", "Python"))  # Hello Python
print(msg.count("l"))           # 3
print(msg.startswith("Hello"))  # True
print(msg.endswith("World"))    # True

# --- Example 13: strip() — remove whitespace ---
messy = "   hello   "
print(messy.strip())   # "hello" (both sides)
print(messy.lstrip())  # "hello   " (left only)
print(messy.rstrip())  # "   hello" (right only)

# --- Example 14: find() — locate a substring ---
text = "I love Python"
print(text.find("Python"))   # 7 (starts at index 7)
print(text.find("Java"))     # -1 (not found)

# ============================================
# TRY IT YOURSELF:
# 1. Create a string and print every other character
# 2. Reverse your name using slicing
# 3. Try .upper(), .lower(), .replace() on a sentence
# ============================================
