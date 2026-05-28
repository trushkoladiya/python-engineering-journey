# ============================================
# MODULE 3 - SUBTOPIC 3: Assignment Operators
# ============================================

# --- Example 1: Basic assignment ---
x = 10
name = "Python"
pi = 3.14
print(x, name, pi)   # 10 Python 3.14

# --- Example 2: Multiple assignment ---
a, b, c = 1, 2, 3
print(a)   # 1
print(b)   # 2
print(c)   # 3

# --- Example 3: Same value to multiple variables ---
x = y = z = 0
print(x, y, z)   # 0 0 0

# --- Example 4: Swapping with multiple assignment ---
a = 5
b = 10
a, b = b, a      # swap!
print(a)   # 10
print(b)   # 5

# --- Example 5: Add and assign (+=) ---
score = 100
print(score)       # 100
score += 25        # same as: score = score + 25
print(score)       # 125

# --- Example 6: Subtract and assign (-=) ---
health = 100
health -= 30       # same as: health = health - 30
print(health)      # 70

# --- Example 7: Multiply and assign (*=) ---
price = 10
price *= 3         # same as: price = price * 3
print(price)       # 30

# --- Example 8: Divide and assign (/=) ---
total = 100
total /= 4         # same as: total = total / 4
print(total)       # 25.0 (always float with /)
print(type(total)) # <class 'float'>

# --- Example 9: Floor divide and assign (//=) ---
items = 17
items //= 5        # same as: items = items // 5
print(items)       # 3

# --- Example 10: Modulus and assign (%=) ---
number = 17
number %= 5        # same as: number = number % 5
print(number)      # 2 (remainder of 17 ÷ 5)

# --- Example 11: Exponent and assign (**=) ---
base = 2
base **= 10        # same as: base = base ** 10
print(base)        # 1024

# --- Example 12: String concatenation with += ---
greeting = "Hello"
greeting += " World"
print(greeting)     # Hello World

# --- Example 13: Repetition with *= ---
line = "-"
line *= 20
print(line)         # --------------------

# ============================================
# TRY IT YOURSELF:
# 1. Start with x = 50, add 10, subtract 5, multiply by 2
# 2. Swap two variables using multiple assignment
# 3. Build a string step by step using +=
# ============================================
