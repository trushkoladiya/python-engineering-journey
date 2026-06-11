# ============================================
# MODULE 16 - SUBTOPIC 2: Lambda Functions (Advanced Usage)
# ============================================

# Lambda = small anonymous function in one line.
# We learned basics in Module 8. Now let's go deeper.

# =============================
# 1. LAMBDA RECAP
# =============================

print("=== Lambda Recap ===")
print()

# Regular function
def add(a, b):
    return a + b

# Same thing as a lambda
add_lambda = lambda a, b: a + b

print(f"  add(3, 4) = {add(3, 4)}")
print(f"  add_lambda(3, 4) = {add_lambda(3, 4)}")
print()

# =============================
# 2. SORTING WITH LAMBDA
# =============================

print("=== Sorting with Lambda ===")
print()

students = [
    ("Trush", 85),
    ("Rahul", 92),
    ("Eve", 78),
    ("Charlie", 90),
]

# Sort by name (default)
by_name = sorted(students, key=lambda s: s[0])
print(f"  By name: {by_name}")

# Sort by grade
by_grade = sorted(students, key=lambda s: s[1])
print(f"  By grade (asc): {by_grade}")

# Sort by grade descending
by_grade_desc = sorted(students, key=lambda s: -s[1])
print(f"  By grade (desc): {by_grade_desc}")
print()

# =============================
# 3. MULTI-CRITERIA SORTING
# =============================

print("=== Multi-Criteria Sorting ===")
print()

employees = [
    {"name": "Trush", "dept": "Engineering", "salary": 90000},
    {"name": "Rahul", "dept": "Marketing", "salary": 75000},
    {"name": "Eve", "dept": "Engineering", "salary": 85000},
    {"name": "Charlie", "dept": "Marketing", "salary": 80000},
]

# Sort by department, then by salary descending
sorted_emp = sorted(employees, key=lambda e: (e["dept"], -e["salary"]))
for emp in sorted_emp:
    print(f"  {emp['name']:10} | {emp['dept']:12} | ${emp['salary']:,}")
print()

# =============================
# 4. LAMBDA WITH CONDITIONAL LOGIC
# =============================

print("=== Lambda with Conditionals ===")
print()

# Ternary expression inside lambda
classify = lambda x: "positive" if x > 0 else ("zero" if x == 0 else "negative")

test_values = [5, 0, -3, 10, -1]
for val in test_values:
    print(f"  {val:3} → {classify(val)}")
print()

# Grade classifier
grade = lambda score: "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "F"))

scores = [95, 82, 67, 91, 73]
for s in scores:
    print(f"  Score {s} → Grade {grade(s)}")
print()

# =============================
# 5. LAMBDA IN DATA STRUCTURES
# =============================

print("=== Lambda in Data Structures ===")
print()

# Dictionary of operations
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "power": lambda a, b: a ** b,
}

a, b = 10, 3
for name, func in operations.items():
    print(f"  {name}({a}, {b}) = {func(a, b)}")
print()

# =============================
# 6. LAMBDA AS SORT KEY FOR COMPLEX DATA
# =============================

print("=== Complex Sorting Examples ===")
print()

# Sort strings by length
words = ["python", "is", "a", "powerful", "language"]
by_length = sorted(words, key=lambda w: len(w))
print(f"  By length: {by_length}")

# Sort strings by last character
by_last = sorted(words, key=lambda w: w[-1])
print(f"  By last char: {by_last}")

# Sort by number of vowels
count_vowels = lambda s: sum(1 for c in s if c in "aeiou")
by_vowels = sorted(words, key=count_vowels)
print(f"  By vowel count: {by_vowels}")
print()

# =============================
# 7. LAMBDA WITH max() AND min()
# =============================

print("=== Lambda with max() and min() ===")
print()

products = [
    {"name": "Laptop", "price": 999, "rating": 4.5},
    {"name": "Phone", "price": 699, "rating": 4.8},
    {"name": "Tablet", "price": 449, "rating": 4.2},
    {"name": "Watch", "price": 299, "rating": 4.6},
]

cheapest = min(products, key=lambda p: p["price"])
print(f"  Cheapest: {cheapest['name']} (${cheapest['price']})")

best_rated = max(products, key=lambda p: p["rating"])
print(f"  Best rated: {best_rated['name']} ({best_rated['rating']}★)")

# Best value = highest rating/price ratio
best_value = max(products, key=lambda p: p["rating"] / p["price"])
print(f"  Best value: {best_value['name']}")
print()

# =============================
# 8. LAMBDA vs DEF — READABILITY
# =============================

print("=== Lambda vs def — When to Choose ===")
print()

# Good lambda use — simple, clear
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums = sorted(numbers, key=lambda x: -x)
print(f"  Sorted descending: {sorted_nums}")

# Bad lambda use — too complex, use def instead
# BAD: lambda x: x[1] if len(x) > 1 and x[0].isalpha() else x[0]
# GOOD: write a regular function with a descriptive name

def extract_sort_key(item):
    """Extract the appropriate sort key from item."""
    if len(item) > 1 and item[0].isalpha():
        return item[1]
    return item[0]

print(f"  (Use def when logic gets complex)")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Sort a list of tuples (name, age) by age descending
# 2. Create a dictionary with 4 math lambdas
#    and use them in a loop
# 3. Use lambda with max() to find the longest word
#    in a list
# ============================================
