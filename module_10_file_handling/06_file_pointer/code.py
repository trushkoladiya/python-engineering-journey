# ============================================
# MODULE 10 - SUBTOPIC 6: File Pointer Control
# ============================================

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(SCRIPT_DIR, "pointer_test.txt")

# Setup
with open(filepath, "w") as f:
    f.write("ABCDEFGHIJ\n")
    f.write("1234567890\n")
    f.write("Hello World\n")

# =============================
# 1. tell() — CURRENT POSITION
# =============================

# --- Example 1: Track position while reading ---
with open(filepath, "r") as file:
    print(f"Start position: {file.tell()}")
    
    chunk1 = file.read(5)
    print(f"After reading 5 chars: tell() = {file.tell()}, got '{chunk1}'")
    
    chunk2 = file.read(5)
    print(f"After reading 5 more: tell() = {file.tell()}, got '{chunk2}'")

# --- Example 2: Position after readline ---
with open(filepath, "r") as file:
    line1 = file.readline()
    pos1 = file.tell()
    line2 = file.readline()
    pos2 = file.tell()
    
    print(f"\nAfter line 1: position = {pos1}")
    print(f"After line 2: position = {pos2}")

# =============================
# 2. seek() — MOVE THE POINTER
# =============================

# --- Example 3: Read from the beginning again ---
with open(filepath, "r") as file:
    first_read = file.read()
    print(f"\nFirst read: {len(first_read)} chars")
    
    second_read = file.read()
    print(f"Second read (no seek): {len(second_read)} chars (empty!)")
    
    file.seek(0)   # Go back to start
    third_read = file.read()
    print(f"Third read (after seek(0)): {len(third_read)} chars")

# --- Example 4: Seek to specific positions ---
with open(filepath, "r") as file:
    file.seek(0)
    print(f"\nseek(0): '{file.read(5)}'")
    
    file.seek(5)
    print(f"seek(5): '{file.read(5)}'")

# --- Example 5: Count lines and re-read ---
with open(filepath, "r") as file:
    # First pass: count lines
    line_count = sum(1 for _ in file)
    
    # Go back and read content
    file.seek(0)
    content = file.read()
    
    print(f"\nLines: {line_count}")
    print(f"Content (re-read):\n{content}", end="")

# =============================
# 3. PRACTICAL USES
# =============================

# --- Example 6: Read file twice for different purposes ---
data_file = os.path.join(SCRIPT_DIR, "scores.txt")
with open(data_file, "w") as f:
    f.write("85\n72\n91\n68\n95\n")

with open(data_file, "r") as file:
    # First pass: find the max
    scores = [int(line.strip()) for line in file]
    max_score = max(scores)
    
    # Second pass: find who scored highest
    file.seek(0)
    for i, line in enumerate(file, 1):
        score = int(line.strip())
        if score == max_score:
            print(f"\nHighest score: {score} (line {i})")

# =============================
# CLEANUP
# =============================
for f in [filepath, data_file]:
    if os.path.exists(f):
        os.remove(f)
print("\n✓ Temp files cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Read a file, seek back to the start, read again
# 2. Use tell() to track position while reading character by character
# 3. Read a file twice — once to count words, once to find the longest
# ============================================
