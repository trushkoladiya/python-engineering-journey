# ============================================
# MODULE 3 - SUBTOPIC 8: Expressions & Evaluation
# ============================================

# --- Example 1: Simple expressions ---
# Every expression produces a value
print(5 + 3)           # 8
print(10 > 5)          # True
print("Hi" + " there") # Hi there

# --- Example 2: Storing expression results ---
result = 5 + 3 * 2     # expression evaluates to 11
print(result)           # 11

total = (100 - 20) / 4  # expression evaluates to 20.0
print(total)             # 20.0

# --- Example 3: Combining arithmetic operators ---
print(10 + 5 * 2)       # 20 — multiplication first
print(10 - 3 + 2)       # 9  — left to right
print(2 ** 3 + 1)       # 9  — exponent first (8 + 1)

# --- Example 4: Parentheses control order ---
print(10 + 5 * 2)       # 20 — without parentheses
print((10 + 5) * 2)     # 30 — parentheses first

print(2 + 3 ** 2)       # 11 — exponent first (2 + 9)
print((2 + 3) ** 2)     # 25 — parentheses first (5 ** 2)

# --- Example 5: Nested parentheses ---
result = ((10 + 5) * 2) - (3 ** 2)
# Step 1: (10 + 5) = 15
# Step 2: 15 * 2 = 30
# Step 3: 3 ** 2 = 9
# Step 4: 30 - 9 = 21
print(result)            # 21

# --- Example 6: Multiple operators in one expression ---
x = 10
y = 3
z = 2
result = x + y * z - x // z
# Step 1: y * z = 6
# Step 2: x // z = 5
# Step 3: 10 + 6 - 5 = 11
print(result)            # 11

# --- Example 7: Boolean expressions ---
a = 10
b = 20
print(a < b)             # True — comparison expression
print(a == b)            # False
print(a < b and b < 30)  # True — logical expression

# --- Example 8: Mixing comparison and arithmetic ---
age = 21
is_young_adult = age >= 18 and age <= 30
print(is_young_adult)    # True

score = 85
passed = score >= 60
print(passed)            # True

# --- Example 9: Type mixing in expressions ---
print(5 + 3.0)           # 8.0  — int promoted to float
print(True + True)       # 2    — True = 1
print(False + 10)        # 10   — False = 0
print(True * 5)          # 5

# --- Example 10: Complex real-world expression ---
# Calculate final price: base price + tax - discount
base_price = 100
tax_rate = 0.18
discount = 15

final_price = base_price + (base_price * tax_rate) - discount
# Step 1: base_price * tax_rate = 18.0
# Step 2: 100 + 18.0 = 118.0
# Step 3: 118.0 - 15 = 103.0
print(final_price)       # 103.0

# --- Example 11: String expressions ---
first = "Hello"
last = "World"
full = first + " " + last
print(full)              # Hello World

line = "=" * 30
print(line)              # ==============================

# --- Example 12: Left-to-right evaluation (same precedence) ---
print(100 / 5 / 4)       # 5.0  (left to right: 20 / 4)
print(100 / (5 / 4))     # 80.0 (parentheses: 100 / 1.25)

print(2 ** 2 ** 3)       # 256  — EXCEPTION: ** is right-to-left!
# 2 ** (2 ** 3) = 2 ** 8 = 256 — NOT (2**2)**3 = 64
print((2 ** 2) ** 3)     # 64   — parentheses override

# ============================================
# TRY IT YOURSELF:
# 1. Calculate: (50 + 30) * 2 - 10 ** 2
# 2. What is 2 ** 3 ** 2? (hint: right-to-left!)
# 3. Calculate a restaurant bill: meal + (meal * tip%) - coupon
# ============================================
