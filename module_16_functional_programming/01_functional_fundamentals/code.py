# ============================================
# MODULE 16 - SUBTOPIC 1: Functional Programming Fundamentals
# ============================================

# Functional programming is a STYLE of writing code
# that focuses on functions transforming data.

# =============================
# 1. FUNCTIONS AS FIRST-CLASS CITIZENS
# =============================

print("=== Functions as First-Class Citizens ===")
print()

def square(x):
    """Return the square of x."""
    return x ** 2

def cube(x):
    """Return the cube of x."""
    return x ** 3

# Functions can be assigned to variables
operation = square
print(f"  operation(5) = {operation(5)}")   # 25

operation = cube
print(f"  operation(5) = {operation(5)}")   # 125
print()

# Functions can be stored in data structures
math_operations = {
    "square": square,
    "cube": cube,
}

for name, func in math_operations.items():
    print(f"  {name}(3) = {func(3)}")
print()

# =============================
# 2. PASSING FUNCTIONS AS ARGUMENTS
# =============================

print("=== Passing Functions as Arguments ===")
print()

def apply_operation(func, value):
    """Apply a function to a value and return the result."""
    return func(value)

print(f"  apply_operation(square, 4) = {apply_operation(square, 4)}")
print(f"  apply_operation(cube, 4)   = {apply_operation(cube, 4)}")
print()

# Apply to a list of values
def apply_to_list(func, items):
    """Apply a function to each item in a list."""
    result = []
    for item in items:
        result.append(func(item))
    return result

numbers = [1, 2, 3, 4, 5]
squared = apply_to_list(square, numbers)
print(f"  numbers: {numbers}")
print(f"  squared: {squared}")
print()

# =============================
# 3. RETURNING FUNCTIONS
# =============================

print("=== Returning Functions ===")
print()

def make_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"  double(10) = {double(10)}")   # 20
print(f"  triple(10) = {triple(10)}")   # 30
print()

# =============================
# 4. PURE FUNCTIONS
# =============================

print("=== Pure Functions ===")
print()

# PURE: depends ONLY on input, no side effects
def add(a, b):
    return a + b

def to_uppercase(text):
    return text.upper()

# Same input → same output, every time
print(f"  add(3, 4) = {add(3, 4)}")
print(f"  add(3, 4) = {add(3, 4)}")   # always the same!
print(f"  to_uppercase('hello') = '{to_uppercase('hello')}'")
print()

# IMPURE: modifies external state
log = []

def impure_add(a, b):
    result = a + b
    log.append(result)   # side effect — changes external list!
    return result

impure_add(1, 2)
impure_add(3, 4)
print(f"  log after impure_add calls: {log}")
print("  (This is a side effect — functional programming avoids this)")
print()

# =============================
# 5. IMMUTABILITY CONCEPT
# =============================

print("=== Immutability Concept ===")
print()

# Mutable approach — changes original data
mutable_list = [1, 2, 3]
mutable_list.append(4)
print(f"  Mutable: {mutable_list}")   # original changed

# Immutable approach — creates new data
original = (1, 2, 3)
new_tuple = original + (4,)
print(f"  Original tuple: {original}")
print(f"  New tuple:      {new_tuple}")
print()

# Functional style with lists — create new instead of mutating
original_list = [1, 2, 3, 4, 5]
# Instead of modifying original_list, create a new one
filtered = [x for x in original_list if x > 2]
print(f"  Original list: {original_list}")
print(f"  Filtered (new): {filtered}")
print()

# =============================
# 6. COMPARING STYLES
# =============================

print("=== Imperative vs Functional Style ===")
print()

# Task: Get squares of even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Imperative style — step by step, mutating
result_imperative = []
for n in numbers:
    if n % 2 == 0:
        result_imperative.append(n ** 2)
print(f"  Imperative result: {result_imperative}")

# Functional style — descriptive, no mutation
result_functional = [n ** 2 for n in numbers if n % 2 == 0]
print(f"  Functional result: {result_functional}")
print()

# =============================
# 7. FUNCTIONS IN LISTS
# =============================

print("=== Functions in Lists (Pipeline Preview) ===")
print()

def add_ten(x):
    return x + 10

def double(x):
    return x * 2

def negate(x):
    return -x

# A list of functions — a simple "pipeline"
pipeline = [add_ten, double, negate]

value = 5
print(f"  Starting value: {value}")
for func in pipeline:
    value = func(value)
    print(f"  After {func.__name__}: {value}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a pure function that reverses a string
# 2. Write a function that takes a function and a list,
#    and returns a new list with the function applied
# 3. Store 3 different functions in a dictionary
#    and call each one
# ============================================
