# ============================================
# MODULE 15 - SUBTOPIC 7: Generator Expressions
# ============================================

# Generator expressions are like list comprehensions,
# but produce values lazily using () instead of [].

# =============================
# 1. BASIC SYNTAX
# =============================

print("=== Basic Syntax ===")
print()

# List comprehension → creates a list
squares_list = [x**2 for x in range(6)]

# Generator expression → creates a generator
squares_gen = (x**2 for x in range(6))

print(f"  List comprehension: {squares_list}")
print(f"  Generator expression: {squares_gen}")
print(f"  Type of list: {type(squares_list)}")
print(f"  Type of generator: {type(squares_gen)}")
print()

# Convert generator to list to see values
print(f"  list(squares_gen): {list(squares_gen)}")
print()

# =============================
# 2. COMPARISON: [] vs ()
# =============================

print("=== List Comprehension vs Generator Expression ===")
print()

# Both produce the same values
nums_list = [n * 10 for n in range(5)]
nums_gen = (n * 10 for n in range(5))

print(f"  List: {nums_list}")
print(f"  Generator values: {list(nums_gen)}")
print()

# Key difference: memory
# The list stores ALL values at once
# The generator produces ONE at a time

# =============================
# 3. USING next() WITH GENERATOR EXPRESSIONS
# =============================

print("=== Using next() ===")
print()

gen = (x**3 for x in range(1, 6))

print(f"  next() = {next(gen)}")   # 1
print(f"  next() = {next(gen)}")   # 8
print(f"  next() = {next(gen)}")   # 27
print(f"  next() = {next(gen)}")   # 64
print(f"  next() = {next(gen)}")   # 125
print()

# =============================
# 4. WITH BUILT-IN FUNCTIONS
# =============================

print("=== With Built-in Functions ===")
print()

# sum() — no extra parentheses needed inside function call!
total = sum(x**2 for x in range(1, 11))
print(f"  sum(x² for x in 1..10) = {total}")

# max()
longest = max(len(w) for w in ["cat", "elephant", "dog", "hippopotamus"])
print(f"  Longest word length: {longest}")

# min()
smallest_sq = min(x**2 for x in range(-5, 6) if x != 0)
print(f"  Smallest non-zero square: {smallest_sq}")

# any()
has_negative = any(x < 0 for x in [1, 2, -3, 4])
print(f"  Has negative number? {has_negative}")

# all()
all_positive = all(x > 0 for x in [1, 2, 3, 4])
print(f"  All positive? {all_positive}")
print()

# =============================
# 5. WITH FILTERING
# =============================

print("=== With Conditions (Filtering) ===")
print()

# Even squares
even_squares = (x**2 for x in range(10) if x % 2 == 0)
print(f"  Even squares: {list(even_squares)}")

# Words starting with 'p'
words = ["python", "java", "perl", "php", "go", "pascal"]
p_words = (w for w in words if w.startswith("p"))
print(f"  P-words: {list(p_words)}")

# Numbers divisible by 3 or 5
special = (n for n in range(1, 21) if n % 3 == 0 or n % 5 == 0)
print(f"  Divisible by 3 or 5: {list(special)}")
print()

# =============================
# 6. GENERATOR EXHAUSTION
# =============================

print("=== Generator Exhaustion ===")
print()

gen = (x for x in range(3))

print("  First iteration:")
print(f"    {list(gen)}")

print("  Second iteration (exhausted!):")
print(f"    {list(gen)}")
print()

# Lists can be iterated multiple times
lst = [x for x in range(3)]
print(f"  List — first:  {lst}")
print(f"  List — second: {lst}")
print("  → Lists are reusable, generators are not!")
print()

# =============================
# 7. NESTED GENERATOR EXPRESSIONS
# =============================

print("=== Nested Expressions ===")
print()

# Flatten a 2D structure
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = (num for row in matrix for num in row)
print(f"  Matrix: {matrix}")
print(f"  Flattened: {list(flat)}")
print()

# All pairs
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
combos = (f"{c}-{s}" for c in colors for s in sizes)
print(f"  Combinations: {list(combos)}")
print()

# =============================
# 8. PRACTICAL EXAMPLES
# =============================

print("=== Practical Examples ===")
print()

# Reading: sum of string lengths
names = ["Trush", "Rahul", "Charlie", "Diana"]
total_chars = sum(len(name) for name in names)
print(f"  Names: {names}")
print(f"  Total characters: {total_chars}")

# Joining with transformation
upper_names = ", ".join(n.upper() for n in names)
print(f"  Upper names: {upper_names}")

# Finding: first match
numbers = [4, 7, 2, 9, 1, 8, 3]
first_big = next((n for n in numbers if n > 5), None)
print(f"  Numbers: {numbers}")
print(f"  First > 5: {first_big}")

# No match
first_huge = next((n for n in numbers if n > 100), None)
print(f"  First > 100: {first_huge}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a generator expression for cubes of 1-10
# 2. Use sum() with a generator expression (no extra parens!)
# 3. Use next() to find the first even number in a list
# ============================================
