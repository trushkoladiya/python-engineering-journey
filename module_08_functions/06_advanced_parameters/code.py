# ============================================
# MODULE 8 - SUBTOPIC 6: Advanced Parameters
# ============================================

# =============================
# 1. *args — VARIABLE POSITIONAL ARGUMENTS
# =============================

# --- Example 1: Basic *args ---
def add_all(*args):
    print(f"  args = {args} (type: {type(args).__name__})")
    return sum(args)

print("Sum of numbers:")
print(f"  add_all(1, 2) = {add_all(1, 2)}")
print(f"  add_all(1, 2, 3, 4, 5) = {add_all(1, 2, 3, 4, 5)}")

# --- Example 2: *args with regular parameter ---
def greet_all(greeting, *names):
    for name in names:
        print(f"  {greeting}, {name}!")

print("\nGreetings:")
greet_all("Hello", "Trush", "Rahul", "Charlie")

# --- Example 3: Find max from any number of values ---
def find_max(*values):
    if len(values) == 0:
        return None
    result = values[0]
    for v in values:
        if v > result:
            result = v
    return result

print(f"\nMax: {find_max(5, 2, 8, 1)}")
print(f"Max: {find_max(100, 200)}")

# =============================
# 2. **kwargs — VARIABLE KEYWORD ARGUMENTS
# =============================

# --- Example 4: Basic **kwargs ---
def show_info(**kwargs):
    print(f"  kwargs = {kwargs} (type: {type(kwargs).__name__})")
    for key, value in kwargs.items():
        print(f"    {key}: {value}")

print("\nUser info:")
show_info(name="Trush", age=21, city="Mumbai")

# --- Example 5: **kwargs with regular parameters ---
def create_profile(name, **details):
    print(f"\n  Profile for {name}:")
    for key, value in details.items():
        print(f"    {key}: {value}")

create_profile("Trush", age=21, job="Developer", city="Mumbai")
create_profile("Rahul", age=30, hobby="Reading")

# --- Example 6: Building a config dictionary ---
def make_config(**settings):
    config = {"debug": False, "verbose": False}   # Defaults
    config.update(settings)                         # Override with provided
    return config

print("\nConfigs:")
print(f"  Default: {make_config()}")
print(f"  Custom:  {make_config(debug=True, theme='dark')}")

# =============================
# 3. COMBINING *args AND **kwargs
# =============================

# --- Example 7: Both together ---
def universal(*args, **kwargs):
    print(f"\n  Positional: {args}")
    print(f"  Keyword: {kwargs}")

universal(1, 2, 3, name="Trush", age=21)

# --- Example 8: Practical — flexible formatter ---
def log_message(*messages, **options):
    separator = options.get("sep", " ")
    prefix = options.get("prefix", "[LOG]")
    text = separator.join(str(m) for m in messages)
    print(f"  {prefix} {text}")

print("\nLog messages:")
log_message("Hello", "World")
log_message("Error", "File not found", prefix="[ERROR]")
log_message("A", "B", "C", sep=" -> ", prefix="[FLOW]")

# =============================
# 4. KEYWORD-ONLY ARGUMENTS
# =============================

# --- Example 9: Forcing keyword arguments ---
def greet(name, *, greeting="Hello", punctuation="!"):
    print(f"  {greeting}, {name}{punctuation}")

print("\nKeyword-only:")
greet("Trush")
greet("Rahul", greeting="Hi")
greet("Charlie", greeting="Hey", punctuation=".")
# greet("Dave", "Hi")   # ❌ TypeError: takes 1 positional argument

# --- Example 10: Required keyword-only argument ---
def divide(a, b, *, show_remainder=False):
    result = a / b
    print(f"  {a} / {b} = {result:.2f}")
    if show_remainder:
        print(f"  Remainder: {a % b}")

print("\nDivision:")
divide(10, 3)
divide(10, 3, show_remainder=True)

# =============================
# 5. MUTABLE DEFAULT ARGUMENT PROBLEM
# =============================

# --- Example 11: THE BUG — mutable default ---
def add_item_bad(item, items=[]):
    items.append(item)
    return items

print("\n❌ Bad (mutable default):")
print(f"  Call 1: {add_item_bad('apple')}")
print(f"  Call 2: {add_item_bad('banana')}")    # ['apple', 'banana'] — BUG!
print(f"  Call 3: {add_item_bad('cherry')}")    # Keeps growing!

# --- Example 12: THE FIX — use None ---
def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print("\n✅ Good (None default):")
print(f"  Call 1: {add_item_good('apple')}")
print(f"  Call 2: {add_item_good('banana')}")   # ['banana'] — correct!
print(f"  Call 3: {add_item_good('cherry')}")   # ['cherry'] — correct!

# =============================
# 6. ARGUMENT ORDER RULE
# =============================

# --- Example 13: Correct order of parameters ---
# The order must be:
# 1. Regular parameters
# 2. *args
# 3. Keyword-only parameters
# 4. **kwargs

def full_example(a, b, *args, option="default", **kwargs):
    print(f"\n  a={a}, b={b}")
    print(f"  args={args}")
    print(f"  option={option}")
    print(f"  kwargs={kwargs}")

full_example(1, 2, 3, 4, option="custom", extra="yes")

# ============================================
# TRY IT YOURSELF:
# 1. Create a function that accepts any number of numbers and returns their average
# 2. Create a function using **kwargs that builds a user profile
# 3. Fix a function that has a mutable default argument
# ============================================
