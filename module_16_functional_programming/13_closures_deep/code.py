# ============================================
# MODULE 16 - SUBTOPIC 13: Closures (Deep Use)
# ============================================

# A closure is a function that "remembers" variables
# from its enclosing scope, even after that scope is gone.

# =============================
# 1. BASIC CLOSURE
# =============================

print("=== Basic Closure ===")
print()

def make_greeter(greeting):
    """Return a function that greets with a specific greeting."""
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello = make_greeter("Hello")
hola = make_greeter("Hola")
namaste = make_greeter("Namaste")

print(f"  {hello('Trush')}")
print(f"  {hola('Rahul')}")
print(f"  {namaste('Eve')}")
print()

# =============================
# 2. CLOSURE WITH STATE
# =============================

print("=== Closure with State (nonlocal) ===")
print()

def make_counter(start=0):
    """Return a counter function with persistent state."""
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c1 = make_counter()
c2 = make_counter(100)

print(f"  c1(): {c1()}")   # 1
print(f"  c1(): {c1()}")   # 2
print(f"  c1(): {c1()}")   # 3
print(f"  c2(): {c2()}")   # 101
print(f"  c2(): {c2()}")   # 102
print("  (c1 and c2 have independent state!)")
print()

# =============================
# 3. ACCUMULATOR
# =============================

print("=== Accumulator Closure ===")
print()

def make_accumulator(initial=0):
    """Return functions to add, get total, and reset."""
    total = initial

    def add(amount):
        nonlocal total
        total += amount
        return total

    def get_total():
        return total

    def reset():
        nonlocal total
        total = initial
        return total

    return add, get_total, reset

add, get_total, reset = make_accumulator()

add(10)
add(20)
add(30)
print(f"  After adding 10, 20, 30:")
print(f"  Total: {get_total()}")

add(5)
print(f"  After adding 5: {get_total()}")

reset()
print(f"  After reset: {get_total()}")
print()

# =============================
# 4. LOGGER CLOSURE
# =============================

print("=== Logger Closure ===")
print()

def make_logger(prefix):
    """Return a logger that prepends a prefix."""
    log_history = []

    def log(message):
        entry = f"[{prefix}] {message}"
        log_history.append(entry)
        print(f"  {entry}")

    def get_history():
        return list(log_history)   # return a copy

    return log, get_history

debug, debug_history = make_logger("DEBUG")
error, error_history = make_logger("ERROR")

debug("Loading configuration")
debug("Connecting to database")
error("Connection timeout!")
debug("Retrying...")

print()
print(f"  Debug history: {debug_history()}")
print(f"  Error history: {error_history()}")
print()

# =============================
# 5. INSPECTING CLOSURES
# =============================

print("=== Inspecting Closures ===")
print()

def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

times5 = make_multiplier(5)

# Every closure has a __closure__ attribute
print(f"  times5.__closure__: {times5.__closure__}")
print(f"  Captured value: {times5.__closure__[0].cell_contents}")
print(f"  Function name: {times5.__name__}")
print()

# =============================
# 6. CLOSURE FOR MEMOIZATION (CACHING)
# =============================

print("=== Memoization with Closures ===")
print()

def make_memoized(func):
    """Return a memoized version of func."""
    cache = {}

    def memoized(*args):
        if args not in cache:
            print(f"    Computing {func.__name__}{args}...")
            cache[args] = func(*args)
        else:
            print(f"    Cache hit for {func.__name__}{args}")
        return cache[args]

    def get_cache():
        return dict(cache)

    return memoized, get_cache

def expensive_square(x):
    return x ** 2

cached_square, get_cache = make_memoized(expensive_square)

print(f"  {cached_square(4)}")   # computes
print(f"  {cached_square(4)}")   # cache hit!
print(f"  {cached_square(5)}")   # computes
print(f"  {cached_square(4)}")   # cache hit!
print(f"  Cache: {get_cache()}")
print()

# =============================
# 7. CLOSURE FOR RATE LIMITING
# =============================

print("=== Rate Limiter Closure ===")
print()

import time

def make_rate_limiter(max_calls, period_seconds=1):
    """Return a function that limits calls within a time period."""
    call_times = []

    def is_allowed():
        nonlocal call_times
        now = time.time()
        # Remove old calls outside the period
        call_times = [t for t in call_times if now - t < period_seconds]
        if len(call_times) < max_calls:
            call_times.append(now)
            return True
        return False

    return is_allowed

# Allow 3 calls per second
limiter = make_rate_limiter(3, period_seconds=1)

for i in range(5):
    allowed = limiter()
    print(f"  Call {i + 1}: {'ALLOWED' if allowed else 'BLOCKED'}")
print()

# =============================
# 8. CLOSURE GOTCHA: LOOP VARIABLE CAPTURE
# =============================

print("=== Closure Gotcha: Loop Variable ===")
print()

# WRONG: all closures capture the SAME variable
funcs_wrong = []
for i in range(5):
    funcs_wrong.append(lambda: i)

# All return 4 (the final value of i)!
print("  Wrong (all same):", [f() for f in funcs_wrong])

# RIGHT: capture the VALUE using default argument
funcs_right = []
for i in range(5):
    funcs_right.append(lambda x=i: x)   # x=i captures current value

print("  Right (different):", [f() for f in funcs_right])
print()

# =============================
# 9. CLOSURE vs CLASS
# =============================

print("=== Closure vs Class ===")
print()

# Closure approach
def make_counter_closure(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# Class approach (same functionality)
class Counter:
    def __init__(self, start=0):
        self.count = start
    def increment(self):
        self.count += 1
        return self.count

# Both work the same way
closure_counter = make_counter_closure()
class_counter = Counter()

print("  Closure:", [closure_counter() for _ in range(5)])
print("  Class:  ", [class_counter.increment() for _ in range(5)])
print("  (Closures are simpler for single-function state)")
print()

# =============================
# 10. PRACTICAL: EVENT HANDLER
# =============================

print("=== Practical: Event System ===")
print()

def make_event_handler():
    """Simple event system using closures."""
    handlers = {}

    def on(event_name, handler):
        """Register a handler for an event."""
        if event_name not in handlers:
            handlers[event_name] = []
        handlers[event_name].append(handler)

    def emit(event_name, *args):
        """Trigger all handlers for an event."""
        if event_name in handlers:
            for handler in handlers[event_name]:
                handler(*args)

    return on, emit

on, emit = make_event_handler()

# Register handlers
on("greet", lambda name: print(f"    Hello, {name}!"))
on("greet", lambda name: print(f"    Welcome, {name}!"))
on("farewell", lambda name: print(f"    Goodbye, {name}!"))

# Trigger events
print("  Emitting 'greet':")
emit("greet", "Trush")
print("  Emitting 'farewell':")
emit("farewell", "Rahul")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a closure that tracks the running average
#    of numbers added to it
# 2. Create a "make_password_checker" closure that
#    locks after 3 failed attempts
# 3. Build a simple undo system using closures
# ============================================
