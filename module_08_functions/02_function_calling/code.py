# ============================================
# MODULE 8 - SUBTOPIC 2: Function Calling
# ============================================

# =============================
# 1. BASIC FUNCTION CALLING
# =============================

# --- Example 1: Define and call ---
def greet():
    print("Hello, World!")

greet()   # Calling the function

# --- Example 2: Calling multiple times ---
def say_thanks():
    print("Thank you!")

print("\nSaying thanks 3 times:")
say_thanks()
say_thanks()
say_thanks()

# =============================
# 2. EXECUTION FLOW
# =============================

# --- Example 3: Understanding the order ---
print("\n--- Execution Flow ---")
print("1. Before function definition")

def my_function():
    print("3. Inside the function")

print("2. After definition, before call")
my_function()
print("4. After function call")

# --- Example 4: Two functions, different order ---
print("\n--- Two Functions ---")

def first():
    print("  Running first()")

def second():
    print("  Running second()")

print("Calling second, then first:")
second()
first()

# =============================
# 3. FUNCTIONS CALLING OTHER FUNCTIONS
# =============================

# --- Example 5: One function calling another ---
def print_line():
    print("-" * 30)

def print_header():
    print_line()
    print("  WELCOME TO PYTHON")
    print_line()

print()
print_header()

# --- Example 6: Chain of function calls ---
def step_one():
    print("  Step 1: Prepare data")

def step_two():
    print("  Step 2: Process data")

def step_three():
    print("  Step 3: Show results")

def run_all_steps():
    print("\nRunning all steps:")
    step_one()
    step_two()
    step_three()
    print("  Done!")

run_all_steps()

# =============================
# 4. CALLING IN LOOPS
# =============================

# --- Example 7: Calling a function in a loop ---
def print_star():
    print("⭐", end=" ")

print("\n\nStars:")
for i in range(5):
    print_star()
print()   # New line after stars

# --- Example 8: Calling with loop counter ---
def show_number(n):
    print(f"  Number: {n}")

print("\nCounting:")
for i in range(1, 4):
    show_number(i)

# =============================
# 5. CALLING IN CONDITIONS
# =============================

# --- Example 9: Calling based on condition ---
def celebrate():
    print("  🎉 Congratulations!")

def encourage():
    print("  💪 Keep trying!")

score = 85
print(f"\nScore: {score}")
if score >= 70:
    celebrate()
else:
    encourage()

# --- Example 10: Multiple conditions ---
def morning_routine():
    print("  ☀️ Good morning! Time for coffee.")

def evening_routine():
    print("  🌙 Good evening! Time to relax.")

hour = 9
print(f"\nHour: {hour}")
if hour < 12:
    morning_routine()
else:
    evening_routine()

# =============================
# 6. COMMON MISTAKE
# =============================

# --- Example 11: Forgetting parentheses ---
def hello():
    print("Hello!")

print("\nWith parentheses:")
hello()      # ✅ Calls the function

print("\nWithout parentheses:")
print(hello)  # ❌ Prints the function object, doesn't call it

# ============================================
# TRY IT YOURSELF:
# 1. Create two functions and call them in different orders
# 2. Create a function and call it inside a for loop
# 3. Create a function that calls another function
# ============================================
