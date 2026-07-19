# ============================================
# MODULE 13 - SUBTOPIC 13: Callable Objects (__call__)
# ============================================

# __call__ lets objects be called like functions: obj()

# =============================
# 1. BASIC __call__
# =============================

# --- Example 1: An object you can call ---
print("=== Basic __call__ ===")
print()

class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"

hello = Greeter("Hello")
hi = Greeter("Hi there")

# Call the objects like functions!
print(f"  {hello('Trush')}")
print(f"  {hello('Rahul')}")
print(f"  {hi('Charlie')}")
print()

# =============================
# 2. STATEFUL CALLABLE
# =============================

# --- Example 2: Remembering state between calls ---
print("=== Stateful Callable ===")
print()

class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0

counter = Counter()
print(f"  Call 1: {counter()}")
print(f"  Call 2: {counter()}")
print(f"  Call 3: {counter()}")

counter.reset()
print(f"  After reset: {counter()}")
print()

# =============================
# 3. CONFIGURABLE CALLABLE
# =============================

# --- Example 3: Set up once, call many times ---
print("=== Configurable Callable ===")
print()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)
to_percent = Multiplier(100)

print(f"  double(5) = {double(5)}")
print(f"  triple(5) = {triple(5)}")
print(f"  to_percent(0.75) = {to_percent(0.75)}")
print()

# Use like regular functions!
numbers = [1, 2, 3, 4, 5]
doubled = [double(n) for n in numbers]
tripled = [triple(n) for n in numbers]

print(f"  Numbers: {numbers}")
print(f"  Doubled: {doubled}")
print(f"  Tripled: {tripled}")
print()

# =============================
# 4. CALLABLE WITH HISTORY
# =============================

# --- Example 4: Recording all calls ---
print("=== Callable with History ===")
print()

class Logger:
    def __init__(self, prefix="LOG"):
        self.prefix = prefix
        self.history = []

    def __call__(self, message):
        entry = f"[{self.prefix}] {message}"
        self.history.append(entry)
        print(f"    {entry}")

    def show_history(self):
        return self.history.copy()

log = Logger("APP")
log("Server started")
log("User logged in")
log("Data processed")

print(f"  History: {log.show_history()}")
print()

# =============================
# 5. CHECKING CALLABLE
# =============================

# --- Example 5: callable() check ---
print("=== Checking Callable ===")
print()

class CallableClass:
    def __call__(self):
        pass

class NotCallableClass:
    pass

def regular_function():
    pass

items = [
    ("CallableClass instance", CallableClass()),
    ("NotCallableClass instance", NotCallableClass()),
    ("regular_function", regular_function),
    ("int 42", 42),
    ("str 'hello'", "hello"),
    ("list [1,2,3]", [1, 2, 3]),
    ("built-in print", print),
    ("built-in len", len),
]

for name, item in items:
    print(f"  callable({name})? {callable(item)}")
print()

# =============================
# 6. PRACTICAL: VALIDATOR
# =============================

# --- Example 6: Reusable validation callable ---
print("=== Practical: Validator ===")
print()

class RangeValidator:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __call__(self, value):
        if value < self.min_val or value > self.max_val:
            raise ValueError(
                f"{value} not in range [{self.min_val}, {self.max_val}]"
            )
        return value

validate_age = RangeValidator(0, 150)
validate_score = RangeValidator(0, 100)
validate_temperature = RangeValidator(-273, 1000)

# Use like functions
tests = [
    ("Age 25", validate_age, 25),
    ("Age 200", validate_age, 200),
    ("Score 85", validate_score, 85),
    ("Score -5", validate_score, -5),
    ("Temp 20°C", validate_temperature, 20),
]

for label, validator, value in tests:
    try:
        validator(value)
        print(f"  {label}: valid ✓")
    except ValueError as e:
        print(f"  {label}: {e} ✗")
print()

# =============================
# 7. PRACTICAL: CACHING CALLABLE
# =============================

# --- Example 7: Cache expensive computations ---
print("=== Caching Callable ===")
print()

class CachedCompute:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            print(f"    Cache hit for {args}")
            return self.cache[args]
        print(f"    Computing for {args}")
        result = self.func(*args)
        self.cache[args] = result
        return result

def expensive_add(a, b):
    return a + b

cached_add = CachedCompute(expensive_add)

print(f"  Result: {cached_add(3, 4)}")    # computes
print(f"  Result: {cached_add(3, 4)}")    # cache hit!
print(f"  Result: {cached_add(5, 6)}")    # computes
print(f"  Result: {cached_add(5, 6)}")    # cache hit!

# ============================================
# TRY IT YOURSELF:
# 1. Create a Formatter callable: Formatter("${:.2f}")(42) → "$42.00"
# 2. Create a RetryCall that retries a function N times on failure
# 3. Create a Timer callable that tracks how many times it's called
# ============================================
