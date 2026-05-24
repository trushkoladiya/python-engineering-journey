# ============================================
# MODULE 1 - SUBTOPIC 5: Input & Output
# ============================================

# --- Example 1: Basic print ---
print("Hello, World!")
print(42)
print(3.14)
print(True)

# --- Example 2: Printing multiple values ---
print("Name:", "Trush")       # Name: Trush
print("Score:", 100)          # Score: 100
print("A", "B", "C", "D")    # A B C D

# --- Example 3: Custom separator ---
print("2025", "05", "07", sep="-")  # 2025-05-07
print("a", "b", "c", sep=" | ")    # a | b | c
print("x", "y", "z", sep="")       # xyz

# --- Example 4: Custom end ---
print("Hello", end=" ")
print("World")  # Hello World (on same line)
print()  # blank line

print("Loading", end="...")
print("Done!")  # Loading...Done!

# --- Example 5: String concatenation ---
first_name = "Trush"
last_name = "Koladiya"
full_name = first_name + " " + last_name
print("Full name: " + full_name)

# --- Example 6: f-strings (best way to format) ---
name = "Trush"
age = 21
city = "Mumbai"
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"{name} lives in {city}")

# --- Example 7: f-strings with expressions ---
price = 50
quantity = 3
print(f"Total: {price * quantity}")  # Total: 150

a = 10
b = 20
print(f"{a} + {b} = {a + b}")  # 10 + 20 = 30

# --- Example 8: input() — getting user input ---
# Uncomment the lines below to try (they wait for you to type)

# user_name = input("What is your name? ")
# print(f"Hello, {user_name}!")

# --- Example 9: input() always returns a string ---
# num = input("Enter a number: ")
# print(type(num))  # <class 'str'> — it's a string!

# --- Example 10: Converting input to a number ---
# age = int(input("Enter your age: "))
# print(f"Next year you will be {age + 1}")

# --- Example 11: Float input ---
# weight = float(input("Enter your weight in kg: "))
# print(f"Your weight is {weight} kg")

# ============================================
# TRY IT YOURSELF:
# 1. Uncomment the input examples and run the file
# 2. Try printing your name and age using f-strings
# 3. Try using different sep and end values
# ============================================
