# ============================================
# MODULE 5 - SUBTOPIC 14: Common String Patterns
# ============================================

# =============================
# 1. PALINDROME CHECK
# =============================

# --- Example 1: Simple palindrome check ---
word = "racecar"
if word == word[::-1]:
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is NOT a palindrome")

# --- Example 2: Check multiple words ---
words = ["madam", "hello", "level", "python", "radar", "world", "noon"]
print()
print("--- Palindrome Check ---")
for w in words:
    if w == w[::-1]:
        print(f"  {w} → ✓ palindrome")
    else:
        print(f"  {w} → ✗ not a palindrome")

# --- Example 3: Case-insensitive palindrome ---
word = "Racecar"
clean = word.lower()
print()
if clean == clean[::-1]:
    print(f"'{word}' is a palindrome (case-insensitive)")

# --- Example 4: Palindrome sentence (ignore spaces) ---
sentence = "was it a car or a cat i saw"
no_spaces = sentence.replace(" ", "")
print()
print(f"Sentence: '{sentence}'")
if no_spaces == no_spaces[::-1]:
    print("This sentence is a palindrome!")

# =============================
# 2. CHARACTER FREQUENCY COUNTING
# =============================

# --- Example 5: Count each character ---
text = "mississippi"
print()
print(f"--- Frequency in '{text}' ---")
counted = ""   # track what we already counted
for char in text:
    if char not in counted:
        print(f"  '{char}' appears {text.count(char)} times")
        counted = counted + char

# --- Example 6: Find the most common character ---
text = "abracadabra"
most_common = text[0]
highest_count = 0
counted = ""
for char in text:
    if char not in counted:
        c = text.count(char)
        if c > highest_count:
            highest_count = c
            most_common = char
        counted = counted + char
print()
print(f"In '{text}', most common: '{most_common}' ({highest_count} times)")

# --- Example 7: Count vowels vs consonants ---
text = "Hello World Python"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print()
print(f"Text: '{text}'")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

# =============================
# 3. SUBSTRING SEARCH PATTERNS
# =============================

# --- Example 8: Find all occurrences of a substring ---
text = "the cat sat on the mat near the hat"
sub = "the"
print()
print(f"--- Finding '{sub}' in text ---")
pos = text.find(sub)
positions = []
while pos != -1:
    positions = positions + [str(pos)]
    pos = text.find(sub, pos + 1)
print(f"Found at positions: {', '.join(positions)}")
print(f"Total: {text.count(sub)} times")

# --- Example 9: Replace and count ---
text = "I like Python. Python is great. Python is fun."
word = "Python"
count = text.count(word)
replaced = text.replace(word, "PYTHON")
print()
print(f"Original: {text}")
print(f"'{word}' found {count} times")
print(f"After replace: {replaced}")

# --- Example 10: Check if string starts or ends with something ---
filenames = ["report.pdf", "data.csv", "image.png", "notes.txt", "chart.pdf"]
print()
print("--- PDF files ---")
for name in filenames:
    if name[-4:] == ".pdf":
        print(f"  Found PDF: {name}")

# =============================
# 4. BASIC PARSING
# =============================

# --- Example 11: Parse key-value pairs ---
data = "Name: Trush, Age: 21, City: Ahmedabad"
pairs = data.split(", ")
print()
print("--- Parsed Data ---")
for pair in pairs:
    parts = pair.split(": ")
    key = parts[0]
    value = parts[1]
    print(f"  {key} → {value}")

# --- Example 12: Parse a URL-like string ---
url = "page=home&user=trush&theme=dark"
params = url.split("&")
print()
print("--- URL Parameters ---")
for param in params:
    parts = param.split("=")
    print(f"  {parts[0]}: {parts[1]}")

# --- Example 13: Parse CSV data ---
csv_data = """name,age,score
Trush,21,95
Rahul,22,87
Priya,23,92"""

lines = csv_data.split("\n")
header = lines[0].split(",")
print()
print("--- CSV Data ---")
print(f"  Columns: {', '.join(header)}")
print()
for i in range(1, len(lines)):
    values = lines[i].split(",")
    print(f"  Row {i}:")
    for j in range(len(header)):
        print(f"    {header[j]}: {values[j]}")

# =============================
# 5. WORD ANALYSIS
# =============================

# --- Example 14: Word count ---
text = "the quick brown fox jumps over the lazy dog"
words = text.split()
print()
print(f"Text: '{text}'")
print(f"Word count: {len(words)}")

# --- Example 15: Unique words ---
text = "the cat and the dog and the bird"
words = text.split()
unique = []
for word in words:
    if word not in unique:
        unique = unique + [word]
print()
print(f"Text: '{text}'")
print(f"Total words: {len(words)}")
print(f"Unique words: {len(unique)} → {', '.join(unique)}")

# --- Example 16: Word frequency ---
text = "to be or not to be that is the question"
words = text.split()
counted_words = []
print()
print(f"--- Word Frequency ---")
for word in words:
    if word not in counted_words:
        count = 0
        for w in words:
            if w == word:
                count += 1
        print(f"  '{word}': {count}")
        counted_words = counted_words + [word]

# =============================
# 6. STRING TRANSFORMATION
# =============================

# --- Example 17: Title case with custom rules ---
text = "hello world from python"
words = text.split()
title_words = []
for word in words:
    title_words = title_words + [word[0].upper() + word[1:]]
result = " ".join(title_words)
print()
print(f"Original: {text}")
print(f"Title case: {result}")

# --- Example 18: Censor a word ---
text = "I love Python and Python is great"
bad_word = "Python"
censored = text.replace(bad_word, "*" * len(bad_word))
print()
print(f"Original: {text}")
print(f"Censored: {censored}")

# --- Example 19: Reverse each word ---
sentence = "Hello World Python"
words = sentence.split()
reversed_words = []
for word in words:
    reversed_words = reversed_words + [word[::-1]]
result = " ".join(reversed_words)
print()
print(f"Original: {sentence}")
print(f"Words reversed: {result}")   # olleH dlroW nohtyP

# ============================================
# TRY IT YOURSELF:
# 1. Check if "A man a plan a canal Panama" is a palindrome (ignore spaces and case)
# 2. Count the frequency of each word in "she sells sea shells by the sea shore"
# 3. Parse "first_name=John&last_name=Doe&email=john@email.com" into key-value pairs
# ============================================
