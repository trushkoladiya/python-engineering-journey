# ============================================
# MODULE 15 - SUBTOPIC 5: Generators Basics
# ============================================

# Generators are a SIMPLE way to create iterators.
# Use 'yield' instead of 'return'.

# =============================
# 1. YOUR FIRST GENERATOR
# =============================

print("=== Your First Generator ===")
print()

def simple_generator():
    """A generator that yields three values."""
    yield 1
    yield 2
    yield 3

# Using it in a for loop
print("  for loop:")
for value in simple_generator():
    print(f"    {value}")
print()

# Using next() manually
gen = simple_generator()
print(f"  next(gen) = {next(gen)}")
print(f"  next(gen) = {next(gen)}")
print(f"  next(gen) = {next(gen)}")
print()

# =============================
# 2. GENERATOR vs NORMAL FUNCTION
# =============================

print("=== Generator vs Normal Function ===")
print()

# Normal function — returns ALL at once
def get_numbers_list():
    return [1, 2, 3, 4, 5]

# Generator function — yields ONE at a time
def get_numbers_gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# Calling a normal function returns the result
result = get_numbers_list()
print(f"  Normal function returns: {result}")
print(f"  Type: {type(result)}")
print()

# Calling a generator function returns a generator OBJECT
gen = get_numbers_gen()
print(f"  Generator function returns: {gen}")
print(f"  Type: {type(gen)}")
print(f"  Values: {list(gen)}")
print()

# =============================
# 3. yield WITH LOOPS
# =============================

print("=== yield with Loops ===")
print()

def count_up(n):
    """Count from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

print("  count_up(5):")
for num in count_up(5):
    print(f"    {num}", end=" ")
print()
print()

# =============================
# 4. GENERATORS ARE ITERATORS
# =============================

print("=== Generators ARE Iterators ===")
print()

def greetings():
    yield "Hello"
    yield "Bonjour"
    yield "Hola"

gen = greetings()

# Has __iter__ and __next__
print(f"  Has __iter__? {hasattr(gen, '__iter__')}")
print(f"  Has __next__? {hasattr(gen, '__next__')}")
print(f"  iter(gen) is gen? {iter(gen) is gen}")
print()

# Works with next()
print(f"  next(gen) = '{next(gen)}'")
print(f"  next(gen) = '{next(gen)}'")
print(f"  next(gen) = '{next(gen)}'")
print()

# =============================
# 5. GENERATOR WITH PROCESSING
# =============================

print("=== Generator with Processing ===")
print()

def squares(n):
    """Yield squares of numbers 1 to n."""
    for i in range(1, n + 1):
        yield i ** 2

print(f"  squares(6): {list(squares(6))}")
print()

def even_numbers(limit):
    """Yield even numbers up to limit."""
    num = 0
    while num <= limit:
        yield num
        num += 2

print(f"  even_numbers(12): {list(even_numbers(12))}")
print()

# =============================
# 6. FIBONACCI GENERATOR
# =============================

print("=== Fibonacci Generator ===")
print()

# Compare with the iterator class from subtopic 4
# — MUCH simpler!

def fibonacci(count):
    """Yield first 'count' Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

print(f"  First 10 Fibonacci: {list(fibonacci(10))}")
print()

# The class version needed ~20 lines
# The generator version needs ~5 lines!

# =============================
# 7. LAZY EVALUATION
# =============================

print("=== Lazy Evaluation ===")
print()

def count_forever():
    """An infinite counter — only possible with generators!"""
    n = 0
    while True:
        yield n
        n += 1

# This would be IMPOSSIBLE with a list (infinite memory!)
# But generators produce values on demand

counter = count_forever()
print(f"  Infinite counter (first 8):")
for _ in range(8):
    print(f"    {next(counter)}", end=" ")
print()
print()

# =============================
# 8. GENERATOR WITH CONDITIONAL yield
# =============================

print("=== Conditional Yielding ===")
print()

def only_positive(numbers):
    """Yield only positive numbers."""
    for n in numbers:
        if n > 0:
            yield n

data = [3, -1, 4, -5, 9, -2, 6]
print(f"  Input: {data}")
print(f"  only_positive: {list(only_positive(data))}")
print()

def words_longer_than(text, min_length):
    """Yield words longer than min_length."""
    for word in text.split():
        if len(word) > min_length:
            yield word

sentence = "The quick brown fox jumps over the lazy dog"
long_words = list(words_longer_than(sentence, 3))
print(f"  Words longer than 3 chars: {long_words}")
print()

# =============================
# 9. WORKS WITH ALL BUILT-INS
# =============================

print("=== Generators Work with Built-ins ===")
print()

print(f"  sum(count_up(100)) = {sum(count_up(100))}")
print(f"  max(squares(5)) = {max(squares(5))}")
print(f"  min(fibonacci(8)) = {min(fibonacci(8))}")
print(f"  sorted(fibonacci(8)) = {sorted(fibonacci(8))}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Write a generator that yields letters of the alphabet
# 2. Write a generator that yields multiples of 3 up to N
# 3. Write a generator that filters a list to only even numbers
# ============================================
