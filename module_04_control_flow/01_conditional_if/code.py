# ============================================
# MODULE 4 - SUBTOPIC 1: Conditional Statements (if)
# ============================================

# --- Example 1: Basic if statement ---
age = 21
if age >= 18:
    print("You are an adult")   # You are an adult

# --- Example 2: if with different conditions ---
temperature = 38
if temperature > 37:
    print("You have a fever")   # You have a fever

score = 85
if score >= 80:
    print("You passed with distinction")  # You passed with distinction

# --- Example 3: Condition evaluates to False — nothing happens ---
x = 5
if x > 100:
    print("x is very large")   # This does NOT print

# --- Example 4: Multiple lines inside if block ---
balance = 5000
if balance > 1000:
    print("You have sufficient balance")   # prints
    print("You can make a withdrawal")     # prints
    print("Current balance:", balance)      # prints

# --- Example 5: Code after if block always runs ---
num = 3
if num > 10:
    print("Big number")        # does NOT print (3 is not > 10)
print("Check complete")       # ALWAYS prints (not indented under if)

# --- Example 6: Boolean condition evaluation (truthy/falsy) ---
# Non-zero numbers are truthy
if 1:
    print("1 is truthy")       # prints

if -5:
    print("-5 is truthy")      # prints

# Zero is falsy
if 0:
    print("0 is truthy")       # does NOT print

# Non-empty strings are truthy
name = "Trush"
if name:
    print("Name is not empty") # prints

# Empty string is falsy
empty = ""
if empty:
    print("This won't print")  # does NOT print

# None is falsy
value = None
if value:
    print("This won't print")  # does NOT print

# --- Example 7: Using comparison operators in conditions ---
a = 15
b = 20

if a < b:
    print(a, "is less than", b)     # 15 is less than 20

if a != b:
    print("a and b are different")  # a and b are different

if a == 15:
    print("a is exactly 15")        # a is exactly 15

# --- Example 8: Using variables as conditions ---
is_sunny = True
if is_sunny:
    print("Wear sunglasses")   # Wear sunglasses

is_raining = False
if is_raining:
    print("Take an umbrella")  # does NOT print

# --- Example 9: Indentation matters ---
number = 7
if number > 5:
    print("Greater than 5")    # inside if — prints only when True
    print("Still inside if")   # inside if — prints only when True
print("Outside if block")     # outside if — always prints

# ============================================
# TRY IT YOURSELF:
# 1. Create a variable 'marks' = 45, check if marks >= 40 and print "Passed"
# 2. Check if a string variable is not empty (truthy) and print it
# 3. Use a boolean variable to control whether a message prints
# ============================================
