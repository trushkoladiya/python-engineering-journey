# ============================================
# MODULE 13 - SUBTOPIC 17: Debugging & Best Practices
# ============================================

# Knowing when NOT to use advanced OOP is critical.
# Simple > Clever. Readability > Cleverness.

# =============================
# 1. OVERENGINEERING vs SIMPLICITY
# =============================

# --- Example 1: Too complex for the job ---
print("=== Overengineering vs Simplicity ===")
print()

# BAD: Overengineered — metaclass for something simple
print("  Overengineered approach:")
print("    Using metaclass to auto-register classes")
print("    Using abstract base class for one implementation")
print("    Using __slots__ for a class with 3 instances")
print()

# GOOD: Simple and clear
class SimpleUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"

user = SimpleUser("Trush", "trush@example.com")
print(f"  Simple approach: {user}")
print("  → Clear, readable, works perfectly!")
print()

# =============================
# 2. INHERITANCE DEPTH
# =============================

# --- Example 2: Too deep vs just right ---
print("=== Inheritance Depth ===")
print()

# BAD: 5 levels deep
class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D(C):
    pass
class E(D):
    pass

print(f"  Bad: E has {len(E.__mro__) - 1} levels of inheritance")
print("  → Hard to understand, hard to debug")
print()

# GOOD: Shallow + composition
class Logger:
    def log(self, msg):
        print(f"    [LOG] {msg}")

class Validator:
    def validate(self, data):
        return len(data) > 0

class UserService:
    def __init__(self):
        self.logger = Logger()         # composition
        self.validator = Validator()   # composition

    def create_user(self, name):
        if self.validator.validate(name):
            self.logger.log(f"Created user: {name}")
            return {"name": name}
        self.logger.log(f"Invalid name: '{name}'")
        return None

service = UserService()
service.create_user("Trush")
service.create_user("")
print()

# =============================
# 3. GOD CLASS ANTI-PATTERN
# =============================

# --- Example 3: One class doing too much ---
print("=== God Class Anti-Pattern ===")
print()

# BAD: Does EVERYTHING
class GodClass:
    """Does user management, email, validation, reporting..."""
    def create_user(self, name): pass
    def delete_user(self, name): pass
    def send_email(self, to, msg): pass
    def validate_email(self, email): pass
    def generate_report(self): pass
    def export_csv(self): pass
    def connect_db(self): pass
    def run_query(self, sql): pass

print("  Bad: GodClass has 8 unrelated methods!")
print("  Fix: Split into UserService, EmailService, ReportService, Database")
print()

# GOOD: Focused classes
class UserManager:
    def create(self, name):
        return f"Created {name}"

    def delete(self, name):
        return f"Deleted {name}"

class EmailService:
    def send(self, to, message):
        return f"Email to {to}: {message}"

print(f"  {UserManager().create('Trush')}")
print(f"  {EmailService().send('trush@test.com', 'Welcome!')}")
print()

# =============================
# 4. OPERATOR OVERLOADING MISUSE
# =============================

# --- Example 4: When operators don't make sense ---
print("=== Operator Overloading: Good vs Bad ===")
print()

# GOOD: + makes sense for vectors
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v = Vector(1, 2) + Vector(3, 4)
print(f"  Good: Vector(1,2) + Vector(3,4) = {v}")

# BAD: + doesn't make sense for users
class User:
    def __init__(self, name):
        self.name = name

    # What does "adding" two users mean?? Confusing!
    # def __add__(self, other): ???

print("  Bad: User('Trush') + User('Rahul') = ???")
print("  → Only overload operators when the meaning is obvious")
print()

# =============================
# 5. YAGNI — YOU AREN'T GONNA NEED IT
# =============================

# --- Example 5: Don't add features "just in case" ---
print("=== YAGNI Principle ===")
print()

# BAD: Built for every possible future scenario
class OverDesignedConfig:
    """Has caching, encryption, versioning, hooks...
    but you only need key-value storage right now."""
    pass

# GOOD: Build what you need now
class SimpleConfig:
    def __init__(self):
        self._data = {}

    def set(self, key, value):
        self._data[key] = value

    def get(self, key, default=None):
        return self._data.get(key, default)

config = SimpleConfig()
config.set("debug", True)
print(f"  Simple config: debug={config.get('debug')}")
print("  → Add features WHEN you need them, not before")
print()

# =============================
# 6. DEBUGGING CHECKLIST
# =============================

# --- Example 6: Common mistakes and fixes ---
print("=== Common Mistakes ===")
print()

# Mistake 1: Forgetting super().__init__()
class Parent:
    def __init__(self):
        self.parent_attr = "from parent"

class BadChild(Parent):
    def __init__(self):
        # Missing super().__init__()!
        self.child_attr = "from child"

class GoodChild(Parent):
    def __init__(self):
        super().__init__()           # ← Always call super()!
        self.child_attr = "from child"

bad = BadChild()
good = GoodChild()

print(f"  BadChild has parent_attr? {hasattr(bad, 'parent_attr')}")
print(f"  GoodChild has parent_attr? {hasattr(good, 'parent_attr')}")
print()

# Mistake 2: Mutable default class attribute
class BadList:
    items = []    # shared by ALL instances!

    def add(self, item):
        self.items.append(item)

class GoodList:
    def __init__(self):
        self.items = []    # each instance gets its own

    def add(self, item):
        self.items.append(item)

b1 = BadList()
b2 = BadList()
b1.add("hello")
print(f"  Bad: b2.items = {b2.items}  (shared!)")

g1 = GoodList()
g2 = GoodList()
g1.add("hello")
print(f"  Good: g2.items = {g2.items}  (separate)")
print()

# =============================
# 7. DECISION GUIDE
# =============================

print("=" * 50)
print("  ADVANCED OOP DECISION GUIDE")
print("=" * 50)
print()
print("  Before using an advanced feature, ask:")
print()
print("  1. Does a SIMPLER solution exist?")
print("     → If yes, use the simpler one")
print()
print("  2. Would a junior dev understand this?")
print("     → If no, simplify or add comments")
print()
print("  3. Am I solving a REAL problem or a HYPOTHETICAL one?")
print("     → Only solve real problems (YAGNI)")
print()
print("  4. Is this making the code MORE or LESS maintainable?")
print("     → Always choose maintainability")
print()
print("  5. Can I test this easily?")
print("     → If it's hard to test, redesign it")

# ============================================
# MODULE 13 COMPLETE!
#
# You've learned:
#   1. Object lifecycle (__new__, __init__, __del__)
#   2. All comparison operators
#   3. Full arithmetic overloading
#   4. Attribute access hooks
#   5. Properties (@property)
#   6. MRO deep dive
#   7. Metaclasses (intro)
#   8. Abstract Base Classes (deep)
#   9. Duck typing & EAFP
#  10. Composition vs Inheritance
#  11. Design Patterns (Singleton, Factory, Strategy)
#  12. Class internals (__dict__, __slots__)
#  13. Callable objects (__call__)
#  14. Context managers (__enter__, __exit__)
#  15. Advanced decorators
#  16. Fluent interfaces & immutable objects
#  17. Debugging & best practices
#
# Remember: SIMPLE > CLEVER. Always.
# ============================================
