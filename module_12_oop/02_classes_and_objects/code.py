# ============================================
# MODULE 12 - SUBTOPIC 2: Classes and Objects
# ============================================

# A CLASS is a blueprint. An OBJECT is a real instance of that blueprint.

# =============================
# 1. DEFINING A SIMPLE CLASS
# =============================

# --- Example 1: Simplest possible class ---
print("=== Simplest Class ===")
print()

class Dog:
    pass   # 'pass' means "nothing here yet"

# 'Dog' is now a class — a blueprint
print(f"  Dog is a: {type(Dog)}")
print()

# =============================
# 2. CREATING OBJECTS
# =============================

# --- Example 2: Making objects from a class ---
print("=== Creating Objects ===")
print()

# Call the class like a function to create an object
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

print(f"  dog1: {dog1}")
print(f"  dog2: {dog2}")
print(f"  dog3: {dog3}")
print(f"  Each object has a unique memory address!")
print()

# --- Example 3: Objects are independent ---
print("=== Objects Are Independent ===")
print()

print(f"  dog1 == dog2? {dog1 == dog2}")   # False — different objects
print(f"  dog1 is dog2? {dog1 is dog2}")   # False — different in memory
print()

# =============================
# 3. ADDING ATTRIBUTES
# =============================

# --- Example 4: Attaching data to objects ---
print("=== Adding Attributes ===")
print()

dog1.name = "Buddy"
dog1.age = 3
dog1.breed = "Golden Retriever"

dog2.name = "Max"
dog2.age = 5
dog2.breed = "German Shepherd"

print(f"  Dog 1: {dog1.name}, age {dog1.age}, breed {dog1.breed}")
print(f"  Dog 2: {dog2.name}, age {dog2.age}, breed {dog2.breed}")
print()

# =============================
# 4. EACH OBJECT IS SEPARATE
# =============================

# --- Example 5: Changing one object doesn't affect others ---
print("=== Objects Are Separate ===")
print()

dog1.name = "Buddy Jr."
print(f"  dog1.name changed to: '{dog1.name}'")
print(f"  dog2.name still: '{dog2.name}'")
print()

# =============================
# 5. MULTIPLE CLASSES
# =============================

# --- Example 6: Creating different classes ---
print("=== Multiple Classes ===")
print()

class Car:
    pass

class Book:
    pass

my_car = Car()
my_car.brand = "Toyota"
my_car.year = 2023

my_book = Book()
my_book.title = "Python Basics"
my_book.pages = 250

print(f"  Car: {my_car.brand}, {my_car.year}")
print(f"  Book: '{my_book.title}', {my_book.pages} pages")
print()

# =============================
# 6. CHECKING TYPE
# =============================

# --- Example 7: type() and isinstance() ---
print("=== Checking Object Type ===")
print()

print(f"  type(dog1): {type(dog1)}")
print(f"  type(my_car): {type(my_car)}")
print(f"  type(my_book): {type(my_book)}")
print()

print(f"  isinstance(dog1, Dog): {isinstance(dog1, Dog)}")
print(f"  isinstance(dog1, Car): {isinstance(dog1, Car)}")
print(f"  isinstance(my_car, Car): {isinstance(my_car, Car)}")
print()

# =============================
# 7. OBJECTS WITH COLLECTIONS
# =============================

# --- Example 8: Storing objects in a list ---
print("=== Objects in Collections ===")
print()

class Student:
    pass

students = []

s1 = Student()
s1.name = "Trush"
s1.grade = "A"
students.append(s1)

s2 = Student()
s2.name = "Rahul"
s2.grade = "B+"
students.append(s2)

s3 = Student()
s3.name = "Charlie"
s3.grade = "A-"
students.append(s3)

for student in students:
    print(f"  {student.name}: grade {student.grade}")

print()

# =============================
# 8. CLASS NAMING CONVENTION
# =============================

# --- Example 9: CamelCase for classes ---
print("=== Naming Convention ===")
print()

# Good class names (CamelCase):
#   Dog, BankAccount, StudentRecord, ShoppingCart

# Bad class names:
#   dog, bank_account, STUDENT  (these are for variables/constants)

print("  Classes use CamelCase:  Dog, BankAccount, StudentRecord")
print("  Variables use snake_case: my_dog, bank_account, student_list")

# ============================================
# TRY IT YOURSELF:
# 1. Create a class called 'Phone' and make 2 phone objects
# 2. Add attributes: brand, model, price
# 3. Store them in a list and print each phone's info
# ============================================
