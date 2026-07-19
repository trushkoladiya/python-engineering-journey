# ============================================
# MODULE 13 - SUBTOPIC 12: Class Internals & Memory
# ============================================

# __dict__ = where attributes are stored
# __slots__ = memory-efficient alternative
import sys

# =============================
# 1. __dict__ — ATTRIBUTE STORAGE
# =============================

# --- Example 1: Exploring __dict__ ---
print("=== __dict__ — Attribute Storage ===")
print()

class Dog:
    species = "Canis familiaris"    # class attribute

    def __init__(self, name, age):
        self.name = name            # instance attribute
        self.age = age              # instance attribute

buddy = Dog("Buddy", 3)

# Instance __dict__ — only instance attributes
print(f"  buddy.__dict__ = {buddy.__dict__}")

# Class __dict__ — class attributes + methods
print(f"  Dog.__dict__ keys: {list(Dog.__dict__.keys())}")

# vars() is the same as __dict__
print(f"  vars(buddy) = {vars(buddy)}")
print()

# =============================
# 2. MODIFYING __dict__ DIRECTLY
# =============================

# --- Example 2: You can modify __dict__ ---
print("=== Modifying __dict__ ===")
print()

class Person:
    def __init__(self, name):
        self.name = name

p = Person("Trush")
print(f"  Before: {p.__dict__}")

# Add attribute via __dict__
p.__dict__["age"] = 21
p.__dict__["email"] = "trush@example.com"
print(f"  After:  {p.__dict__}")
print(f"  p.age = {p.age}")
print(f"  p.email = {p.email}")
print()

# =============================
# 3. CLASS __dict__ vs INSTANCE __dict__
# =============================

# --- Example 3: Where attributes live ---
print("=== Class vs Instance __dict__ ===")
print()

class Car:
    wheels = 4    # class attribute → in Car.__dict__

    def __init__(self, brand):
        self.brand = brand    # instance attribute → in car.__dict__

car = Car("Toyota")

print(f"  'brand' in car.__dict__?  {('brand' in car.__dict__)}")
print(f"  'wheels' in car.__dict__? {('wheels' in car.__dict__)}")
print(f"  'wheels' in Car.__dict__? {('wheels' in Car.__dict__)}")
print()
print("  Python looks in instance __dict__ first,")
print("  then class __dict__, then parent __dict__")
print()

# =============================
# 4. __slots__ — MEMORY OPTIMIZATION
# =============================

# --- Example 4: Restricting attributes ---
print("=== __slots__ ===")
print()

class PointSlotted:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointNormal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p_slot = PointSlotted(1, 2)
p_norm = PointNormal(1, 2)

print(f"  Slotted: x={p_slot.x}, y={p_slot.y}")
print(f"  Normal:  x={p_norm.x}, y={p_norm.y}")
print()

# Slotted objects have NO __dict__
print(f"  Normal has __dict__? {hasattr(p_norm, '__dict__')}")
print(f"  Slotted has __dict__? {hasattr(p_slot, '__dict__')}")
print()

# Can't add new attributes to slotted objects
try:
    p_slot.z = 3
except AttributeError as e:
    print(f"  p_slot.z = 3 → {e}")

# Normal objects can
p_norm.z = 3
print(f"  p_norm.z = {p_norm.z} (works fine)")
print()

# =============================
# 5. MEMORY COMPARISON
# =============================

# --- Example 5: __slots__ saves memory ---
print("=== Memory Comparison ===")
print()

size_normal = sys.getsizeof(p_norm) + sys.getsizeof(p_norm.__dict__)
size_slotted = sys.getsizeof(p_slot)

print(f"  Normal Point size:  ~{size_normal} bytes")
print(f"  Slotted Point size: ~{size_slotted} bytes")
print()

# With many instances, the savings add up
normal_points = [PointNormal(i, i) for i in range(1000)]
slotted_points = [PointSlotted(i, i) for i in range(1000)]

# Rough size estimate
normal_total = sum(sys.getsizeof(p) + sys.getsizeof(p.__dict__) for p in normal_points)
slotted_total = sum(sys.getsizeof(p) for p in slotted_points)

print(f"  1000 Normal Points:  ~{normal_total:,} bytes")
print(f"  1000 Slotted Points: ~{slotted_total:,} bytes")
print(f"  Savings: ~{normal_total - slotted_total:,} bytes ({(1 - slotted_total/normal_total)*100:.0f}%)")
print()

# =============================
# 6. __slots__ WITH METHODS
# =============================

# --- Example 6: __slots__ with full class features ---
print("=== __slots__ with Methods ===")
print()

class Vector:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2

print(f"  {v1} magnitude = {v1.magnitude()}")
print(f"  {v1} + {v2} = {v3}")
print("  → __slots__ works with all methods and dunders!")
print()

# =============================
# 7. INSPECTING OBJECTS
# =============================

# --- Example 7: Useful inspection tools ---
print("=== Inspecting Objects ===")
print()

class Employee:
    company = "TechCorp"

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def info(self):
        return f"{self.name} ({self.role})"

emp = Employee("Trush", "Developer")

# dir() — shows ALL available attributes/methods
print(f"  dir(emp) filtered: {[a for a in dir(emp) if not a.startswith('_')]}")

# vars() — instance attributes only
print(f"  vars(emp) = {vars(emp)}")

# type() — class info
print(f"  type(emp) = {type(emp)}")

# hasattr / getattr
print(f"  hasattr(emp, 'name') = {hasattr(emp, 'name')}")
print(f"  getattr(emp, 'salary', 'N/A') = {getattr(emp, 'salary', 'N/A')}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a class and explore its __dict__
# 2. Create the same class with __slots__ and compare memory
# 3. Try adding attributes dynamically to both and see what happens
# ============================================
