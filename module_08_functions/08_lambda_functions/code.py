# ============================================
# MODULE 8 - SUBTOPIC 8: Lambda Functions
# ============================================

# =============================
# 1. BASIC LAMBDA SYNTAX
# =============================

# --- Example 1: Simple lambda ---
double = lambda x: x * 2
print("double(5) =", double(5))     # 10
print("double(12) =", double(12))   # 24

# --- Example 2: Lambda vs regular function ---
# Regular function
def square_func(x):
    return x * x

# Lambda equivalent
square_lambda = lambda x: x * x

print(f"\nRegular: {square_func(5)}")
print(f"Lambda:  {square_lambda(5)}")

# --- Example 3: Multiple parameters ---
add = lambda a, b: a + b
multiply = lambda a, b: a * b

print(f"\nadd(3, 4) = {add(3, 4)}")
print(f"multiply(3, 4) = {multiply(3, 4)}")

# =============================
# 2. LAMBDA WITH EXPRESSIONS
# =============================

# --- Example 4: Conditional expression in lambda ---
is_even = lambda n: n % 2 == 0
print(f"\nis_even(4) = {is_even(4)}")   # True
print(f"is_even(7) = {is_even(7)}")     # False

# --- Example 5: Ternary in lambda ---
classify = lambda n: "even" if n % 2 == 0 else "odd"
print(f"\n8 is {classify(8)}")
print(f"7 is {classify(7)}")

# --- Example 6: String operations ---
shout = lambda text: text.upper() + "!!!"
whisper = lambda text: text.lower() + "..."

print(f"\n{shout('hello')}")
print(f"{whisper('HELLO')}")

# =============================
# 3. LAMBDA WITH sort() AND sorted()
# =============================

# --- Example 7: Sort by string length ---
words = ["banana", "apple", "fig", "cherry", "date"]
words.sort(key=lambda w: len(w))
print(f"\nSorted by length: {words}")

# --- Example 8: Sort tuples by second element ---
students = [("Trush", 85), ("Rahul", 92), ("Charlie", 78), ("Diana", 95)]
students.sort(key=lambda s: s[1])
print(f"\nSorted by score (ascending): {students}")

students.sort(key=lambda s: s[1], reverse=True)
print(f"Sorted by score (descending): {students}")

# --- Example 9: Sort dicts by value ---
people = [
    {"name": "Trush", "age": 21},
    {"name": "Rahul", "age": 25},
    {"name": "Charlie", "age": 35},
]
sorted_people = sorted(people, key=lambda p: p["age"])
print(f"\nSorted by age:")
for p in sorted_people:
    print(f"  {p['name']}: {p['age']}")

# =============================
# 4. LAMBDA WITH map() AND filter()
# =============================

# --- Example 10: map() with lambda ---
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"\nOriginal: {numbers}")
print(f"Squared:  {squared}")

# --- Example 11: filter() with lambda ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nAll:  {numbers}")
print(f"Even: {evens}")

# --- Example 12: Chaining map and filter ---
numbers = range(1, 11)
# Get squares of even numbers
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(f"\nSquares of evens (1-10): {result}")

# =============================
# 5. LAMBDA IN DATA STRUCTURES
# =============================

# --- Example 13: Dictionary of lambdas ---
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else "Error",
}

print("\nCalculator:")
for name, func in operations.items():
    print(f"  {name}(10, 3) = {func(10, 3)}")

# --- Example 14: List of lambdas ---
transformations = [
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x + 100,
]

value = 5
print(f"\nTransformations of {value}:")
for t in transformations:
    print(f"  → {t(value)}")

# =============================
# 6. WHEN NOT TO USE LAMBDA
# =============================

# --- Example 15: Too complex — use def instead ---
# ❌ Hard to read lambda
# complex_lambda = lambda x: x ** 2 if x > 0 else -x ** 2 if x < 0 else 0

# ✅ Clear def function
def transform(x):
    if x > 0:
        return x ** 2
    elif x < 0:
        return -(x ** 2)
    return 0

print(f"\ntransform(3) = {transform(3)}")
print(f"transform(-3) = {transform(-3)}")
print(f"transform(0) = {transform(0)}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a lambda that returns the cube of a number
# 2. Sort a list of tuples by the last element using lambda
# 3. Use filter() with a lambda to keep only positive numbers
# ============================================
