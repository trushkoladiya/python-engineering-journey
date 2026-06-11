# ============================================
# MODULE 12 - SUBTOPIC 12: Object Relationships
# ============================================

# Objects relate to each other in 3 ways:
#   Association  → connected but independent
#   Aggregation  → weak ownership (parts survive alone)
#   Composition  → strong ownership (parts die with parent)

# =============================
# 1. ASSOCIATION
# =============================

# --- Example 1: Objects know each other, no ownership ---
print("=== Association ===")
print()

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Student:
    def __init__(self, name):
        self.name = name

# They are connected but independent
teacher = Teacher("Mr. Smith", "Math")
student1 = Student("Trush")
student2 = Student("Rahul")

# Teacher knows students, students know teacher — but no ownership
print(f"  Teacher: {teacher.name} ({teacher.subject})")
print(f"  Student: {student1.name}")
print(f"  Student: {student2.name}")
print("  → They are associated, but neither owns the other")
print()

# =============================
# 2. AGGREGATION (WEAK OWNERSHIP)
# =============================

# --- Example 2: Department has employees (employees exist independently) ---
print("=== Aggregation ===")
print()

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def info(self):
        return f"{self.name} ({self.role})"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        self.employees = [e for e in self.employees if e.name != name]

    def show(self):
        print(f"  Department: {self.name}")
        if self.employees:
            for emp in self.employees:
                print(f"    - {emp.info()}")
        else:
            print(f"    (empty)")

# Employees exist independently
trush = Employee("Trush", "Developer")
rahul = Employee("Rahul", "Designer")
charlie = Employee("Charlie", "Manager")

# Department aggregates employees
engineering = Department("Engineering")
engineering.add_employee(trush)
engineering.add_employee(rahul)

design = Department("Design")
design.add_employee(rahul)       # Rahul can be in multiple departments!
design.add_employee(charlie)

engineering.show()
design.show()
print()

# If we delete a department, employees still exist
del engineering
print(f"  After deleting Engineering dept:")
print(f"  Trush still exists: {trush.info()}")
print(f"  Rahul still exists: {rahul.info()}")
print()

# =============================
# 3. COMPOSITION (STRONG OWNERSHIP)
# =============================

# --- Example 3: Car contains its own engine ---
print("=== Composition ===")
print()

class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start(self):
        return f"Engine ({self.horsepower}hp, {self.fuel_type}) started"

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, brand, hp, fuel, wheel_size):
        self.brand = brand
        # Engine and Wheels are CREATED inside Car — composition
        self.engine = Engine(hp, fuel)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]

    def start(self):
        return f"{self.brand}: {self.engine.start()}"

    def info(self):
        return (f"{self.brand}: {self.engine.horsepower}hp, "
                f"{self.engine.fuel_type}, "
                f"{len(self.wheels)} wheels (size {self.wheels[0].size})")

car = Car("Toyota", 180, "Gasoline", 17)
print(f"  {car.info()}")
print(f"  {car.start()}")
print("  → Engine and Wheels are created BY the car — they don't exist alone")
print()

# =============================
# 4. COMPOSITION: HOUSE EXAMPLE
# =============================

# --- Example 4: A house is composed of rooms ---
print("=== House Composition ===")
print()

class Room:
    def __init__(self, name, area_sqft):
        self.name = name
        self.area_sqft = area_sqft

    def info(self):
        return f"{self.name} ({self.area_sqft} sq ft)"

class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []    # rooms are created for this house

    def add_room(self, name, area):
        self.rooms.append(Room(name, area))  # Room created inside House

    def total_area(self):
        total = 0
        for room in self.rooms:
            total += room.area_sqft
        return total

    def show(self):
        print(f"  House at {self.address}:")
        for room in self.rooms:
            print(f"    - {room.info()}")
        print(f"    Total: {self.total_area()} sq ft")

house = House("123 Main St")
house.add_room("Living Room", 300)
house.add_room("Bedroom", 200)
house.add_room("Kitchen", 150)
house.add_room("Bathroom", 80)

house.show()
print()

# =============================
# 5. AGGREGATION vs COMPOSITION
# =============================

# --- Example 5: Side-by-side comparison ---
print("=== Aggregation vs Composition ===")
print()

# AGGREGATION: Library has books (books exist independently)
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):       # receives existing book
        self.books.append(book)

# Books exist before the library
book1 = Book("Python Basics")
book2 = Book("Data Science")

library = Library("City Library")
library.add_book(book1)
library.add_book(book2)

print(f"  Aggregation: Library has {len(library.books)} books")
print(f"  Books exist independently: '{book1.title}'")
print()

# COMPOSITION: Computer has CPU (CPU created with computer)
class CPU:
    def __init__(self, model, cores):
        self.model = model
        self.cores = cores

class Computer:
    def __init__(self, brand, cpu_model, cpu_cores):
        self.brand = brand
        self.cpu = CPU(cpu_model, cpu_cores)    # created INSIDE

pc = Computer("Dell", "i7", 8)
print(f"  Composition: {pc.brand} has {pc.cpu.model} ({pc.cpu.cores} cores)")
print(f"  CPU was created BY the computer")
print()

# =============================
# 6. PRACTICAL: SCHOOL SYSTEM
# =============================

# --- Example 6: Mixed relationships ---
print("=== School System ===")
print()

class Address:
    """Composed — created by School."""
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def full(self):
        return f"{self.street}, {self.city}"

class SchoolStudent:
    """Aggregated — exists independently."""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class School:
    def __init__(self, name, street, city):
        self.name = name
        self.address = Address(street, city)   # composition
        self.students = []                      # aggregation

    def enroll(self, student):
        self.students.append(student)

    def show(self):
        print(f"  {self.name} — {self.address.full()}")
        print(f"  Students ({len(self.students)}):")
        for s in self.students:
            print(f"    - {s.name} (grade {s.grade})")

# Students exist independently (aggregation)
s1 = SchoolStudent("Trush", "A")
s2 = SchoolStudent("Rahul", "B+")
s3 = SchoolStudent("Charlie", "A-")

# School creates its own address (composition)
school = School("Python Academy", "456 Code Ave", "Dev City")
school.enroll(s1)
school.enroll(s2)
school.enroll(s3)

school.show()

# ============================================
# TRY IT YOURSELF:
# 1. Create a 'Playlist' (composition) that creates Song objects
# 2. Create a 'Team' (aggregation) that has Player objects
# 3. Think about: would the parts make sense without the whole?
# ============================================
