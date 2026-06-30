# ============================================
# MODULE 8 - SUBTOPIC 12: Nested Functions & Closures
# ============================================

# =============================
# 1. BASIC INNER FUNCTIONS
# =============================

# --- Example 1: Simple inner function ---
def outer():
    print("Outer function running")
    
    def inner():
        print("  Inner function running")
    
    inner()   # Call inner from within outer

outer()
# inner()   # ❌ NameError — inner is not accessible outside

# --- Example 2: Inner function as a helper ---
def format_data(name, scores):
    def calculate_average(nums):
        return sum(nums) / len(nums)
    
    avg = calculate_average(scores)
    print(f"\n{name}: scores={scores}, average={avg:.1f}")

format_data("Trush", [90, 85, 92])
format_data("Rahul", [78, 82, 75])

# --- Example 3: Multiple inner functions ---
def process_text(text):
    def clean(t):
        return t.strip().lower()
    
    def word_count(t):
        return len(t.split())
    
    cleaned = clean(text)
    count = word_count(cleaned)
    print(f"\n  Original: '{text}'")
    print(f"  Cleaned:  '{cleaned}'")
    print(f"  Words:    {count}")

process_text("  Hello World Python  ")

# =============================
# 2. CLOSURES — REMEMBERING OUTER VARIABLES
# =============================

# --- Example 4: Basic closure ---
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"   # 'greeting' comes from outer
    return greeter

hello = make_greeter("Hello")
hi = make_greeter("Hi")
hey = make_greeter("Hey there")

print(f"\n{hello('Trush')}")
print(f"{hi('Rahul')}")
print(f"{hey('Charlie')}")

# --- Example 5: Closure remembers the value ---
def make_multiplier(factor):
    def multiplier(n):
        return n * factor   # 'factor' is remembered
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
times_ten = make_multiplier(10)

print(f"\ndouble(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")
print(f"times_ten(5) = {times_ten(5)}")

# --- Example 6: Each closure has its own copy ---
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_5 = make_adder(5)
add_10 = make_adder(10)
add_100 = make_adder(100)

print(f"\nadd_5(3) = {add_5(3)}")       # 8
print(f"add_10(3) = {add_10(3)}")       # 13
print(f"add_100(3) = {add_100(3)}")     # 103

# =============================
# 3. CLOSURES WITH STATE
# =============================

# --- Example 7: Counter using closure ---
def make_counter():
    count = [0]   # Using a list so inner function can modify it
    def counter():
        count[0] = count[0] + 1
        return count[0]
    return counter

my_counter = make_counter()
print(f"\nCounter: {my_counter()}")   # 1
print(f"Counter: {my_counter()}")     # 2
print(f"Counter: {my_counter()}")     # 3

# Each counter is independent
another_counter = make_counter()
print(f"\nNew counter: {another_counter()}")   # 1 (fresh start)

# --- Example 8: Running total ---
def make_accumulator():
    total = [0]
    def add(amount):
        total[0] = total[0] + amount
        return total[0]
    return add

wallet = make_accumulator()
print(f"\nWallet balance: {wallet(100)}")   # 100
print(f"Wallet balance: {wallet(50)}")      # 150
print(f"Wallet balance: {wallet(25)}")      # 175

# --- Example 9: Logger ---
def make_logger(prefix):
    messages = []
    def log(message):
        messages.append(f"[{prefix}] {message}")
        return messages
    return log

app_log = make_logger("APP")
app_log("Started")
app_log("Processing data")
all_logs = app_log("Done")

print("\nLogs:")
for msg in all_logs:
    print(f"  {msg}")

# =============================
# 4. nonlocal KEYWORD
# =============================

# --- Example 10: Using nonlocal to modify outer variable ---
def make_counter_v2():
    count = 0   # Regular variable, not a list
    def counter():
        nonlocal count   # Tell Python to use the outer variable
        count = count + 1
        return count
    return counter

counter = make_counter_v2()
print(f"\nCounter v2: {counter()}")   # 1
print(f"Counter v2: {counter()}")     # 2
print(f"Counter v2: {counter()}")     # 3

# =============================
# 5. PRACTICAL EXAMPLES
# =============================

# --- Example 11: Validator factory ---
def make_range_validator(min_val, max_val):
    def validate(value):
        return min_val <= value <= max_val
    return validate

is_valid_age = make_range_validator(0, 120)
is_valid_score = make_range_validator(0, 100)
is_valid_temperature = make_range_validator(-50, 50)

print(f"\nValid age 25: {is_valid_age(25)}")
print(f"Valid age 200: {is_valid_age(200)}")
print(f"Valid score 85: {is_valid_score(85)}")

# --- Example 12: Formatter factory ---
def make_formatter(template):
    def formatter(**kwargs):
        return template.format(**kwargs)
    return formatter

email_format = make_formatter("Dear {name},\n{body}\nBest, {sender}")
result = email_format(name="Trush", body="How are you?", sender="Rahul")
print(f"\n{result}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a closure that remembers a greeting and personalizes it
# 2. Build a counter that can also be reset
# 3. Create a validator factory for different data ranges
# ============================================
