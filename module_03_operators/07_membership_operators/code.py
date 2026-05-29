# ============================================
# MODULE 3 - SUBTOPIC 7: Membership Operators
# ============================================

# --- Example 1: in with strings ---
message = "Python is fun"
print("Python" in message)    # True
print("python" in message)    # False (case-sensitive!)
print("is" in message)        # True
print("Java" in message)      # False

# --- Example 2: not in with strings ---
email = "trushkoladiya.work@gmail.com"
print("@" in email)           # True
print("@" not in email)       # False
print(".com" in email)        # True

# --- Example 3: in with lists ---
numbers = [10, 20, 30, 40, 50]
print(30 in numbers)          # True
print(99 in numbers)          # False
print(10 in numbers)          # True

# --- Example 4: not in with lists ---
fruits = ["apple", "banana", "cherry"]
print("mango" not in fruits)   # True — mango is missing
print("apple" not in fruits)   # False — apple IS there

# --- Example 5: in with tuples ---
colors = ("red", "green", "blue")
print("red" in colors)         # True
print("yellow" in colors)      # False
print("green" not in colors)   # False — green IS there

# --- Example 6: in with sets ---
vowels = {"a", "e", "i", "o", "u"}
print("a" in vowels)           # True
print("z" in vowels)           # False
print("x" not in vowels)       # True

# --- Example 7: in with dictionaries (checks KEYS) ---
student = {"name": "Trush", "age": 21, "grade": "A"}
print("name" in student)       # True  — "name" is a key
print("Trush" in student)      # False — "Trush" is a value, not a key
print("age" in student)        # True
print("email" in student)      # False

# --- Example 8: not in with dictionaries ---
config = {"theme": "dark", "language": "en"}
print("theme" in config)       # True
print("font" not in config)    # True — no "font" key

# --- Example 9: Checking single characters ---
letter = "e"
print(letter in "hello")       # True
print(letter in "world")       # False
print(letter in "aeiou")       # True — it's a vowel!

# --- Example 10: Practical usage — checking substrings ---
filename = "report_2024.pdf"
print(".pdf" in filename)      # True — it's a PDF
print(".txt" in filename)      # False

url = "https://example.com"
print("https" in url)          # True — secure connection
print("http" in url)           # True — "http" is inside "https" too

# ============================================
# TRY IT YOURSELF:
# 1. Check if "o" is in "Hello World"
# 2. Check if 7 is NOT in [1, 2, 3, 4, 5]
# 3. Check if "password" is a key in {"username": "admin", "password": "1234"}
# ============================================
