# ============================================
# MODULE 10 - SUBTOPIC 12: Performance & Best Practices
# ============================================

import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================
# 1. EFFICIENT READING — LINE BY LINE
# =============================

# --- Setup: Create a larger test file ---
large_file = os.path.join(SCRIPT_DIR, "large_test.txt")

with open(large_file, "w") as f:
    for i in range(10000):
        f.write(f"Line {i}: This is test data for performance testing.\n")

file_size = os.path.getsize(large_file)
print(f"Test file: {file_size:,} bytes ({file_size/1024:.0f} KB)")

# --- Example 1: BAD — read() loads entire file into memory ---
start = time.time()
with open(large_file, "r") as file:
    content = file.read()   # All 10K lines in memory!
    line_count = content.count("\n")
t1 = time.time() - start
print(f"\nread() entire file:  {line_count} lines in {t1:.4f}s")

# --- Example 2: GOOD — iterate line by line ---
start = time.time()
line_count = 0
with open(large_file, "r") as file:
    for line in file:   # One line at a time — memory efficient!
        line_count += 1
t2 = time.time() - start
print(f"Line-by-line:        {line_count} lines in {t2:.4f}s")

# =============================
# 2. CHUNK READING
# =============================

# --- Example 3: Read in fixed-size chunks ---
start = time.time()
total_chars = 0
with open(large_file, "r") as file:
    while True:
        chunk = file.read(4096)   # 4KB chunks
        if not chunk:
            break
        total_chars += len(chunk)
t3 = time.time() - start
print(f"Chunk reading (4KB): {total_chars:,} chars in {t3:.4f}s")

# =============================
# 3. SAFE WRITING — TEMP FILE PATTERN
# =============================

# --- Example 4: BAD — direct write can corrupt on failure ---
data_file = os.path.join(SCRIPT_DIR, "important.txt")

with open(data_file, "w") as f:
    f.write("Important data\n")
    f.write("More important data\n")

# If program crashes DURING write, file is corrupted!

# --- Example 5: GOOD — write to temp, then rename ---
temp_file = os.path.join(SCRIPT_DIR, "important.tmp")

# Write to temp file
with open(temp_file, "w") as f:
    f.write("Updated data\n")
    f.write("Safely written\n")

# Only rename after successful write
os.rename(temp_file, data_file)
print(f"\nSafe write: temp → rename (atomic on most OS)")

with open(data_file, "r") as f:
    print(f"Content: {f.read()}", end="")

# =============================
# 4. FLUSHING DATA
# =============================

# --- Example 6: flush() forces write to disk ---
flush_file = os.path.join(SCRIPT_DIR, "flush_test.txt")

with open(flush_file, "w") as file:
    file.write("Critical data\n")
    file.flush()   # Force write to disk immediately
    # Even if program crashes after this, data is saved
    print(f"\nFlushed data to disk")

# =============================
# 5. AVOID COMMON MISTAKES
# =============================

# --- Example 7: Don't open files in loops unnecessarily ---
loop_file = os.path.join(SCRIPT_DIR, "loop_test.txt")

# ❌ BAD — opens/closes file 100 times
start = time.time()
for i in range(100):
    with open(loop_file, "a") as f:
        f.write(f"Line {i}\n")
t_bad = time.time() - start

os.remove(loop_file)

# ✅ GOOD — opens file once
start = time.time()
with open(loop_file, "w") as f:
    for i in range(100):
        f.write(f"Line {i}\n")
t_good = time.time() - start

print(f"\nLoop writing:")
print(f"  Open in loop:    {t_bad:.4f}s")
print(f"  Open once:       {t_good:.4f}s")
print(f"  Speedup: ~{t_bad/max(t_good, 0.0001):.0f}x")

# =============================
# 6. BEST PRACTICES SUMMARY
# =============================

print(f"""
╔═══════════════════════════════════════════════╗
║      FILE HANDLING BEST PRACTICES             ║
╠═══════════════════════════════════════════════╣
║  ✓ Always use 'with' for auto-closing         ║
║  ✓ Iterate line-by-line for large files       ║
║  ✓ Use chunk reading for very large files     ║
║  ✓ Write to temp file, then rename            ║
║  ✓ flush() for critical data                  ║
║  ✓ Open files outside loops                   ║
║  ✓ Specify encoding='utf-8'                   ║
║  ✓ Handle exceptions with try/except          ║
╚═══════════════════════════════════════════════╝
""")

# =============================
# CLEANUP
# =============================
for f in ["large_test.txt", "important.txt", "flush_test.txt", "loop_test.txt"]:
    path = os.path.join(SCRIPT_DIR, f)
    if os.path.exists(path):
        os.remove(path)
print("✓ Temp files cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Time reading a large file with read() vs line-by-line
# 2. Implement the temp-file-then-rename pattern
# 3. Compare opening a file in a loop vs opening once
# ============================================
