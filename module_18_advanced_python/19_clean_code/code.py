# ============================================
# MODULE 18 - SUBTOPIC 19: Clean Code & Architecture
# ============================================

# Writing code that humans can understand and maintain.

# =============================
# 1. MEANINGFUL NAMES
# =============================

print("=== Meaningful Names ===")
print()

# BAD names
x = 86400
d = []
def f(l):
    return [i for i in l if i > 0]

# GOOD names
SECONDS_PER_DAY = 86400
active_users = []
def get_positive_numbers(numbers):
    return [n for n in numbers if n > 0]

print("  Bad:  x = 86400")
print("  Good: SECONDS_PER_DAY = 86400")
print()
print("  Bad:  def f(l): ...")
print("  Good: def get_positive_numbers(numbers): ...")
print()

# Name Guidelines:
# - Variables: lowercase_with_underscores (user_name, total_count)
# - Constants: UPPERCASE_WITH_UNDERSCORES (MAX_RETRIES, API_URL)
# - Functions: verb_noun (get_user, calculate_total, validate_input)
# - Classes: PascalCase (UserAccount, DataProcessor)
# - Boolean: is_/has_/can_ prefix (is_active, has_permission)

# =============================
# 2. SINGLE RESPONSIBILITY
# =============================

print("=== Single Responsibility ===")
print()

# BAD: one function does everything
def process_order_bad(order_data):
    # Validate
    if not order_data.get("items"):
        return "No items"
    # Calculate
    total = sum(item["price"] * item["qty"] for item in order_data["items"])
    # Apply discount
    if total > 100:
        total *= 0.9
    # Format
    return f"Order total: ${total:.2f}"

# GOOD: each function does ONE thing
def validate_order(order_data):
    """Check if order data is valid."""
    if not order_data.get("items"):
        raise ValueError("Order must have items")
    for item in order_data["items"]:
        if item["price"] <= 0 or item["qty"] <= 0:
            raise ValueError(f"Invalid item: {item}")

def calculate_total(items):
    """Calculate the sum of all item prices."""
    return sum(item["price"] * item["qty"] for item in items)

def apply_discount(total, threshold=100, discount=0.1):
    """Apply discount if total exceeds threshold."""
    if total > threshold:
        return total * (1 - discount)
    return total

def format_total(total):
    """Format total as a currency string."""
    return f"${total:.2f}"

# Usage
order = {"items": [{"price": 50, "qty": 2}, {"price": 30, "qty": 1}]}

validate_order(order)
total = calculate_total(order["items"])
total = apply_discount(total)
result = format_total(total)

print(f"  Order: {order['items']}")
print(f"  Total: {result}")
print(f"  Each function does exactly ONE thing")
print()

# =============================
# 3. AVOID DEEP NESTING
# =============================

print("=== Avoid Deep Nesting ===")
print()

# BAD: deeply nested
def process_user_bad(user):
    if user:
        if user.get("active"):
            if user.get("age", 0) >= 18:
                if user.get("verified"):
                    return f"Processing {user['name']}"
    return "Cannot process"

# GOOD: early returns (guard clauses)
def process_user_good(user):
    if not user:
        return "Cannot process: no user"
    if not user.get("active"):
        return "Cannot process: inactive"
    if user.get("age", 0) < 18:
        return "Cannot process: underage"
    if not user.get("verified"):
        return "Cannot process: unverified"
    return f"Processing {user['name']}"

user = {"name": "Trush", "active": True, "age": 21, "verified": True}
print(f"  Bad:  {process_user_bad(user)}")
print(f"  Good: {process_user_good(user)}")
print()

# =============================
# 4. DRY — DON'T REPEAT YOURSELF
# =============================

print("=== DRY Principle ===")
print()

# BAD: duplicated logic
def get_admin_greeting():
    name = "Admin"
    hour = 14
    if hour < 12:
        return f"Good morning, {name}!"
    elif hour < 18:
        return f"Good afternoon, {name}!"
    return f"Good evening, {name}!"

def get_user_greeting():
    name = "Rahul"
    hour = 14
    if hour < 12:
        return f"Good morning, {name}!"
    elif hour < 18:
        return f"Good afternoon, {name}!"
    return f"Good evening, {name}!"

# GOOD: extract common logic
def get_greeting(name, hour):
    """Generate a time-appropriate greeting."""
    if hour < 12:
        period = "morning"
    elif hour < 18:
        period = "afternoon"
    else:
        period = "evening"
    return f"Good {period}, {name}!"

print(f"  {get_greeting('Admin', 9)}")
print(f"  {get_greeting('Rahul', 14)}")
print(f"  {get_greeting('Guest', 20)}")
print()

# =============================
# 5. CLEAN FUNCTION DESIGN
# =============================

print("=== Clean Function Design ===")
print()

# Rule 1: Few parameters (ideally 0-3)
# BAD
def create_user_bad(name, age, email, city, country, phone, role, active):
    pass

# GOOD — use a data class or dict
class UserConfig:
    def __init__(self, name, age, email, **kwargs):
        self.name = name
        self.age = age
        self.email = email
        self.city = kwargs.get("city", "Unknown")
        self.role = kwargs.get("role", "user")
        self.active = kwargs.get("active", True)

    def __repr__(self):
        return f"UserConfig({self.name}, {self.email})"

config = UserConfig("Trush", 21, "trushkoladiya.work@gmail.com", city="NYC")
print(f"  Clean config: {config}")
print()

# Rule 2: No side effects (when possible)
# BAD — modifies external state silently
global_list = []
def add_item_bad(item):
    global_list.append(item)  # Hidden side effect!

# GOOD — explicit input and output
def add_item_good(items, new_item):
    return items + [new_item]  # Returns new list, no side effects

result = add_item_good([1, 2, 3], 4)
print(f"  No side effects: {result}")
print()

# =============================
# 6. DOCSTRINGS AND COMMENTS
# =============================

print("=== Docstrings and Comments ===")
print()

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms (must be positive).
        height_m: Height in meters (must be positive).

    Returns:
        BMI value as a float.

    Raises:
        ValueError: If weight or height is not positive.
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive")
    return weight_kg / (height_m ** 2)

# Good comments explain WHY, not WHAT
# BAD: increment counter by 1
# GOOD: retry because the API occasionally returns 503 errors

bmi = calculate_bmi(70, 1.75)
print(f"  BMI: {bmi:.1f}")
print(f"  Docstring: {calculate_bmi.__doc__[:50]}...")
print()

# =============================
# 7. CONSISTENT ERROR HANDLING
# =============================

print("=== Consistent Error Handling ===")
print()

class AppError(Exception):
    """Base error for our application."""
    pass

class ValidationError(AppError):
    """Raised when input validation fails."""
    pass

class NotFoundError(AppError):
    """Raised when a resource is not found."""
    pass

def find_user(users, user_id):
    """Find a user by ID with proper error handling."""
    if not isinstance(user_id, int):
        raise ValidationError(f"User ID must be int, got {type(user_id).__name__}")
    
    for user in users:
        if user["id"] == user_id:
            return user
    
    raise NotFoundError(f"User with ID {user_id} not found")

users = [
    {"id": 1, "name": "Trush"},
    {"id": 2, "name": "Rahul"},
]

# Clean error handling
test_cases = [1, 3, "invalid"]
for test_id in test_cases:
    try:
        user = find_user(users, test_id)
        print(f"  Found: {user}")
    except ValidationError as e:
        print(f"  Validation error: {e}")
    except NotFoundError as e:
        print(f"  Not found: {e}")
print()

# =============================
# 8. CODE ORGANIZATION PATTERNS
# =============================

print("=== Code Organization ===")
print()

# Pattern 1: Configuration at the top
DEFAULT_CONFIG = {
    "max_retries": 3,
    "timeout": 30,
    "debug": False,
}

# Pattern 2: Related functions grouped together
class DataProcessor:
    """Groups related data processing functions."""

    def __init__(self, data):
        self.data = data
        self._validated = False

    def validate(self):
        """Validate the data."""
        self._validated = all(isinstance(x, (int, float)) for x in self.data)
        return self

    def transform(self):
        """Transform the data (normalize to 0-1)."""
        if not self._validated:
            raise RuntimeError("Must validate before transforming")
        min_val = min(self.data)
        max_val = max(self.data)
        range_val = max_val - min_val
        if range_val == 0:
            self.data = [0] * len(self.data)
        else:
            self.data = [(x - min_val) / range_val for x in self.data]
        return self

    def summarize(self):
        """Return summary statistics."""
        return {
            "count": len(self.data),
            "min": min(self.data),
            "max": max(self.data),
            "mean": sum(self.data) / len(self.data),
        }

# Clean method chaining
processor = DataProcessor([10, 20, 30, 40, 50])
summary = processor.validate().transform().summarize()
print(f"  Processed data: {processor.data}")
print(f"  Summary: {summary}")
print()

# =============================
# 9. PROJECT STRUCTURE
# =============================

print("=== Recommended Project Structure ===")
print()

structure = """
  my_project/
  ├── src/
  │   ├── __init__.py       # Package marker
  │   ├── main.py           # Entry point
  │   ├── config.py         # Configuration
  │   ├── models/           # Data models
  │   │   ├── __init__.py
  │   │   └── user.py
  │   ├── services/         # Business logic
  │   │   ├── __init__.py
  │   │   └── auth.py
  │   └── utils/            # Helper functions
  │       ├── __init__.py
  │       └── validators.py
  ├── tests/                # Test files
  │   ├── test_models.py
  │   └── test_services.py
  ├── requirements.txt      # Dependencies
  ├── README.md             # Documentation
  └── .gitignore            # Git ignore rules
"""

print(structure)

# =============================
# 10. CLEAN CODE CHECKLIST
# =============================

print("=== Clean Code Checklist ===")
print()

checklist = [
    "Use meaningful, descriptive names",
    "Functions do ONE thing only",
    "Keep functions short (< 20 lines ideally)",
    "Avoid deep nesting (use guard clauses)",
    "Don't Repeat Yourself (DRY)",
    "Write docstrings for public functions",
    "Handle errors consistently",
    "Use constants instead of magic numbers",
    "Group related code together",
    "Follow consistent formatting",
]

for i, item in enumerate(checklist, 1):
    print(f"  {i:2d}. {item}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Refactor a messy function into smaller,
#    clean functions with good names
# 2. Add proper docstrings to 5 of your functions
# 3. Restructure a flat script into a proper
#    project layout with modules
# ============================================
