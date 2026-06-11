# ============================================
# MODULE 13 - SUBTOPIC 15: Advanced Decorators
# ============================================

# Basic decorators from Module 8. Now: parameterized decorators,
# functools.wraps, stacking, and class-based decorators.

from functools import wraps

# =============================
# 1. THE METADATA PROBLEM
# =============================

# --- Example 1: Without @wraps, metadata is lost ---
print("=== Metadata Problem ===")
print()

def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def greet_bad(name):
    """Greet someone by name."""
    return f"Hello, {name}!"

print(f"  Name: '{greet_bad.__name__}'")     # 'wrapper' — wrong!
print(f"  Doc:  '{greet_bad.__doc__}'")       # None — lost!
print()

# =============================
# 2. functools.wraps — FIX METADATA
# =============================

# --- Example 2: @wraps preserves the original info ---
print("=== functools.wraps Fix ===")
print()

def good_decorator(func):
    @wraps(func)    # copies name, docstring, etc. from func to wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def greet_good(name):
    """Greet someone by name."""
    return f"Hello, {name}!"

print(f"  Name: '{greet_good.__name__}'")    # 'greet_good' — correct!
print(f"  Doc:  '{greet_good.__doc__}'")     # preserved!
print()

# =============================
# 3. PARAMETERIZED DECORATORS
# =============================

# --- Example 3: Decorator that takes arguments ---
print("=== Parameterized Decorator ===")
print()

def repeat(n):
    """Decorator that calls the function n times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    """Say hello."""
    print(f"    Hello, {name}!")

say_hello("Trush")
print()

# --- Example 4: Retry decorator ---
print("=== Retry Decorator ===")
print()

def retry(max_attempts, on_fail="raise"):
    """Retry a function up to max_attempts times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"    Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        if on_fail == "raise":
                            raise
                        return None
        return wrapper
    return decorator

call_count = 0

@retry(max_attempts=3, on_fail="silent")
def unstable_function():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Network error")
    return "Success!"

result = unstable_function()
print(f"  Result: {result}")
print()

# =============================
# 4. STACKING DECORATORS
# =============================

# --- Example 5: Multiple decorators applied bottom-up ---
print("=== Stacking Decorators ===")
print()

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"_{func(*args, **kwargs)}_"
    return wrapper

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@bold
@italic
@uppercase
def greet(name):
    """Greet someone."""
    return f"hello, {name}"

# Applied bottom-up: uppercase → italic → bold
print(f"  {greet('Trush')}")
print("  Order: uppercase → italic → bold")
print()

# =============================
# 5. CLASS-BASED DECORATORS
# =============================

# --- Example 6: Using a class as a decorator ---
print("=== Class-Based Decorator ===")
print()

class CountCalls:
    """Counts how many times a function is called."""
    def __init__(self, func):
        self.func = func
        self.count = 0
        wraps(func)(self)    # preserve metadata

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"    Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def process(data):
    """Process some data."""
    return data.upper()

process("hello")
process("world")
process("python")
print(f"  Total calls: {process.count}")
print()

# =============================
# 6. CLASS-BASED WITH PARAMETERS
# =============================

# --- Example 7: Class decorator with config ---
print("=== Class Decorator with Parameters ===")
print()

class ValidateArgs:
    """Validates that all arguments are of the specified type."""
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args):
            for i, arg in enumerate(args):
                if not isinstance(arg, self.expected_type):
                    raise TypeError(
                        f"Arg {i}: expected {self.expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )
            return func(*args)
        return wrapper

@ValidateArgs(int)
def add_numbers(a, b):
    """Add two integers."""
    return a + b

print(f"  add_numbers(3, 4) = {add_numbers(3, 4)}")

try:
    add_numbers(3, "four")
except TypeError as e:
    print(f"  add_numbers(3, 'four') → {e}")
print()

# =============================
# 7. TIMING DECORATOR
# =============================

# --- Example 8: Practical timing decorator ---
print("=== Timing Decorator ===")
print()

import time

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"    {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timed
def slow_sum(n):
    """Sum numbers from 0 to n."""
    return sum(range(n))

@timed
def fast_multiply(a, b):
    """Multiply two numbers."""
    return a * b

slow_sum(1000000)
fast_multiply(42, 58)
print()

# =============================
# 8. PRACTICAL: MEMOIZATION DECORATOR
# =============================

# --- Example 9: Cache results ---
print("=== Memoization Decorator ===")
print()

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"    Cache hit: {func.__name__}{args}")
            return cache[args]
        print(f"    Computing: {func.__name__}{args}")
        result = func(*args)
        cache[args] = result
        return result

    wrapper.cache = cache
    return wrapper

@memoize
def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"  fibonacci(10) = {fibonacci(10)}")
print(f"  Cache size: {len(fibonacci.cache)} entries")

# ============================================
# TRY IT YOURSELF:
# 1. Create a @log_calls decorator that logs function name and args
# 2. Create a @require_positive decorator for numeric arguments
# 3. Create a class-based @Throttle(max_calls=5) decorator
# ============================================
