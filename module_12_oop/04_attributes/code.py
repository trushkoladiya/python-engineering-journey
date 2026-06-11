# ============================================
# MODULE 12 - SUBTOPIC 4: Attributes
# ============================================

# Two types of attributes:
#   Instance attributes → unique per object (defined in __init__)
#   Class attributes → shared by all objects (defined in class body)

# =============================
# 1. INSTANCE ATTRIBUTES
# =============================

# --- Example 1: Each object has its own data ---
print("=== Instance Attributes ===")
print()

class Dog:
    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age      # instance attribute

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"  dog1: name='{dog1.name}', age={dog1.age}")
print(f"  dog2: name='{dog2.name}', age={dog2.age}")
print()

# Changing one object doesn't affect the other
dog1.age = 4
print(f"  After changing dog1.age to 4:")
print(f"  dog1.age = {dog1.age}")
print(f"  dog2.age = {dog2.age}  (unchanged!)")
print()

# =============================
# 2. CLASS ATTRIBUTES
# =============================

# --- Example 2: Shared data across all objects ---
print("=== Class Attributes ===")
print()

class Cat:
    species = "Felis catus"     # class attribute — shared by ALL cats
    legs = 4                     # class attribute — all cats have 4 legs

    def __init__(self, name, color):
        self.name = name         # instance attribute
        self.color = color       # instance attribute

cat1 = Cat("Whiskers", "orange")
cat2 = Cat("Shadow", "black")

print(f"  cat1: {cat1.name}, {cat1.color}, species='{cat1.species}', legs={cat1.legs}")
print(f"  cat2: {cat2.name}, {cat2.color}, species='{cat2.species}', legs={cat2.legs}")
print(f"  Both share the same species and legs!")
print()

# =============================
# 3. CLASS ATTRIBUTE AS COUNTER
# =============================

# --- Example 3: Counting how many objects are created ---
print("=== Class Attribute as Counter ===")
print()

class Student:
    count = 0    # class attribute — tracks total students

    def __init__(self, name):
        self.name = name
        Student.count += 1    # increment the shared counter

print(f"  Students before: {Student.count}")

s1 = Student("Trush")
print(f"  After creating {s1.name}: count = {Student.count}")

s2 = Student("Rahul")
print(f"  After creating {s2.name}: count = {Student.count}")

s3 = Student("Charlie")
print(f"  After creating {s3.name}: count = {Student.count}")
print()

# All objects see the same count
print(f"  s1 sees count: {s1.count}")
print(f"  s2 sees count: {s2.count}")
print(f"  s3 sees count: {s3.count}")
print()

# =============================
# 4. INSTANCE vs CLASS — THE DIFFERENCE
# =============================

# --- Example 4: Side-by-side comparison ---
print("=== Instance vs Class Attribute ===")
print()

class Car:
    wheels = 4              # class attribute — all cars have 4 wheels

    def __init__(self, brand, color):
        self.brand = brand  # instance attribute — varies per car
        self.color = color  # instance attribute — varies per car

car1 = Car("Toyota", "red")
car2 = Car("Honda", "blue")

print(f"  car1: {car1.brand}, {car1.color}, wheels={car1.wheels}")
print(f"  car2: {car2.brand}, {car2.color}, wheels={car2.wheels}")
print()

# Class attribute accessed via the class itself
print(f"  Car.wheels = {Car.wheels}")
print()

# =============================
# 5. DYNAMIC ATTRIBUTE ASSIGNMENT
# =============================

# --- Example 5: Adding attributes after creation ---
print("=== Dynamic Attributes ===")
print()

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Trush")
p2 = Person("Rahul")

# Add a new attribute to p1 only
p1.hobby = "painting"

print(f"  p1.name = '{p1.name}', p1.hobby = '{p1.hobby}'")
print(f"  p2.name = '{p2.name}'")

# p2 does NOT have 'hobby'
try:
    print(f"  p2.hobby = '{p2.hobby}'")
except AttributeError as e:
    print(f"  p2 has no hobby: {e}")
print()

# =============================
# 6. CHECKING ATTRIBUTES
# =============================

# --- Example 6: hasattr() and getattr() ---
print("=== Checking Attributes ===")
print()

print(f"  Does p1 have 'name'? {hasattr(p1, 'name')}")
print(f"  Does p1 have 'hobby'? {hasattr(p1, 'hobby')}")
print(f"  Does p2 have 'hobby'? {hasattr(p2, 'hobby')}")
print()

# getattr with a default value
email = getattr(p1, "email", "not set")
print(f"  p1's email: {email}")
print()

# =============================
# 7. CLASS ATTRIBUTES WITH DEFAULTS
# =============================

# --- Example 7: Practical use of class attributes ---
print("=== Practical Class Attributes ===")
print()

class BankAccount:
    bank_name = "Python National Bank"   # shared by all accounts
    interest_rate = 0.05                  # 5% for all accounts

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

acc1 = BankAccount("Trush", 1000)
acc2 = BankAccount("Rahul", 5000)

print(f"  Bank: {BankAccount.bank_name}")
print(f"  Interest Rate: {BankAccount.interest_rate * 100}%")
print(f"  {acc1.owner}: ${acc1.balance}")
print(f"  {acc2.owner}: ${acc2.balance}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a 'Game' class with a class attribute 'total_games = 0'
# 2. In __init__, take 'title' and 'genre' as instance attributes
# 3. Increment total_games each time a game is created
# 4. Create 3 games and print the total count
# ============================================
