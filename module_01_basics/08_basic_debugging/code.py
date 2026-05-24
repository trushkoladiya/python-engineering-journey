# ============================================
# MODULE 1 - SUBTOPIC 8: Basic Debugging
# ============================================

# --- Example 1: Correct code (no errors) ---
print("This line works perfectly!")
x = 10
print(x)

# --- Example 2: Common Syntax Errors ---
# Uncomment each one, ONE AT A TIME, to see the error

# print("hello"         # SyntaxError: missing closing )
# print("hello')        # SyntaxError: mismatched quotes
#     print("hello")    # IndentationError: unexpected indent

# --- Example 3: Runtime Errors ---
# These are correct syntax but fail when running

# print(10 / 0)           # ZeroDivisionError: division by zero
# print(int("hello"))     # ValueError: invalid literal for int()
# print(unknown_variable) # NameError: name 'unknown_variable' is not defined

# --- Example 4: NameError — using a variable that doesn't exist ---
# print(age)  # ❌ NameError — 'age' was never created

age = 21
print(age)    # ✅ Now it works because age is defined

# --- Example 5: TypeError — mixing incompatible types ---
# print("Age: " + 25)  # ❌ TypeError: can't add string and integer

print("Age: " + str(25))  # ✅ Convert to string first
print("Age:", 25)          # ✅ Or use comma (print handles it)

# --- Example 6: Debugging with print ---
# Use print() to check values when something seems wrong
a = 10
b = 3
result = a + b
print("DEBUG: a =", a)       # check what a holds
print("DEBUG: b =", b)       # check what b holds
print("DEBUG: result =", result)  # check the result

# --- Example 7: Fixing errors step by step ---
# Step 1: See the error
# Step 2: Read the LAST line of the error message
# Step 3: Look at the line number
# Step 4: Fix that one error
# Step 5: Run again

# Practice: Fix this code (uncomment and fix)
# greeting = "Hello
# print(greeting)
# FIX: greeting = "Hello"

# --- Example 8: Multiple errors — fix one at a time ---
# Always fix the FIRST error and run again
# Sometimes fixing one error fixes others too

name = "Trush"
age = 21
print(f"{name} is {age} years old")  # ✅ correct

# ============================================
# TRY IT YOURSELF:
# 1. Uncomment each error example ONE AT A TIME
# 2. Read the error message carefully
# 3. Try to fix each error before moving to the next
# ============================================
