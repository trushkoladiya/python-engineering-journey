# ============================================
# MODULE 9 - SUBTOPIC 2: Call Stack Understanding
# ============================================

# =============================
# 1. VISUALIZING THE CALL STACK
# =============================

# --- Example 1: Tracing calls with indentation ---
def factorial(n, depth=0):
    indent = "  " * depth
    print(f"{indent}→ factorial({n}) called")
    
    if n <= 1:
        print(f"{indent}← factorial({n}) returns 1")
        return 1
    
    result = n * factorial(n - 1, depth + 1)
    print(f"{indent}← factorial({n}) returns {result}")
    return result

print("Tracing factorial(5):")
answer = factorial(5)
print(f"Final answer: {answer}\n")

# =============================
# 2. STACK FRAMES — EACH CALL HAS ITS OWN VARIABLES
# =============================

# --- Example 2: Showing local variables per call ---
def countdown(n):
    print(f"  ENTER: n = {n} (id of n: {id(n)})")
    if n <= 0:
        print(f"  BASE CASE reached")
        return
    countdown(n - 1)
    print(f"  EXIT:  n = {n}")   # n is still its original value!

print("Countdown with stack trace:")
countdown(4)

# --- Example 3: Proving each call has separate variables ---
def accumulate(n):
    """Each call has its own 'n' — they don't share."""
    if n <= 0:
        return 0
    local_value = n * 10   # Each frame has its own local_value
    result = local_value + accumulate(n - 1)
    print(f"  n={n}, local_value={local_value}, accumulated={result}")
    return result

print(f"\nAccumulate(4):")
print(f"Result: {accumulate(4)}")   # 10 + 20 + 30 + 40 = 100

# =============================
# 3. LIFO — LAST IN, FIRST OUT
# =============================

# --- Example 4: Order of execution ---
def print_order(n):
    if n <= 0:
        return
    print(f"  Before recursive call: n={n}")
    print_order(n - 1)
    print(f"  After recursive call:  n={n}")   # Runs in REVERSE order

print(f"\nLIFO demonstration:")
print_order(3)

# --- Example 5: Building on the way UP ---
def reverse_count(n):
    """Prints numbers in reverse using post-recursion execution."""
    if n <= 0:
        return
    reverse_count(n - 1)   # Go deeper first
    print(f"  {n}")         # Print on the way BACK UP

print(f"\nReverse counting (prints after recursion returns):")
reverse_count(5)

# =============================
# 4. CALL STACK DEPTH
# =============================

# --- Example 6: Tracking recursion depth ---
def show_depth(n, depth=1):
    print(f"{'  ' * depth}Depth {depth}: processing n={n}")
    if n <= 1:
        print(f"{'  ' * depth}Max depth reached: {depth}")
        return depth
    return show_depth(n - 1, depth + 1)

print(f"\nCall stack depth for sum_to(6):")
max_depth = show_depth(6)
print(f"Total depth: {max_depth}")

# --- Example 7: Visualizing the stack as a list ---
def factorial_with_stack(n, stack=None):
    if stack is None:
        stack = []
    
    stack.append(f"factorial({n})")
    print(f"  Stack: {stack}")
    
    if n <= 1:
        result = 1
    else:
        result = n * factorial_with_stack(n - 1, stack)
    
    stack.pop()
    return result

print(f"\nStack visualization:")
result = factorial_with_stack(5)
print(f"Result: {result}")

# =============================
# 5. PRE-RECURSION vs POST-RECURSION CODE
# =============================

# --- Example 8: Code runs BEFORE and AFTER the recursive call ---
def process(n):
    if n <= 0:
        print("  [Base case]")
        return
    
    # PRE-RECURSION: runs on the way DOWN
    print(f"  Going DOWN: n={n}")
    
    process(n - 1)
    
    # POST-RECURSION: runs on the way UP
    print(f"  Coming UP:  n={n}")

print(f"\nPre vs Post recursion:")
process(3)

# =============================
# 6. PRACTICAL: STRING REVERSAL EXPLAINED
# =============================

# --- Example 9: Step-by-step string reversal ---
def reverse(s, depth=0):
    indent = "  " * depth
    print(f"{indent}reverse('{s}')")
    
    if len(s) <= 1:
        print(f"{indent}→ returns '{s}'")
        return s
    
    result = reverse(s[1:], depth + 1) + s[0]
    print(f"{indent}→ returns '{result}'")
    return result

print(f"\nString reversal traced:")
result = reverse("ABC")
print(f"Final: '{result}'")

# ============================================
# TRY IT YOURSELF:
# 1. Trace the call stack for power(2, 4) by adding print statements
# 2. Write a function that prints numbers 1-to-n using POST-recursion
# 3. Track the maximum stack depth of fibonacci(6)
# ============================================
