# ============================================
# MODULE 7 - SUBTOPIC 7: Use Cases of Tuples
# ============================================

# =============================
# 1. FIXED DATA COLLECTIONS
# =============================

# --- Example 1: Days of the week ---
days = ("Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday")
print("Days:", days)
print("Total days:", len(days))

# --- Example 2: Months of the year ---
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
month_number = 3
print(f"\nMonth {month_number} is {months[month_number - 1]}")   # Mar

# --- Example 3: RGB colors ---
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
print(f"\nRed:   {red}")
print(f"Green: {green}")
print(f"Blue:  {blue}")

# =============================
# 2. AS DICTIONARY KEYS
# =============================

# --- Example 4: City distances ---
distances = {}
distances[("Delhi", "Mumbai")] = 1400
distances[("Mumbai", "Chennai")] = 1330
distances[("Delhi", "Kolkata")] = 1500

print("\nCity distances:")
for route, dist in distances.items():
    print(f"  {route[0]} → {route[1]}: {dist} km")

# --- Example 5: Grid positions ---
grid = {}
grid[(0, 0)] = "Start"
grid[(1, 2)] = "Treasure"
grid[(3, 3)] = "Exit"

print(f"\nAt (0,0): {grid[(0, 0)]}")
print(f"At (1,2): {grid[(1, 2)]}")

# =============================
# 3. AS SET ELEMENTS
# =============================

# --- Example 6: Tracking visited coordinates ---
visited = set()
visited.add((0, 0))
visited.add((1, 0))
visited.add((1, 1))
visited.add((0, 0))   # duplicate — won't be added

print(f"\nVisited positions: {visited}")
print(f"Total unique: {len(visited)}")

# --- Example 7: Checking if position was visited ---
pos = (1, 1)
if pos in visited:
    print(f"Position {pos} was already visited")

# =============================
# 4. STORING RECORDS
# =============================

# --- Example 8: Student records ---
students = [
    ("Trush", 95, "A"),
    ("Rahul", 87, "B"),
    ("Charlie", 92, "A"),
    ("Diana", 78, "C"),
]

print("\nStudent Report:")
print("-" * 30)
for name, score, grade in students:
    print(f"  {name:10s} | Score: {score} | Grade: {grade}")

# --- Example 9: Finding best student ---
best_score = 0
best_name = ""
for name, score, grade in students:
    if score > best_score:
        best_score = score
        best_name = name

print(f"\nBest student: {best_name} with score {best_score}")

# =============================
# 5. SWAPPING AND MULTIPLE ASSIGNMENT
# =============================

# --- Example 10: Quick variable assignment ---
x, y, z = 10, 20, 30
print(f"\nx={x}, y={y}, z={z}")

# --- Example 11: Swapping values ---
a, b = 5, 10
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# =============================
# 6. PROTECTING DATA
# =============================

# --- Example 12: Config that shouldn't change ---
# Using a tuple ensures the data stays constant
VALID_STATUSES = ("active", "inactive", "pending", "banned")
MAX_RETRIES = 3

user_status = "active"
if user_status in VALID_STATUSES:
    print(f"\nStatus '{user_status}' is valid ✓")

# Cannot accidentally modify:
# VALID_STATUSES[0] = "something"   # TypeError!

# --- Example 13: Tuple vs List for safety ---
# List — can be accidentally modified
settings_list = ["dark", "light", "auto"]
settings_list[0] = "broken"   # Oops! Modified by mistake

# Tuple — safe from modification
settings_tuple = ("dark", "light", "auto")
# settings_tuple[0] = "broken"   # TypeError! Protected!
print("Settings (safe):", settings_tuple)

# ============================================
# TRY IT YOURSELF:
# 1. Create a tuple of your top 3 cities and use it as constants
# 2. Create a dictionary that uses (x, y) tuples as keys
# 3. Create a list of student tuples and find the highest scorer
# ============================================
