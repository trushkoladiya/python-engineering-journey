# ============================================
# MODULE 3 - SUBTOPIC 10: Operator Precedence & Associativity (Deep)
# ============================================

# --- Example 1: Basic precedence — * before + ---
print(2 + 3 * 4)         # 14  (3*4=12, then 2+12)
print((2 + 3) * 4)       # 20  (parentheses first)

# --- Example 2: ** before * ---
print(2 * 3 ** 2)        # 18  (3**2=9, then 2*9)
print((2 * 3) ** 2)      # 36  (parentheses first: 6**2)

# --- Example 3: Unary minus vs exponentiation ---
print(-2 ** 2)            # -4  (** first: 2**2=4, then -4)
print((-2) ** 2)          # 4   (parentheses: (-2)**2 = 4)

# --- Example 4: Division and modulus — same level, left to right ---
print(20 / 4 * 2)         # 10.0  (left to right: 5.0 * 2)
print(20 / (4 * 2))       # 2.5   (parentheses: 20 / 8)

print(17 % 5 * 3)         # 6  (17%5=2, then 2*3=6)
print(17 % (5 * 3))       # 2  (5*3=15, then 17%15=2)

# --- Example 5: Exponentiation is RIGHT to LEFT ---
print(2 ** 3 ** 2)        # 512  → 2 ** (3**2) = 2 ** 9 = 512
print((2 ** 3) ** 2)      # 64   → 8 ** 2 = 64
# This is the ONLY common operator that goes right to left!

# --- Example 6: Comparison operators precedence ---
# Arithmetic happens BEFORE comparisons
print(5 + 3 > 7)          # True  (8 > 7)
print(10 - 5 == 5)        # True  (5 == 5)
print(2 * 3 >= 6)         # True  (6 >= 6)

# --- Example 7: Logical operator precedence: not > and > or ---
print(True or True and False)     # True
# Step: and first → True and False = False
# Then: True or False = True

print((True or True) and False)   # False
# Parentheses first: True or True = True
# Then: True and False = False

# --- Example 8: not has highest logical precedence ---
print(not True and False)         # False
# Step: not True = False
# Then: False and False = False

print(not (True and False))       # True
# Step: True and False = False
# Then: not False = True

# --- Example 9: Complex mixed expression ---
x = 10
y = 5
z = 3

result = x + y * z ** 2 - x // z
# Step 1: z ** 2 = 9       (exponent first)
# Step 2: y * 9 = 45       (multiplication)
# Step 3: x // z = 3       (floor division)
# Step 4: 10 + 45 - 3 = 52 (left to right)
print(result)               # 52

# --- Example 10: Comparison + logical combined ---
age = 21
income = 50000

# Comparisons first, then logical
eligible = age >= 18 and age <= 65 and income >= 30000
print(eligible)   # True

# Same with parentheses for clarity (recommended!)
eligible = (age >= 18) and (age <= 65) and (income >= 30000)
print(eligible)   # True

# --- Example 11: Bitwise precedence ---
# & before | before ^ ... but parentheses are always clearer
print(5 | 3 & 6)          # 7
# Step: 3 & 6 = 2 (AND first — higher precedence)
# Then: 5 | 2 = 7

print((5 | 3) & 6)        # 6
# Parentheses: 5 | 3 = 7
# Then: 7 & 6 = 6

# --- Example 12: The golden rule — use parentheses! ---
# Without parentheses (confusing)
result = 2 + 3 * 4 - 1 ** 2 + 10 // 3
print(result)   # 17
# 1**2=1, 3*4=12, 10//3=3, then: 2+12-1+3=16... wait
# Let's be explicit:

# With parentheses (crystal clear!)
result = 2 + (3 * 4) - (1 ** 2) + (10 // 3)
print(result)   # 16

# ALWAYS use parentheses when mixing 3+ operators
# Your future self will thank you!

# ============================================
# TRY IT YOURSELF:
# 1. What is: 2 ** 2 ** 3? (hint: right to left!)
# 2. What is: True or False and False?
# 3. Rewrite 5 + 3 * 2 - 1 with parentheses to show order
# ============================================
