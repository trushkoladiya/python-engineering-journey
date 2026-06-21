# ============================================
# MODULE 7 - SUBTOPIC 6: Tuple Packing & Unpacking
# ============================================

# =============================
# 1. PACKING
# =============================

# --- Example 1: Automatic packing ---
person = "Trush", 21, "New York"
print("Packed:", person)
print("Type:", type(person))   # <class 'tuple'>

# --- Example 2: Packing with parentheses (same result) ---
coordinates = (40.7128, -74.0060)
print("\nCoordinates:", coordinates)

# --- Example 3: Packing different types ---
record = "Rahul", 30, True, 85.5
print("Record:", record)

# =============================
# 2. UNPACKING
# =============================

# --- Example 4: Basic unpacking ---
person = ("Trush", 21, "New York")
name, age, city = person

print(f"\nName: {name}")
print(f"Age: {age}")
print(f"City: {city}")

# --- Example 5: Unpacking coordinates ---
point = (10, 20)
x, y = point
print(f"\nX: {x}, Y: {y}")

# --- Example 6: Unpacking in a loop ---
students = [("Trush", 95), ("Rahul", 87), ("Charlie", 92)]
print("\nStudent scores:")
for name, score in students:
    print(f"  {name}: {score}")

# --- Example 7: Unpacking from enumerate ---
fruits = ("apple", "banana", "cherry")
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# =============================
# 3. EXTENDED UNPACKING WITH *
# =============================

# --- Example 8: Capture first and rest ---
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(f"\nFirst: {first}")
print(f"Rest: {rest}")       # [2, 3, 4, 5] — a list!

# --- Example 9: Capture first, middle, last ---
data = (10, 20, 30, 40, 50, 60)
first, *middle, last = data
print(f"\nFirst: {first}")
print(f"Middle: {middle}")   # [20, 30, 40, 50]
print(f"Last: {last}")

# --- Example 10: Capture last only ---
letters = ("a", "b", "c", "d", "e")
*beginning, last = letters
print(f"\nBeginning: {beginning}")   # ['a', 'b', 'c', 'd']
print(f"Last: {last}")

# --- Example 11: Star with two elements ---
pair = (1, 2)
first, *rest = pair
print(f"\nFirst: {first}")
print(f"Rest: {rest}")   # [2]

# --- Example 12: Star getting empty list ---
tiny = (42,)
only, *rest = tiny
print(f"\nOnly: {only}")
print(f"Rest: {rest}")   # []

# =============================
# 4. SWAPPING VARIABLES
# =============================

# --- Example 13: Classic swap (without temp variable) ---
a = 10
b = 20
print(f"\nBefore swap: a={a}, b={b}")

a, b = b, a
print(f"After swap:  a={a}, b={b}")

# --- Example 14: Three-way swap ---
x, y, z = 1, 2, 3
print(f"\nBefore: x={x}, y={y}, z={z}")

x, y, z = z, x, y
print(f"After:  x={x}, y={y}, z={z}")

# --- Example 15: Practical swap example ---
names = ["Trush", "Amit", "Rahul"]
print(f"\nBefore sort step: {names}")

# Swap first two elements if out of order
if names[0] > names[1]:
    names[0], names[1] = names[1], names[0]

print(f"After swap: {names}")

# =============================
# 5. PRACTICAL UNPACKING
# =============================

# --- Example 16: Unpacking returned data ---
# Simulating data that might come from a calculation
rgb = (255, 128, 0)
red, green, blue = rgb
print(f"\nRed: {red}, Green: {green}, Blue: {blue}")

# --- Example 17: Ignoring values with _ ---
record = ("Trush", 21, "trushkoladiya.work@gmail.com", "New York")
name, _, email, _ = record   # _ is used for values we don't need
print(f"\nName: {name}")
print(f"Email: {email}")

# --- Example 18: Unpacking with * to ignore middle ---
data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first, second, *_, last = data
print(f"\nFirst: {first}, Second: {second}, Last: {last}")

# ============================================
# TRY IT YOURSELF:
# 1. Pack your name, age, and city into a tuple, then unpack them
# 2. Use extended unpacking to get the first and last elements
# 3. Swap two variables using tuple unpacking
# ============================================
