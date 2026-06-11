# ============================================
# MODULE 13 - SUBTOPIC 7: Metaclasses (Introduction)
# ============================================

# A metaclass is the "class of a class."
# In Python, classes are objects too — created by the metaclass 'type'.

# =============================
# 1. CLASSES ARE OBJECTS
# =============================

# --- Example 1: type() reveals the class of anything ---
print("=== Classes Are Objects ===")
print()

class Dog:
    pass

# Regular objects have types
print(f"  type(42) = {type(42)}")            # int
print(f"  type('hello') = {type('hello')}")  # str
print(f"  type([1,2]) = {type([1,2])}")      # list

# Classes ALSO have a type
print(f"  type(Dog) = {type(Dog)}")          # type!
print(f"  type(int) = {type(int)}")          # type!
print(f"  type(str) = {type(str)}")          # type!
print()
print("  → 'type' is the metaclass — the class that creates classes")
print()

# =============================
# 2. CREATING CLASSES WITH type()
# =============================

# --- Example 2: type() as a class factory ---
print("=== Creating Classes with type() ===")
print()

# Normal class definition:
class NormalDog:
    species = "Canis familiaris"

    def bark(self):
        return "Woof!"

# Same thing using type():
def bark(self):
    return "Woof!"

DynamicDog = type("DynamicDog", (), {
    "species": "Canis familiaris",
    "bark": bark,
})

# They work the same!
d1 = NormalDog()
d2 = DynamicDog()

print(f"  NormalDog:  species='{d1.species}', bark='{d1.bark()}'")
print(f"  DynamicDog: species='{d2.species}', bark='{d2.bark()}'")
print(f"  type(NormalDog)  = {type(NormalDog)}")
print(f"  type(DynamicDog) = {type(DynamicDog)}")
print()

# =============================
# 3. type() WITH INHERITANCE
# =============================

# --- Example 3: Dynamic class with parent ---
print("=== Dynamic Class with Inheritance ===")
print()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Create Cat dynamically, inheriting from Animal
def cat_speak(self):
    return f"{self.name} says Meow!"

Cat = type("Cat", (Animal,), {
    "speak": cat_speak,
})

kitty = Cat("Whiskers")
print(f"  {kitty.speak()}")
print(f"  isinstance(kitty, Animal)? {isinstance(kitty, Animal)}")
print()

# =============================
# 4. CUSTOM METACLASS (BASIC)
# =============================

# --- Example 4: A metaclass that prints when a class is created ---
print("=== Custom Metaclass ===")
print()

class VerboseMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"  [META] Creating class '{name}'")
        print(f"         Bases: {[b.__name__ for b in bases]}")
        print(f"         Methods: {[k for k in namespace if not k.startswith('_')]}")
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

class MyService(metaclass=VerboseMeta):
    def start(self):
        return "started"

    def stop(self):
        return "stopped"

print()
service = MyService()
print(f"  service.start() = '{service.start()}'")
print()

# =============================
# 5. METACLASS THAT ENFORCES RULES
# =============================

# --- Example 5: Require all methods to have docstrings ---
print("=== Enforcing Rules ===")
print()

class DocstringMeta(type):
    def __new__(mcs, name, bases, namespace):
        for key, value in namespace.items():
            if callable(value) and not key.startswith("_"):
                if not getattr(value, "__doc__", None):
                    raise TypeError(
                        f"Method '{key}' in class '{name}' must have a docstring"
                    )
        return super().__new__(mcs, name, bases, namespace)

# This class is fine — all methods have docstrings
class GoodService(metaclass=DocstringMeta):
    def process(self):
        """Process the data."""
        return "processed"

    def validate(self):
        """Validate the input."""
        return "valid"

print(f"  GoodService created successfully")
print(f"  process: '{GoodService().process()}'")

# This would fail — missing docstring
try:
    class BadService(metaclass=DocstringMeta):
        def process(self):
            return "no docstring!"
except TypeError as e:
    print(f"  BadService failed: {e}")
print()

# =============================
# 6. AUTO-REGISTRATION METACLASS
# =============================

# --- Example 6: Automatically register all subclasses ---
print("=== Auto-Registration ===")
print()

class RegistryMeta(type):
    registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:    # don't register the base class itself
            RegistryMeta.registry[name] = cls
        return cls

class Plugin(metaclass=RegistryMeta):
    """Base class for plugins."""
    def run(self):
        return f"{type(self).__name__} running"

class ImagePlugin(Plugin):
    pass

class VideoPlugin(Plugin):
    pass

class AudioPlugin(Plugin):
    pass

print(f"  Registered plugins: {list(RegistryMeta.registry.keys())}")
print()

# Create plugins from registry
for name, cls in RegistryMeta.registry.items():
    plugin = cls()
    print(f"    {plugin.run()}")
print()

# =============================
# 7. WHEN (NOT) TO USE METACLASSES
# =============================

print("=== When to Use Metaclasses ===")
print()
print("  ✓ Framework internals (Django models, etc.)")
print("  ✓ Auto-registering subclasses")
print("  ✓ Enforcing class-level rules")
print()
print("  ✗ Simple validation (use __init_subclass__ instead)")
print("  ✗ Instance-level behavior (use __init__)")
print("  ✗ When decorators or inheritance will do")
print()
print("  Rule: If you're not sure you need it, you don't.")

# ============================================
# TRY IT YOURSELF:
# 1. Use type() to create a class dynamically
# 2. Create a metaclass that adds a 'created_at' attribute
# 3. Create a metaclass that prevents class names under 3 chars
# ============================================
