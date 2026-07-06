# ============================================
# MODULE 10 - SUBTOPIC 8: File Modes Deep Behavior
# ============================================

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================
# 1. r+ MODE — READ AND WRITE
# =============================

# --- Example 1: Read then write ---
filepath = os.path.join(SCRIPT_DIR, "rplus.txt")

# Create the file first (r+ requires it to exist)
with open(filepath, "w") as f:
    f.write("Hello World\n")
    f.write("Line Two\n")

# Read and write with r+
with open(filepath, "r+") as file:
    content = file.read()
    print(f"r+ read: {repr(content)}")
    
    # Pointer is at the end now, so write appends
    file.write("Added with r+\n")

with open(filepath, "r") as file:
    print(f"After r+:\n{file.read()}", end="")

# --- Example 2: r+ write at specific position ---
with open(filepath, "r+") as file:
    file.seek(6)   # Move to position 6
    file.write("Python")   # Overwrites bytes at that position!

with open(filepath, "r") as file:
    print(f"\nAfter seek+write:\n{file.read()}", end="")

# =============================
# 2. w+ MODE — WRITE AND READ
# =============================

# --- Example 3: Write then read back ---
filepath2 = os.path.join(SCRIPT_DIR, "wplus.txt")

with open(filepath2, "w+") as file:
    file.write("Written with w+\n")
    file.write("Second line\n")
    
    # Pointer is at end — read returns nothing
    print(f"\nw+ read at end: '{file.read()}'")
    
    # Seek back to start
    file.seek(0)
    print(f"w+ read after seek(0):\n{file.read()}", end="")

# --- Example 4: w+ erases existing content ---
with open(filepath2, "w") as f:
    f.write("Original content\n")

with open(filepath2, "w+") as file:
    # Opening with w+ ERASES everything!
    file.seek(0)
    content = file.read()
    print(f"\nw+ erased original: '{content}' (empty!)")
    
    file.write("Fresh start with w+\n")
    file.seek(0)
    print(f"New content: {file.read()}", end="")

# =============================
# 3. a+ MODE — APPEND AND READ
# =============================

# --- Example 5: Append then read ---
filepath3 = os.path.join(SCRIPT_DIR, "aplus.txt")

with open(filepath3, "w") as f:
    f.write("Original line\n")

with open(filepath3, "a+") as file:
    # Pointer starts at end
    print(f"\na+ tell(): {file.tell()} (at end)")
    
    # Write always goes to end
    file.write("Appended line\n")
    
    # Must seek to read
    file.seek(0)
    print(f"a+ full content:\n{file.read()}", end="")

# --- Example 6: Multiple append+read cycles ---
filepath4 = os.path.join(SCRIPT_DIR, "log.txt")

for i in range(1, 4):
    with open(filepath4, "a+") as file:
        file.write(f"Log entry {i}\n")
        file.seek(0)
        content = file.read()
        print(f"\nAfter entry {i}:")
        print(content, end="")

# =============================
# 4. MODE COMPARISON
# =============================

# --- Example 7: Side-by-side summary ---
print(f"""
╔══════════╦═══════╦═══════╦═════════╦════════╗
║  Mode    ║ Read  ║ Write ║ Creates ║ Erases ║
╠══════════╬═══════╬═══════╬═════════╬════════╣
║  'r'     ║  ✅   ║  ❌   ║   ❌    ║   ❌   ║
║  'w'     ║  ❌   ║  ✅   ║   ✅    ║   ✅   ║
║  'a'     ║  ❌   ║  ✅   ║   ✅    ║   ❌   ║
║  'r+'    ║  ✅   ║  ✅   ║   ❌    ║   ❌   ║
║  'w+'    ║  ✅   ║  ✅   ║   ✅    ║   ✅   ║
║  'a+'    ║  ✅   ║  ✅   ║   ✅    ║   ❌   ║
╚══════════╩═══════╩═══════╩═════════╩════════╝
""")

# =============================
# CLEANUP
# =============================
for f in ["rplus.txt", "wplus.txt", "aplus.txt", "log.txt"]:
    path = os.path.join(SCRIPT_DIR, f)
    if os.path.exists(path):
        os.remove(path)
print("✓ Temp files cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Use r+ to read a file and add a line at the end
# 2. Use w+ to write data and immediately read it back
# 3. Use a+ to build a log file over multiple operations
# ============================================
