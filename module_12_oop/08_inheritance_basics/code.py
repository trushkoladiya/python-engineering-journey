# ============================================
# MODULE 12 - SUBTOPIC 8: Inheritance Basics
# ============================================

# Inheritance = a child class reuses code from a parent class.
# The child gets all attributes and methods from the parent.

# =============================
# 1. BASIC INHERITANCE
# =============================

# --- Example 1: Simple parent → child ---
print("=== Basic Inheritance ===")
print()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def info(self):
        return f"Animal: {self.name}"

# Dog inherits from Animal
class Dog(Animal):
    pass   # no new code — gets everything from Animal

buddy = Dog("Buddy")
print(f"  {buddy.info()}")         # inherited from Animal
print(f"  {buddy.speak()}")        # inherited from Animal
print(f"  Type: {type(buddy)}")    # Dog
print(f"  Is Animal? {isinstance(buddy, Animal)}")  # True!
print()

# =============================
# 2. CHILD ADDS NEW METHODS
# =============================

# --- Example 2: Extending the parent ---
print("=== Child Adds Methods ===")
print()

class Cat(Animal):
    def purr(self):
        return f"{self.name} purrs..."

whiskers = Cat("Whiskers")
print(f"  {whiskers.speak()}")    # from Animal
print(f"  {whiskers.purr()}")     # new method in Cat

# Dog doesn't have purr()
try:
    buddy.purr()
except AttributeError as e:
    print(f"  buddy.purr() → Error: {e}")
print()

# =============================
# 3. USING super().__init__()
# =============================

# --- Example 3: Child has its own __init__ ---
print("=== Using super().__init__() ===")
print()

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)   # call parent's __init__
        self.doors = doors              # add new attribute

    def car_info(self):
        return f"{self.info()}, {self.doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_cc):
        super().__init__(brand, year)
        self.engine_cc = engine_cc

    def bike_info(self):
        return f"{self.info()}, {self.engine_cc}cc engine"

car = Car("Toyota", 2023, 4)
bike = Motorcycle("Harley", 2022, 1200)

print(f"  Car: {car.car_info()}")
print(f"  Bike: {bike.bike_info()}")
print()

# =============================
# 4. METHOD OVERRIDING
# =============================

# --- Example 4: Child replaces parent method ---
print("=== Method Overriding ===")
print()

class Animal2:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a generic sound"

class Dog2(Animal2):
    def speak(self):    # overrides Animal2.speak()
        return f"{self.name} says: Woof!"

class Cat2(Animal2):
    def speak(self):    # overrides Animal2.speak()
        return f"{self.name} says: Meow!"

class Duck2(Animal2):
    def speak(self):
        return f"{self.name} says: Quack!"

animals = [Dog2("Buddy"), Cat2("Whiskers"), Duck2("Donald"), Animal2("Unknown")]

for animal in animals:
    print(f"  {animal.speak()}")
print()

# =============================
# 5. CALLING PARENT METHOD WITH super()
# =============================

# --- Example 5: Extend parent method, don't replace ---
print("=== Extending Parent Method ===")
print()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name}, salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        # Call parent's get_info() and ADD to it
        base_info = super().get_info()
        return f"{base_info}, dept: {self.department}"

emp = Employee("Trush", 50000)
mgr = Manager("Rahul", 80000, "Engineering")

print(f"  Employee: {emp.get_info()}")
print(f"  Manager:  {mgr.get_info()}")
print()

# =============================
# 6. INHERITANCE CHAIN
# =============================

# --- Example 6: Checking inheritance ---
print("=== Inheritance Checks ===")
print()

class A:
    pass

class B(A):
    pass

class C(B):
    pass

obj = C()

print(f"  type(obj): {type(obj)}")
print(f"  isinstance(obj, C): {isinstance(obj, C)}")
print(f"  isinstance(obj, B): {isinstance(obj, B)}")
print(f"  isinstance(obj, A): {isinstance(obj, A)}")
print(f"  isinstance(obj, object): {isinstance(obj, object)}")
print("  → C inherits from B, B inherits from A!")
print()

# =============================
# 7. PRACTICAL: SHAPE HIERARCHY
# =============================

# --- Example 7: Real-world inheritance ---
print("=== Shape Hierarchy ===")
print()

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def describe(self):
        return f"{self.name}: area = {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(6, 8),
    Rectangle(10, 10),
]

for shape in shapes:
    print(f"  {shape.describe()}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a 'Pet' parent class with name and age
# 2. Create 'Dog' and 'Cat' children with unique methods
# 3. Override speak() in each child
# 4. Create a list of pets and call speak() on each
# ============================================
