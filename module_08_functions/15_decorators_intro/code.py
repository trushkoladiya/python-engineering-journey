# ============================================
# MODULE 8 - SUBTOPIC 15: Decorators (Introduction)
# ============================================
# Advanced decorators are covered in Module 13.
# Here we learn the basics: what they are and how to write simple ones.

# =============================
# 1. THE CONCEPT — WRAPPING A FUNCTION
# =============================

# --- Example 1: Manual wrapping (before learning @ syntax) ---
def shout(func):
    """A decorator that prints the result in uppercase."""
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def say_hello():
    return "hello, world!"

# Manually wrap the function
say_hello = shout(say_hello)
print(say_hello())   # HELLO, WORLD!

# =============================
# 2. THE @ SYNTAX
# =============================

# --- Example 2: Using @ decorator syntax ---
def shout_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@shout_decorator
def greet():
    return "good morning!"

# @shout_decorator is the same as: greet = shout_decorator(greet)
print(f"\n{greet()}")   # GOOD MORNING!

# --- Example 3: Another simple decorator ---
def add_stars(func):
    """Add stars around the output."""
    def wrapper():
        print("* * * * * * * * * *")
        func()
        print("* * * * * * * * * *")
    return wrapper

@add_stars
def say_name():
    print("  Hello, I am Python!")

print()
say_name()

# =============================
# 3. DECORATOR THAT RUNS CODE BEFORE/AFTER
# =============================

# --- Example 4: Before and after ---
def log_call(func):
    """Print a message before and after the function runs."""
    def wrapper():
        print(f"  → Calling {func.__name__}()")
        func()
        print(f"  → {func.__name__}() finished")
    return wrapper

@log_call
def process_data():
    print("  Processing...")

print("\nWith logging:")
process_data()

# =============================
# 4. DECORATORS WITH FUNCTION ARGUMENTS
# =============================

# --- Example 5: Handling *args and **kwargs ---
def log_args(func):
    """Log the arguments passed to a function."""
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  → Returned: {result}")
        return result
    return wrapper

@log_args
def add(a, b):
    return a + b

@log_args
def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print("\nLogged calls:")
add(3, 5)
print()
greet_person("Trush", greeting="Hi")

# =============================
# 5. PRACTICAL DECORATOR: TIMER
# =============================

# --- Example 6: Timing a function ---
import time

def timer(func):
    """Measure how long a function takes to run."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"  ⏱ {func.__name__}() took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    total = 0
    for i in range(1000000):
        total = total + i
    return total

print("\nTimed function:")
result = slow_function()
print(f"  Result: {result}")

# =============================
# 6. PRACTICAL DECORATOR: VALIDATION
# =============================

# --- Example 7: Validating inputs ---
def validate_positive(func):
    """Ensure all positional arguments are positive numbers."""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                print(f"  ❌ Error: negative value {arg} not allowed!")
                return None
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width

print("\nValidation decorator:")
print(f"  area(5, 3) = {calculate_area(5, 3)}")
print(f"  area(-2, 3) = {calculate_area(-2, 3)}")

# =============================
# 7. MULTIPLE DECORATED FUNCTIONS
# =============================

# --- Example 8: Same decorator on different functions ---
def bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

@bold
def get_name():
    return "Trush"

@bold
def get_title():
    return "Python Developer"

print(f"\n{get_name()}")
print(f"{get_title()}")

# =============================
# 8. HOW @ SYNTAX WORKS (BEHIND THE SCENES)
# =============================

# --- Example 9: @ is just syntactic sugar ---
def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

# These two are IDENTICAL:

# Way 1: Using @
@exclaim
def greeting_a():
    return "Hello"

# Way 2: Manual wrapping
def greeting_b():
    return "Hello"

greeting_b = exclaim(greeting_b)

print(f"\n@ syntax:  {greeting_a()}")
print(f"Manual:    {greeting_b()}")
print(f"Same? {greeting_a() == greeting_b()}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a decorator that prints "START" and "END" around a function
# 2. Create a decorator that counts how many times a function is called
# 3. Decorate a function that takes arguments
#
# 📌 Advanced decorator topics (parameterized decorators,
#    stacking, class-based decorators) are covered in Module 13.
# ============================================
