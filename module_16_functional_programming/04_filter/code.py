# ============================================
# MODULE 16 - SUBTOPIC 4: filter()
# ============================================

# filter() selects elements where a function returns True.
# It returns a lazy iterator.

# =============================
# 1. BASIC filter()
# =============================

print("=== Basic filter() ===")
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  numbers: {numbers}")
print(f"  evens:   {evens}")

# Keep only odd numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"  odds:    {odds}")
print()

# =============================
# 2. PREDICATE FUNCTIONS
# =============================

print("=== Predicate Functions ===")
print()

# A predicate is a function that returns True or False

def is_positive(x):
    """Return True if x is positive."""
    return x > 0

def is_long_word(word):
    """Return True if word has more than 4 characters."""
    return len(word) > 4

# Using predicates with filter
data = [-5, -2, 0, 3, 7, -1, 8]
positives = list(filter(is_positive, data))
print(f"  data:      {data}")
print(f"  positives: {positives}")
print()

words = ["hi", "hello", "hey", "greetings", "yo", "welcome"]
long_words = list(filter(is_long_word, words))
print(f"  words:      {words}")
print(f"  long words: {long_words}")
print()

# =============================
# 3. filter() WITH STRINGS
# =============================

print("=== filter() with Strings ===")
print()

# Filter strings that start with a vowel
names = ["Trush", "Rahul", "Eve", "Oscar", "Uma", "Charlie"]
vowel_names = list(filter(lambda n: n[0].lower() in "aeiou", names))
print(f"  Names: {names}")
print(f"  Start with vowel: {vowel_names}")
print()

# Filter non-empty strings
mixed = ["hello", "", "world", "", "", "python"]
non_empty = list(filter(lambda s: s != "", mixed))
print(f"  Mixed: {mixed}")
print(f"  Non-empty: {non_empty}")
print()

# =============================
# 4. filter() WITH None
# =============================

print("=== filter(None, ...) — Remove Falsy Values ===")
print()

# None as the function removes all falsy values
data = [0, 1, "", "hello", None, 42, False, True, [], [1, 2]]
truthy = list(filter(None, data))
print(f"  data:   {data}")
print(f"  truthy: {truthy}")
print()

# Practical: clean up a list of inputs
user_inputs = ["Trush", "", "Rahul", "", "", "Eve"]
cleaned = list(filter(None, user_inputs))
print(f"  Raw inputs: {user_inputs}")
print(f"  Cleaned:    {cleaned}")
print()

# =============================
# 5. filter() WITH DICTIONARIES
# =============================

print("=== filter() with Dictionaries ===")
print()

products = [
    {"name": "Laptop", "price": 999, "in_stock": True},
    {"name": "Phone", "price": 699, "in_stock": False},
    {"name": "Tablet", "price": 449, "in_stock": True},
    {"name": "Watch", "price": 299, "in_stock": True},
    {"name": "Camera", "price": 1299, "in_stock": False},
]

# Filter products in stock
in_stock = list(filter(lambda p: p["in_stock"], products))
print("  In stock:")
for p in in_stock:
    print(f"    {p['name']} - ${p['price']}")
print()

# Filter affordable products (under $500)
affordable = list(filter(lambda p: p["price"] < 500, products))
print("  Under $500:")
for p in affordable:
    print(f"    {p['name']} - ${p['price']}")
print()

# =============================
# 6. CHAINING filter() AND map()
# =============================

print("=== Chaining filter() and map() ===")
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: filter even numbers
# Step 2: square them
evens = filter(lambda x: x % 2 == 0, numbers)
squared_evens = list(map(lambda x: x ** 2, evens))

print(f"  numbers: {numbers}")
print(f"  even numbers squared: {squared_evens}")
print()

# One-liner (nested)
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(f"  Same as one-liner: {result}")
print()

# =============================
# 7. filter() vs LIST COMPREHENSION
# =============================

print("=== filter() vs List Comprehension ===")
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Both do the same thing
result_filter = list(filter(lambda x: x > 4, numbers))
result_comp = [x for x in numbers if x > 4]

print(f"  filter(): {result_filter}")
print(f"  comprehension: {result_comp}")
print(f"  Same? {result_filter == result_comp}")
print()

# Combined filter + map vs comprehension
result_chain = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
result_comp2 = [x ** 2 for x in numbers if x % 2 == 0]
print(f"  filter+map: {result_chain}")
print(f"  comprehension: {result_comp2}")
print()

# =============================
# 8. PRACTICAL EXAMPLE
# =============================

print("=== Practical: Data Cleaning ===")
print()

# Raw data with issues
raw_data = [" Trush ", "  ", "RAHUL", "", "eve", None, "  Charlie  "]

# Step 1: Remove None values
no_none = filter(lambda x: x is not None, raw_data)

# Step 2: Strip whitespace
stripped = map(str.strip, no_none)

# Step 3: Remove empty strings
non_empty = filter(None, stripped)

# Step 4: Title case
cleaned = list(map(str.title, non_empty))

print(f"  Raw:     {raw_data}")
print(f"  Cleaned: {cleaned}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Filter a list of numbers to keep only primes
#    (write an is_prime predicate)
# 2. Filter a list of dicts to find items above a threshold
# 3. Chain filter() and map() to process string data
# ============================================
