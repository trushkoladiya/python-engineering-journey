# ============================================
# MODULE 2 - SUBTOPIC 8: Binary & Base Representations
# ============================================

# --- Example 1: Binary — bin() ---
print(bin(0))     # 0b0
print(bin(1))     # 0b1
print(bin(5))     # 0b101
print(bin(10))    # 0b1010
print(bin(255))   # 0b11111111

# --- Example 2: Octal — oct() ---
print(oct(0))     # 0o0
print(oct(8))     # 0o10
print(oct(10))    # 0o12
print(oct(255))   # 0o377

# --- Example 3: Hexadecimal — hex() ---
print(hex(0))     # 0x0
print(hex(10))    # 0xa
print(hex(15))    # 0xf
print(hex(16))    # 0x10
print(hex(255))   # 0xff

# --- Example 4: Writing numbers in other bases ---
a = 0b1010    # binary for 10
b = 0o12      # octal for 10
c = 0xa       # hex for 10
print(a, b, c)  # 10 10 10 — all the same number!

# --- Example 5: Converting back to decimal ---
print(int("1010", 2))    # 10 (from binary)
print(int("377", 8))     # 255 (from octal)
print(int("ff", 16))     # 255 (from hex)
print(int("1a", 16))     # 26 (from hex)

# --- Example 6: Practical — RGB colors in hex ---
red = 0xff     # 255
green = 0x80   # 128
blue = 0x00    # 0
print(f"RGB: ({red}, {green}, {blue})")  # RGB: (255, 128, 0)

# --- Example 7: Binary of negative numbers ---
print(bin(-5))   # -0b101 (just adds a minus sign)

# --- Example 8: All representations of one number ---
num = 42
print(f"Decimal:     {num}")
print(f"Binary:      {bin(num)}")
print(f"Octal:       {oct(num)}")
print(f"Hexadecimal: {hex(num)}")

# ============================================
# TRY IT YOURSELF:
# 1. Convert 100 to binary, octal, and hex
# 2. Convert binary "11111111" back to decimal
# 3. What decimal number is 0xff?
# ============================================
