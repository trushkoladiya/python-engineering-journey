# ============================================
# MODULE 16 - SUBTOPIC 9: Higher-Order Functions
# ============================================

# A higher-order function either:
# 1. Takes a function as an argument, OR
# 2. Returns a function as its result

# =============================
# 1. FUNCTIONS AS ARGUMENTS
# =============================

print("=== Functions as Arguments ===")
print()

def apply(func, value):
    """Apply a function to a value."""
    return func(value)

print(f"  apply(len, 'hello') = {apply(len, 'hello')}")
print(f"  apply(str.upper, 'hello') = {apply(str.upper, 'hello')}")
print(f"  apply(abs, -42) = {apply(abs, -42)}")
print()

# =============================
# 2. CUSTOM HIGHER-ORDER FUNCTIONS
# =============================

print("=== Custom Higher-Order Functions ===")
print()

def apply_to_each(func, items):
    """Apply a function to each item and return results."""
    return [func(item) for item in items]

numbers = [1, -2, 3, -4, 5]

# Different functions, same structure
abs_values = apply_to_each(abs, numbers)
squared = apply_to_each(lambda x: x ** 2, numbers)
as_strings = apply_to_each(str, numbers)

print(f"  numbers:    {numbers}")
print(f"  abs values: {abs_values}")
print(f"  squared:    {squared}")
print(f"  as strings: {as_strings}")
print()

# =============================
# 3. FUNCTIONS RETURNING FUNCTIONS
# =============================

print("=== Functions Returning Functions ===")
print()

def make_adder(n):
    """Return a function that adds n to its argument."""
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
add100 = make_adder(100)

print(f"  add5(10) = {add5(10)}")
print(f"  add5(20) = {add5(20)}")
print(f"  add100(10) = {add100(10)}")
print()

# =============================
# 4. FUNCTION FACTORIES
# =============================

print("=== Function Factories ===")
print()

def make_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
times_ten = make_multiplier(10)

value = 7
print(f"  double({value}) = {double(value)}")
print(f"  triple({value}) = {triple(value)}")
print(f"  times_ten({value}) = {times_ten(value)}")
print()

# Using the factory in a loop
multipliers = [make_multiplier(i) for i in range(1, 6)]
for i, m in enumerate(multipliers, 1):
    print(f"  ×{i}(10) = {m(10)}")
print()

# =============================
# 5. MAKE VALIDATOR FACTORY
# =============================

print("=== Validator Factory ===")
print()

def make_range_validator(min_val, max_val):
    """Return a function that checks if a value is in range."""
    def validator(value):
        return min_val <= value <= max_val
    return validator

is_valid_age = make_range_validator(0, 150)
is_valid_score = make_range_validator(0, 100)
is_valid_temp = make_range_validator(-50, 60)

print(f"  is_valid_age(25) = {is_valid_age(25)}")
print(f"  is_valid_age(200) = {is_valid_age(200)}")
print(f"  is_valid_score(85) = {is_valid_score(85)}")
print(f"  is_valid_score(110) = {is_valid_score(110)}")
print(f"  is_valid_temp(37) = {is_valid_temp(37)}")
print()

# =============================
# 6. HIGHER-ORDER WITH MULTIPLE FUNCTIONS
# =============================

print("=== Applying Multiple Functions ===")
print()

def apply_all(functions, value):
    """Apply each function to the value and return all results."""
    return [func(value) for func in functions]

transformations = [
    str.upper,
    str.lower,
    str.title,
    str.swapcase,
    len,
]

text = "Hello World"
results = apply_all(transformations, text)

for func, result in zip(transformations, results):
    name = getattr(func, '__name__', str(func))
    print(f"  {name}('{text}') = {result}")
print()

# =============================
# 7. CONDITIONAL FUNCTION SELECTION
# =============================

print("=== Conditional Function Selection ===")
print()

def get_operation(operator):
    """Return the appropriate function for an operator."""
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else "Error: Division by zero",
    }
    return operations.get(operator, lambda a, b: "Unknown operator")

# Use it like a simple calculator
expressions = [(10, "+", 3), (10, "-", 3), (10, "*", 3), (10, "/", 3)]

for a, op, b in expressions:
    func = get_operation(op)
    result = func(a, b)
    print(f"  {a} {op} {b} = {result}")
print()

# =============================
# 8. RETRY WRAPPER
# =============================

print("=== Higher-Order: Retry Wrapper ===")
print()

def with_retry(func, max_attempts=3):
    """Return a version of func that retries on failure."""
    def wrapper(*args, **kwargs):
        for attempt in range(1, max_attempts + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"    Attempt {attempt} failed: {e}")
                if attempt == max_attempts:
                    print(f"    All {max_attempts} attempts failed!")
                    raise
    return wrapper

# Simulating a flaky function
call_count = 0

def flaky_function(x):
    """Fails the first 2 calls, succeeds on 3rd."""
    global call_count
    call_count += 1
    if call_count < 3:
        raise ValueError(f"Not ready yet (call #{call_count})")
    return x * 2

safe_function = with_retry(flaky_function, max_attempts=3)
result = safe_function(21)
print(f"  Final result: {result}")
print()

# =============================
# 9. BUILT-IN HIGHER-ORDER FUNCTIONS
# =============================

print("=== Built-in Higher-Order Functions ===")
print()

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sorted() — takes a key function
print(f"  sorted: {sorted(numbers)}")
print(f"  sorted(reverse): {sorted(numbers, reverse=True)}")
print(f"  sorted(key=neg): {sorted(numbers, key=lambda x: -x)}")
print()

# map(), filter() — already covered
print(f"  map(str, [1,2,3]): {list(map(str, [1, 2, 3]))}")
print(f"  filter(bool, [0,1,'',2]): {list(filter(bool, [0, 1, '', 2]))}")
print()

# max/min with key
words = ["python", "is", "awesome"]
print(f"  Longest word: {max(words, key=len)}")
print(f"  Shortest word: {min(words, key=len)}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a function factory that creates power functions
#    (square, cube, etc.)
# 2. Write a higher-order function that takes a predicate
#    and returns a function that counts matches in a list
# 3. Create a "make_formatter" that returns functions
#    to format numbers (currency, percentage, etc.)
# ============================================
