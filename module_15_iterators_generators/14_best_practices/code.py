# ============================================
# MODULE 15 - SUBTOPIC 14: Best Practices
# ============================================

# Clean, professional patterns for iterators and generators.

import sys
import itertools

# =============================
# 1. CHOOSE THE RIGHT TOOL
# =============================

print("=== Choose the Right Tool ===")
print()

# GENERATOR: large data, single pass, streaming
def process_large_data():
    """Generator — processes one item at a time."""
    for i in range(1_000_000):
        yield i ** 2

# LIST: small data, multiple passes, random access
def get_top_scores():
    """List — small, reusable, indexable."""
    return [95, 87, 92, 88, 91]

# Show the difference
gen = process_large_data()
lst = get_top_scores()

print(f"  Generator (1M items): {sys.getsizeof(gen):>6} bytes")
print(f"  List (5 items):       {sys.getsizeof(lst):>6} bytes")
print()
print("  Generator → when data is large or streaming")
print("  List      → when data is small or needs reuse")
print()

# =============================
# 2. KEEP GENERATORS SIMPLE
# =============================

print("=== Keep Generators Simple ===")
print()

# BAD: one giant generator doing everything
def bad_process_data(raw_items):
    """Too much responsibility in one generator."""
    for item in raw_items:
        cleaned = item.strip().lower()
        if cleaned and not cleaned.startswith("#"):
            parts = cleaned.split(":")
            if len(parts) == 2:
                key, val = parts
                try:
                    yield key.strip(), int(val.strip())
                except ValueError:
                    continue

# GOOD: small composable generators
def clean_lines(lines):
    """Remove whitespace."""
    for line in lines:
        yield line.strip().lower()

def skip_comments(lines):
    """Skip comment lines."""
    for line in lines:
        if line and not line.startswith("#"):
            yield line

def parse_pairs(lines):
    """Parse 'key: value' pairs."""
    for line in lines:
        parts = line.split(":")
        if len(parts) == 2:
            yield parts[0].strip(), parts[1].strip()

def values_as_int(pairs):
    """Convert values to integers."""
    for key, val in pairs:
        try:
            yield key, int(val)
        except ValueError:
            continue

# Use the composable pipeline
raw = [
    "  Name: Trush  ",
    "# This is a comment",
    "  Age: 30  ",
    "  Score: 95  ",
    "  Invalid: abc  ",
    "  Level: 5  ",
]

pipeline = values_as_int(parse_pairs(skip_comments(clean_lines(raw))))
print("  Composable pipeline result:")
for key, val in pipeline:
    print(f"    {key} = {val}")
print()

# =============================
# 3. USE yield from
# =============================

print("=== Use yield from ===")
print()

# WITHOUT yield from (verbose)
def combine_old(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

# WITH yield from (clean)
def combine_new(*iterables):
    for iterable in iterables:
        yield from iterable

result_old = list(combine_old([1, 2], [3, 4], [5]))
result_new = list(combine_new([1, 2], [3, 4], [5]))

print(f"  Without yield from: {result_old}")
print(f"  With yield from:    {result_new}")
print("  → Same result, cleaner code!")
print()

# yield from with recursive generators
def tree_values(tree):
    """Traverse a nested dict/list structure."""
    if isinstance(tree, dict):
        for key, value in tree.items():
            yield key
            yield from tree_values(value)
    elif isinstance(tree, (list, tuple)):
        for item in tree:
            yield from tree_values(item)
    else:
        yield tree

data = {"a": 1, "b": [2, 3], "c": {"d": 4, "e": 5}}
print(f"  Tree: {data}")
print(f"  All values: {list(tree_values(data))}")
print()

# =============================
# 4. NAME GENERATORS CLEARLY
# =============================

print("=== Name Generators Clearly ===")
print()

print("  Good names (describe what they PRODUCE):")
print("    ✅ read_lines(file)")
print("    ✅ parse_records(lines)")
print("    ✅ filter_active(users)")
print("    ✅ generate_ids()")
print("    ✅ fibonacci()")
print()
print("  Bad names (vague or misleading):")
print("    ❌ process(data)       ← what does it produce?")
print("    ❌ do_stuff(items)     ← meaningless")
print("    ❌ get_data()          ← sounds like it returns a list")
print()

# =============================
# 5. DOCUMENT GENERATOR BEHAVIOR
# =============================

print("=== Document Generator Behavior ===")
print()

def fibonacci(max_count=None):
    """Yield Fibonacci numbers.

    Args:
        max_count: Maximum numbers to yield.
                   None for infinite sequence.

    Yields:
        int: Next Fibonacci number.

    Example:
        >>> list(fibonacci(5))
        [0, 1, 1, 2, 3]
    """
    a, b = 0, 1
    count = 0
    while max_count is None or count < max_count:
        yield a
        a, b = b, a + b
        count += 1

print(f"  fibonacci(8): {list(fibonacci(8))}")
print(f"  Docstring says: Yields Fibonacci numbers")
print("  → Clear documentation prevents misuse!")
print()

# =============================
# 6. MAKE REUSABLE ITERABLES
# =============================

print("=== Make Reusable Iterables (When Needed) ===")
print()

# Generator: single use
gen = (x ** 2 for x in range(5))
print(f"  Generator first pass:  {list(gen)}")
print(f"  Generator second pass: {list(gen)}")
print()

# Reusable: class-based iterable
class Squares:
    """Reusable iterable — creates new iterator each time."""
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            yield i ** 2

sq = Squares(5)
print(f"  Squares first pass:  {list(sq)}")
print(f"  Squares second pass: {list(sq)}")
print("  → Class-based iterable is reusable!")
print()

# =============================
# 7. PREFER GENERATOR EXPRESSIONS FOR SIMPLE CASES
# =============================

print("=== Generator Expressions vs Functions ===")
print()

# For simple transformations, use expressions
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Expression (simple, inline)
evens_expr = sum(x for x in data if x % 2 == 0)

# Function (overkill for this)
def even_sum(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

evens_func = sum(even_sum(data))

print(f"  Expression: sum(x for x if even) = {evens_expr}")
print(f"  Function:   sum(even_sum(data))   = {evens_func}")
print("  → Use expressions for simple one-liners")
print("  → Use functions for complex logic")
print()

# =============================
# 8. COMPLETE CHECKLIST
# =============================

print("=== Best Practices Checklist ===")
print()

checklist = [
    "Use generators for large/streaming data",
    "Use lists for small/reusable data",
    "Keep generators small and focused",
    "Compose small generators into pipelines",
    "Use yield from for delegation",
    "Name generators by what they produce",
    "Document: yields vs returns",
    "Use generator expressions for simple cases",
    "Use class-based iterables when reuse needed",
    "Never modify collections while iterating",
    "Remember: generators exhaust after one pass",
    "Use itertools for common patterns",
]

for item in checklist:
    print(f"  ✅ {item}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Refactor a complex generator into composable steps
# 2. Create a reusable iterable class with __iter__
# 3. Replace a list comprehension with a generator expression
# ============================================
