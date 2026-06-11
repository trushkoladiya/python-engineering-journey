# ============================================
# MODULE 8 - SUBTOPIC 1: Function Definition
# ============================================

# =============================
# 1. YOUR FIRST FUNCTION
# =============================

# --- Example 1: Simplest function ---
def greet():
    print("Hello, World!")

# Call the function
greet()

# --- Example 2: Function with multiple lines ---
def introduce():
    print("My name is Python.")
    print("I am a programming language.")
    print("Nice to meet you!")

introduce()

# =============================
# 2. FUNCTION NAMING
# =============================

# --- Example 3: Good naming with snake_case ---
def say_hello():
    print("\nHello there!")

def print_separator():
    print("-" * 30)

say_hello()
print_separator()

# --- Example 4: Descriptive names ---
def show_welcome_message():
    print("\n=== Welcome to Python! ===")
    print("Let's learn functions today.")
    print("==========================")

show_welcome_message()

# =============================
# 3. FUNCTION STRUCTURE
# =============================

# --- Example 5: Function with variables inside ---
def show_info():
    name = "Trush"
    age = 21
    city = "Mumbai"
    print(f"\nName: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

show_info()

# --- Example 6: Function with a loop ---
def count_to_five():
    print("\nCounting:")
    for i in range(1, 6):
        print(f"  {i}")

count_to_five()

# --- Example 7: Function with a condition ---
def check_time():
    hour = 10
    if hour < 12:
        print("\nGood morning!")
    elif hour < 18:
        print("\nGood afternoon!")
    else:
        print("\nGood evening!")

check_time()

# =============================
# 4. CALLING A FUNCTION MULTIPLE TIMES
# =============================

# --- Example 8: Reuse by calling multiple times ---
def print_star_line():
    print("* * * * * * * * * *")

print("\n")
print_star_line()
print("   Happy Learning!   ")
print_star_line()

# --- Example 9: Function in a loop ---
def say_hi():
    print("Hi!")

print()
for i in range(3):
    say_hi()

# =============================
# 5. FUNCTION DOES NOTHING UNTIL CALLED
# =============================

# --- Example 10: Defined but not called ---
def secret_message():
    print("This won't print unless called!")

# Notice: no output from secret_message above
print("\nThe function exists but wasn't called.")

# Now let's call it:
secret_message()

# --- Example 11: Order of definition and call ---
# The function must be defined BEFORE it is called
def greet_user():
    print("\nHello, user!")

greet_user()   # ✅ Works — defined above

# This would cause an error:
# unknown_function()   # ❌ NameError: not defined

# ============================================
# TRY IT YOURSELF:
# 1. Create a function that prints your name and age
# 2. Create a function that prints a box of asterisks
# 3. Call the same function 5 times using a loop
# ============================================
