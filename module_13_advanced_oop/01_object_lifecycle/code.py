# ============================================
# MODULE 13 - SUBTOPIC 1: Object Lifecycle
# ============================================

# When you create an object, Python calls:
#   1. __new__  → creates the object
#   2. __init__ → initializes the object

# =============================
# 1. THE CREATION FLOW
# =============================

# --- Example 1: Seeing the lifecycle ---
print("=== Object Creation Flow ===")
print()

class Dog:
    def __new__(cls, name, age):
        print(f"  1. __new__ called (cls={cls.__name__})")
        instance = super().__new__(cls)    # actually create the object
        print(f"     Object created at {id(instance)}")
        return instance

    def __init__(self, name, age):
        print(f"  2. __init__ called (self at {id(self)})")
        self.name = name
        self.age = age
        print(f"     Initialized: {self.name}, age {self.age}")

print("Creating a Dog:")
buddy = Dog("Buddy", 3)
print()

# =============================
# 2. __new__ RECEIVES cls, __init__ RECEIVES self
# =============================

# --- Example 2: The parameters explained ---
print("=== Parameters: cls vs self ===")
print()

class Cat:
    def __new__(cls, name):
        # cls = the CLASS itself (Cat)
        print(f"  __new__ receives cls: {cls}")
        print(f"  cls is Cat? {cls is Cat}")
        return super().__new__(cls)

    def __init__(self, name):
        # self = the specific OBJECT just created
        print(f"  __init__ receives self: {self}")
        self.name = name

whiskers = Cat("Whiskers")
print()

# =============================
# 3. NORMAL USAGE — ONLY __init__
# =============================

# --- Example 3: 99% of the time, you only need __init__ ---
print("=== Normal Usage (just __init__) ===")
print()

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student({self.name}, {self.grade})"

s = Student("Trush", "A")
print(f"  {s}")
print("  → No __new__ needed for normal classes!")
print()

# =============================
# 4. __new__ WITH IMMUTABLE TYPES
# =============================

# --- Example 4: Subclassing str (must use __new__) ---
print("=== __new__ with Immutable Types ===")
print()

# str is immutable — you MUST set the value in __new__
class UpperStr(str):
    def __new__(cls, value):
        # Modify the value BEFORE the object is created
        instance = super().__new__(cls, value.upper())
        return instance

s1 = UpperStr("hello world")
s2 = UpperStr("python is great")

print(f"  UpperStr('hello world') = '{s1}'")
print(f"  UpperStr('python is great') = '{s2}'")
print(f"  Type: {type(s1)}")
print()

# --- Example 5: Subclassing int ---
class ClampedInt(int):
    """An integer clamped between 0 and 100."""
    def __new__(cls, value):
        value = max(0, min(100, value))
        return super().__new__(cls, value)

c1 = ClampedInt(50)
c2 = ClampedInt(200)    # clamped to 100
c3 = ClampedInt(-30)    # clamped to 0

print(f"  ClampedInt(50) = {c1}")
print(f"  ClampedInt(200) = {c2}")
print(f"  ClampedInt(-30) = {c3}")
print()

# =============================
# 5. __del__ — DESTRUCTOR
# =============================

# --- Example 6: Cleanup on deletion ---
print("=== __del__ (Destructor) ===")
print()

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        print(f"  Opened '{self.filename}'")

    def __del__(self):
        print(f"  Closed '{self.filename}' (cleanup)")

print("  Creating handler:")
handler = FileHandler("data.txt")
print("  Deleting handler:")
del handler
print()

# =============================
# 6. __new__ CONTROLLING CREATION
# =============================

# --- Example 7: Conditionally returning different objects ---
print("=== __new__ Controls Creation ===")
print()

class PositiveNumber:
    """Only creates an object if value is positive."""
    def __new__(cls, value):
        if value <= 0:
            print(f"  Rejected: {value} (not positive)")
            return None    # don't create the object!
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        if self is not None:
            self.value = value

p1 = PositiveNumber(42)
p2 = PositiveNumber(-5)
p3 = PositiveNumber(0)

print(f"  PositiveNumber(42): {p1}")
print(f"  PositiveNumber(-5): {p2}")
print(f"  PositiveNumber(0): {p3}")
print()

# =============================
# 7. LIFECYCLE SUMMARY
# =============================

print("=== Object Lifecycle Summary ===")
print()

class Tracked:
    def __new__(cls, name):
        print(f"  Step 1: __new__  — Create '{name}'")
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        print(f"  Step 2: __init__ — Initialize '{name}'")

    def __del__(self):
        print(f"  Step 3: __del__  — Destroy '{self.name}'")

print("  Full lifecycle:")
obj = Tracked("test")
del obj

# ============================================
# TRY IT YOURSELF:
# 1. Create a class that prints messages in __new__, __init__, __del__
# 2. Create a subclass of str that reverses the input
# 3. Create a subclass of int that only allows even numbers
# ============================================
