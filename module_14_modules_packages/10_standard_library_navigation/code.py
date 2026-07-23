# ============================================
# MODULE 14 - SUBTOPIC 10: Standard Library Navigation
# ============================================

# Python's standard library is huge. Learn to explore it.

# =============================
# 1. dir() — LIST MODULE CONTENTS
# =============================

print("=== dir() — Exploring a Module ===")
print()

import json

# dir() lists all names in a module
all_names = dir(json)
public_names = [n for n in all_names if not n.startswith("_")]

print(f"  json module has {len(all_names)} names total")
print(f"  {len(public_names)} public names:")
for name in public_names:
    print(f"    - {name}")
print()

# =============================
# 2. type() AND callable() — UNDERSTAND CONTENTS
# =============================

print("=== Understanding Module Contents ===")
print()

import math

# Check what each item IS
items_to_check = ["pi", "e", "sqrt", "ceil", "inf", "nan"]

for item_name in items_to_check:
    item = getattr(math, item_name)
    is_callable = callable(item)
    print(f"  math.{item_name:8s} → type={type(item).__name__:10s} callable={is_callable}")
print()

# =============================
# 3. help() — READ DOCUMENTATION
# =============================

print("=== help() — Reading Docs ===")
print()

# help() shows the docstring and signature
# We'll capture it as a string for cleaner output

import io
import contextlib

# Get help text for json.dumps
help_text = io.StringIO()
with contextlib.redirect_stdout(help_text):
    help(json.dumps)

# Show first few lines
lines = help_text.getvalue().split("\n")
print("  help(json.dumps) — first 8 lines:")
for line in lines[:8]:
    print(f"    {line}")
print("    ...")
print()

# =============================
# 4. __doc__ — QUICK DOCSTRING
# =============================

print("=== __doc__ — Quick Documentation ===")
print()

# Every module and function has a __doc__ attribute
print(f"  math.__doc__:")
if math.__doc__:
    for line in math.__doc__.split("\n")[:3]:
        print(f"    {line}")
print()

print(f"  json.dumps.__doc__ (first line):")
if json.dumps.__doc__:
    print(f"    {json.dumps.__doc__.split(chr(10))[0]}")
print()

# =============================
# 5. CHECKING IF A MODULE EXISTS
# =============================

print("=== Checking Module Availability ===")
print()

import importlib.util

modules_to_check = ["json", "csv", "numpy", "requests", "math", "flask", "os"]

for mod_name in modules_to_check:
    spec = importlib.util.find_spec(mod_name)
    status = "✅ Available" if spec else "❌ Not installed"
    print(f"  {mod_name:12s} → {status}")
print()

# =============================
# 6. EXPLORING USEFUL STANDARD LIBRARY MODULES
# =============================

print("=== Useful Standard Library Modules ===")
print()

# --- json: Read/Write JSON ---
print("  --- json ---")
import json

data = {"name": "Trush", "age": 21, "hobbies": ["reading", "coding"]}
json_str = json.dumps(data, indent=2)
print(f"  json.dumps: {json_str[:50]}...")

parsed = json.loads('{"key": "value", "num": 42}')
print(f"  json.loads: {parsed}")
print()

# --- csv: Read/Write CSV ---
print("  --- csv ---")
import csv
import io

csv_data = "name,age,city\nTrush,21,NYC\nRahul,22,LA"
reader = csv.DictReader(io.StringIO(csv_data))
for row in reader:
    print(f"  {dict(row)}")
print()

# --- copy: Deep and Shallow Copy ---
print("  --- copy ---")
import copy

original = {"name": "Trush", "scores": [90, 85, 92]}
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original["scores"].append(100)
print(f"  original: {original}")
print(f"  shallow (shares list!): {shallow}")
print(f"  deep (independent): {deep}")
print()

# --- pprint: Pretty Printing ---
print("  --- pprint ---")
from pprint import pformat

complex_data = {
    "users": [
        {"name": "Trush", "role": "admin"},
        {"name": "Rahul", "role": "user"},
    ],
    "settings": {"theme": "dark", "language": "en"},
}
print(f"  pformat output:")
for line in pformat(complex_data).split("\n"):
    print(f"    {line}")
print()

# --- pathlib: Modern Path Handling ---
print("  --- pathlib ---")
from pathlib import Path

p = Path("/home/user/documents/report.txt")
print(f"  Path: {p}")
print(f"  Name: {p.name}")
print(f"  Stem: {p.stem}")
print(f"  Suffix: {p.suffix}")
print(f"  Parent: {p.parent}")
print()

# =============================
# 7. COUNTING THE STANDARD LIBRARY
# =============================

print("=== How Big is the Standard Library? ===")
print()

# Count available built-in modules
import sys

builtin_count = len(sys.builtin_module_names)
print(f"  Built-in (C) modules: {builtin_count}")
print(f"  First 10: {list(sys.builtin_module_names)[:10]}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Use dir() to explore the 'string' module
# 2. Use help() on collections.Counter
# 3. Try importing and exploring 'textwrap' module
# 4. Use pathlib.Path to analyze a file path
# ============================================
