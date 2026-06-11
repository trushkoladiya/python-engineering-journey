# ============================================
# MODULE 7 - SUBTOPIC 15: Dictionary Creation
# ============================================

# =============================
# 1. EMPTY DICTIONARY
# =============================

# --- Example 1: Using {} ---
empty = {}
print("Empty dict:", empty)
print("Type:", type(empty))
print("Length:", len(empty))

# --- Example 2: Using dict() ---
empty2 = dict()
print("Also empty:", empty2)

# =============================
# 2. DICTIONARY WITH VALUES
# =============================

# --- Example 3: Basic key-value pairs ---
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print("\nPerson:", person)

# --- Example 4: Number keys ---
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("Squares:", squares)

# --- Example 5: Mixed key types ---
mixed_keys = {"name": "Trush", 1: "one", (0, 0): "origin"}
print("Mixed keys:", mixed_keys)

# =============================
# 3. USING dict() CONSTRUCTOR
# =============================

# --- Example 6: dict() with keyword arguments ---
car = dict(brand="Toyota", model="Camry", year=2024)
print("\nCar:", car)

# --- Example 7: dict() from list of tuples ---
pairs = [("a", 1), ("b", 2), ("c", 3)]
from_tuples = dict(pairs)
print("From tuples:", from_tuples)

# --- Example 8: dict() from zip ---
keys = ["name", "age", "city"]
values = ["Rahul", 30, "Delhi"]
zipped = dict(zip(keys, values))
print("From zip:", zipped)

# =============================
# 4. MIXED VALUE TYPES
# =============================

# --- Example 9: Values can be any type ---
student = {
    "name": "Charlie",
    "age": 20,
    "scores": [90, 85, 92],
    "active": True,
    "address": None,
}
print("\nStudent:", student)

# --- Example 10: Show types of values ---
for key in student:
    print(f"  {key}: {student[key]} ({type(student[key]).__name__})")

# =============================
# 5. NESTED DICTIONARIES
# =============================

# --- Example 11: Dict inside dict ---
students = {
    "Trush": {"age": 21, "grade": "A"},
    "Rahul": {"age": 21, "grade": "B"},
    "Charlie": {"age": 19, "grade": "A"},
}
print("\nAll students:", students)
print("Trush's data:", students["Trush"])

# =============================
# 6. KEY UNIQUENESS
# =============================

# --- Example 12: Duplicate keys — last one wins ---
data = {"a": 1, "b": 2, "a": 99}
print("\nDuplicate key result:", data)   # {'a': 99, 'b': 2}

# =============================
# 7. PRACTICAL CREATION
# =============================

# --- Example 13: Building a dict in a loop ---
squares = {}
for i in range(1, 6):
    squares[i] = i * i
print("\nSquares dict:", squares)

# --- Example 14: From user-like data ---
raw = "name=Trush,age=21,city=Mumbai"
parts = raw.split(",")
result = {}
for part in parts:
    key, value = part.split("=")
    result[key] = value
print("Parsed:", result)

# ============================================
# TRY IT YOURSELF:
# 1. Create a dictionary with 3 friends and their ages
# 2. Create a dict using dict() with keyword arguments
# 3. Build a dict from two lists using zip()
# ============================================
