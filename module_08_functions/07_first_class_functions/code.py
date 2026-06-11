# ============================================
# MODULE 8 - SUBTOPIC 7: Functions as First-Class Objects
# ============================================

# =============================
# 1. ASSIGNING FUNCTIONS TO VARIABLES
# =============================

# --- Example 1: Function reference ---
def greet(name):
    return f"Hello, {name}!"

# Assign the function to a new variable (no parentheses!)
say_hello = greet

print(say_hello("Trush"))   # Hello, Trush!
print(say_hello("Rahul"))     # Hello, Rahul!
print(f"Same function? {greet is say_hello}")   # True

# --- Example 2: Storing functions in a list ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

operations = [add, subtract, multiply]
names = ["Add", "Subtract", "Multiply"]

print("\nOperations on 10 and 3:")
for op, name in zip(operations, names):
    print(f"  {name}: {op(10, 3)}")

# --- Example 3: Storing functions in a dictionary ---
math_ops = {
    "+": add,
    "-": subtract,
    "*": multiply,
}

print("\nUsing dict of functions:")
for symbol, func in math_ops.items():
    print(f"  10 {symbol} 3 = {func(10, 3)}")

# =============================
# 2. PASSING FUNCTIONS AS ARGUMENTS
# =============================

# --- Example 4: Basic function passing ---
def apply(func, value):
    return func(value)

def double(n):
    return n * 2

def square(n):
    return n * n

def negate(n):
    return -n

print(f"\napply(double, 5) = {apply(double, 5)}")
print(f"apply(square, 5) = {apply(square, 5)}")
print(f"apply(negate, 5) = {apply(negate, 5)}")

# --- Example 5: Apply to a list ---
def apply_to_list(func, items):
    result = []
    for item in items:
        result.append(func(item))
    return result

numbers = [1, 2, 3, 4, 5]
print(f"\nOriginal: {numbers}")
print(f"Doubled:  {apply_to_list(double, numbers)}")
print(f"Squared:  {apply_to_list(square, numbers)}")

# --- Example 6: Using with built-in functions ---
def apply_and_print(func, data, label):
    result = func(data)
    print(f"  {label}: {result}")

numbers = [5, 2, 8, 1, 9]
print(f"\nData: {numbers}")
apply_and_print(max, numbers, "Max")
apply_and_print(min, numbers, "Min")
apply_and_print(sum, numbers, "Sum")
apply_and_print(sorted, numbers, "Sorted")

# =============================
# 3. RETURNING FUNCTIONS FROM FUNCTIONS
# =============================

# --- Example 7: Function factory ---
def make_multiplier(factor):
    def multiplier(n):
        return n * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
times_ten = make_multiplier(10)

print(f"\ndouble(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")
print(f"times_ten(5) = {times_ten(5)}")

# --- Example 8: Greeting factory ---
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

hello = make_greeter("Hello")
hi = make_greeter("Hi")
hey = make_greeter("Hey there")

print(f"\n{hello('Trush')}")
print(f"{hi('Rahul')}")
print(f"{hey('Charlie')}")

# --- Example 9: Power function factory ---
def make_power(exponent):
    def power(base):
        return base ** exponent
    return power

square = make_power(2)
cube = make_power(3)

print(f"\nsquare(5) = {square(5)}")
print(f"cube(5) = {cube(5)}")

# =============================
# 4. PRACTICAL EXAMPLES
# =============================

# --- Example 10: Simple calculator using function dispatch ---
def calculator(a, operator, b):
    ops = {
        "+": add,
        "-": subtract,
        "*": multiply,
    }
    
    if operator in ops:
        return ops[operator](a, b)
    return "Unknown operator"

print("\nCalculator:")
print(f"  10 + 3 = {calculator(10, '+', 3)}")
print(f"  10 - 3 = {calculator(10, '-', 3)}")
print(f"  10 * 3 = {calculator(10, '*', 3)}")

# --- Example 11: Filter function ---
def filter_list(func, items):
    result = []
    for item in items:
        if func(item):
            result.append(item)
    return result

def is_positive(n):
    return n > 0

def is_even(n):
    return n % 2 == 0

numbers = [-3, -1, 0, 2, 4, 5, -7, 8]
print(f"\nOriginal: {numbers}")
print(f"Positive: {filter_list(is_positive, numbers)}")
print(f"Even:     {filter_list(is_even, numbers)}")

# ============================================
# TRY IT YOURSELF:
# 1. Store 3 functions in a dictionary and call them by name
# 2. Write a function that takes another function as an argument
# 3. Create a function factory that generates greeting functions
# ============================================
