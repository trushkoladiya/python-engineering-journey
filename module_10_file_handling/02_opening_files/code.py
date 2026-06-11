# ============================================
# MODULE 10 - SUBTOPIC 2: Opening Files
# ============================================

import os

# Get the directory of this script for creating temp files
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================
# 1. BASIC open() USAGE
# =============================

# --- Example 1: Write mode — creates a new file ---
filepath = os.path.join(SCRIPT_DIR, "example.txt")

file = open(filepath, "w")
file.write("Hello, World!\n")
file.write("This is a test file.\n")
file.close()
print(f"✓ Created file: {os.path.basename(filepath)}")

# --- Example 2: Read mode — open existing file ---
file = open(filepath, "r")
content = file.read()
file.close()
print(f"\nContent:\n{content}")

# =============================
# 2. FILE MODES DEMONSTRATION
# =============================

# --- Example 3: Write mode ('w') — overwrites! ---
filepath_w = os.path.join(SCRIPT_DIR, "write_test.txt")

# First write
file = open(filepath_w, "w")
file.write("First write\n")
file.close()

# Second write — OVERWRITES the first!
file = open(filepath_w, "w")
file.write("Second write — first content is GONE!\n")
file.close()

file = open(filepath_w, "r")
print(f"After 'w' mode: {file.read()}", end="")
file.close()

# --- Example 4: Append mode ('a') — adds to end ---
filepath_a = os.path.join(SCRIPT_DIR, "append_test.txt")

file = open(filepath_a, "w")
file.write("Line 1\n")
file.close()

file = open(filepath_a, "a")
file.write("Line 2 (appended)\n")
file.write("Line 3 (appended)\n")
file.close()

file = open(filepath_a, "r")
print(f"\nAfter 'a' mode:\n{file.read()}", end="")
file.close()

# --- Example 5: Exclusive create mode ('x') ---
filepath_x = os.path.join(SCRIPT_DIR, "exclusive_test.txt")

# Remove if exists (for clean demo)
if os.path.exists(filepath_x):
    os.remove(filepath_x)

file = open(filepath_x, "x")
file.write("Created exclusively!\n")
file.close()
print(f"\n✓ 'x' mode: Created {os.path.basename(filepath_x)}")

# Try again — should fail
try:
    file = open(filepath_x, "x")
    file.close()
except FileExistsError:
    print(f"✗ 'x' mode: File already exists — error!")

# =============================
# 3. READ MODE REQUIRES EXISTING FILE
# =============================

# --- Example 6: FileNotFoundError ---
try:
    file = open("nonexistent_file_12345.txt", "r")
except FileNotFoundError:
    print(f"\n✗ 'r' mode: FileNotFoundError for nonexistent file")

# =============================
# 4. FILE OBJECT PROPERTIES
# =============================

# --- Example 7: Checking file properties ---
file = open(filepath, "r")
print(f"\nFile object properties:")
print(f"  Name: {file.name}")
print(f"  Mode: {file.mode}")
print(f"  Closed: {file.closed}")
file.close()
print(f"  Closed (after close): {file.closed}")

# =============================
# 5. ENCODING PARAMETER
# =============================

# --- Example 8: Specifying encoding ---
filepath_enc = os.path.join(SCRIPT_DIR, "encoded.txt")

file = open(filepath_enc, "w", encoding="utf-8")
file.write("Hello! こんにちは! 🐍\n")
file.close()

file = open(filepath_enc, "r", encoding="utf-8")
print(f"\nWith encoding: {file.read()}", end="")
file.close()

# =============================
# CLEANUP
# =============================
for f in ["example.txt", "write_test.txt", "append_test.txt",
          "exclusive_test.txt", "encoded.txt"]:
    path = os.path.join(SCRIPT_DIR, f)
    if os.path.exists(path):
        os.remove(path)
print("\n✓ Temp files cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Create a file with 'w' mode, then read it with 'r' mode
# 2. Test the difference between 'w' and 'a' modes
# 3. Try opening a nonexistent file with 'r' — handle the error
# ============================================
