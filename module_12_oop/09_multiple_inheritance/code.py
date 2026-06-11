# ============================================
# MODULE 12 - SUBTOPIC 9: Multiple Inheritance & MRO
# ============================================

# Multiple inheritance = a class inherits from MORE THAN ONE parent.
# MRO = the order Python searches for methods.

# =============================
# 1. BASIC MULTIPLE INHERITANCE
# =============================

# --- Example 1: Combining two abilities ---
print("=== Basic Multiple Inheritance ===")
print()

class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

# Duck inherits from BOTH
class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"

duck = Duck()
print(f"  {duck.fly()}")       # from Flyable
print(f"  {duck.swim()}")      # from Swimmable
print(f"  {duck.quack()}")     # its own
print()

# =============================
# 2. COMBINING BEHAVIORS (MIXINS)
# =============================

# --- Example 2: Mixin pattern ---
print("=== Mixin Pattern ===")
print()

# Mixins are small classes that add a single behavior

class JsonMixin:
    def to_json_string(self):
        import json
        return json.dumps(self.__dict__)

class PrintableMixin:
    def print_info(self):
        for key, value in self.__dict__.items():
            print(f"    {key}: {value}")

class User(JsonMixin, PrintableMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Trush", "trush@example.com")
print("  User info:")
user.print_info()     # from PrintableMixin
print(f"  JSON: {user.to_json_string()}")  # from JsonMixin
print()

# =============================
# 3. METHOD RESOLUTION ORDER (MRO)
# =============================

# --- Example 3: When parents have the same method ---
print("=== MRO: Same Method in Parents ===")
print()

class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A, B):   # A comes first
    pass

class D(B, A):   # B comes first
    pass

c = C()
d = D()

print(f"  C(A, B).greet() → '{c.greet()}'")   # "Hello from A"
print(f"  D(B, A).greet() → '{d.greet()}'")   # "Hello from B"
print("  → The first parent listed wins!")
print()

# =============================
# 4. CHECKING MRO
# =============================

# --- Example 4: Using __mro__ ---
print("=== Checking MRO ===")
print()

print("  C's MRO:")
for cls in C.__mro__:
    print(f"    {cls.__name__}")

print()

print("  D's MRO:")
for cls in D.__mro__:
    print(f"    {cls.__name__}")
print()

# =============================
# 5. CHILD OVERRIDES ALL
# =============================

# --- Example 5: Child's method takes priority ---
print("=== Child Override ===")
print()

class Parent1:
    def greet(self):
        return "Hello from Parent1"

class Parent2:
    def greet(self):
        return "Hello from Parent2"

class Child(Parent1, Parent2):
    def greet(self):
        return "Hello from Child!"   # child wins!

child = Child()
print(f"  child.greet() → '{child.greet()}'")
print()

# =============================
# 6. super() WITH MULTIPLE INHERITANCE
# =============================

# --- Example 6: super() follows MRO ---
print("=== super() with Multiple Inheritance ===")
print()

class Base:
    def __init__(self):
        self.base_attr = "from Base"
        print("    Base.__init__ called")

class Left(Base):
    def __init__(self):
        super().__init__()
        self.left_attr = "from Left"
        print("    Left.__init__ called")

class Right(Base):
    def __init__(self):
        super().__init__()
        self.right_attr = "from Right"
        print("    Right.__init__ called")

class Child2(Left, Right):
    def __init__(self):
        super().__init__()
        self.child_attr = "from Child"
        print("    Child.__init__ called")

print("  Creating Child2:")
obj = Child2()
print()

print("  MRO for Child2:")
for cls in Child2.__mro__:
    print(f"    {cls.__name__}")
print()

# =============================
# 7. PRACTICAL: CHARACTER ABILITIES
# =============================

# --- Example 7: Game character with multiple abilities ---
print("=== Game Character Abilities ===")
print()

class Healer:
    def heal(self, target):
        return f"{self.name} heals {target} for 20 HP"

class Fighter:
    def attack(self, target):
        return f"{self.name} attacks {target} for 15 damage"

class Mage:
    def cast_spell(self, spell, target):
        return f"{self.name} casts {spell} on {target}"

# Paladin can fight AND heal
class Paladin(Fighter, Healer):
    def __init__(self, name):
        self.name = name

# BattleMage can fight AND cast spells
class BattleMage(Fighter, Mage):
    def __init__(self, name):
        self.name = name

paladin = Paladin("Arthur")
mage = BattleMage("Gandalf")

print(f"  {paladin.attack('Dragon')}")
print(f"  {paladin.heal('Trush')}")
print()
print(f"  {mage.attack('Goblin')}")
print(f"  {mage.cast_spell('Fireball', 'Goblin')}")

# ============================================
# TRY IT YOURSELF:
# 1. Create 3 mixin classes: Printable, Saveable, Comparable
# 2. Create a Product class that uses all three
# 3. Check the MRO using Product.__mro__
# ============================================
