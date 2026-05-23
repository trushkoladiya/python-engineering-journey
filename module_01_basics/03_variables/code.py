# ============================================
# MODULE 1 - SUBTOPIC 3: Variables
# ============================================

# --- Example 1: Creating variables ---
age = 21
name = "Trush"
print(age)
print(name)

# --- Example 2: Variables can be used in expressions ---
price = 100
tax = 10
total = price + tax
print(total)  # 110

# --- Example 3: Changing a variable's value ---
score = 0
print(score)  # 0
score = 50
print(score)  # 50
score = 100
print(score)  # 100

# --- Example 4: Dynamic typing ---
# A variable can hold different types
x = 10
print(x)      # 10 (integer)
x = "hello"
print(x)      # hello (string)
x = 3.14
print(x)      # 3.14 (float)

# --- Example 5: Checking the type ---
a = 42
print(type(a))  # <class 'int'>
a = "world"
print(type(a))  # <class 'str'>

# --- Example 6: Variable naming ---
user_name = "Trush"     # ✅ good - descriptive, uses underscore
user_age = 21           # ✅ good
favorite_color = "blue" # ✅ good
print(user_name)
print(user_age)
print(favorite_color)

# --- Example 7: Case sensitivity ---
color = "red"
Color = "blue"
COLOR = "green"
print(color)   # red
print(Color)   # blue
print(COLOR)   # green
# These are THREE different variables!

# --- Example 8: Multiple assignment ---
a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3

# --- Example 9: Same value to multiple variables ---
x = y = z = 0
print(x)  # 0
print(y)  # 0
print(z)  # 0

# --- Example 10: Swapping values ---
first = "apple"
second = "banana"
print(first, second)  # apple banana

first, second = second, first
print(first, second)  # banana apple

# ============================================
# TRY IT YOURSELF:
# 1. Create a variable for your name and print it
# 2. Create two number variables and print their sum
# 3. Try assigning different types to the same variable
# ============================================
