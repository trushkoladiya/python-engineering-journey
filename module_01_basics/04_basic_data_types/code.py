# ============================================
# MODULE 1 - SUBTOPIC 4: Basic Data Types
# ============================================

# --- Example 1: Integer (int) ---
age = 21
year = 2025
negative = -10
print(age)       # 25
print(year)      # 2025
print(negative)  # -10
print(type(age)) # <class 'int'>

# --- Example 2: Float (float) ---
price = 19.99
temperature = -3.5
height = 5.0  # still a float because of the decimal point
print(price)         # 19.99
print(temperature)   # -3.5
print(type(height))  # <class 'float'>

# --- Example 3: String (str) ---
name = "Trush"
greeting = 'Hello, World!'
empty = ""  # an empty string is still a string
print(name)          # Trush
print(greeting)      # Hello, World!
print(type(name))    # <class 'str'>
print(type(empty))   # <class 'str'>

# --- Example 4: Boolean (bool) ---
is_student = True
is_raining = False
print(is_student)        # True
print(is_raining)        # False
print(type(is_student))  # <class 'bool'>

# --- Example 5: Checking types of different values ---
print(type(100))      # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>

# --- Example 6: Be careful - quotes change everything ---
number = 42
text = "42"
print(type(number))  # <class 'int'>  — it's a number
print(type(text))    # <class 'str'>  — it's text!
# 42 and "42" are NOT the same thing

# --- Example 7: Float vs Integer ---
a = 5    # integer
b = 5.0  # float
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
# They look similar but are different types

# --- Example 8: Boolean values are case-sensitive ---
correct = True   # ✅ this works
# correct = true  # ❌ this would cause an error (lowercase)

# --- Example 9: Storing different types in variables ---
player_name = "Trush"
player_score = 9500
player_health = 85.5
is_alive = True

print(player_name)
print(player_score)
print(player_health)
print(is_alive)

# ============================================
# TRY IT YOURSELF:
# 1. Create one variable of each type and print it
# 2. Use type() on each to verify
# 3. Try: what type is True? What type is "True"?
# ============================================
