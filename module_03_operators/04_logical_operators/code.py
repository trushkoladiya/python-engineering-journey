# ============================================
# MODULE 3 - SUBTOPIC 4: Logical Operators
# ============================================

# --- Example 1: and — both must be True ---
print(True and True)     # True
print(True and False)    # False
print(False and True)    # False
print(False and False)   # False

# --- Example 2: or — at least one must be True ---
print(True or True)      # True
print(True or False)     # True
print(False or True)     # True
print(False or False)    # False

# --- Example 3: not — reverses the value ---
print(not True)          # False
print(not False)         # True

# --- Example 4: Using with comparisons ---
age = 21
print(age > 18 and age < 30)    # True — both true
print(age > 18 and age < 20)    # False — second is false

score = 85
print(score > 90 or score > 80)  # True — second is true
print(score > 90 or score > 95)  # False — both false

# --- Example 5: not with comparisons ---
is_raining = True
print(not is_raining)            # False

temperature = 15
print(not temperature > 30)      # True (temperature is NOT > 30)

# --- Example 6: Combining multiple conditions ---
age = 21
has_id = True
has_ticket = True

can_enter = age >= 18 and has_id and has_ticket
print(f"Can Trush enter: {can_enter}")   # Can Trush enter: True

# --- Example 7: or with multiple conditions ---
is_weekend = False
is_holiday = False
is_vacation = True

is_free = is_weekend or is_holiday or is_vacation
print(is_free)     # True — at least one is True

# --- Example 8: Mixing and, or, not ---
x = 10
result = x > 5 and not x > 20
print(result)      # True — x > 5 is True, x > 20 is False, not False = True

# --- Example 9: Short-circuit evaluation with and ---
# and stops at the first False
print(False and "never checked")    # False
print(True and "checked")           # checked

# --- Example 10: Short-circuit evaluation with or ---
# or stops at the first True
print(True or "never checked")      # True
print(False or "checked")           # checked

# --- Example 11: Practical — checking a range ---
temperature = 22
is_comfortable = temperature >= 18 and temperature <= 28
print(is_comfortable)   # True

# Same thing with chained comparison (cleaner)
print(18 <= temperature <= 28)   # True

# --- Example 12: Truthy/Falsy with logical operators ---
# Non-zero numbers are truthy, 0 is falsy
print(5 and 3)       # 3  (both truthy, returns last)
print(0 and 3)       # 0  (first is falsy, stops)
print(0 or 3)        # 3  (first is falsy, returns second)
print(5 or 3)        # 5  (first is truthy, stops)

# ============================================
# TRY IT YOURSELF:
# 1. Check if a number is between 1 and 100 using and
# 2. Use not to reverse a True value
# 3. Try: print(0 or "" or "hello") — what happens?
# ============================================
