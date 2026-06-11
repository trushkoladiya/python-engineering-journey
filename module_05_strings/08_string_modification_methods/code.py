# ============================================
# MODULE 5 - SUBTOPIC 8: String Modification Methods
# ============================================

# =============================
# 1. replace()
# =============================

# --- Example 1: Basic replacement ---
text = "Hello World"
new_text = text.replace("World", "Python")
print("Original:", text)
print("Replaced:", new_text)   # Hello Python

# --- Example 2: Replace a character ---
text = "banana"
print()
print("Replace 'a' with 'o':", text.replace("a", "o"))   # bonono

# --- Example 3: Replace with empty string (delete) ---
text = "H-e-l-l-o"
print("Remove dashes:", text.replace("-", ""))   # Hello

# --- Example 4: Limit the number of replacements ---
text = "aaa bbb aaa bbb aaa"
print()
print("Replace all 'aaa':", text.replace("aaa", "XXX"))
print("Replace first 2:", text.replace("aaa", "XXX", 2))

# --- Example 5: Chaining replacements ---
text = "Hello, World!"
clean = text.replace(",", "").replace("!", "")
print()
print("Original:", text)
print("No punctuation:", clean)   # Hello World

# =============================
# 2. split()
# =============================

# --- Example 6: Split by whitespace (default) ---
sentence = "Hello World Python"
words = sentence.split()
print()
print("Sentence:", sentence)
print("Words:", words)   # ['Hello', 'World', 'Python']

# --- Example 7: Iterate over split result ---
sentence = "The quick brown fox"
print()
for word in sentence.split():
    print("  Word:", word)

# --- Example 8: Split by comma ---
csv_data = "Trush,21,Ahmedabad"
parts = csv_data.split(",")
print()
print("CSV:", csv_data)
print("Parts:", parts)   # ['Trush', '21', 'Ahmedabad']
print("Name:", parts[0])
print("Age:", parts[1])
print("City:", parts[2])

# --- Example 9: Split by custom separator ---
date = "2024-01-15"
parts = date.split("-")
print()
print("Date:", date)
print("Year:", parts[0])
print("Month:", parts[1])
print("Day:", parts[2])

# --- Example 10: Split with limit ---
text = "one two three four five"
print()
print("Split all:", text.split())
print("Split max 2:", text.split(" ", 2))   # ['one', 'two', 'three four five']

# --- Example 11: Split by newline ---
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.split("\n")
print()
print("Lines:")
for line in lines:
    print("  →", line)

# =============================
# 3. join()
# =============================

# --- Example 12: Join with space ---
words = ["Hello", "World", "Python"]
result = " ".join(words)
print()
print("Joined with space:", result)   # Hello World Python

# --- Example 13: Join with different separators ---
words = ["apple", "banana", "cherry"]
print()
print("Comma:", ", ".join(words))     # apple, banana, cherry
print("Dash:", "-".join(words))       # apple-banana-cherry
print("Arrow:", " → ".join(words))    # apple → banana → cherry
print("Nothing:", "".join(words))     # applebananacherry

# --- Example 14: Join characters of a string ---
word = "Python"
spaced = " ".join(word)
print()
print("Spaced:", spaced)   # P y t h o n

# --- Example 15: Join with newlines ---
lines = ["First line", "Second line", "Third line"]
text = "\n".join(lines)
print()
print(text)

# =============================
# 4. COMBINING METHODS
# =============================

# --- Example 16: Split and rejoin ---
sentence = "Hello   World   Python"   # multiple spaces
words = sentence.split()              # splits by any whitespace
clean = " ".join(words)               # rejoin with single space
print()
print("Messy:", sentence)
print("Clean:", clean)   # Hello World Python

# --- Example 17: Replace and split ---
csv_line = "Trush; Rahul; Priya; Dev"
names = csv_line.replace(" ", "").split(";")
print()
print("Names:")
for name in names:
    print("  →", name)

# --- Example 18: Reverse words in a sentence ---
sentence = "Hello World Python"
words = sentence.split()
words_reversed = []
for word in words:
    words_reversed = [word] + words_reversed   # prepend
reversed_sentence = " ".join(words_reversed)
print()
print("Original:", sentence)
print("Reversed words:", reversed_sentence)   # Python World Hello

# ============================================
# TRY IT YOURSELF:
# 1. Replace all spaces in "Hello World Python" with underscores
# 2. Split "red,green,blue,yellow" by comma and print each color
# 3. Join the characters of your name with dashes
# ============================================
