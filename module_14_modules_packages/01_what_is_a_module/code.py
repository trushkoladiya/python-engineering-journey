# ============================================
# MODULE 14 - SUBTOPIC 1: What is a Module?
# ============================================

# A module is simply a .py file containing Python code.
# Any .py file you create is automatically a module.

# =============================
# 1. CONCEPT: A FILE IS A MODULE
# =============================

# --- Example 1: This file itself is a module ---
print("=== This File is a Module ===")
print()

# Every Python file has a special attribute: __name__
print(f"  This module's name: {__name__}")
print(f"  (When run directly, __name__ is '__main__')")
print()

# Every module also has a __file__ attribute when loaded
# but when running directly, we can check it differently

# =============================
# 2. WHAT CAN A MODULE CONTAIN?
# =============================

# --- Example 2: Modules can contain variables, functions, classes ---
print("=== Module Contents ===")
print()

# A module can contain variables
module_version = "1.0"
author = "Trush"

# A module can contain functions
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# A module can contain classes
class Tool:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Tool: {self.name}"

# Let's use them
print(f"  Version: {module_version}")
print(f"  Author: {author}")
print(f"  greet('Trush'): {greet('Trush')}")
print(f"  add(10, 20): {add(10, 20)}")
print(f"  Tool('Hammer'): {Tool('Hammer')}")
print()

# =============================
# 3. WHY USE MODULES?
# =============================

# --- Example 3: Without modules (everything in one place) ---
print("=== Why Modules Matter ===")
print()

# Imagine putting ALL this code in one file:
# - 50 utility functions
# - 20 classes
# - 100 constants
# - Database code, UI code, logic code...
# → IMPOSSIBLE to manage!

# With modules:
# - utils.py       → utility functions
# - models.py      → classes
# - constants.py   → constants
# - database.py    → database code
# - main.py        → ties everything together

print("  Without modules: ONE giant messy file")
print("  With modules:    Multiple organized files")
print()

# =============================
# 4. MODULES YOU ALREADY KNOW
# =============================

# --- Example 4: Built-in modules ---
print("=== Built-in Modules (You've Seen These) ===")
print()

# These are all modules that come with Python
import math
import random
import os

print(f"  math.pi = {math.pi}")
print(f"  random.randint(1, 10) = {random.randint(1, 10)}")
print(f"  os.name = {os.name}")
print()

# Each of these is a .py file (or C extension) somewhere in Python's install

# =============================
# 5. A MODULE IS JUST A NAMESPACE
# =============================

# --- Example 5: Modules group related names together ---
print("=== Module as a Namespace ===")
print()

# When you import math, you get a NAMESPACE
# that contains: math.pi, math.sqrt, math.ceil, etc.

# This prevents name clashes:
# Your code might have a function called sqrt()
# math also has sqrt()
# No conflict because they're in different namespaces!

def sqrt(n):
    """Our own sqrt — just returns a message."""
    return f"Custom sqrt called with {n}"

print(f"  Our sqrt(16): {sqrt(16)}")
print(f"  math.sqrt(16): {math.sqrt(16)}")
print("  → No conflict! Different namespaces.")
print()

# =============================
# 6. CHECKING MODULE TYPE
# =============================

# --- Example 6: A module is a Python object ---
print("=== Module is an Object ===")
print()

print(f"  type(math) = {type(math)}")
print(f"  type(random) = {type(random)}")
print(f"  type(os) = {type(os)}")
print()

# You can even check what's inside a module
print("  First 10 items in math module:")
math_contents = [item for item in dir(math) if not item.startswith("_")]
for item in math_contents[:10]:
    print(f"    - {item}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a file called mytools.py with a few functions
# 2. Import it from another file and use those functions
# 3. Use dir() on any imported module to see its contents
# ============================================
