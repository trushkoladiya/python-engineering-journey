# ============================================
# MODULE 13 - SUBTOPIC 8: Abstract Base Classes (Deep)
# ============================================

# ABCs define contracts — required interfaces for subclasses.
# This subtopic covers abstract properties, classmethods, and design.

from abc import ABC, abstractmethod

# =============================
# 1. ABSTRACT PROPERTIES
# =============================

# --- Example 1: Requiring a property ---
print("=== Abstract Properties ===")
print()

class Vehicle(ABC):
    @property
    @abstractmethod
    def fuel_type(self):
        """Each vehicle must declare its fuel type."""
        pass

    @property
    @abstractmethod
    def max_speed(self):
        """Each vehicle must declare its max speed."""
        pass

    def describe(self):
        return f"{type(self).__name__}: {self.fuel_type}, max {self.max_speed} km/h"

class ElectricCar(Vehicle):
    @property
    def fuel_type(self):
        return "Electric"

    @property
    def max_speed(self):
        return 200

class GasCar(Vehicle):
    @property
    def fuel_type(self):
        return "Gasoline"

    @property
    def max_speed(self):
        return 220

for v in [ElectricCar(), GasCar()]:
    print(f"  {v.describe()}")
print()

# Missing property → error
try:
    class BrokenCar(Vehicle):
        @property
        def fuel_type(self):
            return "Solar"
        # forgot max_speed!

    BrokenCar()
except TypeError as e:
    print(f"  BrokenCar() → {e}")
print()

# =============================
# 2. ABSTRACT CLASS METHODS
# =============================

# --- Example 2: Requiring a factory method ---
print("=== Abstract Class Methods ===")
print()

class Serializable(ABC):
    @abstractmethod
    def to_string(self):
        """Convert to string representation."""
        pass

    @classmethod
    @abstractmethod
    def from_string(cls, data):
        """Create instance from string."""
        pass

class Config(Serializable):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def to_string(self):
        return f"{self.host}:{self.port}"

    @classmethod
    def from_string(cls, data):
        host, port = data.split(":")
        return cls(host, int(port))

    def __str__(self):
        return f"Config({self.host}:{self.port})"

# Round-trip: object → string → object
c1 = Config("localhost", 8080)
s = c1.to_string()
c2 = Config.from_string(s)

print(f"  Original: {c1}")
print(f"  String:   '{s}'")
print(f"  Restored: {c2}")
print()

# =============================
# 3. DESIGNING CONTRACTS
# =============================

# --- Example 3: A database interface contract ---
print("=== Contract Design ===")
print()

class Database(ABC):
    """Contract: any database must implement these methods."""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass

    @abstractmethod
    def close(self):
        pass

    # Non-abstract helper method
    def execute(self, sql):
        """Connect, query, close — template method."""
        self.connect()
        result = self.query(sql)
        self.close()
        return result

class SQLiteDB(Database):
    def connect(self):
        print("    [SQLite] Connected")

    def query(self, sql):
        print(f"    [SQLite] Running: {sql}")
        return f"SQLite results for: {sql}"

    def close(self):
        print("    [SQLite] Closed")

class PostgresDB(Database):
    def connect(self):
        print("    [Postgres] Connected")

    def query(self, sql):
        print(f"    [Postgres] Running: {sql}")
        return f"Postgres results for: {sql}"

    def close(self):
        print("    [Postgres] Closed")

# One function works with ANY database
def run_report(db):
    result = db.execute("SELECT * FROM users")
    print(f"    Result: {result}")

print("  SQLite:")
run_report(SQLiteDB())
print()
print("  Postgres:")
run_report(PostgresDB())
print()

# =============================
# 4. MULTIPLE ABSTRACT INTERFACES
# =============================

# --- Example 4: A class implementing multiple ABCs ---
print("=== Multiple Abstract Interfaces ===")
print()

class Printable(ABC):
    @abstractmethod
    def to_display(self):
        pass

class Exportable(ABC):
    @abstractmethod
    def to_csv(self):
        pass

class Report(Printable, Exportable):
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def to_display(self):
        lines = [f"  === {self.title} ==="]
        for row in self.data:
            lines.append(f"    {row}")
        return "\n".join(lines)

    def to_csv(self):
        lines = []
        for row in self.data:
            lines.append(",".join(str(v) for v in row))
        return "\n".join(lines)

report = Report("Sales", [
    ("Product", "Amount"),
    ("Laptop", 999),
    ("Mouse", 29),
])

print(report.to_display())
print()
print("  CSV output:")
print(f"  {report.to_csv()}")
print()

# =============================
# 5. __subclasshook__ — STRUCTURAL TYPING
# =============================

# --- Example 5: isinstance() without inheritance ---
print("=== __subclasshook__ ===")
print()

class Drawable(ABC):
    @classmethod
    def __subclasshook__(cls, C):
        # Any class with a 'draw' method is considered Drawable
        if any("draw" in B.__dict__ for B in C.__mro__):
            return True
        return NotImplemented

# This class doesn't inherit from Drawable but HAS draw()
class Circle:
    def draw(self):
        return "Drawing circle"

# This class has no draw()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

c = Circle()
p = Point(1, 2)

print(f"  isinstance(Circle(), Drawable)? {isinstance(c, Drawable)}")
print(f"  isinstance(Point(1,2), Drawable)? {isinstance(p, Drawable)}")
print("  → Structural check: does it have draw()? Not: does it inherit?")
print()

# =============================
# 6. PRACTICAL: PAYMENT PROCESSOR INTERFACE
# =============================

# --- Example 6: Real-world ABC pattern ---
print("=== Payment Processor Interface ===")
print()

class PaymentProcessor(ABC):
    @abstractmethod
    def authorize(self, amount):
        pass

    @abstractmethod
    def capture(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def process(self, amount):
        """Template: authorize then capture."""
        auth = self.authorize(amount)
        if auth:
            return self.capture(amount)
        return "Authorization failed"

class StripeProcessor(PaymentProcessor):
    def authorize(self, amount):
        print(f"    [Stripe] Authorized ${amount:.2f}")
        return True

    def capture(self, amount):
        return f"[Stripe] Captured ${amount:.2f}"

    def refund(self, amount):
        return f"[Stripe] Refunded ${amount:.2f}"

class PayPalProcessor(PaymentProcessor):
    def authorize(self, amount):
        print(f"    [PayPal] Authorized ${amount:.2f}")
        return True

    def capture(self, amount):
        return f"[PayPal] Captured ${amount:.2f}"

    def refund(self, amount):
        return f"[PayPal] Refunded ${amount:.2f}"

processors = [StripeProcessor(), PayPalProcessor()]
for proc in processors:
    result = proc.process(49.99)
    print(f"    {result}")
    print(f"    {proc.refund(10.00)}")
    print()

# ============================================
# TRY IT YOURSELF:
# 1. Create an abstract 'Messenger' with send() and receive()
# 2. Add an abstract property 'service_name'
# 3. Implement EmailMessenger and SMSMessenger
# ============================================
