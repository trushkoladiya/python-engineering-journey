# ============================================
# MODULE 10 - SUBTOPIC 3: Closing Files
# ============================================

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================
# 1. MANUAL CLOSING
# =============================

# --- Example 1: Open, use, close ---
filepath = os.path.join(SCRIPT_DIR, "test_close.txt")

file = open(filepath, "w")
file.write("Hello from manual close!\n")
print(f"Before close: file.closed = {file.closed}")
file.close()
print(f"After close:  file.closed = {file.closed}")

# --- Example 2: Reading after close fails ---
file = open(filepath, "r")
content = file.read()
file.close()

try:
    file.read()   # ❌ Can't read a closed file!
except ValueError as e:
    print(f"\n✗ Reading closed file: {e}")

# =============================
# 2. THE with STATEMENT
# =============================

# --- Example 3: Automatic closing with 'with' ---
with open(filepath, "r") as file:
    content = file.read()
    print(f"\nInside 'with': closed = {file.closed}")

print(f"Outside 'with': closed = {file.closed}")   # Automatically closed!
print(f"Content: {content}", end="")

# --- Example 4: Writing with 'with' ---
filepath2 = os.path.join(SCRIPT_DIR, "test_with.txt")

with open(filepath2, "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

# File is closed and saved here
with open(filepath2, "r") as file:
    print(f"\nWritten with 'with':\n{file.read()}", end="")

# =============================
# 3. WHY with IS BETTER
# =============================

# --- Example 5: Without 'with' — error can leave file open ---
filepath3 = os.path.join(SCRIPT_DIR, "test_error.txt")

# Risky way:
file = open(filepath3, "w")
try:
    file.write("Some data\n")
    # Imagine an error happens here...
    # file.close() would be skipped!
finally:
    file.close()   # Need try/finally to be safe

print(f"\nManual close with try/finally: closed = {file.closed}")

# Safe way (same thing, much cleaner):
with open(filepath3, "w") as file:
    file.write("Some data\n")
    # Even if an error occurs, the file is closed automatically!

print(f"With statement: closed = {file.closed}")

# --- Example 6: 'with' handles errors gracefully ---
filepath4 = os.path.join(SCRIPT_DIR, "test_safe.txt")

with open(filepath4, "w") as file:
    file.write("Important data\n")

try:
    with open(filepath4, "r") as file:
        content = file.read()
        # Simulating an error
        result = int("not a number")
except ValueError:
    print(f"\nError occurred, but file is safely closed: {file.closed}")

# =============================
# 4. MULTIPLE FILES WITH with
# =============================

# --- Example 7: Open two files at once ---
file_a = os.path.join(SCRIPT_DIR, "file_a.txt")
file_b = os.path.join(SCRIPT_DIR, "file_b.txt")

# Write to both
with open(file_a, "w") as fa, open(file_b, "w") as fb:
    fa.write("Content A\n")
    fb.write("Content B\n")

# Read both
with open(file_a, "r") as fa, open(file_b, "r") as fb:
    print(f"\nMultiple files:")
    print(f"  File A: {fa.read()}", end="")
    print(f"  File B: {fb.read()}", end="")

# =============================
# CLEANUP
# =============================
for f in ["test_close.txt", "test_with.txt", "test_error.txt",
          "test_safe.txt", "file_a.txt", "file_b.txt"]:
    path = os.path.join(SCRIPT_DIR, f)
    if os.path.exists(path):
        os.remove(path)
print("\n✓ Temp files cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Open and close a file manually — check .closed
# 2. Rewrite the same code using 'with' — notice how much cleaner it is
# 3. Open two files simultaneously with a single 'with' statement
# ============================================
