# ============================================
# MODULE 1 - SUBTOPIC 6: Type Casting
# ============================================

# --- Example 1: String to Integer ---
x = "10"
print(type(x))  # <class 'str'>
y = int(x)
print(y)         # 10
print(type(y))   # <class 'int'>

# --- Example 2: String to Float ---
price = "19.99"
price = float(price)
print(price)        # 19.99
print(type(price))  # <class 'float'>

# --- Example 3: Integer to String ---
age = 21
age_text = str(age)
print("I am " + age_text + " years old")
print(type(age_text))  # <class 'str'>

# --- Example 4: Integer to Float ---
a = 5
b = float(a)
print(b)         # 5.0
print(type(b))   # <class 'float'>

# --- Example 5: Float to Integer (drops decimal) ---
pi = 3.99
whole = int(pi)
print(whole)  # 3 (it chops off the decimal, does NOT round)

# --- Example 6: Implicit casting (Python does it) ---
result = 10 + 3.5  # int + float → float
print(result)       # 13.5
print(type(result)) # <class 'float'>

# --- Example 7: bool() conversion ---
print(bool(0))      # False
print(bool(1))      # True
print(bool(42))     # True
print(bool(-1))     # True
print(bool(""))     # False (empty string)
print(bool("hi"))   # True (non-empty string)
print(bool(0.0))    # False

# --- Example 8: Practical use — converting input ---
# num = int(input("Enter a number: "))
# print(f"Double of {num} is {num * 2}")

# --- Example 9: Chained conversion ---
text = "3.14"
# int(text) would FAIL — can't go directly from "3.14" to int
number = int(float(text))  # first float, then int
print(number)  # 3

# ============================================
# TRY IT YOURSELF:
# 1. Convert the string "100" to an integer and add 50
# 2. Convert the number 42 to a string and concatenate with text
# 3. Try bool() on different values
# ============================================
