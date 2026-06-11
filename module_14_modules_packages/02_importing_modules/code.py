# ============================================
# MODULE 14 - SUBTOPIC 2: Importing Modules
# ============================================

# Python has three main ways to import modules.
# Each has different behavior and tradeoffs.

# =============================
# 1. import module_name
# =============================

# --- Example 1: Full module import ---
print("=== import module_name ===")
print()

import math

# Access everything using dot notation
print(f"  math.pi = {math.pi}")
print(f"  math.e = {math.e}")
print(f"  math.sqrt(144) = {math.sqrt(144)}")
print(f"  math.ceil(3.2) = {math.ceil(3.2)}")
print(f"  math.floor(3.8) = {math.floor(3.8)}")
print()

# Advantage: clear where each name comes from
# math.sqrt → clearly from the math module

# =============================
# 2. from module_name import name
# =============================

# --- Example 2: Selective import ---
print("=== from module_name import name ===")
print()

from random import randint, choice, shuffle

# Now use directly — no prefix needed
print(f"  randint(1, 100) = {randint(1, 100)}")
print(f"  choice(['a', 'b', 'c']) = {choice(['a', 'b', 'c'])}")

my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(f"  shuffle([1,2,3,4,5]) = {my_list}")
print()

# Advantage: shorter code, no prefix
# Disadvantage: less clear where the name came from

# =============================
# 3. from module_name import *
# =============================

# --- Example 3: Wildcard import (DANGEROUS) ---
print("=== from module_name import * (Dangerous!) ===")
print()

# Let's demonstrate WHY this is dangerous

# Suppose we have a variable called 'log'
log = "My application log"
print(f"  Before wildcard import: log = '{log}'")

from math import *

# Now 'log' has been OVERWRITTEN by math.log!
print(f"  After 'from math import *': log = {log}")
print(f"  Our variable was DESTROYED!")
print()

# This happened silently — no warning, no error
# In a large codebase, this causes very hard-to-find bugs

# =============================
# 4. COMPARING ALL THREE APPROACHES
# =============================

# --- Example 4: Same task, three ways ---
print("=== Comparison: Three Import Styles ===")
print()

# Way 1: import module
import math
result1 = math.factorial(5)
print(f"  import math → math.factorial(5) = {result1}")

# Way 2: from module import name
from math import factorial
result2 = factorial(5)
print(f"  from math import factorial → factorial(5) = {result2}")

# Way 3: from module import * (already done above)
# factorial is already available from the wildcard import
result3 = factorial(5)
print(f"  from math import * → factorial(5) = {result3}")
print()

# =============================
# 5. IMPORTING MULTIPLE ITEMS
# =============================

# --- Example 5: Import several names at once ---
print("=== Importing Multiple Items ===")
print()

from os.path import exists, join, dirname, basename

# Use all of them directly
test_path = "/home/user/documents/report.pdf"
print(f"  Path: {test_path}")
print(f"  dirname:  {dirname(test_path)}")
print(f"  basename: {basename(test_path)}")
print()

# For many imports, use parentheses for readability
from math import (
    sqrt,
    ceil,
    floor,
    pow
)

print(f"  sqrt(25) = {sqrt(25)}")
print(f"  ceil(4.1) = {ceil(4.1)}")
print(f"  floor(4.9) = {floor(4.9)}")
print()

# =============================
# 6. IMPORT DOES NOT RELOAD
# =============================

# --- Example 6: Importing the same module twice ---
print("=== Import is Cached ===")
print()

import math
import math   # Python does NOT reload — uses cached version

# This is efficient! Python loads each module only once.
print("  'import math' twice → loaded only ONCE (cached)")
print(f"  id(math) is the same: {id(math)}")
print()

# =============================
# 7. PRACTICAL GUIDELINES
# =============================

print("=== When to Use Which ===")
print()
print("  ✅ import module_name")
print("     → When using many things from the module")
print("     → Clearest and safest approach")
print()
print("  ✅ from module import name")
print("     → When using only a few specific names")
print("     → Makes code shorter")
print()
print("  ❌ from module import *")
print("     → Almost never in production code")
print("     → Causes silent name clashes")
print("     → Makes debugging harder")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Import 'datetime' module and print today's date
# 2. Import only 'choice' from random and pick from a list
# 3. Try 'from os import *' and see what names appear
# ============================================
