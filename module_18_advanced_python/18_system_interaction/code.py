# ============================================
# MODULE 18 - SUBTOPIC 18: System Interaction
# ============================================

# Interacting with the OS — files, directories, commands, paths.

import os
import shutil
import subprocess
import platform
from pathlib import Path
from datetime import datetime

# =============================
# 1. SYSTEM INFORMATION
# =============================

print("=== System Information ===")
print()

print(f"  OS: {platform.system()} {platform.release()}")
print(f"  Machine: {platform.machine()}")
print(f"  Python: {platform.python_version()}")
print(f"  Hostname: {platform.node()}")
print(f"  Current user: {os.getenv('USER', os.getenv('USERNAME', 'unknown'))}")
print(f"  PID: {os.getpid()}")
print()

# =============================
# 2. CURRENT DIRECTORY AND LISTING
# =============================

print("=== Directory Operations ===")
print()

cwd = os.getcwd()
print(f"  Current dir: {cwd}")

script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"  Script dir: {script_dir}")

# List directory contents
items = os.listdir(script_dir)
print(f"  Contents of script dir:")
for item in sorted(items):
    full_path = os.path.join(script_dir, item)
    item_type = "DIR" if os.path.isdir(full_path) else "FILE"
    print(f"    [{item_type}] {item}")
print()

# =============================
# 3. PATH MANIPULATION WITH os.path
# =============================

print("=== os.path Operations ===")
print()

sample_path = os.path.join("home", "user", "documents", "report.pdf")
print(f"  Joined path: {sample_path}")
print(f"  dirname:     {os.path.dirname(sample_path)}")
print(f"  basename:    {os.path.basename(sample_path)}")
print(f"  splitext:    {os.path.splitext(sample_path)}")
print(f"  exists:      {os.path.exists(sample_path)}")

# Absolute path
print(f"  abspath('.'):  {os.path.abspath('.')}")

# Normalize path
messy = "home/user/../user/./documents/../documents/file.txt"
print(f"  Messy:      {messy}")
print(f"  Normalized: {os.path.normpath(messy)}")
print()

# =============================
# 4. PATHLIB — MODERN PATH HANDLING
# =============================

print("=== pathlib.Path (Modern Approach) ===")
print()

p = Path(script_dir)
print(f"  Path: {p}")
print(f"  Name: {p.name}")
print(f"  Parent: {p.parent}")
print(f"  Parts: {p.parts[-3:]}")
print(f"  Is dir: {p.is_dir()}")
print()

# Build paths with /
new_path = p / "subdir" / "file.txt"
print(f"  Built path: {new_path}")
print(f"  Suffix: {new_path.suffix}")
print(f"  Stem: {new_path.stem}")
print()

# Glob pattern matching
print(f"  Python files in script dir:")
for py_file in sorted(p.glob("*.py")):
    print(f"    {py_file.name}")
print()

# =============================
# 5. FILE OPERATIONS
# =============================

print("=== File Operations ===")
print()

# Create a temporary working directory
work_dir = os.path.join(script_dir, "_demo_workspace")
os.makedirs(work_dir, exist_ok=True)
print(f"  Created workspace: {os.path.basename(work_dir)}")

# Create files
for i in range(3):
    filepath = os.path.join(work_dir, f"file_{i+1}.txt")
    with open(filepath, "w") as f:
        f.write(f"Content of file {i+1}\n" * (i + 1))
    print(f"  Created: file_{i+1}.txt")

# Create a subdirectory
sub_dir = os.path.join(work_dir, "subdir")
os.makedirs(sub_dir, exist_ok=True)
with open(os.path.join(sub_dir, "nested.txt"), "w") as f:
    f.write("Nested file content\n")
print(f"  Created: subdir/nested.txt")
print()

# =============================
# 6. FILE INFO AND METADATA
# =============================

print("=== File Information ===")
print()

for item in sorted(os.listdir(work_dir)):
    full = os.path.join(work_dir, item)
    if os.path.isfile(full):
        stat = os.stat(full)
        size = stat.st_size
        modified = datetime.fromtimestamp(stat.st_mtime)
        print(f"  {item:20s} {size:5d} bytes  modified: {modified:%Y-%m-%d %H:%M}")

print()

# =============================
# 7. SHUTIL — COPY, MOVE, DELETE
# =============================

print("=== shutil Operations ===")
print()

# Copy a file
src = os.path.join(work_dir, "file_1.txt")
dst = os.path.join(work_dir, "file_1_copy.txt")
shutil.copy2(src, dst)  # copy2 preserves metadata
print(f"  Copied: file_1.txt → file_1_copy.txt")

# Move a file
shutil.move(dst, os.path.join(work_dir, "moved_file.txt"))
print(f"  Moved: file_1_copy.txt → moved_file.txt")

# Copy entire directory
shutil.copytree(sub_dir, os.path.join(work_dir, "subdir_copy"))
print(f"  Copied directory: subdir → subdir_copy")

# Get directory size
total_size = sum(
    os.path.getsize(os.path.join(dirpath, filename))
    for dirpath, dirnames, filenames in os.walk(work_dir)
    for filename in filenames
)
print(f"  Total workspace size: {total_size} bytes")
print()

# =============================
# 8. os.walk — TRAVERSE DIRECTORY TREE
# =============================

print("=== os.walk — Directory Tree ===")
print()

print(f"  Walking {os.path.basename(work_dir)}/:")
for dirpath, dirnames, filenames in os.walk(work_dir):
    level = dirpath.replace(work_dir, "").count(os.sep)
    indent = "    " * level
    print(f"  {indent}{os.path.basename(dirpath)}/")
    sub_indent = "    " * (level + 1)
    for filename in sorted(filenames):
        print(f"  {sub_indent}{filename}")
print()

# =============================
# 9. SUBPROCESS — RUNNING COMMANDS
# =============================

print("=== subprocess — Running Commands ===")
print()

# Run a simple command
result = subprocess.run(
    ["echo", "Hello from subprocess!"],
    capture_output=True,
    text=True
)
print(f"  Output: {result.stdout.strip()}")
print(f"  Return code: {result.returncode}")
print()

# Run python --version
result = subprocess.run(
    ["python3", "--version"],
    capture_output=True,
    text=True
)
print(f"  Python version: {result.stdout.strip()}")

# List files (cross-platform)
if platform.system() != "Windows":
    result = subprocess.run(
        ["ls", "-la", work_dir],
        capture_output=True,
        text=True
    )
    print(f"\n  ls -la output:")
    for line in result.stdout.strip().split('\n')[:5]:
        print(f"    {line}")
print()

# =============================
# 10. ENVIRONMENT VARIABLES
# =============================

print("=== Environment Variables ===")
print()

# Read environment variables
home = os.environ.get("HOME", os.environ.get("USERPROFILE", "N/A"))
path = os.environ.get("PATH", "")
shell = os.environ.get("SHELL", "N/A")

print(f"  HOME: {home}")
print(f"  SHELL: {shell}")
print(f"  PATH entries: {len(path.split(os.pathsep))}")

# Show first 3 PATH entries
for entry in path.split(os.pathsep)[:3]:
    print(f"    {entry}")
print()

# =============================
# CLEANUP
# =============================

print("=== Cleanup ===")
print()
shutil.rmtree(work_dir)
print(f"  Removed workspace: {os.path.basename(work_dir)}")
print(f"  Exists: {os.path.exists(work_dir)}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a script that lists all .py files
#    in a directory tree with their sizes
# 2. Create a backup function that copies a directory
#    with a timestamp suffix
# 3. Use subprocess to run a shell command and
#    parse its output
# ============================================
