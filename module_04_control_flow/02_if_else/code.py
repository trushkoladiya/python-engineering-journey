# ============================================
# MODULE 4 - SUBTOPIC 2: if-else
# ============================================

# --- Example 1: Basic if-else ---
age = 21
if age >= 18:
    print("You can vote")            # You can vote
else:
    print("You cannot vote yet")

# --- Example 2: Even or Odd check ---
number = 13
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")        # 13 is odd

# --- Example 3: Positive or Negative ---
value = -8
if value >= 0:
    print("Positive or zero")
else:
    print("Negative")             # Negative

# --- Example 4: Pass or Fail ---
marks = 62
if marks >= 50:
    print("Passed!")              # Passed!
    print("Well done!")           # Well done!
else:
    print("Failed")
    print("Study harder")

# --- Example 5: Storing result in a variable ---
temperature = 35
if temperature > 30:
    weather = "Hot"
else:
    weather = "Pleasant"
print("Today's weather:", weather)   # Today's weather: Hot

# --- Example 6: Checking string emptiness ---
username = "Trush"
if username:
    print("Hello,", username)        # Hello, Trush
else:
    print("No username provided")

# --- Example 7: Comparing two numbers ---
a = 25
b = 40
if a > b:
    bigger = a
else:
    bigger = b
print("Bigger number is:", bigger)  # Bigger number is: 40

# --- Example 8: Checking divisibility ---
num = 15
if num % 5 == 0:
    print(num, "is divisible by 5")   # 15 is divisible by 5
else:
    print(num, "is NOT divisible by 5")

# --- Example 9: Boolean variable in if-else ---
is_logged_in = False
if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in")          # Please log in

# --- Example 10: Default path always executes one side ---
x = 100
if x > 100:
    print("Greater than 100")
else:
    print("100 or less")            # 100 or less
# Note: x is exactly 100, so x > 100 is False → else runs

# ============================================
# TRY IT YOURSELF:
# 1. Check if a number is positive or negative
# 2. Check if a person's age makes them a teenager (13-19) or not
# 3. Compare two strings and print which one is longer
# ============================================
