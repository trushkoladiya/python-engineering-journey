# ============================================
# MODULE 7 - SUBTOPIC 23: Nested Dictionaries
# ============================================

# =============================
# 1. CREATING NESTED DICTIONARIES
# =============================

# --- Example 1: Basic nested dict ---
students = {
    "Trush": {"age": 21, "grade": "A"},
    "Rahul": {"age": 21, "grade": "B"},
    "Charlie": {"age": 19, "grade": "A"},
}
print("Students:", students)

# --- Example 2: Deeper nesting ---
company = {
    "engineering": {
        "team_lead": "Trush",
        "members": ["Rahul", "Charlie"],
        "budget": 50000,
    },
    "marketing": {
        "team_lead": "David",
        "members": ["Eve", "Frank"],
        "budget": 30000,
    },
}
print("\nCompany:", company)

# =============================
# 2. ACCESSING NESTED DATA
# =============================

# --- Example 3: Chained access ---
print("\nTrush's grade:", students["Trush"]["grade"])
print("Rahul's age:", students["Rahul"]["age"])

# --- Example 4: Deep access ---
print("\nEngineering lead:", company["engineering"]["team_lead"])
print("Marketing budget:", company["marketing"]["budget"])
print("First eng member:", company["engineering"]["members"][0])

# --- Example 5: Using variables ---
department = "marketing"
field = "team_lead"
print(f"\n{department} {field}: {company[department][field]}")

# =============================
# 3. MODIFYING NESTED DATA
# =============================

# --- Example 6: Update a nested value ---
students["Trush"]["grade"] = "A+"
print("\nTrush after update:", students["Trush"])

# --- Example 7: Add to nested dict ---
students["Rahul"]["email"] = "rahul@example.com"
print("Rahul after add:", students["Rahul"])

# --- Example 8: Add new nested entry ---
students["Diana"] = {"age": 22, "grade": "B+"}
print("Diana added:", students["Diana"])

# --- Example 9: Modify nested list ---
company["engineering"]["members"].append("Grace")
print(f"\nEngineering team: {company['engineering']['members']}")

# =============================
# 4. ITERATING NESTED DICTS
# =============================

# --- Example 10: Loop through outer and inner ---
students = {
    "Trush": {"age": 21, "grade": "A", "score": 95},
    "Rahul": {"age": 21, "grade": "B", "score": 87},
    "Charlie": {"age": 19, "grade": "A", "score": 92},
}

print("\n--- Student Report ---")
for name, info in students.items():
    print(f"\n  {name}:")
    for key, value in info.items():
        print(f"    {key}: {value}")

# --- Example 11: Collecting specific nested values ---
print("\nAll grades:")
for name, info in students.items():
    print(f"  {name}: {info['grade']}")

# =============================
# 5. SAFE NESTED ACCESS
# =============================

# --- Example 12: Using get() for safety ---
grade = students.get("Diana", {}).get("grade", "N/A")
print(f"\nDiana's grade: {grade}")   # N/A

trush_email = students.get("Trush", {}).get("email", "no email")
print(f"Trush's email: {trush_email}")   # no email

# =============================
# 6. PRACTICAL EXAMPLE
# =============================

# --- Example 13: Grade summary ---
class_data = {
    "Trush": {"math": 90, "science": 85, "english": 92},
    "Rahul": {"math": 78, "science": 82, "english": 75},
    "Charlie": {"math": 95, "science": 88, "english": 91},
}

print("\n--- Grade Averages ---")
for name, subjects in class_data.items():
    scores = list(subjects.values())
    avg = sum(scores) / len(scores)
    print(f"  {name}: {avg:.1f}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a nested dict for 3 products with name, price, stock
# 2. Access and modify a nested value
# 3. Loop through and print all nested data formatted
# ============================================
