# ============================================
# MODULE 4 - SUBTOPIC 3: if-elif-else Ladder
# ============================================

# --- Example 1: Grading system ---
marks = 78
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")       # Grade: C
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# --- Example 2: Temperature categories ---
temp = 22
if temp >= 40:
    print("Extremely hot")
elif temp >= 30:
    print("Hot")
elif temp >= 20:
    print("Pleasant")       # Pleasant
elif temp >= 10:
    print("Cool")
else:
    print("Cold")

# --- Example 3: Number classification ---
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")           # Zero

# --- Example 4: Day of the week ---
day = "Wednesday"
if day == "Monday":
    print("Week starts")
elif day == "Wednesday":
    print("Midweek")        # Midweek
elif day == "Friday":
    print("Almost weekend")
elif day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Regular day")

# --- Example 5: Order matters! ---
# Wrong order — first True wins
score = 95
if score >= 50:
    print("Pass")           # This runs! (50 <= 95 is True, stops here)
elif score >= 90:
    print("Excellent")      # Never reached even though 95 >= 90

# Correct order — most restrictive first
score = 95
if score >= 90:
    print("Excellent")      # Excellent (correct!)
elif score >= 50:
    print("Pass")

# --- Example 6: BMI categories ---
weight = 70   # kg
height = 1.75 # meters
bmi = weight / (height * height)  # using operators from Module 3
print("BMI:", bmi)

if bmi >= 30:
    print("Obese")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal weight")  # Normal weight
else:
    print("Underweight")

# --- Example 7: Age group classification ---
age = 21
if age < 0:
    print("Invalid age")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")           # Adult
else:
    print("Senior")

# --- Example 8: Without else (all elif) ---
color = "green"
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Caution")
elif color == "green":
    print("Go")             # Go
# No else — if none match, nothing happens

# --- Example 9: Multiple elif blocks ---
month = 3
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")          # March
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
else:
    print("Other month")

# ============================================
# TRY IT YOURSELF:
# 1. Classify a number as: "small" (< 10), "medium" (10-99), or "large" (>= 100)
# 2. Create a simple calculator: given two numbers and an operator string,
#    print the result (use +, -, *, /)
# 3. Classify a character as vowel or consonant (store in a variable)
# ============================================
