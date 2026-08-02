# ============================================
# MODULE 16 - SUBTOPIC 10: Function Composition
# ============================================

# Function composition = chaining small functions together.
# Output of one function becomes input of the next.

from functools import reduce

# =============================
# 1. BASIC COMPOSITION
# =============================

print("=== Basic Function Composition ===")
print()

def double(x):
    return x * 2

def add_one(x):
    return x + 1

def square(x):
    return x ** 2

# Manual nesting — hard to read
result = add_one(double(square(3)))
# square(3)=9, double(9)=18, add_one(18)=19
print(f"  add_one(double(square(3))) = {result}")
print()

# =============================
# 2. COMPOSE TWO FUNCTIONS
# =============================

print("=== Composing Two Functions ===")
print()

def compose_two(f, g):
    """Return a new function: first apply f, then g."""
    def composed(x):
        return g(f(x))
    return composed

double_then_add = compose_two(double, add_one)
square_then_double = compose_two(square, double)

print(f"  double_then_add(5) = {double_then_add(5)}")       # 5*2=10, 10+1=11
print(f"  square_then_double(4) = {square_then_double(4)}") # 4²=16, 16*2=32
print()

# =============================
# 3. COMPOSING MULTIPLE FUNCTIONS
# =============================

print("=== Composing Multiple Functions ===")
print()

def pipeline(*functions):
    """Chain any number of functions into one."""
    def apply(value, func):
        return func(value)
    def composed(x):
        return reduce(apply, functions, x)
    return composed

# Build a number pipeline
number_pipeline = pipeline(
    lambda x: x + 1,      # add 1
    lambda x: x * 2,      # double
    lambda x: x ** 2,     # square
)

print(f"  pipeline(5): {number_pipeline(5)}")
# 5+1=6, 6*2=12, 12²=144
print(f"  Steps: 5 → +1=6 → ×2=12 → ²=144")
print()

# =============================
# 4. STRING PROCESSING PIPELINE
# =============================

print("=== String Processing Pipeline ===")
print()

def remove_extra_spaces(text):
    """Collapse multiple spaces into single spaces."""
    return " ".join(text.split())

def add_period(text):
    """Add period at end if not present."""
    return text if text.endswith(".") else text + "."

def capitalize_first(text):
    """Capitalize only the first letter."""
    if not text:
        return text
    return text[0].upper() + text[1:]

# Build the pipeline
clean_text = pipeline(
    str.strip,
    str.lower,
    remove_extra_spaces,
    capitalize_first,
    add_period,
)

messy_inputs = [
    "   HELLO    WORLD   ",
    "  python IS   awesome  ",
    "   THE QUICK   BROWN   FOX   ",
]

for text in messy_inputs:
    print(f"  '{text}'")
    print(f"   → '{clean_text(text)}'")
    print()

# =============================
# 5. DATA TRANSFORMATION PIPELINE
# =============================

print("=== Data Transformation Pipeline ===")
print()

# Pipeline for processing a list of numbers
def remove_negatives(nums):
    return [n for n in nums if n >= 0]

def double_all(nums):
    return [n * 2 for n in nums]

def sort_descending(nums):
    return sorted(nums, reverse=True)

def take_top_3(nums):
    return nums[:3]

process_numbers = pipeline(
    remove_negatives,
    double_all,
    sort_descending,
    take_top_3,
)

data = [5, -3, 8, -1, 2, 10, -7, 4]
result = process_numbers(data)

print(f"  Input:  {data}")
print(f"  Step 1 (remove neg): {remove_negatives(data)}")
print(f"  Step 2 (double):     {double_all(remove_negatives(data))}")
print(f"  Step 3 (sort desc):  {sort_descending(double_all(remove_negatives(data)))}")
print(f"  Step 4 (top 3):      {result}")
print()

# =============================
# 6. TRACED PIPELINE
# =============================

print("=== Traced Pipeline (Debug Mode) ===")
print()

def traced_pipeline(*functions):
    """Pipeline that prints each step."""
    def composed(x):
        result = x
        print(f"    Start: {result}")
        for func in functions:
            result = func(result)
            name = getattr(func, '__name__', '(lambda)')
            print(f"    After {name}: {result}")
        return result
    return composed

traced = traced_pipeline(
    abs,
    lambda x: x + 10,
    double,
    str,
)

print("  Processing -7:")
final = traced(-7)
print(f"  Final: {final}")
print()

# =============================
# 7. COMPOSING WITH map() AND filter()
# =============================

print("=== Composition with map/filter ===")
print()

# Instead of nesting, compose steps clearly
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step-by-step composition
step1 = list(filter(lambda x: x % 2 == 0, numbers))     # evens
step2 = list(map(lambda x: x ** 2, step1))               # square
step3 = list(filter(lambda x: x > 20, step2))            # > 20

print(f"  numbers: {numbers}")
print(f"  evens:   {step1}")
print(f"  squared: {step2}")
print(f"  > 20:    {step3}")
print()

# =============================
# 8. REAL-WORLD: TEXT ANALYZER
# =============================

print("=== Real-World: Text Analyzer ===")
print()

def extract_words(text):
    """Split text into words."""
    return text.lower().split()

def remove_short_words(words):
    """Remove words shorter than 3 characters."""
    return [w for w in words if len(w) >= 3]

def count_unique(words):
    """Count unique words."""
    return len(set(words))

def format_result(count):
    """Format the count as a message."""
    return f"{count} unique significant words"

analyze = pipeline(
    extract_words,
    remove_short_words,
    count_unique,
    format_result,
)

text = "the quick brown fox jumps over the lazy dog and the fox runs"
result = analyze(text)
print(f"  Text: '{text}'")
print(f"  Analysis: {result}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Build a pipeline that processes email addresses:
#    strip → lowercase → validate format → extract domain
# 2. Create a number pipeline: abs → round → format as $
# 3. Build a traced pipeline and process a complex value
# ============================================
