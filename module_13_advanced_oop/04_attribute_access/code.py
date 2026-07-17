# ============================================
# MODULE 13 - SUBTOPIC 4: Attribute Access Control
# ============================================

# Python lets you intercept attribute access, setting, and deletion
# using __getattr__, __getattribute__, __setattr__, __delattr__

# =============================
# 1. __getattr__ — MISSING ATTRIBUTES
# =============================

# --- Example 1: Handle attributes that don't exist ---
print("=== __getattr__ (Missing Attributes) ===")
print()

class FlexibleConfig:
    def __init__(self):
        self.host = "localhost"
        self.port = 8080

    def __getattr__(self, name):
        # Called ONLY when normal lookup fails
        return f"<default for '{name}'>"

config = FlexibleConfig()
print(f"  config.host = {config.host}")          # normal lookup
print(f"  config.port = {config.port}")          # normal lookup
print(f"  config.debug = {config.debug}")        # __getattr__
print(f"  config.timeout = {config.timeout}")    # __getattr__
print()

# =============================
# 2. __getattr__ — DYNAMIC DEFAULTS
# =============================

# --- Example 2: Default values for missing attributes ---
print("=== Dynamic Defaults ===")
print()

class Settings:
    DEFAULTS = {
        "theme": "dark",
        "font_size": 14,
        "language": "en",
        "autosave": True,
    }

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getattr__(self, name):
        if name in Settings.DEFAULTS:
            return Settings.DEFAULTS[name]
        raise AttributeError(f"No setting named '{name}'")

s = Settings(theme="light")
print(f"  theme: {s.theme}")             # set explicitly → "light"
print(f"  font_size: {s.font_size}")     # from DEFAULTS → 14
print(f"  language: {s.language}")        # from DEFAULTS → "en"

try:
    print(s.nonexistent)
except AttributeError as e:
    print(f"  nonexistent: {e}")
print()

# =============================
# 3. __setattr__ — VALIDATE ON SET
# =============================

# --- Example 3: Validation when setting attributes ---
print("=== __setattr__ (Validation) ===")
print()

class Person:
    def __init__(self, name, age):
        self.name = name    # triggers __setattr__
        self.age = age      # triggers __setattr__

    def __setattr__(self, name, value):
        if name == "age":
            if not isinstance(value, int):
                raise TypeError(f"Age must be int, got {type(value).__name__}")
            if value < 0 or value > 150:
                raise ValueError(f"Age must be 0-150, got {value}")
        if name == "name":
            if not isinstance(value, str) or len(value.strip()) == 0:
                raise ValueError("Name must be a non-empty string")
        # MUST call super to actually set the attribute
        super().__setattr__(name, value)

p = Person("Trush", 21)
print(f"  Created: {p.name}, age {p.age}")

p.age = 30
print(f"  Changed age: {p.age}")

try:
    p.age = -5
except ValueError as e:
    print(f"  Invalid age: {e}")

try:
    p.age = "twenty"
except TypeError as e:
    print(f"  Wrong type: {e}")

print(f"  Age unchanged: {p.age}")
print()

# =============================
# 4. __delattr__ — PROTECT ATTRIBUTES
# =============================

# --- Example 4: Prevent deletion of critical attributes ---
print("=== __delattr__ (Protection) ===")
print()

class User:
    PROTECTED = {"user_id", "username"}

    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def __delattr__(self, name):
        if name in User.PROTECTED:
            raise AttributeError(f"Cannot delete protected attribute '{name}'")
        super().__delattr__(name)

    def __str__(self):
        attrs = vars(self)
        parts = [f"{k}={v}" for k, v in attrs.items()]
        return f"User({', '.join(parts)})"

user = User(1, "trush", "trush@example.com")
print(f"  Before: {user}")

# Deleting email is allowed
del user.email
print(f"  After del email: {user}")

# Deleting protected attributes is blocked
try:
    del user.username
except AttributeError as e:
    print(f"  del username: {e}")

try:
    del user.user_id
except AttributeError as e:
    print(f"  del user_id: {e}")
print()

# =============================
# 5. __getattribute__ — INTERCEPT ALL
# =============================

# --- Example 5: Logging every attribute access ---
print("=== __getattribute__ (Logging) ===")
print()

class LoggedAccess:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __getattribute__(self, attr_name):
        # Called for EVERY attribute access
        if attr_name not in ("__class__", "__dict__"):
            print(f"    [LOG] Accessing '{attr_name}'")
        # MUST call super() to actually get the value!
        return super().__getattribute__(attr_name)

obj = LoggedAccess("test", 42)
print(f"  name: {obj.name}")
print(f"  value: {obj.value}")
print()

# =============================
# 6. __setattr__ — TRACKING CHANGES
# =============================

# --- Example 6: Recording attribute history ---
print("=== Change Tracking ===")
print()

class TrackedObject:
    def __init__(self, **kwargs):
        super().__setattr__("_history", [])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
            return
        old = getattr(self, name, "<not set>")
        self._history.append(f"{name}: {old} → {value}")
        super().__setattr__(name, value)

    def show_history(self):
        print("  Change history:")
        for entry in self._history:
            print(f"    {entry}")

obj = TrackedObject(x=10, y=20)
obj.x = 50
obj.y = 100
obj.x = 75

obj.show_history()
print()

# =============================
# 7. PRACTICAL: READ-ONLY ATTRIBUTES
# =============================

# --- Example 7: Making attributes read-only after init ---
print("=== Read-Only After Init ===")
print()

class Frozen:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            super().__setattr__(key, value)
        super().__setattr__("_frozen", True)

    def __setattr__(self, name, value):
        if getattr(self, "_frozen", False):
            raise AttributeError(f"Cannot modify '{name}': object is frozen")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        if getattr(self, "_frozen", False):
            raise AttributeError(f"Cannot delete '{name}': object is frozen")
        super().__delattr__(name)

    def __str__(self):
        attrs = {k: v for k, v in vars(self).items() if not k.startswith("_")}
        return f"Frozen({attrs})"

frozen = Frozen(name="Trush", role="admin", level=5)
print(f"  {frozen}")
print(f"  name: {frozen.name}")

try:
    frozen.name = "Rahul"
except AttributeError as e:
    print(f"  Modify: {e}")

try:
    del frozen.role
except AttributeError as e:
    print(f"  Delete: {e}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a class that logs every attribute change
# 2. Create a class with type-enforced attributes
# 3. Create a class where missing attributes return None
# ============================================
