# ============================================
# MODULE 8 - SUBTOPIC 10: Documentation & Annotations
# ============================================

# =============================
# 1. BASIC DOCSTRINGS
# =============================

# --- Example 1: One-line docstring ---
def add(a, b):
    """Return the sum of a and b."""
    return a + b

print("add(3, 5) =", add(3, 5))
print("Docstring:", add.__doc__)

# --- Example 2: Another simple docstring ---
def is_even(n):
    """Check if a number is even. Returns True or False."""
    return n % 2 == 0

print(f"\nis_even(4): {is_even(4)}")
print(f"Docstring: {is_even.__doc__}")

# =============================
# 2. MULTI-LINE DOCSTRINGS
# =============================

# --- Example 3: Detailed docstring ---
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area (length * width)
    """
    return length * width

print(f"\nArea: {calculate_area(5, 3)}")
print(f"Docstring:\n{calculate_area.__doc__}")

# --- Example 4: Docstring with examples ---
def fahrenheit_to_celsius(f):
    """
    Convert temperature from Fahrenheit to Celsius.

    Formula: (F - 32) * 5/9

    Examples:
        fahrenheit_to_celsius(32)  → 0.0
        fahrenheit_to_celsius(212) → 100.0
    """
    return (f - 32) * 5 / 9

print(f"\n32°F = {fahrenheit_to_celsius(32):.1f}°C")
print(f"212°F = {fahrenheit_to_celsius(212):.1f}°C")

# =============================
# 3. USING help()
# =============================

# --- Example 5: help() shows the docstring ---
def greet(name):
    """Print a friendly greeting for the given name."""
    print(f"Hello, {name}!")

print("\nUsing help():")
help(greet)

# =============================
# 4. TYPE HINTS — PARAMETERS
# =============================

# --- Example 6: Basic type hints ---
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

print(f"\nmultiply(3, 4) = {multiply(3, 4)}")

# --- Example 7: String type hint ---
def make_greeting(name: str, greeting: str = "Hello") -> str:
    """Create a greeting message."""
    return f"{greeting}, {name}!"

print(make_greeting("Trush"))
print(make_greeting("Rahul", "Hi"))

# --- Example 8: Various types ---
def describe_person(name: str, age: int, height: float) -> str:
    """Return a description of a person."""
    return f"{name} is {age} years old and {height:.1f}cm tall"

print(f"\n{describe_person('Trush', 21, 165.5)}")

# =============================
# 5. TYPE HINTS — RETURN TYPES
# =============================

# --- Example 9: Return bool ---
def is_adult(age: int) -> bool:
    """Check if person is an adult (18 or older)."""
    return age >= 18

print(f"\nis_adult(20): {is_adult(20)}")
print(f"is_adult(15): {is_adult(15)}")

# --- Example 10: Return None ---
def print_info(name: str, age: int) -> None:
    """Print person info. Returns nothing."""
    print(f"  {name}, age {age}")

print("\nPerson info:")
print_info("Trush", 21)

# --- Example 11: Return list ---
def get_evens(numbers: list) -> list:
    """Return a list of even numbers from the input."""
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

print(f"\nEvens: {get_evens([1, 2, 3, 4, 5, 6])}")

# =============================
# 6. TYPE HINTS ARE NOT ENFORCED
# =============================

# --- Example 12: Python doesn't enforce type hints ---
def add_typed(a: int, b: int) -> int:
    """Add two values."""
    return a + b

# These all work — Python doesn't check types!
print(f"\nInt: {add_typed(3, 5)}")
print(f"Float: {add_typed(3.5, 2.1)}")
print(f"String: {add_typed('Hello, ', 'World!')}")
print("Type hints are documentation, not enforcement")

# =============================
# 7. WELL-DOCUMENTED FUNCTION
# =============================

# --- Example 13: Complete example ---
def calculate_bmi(weight_kg: float, height_m: float) -> tuple:
    """
    Calculate BMI (Body Mass Index) and return category.

    Parameters:
        weight_kg: Weight in kilograms
        height_m: Height in meters

    Returns:
        Tuple of (bmi_value, category_string)
    """
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return round(bmi, 1), category

bmi, category = calculate_bmi(70, 1.75)
print(f"\nBMI: {bmi} ({category})")

bmi, category = calculate_bmi(90, 1.70)
print(f"BMI: {bmi} ({category})")

# ============================================
# TRY IT YOURSELF:
# 1. Add a docstring to a function you wrote earlier
# 2. Create a function with type hints for all parameters
# 3. Use help() to view your function's documentation
# ============================================
