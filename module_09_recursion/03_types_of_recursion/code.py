# ============================================
# MODULE 9 - SUBTOPIC 3: Types of Recursion
# ============================================

# =============================
# 1. DIRECT RECURSION
# =============================

# --- Example 1: Simple direct recursion ---
def countdown(n):
    """Function calls itself directly."""
    if n <= 0:
        print("  Go!")
        return
    print(f"  {n}")
    countdown(n - 1)   # Direct self-call

print("Direct recursion — countdown:")
countdown(5)

# --- Example 2: Sum using direct recursion ---
def direct_sum(n):
    if n <= 0:
        return 0
    return n + direct_sum(n - 1)

print(f"\nDirect sum(10): {direct_sum(10)}")

# =============================
# 2. INDIRECT RECURSION
# =============================

# --- Example 3: is_even / is_odd mutual recursion ---
def is_even(n):
    """Calls is_odd, which calls is_even back."""
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    """Calls is_even, which calls is_odd back."""
    if n == 0:
        return False
    return is_even(n - 1)

print(f"\nIndirect recursion — even/odd:")
for i in range(6):
    print(f"  {i}: even={is_even(i)}, odd={is_odd(i)}")

# --- Example 4: Print alternating patterns ---
def print_a(n):
    if n <= 0:
        return
    print("  A", end=" ")
    print_b(n - 1)   # Calls B

def print_b(n):
    if n <= 0:
        return
    print("B", end=" ")
    print_a(n - 1)   # Calls A

print(f"\nIndirect recursion — alternating:")
print_a(6)
print()

# =============================
# 3. TAIL RECURSION
# =============================

# --- Example 5: Non-tail recursive factorial ---
def factorial(n):
    """NOT tail recursive: n * ... happens after the call returns."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)   # Multiplication waits for result

print(f"\nNon-tail factorial(5): {factorial(5)}")

# --- Example 6: Tail recursive factorial ---
def factorial_tail(n, accumulator=1):
    """Tail recursive: the recursive call is the LAST operation."""
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, accumulator * n)
    # Nothing happens after this call returns — it IS the result

print(f"Tail factorial(5): {factorial_tail(5)}")

# --- Example 7: Comparing the two approaches ---
def factorial_trace(n, depth=0):
    indent = "  " * depth
    print(f"{indent}factorial({n})")
    if n <= 1:
        return 1
    result = n * factorial_trace(n - 1, depth + 1)
    print(f"{indent}  {n} * ... = {result}")   # Work after return
    return result

def factorial_tail_trace(n, acc=1, depth=0):
    indent = "  " * depth
    print(f"{indent}factorial_tail({n}, acc={acc})")
    if n <= 1:
        return acc
    return factorial_tail_trace(n - 1, acc * n, depth + 1)
    # No work after return!

print(f"\n--- Non-tail (work happens AFTER return): ---")
factorial_trace(4)

print(f"\n--- Tail (all work in arguments): ---")
factorial_tail_trace(4)

# =============================
# 4. TAIL RECURSION EXAMPLES
# =============================

# --- Example 8: Tail recursive sum ---
def sum_tail(n, acc=0):
    if n <= 0:
        return acc
    return sum_tail(n - 1, acc + n)

print(f"\nTail sum(100): {sum_tail(100)}")

# --- Example 9: Tail recursive GCD ---
def gcd(a, b):
    """Euclidean algorithm — naturally tail recursive."""
    if b == 0:
        return a
    return gcd(b, a % b)

print(f"\ngcd(48, 18): {gcd(48, 18)}")    # 6
print(f"gcd(100, 75): {gcd(100, 75)}")    # 25

# --- Example 10: Tail recursive reverse ---
def reverse_tail(s, acc=""):
    if len(s) == 0:
        return acc
    return reverse_tail(s[1:], s[0] + acc)

print(f"\nTail reverse('hello'): {reverse_tail('hello')}")

# =============================
# 5. PYTHON LIMITATION NOTE
# =============================

# --- Example 11: Python doesn't optimize tail recursion ---
# In languages like Scheme or Haskell, tail recursion uses constant stack space.
# In Python, EVERY recursive call still uses a new stack frame.

# This means: even tail recursive functions can hit Python's recursion limit.
# For very deep recursion, convert to a loop:

def sum_loop(n):
    """Equivalent of sum_tail, but as a loop — no recursion limit."""
    total = 0
    while n > 0:
        total = total + n
        n = n - 1
    return total

print(f"\nLoop sum(1000): {sum_loop(1000)}")
# sum_tail(1000) might work, but sum_tail(10000) would crash!

# ============================================
# TRY IT YOURSELF:
# 1. Convert a non-tail recursive function to tail recursive
# 2. Write an indirect recursion pair (func_a calls func_b, vice versa)
# 3. Write a tail-recursive version of power(base, exp)
# ============================================
