# ============================================
# MODULE 7 - SUBTOPIC 22: Dictionary Comprehension
# ============================================

# =============================
# 1. BASIC COMPREHENSION
# =============================

# --- Example 1: Squares ---
squares = {x: x * x for x in range(1, 6)}
print("Squares:", squares)

# --- Example 2: Cubes ---
cubes = {x: x ** 3 for x in range(1, 6)}
print("Cubes:", cubes)

# --- Example 3: String lengths ---
words = ["hello", "world", "python", "code"]
lengths = {word: len(word) for word in words}
print("Lengths:", lengths)

# =============================
# 2. WITH CONDITION
# =============================

# --- Example 4: Only even numbers ---
even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print("\nEven squares:", even_squares)

# --- Example 5: Only passing scores ---
all_scores = {"Trush": 95, "Rahul": 42, "Charlie": 78, "Diana": 35}
passing = {name: score for name, score in all_scores.items() if score >= 50}
print("Passing:", passing)

# --- Example 6: Only long words ---
words = ["hi", "hello", "hey", "howdy", "yo", "greetings"]
long_words = {w: len(w) for w in words if len(w) > 3}
print("Long words:", long_words)

# =============================
# 3. FROM TWO LISTS (using zip)
# =============================

# --- Example 7: Names and scores ---
names = ["Trush", "Rahul", "Charlie"]
scores = [95, 87, 92]
result = {name: score for name, score in zip(names, scores)}
print("\nFrom two lists:", result)

# --- Example 8: Countries and capitals ---
countries = ["India", "USA", "Japan"]
capitals = ["Delhi", "Washington", "Tokyo"]
country_map = {c: cap for c, cap in zip(countries, capitals)}
print("Capitals:", country_map)

# =============================
# 4. TRANSFORMING A DICTIONARY
# =============================

# --- Example 9: Apply discount ---
prices = {"apple": 2.50, "banana": 1.75, "cherry": 4.00}
discounted = {item: round(price * 0.8, 2) for item, price in prices.items()}
print(f"\nOriginal:   {prices}")
print(f"Discounted: {discounted}")

# --- Example 10: Uppercase keys ---
data = {"name": "Trush", "city": "Mumbai", "country": "India"}
upper_keys = {k.upper(): v for k, v in data.items()}
print(f"\nUpper keys: {upper_keys}")

# --- Example 11: Invert a dictionary ---
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"\nOriginal: {original}")
print(f"Inverted: {inverted}")

# =============================
# 5. PRACTICAL EXAMPLES
# =============================

# --- Example 12: Character frequency ---
text = "mississippi"
freq = {char: text.count(char) for char in set(text)}
print(f"\nFrequency of '{text}': {freq}")

# --- Example 13: Number classification ---
numbers = range(1, 11)
classification = {n: "even" if n % 2 == 0 else "odd" for n in numbers}
print(f"Classification: {classification}")

# --- Example 14: Comparison — loop vs comprehension ---
# Using a loop:
result_loop = {}
for i in range(5):
    result_loop[i] = i * 10

# Using comprehension (same result, shorter):
result_comp = {i: i * 10 for i in range(5)}

print(f"\nLoop:          {result_loop}")
print(f"Comprehension: {result_comp}")
print(f"Same result: {result_loop == result_comp}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a dict of numbers and their cubes using comprehension
# 2. Filter a dict to keep only values greater than 50
# 3. Create a dict from two lists using zip and comprehension
# ============================================
