# ============================================
# MODULE 14 - SUBTOPIC 5: Creating Custom Modules
# ============================================

# You can create your own modules by writing .py files.
# This example simulates the concept since we're in a single file.

# =============================
# 1. CONCEPT: YOUR OWN MODULE
# =============================

print("=== Creating Custom Modules ===")
print()

# Imagine you create a file called 'mymath.py' with these contents:
#
#   # mymath.py
#   PI = 3.14159
#   
#   def add(a, b):
#       return a + b
#   
#   def square(n):
#       return n ** 2
#
# Then in main.py:
#   import mymath
#   print(mymath.add(3, 4))  → 7

print("  A module is just a .py file you write.")
print("  Import it by filename (without .py)")
print()

# =============================
# 2. SIMULATING A MODULE IN CODE
# =============================

# --- Example 1: Functions that WOULD go in a module ---
print("=== Functions for a 'validators' Module ===")
print()

# These would normally be in validators.py
def is_positive(n):
    """Check if number is positive."""
    return n > 0

def is_even(n):
    """Check if number is even."""
    return n % 2 == 0

def is_non_empty(text):
    """Check if string is non-empty."""
    return len(text.strip()) > 0

def is_valid_age(age):
    """Check if age is reasonable."""
    return 0 <= age <= 150

# Using them (as if imported from validators.py)
print(f"  is_positive(5): {is_positive(5)}")
print(f"  is_positive(-3): {is_positive(-3)}")
print(f"  is_even(4): {is_even(4)}")
print(f"  is_even(7): {is_even(7)}")
print(f"  is_non_empty('hello'): {is_non_empty('hello')}")
print(f"  is_non_empty('   '): {is_non_empty('   ')}")
print(f"  is_valid_age(25): {is_valid_age(25)}")
print(f"  is_valid_age(200): {is_valid_age(200)}")
print()

# =============================
# 3. GROUPING RELATED CLASSES
# =============================

# --- Example 2: Classes that WOULD go in a module ---
print("=== Classes for a 'shapes' Module ===")
print()

# These would normally be in shapes.py
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius})"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

# Using them
c = Circle(5)
r = Rectangle(4, 6)
print(f"  {c} → area = {c.area():.2f}")
print(f"  {r} → area = {r.area()}")
print()

# =============================
# 4. ACTUALLY CREATING AND IMPORTING A MODULE
# =============================

# --- Example 3: Creating a real module file ---
print("=== Creating a Real Module File ===")
print()

import os
import tempfile
import sys

# Create a temporary module file
module_dir = tempfile.mkdtemp()
module_path = os.path.join(module_dir, "greetings.py")

# Write module content
module_code = '''
# greetings.py — A custom module

DEFAULT_GREETING = "Hello"

def greet(name):
    return f"{DEFAULT_GREETING}, {name}!"

def farewell(name):
    return f"Goodbye, {name}! See you soon."

def formal_greet(name, title="Mr."):
    return f"Good day, {title} {name}."
'''

with open(module_path, "w") as f:
    f.write(module_code)

print(f"  Created module at: {module_path}")

# Add the directory to Python's path so we can import it
sys.path.insert(0, module_dir)

# Now import and use it!
import greetings

print(f"  greetings.DEFAULT_GREETING = '{greetings.DEFAULT_GREETING}'")
print(f"  greetings.greet('Trush') = '{greetings.greet('Trush')}'")
print(f"  greetings.farewell('Rahul') = '{greetings.farewell('Rahul')}'")
print(f"  greetings.formal_greet('Smith') = '{greetings.formal_greet('Smith')}'")
print()

# Cleanup
import shutil
sys.path.remove(module_dir)
shutil.rmtree(module_dir)

# =============================
# 5. MODULE WITH CONSTANTS
# =============================

# --- Example 4: Constants module pattern ---
print("=== Constants Module Pattern ===")
print()

# In real projects, you might have a constants.py:
#
#   # constants.py
#   MAX_RETRIES = 3
#   TIMEOUT_SECONDS = 30
#   API_VERSION = "v2"
#   SUPPORTED_FORMATS = ["json", "xml", "csv"]

# Simulated usage:
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30
API_VERSION = "v2"
SUPPORTED_FORMATS = ["json", "xml", "csv"]

print(f"  MAX_RETRIES = {MAX_RETRIES}")
print(f"  TIMEOUT_SECONDS = {TIMEOUT_SECONDS}")
print(f"  API_VERSION = '{API_VERSION}'")
print(f"  SUPPORTED_FORMATS = {SUPPORTED_FORMATS}")
print()

# =============================
# 6. WHAT GETS EXPORTED?
# =============================

# --- Example 5: Everything at module level is accessible ---
print("=== What Gets Exported ===")
print()

# When you import a module, ALL top-level names are accessible:
# - Variables
# - Functions
# - Classes
# - Other imports

# Convention: prefix "private" names with underscore
# They're still accessible, but signal "don't use this"

_internal_counter = 0    # convention: "private"
public_version = "1.0"   # convention: "public"

def _helper():           # convention: "private"
    return "internal use only"

def public_api():        # convention: "public"
    return "use this!"

print(f"  public_version = '{public_version}'")
print(f"  public_api() = '{public_api()}'")
print(f"  _internal_counter = {_internal_counter} (private by convention)")
print(f"  _helper() = '{_helper()}' (private by convention)")
print("  → Underscore prefix = 'please don't use from outside'")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a file called 'utils.py' with 3 helper functions
# 2. Create a 'constants.py' with project settings
# 3. Import them in a main.py and use the functions
# ============================================
