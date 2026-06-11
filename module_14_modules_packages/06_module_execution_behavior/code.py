# ============================================
# MODULE 14 - SUBTOPIC 6: Module Execution Behavior
# ============================================

# Every module has a __name__ variable.
# Its value depends on HOW the module is run.

# =============================
# 1. CHECKING __name__
# =============================

print("=== __name__ Variable ===")
print()

# When run directly: __name__ == "__main__"
# When imported:     __name__ == "module_name"

print(f"  __name__ = '{__name__}'")
print(f"  This file was run {'directly' if __name__ == '__main__' else 'as an import'}")
print()

# =============================
# 2. THE MAIN GUARD PATTERN
# =============================

print("=== The if __name__ == '__main__' Pattern ===")
print()

# Functions that could be imported
def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def factorial(n):
    """Calculate factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# This code ONLY runs when the file is executed directly
if __name__ == "__main__":
    # Test/demo code goes here
    print("  Running tests (only when executed directly):")
    print(f"    add(3, 4) = {add(3, 4)}")
    print(f"    multiply(5, 6) = {multiply(5, 6)}")
    print(f"    factorial(5) = {factorial(5)}")
    print()

# =============================
# 3. WITHOUT THE GUARD (BAD)
# =============================

print("=== Without Guard (Problem Demo) ===")
print()

# Imagine this code WITHOUT the guard:
#
#   # bad_module.py
#   def greet(name):
#       return f"Hello, {name}!"
#
#   # This runs EVERY time the module is imported!
#   print("Module loaded!")
#   print(greet("World"))
#
# If someone does 'import bad_module', they get unwanted output!

print("  Without guard: code runs on import (bad)")
print("  With guard: code only runs when intended (good)")
print()

# =============================
# 4. PRACTICAL: DUAL-PURPOSE FILE
# =============================

print("=== Dual-Purpose Module ===")
print()

# This file works as BOTH a module AND a script

class Temperature:
    """Temperature converter — can be imported or run directly."""

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32

    @property
    def kelvin(self):
        return self.celsius + 273.15

    def __str__(self):
        return f"{self.celsius}°C = {self.fahrenheit}°F = {self.kelvin}K"

# When imported: user gets Temperature class
# When run directly: show demo

if __name__ == "__main__":
    temps = [0, 20, 37, 100]
    print("  Temperature conversions:")
    for t in temps:
        print(f"    {Temperature(t)}")
    print()

# =============================
# 5. CHECKING OTHER MODULES' __name__
# =============================

print("=== Other Modules' __name__ ===")
print()

import math
import random
import os

print(f"  math.__name__ = '{math.__name__}'")
print(f"  random.__name__ = '{random.__name__}'")
print(f"  os.__name__ = '{os.__name__}'")
print(f"  This file's __name__ = '{__name__}'")
print()

# Notice: imported modules have their FILENAME as __name__
# Only the file you RUN directly has __name__ == "__main__"

# =============================
# 6. REAL-WORLD MODULE PATTERN
# =============================

print("=== Real-World Module Structure ===")
print()

# A well-structured module looks like this:
#
#   """Module docstring — what this module does."""
#   
#   # Imports at the top
#   import os
#   import sys
#   
#   # Constants
#   VERSION = "1.0"
#   
#   # Functions/Classes
#   def main_function():
#       ...
#   
#   class MainClass:
#       ...
#   
#   # Main guard at the bottom
#   if __name__ == "__main__":
#       # Demo / test / CLI code
#       main_function()

print("  Standard module layout:")
print("    1. Docstring")
print("    2. Imports")
print("    3. Constants")
print("    4. Functions & Classes")
print("    5. if __name__ == '__main__':")
print()

# =============================
# 7. SCRIPT WITH ARGUMENTS
# =============================

print("=== Script Mode with sys.argv ===")
print()

import sys

if __name__ == "__main__":
    print(f"  Script name: {sys.argv[0]}")
    print(f"  Arguments: {sys.argv[1:]}")
    print()

    # You could process command line arguments here:
    # python code.py arg1 arg2
    # sys.argv would be ['code.py', 'arg1', 'arg2']

    if len(sys.argv) > 1:
        print(f"  You passed: {', '.join(sys.argv[1:])}")
    else:
        print("  No extra arguments passed.")
    print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a module with functions AND a __main__ guard
# 2. Run it directly — see the test output
# 3. Import it from another file — test output should NOT appear
# ============================================
