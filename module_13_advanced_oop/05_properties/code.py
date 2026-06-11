# ============================================
# MODULE 13 - SUBTOPIC 5: Properties (@property)
# ============================================

# Properties = methods that look like attributes.
# Clean syntax with getter/setter/deleter control.

# =============================
# 1. BASIC PROPERTY (GETTER)
# =============================

# --- Example 1: Read-only property ---
print("=== Basic Property (Getter) ===")
print()

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter — called when you access .radius"""
        return self._radius

    @property
    def area(self):
        """Computed property — calculated on the fly."""
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

c = Circle(5)
print(f"  Radius: {c.radius}")
print(f"  Area: {c.area:.2f}")
print(f"  Circumference: {c.circumference:.2f}")

# area is read-only (no setter)
try:
    c.area = 100
except AttributeError as e:
    print(f"  c.area = 100 → {e}")
print()

# =============================
# 2. PROPERTY WITH SETTER
# =============================

# --- Example 2: Getter + setter with validation ---
print("=== Property with Setter ===")
print()

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius    # calls the setter!

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

    def __str__(self):
        return f"{self._celsius}°C ({self.fahrenheit:.1f}°F)"

t = Temperature(100)
print(f"  {t}")

t.celsius = 0
print(f"  Set celsius=0: {t}")

t.fahrenheit = 212
print(f"  Set fahrenheit=212: {t}")

try:
    t.celsius = -300
except ValueError as e:
    print(f"  Invalid: {e}")
print()

# =============================
# 3. READ-ONLY COMPUTED PROPERTIES
# =============================

# --- Example 3: Properties that compute from other attributes ---
print("=== Computed Properties ===")
print()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

r = Rectangle(5, 3)
print(f"  {r}")
print(f"  Area: {r.area}")
print(f"  Perimeter: {r.perimeter}")
print(f"  Is square? {r.is_square}")

r.width = 3
print(f"  After width=3: area={r.area}, is_square={r.is_square}")
print()

# =============================
# 4. PROPERTY WITH DELETER
# =============================

# --- Example 4: Full getter/setter/deleter ---
print("=== Property with Deleter ===")
print()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError(f"Invalid email: '{value}'")
        self._email = value

    @email.deleter
    def email(self):
        print(f"    Removing email for {self.name}")
        self._email = None

user = User("Trush", "trush@example.com")
print(f"  Email: {user.email}")

user.email = "newtrush@test.org"
print(f"  Changed: {user.email}")

del user.email
print(f"  After delete: {user.email}")
print()

# =============================
# 5. PROPERTY vs MANUAL GETTERS/SETTERS
# =============================

# --- Example 5: Clean syntax comparison ---
print("=== Property vs Manual ===")
print()

# Old way (ugly)
class BankAccountOld:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        if value < 0:
            raise ValueError("Can't be negative")
        self._balance = value

# New way (clean with @property)
class BankAccount:
    def __init__(self, balance):
        self.balance = balance     # uses property setter

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance can't be negative")
        self._balance = value

# Old way:
old_acc = BankAccountOld(1000)
print(f"  Old: get_balance() = {old_acc.get_balance()}")

# New way:
new_acc = BankAccount(1000)
print(f"  New: balance = {new_acc.balance}")

new_acc.balance = 2000
print(f"  New: balance = {new_acc.balance}")

try:
    new_acc.balance = -100
except ValueError as e:
    print(f"  New: {e}")
print()

# =============================
# 6. PRACTICAL: PERSON CLASS
# =============================

# --- Example 6: Full practical example ---
print("=== Practical: Person Class ===")
print()

class Person:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        parts = value.split(" ", 1)
        if len(parts) != 2:
            raise ValueError("Full name must have first and last name")
        self.first_name = parts[0]
        self.last_name = parts[1]

    @property
    def age(self):
        return 2026 - self.birth_year

    @property
    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}."

    def __str__(self):
        return f"{self.full_name} (age {self.age})"

p = Person("Trush", "Smith", 2005)
print(f"  {p}")
print(f"  Initials: {p.initials}")

p.full_name = "Rahul Johnson"
print(f"  After name change: {p}")
print(f"  First: {p.first_name}, Last: {p.last_name}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a Product class with a price property (must be >= 0)
# 2. Add a 'tax_price' computed property (price * 1.1)
# 3. Create a Student with a 'grade' property that only accepts A-F
# ============================================
