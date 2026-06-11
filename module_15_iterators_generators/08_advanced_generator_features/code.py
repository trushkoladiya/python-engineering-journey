# ============================================
# MODULE 15 - SUBTOPIC 8: Advanced Generator Features
# ============================================

# Generators support send(), close(), and throw()
# for two-way communication.

# =============================
# 1. send() — SENDING VALUES IN
# =============================

print("=== send() — Sending Values Into a Generator ===")
print()

def receiver():
    """A generator that receives values via send()."""
    print("    Generator started")
    while True:
        value = yield       # yield receives the sent value
        print(f"    Received: {value}")

gen = receiver()

# MUST call next() first to start the generator
print("  Starting generator with next():")
next(gen)
print()

# Now send values
print("  Sending values:")
gen.send("hello")
gen.send(42)
gen.send([1, 2, 3])
print()

# =============================
# 2. send() WITH PROCESSING
# =============================

print("=== send() with Processing ===")
print()

def accumulator():
    """Accumulates values sent to it."""
    total = 0
    while True:
        value = yield total     # yield current total, receive new value
        if value is not None:
            total += value

gen = accumulator()

# Start and get initial total
initial = next(gen)
print(f"  Initial total: {initial}")

# Send values and get running totals
print(f"  send(10) → total = {gen.send(10)}")
print(f"  send(20) → total = {gen.send(20)}")
print(f"  send(5)  → total = {gen.send(5)}")
print(f"  send(15) → total = {gen.send(15)}")
print()

# =============================
# 3. send() — RUNNING AVERAGE
# =============================

print("=== send() — Running Average ===")
print()

def running_average():
    """Calculate running average of sent values."""
    total = 0
    count = 0
    average = None
    while True:
        value = yield average
        if value is not None:
            total += value
            count += 1
            average = total / count

avg_gen = running_average()
next(avg_gen)   # start

values = [10, 20, 30, 40, 50]
for v in values:
    result = avg_gen.send(v)
    print(f"  Sent {v:2d} → average = {result:.1f}")
print()

# =============================
# 4. close() — STOPPING A GENERATOR
# =============================

print("=== close() — Stopping a Generator ===")
print()

def infinite_counter():
    """Counts forever."""
    n = 0
    try:
        while True:
            yield n
            n += 1
    except GeneratorExit:
        print("    Generator received close signal!")

gen = infinite_counter()

print(f"  next() = {next(gen)}")
print(f"  next() = {next(gen)}")
print(f"  next() = {next(gen)}")

print("  Calling close():")
gen.close()
print()

# After close, generator is done
try:
    next(gen)
except StopIteration:
    print("  Generator is now exhausted (StopIteration)")
print()

# =============================
# 5. close() WITH CLEANUP
# =============================

print("=== close() with Cleanup ===")
print()

def resource_generator():
    """Generator that cleans up on close."""
    print("    Opening resource...")
    try:
        n = 0
        while True:
            yield f"data_{n}"
            n += 1
    finally:
        # finally block runs when generator is closed
        print("    Cleaning up resource!")

gen = resource_generator()

print(f"  {next(gen)}")
print(f"  {next(gen)}")
print("  Closing generator:")
gen.close()
print()

# =============================
# 6. throw() — THROWING EXCEPTIONS
# =============================

print("=== throw() — Throwing Exceptions ===")
print()

def careful_generator():
    """Generator that handles thrown exceptions."""
    n = 0
    while True:
        try:
            yield n
            n += 1
        except ValueError as e:
            print(f"    Caught ValueError: {e}")
            n = 0   # reset on error
        except TypeError as e:
            print(f"    Caught TypeError: {e}")

gen = careful_generator()

print(f"  next() = {next(gen)}")   # 0
print(f"  next() = {next(gen)}")   # 1
print(f"  next() = {next(gen)}")   # 2

# Throw an exception into the generator
print("  Throwing ValueError:")
result = gen.throw(ValueError("Reset!"))
print(f"  After throw: next() = {result}")   # 0 (reset!)

print(f"  next() = {next(gen)}")   # 1
print()

# =============================
# 7. PRACTICAL: CONFIGURABLE GENERATOR
# =============================

print("=== Practical: Configurable Generator ===")
print()

def step_counter():
    """Counter where you can change the step size via send()."""
    value = 0
    step = 1
    while True:
        new_step = yield value
        if new_step is not None:
            step = new_step
            print(f"    Step changed to {step}")
        value += step

gen = step_counter()
next(gen)    # start

print(f"  next() = {next(gen)}")          # 1 (step=1)
print(f"  next() = {next(gen)}")          # 2
print(f"  send(5) = {gen.send(5)}")       # 7 (step changed to 5)
print(f"  next() = {next(gen)}")          # 12
print(f"  send(10) = {gen.send(10)}")     # 22 (step changed to 10)
print(f"  next() = {next(gen)}")          # 32
print()

# =============================
# 8. WHEN TO USE THESE FEATURES
# =============================

print("=== When to Use These Features ===")
print()

print("  send():  Coroutines, interactive pipelines")
print("  close(): Cleanup, stopping infinite generators")
print("  throw(): Error injection, testing")
print()
print("  Most generators only need yield + next()")
print("  These advanced features are for special cases")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a generator that accumulates sent values into a list
# 2. Create an infinite generator and use close() to stop it
# 3. Create a generator that handles thrown exceptions gracefully
# ============================================
