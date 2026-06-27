# ============================================
# MODULE 8 - SUBTOPIC 4: Return Values
# ============================================

# =============================
# 1. BASIC RETURN
# =============================

# --- Example 1: Returning a value ---
def add(a, b):
    return a + b

result = add(3, 5)
print("3 + 5 =", result)   # 8

# --- Example 2: Using return value directly ---
print("10 + 20 =", add(10, 20))

# --- Example 3: Return value in expressions ---
total = add(5, 3) + add(10, 7)
print("(5+3) + (10+7) =", total)   # 25

# =============================
# 2. RETURNING SINGLE VALUES
# =============================

# --- Example 4: Square function ---
def square(n):
    return n * n

print("\nSquares:")
print(f"  5² = {square(5)}")
print(f"  8² = {square(8)}")
print(f"  12² = {square(12)}")

# --- Example 5: Check even/odd ---
def is_even(n):
    return n % 2 == 0

print(f"\nIs 4 even? {is_even(4)}")     # True
print(f"Is 7 even? {is_even(7)}")       # False

# --- Example 6: Get absolute value ---
def absolute(n):
    if n < 0:
        return -n
    return n

print(f"\nabs(-5) = {absolute(-5)}")
print(f"abs(3) = {absolute(3)}")

# =============================
# 3. RETURN STOPS THE FUNCTION
# =============================

# --- Example 7: Code after return doesn't run ---
def check_age(age):
    if age < 0:
        return "Invalid age"
    if age >= 18:
        return "Adult"
    return "Minor"

print(f"\nAge 25: {check_age(25)}")
print(f"Age 10: {check_age(10)}")
print(f"Age -5: {check_age(-5)}")

# --- Example 8: Early return pattern ---
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

print(f"\n10 / 3 = {divide(10, 3)}")
print(f"10 / 0 = {divide(10, 0)}")

# =============================
# 4. RETURNING MULTIPLE VALUES
# =============================

# --- Example 9: Return two values (as tuple) ---
def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([5, 2, 8, 1, 9])
print(f"\nLowest: {lowest}, Highest: {highest}")

# --- Example 10: Return three values ---
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = stats([10, 20, 30, 40, 50])
print(f"\nMin: {low}, Max: {high}, Average: {avg}")

# --- Example 11: Return as tuple ---
def get_name_parts(full_name):
    parts = full_name.split()
    return parts[0], parts[-1]

first, last = get_name_parts("Trush Koladiya")
print(f"\nFirst: {first}, Last: {last}")

# =============================
# 5. NO RETURN — RETURNS None
# =============================

# --- Example 12: Function without return ---
def greet(name):
    print(f"Hello, {name}!")

result = greet("\nTrush")
print(f"Return value: {result}")   # None
print(f"Type: {type(result)}")     # <class 'NoneType'>

# --- Example 13: Explicit return None ---
def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None   # Explicitly return None if not found

found = find_item(["apple", "banana", "cherry"], "banana")
print(f"\nFound: {found}")

not_found = find_item(["apple", "banana", "cherry"], "mango")
print(f"Found: {not_found}")

# =============================
# 6. RETURN vs PRINT
# =============================

# --- Example 14: Print — just displays ---
def add_and_print(a, b):
    print(a + b)

# --- Example 15: Return — gives the value back ---
def add_and_return(a, b):
    return a + b

print("\nPrint version:")
x = add_and_print(3, 5)        # Prints 8
print(f"x = {x}")               # x = None (can't use the value!)

print("\nReturn version:")
y = add_and_return(3, 5)       # Nothing printed
print(f"y = {y}")               # y = 8 (value is usable!)
print(f"y * 2 = {y * 2}")       # 16 — can do math with it

# =============================
# 7. PRACTICAL EXAMPLES
# =============================

# --- Example 16: Grade calculator ---
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"

scores = [95, 82, 67, 55, 78]
print("\nGrades:")
for score in scores:
    grade = get_grade(score)
    print(f"  {score} → {grade}")

# --- Example 17: List processor ---
def process_scores(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count
    passed = sum(1 for s in scores if s >= 60)
    return total, average, passed

t, a, p = process_scores([85, 42, 91, 73, 55, 88])
print(f"\nTotal: {t}, Average: {a:.1f}, Passed: {p}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a function that returns the larger of two numbers
# 2. Create a function that returns both the sum and product
# 3. Compare the difference between return and print
# ============================================
