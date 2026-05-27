# ============================================
# MODULE 2 - SUBTOPIC 7: Type Conversion (Advanced)
# ============================================

# --- Example 1: int() truncates (chops off decimal) ---
print(int(3.99))    # 3 (NOT 4 — no rounding!)
print(int(7.1))     # 7
print(int(-2.9))    # -2 (truncates toward zero)

# --- Example 2: round() actually rounds ---
print(round(3.5))      # 4
print(round(3.14))     # 3
print(round(2.718))    # 3
print(round(3.14159, 2))  # 3.14 (round to 2 decimal places)
print(round(3.14159, 3))  # 3.142

# --- Example 3: Chained conversion ---
text = "3.14"
# int(text)  # ❌ Would fail!
result = int(float(text))  # ✅ string → float → int
print(result)  # 3

# --- Example 4: Whitespace is stripped automatically ---
print(int("  42  "))     # 42
print(float(" 3.14 "))   # 3.14

# --- Example 5: Converting bool to other types ---
print(int(True))     # 1
print(int(False))    # 0
print(float(True))   # 1.0
print(str(True))     # "True"

# --- Example 6: Converting to bool ---
print(bool(42))       # True
print(bool(0))        # False
print(bool("hello"))  # True
print(bool(""))       # False
print(bool(None))     # False

# --- Example 7: ord() — character to number ---
print(ord("A"))   # 65
print(ord("B"))   # 66
print(ord("a"))   # 97
print(ord("z"))   # 122
print(ord("0"))   # 48

# --- Example 8: chr() — number to character ---
print(chr(65))    # A
print(chr(66))    # B
print(chr(97))    # a
print(chr(48))    # 0
print(chr(9731))  # ☃ (snowman!)

# --- Example 9: Practical — converting between types ---
price_text = "49.99"
price = float(price_text)
whole_price = int(price)
display = str(whole_price)
print(f"Original: {price_text}")
print(f"As float: {price}")
print(f"As int: {whole_price}")
print(f"As string: {display}")

# ============================================
# TRY IT YOURSELF:
# 1. Try int(3.99) vs round(3.99) — see the difference
# 2. Find the ord() of 'T' (Trush's first initial)
# 3. Try int("3.14") — see the error, then fix it
# ============================================
