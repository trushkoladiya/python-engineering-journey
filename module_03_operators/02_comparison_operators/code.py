# ============================================
# MODULE 3 - SUBTOPIC 2: Comparison (Relational) Operators
# ============================================

# --- Example 1: Equal to (==) ---
print(5 == 5)       # True
print(5 == 3)       # False
print("hi" == "hi") # True
print("hi" == "Hi") # False (case-sensitive!)

# --- Example 2: Not equal to (!=) ---
print(5 != 3)       # True
print(5 != 5)       # False
print("a" != "b")   # True

# --- Example 3: Greater than (>) ---
print(10 > 5)       # True
print(5 > 10)       # False
print(5 > 5)        # False (not greater, just equal)

# --- Example 4: Less than (<) ---
print(3 < 7)        # True
print(7 < 3)        # False
print(5 < 5)        # False

# --- Example 5: Greater than or equal (>=) ---
print(10 >= 10)     # True (equal counts!)
print(10 >= 5)      # True
print(3 >= 5)       # False

# --- Example 6: Less than or equal (<=) ---
print(5 <= 5)       # True (equal counts!)
print(3 <= 5)       # True
print(7 <= 5)       # False

# --- Example 7: Comparing different types ---
print(10 == 10.0)   # True — Python compares the values
print(10 > 9.5)     # True
print(1 == True)    # True — True is treated as 1
print(0 == False)   # True — False is treated as 0

# --- Example 8: Storing comparison results ---
age = 21
is_adult = age >= 18
print(is_adult)         # True
print(type(is_adult))   # <class 'bool'>

price = 50
is_expensive = price > 100
print(is_expensive)     # False

# --- Example 9: == vs = ---
x = 10              # assignment (storing value)
print(x == 10)      # comparison (checking equality) → True
print(x == 5)       # False

# --- Example 10: Chained comparisons ---
score = 75
print(0 <= score <= 100)    # True — score is in range
print(60 <= score <= 80)    # True
print(80 < score < 100)     # False

temperature = 22
print(15 < temperature < 30)  # True — comfortable range

# --- Example 11: Comparing strings (alphabetical order) ---
print("apple" < "banana")   # True (a comes before b)
print("cat" > "bat")        # True (c comes after b)
print("abc" == "abc")       # True

# ============================================
# TRY IT YOURSELF:
# 1. Check if 100 is equal to 100.0
# 2. Store the result of 50 > 30 in a variable and print it
# 3. Use a chained comparison to check if 25 is between 20 and 30
# ============================================
