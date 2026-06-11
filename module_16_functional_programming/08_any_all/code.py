# ============================================
# MODULE 16 - SUBTOPIC 8: any() and all()
# ============================================

# any() — True if AT LEAST ONE element is truthy
# all() — True if ALL elements are truthy

# =============================
# 1. BASIC any() AND all()
# =============================

print("=== Basic any() and all() ===")
print()

all_true = [True, True, True]
some_true = [True, False, True]
all_false = [False, False, False]

print(f"  all_true:  any={any(all_true)}, all={all(all_true)}")
print(f"  some_true: any={any(some_true)}, all={all(some_true)}")
print(f"  all_false: any={any(all_false)}, all={all(all_false)}")
print()

# =============================
# 2. WITH NUMBERS (TRUTHY/FALSY)
# =============================

print("=== With Numbers ===")
print()

# 0 is falsy, everything else is truthy
nums1 = [1, 2, 3, 4]
nums2 = [0, 0, 0, 1]
nums3 = [0, 0, 0, 0]

print(f"  {nums1}: any={any(nums1)}, all={all(nums1)}")
print(f"  {nums2}: any={any(nums2)}, all={all(nums2)}")
print(f"  {nums3}: any={any(nums3)}, all={all(nums3)}")
print()

# =============================
# 3. EMPTY ITERABLES
# =============================

print("=== Empty Iterables ===")
print()

empty = []
print(f"  any([]) = {any(empty)}")   # False — no truthy element exists
print(f"  all([]) = {all(empty)}")   # True  — no falsy element exists
print("  (all([]) is True — this is called 'vacuous truth')")
print()

# =============================
# 4. WITH CONDITIONS (GENERATOR EXPRESSIONS)
# =============================

print("=== Conditions with Generator Expressions ===")
print()

ages = [18, 25, 16, 30, 22]
print(f"  ages: {ages}")

# Are ALL adults (>= 18)?
all_adults = all(age >= 18 for age in ages)
print(f"  All adults? {all_adults}")

# Is ANY minor (< 18)?
has_minor = any(age < 18 for age in ages)
print(f"  Any minors? {has_minor}")

# Are ALL minors?
all_minors = all(age < 18 for age in ages)
print(f"  All minors? {all_minors}")
print()

# =============================
# 5. WITH STRINGS
# =============================

print("=== With Strings ===")
print()

words = ["hello", "world", "python"]

# Do all words start with a lowercase letter?
all_lower = all(w[0].islower() for w in words)
print(f"  words: {words}")
print(f"  All start lowercase? {all_lower}")

# Does any word contain 'th'?
has_th = any("th" in w for w in words)
print(f"  Any contain 'th'? {has_th}")
print()

# Check string properties
password = "MyP@ss123"
print(f"  Password: '{password}'")
print(f"  Has uppercase? {any(c.isupper() for c in password)}")
print(f"  Has lowercase? {any(c.islower() for c in password)}")
print(f"  Has digit?     {any(c.isdigit() for c in password)}")
print(f"  Has special?   {any(not c.isalnum() for c in password)}")
print()

# =============================
# 6. PASSWORD VALIDATOR
# =============================

print("=== Practical: Password Validator ===")
print()

def is_strong_password(pwd):
    """Check if password meets all strength criteria."""
    checks = {
        "Length >= 8": len(pwd) >= 8,
        "Has uppercase": any(c.isupper() for c in pwd),
        "Has lowercase": any(c.islower() for c in pwd),
        "Has digit": any(c.isdigit() for c in pwd),
        "Has special char": any(not c.isalnum() for c in pwd),
    }
    return checks

passwords = ["hello", "Hello123", "H3llo!World", "12345678"]

for pwd in passwords:
    checks = is_strong_password(pwd)
    is_strong = all(checks.values())
    print(f"  '{pwd}':")
    for check, passed in checks.items():
        status = "✓" if passed else "✗"
        print(f"    {status} {check}")
    print(f"    → {'STRONG' if is_strong else 'WEAK'}")
    print()

# =============================
# 7. WITH LISTS AND DICTS
# =============================

print("=== With Complex Data ===")
print()

students = [
    {"name": "Trush", "passed": True},
    {"name": "Rahul", "passed": True},
    {"name": "Eve", "passed": False},
]

all_passed = all(s["passed"] for s in students)
any_failed = any(not s["passed"] for s in students)

print(f"  All passed? {all_passed}")
print(f"  Any failed? {any_failed}")
print()

# =============================
# 8. SHORT-CIRCUIT BEHAVIOR
# =============================

print("=== Short-Circuit Behavior ===")
print()

# any() stops at the first True
def check_and_print(value):
    print(f"    Checking {value}...")
    return value > 3

numbers = [1, 2, 5, 8, 10]  # stops at 5 (first True)
print("  any() — stops at first True:")
result = any(check_and_print(n) for n in numbers)
print(f"  Result: {result}")
print()

# all() stops at the first False
print("  all() — stops at first False:")
result = all(check_and_print(n) for n in numbers)
print(f"  Result: {result}")
print()

# =============================
# 9. COMBINING any() AND all()
# =============================

print("=== Combining any() and all() ===")
print()

# Matrix: check if any row has all positive numbers
matrix = [
    [1, -2, 3],
    [4, 5, 6],
    [-1, 2, -3],
]

print("  Matrix:")
for row in matrix:
    all_pos = all(x > 0 for x in row)
    print(f"    {row} — all positive? {all_pos}")

has_all_positive_row = any(all(x > 0 for x in row) for row in matrix)
print(f"  Any row all positive? {has_all_positive_row}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a function that checks if all numbers
#    in a list are even
# 2. Check if any string in a list is a palindrome
# 3. Validate that all items in a shopping cart
#    have a price > 0
# ============================================
