# ============================================
# MODULE 10 - SUBTOPIC 7: Text vs Binary Files
# ============================================

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================
# 1. TEXT FILES
# =============================

# --- Example 1: Writing and reading text ---
text_file = os.path.join(SCRIPT_DIR, "text_example.txt")

with open(text_file, "w", encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("Python is great! 🐍\n")

with open(text_file, "r", encoding="utf-8") as file:
    content = file.read()
    print(f"Text file content:\n{content}")
    print(f"Type: {type(content)}")   # <class 'str'>

# --- Example 2: Encoding matters ---
encoded_file = os.path.join(SCRIPT_DIR, "encoded.txt")

with open(encoded_file, "w", encoding="utf-8") as file:
    file.write("English: Hello\n")
    file.write("Japanese: こんにちは\n")
    file.write("Emoji: 🎉🐍✨\n")

with open(encoded_file, "r", encoding="utf-8") as file:
    print(f"Encoded content:\n{file.read()}")

# =============================
# 2. BINARY FILES
# =============================

# --- Example 3: Writing binary data ---
binary_file = os.path.join(SCRIPT_DIR, "binary_example.bin")

with open(binary_file, "wb") as file:
    file.write(b"Hello")           # b"..." is bytes literal
    file.write(bytes([0, 1, 2, 3, 255]))   # Raw bytes

with open(binary_file, "rb") as file:
    data = file.read()
    print(f"\nBinary data: {data}")
    print(f"Type: {type(data)}")    # <class 'bytes'>
    print(f"Length: {len(data)} bytes")
    print(f"As list: {list(data)}")

# --- Example 4: Difference between text and binary ---
test_file = os.path.join(SCRIPT_DIR, "compare.txt")

with open(test_file, "w") as file:
    file.write("ABC\n")

# Read as text
with open(test_file, "r") as file:
    text = file.read()
    print(f"\nText mode: {repr(text)}")

# Read as binary
with open(test_file, "rb") as file:
    binary = file.read()
    print(f"Binary mode: {repr(binary)}")

# =============================
# 3. COPYING A BINARY FILE
# =============================

# --- Example 5: Copy any file using binary mode ---
source = os.path.join(SCRIPT_DIR, "source.bin")
copy = os.path.join(SCRIPT_DIR, "copy.bin")

# Create source with mixed data
with open(source, "wb") as file:
    file.write(b"\x89PNG\r\n")   # Fake PNG header
    file.write(bytes(range(50)))

# Copy it
with open(source, "rb") as src:
    with open(copy, "wb") as dst:
        dst.write(src.read())

# Verify
with open(source, "rb") as s, open(copy, "rb") as c:
    print(f"\nBinary copy:")
    print(f"  Source size: {len(s.read())} bytes")
    print(f"  Copy size:   {len(c.read())} bytes")
    s.seek(0)
    c.seek(0)
    print(f"  Identical: {s.read() == c.read()}")

# =============================
# 4. ENCODING ERRORS
# =============================

# --- Example 6: What happens with wrong encoding ---
bad_file = os.path.join(SCRIPT_DIR, "bad_encode.txt")

# Write with UTF-8
with open(bad_file, "w", encoding="utf-8") as file:
    file.write("Café résumé naïve")

# Read with correct encoding
with open(bad_file, "r", encoding="utf-8") as file:
    print(f"\nCorrect encoding: {file.read()}")

# Try reading with wrong encoding (may produce garbled text)
try:
    with open(bad_file, "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError as e:
    print(f"Wrong encoding error: {e}")

# =============================
# 5. BYTES ↔ STRING CONVERSION
# =============================

# --- Example 7: Converting between types ---
text = "Hello, Python! 🐍"

# String → Bytes (encode)
encoded = text.encode("utf-8")
print(f"\nString: {text}")
print(f"Encoded: {encoded}")
print(f"Length: {len(encoded)} bytes")

# Bytes → String (decode)
decoded = encoded.decode("utf-8")
print(f"Decoded: {decoded}")

# =============================
# CLEANUP
# =============================
for f in ["text_example.txt", "encoded.txt", "binary_example.bin",
          "compare.txt", "source.bin", "copy.bin", "bad_encode.txt"]:
    path = os.path.join(SCRIPT_DIR, f)
    if os.path.exists(path):
        os.remove(path)
print("\n✓ Temp files cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Write a text file with special characters and read it back
# 2. Create a binary file with bytes 0-255 and read it back
# 3. Copy a real file (like this .py file) using binary mode
# ============================================
