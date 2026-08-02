# ============================================
# MODULE 16 - SUBTOPIC 12: Partial Functions
# ============================================

# functools.partial lets you "freeze" some arguments
# of a function, creating a simpler version.

from functools import partial

# =============================
# 1. BASIC partial()
# =============================

print("=== Basic partial() ===")
print()

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

# Create specialized versions
double = partial(multiply, 2)       # a=2, b=?
triple = partial(multiply, 3)       # a=3, b=?
times_ten = partial(multiply, 10)   # a=10, b=?

print(f"  double(5) = {double(5)}")
print(f"  triple(5) = {triple(5)}")
print(f"  times_ten(5) = {times_ten(5)}")
print()

# =============================
# 2. partial() WITH KEYWORD ARGUMENTS
# =============================

print("=== partial() with Keyword Arguments ===")
print()

def power(base, exponent):
    """Raise base to exponent."""
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"  square(5) = {square(5)}")
print(f"  square(10) = {square(10)}")
print(f"  cube(3) = {cube(3)}")
print(f"  cube(4) = {cube(4)}")
print()

# =============================
# 3. partial() vs LAMBDA
# =============================

print("=== partial() vs Lambda ===")
print()

def add(a, b):
    return a + b

# Both achieve the same thing
add_10_partial = partial(add, 10)
add_10_lambda = lambda b: add(10, b)

print(f"  partial: add_10(5) = {add_10_partial(5)}")
print(f"  lambda:  add_10(5) = {add_10_lambda(5)}")
print()

# partial is more readable and preserves function info
print(f"  partial func: {add_10_partial.func.__name__}")
print(f"  partial args: {add_10_partial.args}")
print(f"  partial kwargs: {add_10_partial.keywords}")
print()

# =============================
# 4. partial() WITH BUILT-IN FUNCTIONS
# =============================

print("=== partial() with Built-in Functions ===")
print()

# Pre-configure int() to parse binary
parse_binary = partial(int, base=2)
parse_hex = partial(int, base=16)
parse_octal = partial(int, base=8)

print(f"  parse_binary('1010') = {parse_binary('1010')}")
print(f"  parse_binary('1111') = {parse_binary('1111')}")
print(f"  parse_hex('FF') = {parse_hex('FF')}")
print(f"  parse_hex('1A') = {parse_hex('1A')}")
print(f"  parse_octal('77') = {parse_octal('77')}")
print()

# =============================
# 5. partial() WITH sorted()
# =============================

print("=== partial() with sorted() ===")
print()

sort_desc = partial(sorted, reverse=True)
sort_by_len = partial(sorted, key=len)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
words = ["python", "is", "a", "great", "language"]

print(f"  sort_desc({numbers})")
print(f"    = {sort_desc(numbers)}")
print()
print(f"  sort_by_len({words})")
print(f"    = {sort_by_len(words)}")
print()

# =============================
# 6. partial() WITH print()
# =============================

print("=== partial() with print() ===")
print()

# Create specialized printers
debug = partial(print, "[DEBUG]")
info = partial(print, "[INFO]")
error = partial(print, "[ERROR]")

debug("Loading configuration...")
info("Server started on port 8080")
error("Connection timeout!")
print()

# Print with custom separator
csv_print = partial(print, sep=",")
csv_print("Name", "Age", "City")
csv_print("Trush", 21, "NYC")
csv_print("Rahul", 22, "LA")
print()

# =============================
# 7. partial() IN DATA PROCESSING
# =============================

print("=== Data Processing with partial() ===")
print()

def format_number(number, prefix="", suffix="", decimals=2):
    """Format a number with optional prefix and suffix."""
    return f"{prefix}{number:.{decimals}f}{suffix}"

# Create specialized formatters
format_price = partial(format_number, prefix="$", decimals=2)
format_percent = partial(format_number, suffix="%", decimals=1)
format_temp = partial(format_number, suffix="°C", decimals=1)

prices = [9.99, 24.5, 149.999]
percentages = [0.856, 0.234, 0.9123]
temps = [36.6, 38.5, 37.1]

print("  Prices:", [format_price(p) for p in prices])
print("  Percentages:", [format_percent(p * 100) for p in percentages])
print("  Temperatures:", [format_temp(t) for t in temps])
print()

# =============================
# 8. partial() WITH map() AND filter()
# =============================

print("=== partial() with map() and filter() ===")
print()

def is_greater_than(threshold, value):
    """Check if value is greater than threshold."""
    return value > threshold

# Create specialized filters
is_adult = partial(is_greater_than, 17)       # age > 17
is_passing = partial(is_greater_than, 59)     # score > 59
is_positive = partial(is_greater_than, 0)     # > 0

ages = [15, 22, 17, 30, 12, 18]
scores = [45, 72, 58, 91, 60, 33]
values = [-3, 0, 5, -1, 8, -2]

print(f"  ages {ages}")
print(f"  adults: {list(filter(is_adult, ages))}")
print()
print(f"  scores {scores}")
print(f"  passing: {list(filter(is_passing, scores))}")
print()
print(f"  values {values}")
print(f"  positive: {list(filter(is_positive, values))}")
print()

# =============================
# 9. BUILDING A TOOLKIT
# =============================

print("=== Building a Toolkit with partial() ===")
print()

def calculate(operation, a, b):
    """Perform a math operation."""
    ops = {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b != 0 else float("inf"),
    }
    return ops.get(operation, 0)

# Create specialized calculators
add = partial(calculate, "add")
sub = partial(calculate, "sub")
mul = partial(calculate, "mul")
div = partial(calculate, "div")

print(f"  add(10, 3) = {add(10, 3)}")
print(f"  sub(10, 3) = {sub(10, 3)}")
print(f"  mul(10, 3) = {mul(10, 3)}")
print(f"  div(10, 3) = {div(10, 3):.2f}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use partial to create format_date functions
#    for different date formats
# 2. Create partial-based validators (is_even, is_positive, etc.)
# 3. Use partial with map() to transform a list
#    of temperatures from C to F
# ============================================
