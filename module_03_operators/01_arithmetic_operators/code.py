# ============================================
# MODULE 3 - SUBTOPIC 1: Arithmetic Operators
# ============================================

# --- Example 1: Addition ---
a = 15
b = 7
result = a + b
print(result)         # 22

# --- Example 2: Subtraction ---
result = a - b
print(result)         # 8

# --- Example 3: Multiplication ---
result = a * b
print(result)         # 105

# --- Example 4: Division (always returns float) ---
result = a / b
print(result)         # 2.142857142857143
print(type(result))   # <class 'float'>

# Even when it divides evenly, / gives a float
print(10 / 2)         # 5.0 — not 5!
print(type(10 / 2))   # <class 'float'>

# --- Example 5: Floor Division (rounds down) ---
print(15 // 4)        # 3  (3.75 rounded down)
print(17 // 5)        # 3  (3.4 rounded down)
print(-7 // 2)        # -4 (rounds toward negative infinity!)
print(type(15 // 4))  # <class 'int'>

# --- Example 6: Modulus (remainder) ---
print(10 % 3)         # 1  (10 ÷ 3 = 3 remainder 1)
print(20 % 5)         # 0  (divides evenly)
print(7 % 2)          # 1  (odd number check: remainder is 1)
print(8 % 2)          # 0  (even number check: remainder is 0)

# --- Example 7: Exponentiation ---
print(2 ** 3)         # 8   (2 × 2 × 2)
print(5 ** 2)         # 25  (5 × 5)
print(10 ** 0)        # 1   (any number to power 0 = 1)
print(9 ** 0.5)       # 3.0 (square root!)
print(27 ** (1/3))    # 3.0 (cube root!)

# --- Example 8: Operator Precedence ---
# Python follows standard math: ** > *, /, //, % > +, -
print(2 + 3 * 4)      # 14  (multiplication first: 3*4=12, then 2+12=14)
print(10 - 2 ** 3)     # 2   (exponent first: 2**3=8, then 10-8=2)

# --- Example 9: Using parentheses to control order ---
print((2 + 3) * 4)    # 20  (parentheses first)
print((10 - 2) ** 3)  # 512 (parentheses first)
print((5 + 5) / (3 - 1))  # 5.0

# --- Example 10: Mixed type results ---
# int + int = int
print(type(5 + 3))    # <class 'int'>

# int + float = float (type promotion)
print(type(5 + 3.0))  # <class 'float'>
print(5 + 3.0)        # 8.0

# int * float = float
print(2 * 3.5)        # 7.0

# ============================================
# TRY IT YOURSELF:
# 1. Calculate the area of a rectangle (length * width)
# 2. Check if 123 is divisible by 3 using %
# 3. Calculate 2 to the power of 10
# ============================================
