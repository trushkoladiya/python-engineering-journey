# ============================================
# MODULE 5 - SUBTOPIC 1: String Creation
# ============================================

# =============================
# 1. SINGLE QUOTES
# =============================

# --- Example 1: Basic single-quoted string ---
name = 'Trush'
print("Name:", name)           # Name: Trush

# --- Example 2: Another single-quoted string ---
city = 'Ahmedabad'
print("City:", city)           # City: Ahmedabad

# =============================
# 2. DOUBLE QUOTES
# =============================

# --- Example 3: Basic double-quoted string ---
greeting = "Hello, World!"
print("Greeting:", greeting)   # Greeting: Hello, World!

# --- Example 4: Double quotes are identical to single quotes ---
word1 = 'Python'
word2 = "Python"
print("Same?", word1 == word2)  # Same? True

# =============================
# 3. MIXING QUOTES
# =============================

# --- Example 5: Apostrophe inside double quotes ---
message = "It's a wonderful day"
print(message)   # It's a wonderful day

# --- Example 6: Double quotes inside single quotes ---
html_tag = '<input type="text">'
print(html_tag)   # <input type="text">

# --- Example 7: Quote inside the same type (using escape) ---
escaped = 'It\'s also possible with backslash'
print(escaped)    # It's also possible with backslash

# =============================
# 4. TRIPLE QUOTES
# =============================

# --- Example 8: Triple single quotes ---
poem = '''Roses are red,
Violets are blue,
Python is great,
And so are you.'''
print(poem)

# --- Example 9: Triple double quotes ---
info = """Name: Trush
Age: 21
City: Ahmedabad"""
print()
print(info)

# =============================
# 5. MULTI-LINE STRINGS
# =============================

# --- Example 10: Multi-line address ---
address = """Trush Koladiya
42 MG Road
Floor 3
Ahmedabad, Gujarat 380001"""
print()
print("Address:")
print(address)

# --- Example 11: Multi-line preserves blank lines too ---
spaced = """Line 1

Line 3

Line 5"""
print()
print(spaced)

# =============================
# 6. EMPTY STRINGS
# =============================

# --- Example 12: Creating empty strings ---
empty1 = ""
empty2 = ''
print("Empty string length:", len(empty1))   # 0
print("Are they equal?", empty1 == empty2)   # True

# --- Example 13: Empty vs non-empty ---
text = "Hello"
nothing = ""
print("text is empty?", len(text) == 0)       # False
print("nothing is empty?", len(nothing) == 0) # True

# =============================
# 7. STRING TYPE
# =============================

# --- Example 14: Checking the type ---
word = "Python"
print("Type:", type(word))    # <class 'str'>

# --- Example 15: Numbers vs strings ---
num_str = "42"
num_int = 42
print("'42' type:", type(num_str))   # <class 'str'>
print("42 type:", type(num_int))     # <class 'int'>
print("Are they equal?", num_str == num_int)  # False — different types!

# ============================================
# TRY IT YOURSELF:
# 1. Create a string with your name using single quotes
# 2. Create a multi-line string with your address
# 3. Create a string that contains both single and double quotes
# ============================================
