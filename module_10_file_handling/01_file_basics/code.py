# ============================================
# MODULE 10 - SUBTOPIC 1: File Basics
# ============================================

import os

# =============================
# 1. FILE vs MEMORY
# =============================

# --- Example 1: Variables are temporary ---
name = "Trush"
print(f"Variable: {name}")
# When this script ends, 'name' disappears from memory

# --- Example 2: Files are permanent ---
# If we write to a file, the data stays even after the program ends
print("Files persist on disk — variables don't.")

# =============================
# 2. FILE PATHS
# =============================

# --- Example 3: Current working directory ---
cwd = os.getcwd()
print(f"\nCurrent directory: {cwd}")

# --- Example 4: Relative paths ---
# These are relative to the current directory
relative_examples = [
    "data.txt",             # Same folder
    "folder/data.txt",      # Inside subfolder
    "../data.txt",          # Parent folder
]

print("\nRelative path examples:")
for path in relative_examples:
    print(f"  {path}")

# --- Example 5: Absolute paths ---
print(f"\nAbsolute path of this script: {os.path.abspath(__file__)}")
print(f"Directory of this script: {os.path.dirname(os.path.abspath(__file__))}")

# =============================
# 3. PATH OPERATIONS
# =============================

# --- Example 6: Joining paths safely ---
folder = "my_project"
filename = "data.txt"
full_path = os.path.join(folder, filename)
print(f"\nJoined path: {full_path}")

# --- Example 7: Splitting paths ---
path = "/home/user/documents/report.txt"
directory = os.path.dirname(path)
file_name = os.path.basename(path)
name_part, extension = os.path.splitext(file_name)

print(f"\nPath: {path}")
print(f"  Directory: {directory}")
print(f"  Filename:  {file_name}")
print(f"  Name:      {name_part}")
print(f"  Extension: {extension}")

# =============================
# 4. CHECKING IF FILES EXIST
# =============================

# --- Example 8: File existence checks ---
test_files = ["data.txt", __file__, "/nonexistent/file.txt"]

print("\nFile existence:")
for f in test_files:
    exists = os.path.exists(f)
    print(f"  '{f}': {'✓ exists' if exists else '✗ not found'}")

# --- Example 9: Check if path is file or directory ---
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

print(f"\nPath type:")
print(f"  '{script_path}': is_file={os.path.isfile(script_path)}")
print(f"  '{script_dir}': is_dir={os.path.isdir(script_dir)}")

# =============================
# 5. COMMON FILE EXTENSIONS
# =============================

# --- Example 10: File type reference ---
file_types = {
    ".txt": "Plain text",
    ".csv": "Comma-separated values",
    ".json": "Structured data (JSON)",
    ".log": "Log files",
    ".py": "Python source code",
    ".md": "Markdown documentation",
}

print("\nCommon file types:")
for ext, desc in file_types.items():
    print(f"  {ext:6s} → {desc}")

# ============================================
# TRY IT YOURSELF:
# 1. Print your current working directory
# 2. Build a full path using os.path.join()
# 3. Check if a file exists on your system
# ============================================
