# ============================================
# MODULE 12 - SUBTOPIC 11: Abstraction & ABCs
# ============================================

# Abstraction = hide the details, show only the interface.
# Abstract Base Classes (ABCs) enforce that child classes
# implement certain methods.

from abc import ABC, abstractmethod

# =============================
# 1. THE PROBLEM WITHOUT ABSTRACTION
# =============================

# --- Example 1: No enforcement ---
print("=== Without Abstraction ===")
print()

class ShapeBad:
    def area(self):
        pass    # "should" be implemented, but nothing forces it

class CircleBad(ShapeBad):
    def __init__(self, radius):
        self.radius = radius
    # Forgot to implement area()!

c = CircleBad(5)
print(f"  CircleBad area: {c.area()}")   # Returns None — no error, just wrong!
print("  Problem: no enforcement, no error, just a silent bug!")
print()

# =============================
# 2. ABSTRACT BASE CLASS
# =============================

# --- Example 2: Enforcing implementation ---
print("=== Abstract Base Class ===")
print()

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter."""
        pass

    def describe(self):
        """Non-abstract method — shared by all shapes."""
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"

# Can't create Shape directly!
try:
    s = Shape()
except TypeError as e:
    print(f"  Shape() → TypeError: {e}")
print()

# =============================
# 3. IMPLEMENTING ABSTRACT CLASSES
# =============================

# --- Example 3: Concrete implementations ---
print("=== Concrete Implementations ===")
print()

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c, base, height):
        self.a = a
        self.b = b
        self.c = c
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.a + self.b + self.c

# All shapes work with the same interface
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(3, 4, 5, 3, 4),
]

for shape in shapes:
    print(f"  {shape.describe()}")
print()

# =============================
# 4. FORGETTING TO IMPLEMENT
# =============================

# --- Example 4: What happens if you forget ---
print("=== Forgetting Abstract Methods ===")
print()

class IncompleteShape(Shape):
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0
    # Forgot perimeter()!

try:
    s = IncompleteShape("test")
except TypeError as e:
    print(f"  IncompleteShape() → TypeError: {e}")
    print("  → Python forces you to implement ALL abstract methods!")
print()

# =============================
# 5. ABSTRACT CLASS WITH NORMAL METHODS
# =============================

# --- Example 5: Mix of abstract and regular methods ---
print("=== Abstract + Normal Methods ===")
print()

class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def max_speed(self):
        pass

    # Normal method — shared by all vehicles
    def info(self):
        return (f"{self.brand} ({self.year}): "
                f"fuel={self.fuel_type()}, max speed={self.max_speed()} km/h")

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"

    def max_speed(self):
        return 200

class GasCar(Vehicle):
    def fuel_type(self):
        return "Gasoline"

    def max_speed(self):
        return 180

class Bicycle(Vehicle):
    def fuel_type(self):
        return "Human power"

    def max_speed(self):
        return 30

vehicles = [
    ElectricCar("Tesla", 2024),
    GasCar("Toyota", 2023),
    Bicycle("Trek", 2022),
]

for v in vehicles:
    print(f"  {v.info()}")
print()

# =============================
# 6. PRACTICAL: NOTIFICATION SYSTEM
# =============================

# --- Example 6: Abstract notification interface ---
print("=== Notification System ===")
print()

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

    def format_message(self, message):
        return f"[NOTIFICATION] {message}"

class EmailNotifier(Notifier):
    def send(self, recipient, message):
        formatted = self.format_message(message)
        return f"Email to {recipient}: {formatted}"

class SMSNotifier(Notifier):
    def send(self, recipient, message):
        formatted = self.format_message(message)
        return f"SMS to {recipient}: {formatted}"

class SlackNotifier(Notifier):
    def send(self, recipient, message):
        formatted = self.format_message(message)
        return f"Slack to #{recipient}: {formatted}"

# One function works with ANY notifier
def notify_all(notifiers, recipient, message):
    for notifier in notifiers:
        print(f"  {notifier.send(recipient, message)}")

notifiers = [EmailNotifier(), SMSNotifier(), SlackNotifier()]
notify_all(notifiers, "team", "Deploy completed!")

# ============================================
# TRY IT YOURSELF:
# 1. Create an abstract 'Database' class with:
#    abstract methods: connect(), query(sql), close()
# 2. Implement 'SQLiteDB' and 'PostgresDB' subclasses
# 3. Write a function that works with any database
# ============================================
