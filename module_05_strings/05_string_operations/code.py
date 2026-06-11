# ============================================
# MODULE 5 - SUBTOPIC 5: String Operations
# ============================================

# =============================
# 1. CONCATENATION (+)
# =============================

# --- Example 1: Basic concatenation ---
first = "Hello"
second = "World"
result = first + " " + second
print("Concatenated:", result)   # Hello World

# --- Example 2: Building a sentence ---
name = "Trush"
age = "21"
sentence = "My name is " + name + " and I am " + age + " years old."
print(sentence)

# --- Example 3: Concatenating in a loop ---
word = "Python"
spaced = ""
for char in word:
    spaced = spaced + char + " "
print("Spaced:", spaced)   # P y t h o n

# =============================
# 2. REPETITION (*)
# =============================

# --- Example 4: Repeat a string ---
line = "-" * 30
print()
print(line)          # ------------------------------
print("Title Here")
print(line)          # ------------------------------

# --- Example 5: Repeating words ---
laugh = "ha" * 5
print("Laughing:", laugh)   # hahahahaha

# --- Example 6: Creating patterns ---
print()
for i in range(1, 6):
    print("*" * i)
# *
# **
# ***
# ****
# *****

# --- Example 7: Building a box ---
print()
width = 20
print("+" + "-" * (width - 2) + "+")
print("|" + " " * (width - 2) + "|")
print("|" + "  Hello World!  " + "|")
print("|" + " " * (width - 2) + "|")
print("+" + "-" * (width - 2) + "+")

# =============================
# 3. MEMBERSHIP (in, not in)
# =============================

# --- Example 8: Check if substring exists ---
text = "Hello World"
print()
print("'Hello' in text:", "Hello" in text)     # True
print("'World' in text:", "World" in text)     # True
print("'Python' in text:", "Python" in text)   # False

# --- Example 9: Using 'not in' ---
email = "trushkoladiya.work@gmail.com"
print()
print("Has @?", "@" in email)              # True
print("Missing @?", "@" not in email)      # False

# --- Example 10: Using membership with conditions ---
sentence = "The quick brown fox jumps over the lazy dog"
print()
words_to_find = ["fox", "cat", "dog", "bird"]
for word in words_to_find:
    if word in sentence:
        print(word, "→ FOUND")
    else:
        print(word, "→ not found")

# --- Example 11: Case-sensitive membership ---
text = "Hello World"
print()
print("'hello' in text:", "hello" in text)   # False — case matters!
print("'Hello' in text:", "Hello" in text)   # True

# =============================
# 4. LENGTH (len())
# =============================

# --- Example 12: Basic length ---
word = "Python"
print()
print("Length of", word, ":", len(word))   # 6

# --- Example 13: Spaces count ---
text = "Hi there"
print("Length of '" + text + "':", len(text))   # 8

# --- Example 14: Empty string length ---
empty = ""
print("Empty string length:", len(empty))   # 0

# --- Example 15: Comparing lengths ---
words = ["Python", "Java", "Go", "JavaScript", "C"]
print()
for w in words:
    print(w, "→", len(w), "characters")

# --- Example 16: Finding the longest word ---
words = ["apple", "banana", "cherry", "kiwi", "strawberry"]
longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
print()
print("Longest word:", longest)   # strawberry

# =============================
# 5. COMBINING OPERATIONS
# =============================

# --- Example 17: Concatenation + length ---
first = "Hello"
second = "World"
combined = first + second
print()
print("Combined:", combined)
print("Length:", len(combined))    # 10

# --- Example 18: Check before concatenate ---
text = "Python is fun"
addition = " and easy"
if addition not in text:
    text = text + addition
print(text)   # Python is fun and easy

# ============================================
# TRY IT YOURSELF:
# 1. Create a horizontal line of 40 equal signs using repetition
# 2. Check if your name is in the string "Trush, Rahul, Priya"
# 3. Find the length of "supercalifragilisticexpialidocious"
# ============================================
