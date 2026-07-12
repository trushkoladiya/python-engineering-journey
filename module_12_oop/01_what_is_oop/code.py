# ============================================
# MODULE 12 - SUBTOPIC 1: What is OOP
# ============================================

# OOP = Object-Oriented Programming
# It means organizing code by combining DATA + BEHAVIOR into objects.

# =============================
# 1. THE PROBLEM WITHOUT OOP
# =============================

# --- Example 1: Managing data without OOP ---
print("=== Without OOP: Scattered Data ===")
print()

# Student data scattered in separate variables
student1_name = "Trush"
student1_age = 21
student1_grade = "A"

student2_name = "Rahul"
student2_age = 22
student2_grade = "B"

print(f"  Student 1: {student1_name}, age {student1_age}, grade {student1_grade}")
print(f"  Student 2: {student2_name}, age {student2_age}, grade {student2_grade}")
print()

# --- Example 2: Using dicts (better, but still limited) ---
print("=== Without OOP: Using Dicts ===")
print()

student1 = {"name": "Trush", "age": 21, "grade": "A"}
student2 = {"name": "Rahul", "age": 22, "grade": "B"}

print(f"  Student 1: {student1['name']}, age {student1['age']}")
print(f"  Student 2: {student2['name']}, age {student2['age']}")
print()

# This works, but dicts can't have behavior (functions) attached to them.
# You also can't enforce what keys they must have.

# =============================
# 2. YOU ALREADY USE OBJECTS!
# =============================

# --- Example 3: Strings are objects ---
print("=== You Already Use Objects! ===")
print()

message = "hello world"

# .upper() is a METHOD — a function that belongs to the string object
print(f"  message = '{message}'")
print(f"  message.upper() = '{message.upper()}'")
print(f"  message.title() = '{message.title()}'")
print(f"  message.split() = {message.split()}")
print()

# --- Example 4: Lists are objects ---
numbers = [3, 1, 4, 1, 5]
print(f"  numbers = {numbers}")
numbers.append(9)
print(f"  After .append(9): {numbers}")
numbers.sort()
print(f"  After .sort(): {numbers}")
print()

# Every string, list, dict, set — they're all objects with methods!

# =============================
# 3. THE OOP IDEA
# =============================

# --- Example 5: What OOP looks like (preview) ---
print("=== OOP: Data + Behavior Together ===")
print()

# A CLASS is a blueprint
# An OBJECT is a specific instance of that blueprint

# Here's a simple class (don't worry about the syntax yet — next subtopic!)
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hi, I'm {self.name}, age {self.age}, grade {self.grade}"


# Creating objects from the blueprint
trush = Student("Trush", 21, "A")
rahul = Student("Rahul", 22, "B")

# Data AND behavior live together
print(f"  {trush.introduce()}")
print(f"  {rahul.introduce()}")
print()

# =============================
# 4. CLASS vs OBJECT ANALOGY
# =============================

# --- Example 6: Blueprint vs instance ---
print("=== Class vs Object ===")
print()

# Think of a class as a blueprint:
#   - Class = cookie cutter (the shape)
#   - Object = cookie (the actual thing made from the shape)

print("  Class 'Student' = the blueprint")
print("  trush = Student('Trush', 21, 'A')  → an actual student object")
print("  rahul = Student('Rahul', 22, 'B')      → another student object")
print()

# Each object has its OWN data
print(f"  trush.name = '{trush.name}'")
print(f"  rahul.name = '{rahul.name}'")
print(f"  Same class, different data!")
print()

# =============================
# 5. WHY OOP MATTERS
# =============================

# --- Example 7: Comparison ---
print("=== Why OOP? ===")
print()

# Without OOP — functions and data are separate
def get_full_info_dict(student_dict):
    return f"{student_dict['name']}, age {student_dict['age']}"

student_dict = {"name": "Charlie", "age": 19}
print(f"  Without OOP: {get_full_info_dict(student_dict)}")

# With OOP — data and behavior are together
charlie = Student("Charlie", 19, "B+")
print(f"  With OOP:    {charlie.introduce()}")
print()

print("  OOP advantages:")
print("    ✓ Data + behavior live together")
print("    ✓ Easy to create many similar objects")
print("    ✓ Code mirrors real-world concepts")
print("    ✓ Better organization for large programs")

# ============================================
# TRY IT YOURSELF:
# 1. Think of 3 real-world things that could be objects
#    (e.g., a car, a book, a phone)
# 2. For each, list what DATA it would have (attributes)
# 3. For each, list what BEHAVIOR it would have (methods)
# ============================================
