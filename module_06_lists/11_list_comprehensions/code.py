# ============================================
# MODULE 6 - SUBTOPIC 11: List Comprehensions
# ============================================

# =============================
# 1. BASIC LIST COMPREHENSION
# =============================

# --- Example 1: Squares ---
squares = [x ** 2 for x in range(6)]
print("Squares:", squares)   # [0, 1, 4, 9, 16, 25]

# Compare with traditional way:
squares_old = []
for x in range(6):
    squares_old.append(x ** 2)
print("Same?", squares == squares_old)   # True

# --- Example 2: Doubling numbers ---
doubled = [n * 2 for n in range(1, 6)]
print("\nDoubled:", doubled)   # [2, 4, 6, 8, 10]

# --- Example 3: String operations ---
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print("Upper:", upper)   # ['HELLO', 'WORLD', 'PYTHON']

# --- Example 4: Lengths of words ---
words = ["apple", "banana", "cherry", "kiwi"]
lengths = [len(w) for w in words]
print("Lengths:", lengths)   # [5, 6, 6, 4]

# =============================
# 2. CONDITIONAL COMPREHENSION (filter)
# =============================

# --- Example 5: Even numbers only ---
evens = [x for x in range(20) if x % 2 == 0]
print("\nEvens:", evens)

# --- Example 6: Positive numbers only ---
nums = [5, -3, 8, -1, 0, 7, -4, 2]
positives = [n for n in nums if n > 0]
print("Positives:", positives)   # [5, 8, 7, 2]

# --- Example 7: Words longer than 4 characters ---
words = ["hi", "hello", "hey", "world", "ok", "python"]
long_words = [w for w in words if len(w) > 4]
print("Long words:", long_words)   # ['hello', 'world', 'python']

# --- Example 8: Filter and transform ---
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [n ** 2 for n in nums if n % 2 == 0]
print("Even squares:", even_squares)   # [4, 16, 36, 64, 100]

# =============================
# 3. IF-ELSE IN COMPREHENSION
# =============================

# --- Example 9: Label even/odd ---
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print("\nLabels:", labels)   # ['even', 'odd', 'even', 'odd', 'even', 'odd']

# --- Example 10: Pass/fail ---
scores = [85, 42, 91, 67, 38, 75]
results = ["pass" if s >= 50 else "fail" for s in scores]
print("Results:", results)

# --- Example 11: Absolute values ---
nums = [5, -3, 8, -1, -7, 2]
absolute = [n if n >= 0 else -n for n in nums]
print("Absolute:", absolute)   # [5, 3, 8, 1, 7, 2]

# --- Example 12: Clamp values (min 0, max 100) ---
raw = [-5, 25, 110, 50, -10, 100, 75, 150]
clamped = [max(0, min(100, x)) for x in raw]
print("Clamped:", clamped)   # [0, 25, 100, 50, 0, 100, 75, 100]

# =============================
# 4. NESTED LIST COMPREHENSION
# =============================

# --- Example 13: Create a 3x3 matrix of zeros ---
matrix = [[0 for col in range(3)] for row in range(3)]
print("\n3x3 zeros:")
for row in matrix:
    print(f"  {row}")

# --- Example 14: Multiplication table ---
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication table:")
for row in table:
    print(f"  {row}")

# --- Example 15: Flatten a nested list ---
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for row in nested for item in row]
print(f"\nNested: {nested}")
print(f"Flat: {flat}")   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# =============================
# 5. COMPREHENSION FROM STRINGS
# =============================

# --- Example 16: Characters to list ---
vowels = [c for c in "Hello World" if c.lower() in "aeiou"]
print(f"\nVowels in 'Hello World': {vowels}")

# --- Example 17: Words from sentence ---
sentence = "the quick brown fox jumps over the lazy dog"
short_words = [w for w in sentence.split() if len(w) <= 3]
print(f"Short words: {short_words}")

# --- Example 18: Character codes ---
word = "Python"
codes = [ord(c) for c in word]
print(f"Codes of '{word}': {codes}")

# =============================
# 6. PRACTICAL PATTERNS
# =============================

# --- Example 19: Remove duplicates (preserving order) ---
data = [1, 2, 3, 2, 4, 1, 5, 3]
seen = []
unique = []
for item in data:
    if item not in seen:
        seen.append(item)
        unique.append(item)
print(f"\nOriginal: {data}")
print(f"Unique: {unique}")

# --- Example 20: Convert list of strings to integers ---
str_nums = ["10", "20", "30", "40"]
int_nums = [int(s) for s in str_nums]
print(f"\nStrings: {str_nums}")
print(f"Integers: {int_nums}")

# --- Example 21: Generate coordinates ---
coords = [(x, y) for x in range(3) for y in range(3)]
print(f"\nCoordinates: {coords}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a list of cubes from 1 to 10 using comprehension
# 2. Filter words that start with 'a' from a sentence
# 3. Create a 5x5 grid filled with the value True
# ============================================
