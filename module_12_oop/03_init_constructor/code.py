# ============================================
# MODULE 12 - SUBTOPIC 3: The __init__ Constructor
# ============================================

# __init__ is a special method that runs AUTOMATICALLY
# when you create an object. It initializes the object's data.

# =============================
# 1. WITHOUT __init__ (THE OLD WAY)
# =============================

# --- Example 1: Manually adding attributes (messy) ---
print("=== Without __init__ (Messy) ===")
print()

class DogOld:
    pass

dog = DogOld()
dog.name = "Buddy"
dog.age = 3

print(f"  {dog.name}, age {dog.age}")
print("  Problem: you must remember to add every attribute manually!")
print()

# =============================
# 2. WITH __init__ (THE RIGHT WAY)
# =============================

# --- Example 2: Using __init__ ---
print("=== With __init__ (Clean) ===")
print()

class Dog:
    def __init__(self, name, age):
        self.name = name    # save name on THIS object
        self.age = age      # save age on THIS object

# __init__ runs automatically when you call Dog(...)
buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

print(f"  {buddy.name}, age {buddy.age}")
print(f"  {max_dog.name}, age {max_dog.age}")
print()

# =============================
# 3. UNDERSTANDING 'self'
# =============================

# --- Example 3: self explained ---
print("=== Understanding 'self' ===")
print()

class Cat:
    def __init__(self, name, color):
        # 'self' = the specific cat being created
        self.name = name      # self.name belongs to THIS cat
        self.color = color    # self.color belongs to THIS cat
        print(f"    A {color} cat named '{name}' was created!")

# When you call Cat("Whiskers", "orange"):
#   Python creates a new Cat object
#   Python calls __init__(new_object, "Whiskers", "orange")
#   'self' becomes that new_object
cat1 = Cat("Whiskers", "orange")
cat2 = Cat("Shadow", "black")
print()

print(f"  cat1.name = '{cat1.name}', cat1.color = '{cat1.color}'")
print(f"  cat2.name = '{cat2.name}', cat2.color = '{cat2.color}'")
print()

# =============================
# 4. DEFAULT VALUES
# =============================

# --- Example 4: Parameters with defaults ---
print("=== Default Values ===")
print()

class Student:
    def __init__(self, name, grade="N/A", active=True):
        self.name = name
        self.grade = grade
        self.active = active

s1 = Student("Trush", "A")          # active defaults to True
s2 = Student("Rahul")                 # grade defaults to "N/A", active to True
s3 = Student("Charlie", "B", False) # all specified

print(f"  {s1.name}: grade={s1.grade}, active={s1.active}")
print(f"  {s2.name}: grade={s2.grade}, active={s2.active}")
print(f"  {s3.name}: grade={s3.grade}, active={s3.active}")
print()

# =============================
# 5. COMPUTED ATTRIBUTES
# =============================

# --- Example 5: Setting extra attributes in __init__ ---
print("=== Computed Attributes ===")
print()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height           # computed from inputs
        self.perimeter = 2 * (width + height) # computed from inputs

r1 = Rectangle(5, 3)
r2 = Rectangle(10, 7)

print(f"  Rectangle 1: {r1.width}x{r1.height}, area={r1.area}, perimeter={r1.perimeter}")
print(f"  Rectangle 2: {r2.width}x{r2.height}, area={r2.area}, perimeter={r2.perimeter}")
print()

# =============================
# 6. VALIDATION IN __init__
# =============================

# --- Example 6: Checking inputs during creation ---
print("=== Validation in __init__ ===")
print()

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        if balance < 0:
            print(f"    Warning: Negative balance not allowed, setting to 0")
            self.balance = 0
        else:
            self.balance = balance

acc1 = BankAccount("Trush", 1000)
acc2 = BankAccount("Rahul", -500)    # validation catches this
acc3 = BankAccount("Charlie")       # defaults to 0

print(f"  {acc1.owner}: ${acc1.balance}")
print(f"  {acc2.owner}: ${acc2.balance}")
print(f"  {acc3.owner}: ${acc3.balance}")
print()

# =============================
# 7. __init__ WITH COLLECTIONS
# =============================

# --- Example 7: Initializing with lists/dicts ---
print("=== __init__ with Collections ===")
print()

class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []       # start with empty list
        self.total = 0.0

cart1 = ShoppingCart("Trush")
cart2 = ShoppingCart("Rahul")

# Each cart has its OWN items list
cart1.items.append("Apple")
cart1.items.append("Bread")

print(f"  {cart1.owner}'s cart: {cart1.items}")
print(f"  {cart2.owner}'s cart: {cart2.items}")
print("  Each object gets its own list!")
print()

# =============================
# 8. PRACTICAL: CREATING MANY OBJECTS
# =============================

# --- Example 8: Creating objects from data ---
print("=== Creating Objects from Data ===")
print()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_value = price * quantity

product_data = [
    ("Laptop", 999.99, 5),
    ("Mouse", 29.99, 50),
    ("Keyboard", 79.99, 30),
    ("Monitor", 449.99, 10),
]

products = []
for name, price, qty in product_data:
    products.append(Product(name, price, qty))

print(f"  {'Product':<12} {'Price':>8} {'Qty':>5} {'Total':>10}")
print(f"  {'-'*37}")
for p in products:
    print(f"  {p.name:<12} ${p.price:>7.2f} {p.quantity:>5} ${p.total_value:>9.2f}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a 'Book' class with __init__(title, author, pages)
# 2. Add a default parameter 'read=False'
# 3. Create 3 Book objects and store them in a list
# 4. Print each book's info
# ============================================
