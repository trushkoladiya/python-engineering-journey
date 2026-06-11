# ============================================
# MODULE 10 - SUBTOPIC 4: Reading Files
# ============================================

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Setup: Create a test file ---
filepath = os.path.join(SCRIPT_DIR, "sample.txt")
with open(filepath, "w") as f:
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Python is great.\n")
    f.write("Line 3: File handling rocks!\n")
    f.write("Line 4: Keep learning.\n")
    f.write("Line 5: The end.\n")

# =============================
# 1. read() — ENTIRE FILE
# =============================

# --- Example 1: Read everything at once ---
with open(filepath, "r") as file:
    content = file.read()

print("read() — entire file:")
print(content)

# --- Example 2: Read specific number of characters ---
with open(filepath, "r") as file:
    first_20 = file.read(20)    # First 20 characters
    next_20 = file.read(20)     # Next 20 characters

print("Partial read:")
print(f"  First 20: '{first_20}'")
print(f"  Next 20:  '{next_20}'")

# =============================
# 2. readline() — ONE LINE AT A TIME
# =============================

# --- Example 3: Read line by line ---
with open(filepath, "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()

print(f"\nreadline():")
print(f"  Line 1: {line1}", end="")
print(f"  Line 2: {line2}", end="")
print(f"  Line 3: {line3}", end="")

# --- Example 4: Read all lines with a loop ---
print(f"\nAll lines with readline loop:")
with open(filepath, "r") as file:
    line = file.readline()
    while line:
        print(f"  {line.strip()}")
        line = file.readline()

# =============================
# 3. readlines() — ALL LINES AS A LIST
# =============================

# --- Example 5: Get a list of lines ---
with open(filepath, "r") as file:
    lines = file.readlines()

print(f"\nreadlines():")
print(f"  Type: {type(lines)}")
print(f"  Count: {len(lines)} lines")
print(f"  Raw: {lines[:2]}...")

# --- Example 6: Process the list ---
print(f"\nProcessed lines:")
for i, line in enumerate(lines, 1):
    print(f"  {i}. {line.strip()}")

# =============================
# 4. ITERATING DIRECTLY (BEST WAY)
# =============================

# --- Example 7: for line in file (memory efficient) ---
print(f"\nDirect iteration:")
with open(filepath, "r") as file:
    for line in file:
        print(f"  → {line.strip()}")

# --- Example 8: Using enumerate ---
print(f"\nWith line numbers:")
with open(filepath, "r") as file:
    for num, line in enumerate(file, 1):
        print(f"  [{num}] {line.strip()}")

# =============================
# 5. FILE POINTER BEHAVIOR
# =============================

# --- Example 9: Pointer moves after reading ---
with open(filepath, "r") as file:
    first_read = file.read()
    second_read = file.read()   # Empty — pointer at end!

print(f"\nFile pointer:")
print(f"  First read length: {len(first_read)}")
print(f"  Second read length: {len(second_read)}")   # 0!
print(f"  Second read empty because pointer reached the end")

# =============================
# 6. STRIPPING NEWLINES
# =============================

# --- Example 10: strip() removes trailing whitespace/newlines ---
with open(filepath, "r") as file:
    lines = file.readlines()

print(f"\nWith and without strip():")
print(f"  Raw:     {repr(lines[0])}")
print(f"  Stripped: {repr(lines[0].strip())}")

# --- Example 11: List comprehension to clean lines ---
with open(filepath, "r") as file:
    clean_lines = [line.strip() for line in file]

print(f"\nClean lines: {clean_lines}")

# =============================
# CLEANUP
# =============================
os.remove(filepath)
print("\n✓ Temp file cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Create a file and read it with all three methods
# 2. Count the number of words in a file
# 3. Find the longest line in a file
# ============================================
