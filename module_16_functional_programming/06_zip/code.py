# ============================================
# MODULE 16 - SUBTOPIC 6: zip()
# ============================================

# zip() combines multiple iterables element by element.
# It returns a lazy iterator of tuples.

# =============================
# 1. BASIC zip()
# =============================

print("=== Basic zip() ===")
print()

names = ["Trush", "Rahul", "Eve", "Charlie"]
ages = [25, 30, 22, 28]

paired = list(zip(names, ages))
print(f"  names: {names}")
print(f"  ages:  {ages}")
print(f"  zipped: {paired}")
print()

# =============================
# 2. ITERATING IN PARALLEL
# =============================

print("=== Iterating in Parallel ===")
print()

students = ["Trush", "Rahul", "Eve"]
grades = ["A", "B+", "A-"]
scores = [95, 87, 91]

for student, grade, score in zip(students, grades, scores):
    print(f"  {student}: Grade {grade} (Score: {score})")
print()

# =============================
# 3. UNEQUAL LENGTHS
# =============================

print("=== Unequal Lengths ===")
print()

a = [1, 2, 3, 4, 5]
b = [10, 20, 30]

# zip stops at the SHORTEST iterable
result = list(zip(a, b))
print(f"  a: {a}")
print(f"  b: {b}")
print(f"  zip(a, b): {result}")
print("  (elements 4, 5 from 'a' are dropped)")
print()

# =============================
# 4. zip() WITH THREE+ ITERABLES
# =============================

print("=== Multiple Iterables ===")
print()

first_names = ["Trush", "Rahul", "Eve"]
last_names = ["Smith", "Jones", "Wilson"]
departments = ["Engineering", "Marketing", "Design"]

for first, last, dept in zip(first_names, last_names, departments):
    print(f"  {first} {last} — {dept}")
print()

# =============================
# 5. BUILDING DICTIONARIES WITH zip()
# =============================

print("=== Building Dictionaries ===")
print()

keys = ["name", "age", "city", "role"]
values = ["Trush", 21, "NYC", "Engineer"]

person = dict(zip(keys, values))
print(f"  keys:   {keys}")
print(f"  values: {values}")
print(f"  dict:   {person}")
print()

# Multiple records
names = ["Trush", "Rahul", "Eve"]
scores = [95, 87, 91]
grade_book = dict(zip(names, scores))
print(f"  Grade book: {grade_book}")
print()

# =============================
# 6. UNZIPPING WITH zip(*)
# =============================

print("=== Unzipping with zip(*) ===")
print()

pairs = [("Trush", 21), ("Rahul", 22), ("Eve", 22)]
print(f"  pairs: {pairs}")

names, ages = zip(*pairs)
print(f"  names: {names}")
print(f"  ages:  {ages}")
print()

# With three elements
records = [("Trush", "A", 95), ("Rahul", "B+", 87), ("Eve", "A-", 91)]
names, grades, scores = zip(*records)
print(f"  records: {records}")
print(f"  names:   {names}")
print(f"  grades:  {grades}")
print(f"  scores:  {scores}")
print()

# =============================
# 7. zip() WITH map() AND filter()
# =============================

print("=== zip() with map() and filter() ===")
print()

# Combine zip with other functional tools
prices = [10.0, 25.0, 5.0, 30.0]
quantities = [3, 1, 10, 2]

# Calculate totals using map + zip
totals = list(map(lambda pq: pq[0] * pq[1], zip(prices, quantities)))
print(f"  prices:     {prices}")
print(f"  quantities: {quantities}")
print(f"  totals:     {totals}")
print()

# Cleaner with unpacking
totals2 = list(map(lambda pq: pq[0] * pq[1], zip(prices, quantities)))

# Even cleaner with starred lambda
import itertools
totals3 = [p * q for p, q in zip(prices, quantities)]
print(f"  totals (comprehension): {totals3}")
print()

# =============================
# 8. TRANSPOSING A MATRIX
# =============================

print("=== Transposing a Matrix ===")
print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("  Original matrix:")
for row in matrix:
    print(f"    {row}")

transposed = list(zip(*matrix))
print("\n  Transposed:")
for row in transposed:
    print(f"    {list(row)}")
print()

# =============================
# 9. PRACTICAL: COMPARING LISTS
# =============================

print("=== Practical: Comparing Lists ===")
print()

expected = [10, 20, 30, 40, 50]
actual = [10, 22, 30, 38, 50]

print("  Checking results:")
for i, (exp, act) in enumerate(zip(expected, actual)):
    status = "✓" if exp == act else "✗"
    print(f"    Item {i}: expected={exp}, actual={act} {status}")
print()

# Count matches
matches = sum(1 for e, a in zip(expected, actual) if e == a)
print(f"  Matches: {matches}/{len(expected)}")
print()

# =============================
# 10. zip() WITH enumerate()
# =============================

print("=== zip() with enumerate() ===")
print()

names = ["Trush", "Rahul", "Eve"]
scores = [95, 87, 91]

for i, (name, score) in enumerate(zip(names, scores), 1):
    print(f"  {i}. {name}: {score}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use zip() to pair a list of products with prices,
#    then build a dictionary
# 2. Use zip() to add corresponding elements of two lists
# 3. Transpose a 4×3 matrix using zip(*)
# ============================================
