# ============================================
# MODULE 16 - SUBTOPIC 3: map()
# ============================================

# map() applies a function to EVERY item in an iterable.
# It returns a lazy iterator (map object).

# =============================
# 1. BASIC map()
# =============================

print("=== Basic map() ===")
print()

numbers = [1, 2, 3, 4, 5]

# Using a named function
def square(x):
    return x ** 2

squared = list(map(square, numbers))
print(f"  numbers:  {numbers}")
print(f"  squared:  {squared}")
print()

# Using a lambda
doubled = list(map(lambda x: x * 2, numbers))
print(f"  doubled:  {doubled}")
print()

# =============================
# 2. map() RETURNS A LAZY ITERATOR
# =============================

print("=== map() is Lazy ===")
print()

result = map(lambda x: x ** 2, [1, 2, 3, 4])
print(f"  map object: {result}")
print(f"  Type: {type(result)}")

# Consume one at a time with next()
print(f"  next(): {next(result)}")
print(f"  next(): {next(result)}")

# Or convert all at once
print(f"  remaining: {list(result)}")
print()

# =============================
# 3. map() WITH STRINGS
# =============================

print("=== map() with Strings ===")
print()

words = ["hello", "world", "python"]

# Uppercase all words
upper_words = list(map(str.upper, words))
print(f"  Original:  {words}")
print(f"  Uppercase: {upper_words}")

# Get lengths
lengths = list(map(len, words))
print(f"  Lengths:   {lengths}")
print()

# =============================
# 4. map() WITH NAMED FUNCTIONS
# =============================

print("=== map() with Named Functions ===")
print()

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return round((f - 32) * 5 / 9, 1)

temps_f = [32, 50, 68, 86, 100, 212]
temps_c = list(map(fahrenheit_to_celsius, temps_f))

print(f"  Fahrenheit: {temps_f}")
print(f"  Celsius:    {temps_c}")
print()

# =============================
# 5. map() WITH MULTIPLE ITERABLES
# =============================

print("=== map() with Multiple Iterables ===")
print()

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

# Add corresponding elements
sums = list(map(lambda x, y: x + y, a, b))
print(f"  a:    {a}")
print(f"  b:    {b}")
print(f"  sums: {sums}")
print()

# Multiply corresponding elements
products = list(map(lambda x, y: x * y, a, b))
print(f"  products: {products}")
print()

# Three iterables
c = [100, 200, 300, 400]
combined = list(map(lambda x, y, z: x + y + z, a, b, c))
print(f"  a + b + c: {combined}")
print()

# =============================
# 6. map() FOR DATA TRANSFORMATION
# =============================

print("=== Data Transformation ===")
print()

# Convert string numbers to integers
string_numbers = ["10", "20", "30", "40"]
int_numbers = list(map(int, string_numbers))
print(f"  Strings:  {string_numbers}")
print(f"  Integers: {int_numbers}")
print()

# Format data
prices = [9.99, 24.50, 3.75, 149.00]
formatted = list(map(lambda p: f"${p:.2f}", prices))
print(f"  Prices:    {prices}")
print(f"  Formatted: {formatted}")
print()

# =============================
# 7. map() WITH DICTIONARIES
# =============================

print("=== map() with Dictionaries ===")
print()

students = [
    {"name": "Trush", "score": 85},
    {"name": "Rahul", "score": 92},
    {"name": "Eve", "score": 78},
]

# Extract just names
names = list(map(lambda s: s["name"], students))
print(f"  Names: {names}")

# Extract scores
scores = list(map(lambda s: s["score"], students))
print(f"  Scores: {scores}")

# Add grade to each student
def add_grade(student):
    score = student["score"]
    grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
    return {**student, "grade": grade}

graded = list(map(add_grade, students))
for s in graded:
    print(f"  {s['name']}: {s['score']} → {s['grade']}")
print()

# =============================
# 8. map() vs LIST COMPREHENSION
# =============================

print("=== map() vs List Comprehension ===")
print()

numbers = [1, 2, 3, 4, 5]

# Both do the same thing
result_map = list(map(lambda x: x ** 2, numbers))
result_comp = [x ** 2 for x in numbers]

print(f"  map():          {result_map}")
print(f"  comprehension:  {result_comp}")
print(f"  Same? {result_map == result_comp}")
print()

# map() is cleaner with existing functions
words = ["hello", "world"]
print(f"  map(str.upper): {list(map(str.upper, words))}")
print(f"  comprehension:  {[w.upper() for w in words]}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use map() to convert a list of celsius to fahrenheit
# 2. Use map() with two lists to calculate (a² + b²)
# 3. Use map() to extract a specific key from a list of dicts
# ============================================
