# ============================================
# MODULE 8 - SUBTOPIC 5: Variable Scope
# ============================================

# =============================
# 1. LOCAL VARIABLES
# =============================

# --- Example 1: Variable only exists inside function ---
def my_function():
    message = "I am local"
    print(f"Inside: {message}")

my_function()
# print(message)   # ❌ NameError: 'message' is not defined
print("The variable 'message' does not exist outside the function")

# --- Example 2: Each function has its own local scope ---
def func_a():
    x = 10
    print(f"  func_a: x = {x}")

def func_b():
    x = 20
    print(f"  func_b: x = {x}")

print("\nSeparate scopes:")
func_a()
func_b()

# --- Example 3: Local variable doesn't affect outside ---
def change_value():
    name = "Rahul"
    print(f"  Inside function: {name}")

name = "Trush"
print(f"\nBefore call: {name}")
change_value()
print(f"After call: {name}")   # Still "Trush"

# =============================
# 2. GLOBAL VARIABLES
# =============================

# --- Example 4: Reading a global variable ---
greeting = "Hello"

def say_greeting():
    print(f"  {greeting}, World!")   # Can READ global

print("\nReading global:")
say_greeting()

# --- Example 5: Global variable accessible everywhere ---
PI = 3.14159

def circle_area(radius):
    return PI * radius * radius

print(f"\nPI = {PI}")
print(f"Area of circle (r=5): {circle_area(5):.2f}")

# =============================
# 3. THE global KEYWORD
# =============================

# --- Example 6: Modifying global with 'global' keyword ---
count = 0

def increment():
    global count
    count = count + 1

print(f"\nBefore: count = {count}")
increment()
increment()
increment()
print(f"After 3 increments: count = {count}")   # 3

# --- Example 7: Without global keyword ---
score = 100

def try_to_change():
    score = 999   # This creates a LOCAL variable, doesn't change global!
    print(f"  Inside: score = {score}")   # 999

print(f"\nGlobal score: {score}")   # 100
try_to_change()
print(f"Global score: {score}")     # Still 100!

# --- Example 8: With global keyword ---
score2 = 100

def actually_change():
    global score2
    score2 = 999
    print(f"  Inside: score2 = {score2}")

print(f"\nGlobal score2: {score2}")   # 100
actually_change()
print(f"Global score2: {score2}")     # 999 — changed!

# =============================
# 4. VARIABLE SHADOWING
# =============================

# --- Example 9: Local shadows global ---
x = 100

def shadow_demo():
    x = 5   # This is a NEW local variable, not the global
    print(f"  Local x: {x}")

print(f"\nGlobal x: {x}")
shadow_demo()
print(f"Global x still: {x}")   # Unchanged

# --- Example 10: Be careful with shadowing ---
data = [1, 2, 3]

def process():
    data = [99, 99]   # Shadows global 'data'
    print(f"  Inside: {data}")

print(f"\nGlobal data: {data}")
process()
print(f"Global data: {data}")   # Unchanged — [1, 2, 3]

# =============================
# 5. BEST PRACTICE: USE PARAMETERS AND RETURN
# =============================

# --- Example 11: Bad — using global ---
total_bad = 0

def add_to_total_bad(value):
    global total_bad
    total_bad = total_bad + value

add_to_total_bad(10)
add_to_total_bad(20)
print(f"\nBad approach (global): {total_bad}")

# --- Example 12: Good — using parameters and return ---
def add_to_total_good(current_total, value):
    return current_total + value

total_good = 0
total_good = add_to_total_good(total_good, 10)
total_good = add_to_total_good(total_good, 20)
print(f"Good approach (params): {total_good}")

# --- Example 13: Practical — counter without global ---
def count_vowels(text):
    count = 0   # Local variable
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count = count + 1
    return count

word = "Hello World"
result = count_vowels(word)
print(f"\nVowels in '{word}': {result}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a local variable inside a function and try to access it outside
# 2. Use the global keyword to modify a variable from inside a function
# 3. Rewrite a global-based function to use parameters and return instead
# ============================================
