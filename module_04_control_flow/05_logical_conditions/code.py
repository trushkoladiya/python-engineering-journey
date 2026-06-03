# ============================================
# MODULE 4 - SUBTOPIC 5: Logical Conditions in Control Flow
# ============================================

# --- Example 1: Using 'and' — both must be True ---
age = 21
has_id = True
if age >= 18 and has_id:
    print("Access granted")          # Access granted

# If either is False, the block does not run
age = 15
has_id = True
if age >= 18 and has_id:
    print("Access granted")          # does NOT print (age < 18)

# --- Example 2: Using 'or' — at least one must be True ---
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend!")                 # Weekend!

day = "Monday"
if day == "Saturday" or day == "Sunday":
    print("Weekend!")                 # does NOT print
else:
    print("Weekday")                 # Weekday

# --- Example 3: Using 'not' — reverses the condition ---
is_banned = False
if not is_banned:
    print("Welcome!")                 # Welcome! (not False = True)

is_logged_in = True
if not is_logged_in:
    print("Please log in")           # does NOT print (not True = False)

# --- Example 4: Combining and + or ---
temperature = 28
is_sunny = True
has_umbrella = False

# Parentheses make the logic clear
if temperature > 20 and (is_sunny or has_umbrella):
    print("Good day to go out!")      # Good day to go out!

# --- Example 5: Replacing nested if with 'and' ---
# Nested version:
username = "trush"
password = "python123"
if username == "trush":
    if password == "python123":
        print("Login OK (nested)")    # Login OK (nested)

# Same thing using 'and' — cleaner:
if username == "trush" and password == "python123":
    print("Login OK (flat)")          # Login OK (flat)

# --- Example 6: Range check using 'and' ---
score = 75
if score >= 70 and score <= 80:
    print("Score is in the 70-80 range")   # prints

# Python also supports chained comparisons (same thing):
if 70 <= score <= 80:
    print("Chained comparison works!")      # prints

# --- Example 7: Multiple 'or' conditions ---
color = "green"
if color == "red" or color == "yellow" or color == "green":
    print("Traffic light color")       # Traffic light color

# --- Example 8: not with comparison ---
x = 10
if not x == 5:
    print("x is not 5")               # x is not 5

# This is the same as:
if x != 5:
    print("x is not 5 (using !=)")    # x is not 5 (using !=)

# --- Example 9: Short-circuit with 'and' ---
# Python stops checking after first False
x = 0
if x != 0 and 100 / x > 5:
    print("Big number")
else:
    print("Safe — no division by zero")  # Safe — no division by zero
# 100/x was never evaluated because x != 0 was already False

# --- Example 10: Short-circuit with 'or' ---
# Python stops checking after first True
name = "Trush"
if name or len(name) > 100:
    print("Name exists")              # Name exists
# len(name) > 100 was never checked because name was truthy

# --- Example 11: Complex real-world condition ---
age = 21
income = 50000
has_good_credit = True

if age >= 21 and income >= 30000 and has_good_credit:
    print("Loan approved")            # Loan approved
else:
    print("Loan denied")

# --- Example 12: Precedence — 'not' > 'and' > 'or' ---
# Without parentheses:
a = True
b = False
c = True

result = a or b and not c
# Evaluated as: a or (b and (not c)) = True or (False and False) = True
print(result)                          # True

# With parentheses for clarity:
result = (a or b) and (not c)
# (True or False) and (not True) = True and False = False
print(result)                          # False

# ============================================
# TRY IT YOURSELF:
# 1. Check if a number is between 1 and 100 (inclusive) using 'and'
# 2. Check if a character is a vowel using multiple 'or' conditions
# 3. Use short-circuit to safely check division (avoid divide by zero)
# ============================================
