# ============================================
# MODULE 16 - SUBTOPIC 14: Decorators (Advanced Usage)
# ============================================

# Decorators wrap functions to add behavior.
# Here we explore advanced patterns in a functional context.

from functools import wraps
import time

# =============================
# 1. RECAP: BASIC DECORATOR
# =============================

print("=== Basic Decorator Recap ===")
print()

def uppercase_result(func):
    """Decorator that uppercases the string result."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result
    return wrapper

@uppercase_result
def greet(name):
    """Greet someone."""
    return f"hello, {name}"

print(f"  greet('Trush') = '{greet('Trush')}'")
print(f"  Function name: {greet.__name__}")
print(f"  Docstring: {greet.__doc__}")
print()

# =============================
# 2. STACKING MULTIPLE DECORATORS
# =============================

print("=== Stacking Decorators ===")
print()

def add_exclaim(func):
    """Add exclamation mark to result."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"
    return wrapper

def add_greeting(func):
    """Add 'Hey! ' prefix to result."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return "Hey! " + func(*args, **kwargs)
    return wrapper

def make_title(func):
    """Title-case the result."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).title()
    return wrapper

# Decorators apply BOTTOM to TOP
@add_greeting      # 3rd: add "Hey! " prefix
@add_exclaim       # 2nd: add "!"
@make_title        # 1st: title case
def get_name(name):
    return name

print(f"  get_name('trush koladiya') = '{get_name('trush koladiya')}'")
print("  Order: make_title → add_exclaim → add_greeting")
print()

# =============================
# 3. PARAMETERIZED DECORATORS
# =============================

print("=== Parameterized Decorators ===")
print()

def repeat(n):
    """Decorator that calls function n times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def roll_dice():
    """Simulate a dice roll."""
    import random
    return random.randint(1, 6)

print(f"  roll_dice() (3 rolls): {roll_dice()}")
print()

# Another parameterized decorator
def prefix_result(prefix):
    """Decorator that adds a prefix to the result."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}{result}"
        return wrapper
    return decorator

@prefix_result(">>> ")
def calculate(a, b):
    return a + b

print(f"  calculate(3, 4) = '{calculate(3, 4)}'")
print()

# =============================
# 4. TIMING DECORATOR
# =============================

print("=== Timing Decorator ===")
print()

def timer(func):
    """Measure execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"    {func.__name__} took {elapsed:.6f} seconds")
        return result
    return wrapper

@timer
def slow_sum(n):
    """Sum numbers from 1 to n."""
    return sum(range(1, n + 1))

@timer
def fast_sum(n):
    """Sum using formula."""
    return n * (n + 1) // 2

print("  Timing comparison:")
result1 = slow_sum(1_000_000)
result2 = fast_sum(1_000_000)
print(f"  Both equal? {result1 == result2}")
print()

# =============================
# 5. RETRY DECORATOR
# =============================

print("=== Retry Decorator ===")
print()

def retry(max_attempts=3, exceptions=(Exception,)):
    """Retry a function on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"    Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator

attempt_count = 0

@retry(max_attempts=3, exceptions=(ValueError,))
def flaky_operation():
    """Fails first 2 times, succeeds on 3rd."""
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ValueError("Not ready")
    return "Success!"

print("  Running flaky_operation:")
result = flaky_operation()
print(f"  Result: {result}")
print()

# =============================
# 6. VALIDATION DECORATOR
# =============================

print("=== Validation Decorator ===")
print()

def validate_types(*types):
    """Decorator to validate argument types."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Expected {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(str, int)
def create_user(name, age):
    return {"name": name, "age": age}

# Valid call
user = create_user("Trush", 21)
print(f"  create_user('Trush', 21) = {user}")

# Invalid call
try:
    create_user("Trush", "twenty-one")
except TypeError as e:
    print(f"  create_user('Trush', 'twenty-one') → Error: {e}")
print()

# =============================
# 7. CACHING DECORATOR
# =============================

print("=== Caching Decorator ===")
print()

def cache(func):
    """Simple caching decorator."""
    memo = {}

    @wraps(func)
    def wrapper(*args):
        if args in memo:
            print(f"    Cache hit for {args}")
            return memo[args]
        print(f"    Computing for {args}")
        result = func(*args)
        memo[args] = result
        return result

    wrapper.cache_info = lambda: dict(memo)
    return wrapper

@cache
def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"  fibonacci(6):")
result = fibonacci(6)
print(f"  Result: {result}")
print()

# =============================
# 8. DECORATOR THAT RETURNS METADATA
# =============================

print("=== Decorator with Metadata ===")
print()

def track_calls(func):
    """Track how many times a function is called."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper

@track_calls
def process(x):
    return x * 2

for i in range(5):
    process(i)

print(f"  process was called {process.call_count} times")
print()

# =============================
# 9. COMBINING DECORATORS
# =============================

print("=== Combining Decorators in Practice ===")
print()

@timer
@track_calls
def compute_squares(n):
    """Compute squares of numbers 1 to n."""
    return [i ** 2 for i in range(1, n + 1)]

result = compute_squares(100_000)
print(f"  First 5 squares: {result[:5]}")
print(f"  Call count: {compute_squares.call_count}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a decorator that logs function arguments
#    and return values
# 2. Write a parameterized decorator that limits
#    how many times a function can be called
# 3. Create a decorator that converts results to JSON
# ============================================
