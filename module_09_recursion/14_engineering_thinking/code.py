# ============================================
# MODULE 9 - SUBTOPIC 14: Engineering-Level Thinking
# ============================================

# =============================
# 1. THE 3-QUESTION METHOD
# =============================
# For ANY problem, ask:
#   Q1: What's the simplest version? (base case)
#   Q2: If I had the answer for smaller input, how do I build the full answer?
#   Q3: What gets smaller each call?

# --- Example 1: Design — count occurrences in nested list ---
# Q1: Empty list → 0 occurrences
# Q2: Check first element, add to count of the rest
# Q3: The list gets shorter

def count_in_nested(data, target):
    """Count occurrences of target in a nested structure."""
    if isinstance(data, list):
        if len(data) == 0:
            return 0   # Q1: base case
        return count_in_nested(data[0], target) + count_in_nested(data[1:], target)
    # Leaf node
    return 1 if data == target else 0

nested = [1, [2, 1, [3, 1]], [1, [1, 2]]]
print(f"Count 1 in {nested}: {count_in_nested(nested, 1)}")   # 5

# =============================
# 2. TRUST THE RECURSION
# =============================

# --- Example 2: Don't trace — trust it ---
# Design one level at a time. Assume the recursive call gives the correct answer.

def sorted_insert(sorted_list, value):
    """Insert value into its correct position in a sorted list."""
    # Q1: empty list or value belongs at the start
    if len(sorted_list) == 0 or value <= sorted_list[0]:
        return [value] + sorted_list
    # Q2: Trust that sorted_insert works for the rest
    return [sorted_list[0]] + sorted_insert(sorted_list[1:], value)

def insertion_sort(items):
    """Sort using recursive insertion."""
    if len(items) <= 1:
        return items
    # Trust: insertion_sort(items[1:]) returns a sorted list
    sorted_rest = insertion_sort(items[1:])
    # Insert first element into the sorted rest
    return sorted_insert(sorted_rest, items[0])

data = [5, 3, 8, 1, 9, 2]
print(f"\nInsertion sort:")
print(f"  Input:  {data}")
print(f"  Sorted: {insertion_sort(data)}")

# =============================
# 3. REAL PROBLEM: EXPRESSION EVALUATOR
# =============================

# --- Example 3: Evaluate nested math expressions ---
# Expression format: [operator, operand1, operand2]
# operands can be numbers or nested expressions

def evaluate(expr):
    """Evaluate a nested expression like ['+', 3, ['*', 2, 5]]."""
    # Base case: it's just a number
    if isinstance(expr, (int, float)):
        return expr
    
    op = expr[0]
    # Trust: evaluate works on sub-expressions
    left = evaluate(expr[1])
    right = evaluate(expr[2])
    
    if op == '+': return left + right
    if op == '-': return left - right
    if op == '*': return left * right
    if op == '/': return left / right

# 3 + (2 * 5) = 13
expr1 = ['+', 3, ['*', 2, 5]]
print(f"\nExpression evaluator:")
print(f"  {expr1} = {evaluate(expr1)}")

# (10 - 3) * (2 + 5) = 49
expr2 = ['*', ['-', 10, 3], ['+', 2, 5]]
print(f"  {expr2} = {evaluate(expr2)}")

# ((1 + 2) * (3 + 4)) - 5 = 16
expr3 = ['-', ['*', ['+', 1, 2], ['+', 3, 4]], 5]
print(f"  {expr3} = {evaluate(expr3)}")

# =============================
# 4. REAL PROBLEM: DEEP COMPARISON
# =============================

# --- Example 4: Compare two nested structures ---
def deep_equal(a, b):
    """Check if two nested structures are equal."""
    if type(a) != type(b):
        return False
    if isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        return all(deep_equal(a[k], b[k]) for k in a)
    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        return all(deep_equal(x, y) for x, y in zip(a, b))
    return a == b

data1 = {"a": [1, {"b": 2}], "c": 3}
data2 = {"a": [1, {"b": 2}], "c": 3}
data3 = {"a": [1, {"b": 9}], "c": 3}

print(f"\nDeep comparison:")
print(f"  data1 == data2: {deep_equal(data1, data2)}")   # True
print(f"  data1 == data3: {deep_equal(data1, data3)}")   # False

# =============================
# 5. REAL PROBLEM: JSON-LIKE FORMATTER
# =============================

# --- Example 5: Pretty print nested data ---
def pretty_print(data, indent=0):
    """Format nested data with indentation."""
    prefix = "  " * indent
    if isinstance(data, dict):
        print(f"{prefix}{{")
        for key, value in data.items():
            print(f"{prefix}  {key}:")
            pretty_print(value, indent + 2)
        print(f"{prefix}}}")
    elif isinstance(data, list):
        print(f"{prefix}[")
        for item in data:
            pretty_print(item, indent + 1)
        print(f"{prefix}]")
    else:
        print(f"{prefix}{data}")

config = {
    "app": {
        "name": "MyApp",
        "version": 2,
        "features": ["auth", "api", "dashboard"],
    },
    "debug": True,
}

print(f"\nPretty print:")
pretty_print(config)

# =============================
# 6. DESIGN PATTERN RECOGNITION
# =============================

# --- Example 6: Summary of patterns ---
print(f"""
╔═══════════════════════════════════════════════╗
║     RECURSIVE PATTERN RECOGNITION             ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  "Process each element"     → Linear          ║
║  "Find all combinations"   → Backtracking     ║
║  "Split and merge"         → Divide & Conquer ║
║  "Nested structure"        → Tree recursion   ║
║  "Same subproblem again"   → Memoize it!      ║
║                                               ║
║  STEPS:                                       ║
║  1. Identify the pattern                      ║
║  2. Define base case                          ║
║  3. Define recursive case                     ║
║  4. Trust the recursion                       ║
║  5. Test with small inputs                    ║
║                                               ║
╚═══════════════════════════════════════════════╝
""")

# ============================================
# TRY IT YOURSELF:
# 1. Design a recursive function to find all paths in a dictionary
# 2. Build a recursive calculator that handles +, -, *, /
# 3. Write a recursive function to deep-copy any nested structure
# ============================================
