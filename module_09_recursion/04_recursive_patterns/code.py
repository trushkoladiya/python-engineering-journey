# ============================================
# MODULE 9 - SUBTOPIC 4: Basic Recursive Patterns
# ============================================

# =============================
# 1. LINEAR RECURSION
# =============================

# --- Example 1: Factorial — one call per level ---
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)   # ONE recursive call

print("Linear: factorial(6) =", factorial(6))   # 720

# --- Example 2: Linear sum ---
def linear_sum(items):
    if len(items) == 0:
        return 0
    return items[0] + linear_sum(items[1:])   # ONE call

print("Linear: sum([1,2,3,4,5]) =", linear_sum([1, 2, 3, 4, 5]))

# --- Example 3: Count calls in linear recursion ---
def factorial_counted(n, counter):
    counter[0] += 1
    if n <= 1:
        return 1
    return n * factorial_counted(n - 1, counter)

count = [0]
factorial_counted(10, count)
print(f"\nLinear factorial(10): {count[0]} calls")   # 10 calls

# =============================
# 2. BINARY / TREE RECURSION
# =============================

# --- Example 4: Fibonacci — two calls per level ---
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # TWO recursive calls

print(f"\nTree: fibonacci(8) = {fibonacci(8)}")

# --- Example 5: Count calls in tree recursion ---
def fibonacci_counted(n, counter):
    counter[0] += 1
    if n <= 1:
        return n
    return fibonacci_counted(n - 1, counter) + fibonacci_counted(n - 2, counter)

count = [0]
fibonacci_counted(10, count)
print(f"Tree fibonacci(10): {count[0]} calls")   # Many more calls!

count2 = [0]
fibonacci_counted(20, count2)
print(f"Tree fibonacci(20): {count2[0]} calls")   # Grows exponentially!

# --- Example 6: Visualizing tree recursion ---
def fib_tree(n, depth=0):
    indent = "  " * depth
    if n <= 1:
        print(f"{indent}fib({n}) = {n}")
        return n
    print(f"{indent}fib({n})")
    left = fib_tree(n - 1, depth + 1)
    right = fib_tree(n - 2, depth + 1)
    result = left + right
    print(f"{indent}fib({n}) = {left} + {right} = {result}")
    return result

print(f"\nTree recursion visualization:")
fib_tree(4)

# =============================
# 3. COMPARING LINEAR vs TREE
# =============================

# --- Example 7: Same problem, different patterns ---
# Linear approach to sum: n calls
def sum_linear(n):
    if n <= 0: return 0
    return n + sum_linear(n - 1)

# Tree approach to sum (splitting in half): log(n) depth but same total work
def sum_tree(items):
    if len(items) == 0:
        return 0
    if len(items) == 1:
        return items[0]
    mid = len(items) // 2
    return sum_tree(items[:mid]) + sum_tree(items[mid:])

numbers = list(range(1, 11))
print(f"\nLinear sum: {sum_linear(10)}")
print(f"Tree sum: {sum_tree(numbers)}")

# --- Example 8: Power — linear vs fast ---
# Linear: O(n) calls
def power_linear(base, exp):
    if exp == 0: return 1
    return base * power_linear(base, exp - 1)

# Fast power (divide and conquer): O(log n) calls
def power_fast(base, exp):
    if exp == 0: return 1
    if exp % 2 == 0:
        half = power_fast(base, exp // 2)
        return half * half        # Reuse the result!
    return base * power_fast(base, exp - 1)

print(f"\nLinear power(2, 10) = {power_linear(2, 10)}")
print(f"Fast power(2, 10) = {power_fast(2, 10)}")

# Count calls for each
count_lin = [0]
count_fast = [0]

def power_linear_c(base, exp, c):
    c[0] += 1
    if exp == 0: return 1
    return base * power_linear_c(base, exp - 1, c)

def power_fast_c(base, exp, c):
    c[0] += 1
    if exp == 0: return 1
    if exp % 2 == 0:
        half = power_fast_c(base, exp // 2, c)
        return half * half
    return base * power_fast_c(base, exp - 1, c)

power_linear_c(2, 20, count_lin)
power_fast_c(2, 20, count_fast)
print(f"\npower(2, 20):")
print(f"  Linear: {count_lin[0]} calls")
print(f"  Fast:   {count_fast[0]} calls")

# ============================================
# TRY IT YOURSELF:
# 1. Count the number of calls in factorial(15) vs fibonacci(15)
# 2. Write a tree-recursive function to find the max in a list
# 3. Implement fast power for base^1000 and verify the call count
# ============================================
