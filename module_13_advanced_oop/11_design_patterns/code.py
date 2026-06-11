# ============================================
# MODULE 13 - SUBTOPIC 11: Design Patterns (Introduction)
# ============================================

# Design patterns = proven solutions to common problems.
# Three fundamental patterns: Singleton, Factory, Strategy.

# =============================
# 1. SINGLETON PATTERN
# =============================

# --- Example 1: Only one instance ever ---
print("=== Singleton Pattern ===")
print()

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("    Creating the ONE Logger instance")
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        self.logs.append(message)
        print(f"    [LOG] {message}")

    def show_logs(self):
        return self.logs.copy()

# No matter how many times you call Logger(), you get the same object
logger1 = Logger()
logger2 = Logger()

print(f"  logger1 is logger2? {logger1 is logger2}")  # True!
print()

logger1.log("App started")
logger2.log("Processing data")     # same object!

print(f"  All logs: {logger1.show_logs()}")
print()

# =============================
# 2. SINGLETON — CONFIGURATION
# =============================

# --- Example 2: App configuration singleton ---
print("=== Singleton: Configuration ===")
print()

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._settings = {}
        return cls._instance

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key, default=None):
        return self._settings.get(key, default)

    def show(self):
        return dict(self._settings)

# Set config in one place
config = Config()
config.set("debug", True)
config.set("host", "localhost")
config.set("port", 8080)

# Read it anywhere — same instance
another_ref = Config()
print(f"  debug: {another_ref.get('debug')}")
print(f"  host: {another_ref.get('host')}")
print(f"  All: {another_ref.show()}")
print()

# =============================
# 3. FACTORY PATTERN
# =============================

# --- Example 3: Create objects without knowing the class ---
print("=== Factory Pattern ===")
print()

class Shape:
    def area(self):
        raise NotImplementedError

    def __str__(self):
        return f"{type(self).__name__}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class ShapeFactory:
    """Creates shapes without the caller knowing the classes."""

    @staticmethod
    def create(shape_type, **kwargs):
        shapes = {
            "circle": Circle,
            "rectangle": Rectangle,
            "triangle": Triangle,
        }
        if shape_type not in shapes:
            raise ValueError(f"Unknown shape: {shape_type}")
        return shapes[shape_type](**kwargs)

# User doesn't need to know Circle, Rectangle, Triangle classes
s1 = ShapeFactory.create("circle", radius=5)
s2 = ShapeFactory.create("rectangle", width=4, height=6)
s3 = ShapeFactory.create("triangle", base=3, height=8)

for shape in [s1, s2, s3]:
    print(f"  {shape}: area = {shape.area():.2f}")
print()

# =============================
# 4. FACTORY — FROM DATA
# =============================

# --- Example 4: Create objects from configuration data ---
print("=== Factory: From Data ===")
print()

class NotifierFactory:
    @staticmethod
    def create(config):
        notifier_type = config.get("type")
        if notifier_type == "email":
            return EmailNotifier(config["address"])
        elif notifier_type == "sms":
            return SMSNotifier(config["phone"])
        elif notifier_type == "slack":
            return SlackNotifier(config["channel"])
        raise ValueError(f"Unknown notifier: {notifier_type}")

class EmailNotifier:
    def __init__(self, address):
        self.address = address
    def send(self, msg):
        return f"Email to {self.address}: {msg}"

class SMSNotifier:
    def __init__(self, phone):
        self.phone = phone
    def send(self, msg):
        return f"SMS to {self.phone}: {msg}"

class SlackNotifier:
    def __init__(self, channel):
        self.channel = channel
    def send(self, msg):
        return f"Slack #{self.channel}: {msg}"

# Create notifiers from config data
configs = [
    {"type": "email", "address": "trush@example.com"},
    {"type": "sms", "phone": "+1234567890"},
    {"type": "slack", "channel": "alerts"},
]

for cfg in configs:
    notifier = NotifierFactory.create(cfg)
    print(f"  {notifier.send('Server is up!')}")
print()

# =============================
# 5. STRATEGY PATTERN
# =============================

# --- Example 5: Swappable algorithms ---
print("=== Strategy Pattern ===")
print()

class BubbleSortStrategy:
    def sort(self, data):
        result = data.copy()
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result

    def __str__(self):
        return "BubbleSort"

class BuiltinSortStrategy:
    def sort(self, data):
        return sorted(data)

    def __str__(self):
        return "BuiltinSort"

class ReverseSortStrategy:
    def sort(self, data):
        return sorted(data, reverse=True)

    def __str__(self):
        return "ReverseSort"

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

    def set_strategy(self, strategy):
        self.strategy = strategy

data = [64, 34, 25, 12, 22, 11, 90]

sorter = Sorter(BubbleSortStrategy())
print(f"  {sorter.strategy}: {sorter.sort(data)}")

sorter.set_strategy(BuiltinSortStrategy())
print(f"  {sorter.strategy}: {sorter.sort(data)}")

sorter.set_strategy(ReverseSortStrategy())
print(f"  {sorter.strategy}: {sorter.sort(data)}")
print()

# =============================
# 6. STRATEGY — PRICING
# =============================

# --- Example 6: Different pricing strategies ---
print("=== Strategy: Pricing ===")
print()

class RegularPricing:
    def calculate(self, price):
        return price

    def __str__(self):
        return "Regular (no discount)"

class MemberPricing:
    def calculate(self, price):
        return price * 0.9    # 10% off

    def __str__(self):
        return "Member (10% off)"

class VIPPricing:
    def calculate(self, price):
        return price * 0.75   # 25% off

    def __str__(self):
        return "VIP (25% off)"

class ShoppingCart:
    def __init__(self, pricing_strategy):
        self.items = []
        self.pricing = pricing_strategy

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def total(self):
        raw_total = sum(item["price"] for item in self.items)
        return self.pricing.calculate(raw_total)

    def show(self):
        raw = sum(item["price"] for item in self.items)
        final = self.total()
        saving = raw - final
        print(f"  Strategy: {self.pricing}")
        print(f"  Raw total: ${raw:.2f}")
        print(f"  Final: ${final:.2f} (saved ${saving:.2f})")

items = [("Laptop", 999), ("Mouse", 29), ("Keyboard", 79)]

for strategy in [RegularPricing(), MemberPricing(), VIPPricing()]:
    cart = ShoppingCart(strategy)
    for name, price in items:
        cart.add_item(name, price)
    cart.show()
    print()

# ============================================
# TRY IT YOURSELF:
# 1. Create a Singleton for a database connection
# 2. Create a Factory that builds different report types
# 3. Create a Strategy pattern for different tax calculations
# ============================================
