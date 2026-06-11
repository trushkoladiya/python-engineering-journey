# ============================================
# MODULE 13 - SUBTOPIC 6: MRO Deep Dive
# ============================================

# MRO = the order Python searches for methods.
# Uses C3 linearization to handle complex inheritance.

# =============================
# 1. SIMPLE MRO
# =============================

# --- Example 1: Linear inheritance ---
print("=== Simple MRO ===")
print()

class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(B):
    def who(self):
        return "C"

obj = C()
print(f"  C().who() = '{obj.who()}'")
print(f"  MRO: {' → '.join(cls.__name__ for cls in C.__mro__)}")
print()

# =============================
# 2. THE DIAMOND PROBLEM
# =============================

# --- Example 2: Diamond inheritance ---
print("=== Diamond Problem ===")
print()

#       A
#      / \
#     B   C
#      \ /
#       D

class Base:
    def who(self):
        return "Base"

class Left(Base):
    def who(self):
        return "Left"

class Right(Base):
    def who(self):
        return "Right"

class Child(Left, Right):
    pass

obj = Child()
print(f"  Child().who() = '{obj.who()}'")
print(f"  MRO: {' → '.join(cls.__name__ for cls in Child.__mro__)}")
print("  → Left is checked before Right (listed first)")
print()

# =============================
# 3. super() FOLLOWS MRO
# =============================

# --- Example 3: super() calls next in MRO, not parent ---
print("=== super() Follows MRO ===")
print()

class A2:
    def method(self):
        print("    A2.method()")

class B2(A2):
    def method(self):
        print("    B2.method()")
        super().method()        # next in MRO

class C2(A2):
    def method(self):
        print("    C2.method()")
        super().method()        # next in MRO

class D2(B2, C2):
    def method(self):
        print("    D2.method()")
        super().method()        # next in MRO

print(f"  MRO: {' → '.join(cls.__name__ for cls in D2.__mro__)}")
print("  Calling D2().method():")
D2().method()
print("  → Each class is visited exactly once!")
print()

# =============================
# 4. COOPERATIVE super().__init__
# =============================

# --- Example 4: init chain with super() ---
print("=== Cooperative __init__ ===")
print()

class Animal:
    def __init__(self, species):
        self.species = species
        print(f"    Animal.__init__(species='{species}')")

class Flyable:
    def __init__(self, can_fly=True):
        self.can_fly = can_fly
        print(f"    Flyable.__init__(can_fly={can_fly})")

# Proper cooperative init with **kwargs
class CoopAnimal:
    def __init__(self, species="unknown", **kwargs):
        super().__init__(**kwargs)
        self.species = species
        print(f"    CoopAnimal.__init__(species='{species}')")

class CoopFlyable:
    def __init__(self, can_fly=True, **kwargs):
        super().__init__(**kwargs)
        self.can_fly = can_fly
        print(f"    CoopFlyable.__init__(can_fly={can_fly})")

class Bird(CoopAnimal, CoopFlyable):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        print(f"    Bird.__init__(name='{name}')")

print(f"  MRO: {' → '.join(cls.__name__ for cls in Bird.__mro__)}")
print("  Creating Bird:")
bird = Bird("Eagle", species="bird", can_fly=True)
print(f"  Result: {bird.name}, {bird.species}, can_fly={bird.can_fly}")
print()

# =============================
# 5. COMPLEX HIERARCHY
# =============================

# --- Example 5: Deeper diamond ---
print("=== Complex Hierarchy ===")
print()

#       Base
#      / | \
#     A  B  C
#     |\ | /|
#     | D E |
#      \ | /
#       F

class Base3:
    pass

class A3(Base3):
    pass

class B3(Base3):
    pass

class C3(Base3):
    pass

class D3(A3, B3):
    pass

class E3(B3, C3):
    pass

class F3(D3, E3):
    pass

print("  F3's MRO:")
for i, cls in enumerate(F3.__mro__):
    print(f"    {i}. {cls.__name__}")
print()

# =============================
# 6. MRO WITH METHODS
# =============================

# --- Example 6: Which method gets called? ---
print("=== MRO Method Resolution ===")
print()

class Logger:
    def log(self, msg):
        return f"[Logger] {msg}"

class FileLogger(Logger):
    def log(self, msg):
        return f"[FileLogger] {msg}"

class NetworkLogger(Logger):
    def log(self, msg):
        return f"[NetworkLogger] {msg}"

class HybridLogger(FileLogger, NetworkLogger):
    pass    # no override — which log() is used?

h = HybridLogger()
print(f"  HybridLogger.log(): '{h.log('test')}'")
print(f"  MRO: {' → '.join(cls.__name__ for cls in HybridLogger.__mro__)}")
print("  → FileLogger.log() wins because it's listed first")
print()

# =============================
# 7. PRACTICAL: USING MRO TO DEBUG
# =============================

# --- Example 7: Finding where a method comes from ---
print("=== Debugging with MRO ===")
print()

class Widget:
    def render(self):
        return "Widget.render"

class Clickable:
    def on_click(self):
        return "Clickable.on_click"

class Draggable:
    def on_drag(self):
        return "Draggable.on_drag"

class Button(Clickable, Widget):
    def render(self):
        return "Button.render"

class DragButton(Draggable, Button):
    pass

db = DragButton()
print(f"  DragButton.render() = '{db.render()}'")
print(f"  DragButton.on_click() = '{db.on_click()}'")
print(f"  DragButton.on_drag() = '{db.on_drag()}'")
print()

print("  Where does each method come from?")
for method_name in ["render", "on_click", "on_drag"]:
    for cls in DragButton.__mro__:
        if method_name in cls.__dict__:
            print(f"    {method_name}() → {cls.__name__}")
            break

# ============================================
# TRY IT YOURSELF:
# 1. Create a diamond hierarchy and trace super() calls
# 2. Use __mro__ to verify which method gets called
# 3. Try rearranging parent order and see how MRO changes
# ============================================
