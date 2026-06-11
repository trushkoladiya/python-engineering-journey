# ============================================
# MODULE 15 - SUBTOPIC 4: Creating Custom Iterators
# ============================================

# Create your own iterators by implementing
# __iter__() and __next__() in a class.

# =============================
# 1. BASIC CUSTOM ITERATOR
# =============================

print("=== Basic Custom Iterator: CountUp ===")
print()

class CountUp:
    """Iterator that counts from start to end."""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self   # iterator returns itself

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Use in a for loop
print("  CountUp(1, 5):")
for num in CountUp(1, 5):
    print(f"    {num}")
print()

# Use with next()
print("  Using next() manually:")
counter = CountUp(10, 13)
print(f"    next() = {next(counter)}")
print(f"    next() = {next(counter)}")
print(f"    next() = {next(counter)}")
print(f"    next() = {next(counter)}")
print()

# =============================
# 2. COUNTDOWN ITERATOR
# =============================

print("=== Countdown Iterator ===")
print()

class Countdown:
    """Iterator that counts down to zero."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("  Countdown(5):")
for num in Countdown(5):
    print(f"    {num}")
print()

# =============================
# 3. ITERATOR OVER CUSTOM DATA
# =============================

print("=== Custom Data Iterator ===")
print()

class EvenNumbers:
    """Iterator that yields even numbers up to a limit."""

    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

print("  EvenNumbers(10):")
for n in EvenNumbers(10):
    print(f"    {n}", end=" ")
print()
print()

# =============================
# 4. POWERS ITERATOR
# =============================

print("=== Powers Iterator ===")
print()

class PowersOfTwo:
    """Iterator that yields powers of 2."""

    def __init__(self, max_power):
        self.max_power = max_power
        self.current_power = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_power > self.max_power:
            raise StopIteration
        value = 2 ** self.current_power
        self.current_power += 1
        return value

print("  PowersOfTwo(8):")
for power in PowersOfTwo(8):
    print(f"    {power}")
print()

# =============================
# 5. WORKS WITH BUILT-IN FUNCTIONS
# =============================

print("=== Custom Iterators + Built-in Functions ===")
print()

# Convert to list
evens = list(EvenNumbers(20))
print(f"  list(EvenNumbers(20)) = {evens}")

# Use with sum
total = sum(CountUp(1, 10))
print(f"  sum(CountUp(1, 10)) = {total}")

# Use with max/min
powers = list(PowersOfTwo(5))
print(f"  PowersOfTwo(5) as list = {powers}")
print(f"  max = {max(PowersOfTwo(5))}")
print()

# =============================
# 6. STRING REPEATER ITERATOR
# =============================

print("=== String Repeater ===")
print()

class Repeater:
    """Repeats a value a fixed number of times."""

    def __init__(self, value, times):
        self.value = value
        self.times = times
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.times:
            raise StopIteration
        self.count += 1
        return self.value

print("  Repeater('hello', 3):")
for item in Repeater("hello", 3):
    print(f"    {item}")
print()

# Works with list()
print(f"  list(Repeater('x', 5)) = {list(Repeater('x', 5))}")
print()

# =============================
# 7. FIBONACCI ITERATOR
# =============================

print("=== Fibonacci Iterator ===")
print()

class Fibonacci:
    """Iterator that yields Fibonacci numbers up to a count."""

    def __init__(self, count):
        self.count = count
        self.generated = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated >= self.count:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.generated += 1
        return value

print("  First 10 Fibonacci numbers:")
print(f"  {list(Fibonacci(10))}")
print()

# =============================
# 8. SEPARATING ITERABLE FROM ITERATOR
# =============================

print("=== Separating Iterable from Iterator ===")
print()

# Better pattern: the iterable creates NEW iterators each time

class NumberRange:
    """An iterable that creates fresh iterators."""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # Return a NEW iterator each time
        return NumberRangeIterator(self.start, self.end)

class NumberRangeIterator:
    """The actual iterator with state."""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Can iterate MULTIPLE times (unlike simple iterators)
nums = NumberRange(1, 4)

print("  First loop:")
for n in nums:
    print(f"    {n}", end=" ")
print()

print("  Second loop (works again!):")
for n in nums:
    print(f"    {n}", end=" ")
print()
print()

print("  → Separating iterable from iterator allows reuse!")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Create an iterator that yields odd numbers up to N
# 2. Create an iterator that yields squares: 1, 4, 9, 16...
# 3. Create an iterator that cycles through a list of colors
# ============================================
