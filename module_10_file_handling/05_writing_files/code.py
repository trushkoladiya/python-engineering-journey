# ============================================
# MODULE 10 - SUBTOPIC 5: Writing to Files
# ============================================

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================
# 1. write() — WRITE A STRING
# =============================

# --- Example 1: Basic writing ---
filepath = os.path.join(SCRIPT_DIR, "output.txt")

with open(filepath, "w") as file:
    file.write("Hello, World!\n")
    file.write("Python file writing.\n")

with open(filepath, "r") as file:
    print("write():")
    print(file.read(), end="")

# --- Example 2: Writing without \n ---
filepath2 = os.path.join(SCRIPT_DIR, "no_newline.txt")

with open(filepath2, "w") as file:
    file.write("No newline")
    file.write("concatenated")   # No \n — runs together!

with open(filepath2, "r") as file:
    print(f"\nWithout \\n: '{file.read()}'")

# --- Example 3: Writing numbers (must convert to string) ---
filepath3 = os.path.join(SCRIPT_DIR, "numbers.txt")

with open(filepath3, "w") as file:
    for i in range(1, 6):
        file.write(f"Number: {i}\n")

with open(filepath3, "r") as file:
    print(f"\nNumbers:\n{file.read()}", end="")

# =============================
# 2. writelines() — WRITE A LIST
# =============================

# --- Example 4: Writing a list of strings ---
filepath4 = os.path.join(SCRIPT_DIR, "lines.txt")

lines = ["Apple\n", "Banana\n", "Cherry\n", "Date\n"]
with open(filepath4, "w") as file:
    file.writelines(lines)

with open(filepath4, "r") as file:
    print(f"\nwritelines():\n{file.read()}", end="")

# --- Example 5: Creating lines from data ---
filepath5 = os.path.join(SCRIPT_DIR, "students.txt")

students = ["Trush", "Rahul", "Charlie", "Diana"]
lines = [f"{name}\n" for name in students]   # Add \n to each

with open(filepath5, "w") as file:
    file.writelines(lines)

with open(filepath5, "r") as file:
    print(f"\nStudents:\n{file.read()}", end="")

# =============================
# 3. OVERWRITING vs APPENDING
# =============================

# --- Example 6: 'w' mode overwrites ---
filepath6 = os.path.join(SCRIPT_DIR, "overwrite.txt")

with open(filepath6, "w") as file:
    file.write("Original content\n")

with open(filepath6, "w") as file:
    file.write("Replaced content!\n")   # Original is GONE

with open(filepath6, "r") as file:
    print(f"\nOverwrite ('w'):\n{file.read()}", end="")

# --- Example 7: 'a' mode appends ---
filepath7 = os.path.join(SCRIPT_DIR, "append.txt")

with open(filepath7, "w") as file:
    file.write("Line 1\n")

with open(filepath7, "a") as file:
    file.write("Line 2 (appended)\n")
    file.write("Line 3 (appended)\n")

with open(filepath7, "r") as file:
    print(f"\nAppend ('a'):\n{file.read()}", end="")

# =============================
# 4. USING print() TO WRITE
# =============================

# --- Example 8: print() with file parameter ---
filepath8 = os.path.join(SCRIPT_DIR, "print_write.txt")

with open(filepath8, "w") as file:
    print("Hello from print!", file=file)
    print("Line 2", file=file)
    print(f"Number: {42}", file=file)
    # print() adds \n automatically!

with open(filepath8, "r") as file:
    print(f"\nUsing print(file=):\n{file.read()}", end="")

# =============================
# 5. PRACTICAL EXAMPLES
# =============================

# --- Example 9: Write a multiplication table ---
filepath9 = os.path.join(SCRIPT_DIR, "table.txt")

with open(filepath9, "w") as file:
    for i in range(1, 6):
        row = " | ".join(f"{i*j:3d}" for j in range(1, 6))
        file.write(f"  {row}\n")

with open(filepath9, "r") as file:
    print(f"\nMultiplication table:\n{file.read()}", end="")

# --- Example 10: Save a report ---
filepath10 = os.path.join(SCRIPT_DIR, "report.txt")

scores = {"Trush": 92, "Rahul": 78, "Charlie": 85, "Diana": 95}

with open(filepath10, "w") as file:
    file.write("=" * 30 + "\n")
    file.write("  Student Report\n")
    file.write("=" * 30 + "\n")
    for name, score in scores.items():
        file.write(f"  {name:10s}: {score}\n")
    file.write("=" * 30 + "\n")
    avg = sum(scores.values()) / len(scores)
    file.write(f"  Average:    {avg:.1f}\n")

with open(filepath10, "r") as file:
    print(f"\nReport:\n{file.read()}", end="")

# =============================
# CLEANUP
# =============================
for f in ["output.txt", "no_newline.txt", "numbers.txt", "lines.txt",
          "students.txt", "overwrite.txt", "append.txt",
          "print_write.txt", "table.txt", "report.txt"]:
    path = os.path.join(SCRIPT_DIR, f)
    if os.path.exists(path):
        os.remove(path)
print("\n\n✓ Temp files cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Write your name and age to a file
# 2. Append 3 lines to an existing file
# 3. Save a dictionary as key:value lines to a file
# ============================================
