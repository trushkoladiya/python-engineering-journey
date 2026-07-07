# ============================================
# MODULE 10 - SUBTOPIC 9: Exception Handling with Files
# ============================================

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================
# 1. FileNotFoundError
# =============================

# --- Example 1: File doesn't exist ---
try:
    with open("nonexistent_file_xyz.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("✗ FileNotFoundError: The file doesn't exist!")

# --- Example 2: Graceful handling ---
def read_file_safe(filepath):
    """Read a file safely, return None if not found."""
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"  File not found: {filepath}")
        return None

result = read_file_safe("missing.txt")
print(f"  Result: {result}")

# =============================
# 2. PermissionError
# =============================

# --- Example 3: Permission denied (simulated) ---
try:
    # On most systems, you can't write to /etc/
    with open("/etc/shadow", "r") as file:
        content = file.read()
except PermissionError:
    print(f"\n✗ PermissionError: No permission to read that file!")
except FileNotFoundError:
    print(f"\n✗ FileNotFoundError: System file not accessible")

# =============================
# 3. MULTIPLE EXCEPTIONS
# =============================

# --- Example 4: Handling multiple error types ---
def safe_read(filepath):
    """Handle all common file errors."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: '{filepath}' not found"
    except PermissionError:
        return f"Error: No permission to read '{filepath}'"
    except UnicodeDecodeError:
        return f"Error: Cannot decode '{filepath}' as UTF-8"
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"

print(f"\nSafe read results:")
print(f"  {safe_read('missing.txt')}")

# =============================
# 4. try/except/else/finally
# =============================

# --- Example 5: Full pattern ---
filepath = os.path.join(SCRIPT_DIR, "test_except.txt")

# Create test file
with open(filepath, "w") as f:
    f.write("Test data\n")

try:
    with open(filepath, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("\nFile not found!")
else:
    # Runs only if NO exception occurred
    print(f"\nSuccess! Content: {content.strip()}")
finally:
    # Runs ALWAYS — whether error or not
    print("Finally: cleanup done")

# --- Example 6: finally for cleanup ---
def process_file(filepath):
    """Process a file with full error handling."""
    file = None
    try:
        file = open(filepath, "r")
        content = file.read()
        # Process the content
        words = content.split()
        print(f"\n  Words found: {len(words)}")
    except FileNotFoundError:
        print(f"\n  File not found: {filepath}")
    except Exception as e:
        print(f"\n  Error: {e}")
    finally:
        if file and not file.closed:
            file.close()
            print("  File closed in finally")

process_file(filepath)
process_file("nonexistent.txt")

# =============================
# 5. PRACTICAL: SAFE FILE WRITER
# =============================

# --- Example 7: Write with error handling ---
def write_safe(filepath, content):
    """Write content to file with error handling."""
    try:
        with open(filepath, "w") as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"  Cannot write to {filepath}: no permission")
        return False
    except OSError as e:
        print(f"  OS Error: {e}")
        return False

safe_path = os.path.join(SCRIPT_DIR, "safe_write.txt")
success = write_safe(safe_path, "Safe content!\n")
print(f"\nWrite successful: {success}")

# --- Example 8: Check before opening ---
def read_if_exists(filepath):
    """Only try to read if file exists."""
    if not os.path.exists(filepath):
        print(f"  '{os.path.basename(filepath)}' does not exist")
        return None
    if not os.path.isfile(filepath):
        print(f"  '{os.path.basename(filepath)}' is not a file")
        return None
    
    with open(filepath, "r") as file:
        return file.read()

print(f"\nCheck before read:")
result = read_if_exists(safe_path)
print(f"  Content: {result.strip() if result else 'None'}")
read_if_exists("nope.txt")

# =============================
# CLEANUP
# =============================
for f in ["test_except.txt", "safe_write.txt"]:
    path = os.path.join(SCRIPT_DIR, f)
    if os.path.exists(path):
        os.remove(path)
print(f"\n✓ Temp files cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Write a function that reads a file and handles all errors
# 2. Use try/except/else/finally with file operations
# 3. Check if a file exists before trying to read it
# ============================================
