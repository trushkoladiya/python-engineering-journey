# ============================================
# MODULE 10 - SUBTOPIC 11: File System Operations
# ============================================

import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================
# 1. CHECKING EXISTENCE
# =============================

# --- Example 1: Check if file/directory exists ---
print("Existence checks:")
print(f"  This script exists: {os.path.exists(__file__)}")
print(f"  This dir exists:    {os.path.exists(SCRIPT_DIR)}")
print(f"  Missing file:       {os.path.exists('xyz123.txt')}")

# --- Example 2: File vs directory ---
print(f"\nType checks:")
print(f"  Is file:  {os.path.isfile(__file__)}")
print(f"  Is dir:   {os.path.isdir(SCRIPT_DIR)}")

# =============================
# 2. FILE INFORMATION
# =============================

# --- Example 3: File size ---
file_size = os.path.getsize(__file__)
print(f"\nThis script:")
print(f"  Size: {file_size} bytes ({file_size/1024:.1f} KB)")

# --- Example 4: Modification time ---
mod_time = os.path.getmtime(__file__)
readable_time = time.ctime(mod_time)
print(f"  Last modified: {readable_time}")

# =============================
# 3. LISTING DIRECTORY CONTENTS
# =============================

# --- Example 5: List files in a directory ---
parent_dir = os.path.dirname(SCRIPT_DIR)
items = os.listdir(parent_dir)

print(f"\nContents of module_10 directory:")
for item in sorted(items)[:10]:   # Show first 10
    full_path = os.path.join(parent_dir, item)
    item_type = "DIR " if os.path.isdir(full_path) else "FILE"
    print(f"  [{item_type}] {item}")

# --- Example 6: Filter by extension ---
print(f"\nPython files in this folder:")
for item in os.listdir(SCRIPT_DIR):
    if item.endswith(".py"):
        size = os.path.getsize(os.path.join(SCRIPT_DIR, item))
        print(f"  {item} ({size} bytes)")

# =============================
# 4. CREATING DIRECTORIES
# =============================

# --- Example 7: Create a directory ---
test_dir = os.path.join(SCRIPT_DIR, "test_folder")

os.makedirs(test_dir, exist_ok=True)   # exist_ok prevents error if exists
print(f"\nCreated: {os.path.basename(test_dir)}")
print(f"  Exists: {os.path.exists(test_dir)}")

# --- Example 8: Nested directories ---
nested_dir = os.path.join(SCRIPT_DIR, "a", "b", "c")
os.makedirs(nested_dir, exist_ok=True)
print(f"Created nested: a/b/c → {os.path.exists(nested_dir)}")

# =============================
# 5. CREATING AND DELETING FILES
# =============================

# --- Example 9: Create a temp file ---
temp_file = os.path.join(SCRIPT_DIR, "temp_data.txt")

with open(temp_file, "w") as f:
    f.write("Temporary data\n")
print(f"\nCreated: {os.path.basename(temp_file)}")
print(f"  Exists: {os.path.exists(temp_file)}")

# --- Example 10: Delete a file ---
os.remove(temp_file)
print(f"  Deleted: {not os.path.exists(temp_file)}")

# --- Example 11: Safe delete ---
def safe_delete(filepath):
    """Delete a file only if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"  ✓ Deleted: {os.path.basename(filepath)}")
    else:
        print(f"  ✗ Not found: {os.path.basename(filepath)}")

print(f"\nSafe delete:")
safe_delete(temp_file)   # Already deleted

# =============================
# 6. RENAMING FILES
# =============================

# --- Example 12: Rename a file ---
old_name = os.path.join(SCRIPT_DIR, "old_name.txt")
new_name = os.path.join(SCRIPT_DIR, "new_name.txt")

with open(old_name, "w") as f:
    f.write("Rename test\n")

os.rename(old_name, new_name)
print(f"\nRenamed:")
print(f"  Old exists: {os.path.exists(old_name)}")
print(f"  New exists: {os.path.exists(new_name)}")

# =============================
# CLEANUP
# =============================
safe_delete(new_name)

# Remove test directories
import shutil
for d in ["test_folder", "a"]:
    path = os.path.join(SCRIPT_DIR, d)
    if os.path.exists(path):
        shutil.rmtree(path)

print(f"\n✓ Cleanup complete")

# ============================================
# TRY IT YOURSELF:
# 1. List all files in your home directory
# 2. Create a nested directory structure and verify it
# 3. Write a function that finds all .txt files in a directory
# ============================================
