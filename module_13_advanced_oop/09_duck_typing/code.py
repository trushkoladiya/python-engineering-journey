# ============================================
# MODULE 13 - SUBTOPIC 9: Duck Typing & Dynamic Typing
# ============================================

# Duck typing = "If it walks like a duck and quacks like a duck,
#                then it's a duck."
# Python cares about BEHAVIOR, not TYPE.

# =============================
# 1. BASIC DUCK TYPING
# =============================

# --- Example 1: No inheritance needed —  just matching methods ---
print("=== Basic Duck Typing ===")
print()

class Duck:
    def quack(self):
        return "Quack!"

    def walk(self):
        return "Waddle waddle"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

    def walk(self):
        return "Walking normally"

class RubberDuck:
    def quack(self):
        return "Squeak!"

    def walk(self):
        return "Rolls on the floor"

# This function works with ANY object that has quack() and walk()
def duck_test(thing):
    name = type(thing).__name__
    print(f"  {name}: {thing.quack()}, {thing.walk()}")

duck_test(Duck())
duck_test(Person())
duck_test(RubberDuck())
print()

# =============================
# 2. DUCK TYPING IN PRACTICE
# =============================

# --- Example 2: Any object with the right methods works ---
print("=== Practical Duck Typing ===")
print()

# These classes have NO common parent, but they all work the same way

class FileLogger:
    def log(self, message):
        return f"[FILE] {message}"

class ConsoleLogger:
    def log(self, message):
        return f"[CONSOLE] {message}"

class NetworkLogger:
    def log(self, message):
        return f"[NETWORK] {message}"

# One function works with ALL of them
def process_data(data, logger):
    logger.log(f"Processing: {data}")
    result = data.upper()
    print(f"  {logger.log(f'Result: {result}')}")
    return result

loggers = [FileLogger(), ConsoleLogger(), NetworkLogger()]
for logger in loggers:
    process_data("hello", logger)
print()

# =============================
# 3. PYTHON BUILT-INS USE DUCK TYPING
# =============================

# --- Example 3: len(), for, in all use duck typing ---
print("=== Built-in Duck Typing ===")
print()

class Inventory:
    def __init__(self):
        self.items = ["apple", "banana", "cherry"]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

inv = Inventory()

# len() works — because Inventory has __len__
print(f"  len(inv) = {len(inv)}")

# 'in' works — because Inventory has __contains__
print(f"  'banana' in inv? {'banana' in inv}")

# for loop works — because Inventory has __iter__
print("  Items:", end=" ")
for item in inv:
    print(item, end=" ")
print()
print()

# =============================
# 4. EAFP vs LBYL
# =============================

# --- Example 4: Two approaches ---
print("=== EAFP vs LBYL ===")
print()

class Speaker:
    def speak(self):
        return "Hello!"

class Silent:
    pass

items = [Speaker(), Silent(), Speaker()]

# LBYL — Look Before You Leap
print("  LBYL approach:")
for item in items:
    if hasattr(item, "speak"):
        print(f"    {type(item).__name__}: {item.speak()}")
    else:
        print(f"    {type(item).__name__}: can't speak")

print()

# EAFP — Easier to Ask Forgiveness (Pythonic)
print("  EAFP approach:")
for item in items:
    try:
        print(f"    {type(item).__name__}: {item.speak()}")
    except AttributeError:
        print(f"    {type(item).__name__}: can't speak")
print()

# =============================
# 5. DUCK TYPING WITH OPERATORS
# =============================

# --- Example 5: + works with anything that has __add__ ---
print("=== Duck Typing with Operators ===")
print()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

class Color:
    def __init__(self, r, g, b):
        self.r = min(255, r)
        self.g = min(255, g)
        self.b = min(255, b)

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __str__(self):
        return f"RGB({self.r}, {self.g}, {self.b})"

# Same operator, different types
v = Vector(1, 2) + Vector(3, 4)
c = Color(100, 50, 0) + Color(50, 100, 200)
s = "hello " + "world"
n = [1, 2] + [3, 4]

print(f"  Vector + Vector = {v}")
print(f"  Color + Color   = {c}")
print(f"  str + str       = '{s}'")
print(f"  list + list     = {n}")
print("  → + works with ANY type that defines __add__!")
print()

# =============================
# 6. CALLABLE DUCK TYPING
# =============================

# --- Example 6: Anything callable works as a callback ---
print("=== Callable Duck Typing ===")
print()

def simple_function(x):
    return x * 2

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Both work as callbacks — duck typing!
def apply(func, value):
    return func(value)

print(f"  simple_function(5) = {apply(simple_function, 5)}")
print(f"  Multiplier(3)(5)   = {apply(Multiplier(3), 5)}")
print(f"  Multiplier(10)(5)  = {apply(Multiplier(10), 5)}")
print("  → Both are 'callable' — that's all that matters")
print()

# =============================
# 7. PRACTICAL: FLEXIBLE DATA EXPORTER
# =============================

# --- Example 7: Export to any format using duck typing ---
print("=== Flexible Data Exporter ===")
print()

class CSVWriter:
    def write(self, data):
        return ",".join(str(v) for v in data)

class JSONWriter:
    def write(self, data):
        import json
        return json.dumps(data)

class MarkdownWriter:
    def write(self, data):
        return " | ".join(str(v) for v in data)

# One function, any writer — duck typing
def export_data(data_rows, writer):
    print(f"  Using {type(writer).__name__}:")
    for row in data_rows:
        print(f"    {writer.write(row)}")

data = [
    ["Name", "Age", "City"],
    ["Trush", 21, "NYC"],
    ["Rahul", 22, "LA"],
]

export_data(data, CSVWriter())
print()
export_data(data, JSONWriter())
print()
export_data(data, MarkdownWriter())

# ============================================
# TRY IT YOURSELF:
# 1. Create 3 unrelated classes with a common method name
# 2. Write one function that works with all three (duck typing)
# 3. Try EAFP style to handle objects that might not have the method
# ============================================
