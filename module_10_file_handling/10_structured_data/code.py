# ============================================
# MODULE 10 - SUBTOPIC 10: Working with Structured Data
# ============================================

import os
import csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================
# 1. MANUAL PARSING — LINE BY LINE
# =============================

# --- Example 1: Parse comma-separated data ---
data_file = os.path.join(SCRIPT_DIR, "students.txt")

with open(data_file, "w") as f:
    f.write("Trush,21,92\n")
    f.write("Rahul,22,85\n")
    f.write("Charlie,23,78\n")
    f.write("Diana,21,95\n")

print("Manual parsing:")
with open(data_file, "r") as file:
    for line in file:
        name, age, score = line.strip().split(",")
        print(f"  {name}: age={age}, score={score}")

# --- Example 2: Process and calculate ---
print(f"\nCalculations:")
with open(data_file, "r") as file:
    scores = []
    for line in file:
        parts = line.strip().split(",")
        name = parts[0]
        score = int(parts[2])
        scores.append(score)
        print(f"  {name}: {score}")
    
    print(f"  Average: {sum(scores)/len(scores):.1f}")
    print(f"  Highest: {max(scores)}")

# =============================
# 2. CSV MODULE — WRITING
# =============================

# --- Example 3: Write CSV with csv.writer ---
csv_file = os.path.join(SCRIPT_DIR, "grades.csv")

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Subject", "Score"])   # Header
    writer.writerow(["Trush", "Math", 92])
    writer.writerow(["Rahul", "Science", 85])
    writer.writerow(["Charlie", "English", 78])

with open(csv_file, "r") as file:
    print(f"\nCSV file content:\n{file.read()}", end="")

# --- Example 4: Write multiple rows at once ---
csv_file2 = os.path.join(SCRIPT_DIR, "products.csv")

products = [
    ["Product", "Price", "Stock"],
    ["Apple", 2.50, 100],
    ["Banana", 1.75, 50],
    ["Cherry", 4.00, 30],
]

with open(csv_file2, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(products)

print(f"\nProducts CSV:")
with open(csv_file2, "r") as file:
    print(file.read(), end="")

# =============================
# 3. CSV MODULE — READING
# =============================

# --- Example 5: Read CSV with csv.reader ---
print(f"\nReading grades CSV:")
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)   # Skip header
    print(f"  Header: {header}")
    for row in reader:
        print(f"  {row[0]}: {row[1]} = {row[2]}")

# --- Example 6: CSV as list of lists ---
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    all_data = list(reader)

print(f"\nAll data: {all_data}")

# =============================
# 4. CSV DictWriter / DictReader
# =============================

# --- Example 7: Write with DictWriter ---
dict_file = os.path.join(SCRIPT_DIR, "employees.csv")

employees = [
    {"name": "Trush", "department": "Engineering", "salary": 75000},
    {"name": "Rahul", "department": "Marketing", "salary": 65000},
    {"name": "Charlie", "department": "Engineering", "salary": 80000},
]

with open(dict_file, "w", newline="") as file:
    fieldnames = ["name", "department", "salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)

# --- Example 8: Read with DictReader ---
print(f"\nDictReader:")
with open(dict_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"  {row['name']}: {row['department']}, ${row['salary']}")

# =============================
# 5. PRACTICAL: DATA PROCESSING
# =============================

# --- Example 9: Analyze CSV data ---
print(f"\nSalary analysis:")
with open(dict_file, "r") as file:
    reader = csv.DictReader(file)
    employees_data = list(reader)

salaries = [int(e["salary"]) for e in employees_data]
print(f"  Total:   ${sum(salaries):,}")
print(f"  Average: ${sum(salaries)/len(salaries):,.0f}")
print(f"  Highest: ${max(salaries):,}")

# Group by department
departments = {}
for emp in employees_data:
    dept = emp["department"]
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(emp["name"])

print(f"\n  By department:")
for dept, names in departments.items():
    print(f"    {dept}: {', '.join(names)}")

# =============================
# CLEANUP
# =============================
for f in ["students.txt", "grades.csv", "products.csv", "employees.csv"]:
    path = os.path.join(SCRIPT_DIR, f)
    if os.path.exists(path):
        os.remove(path)
print(f"\n✓ Temp files cleaned up")

# ============================================
# TRY IT YOURSELF:
# 1. Create a CSV with your friends' names and ages
# 2. Read a CSV and calculate the average of a numeric column
# 3. Use DictReader to process a CSV by column name
# ============================================
