# ============================================
# MODULE 3 - SUBTOPIC 5: Bitwise Operators
# ============================================

# --- Quick refresher: seeing binary (from Module 2) ---
print(bin(5))     # 0b101
print(bin(3))     # 0b11
print(bin(10))    # 0b1010

# --- Example 1: Bitwise AND (&) ---
# Both bits must be 1 → result bit is 1
# 5 = 101
# 3 = 011
# & = 001 = 1
print(5 & 3)      # 1

# --- Example 2: Bitwise OR (|) ---
# At least one bit is 1 → result bit is 1
# 5 = 101
# 3 = 011
# | = 111 = 7
print(5 | 3)      # 7

# --- Example 3: Bitwise XOR (^) ---
# Bits are different → result bit is 1
# 5 = 101
# 3 = 011
# ^ = 110 = 6
print(5 ^ 3)      # 6

# --- Example 4: Bitwise NOT (~) ---
# Flips all bits. Result = -(n + 1)
print(~5)          # -6
print(~0)          # -1
print(~(-3))       # 2

# --- Example 5: Left shift (<<) ---
# Shifts bits to the left → multiplies by 2 per shift
print(5 << 1)      # 10  (5 × 2^1 = 5 × 2)
print(5 << 2)      # 20  (5 × 2^2 = 5 × 4)
print(5 << 3)      # 40  (5 × 2^3 = 5 × 8)
print(1 << 4)      # 16  (1 × 2^4 = 16)

# --- Example 6: Right shift (>>) ---
# Shifts bits to the right → divides by 2 per shift
print(20 >> 1)     # 10  (20 ÷ 2)
print(20 >> 2)     # 5   (20 ÷ 4)
print(16 >> 4)     # 1   (16 ÷ 16)

# --- Example 7: Visualizing with bin() ---
a = 12
b = 10
print(bin(a))          # 0b1100
print(bin(b))          # 0b1010
print(bin(a & b))      # 0b1000 → 8
print(bin(a | b))      # 0b1110 → 14
print(bin(a ^ b))      # 0b0110 → 6

print(a & b)           # 8
print(a | b)           # 14
print(a ^ b)           # 6

# --- Example 8: XOR special property ---
# XOR-ing a number with itself gives 0
print(7 ^ 7)           # 0
print(42 ^ 42)         # 0

# XOR-ing with 0 gives the number back
print(7 ^ 0)           # 7

# --- Example 9: Powers of 2 using left shift ---
print(1 << 0)    # 1   (2^0)
print(1 << 1)    # 2   (2^1)
print(1 << 2)    # 4   (2^2)
print(1 << 3)    # 8   (2^3)
print(1 << 10)   # 1024 (2^10)

# --- Example 10: Augmented bitwise assignment ---
x = 12
x &= 10       # same as x = x & 10
print(x)       # 8

y = 5
y |= 3        # same as y = y | 3
print(y)       # 7

z = 10
z ^= 10       # same as z = z ^ 10
print(z)       # 0

n = 1
n <<= 5       # same as n = n << 5
print(n)       # 32

# ============================================
# TRY IT YOURSELF:
# 1. Find 7 & 3 and verify with bin()
# 2. Use left shift to calculate 2^8
# 3. What is ~(-1)?
# ============================================
