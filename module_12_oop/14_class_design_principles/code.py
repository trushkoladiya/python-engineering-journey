# ============================================
# MODULE 12 - SUBTOPIC 14: Class Design Principles
# ============================================

# Good class design = focused, simple, reusable classes.
# These principles help you write maintainable OOP code.

# =============================
# 1. SINGLE RESPONSIBILITY PRINCIPLE
# =============================

# --- Example 1: Bad — one class doing too much ---
print("=== Single Responsibility ===")
print()

# BAD: This class does too many things
class UserManagerBad:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.messages = []

    def create(self):
        return f"Created user: {self.name}"

    def send_email(self, msg):
        return f"Email sent to {self.email}: {msg}"

    def save_to_file(self, filename):
        return f"Saved {self.name} to {filename}"

    def generate_report(self):
        return f"Report for {self.name}"

print("  Bad design: UserManagerBad does 4 different jobs!")
print()

# GOOD: Split into focused classes
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"User({self.name}, {self.email})"

class EmailService:
    def send(self, user, message):
        return f"Email to {user.email}: {message}"

class UserStorage:
    def save(self, user, filename):
        return f"Saved {user.name} to {filename}"

class ReportGenerator:
    def generate(self, user):
        return f"Report for {user.name}"

user = User("Trush", "trush@example.com")
email_svc = EmailService()
storage = UserStorage()
reporter = ReportGenerator()

print("  Good design: each class has ONE job:")
print(f"    {user}")
print(f"    {email_svc.send(user, 'Welcome!')}")
print(f"    {storage.save(user, 'users.txt')}")
print(f"    {reporter.generate(user)}")
print()

# =============================
# 2. CLEAN NAMING
# =============================

# --- Example 2: Names should describe the purpose ---
print("=== Clean Naming ===")
print()

# Bad names
class D:               # what is D?
    def p(self, x):    # what is p? what is x?
        pass

# Good names
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        return f"Connected to {self.host}:{self.port}"

db = DatabaseConnection("localhost", 5432)
print(f"  {db.connect()}")
print("  → Class name tells you exactly what it is")
print()

# =============================
# 3. SMALL, FOCUSED METHODS
# =============================

# --- Example 3: Each method does ONE thing ---
print("=== Small Methods ===")
print()

class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self, item, price, quantity):
        """Add a single order."""
        order = {"item": item, "price": price, "qty": quantity}
        self.orders.append(order)

    def calculate_total(self):
        """Calculate total of all orders."""
        total = 0
        for order in self.orders:
            total += order["price"] * order["qty"]
        return total

    def get_summary(self):
        """Get a formatted summary."""
        lines = []
        for order in self.orders:
            subtotal = order["price"] * order["qty"]
            lines.append(f"    {order['item']}: ${subtotal:.2f}")
        lines.append(f"    Total: ${self.calculate_total():.2f}")
        return "\n".join(lines)

processor = OrderProcessor()
processor.add_order("Laptop", 999.99, 1)
processor.add_order("Mouse", 29.99, 2)
processor.add_order("Cable", 9.99, 3)

print("  Order Summary:")
print(processor.get_summary())
print()

# =============================
# 4. COMPOSITION OVER INHERITANCE
# =============================

# --- Example 4: Compose instead of inheriting ---
print("=== Composition Over Inheritance ===")
print()

# Using composition — clear and flexible
class Logger:
    def log(self, message):
        print(f"    [LOG] {message}")

class Validator:
    def validate_email(self, email):
        return "@" in email and "." in email

class UserService:
    def __init__(self):
        self.logger = Logger()        # HAS a logger
        self.validator = Validator()  # HAS a validator

    def register(self, name, email):
        if not self.validator.validate_email(email):
            self.logger.log(f"Invalid email: {email}")
            return f"Registration failed for {name}"

        self.logger.log(f"Registered: {name} ({email})")
        return f"Welcome, {name}!"

service = UserService()
print(f"  {service.register('Trush', 'trush@example.com')}")
print(f"  {service.register('Rahul', 'invalid-email')}")
print()

# =============================
# 5. KEEP __init__ SIMPLE
# =============================

# --- Example 5: Don't do heavy work in __init__ ---
print("=== Simple __init__ ===")
print()

# Good: just set up data
class Config:
    def __init__(self, settings):
        self.settings = settings
        self._validated = False

    def validate(self):
        """Validation is done explicitly, not in __init__."""
        for key in ["host", "port"]:
            if key not in self.settings:
                return f"Missing required setting: {key}"
        self._validated = True
        return "Config is valid"

    def get(self, key, default=None):
        return self.settings.get(key, default)

config = Config({"host": "localhost", "port": 8080, "debug": True})
print(f"  {config.validate()}")
print(f"  host: {config.get('host')}")
print(f"  debug: {config.get('debug')}")
print()

# =============================
# 6. ENCAPSULATE INTERNAL DETAILS
# =============================

# --- Example 6: Hide implementation, expose interface ---
print("=== Encapsulate Details ===")
print()

class PasswordManager:
    def __init__(self):
        self._passwords = {}    # internal storage hidden

    def store(self, site, password):
        """Store a password (simplified — real apps encrypt!)."""
        self._passwords[site] = password
        return f"Stored password for {site}"

    def retrieve(self, site):
        """Retrieve a password."""
        if site in self._passwords:
            return self._passwords[site]
        return "Not found"

    def list_sites(self):
        """Show stored sites (not passwords!)."""
        return list(self._passwords.keys())

pm = PasswordManager()
print(f"  {pm.store('github.com', 'secret123')}")
print(f"  {pm.store('gmail.com', 'pass456')}")
print(f"  Sites: {pm.list_sites()}")
print(f"  github.com password: {pm.retrieve('github.com')}")
print("  → Internal _passwords dict is hidden behind methods")
print()

# =============================
# 7. DESIGN CHECKLIST
# =============================

print("=== Class Design Checklist ===")
print()
print("  ✓ Does the class have ONE clear responsibility?")
print("  ✓ Can you describe it in one sentence (no 'and')?")
print("  ✓ Are method names clear and descriptive?")
print("  ✓ Is __init__ simple (just initialization)?")
print("  ✓ Are internal details hidden behind methods?")
print("  ✓ Are you using composition instead of deep inheritance?")
print("  ✓ Is each method small and focused?")

# ============================================
# TRY IT YOURSELF:
# 1. Take a large class and split it into smaller ones
# 2. Refactor a class with deep inheritance to use composition
# 3. Review your earlier classes — do they follow these principles?
# ============================================
