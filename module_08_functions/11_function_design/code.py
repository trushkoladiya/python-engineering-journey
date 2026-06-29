# ============================================
# MODULE 8 - SUBTOPIC 11: Function Design Principles
# ============================================

# =============================
# 1. SINGLE RESPONSIBILITY
# =============================

# --- Example 1: Bad — doing too many things ---
def process_order_bad(items, prices):
    # Calculates total, applies discount, prints receipt, ALL in one
    total = 0
    for i in range(len(items)):
        total = total + prices[i]
    if total > 100:
        total = total * 0.9
    print("--- Receipt ---")
    for i in range(len(items)):
        print(f"  {items[i]}: ${prices[i]:.2f}")
    print(f"  Total: ${total:.2f}")

# --- Example 2: Good — each function does one thing ---
def calculate_total(prices):
    """Calculate the sum of all prices."""
    return sum(prices)

def apply_discount(total, threshold=100, discount=0.10):
    """Apply discount if total exceeds threshold."""
    if total > threshold:
        return total * (1 - discount)
    return total

def print_receipt(items, prices, final_total):
    """Display a formatted receipt."""
    print("\n--- Receipt ---")
    for item, price in zip(items, prices):
        print(f"  {item}: ${price:.2f}")
    print(f"  Total: ${final_total:.2f}")

# Using the clean functions:
items = ["Burger", "Pizza", "Salad", "Drink", "Dessert"]
prices = [12.99, 15.50, 8.75, 3.50, 7.25]

total = calculate_total(prices)
final = apply_discount(total)
print_receipt(items, prices, final)

# =============================
# 2. REUSABILITY
# =============================

# --- Example 3: Too specific (not reusable) ---
def add_5_and_3():
    return 5 + 3

# --- Example 4: Reusable version ---
def add(a, b):
    """Return the sum of any two numbers."""
    return a + b

print(f"\nadd(5, 3) = {add(5, 3)}")
print(f"add(100, 200) = {add(100, 200)}")
print(f"add(1.5, 2.5) = {add(1.5, 2.5)}")

# --- Example 5: Reusable validation ---
def is_valid_score(score, min_val=0, max_val=100):
    """Check if score is within valid range."""
    return min_val <= score <= max_val

# Works for any range!
print(f"\nis_valid_score(85): {is_valid_score(85)}")
print(f"is_valid_score(150): {is_valid_score(150)}")
print(f"is_valid_score(3, 1, 5): {is_valid_score(3, 1, 5)}")

# =============================
# 3. READABILITY
# =============================

# --- Example 6: Bad names ---
def p(x):
    return x > 0

def f(a, b):
    return a ** b

# --- Example 7: Good names ---
def is_positive(number):
    """Check if a number is positive."""
    return number > 0

def power(base, exponent):
    """Raise base to the given exponent."""
    return base ** exponent

print(f"\nis_positive(5): {is_positive(5)}")
print(f"is_positive(-3): {is_positive(-3)}")
print(f"power(2, 10): {power(2, 10)}")

# =============================
# 4. KEEP FUNCTIONS SHORT
# =============================

# --- Example 8: Breaking a complex task into small functions ---
def get_grade(score):
    """Convert a score to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"

def calculate_average(scores):
    """Calculate the average of a list of scores."""
    return sum(scores) / len(scores)

def format_report(name, scores):
    """Generate a formatted student report."""
    avg = calculate_average(scores)
    grade = get_grade(avg)
    return f"{name}: avg={avg:.1f}, grade={grade}"

# Using the small, focused functions:
students = {
    "Trush": [92, 88, 95],
    "Rahul": [78, 82, 75],
    "Charlie": [65, 70, 60],
}

print("\n--- Student Reports ---")
for name, scores in students.items():
    print(f"  {format_report(name, scores)}")

# =============================
# 5. PURE vs IMPURE FUNCTIONS
# =============================

# --- Example 9: Pure function — no side effects ---
def multiply(a, b):
    """Pure: same input always gives same output."""
    return a * b

# Always returns 15 for (3, 5)
print(f"\nPure: multiply(3, 5) = {multiply(3, 5)}")
print(f"Pure: multiply(3, 5) = {multiply(3, 5)}")

# --- Example 10: Impure function — has side effects ---
call_count = 0

def multiply_impure(a, b):
    """Impure: modifies external state."""
    global call_count
    call_count = call_count + 1
    return a * b

print(f"\nImpure: multiply_impure(3, 5) = {multiply_impure(3, 5)}")
print(f"Side effect: call_count = {call_count}")
multiply_impure(2, 4)
print(f"Side effect: call_count = {call_count}")

# --- Example 11: Prefer pure functions ---
# ❌ Impure — modifies the input list
def sort_list_bad(items):
    items.sort()   # Modifies original!
    return items

# ✅ Pure — returns a new list
def sort_list_good(items):
    return sorted(items)   # Original unchanged

original = [3, 1, 4, 1, 5]
sorted_version = sort_list_good(original)
print(f"\nOriginal: {original}")      # Unchanged
print(f"Sorted: {sorted_version}")

# ============================================
# TRY IT YOURSELF:
# 1. Refactor a long function into 2-3 smaller functions
# 2. Rename a function and its parameters for clarity
# 3. Convert an impure function to a pure one
# ============================================
