# ============================================
# MODULE 2 - SUBTOPIC 9: Arithmetic Behavior with Types
# ============================================

# --- Example 1: Type promotion (int + float → float) ---
result = 5 + 2.0
print(result)        # 7.0
print(type(result))  # <class 'float'>

result2 = 10 * 1.5
print(result2)        # 15.0
print(type(result2))  # <class 'float'>

# --- Example 2: True division (/) — always returns float ---
print(10 / 2)     # 5.0 (not 5!)
print(7 / 2)      # 3.5
print(9 / 3)      # 3.0
print(type(10/2)) # <class 'float'>

# --- Example 3: Floor division (//) — rounds down ---
print(7 // 2)     # 3
print(10 // 3)    # 3
print(15 // 4)    # 3
print(9 // 3)     # 3

# --- Example 4: Floor division with negatives ---
print(7 // 2)     # 3
print(-7 // 2)    # -4 (rounds DOWN, not toward zero!)
print(7 // -2)    # -4
print(-7 // -2)   # 3

# --- Example 5: Modulo (%) — remainder ---
print(7 % 2)      # 1 (7 = 2*3 + 1)
print(10 % 3)     # 1 (10 = 3*3 + 1)
print(15 % 5)     # 0 (divides evenly)
print(8 % 3)      # 2

# --- Example 6: Modulo use — even or odd ---
print(10 % 2)  # 0 → even
print(7 % 2)   # 1 → odd
print(4 % 2)   # 0 → even

# --- Example 7: Floor division + modulo relationship ---
# a == (a // b) * b + (a % b)
a = 17
b = 5
quotient = a // b   # 3
remainder = a % b   # 2
print(f"{a} = {b} * {quotient} + {remainder}")  # 17 = 5 * 3 + 2

# --- Example 8: Mixed type operations ---
print(type(5 + 3))      # int + int → int
print(type(5 + 3.0))    # int + float → float
print(type(5.0 + 3.0))  # float + float → float
print(type(5 / 3))      # always float
print(type(5 // 3))     # int // int → int

# --- Example 9: Float floor division ---
print(7.0 // 2)     # 3.0 (float // int → float)
print(7 // 2.0)     # 3.0 (int // float → float)
print(7.0 // 2.0)   # 3.0

# --- Example 10: Power operator ---
print(2 ** 3)       # 8
print(3 ** 2)       # 9
print(2 ** 10)      # 1024
print(type(2**3))   # <class 'int'>
print(type(2**0.5)) # <class 'float'> (square root)

# ============================================
# TRY IT YOURSELF:
# 1. Try 10 / 3 vs 10 // 3 vs 10 % 3
# 2. Check: is -7 // 2 equal to -3 or -4?
# 3. Use % to check if a number is even or odd
# ============================================
