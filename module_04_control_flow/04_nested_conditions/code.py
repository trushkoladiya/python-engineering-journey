# ============================================
# MODULE 4 - SUBTOPIC 4: Nested Conditions
# ============================================

# --- Example 1: Basic nesting ---
age = 21
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")        # You can drive
    else:
        print("Get a license first")
else:
    print("Too young to drive")

# --- Example 2: Two-level nesting ---
num = -5
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")                  # Negative

# --- Example 3: Nested if with elif ---
score = 85
is_bonus = True

if score >= 50:
    print("Passed!")                   # Passed!
    if is_bonus:
        if score >= 90:
            print("Bonus: Gold star")
        elif score >= 80:
            print("Bonus: Silver star")  # Bonus: Silver star
        else:
            print("Bonus: Bronze star")
    else:
        print("No bonus available")
else:
    print("Failed")

# --- Example 4: Membership and purchase discount ---
is_member = True
purchase_amount = 750

if is_member:
    print("Member detected")          # Member detected
    if purchase_amount >= 1000:
        discount = 20
    elif purchase_amount >= 500:
        discount = 10
    else:
        discount = 5
else:
    if purchase_amount >= 1000:
        discount = 5
    else:
        discount = 0

print("Discount:", str(discount) + "%")  # Discount: 10%

# --- Example 5: Three levels of nesting ---
country = "India"
state = "Gujarat"
city = "Ahmedabad"

if country == "India":
    if state == "Gujarat":
        if city == "Ahmedabad":
            print("Welcome to Ahmedabad, Gujarat, India!")  # prints
        else:
            print("Welcome to Gujarat, India!")
    else:
        print("Welcome to India!")
else:
    print("International visitor")

# --- Example 6: Login system simulation ---
username = "trush"
password = "python123"

if username == "trush":
    if password == "python123":
        print("Login successful!")     # Login successful!
    else:
        print("Wrong password!")
else:
    print("User not found!")

# --- Example 7: Number classification with nesting ---
x = 24
if x > 0:
    print("Positive")                  # Positive
    if x % 2 == 0:
        print("Even")                  # Even
        if x % 4 == 0:
            print("Divisible by 4")    # Divisible by 4
    else:
        print("Odd")

# --- Example 8: Nesting vs flat structure comparison ---
# Nested version:
age = 21
has_ticket = True
if age >= 18:
    if has_ticket:
        print("Enter the concert")    # Enter the concert

# Same logic can sometimes be written flat (next subtopic covers this):
# if age >= 18 and has_ticket:
#     print("Enter the concert")

# ============================================
# TRY IT YOURSELF:
# 1. Check if a number is positive, then check if it's even or odd
# 2. Simulate an ATM: check PIN first, then check if balance is sufficient
# 3. Classify a student: first check if passed, then check grade level
# ============================================
