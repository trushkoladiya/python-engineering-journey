# ============================================
# MODULE 14 - SUBTOPIC 3: Module Usage Patterns
# ============================================

# Different ways to access and use module contents.

# =============================
# 1. DOT NOTATION
# =============================

# --- Example 1: Accessing module contents with dots ---
print("=== Dot Notation ===")
print()

import math

# Variables
print(f"  math.pi = {math.pi}")
print(f"  math.e = {math.e}")
print(f"  math.inf = {math.inf}")

# Functions
print(f"  math.sqrt(64) = {math.sqrt(64)}")
print(f"  math.log(100) = {math.log(100)}")
print()

# The dot says: "look inside this module for this name"

# =============================
# 2. ALIASING MODULES WITH as
# =============================

# --- Example 2: Shortening module names ---
print("=== Module Aliasing ===")
print()

import math as m
import random as rnd
import os as operating_system   # can be any name (but don't do this!)

print(f"  m.pi = {m.pi}")
print(f"  m.sqrt(25) = {m.sqrt(25)}")
print(f"  rnd.randint(1, 10) = {rnd.randint(1, 10)}")
print(f"  operating_system.name = {operating_system.name}")
print()

# --- Example 3: Common community conventions ---
print("=== Common Aliases (Community Standard) ===")
print()

# These are universally recognized aliases:
# import numpy as np        ← everyone uses np
# import pandas as pd       ← everyone uses pd
# import datetime as dt     ← common

import datetime as dt

now = dt.datetime.now()
print(f"  dt.datetime.now() = {now}")
print(f"  Using 'dt' is shorter than 'datetime'")
print()

# =============================
# 3. ALIASING SPECIFIC IMPORTS
# =============================

# --- Example 4: Renaming imported names ---
print("=== Name Aliasing ===")
print()

from math import factorial as fact
from math import gcd as greatest_common_divisor
from random import randint as random_number

print(f"  fact(6) = {fact(6)}")
print(f"  greatest_common_divisor(24, 36) = {greatest_common_divisor(24, 36)}")
print(f"  random_number(1, 50) = {random_number(1, 50)}")
print()

# =============================
# 4. RESOLVING NAME CLASHES
# =============================

# --- Example 5: Aliasing to avoid conflicts ---
print("=== Resolving Name Clashes ===")
print()

# Our own function
def sqrt(n):
    return f"Custom: approximate sqrt of {n} is {n ** 0.5:.1f}"

# Math module's function — renamed to avoid clash
from math import sqrt as math_sqrt

print(f"  Our sqrt(16): {sqrt(16)}")
print(f"  math_sqrt(16): {math_sqrt(16)}")
print("  → Both work, no conflict!")
print()

# =============================
# 5. SELECTIVE IMPORTS
# =============================

# --- Example 6: Import only what you need ---
print("=== Selective Imports ===")
print()

from os.path import exists, getsize, isfile, isdir

# Only these 4 names are available
# The rest of os.path is NOT imported
test_file = __file__   # path to this script
print(f"  Checking: {test_file}")
print(f"  exists?  {exists(test_file)}")
print(f"  isfile?  {isfile(test_file)}")
print(f"  isdir?   {isdir(test_file)}")
if exists(test_file):
    print(f"  size:    {getsize(test_file)} bytes")
print()

# =============================
# 6. CHAINING MODULE ACCESS
# =============================

# --- Example 7: Accessing submodules and nested attributes ---
print("=== Chained Access ===")
print()

import os.path

# Chain of dots: module → submodule → function
home = os.path.expanduser("~")
print(f"  os.path.expanduser('~') = {home}")
print(f"  os.path.sep = '{os.path.sep}'")
print()

# =============================
# 7. CHECKING WHAT'S AVAILABLE
# =============================

# --- Example 8: Using dir() and help() ---
print("=== Exploring Module Contents ===")
print()

import string

# dir() shows all names in a module
public_items = [name for name in dir(string) if not name.startswith("_")]
print(f"  Public items in 'string' module:")
for item in public_items:
    value = getattr(string, item)
    if isinstance(value, str) and len(value) < 50:
        print(f"    {item} = '{value}'")
    else:
        print(f"    {item} = {type(value).__name__}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Import the 'collections' module as 'col' and use col.Counter
# 2. Import 'choice' from random as 'pick' and use it
# 3. Use dir() to explore the 'sys' module
# ============================================
