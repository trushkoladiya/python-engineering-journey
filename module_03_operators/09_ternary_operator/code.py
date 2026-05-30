# ============================================
# MODULE 3 - SUBTOPIC 9: Ternary (Conditional) Operator
# ============================================

# --- Example 1: Basic ternary ---
age = 21
status = "adult" if age >= 18 else "minor"
print(status)   # adult

# --- Example 2: Opposite case ---
age = 15
status = "adult" if age >= 18 else "minor"
print(status)   # minor

# --- Example 3: With numbers ---
x = -5
result = "positive" if x > 0 else "not positive"
print(result)   # not positive

x = 10
result = "positive" if x > 0 else "not positive"
print(result)   # positive

# --- Example 4: Finding the bigger value ---
a = 30
b = 50
bigger = a if a > b else b
print(bigger)   # 50

# --- Example 5: Finding the smaller value ---
smaller = a if a < b else b
print(smaller)  # 30

# --- Example 6: Using directly in print() ---
score = 85
print("Pass" if score >= 60 else "Fail")   # Pass

score = 40
print("Pass" if score >= 60 else "Fail")   # Fail

# --- Example 7: With boolean values ---
is_raining = True
action = "take umbrella" if is_raining else "enjoy the sun"
print(action)   # take umbrella

# --- Example 8: Even or odd check ---
number = 7
parity = "even" if number % 2 == 0 else "odd"
print(parity)   # odd

number = 12
parity = "even" if number % 2 == 0 else "odd"
print(parity)   # even

# --- Example 9: With string operations ---
name = "Trush"
greeting = "Hello, " + name if name else "Hello, stranger"
print(greeting)   # Hello, Trush

name = ""
greeting = "Hello, " + name if name else "Hello, stranger"
print(greeting)   # Hello, stranger

# --- Example 10: Choosing a calculation ---
price = 150
discount = 0.20 if price > 100 else 0.10
final = price - (price * discount)
print(final)      # 120.0  (20% discount applied)

price = 80
discount = 0.20 if price > 100 else 0.10
final = price - (price * discount)
print(final)      # 72.0  (10% discount applied)

# --- Example 11: Absolute value using ternary ---
x = -15
absolute = x if x >= 0 else -x
print(absolute)   # 15

x = 10
absolute = x if x >= 0 else -x
print(absolute)   # 10

# --- Example 12: Nested ternary (use sparingly!) ---
x = 0
result = "positive" if x > 0 else ("zero" if x == 0 else "negative")
print(result)     # zero

x = -3
result = "positive" if x > 0 else ("zero" if x == 0 else "negative")
print(result)     # negative

x = 7
result = "positive" if x > 0 else ("zero" if x == 0 else "negative")
print(result)     # positive

# ============================================
# TRY IT YOURSELF:
# 1. Check if a number is even or odd using ternary
# 2. Find the maximum of two numbers using ternary
# 3. Print "hot" if temp > 35, otherwise "comfortable"
# ============================================
