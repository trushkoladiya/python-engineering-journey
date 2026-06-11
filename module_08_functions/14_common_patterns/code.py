# ============================================
# MODULE 8 - SUBTOPIC 14: Common Patterns
# ============================================

# =============================
# 1. UTILITY / HELPER FUNCTIONS
# =============================

# --- Example 1: Clamp value within bounds ---
def clamp(value, min_val, max_val):
    """Keep value within min and max bounds."""
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value

print("Clamp examples:")
print(f"  clamp(15, 0, 10) = {clamp(15, 0, 10)}")    # 10
print(f"  clamp(-5, 0, 10) = {clamp(-5, 0, 10)}")     # 0
print(f"  clamp(7, 0, 10)  = {clamp(7, 0, 10)}")      # 7

# --- Example 2: Safe division ---
def safe_divide(a, b, default=0):
    """Divide a by b, return default if b is zero."""
    if b == 0:
        return default
    return a / b

print(f"\nsafe_divide(10, 3) = {safe_divide(10, 3):.2f}")
print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")

# --- Example 3: Pluralize ---
def pluralize(word, count):
    """Add 's' to word if count is not 1."""
    if count == 1:
        return f"{count} {word}"
    return f"{count} {word}s"

print(f"\n{pluralize('apple', 1)}")
print(f"{pluralize('apple', 5)}")
print(f"{pluralize('box', 0)}")

# =============================
# 2. VALIDATION FUNCTIONS
# =============================

# --- Example 4: Input validation ---
def is_valid_email(email):
    """Basic email validation."""
    return (
        isinstance(email, str)
        and "@" in email
        and "." in email.split("@")[-1]
        and len(email) >= 5
    )

print("\nEmail validation:")
print(f"  'test@example.com': {is_valid_email('test@example.com')}")
print(f"  'invalid': {is_valid_email('invalid')}")
print(f"  'a@b.c': {is_valid_email('a@b.c')}")

# --- Example 5: Score validation ---
def validate_score(score, min_val=0, max_val=100):
    """Validate that score is a number within range."""
    if not isinstance(score, (int, float)):
        return False, "Score must be a number"
    if score < min_val or score > max_val:
        return False, f"Score must be between {min_val} and {max_val}"
    return True, "Valid"

test_scores = [85, -5, 150, "abc", 72]
print("\nScore validation:")
for score in test_scores:
    valid, message = validate_score(score)
    status = "✓" if valid else "✗"
    print(f"  {status} {score}: {message}")

# --- Example 6: Password strength checker ---
def check_password(password):
    """Check password meets basic requirements."""
    issues = []
    if len(password) < 8:
        issues.append("too short (min 8)")
    if not any(c.isupper() for c in password):
        issues.append("needs uppercase")
    if not any(c.isdigit() for c in password):
        issues.append("needs a digit")
    
    if len(issues) == 0:
        return True, "Strong password"
    return False, ", ".join(issues)

passwords = ["abc", "HelloWorld", "Hello123", "hi1A"]
print("\nPassword check:")
for pw in passwords:
    valid, msg = check_password(pw)
    status = "✓" if valid else "✗"
    print(f"  {status} '{pw}': {msg}")

# =============================
# 3. FUNCTION PIPELINES
# =============================

# --- Example 7: Text processing pipeline ---
def strip_whitespace(text):
    """Remove leading and trailing whitespace."""
    return text.strip()

def to_lowercase(text):
    """Convert text to lowercase."""
    return text.lower()

def remove_extra_spaces(text):
    """Replace multiple spaces with single space."""
    return " ".join(text.split())

def capitalize_words(text):
    """Capitalize first letter of each word."""
    return text.title()

# Apply pipeline
raw = "  hello   WORLD   python   PROGRAMMING  "
print(f"\nPipeline:")
print(f"  Raw:     '{raw}'")

cleaned = strip_whitespace(raw)
cleaned = to_lowercase(cleaned)
cleaned = remove_extra_spaces(cleaned)
cleaned = capitalize_words(cleaned)
print(f"  Result:  '{cleaned}'")

# --- Example 8: Generic pipeline function ---
def pipeline(data, *functions):
    """Apply a series of functions to data in order."""
    result = data
    for func in functions:
        result = func(result)
    return result

result = pipeline(
    "  hello   WORLD  ",
    strip_whitespace,
    to_lowercase,
    remove_extra_spaces,
)
print(f"  Generic: '{result}'")

# =============================
# 4. CALLBACK PATTERN
# =============================

# --- Example 9: Processing with callbacks ---
def process_items(items, action):
    """Apply an action function to each item."""
    for item in items:
        action(item)

def print_item(item):
    print(f"  Processing: {item}")

def shout_item(item):
    print(f"  {str(item).upper()}!")

print("\nCallback — normal:")
process_items(["apple", "banana", "cherry"], print_item)

print("\nCallback — shout:")
process_items(["apple", "banana", "cherry"], shout_item)

# --- Example 10: Transform with callback ---
def transform_list(items, transformer):
    """Return a new list with transformer applied to each item."""
    result = []
    for item in items:
        result.append(transformer(item))
    return result

numbers = [1, 2, 3, 4, 5]

def double(n):
    return n * 2

def square(n):
    return n * n

print(f"\nOriginal: {numbers}")
print(f"Doubled:  {transform_list(numbers, double)}")
print(f"Squared:  {transform_list(numbers, square)}")

# =============================
# 5. LOOKUP TABLE PATTERN
# =============================

# --- Example 11: Function dispatch ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return safe_divide(a, b)

def calculate(a, operator, b):
    """Calculate using function lookup."""
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    func = operations.get(operator)
    if func is None:
        return f"Unknown operator: {operator}"
    return func(a, b)

print("\nCalculator:")
expressions = [("10", "+", "3"), ("10", "-", "3"),
               ("10", "*", "3"), ("10", "/", "3")]
for a, op, b in expressions:
    result = calculate(int(a), op, int(b))
    print(f"  {a} {op} {b} = {result}")

# =============================
# 6. BUILDER PATTERN
# =============================

# --- Example 12: Building complex output ---
def build_report(title, data, show_total=True, show_average=True):
    """Build a formatted report from data."""
    lines = []
    lines.append(f"\n{'=' * 30}")
    lines.append(f"  {title}")
    lines.append(f"{'=' * 30}")
    
    for name, value in data:
        lines.append(f"  {name:15s} {value:>8.2f}")
    
    values = [v for _, v in data]
    lines.append(f"{'-' * 30}")
    
    if show_total:
        lines.append(f"  {'Total':15s} {sum(values):>8.2f}")
    if show_average:
        lines.append(f"  {'Average':15s} {sum(values)/len(values):>8.2f}")
    
    return "\n".join(lines)

sales = [("Monday", 1200), ("Tuesday", 980), ("Wednesday", 1500),
         ("Thursday", 1100), ("Friday", 1800)]

report = build_report("Weekly Sales", sales)
print(report)

# ============================================
# TRY IT YOURSELF:
# 1. Create a utility function and use it in different contexts
# 2. Build a text processing pipeline with 3+ functions
# 3. Create a calculator using the function lookup pattern
# ============================================
