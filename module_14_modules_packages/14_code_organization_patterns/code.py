# ============================================
# MODULE 14 - SUBTOPIC 14: Code Organization Patterns
# ============================================

# How to structure code into modules and packages
# for real-world projects.

import os
import sys
import tempfile
import shutil

# =============================
# 1. THE PROBLEM: ONE BIG FILE
# =============================

print("=== The Problem: Monolithic Code ===")
print()

# Imagine ALL of this in ONE file...
# It quickly becomes unmanageable!

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def validate_email(email):
    return "@" in email and "." in email

def validate_price(price):
    return price > 0

def format_currency(amount):
    return f"${amount:,.2f}"

def format_name(name):
    return name.title()

# 300 more lines...

print("  ONE file with everything = hard to maintain!")
print("  Solution: split into focused modules")
print()

# =============================
# 2. THE SOLUTION: SEPARATED MODULES
# =============================

print("=== Solution: Separated by Responsibility ===")
print()

# Create a well-organized project
base_dir = tempfile.mkdtemp()
project_dir = os.path.join(base_dir, "store")
os.makedirs(project_dir)

# Create __init__.py
with open(os.path.join(project_dir, "__init__.py"), "w") as f:
    f.write("")

# models.py — data classes
with open(os.path.join(project_dir, "models.py"), "w") as f:
    f.write('''
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"User({self.name}, {self.email})"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"Product({self.name}, ${self.price:.2f})"

class Order:
    def __init__(self, user, products):
        self.user = user
        self.products = list(products)
    
    @property
    def total(self):
        return sum(p.price for p in self.products)
    
    def __str__(self):
        return f"Order({self.user.name}, {len(self.products)} items, ${self.total:.2f})"
''')

# validators.py — validation logic
with open(os.path.join(project_dir, "validators.py"), "w") as f:
    f.write('''
def is_valid_email(email):
    return isinstance(email, str) and "@" in email and "." in email

def is_valid_price(price):
    return isinstance(price, (int, float)) and price > 0

def is_valid_name(name):
    return isinstance(name, str) and len(name.strip()) >= 2
''')

# formatters.py — output formatting
with open(os.path.join(project_dir, "formatters.py"), "w") as f:
    f.write('''
def format_currency(amount):
    return f"${amount:,.2f}"

def format_name(name):
    return name.strip().title()

def format_order_summary(order):
    lines = [f"Order for {order.user.name}:"]
    for i, product in enumerate(order.products, 1):
        lines.append(f"  {i}. {product.name} — {format_currency(product.price)}")
    lines.append(f"  Total: {format_currency(order.total)}")
    return "\\n".join(lines)
''')

# Show the structure
print("  Project structure:")
print("    store/")
print("    ├── __init__.py")
print("    ├── models.py       ← User, Product, Order")
print("    ├── validators.py   ← validation functions")
print("    └── formatters.py   ← formatting functions")
print()

# Use the organized code
sys.path.insert(0, base_dir)

from store.models import User, Product, Order
from store.validators import is_valid_email, is_valid_price, is_valid_name
from store.formatters import format_currency, format_name, format_order_summary

# =============================
# 3. USING THE ORGANIZED CODE
# =============================

print("=== Using the Organized Code ===")
print()

# Validate input
name = "  trush koladiya  "
email = "trushkoladiya.work@gmail.com"
print(f"  Validating '{name}':")
print(f"    Valid name? {is_valid_name(name)}")
print(f"    Formatted: '{format_name(name)}'")
print(f"  Validating '{email}':")
print(f"    Valid email? {is_valid_email(email)}")
print()

# Create objects
user = User(format_name(name), email)
products = [
    Product("Laptop", 999.99),
    Product("Mouse", 29.99),
    Product("Keyboard", 79.50),
]

print(f"  {user}")
for p in products:
    print(f"  {p}")
print()

# Create order and display
order = Order(user, products)
print(format_order_summary(order))
print()

# =============================
# 4. CONSTANTS MODULE PATTERN
# =============================

print("=== Constants Module Pattern ===")
print()

# Create constants.py
with open(os.path.join(project_dir, "constants.py"), "w") as f:
    f.write('''
# Application constants
APP_NAME = "MyStore"
VERSION = "1.0.0"

# Business rules
MAX_ITEMS_PER_ORDER = 50
MIN_ORDER_AMOUNT = 10.00
TAX_RATE = 0.08

# Status codes
STATUS_PENDING = "pending"
STATUS_SHIPPED = "shipped"
STATUS_DELIVERED = "delivered"
''')

from store.constants import APP_NAME, VERSION, TAX_RATE, MAX_ITEMS_PER_ORDER

print(f"  {APP_NAME} v{VERSION}")
print(f"  Tax rate: {TAX_RATE * 100}%")
print(f"  Max items per order: {MAX_ITEMS_PER_ORDER}")
print(f"  Order total with tax: {format_currency(order.total * (1 + TAX_RATE))}")
print()

# =============================
# 5. COMMON PROJECT STRUCTURES
# =============================

print("=== Common Project Structures ===")
print()

# --- Small project ---
print("  Small project:")
print("    project/")
print("    ├── main.py")
print("    ├── utils.py")
print("    └── config.py")
print()

# --- Medium project ---
print("  Medium project:")
print("    project/")
print("    ├── main.py")
print("    ├── models.py")
print("    ├── views.py")
print("    ├── utils.py")
print("    ├── config.py")
print("    └── tests/")
print("        ├── test_models.py")
print("        └── test_utils.py")
print()

# --- Large project ---
print("  Large project:")
print("    project/")
print("    ├── main.py")
print("    ├── core/")
print("    │   ├── models.py")
print("    │   └── services.py")
print("    ├── api/")
print("    │   ├── routes.py")
print("    │   └── handlers.py")
print("    ├── utils/")
print("    │   ├── validators.py")
print("    │   └── formatters.py")
print("    ├── config/")
print("    │   ├── settings.py")
print("    │   └── constants.py")
print("    └── tests/")
print()

# =============================
# 6. THE SINGLE RESPONSIBILITY PRINCIPLE
# =============================

print("=== Single Responsibility ===")
print()

print("  Each module should do ONE thing well:")
print()
print("    ✅ validators.py  → only validation")
print("    ✅ formatters.py  → only formatting")
print("    ✅ models.py      → only data classes")
print("    ✅ database.py    → only database access")
print()
print("    ❌ helpers.py     → validation + formatting + database")
print("       (too many responsibilities!)")
print()

# Cleanup
sys.path.remove(base_dir)
shutil.rmtree(base_dir)

# ============================================
# TRY IT YOURSELF:
# 1. Take a large script and split it into 3+ modules
# 2. Create a constants.py for your project settings
# 3. Organize a project with models/, utils/, and main.py
# ============================================
