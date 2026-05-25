# ============================================
# MODULE 2 - SUBTOPIC 1: Numbers (Numeric Types)
# ============================================

# --- Example 1: Integers ---
x = 42
y = -100
z = 0
print(x, y, z)        # 42 -100 0
print(type(x))         # <class 'int'>

# --- Example 2: Large integers (no limit in Python) ---
big = 999999999999999999999999999999
print(big)
print(type(big))       # still <class 'int'>

# --- Example 3: Underscores for readability ---
population = 1_000_000_000
salary = 50_000
print(population)  # 1000000000
print(salary)      # 50000
# Underscores are ignored — just for humans to read

# --- Example 4: Floats ---
price = 19.99
temperature = -3.5
height = 5.9
print(price, temperature, height)
print(type(price))  # <class 'float'>

# --- Example 5: Float precision behavior ---
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 — not exactly 0.3!
# This is normal — computers store decimals in binary

# --- Example 6: Scientific notation ---
a = 1e3      # 1 × 10^3 = 1000.0
b = 2.5e-4   # 2.5 × 10^-4 = 0.00025
c = 5e6      # 5,000,000.0
print(a)         # 1000.0
print(b)         # 0.00025
print(c)         # 5000000.0
print(type(a))   # <class 'float'>

# --- Example 7: Complex numbers ---
z = 3 + 4j
print(z)         # (3+4j)
print(type(z))   # <class 'complex'>

# --- Example 8: Accessing real and imaginary parts ---
z = 5 + 7j
print(z.real)    # 5.0
print(z.imag)    # 7.0

# --- Example 9: Complex arithmetic ---
a = 2 + 3j
b = 1 + 2j
print(a + b)     # (3+5j)
print(a * b)     # (-4+7j)

# --- Example 10: Mixing types ---
print(type(10))      # <class 'int'>
print(type(10.0))    # <class 'float'>
print(type(10 + 0j)) # <class 'complex'>

# ============================================
# TRY IT YOURSELF:
# 1. Create a very large integer and print it
# 2. Try 0.1 + 0.2 == 0.3 — what does it print?
# 3. Create a complex number and print its real part
# ============================================
