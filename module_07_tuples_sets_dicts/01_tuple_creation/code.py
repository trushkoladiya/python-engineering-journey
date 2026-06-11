# ============================================
# MODULE 7 - SUBTOPIC 1: Tuple Creation
# ============================================

# =============================
# 1. EMPTY TUPLE
# =============================

# --- Example 1: Creating an empty tuple with () ---
empty = ()
print("Empty tuple:", empty)
print("Length:", len(empty))   # 0
print("Type:", type(empty))   # <class 'tuple'>

# --- Example 2: Creating an empty tuple with tuple() ---
another = tuple()
print("Also empty:", another)   # ()

# =============================
# 2. SINGLE-ELEMENT TUPLE
# =============================

# --- Example 3: Correct way — with trailing comma ---
single = (42,)
print("\nSingle tuple:", single)
print("Type:", type(single))   # <class 'tuple'>
print("Length:", len(single))  # 1

# --- Example 4: Wrong way — no comma means NOT a tuple ---
not_tuple = (42)
print("\nNot a tuple:", not_tuple)
print("Type:", type(not_tuple))   # <class 'int'>

# --- Example 5: String single-element tuple ---
word = ("hello",)
print("\nString tuple:", word)
print("Type:", type(word))   # <class 'tuple'>

# =============================
# 3. MULTIPLE ELEMENTS
# =============================

# --- Example 6: Tuple of integers ---
numbers = (1, 2, 3, 4, 5)
print("\nNumbers:", numbers)

# --- Example 7: Tuple of strings ---
fruits = ("apple", "banana", "cherry")
print("Fruits:", fruits)

# --- Example 8: Without parentheses (also valid) ---
colors = "red", "green", "blue"
print("Colors:", colors)
print("Type:", type(colors))   # <class 'tuple'>

# =============================
# 4. MIXED DATA TYPES
# =============================

# --- Example 9: Different types in one tuple ---
mixed = (42, "hello", 3.14, True, None)
print("\nMixed:", mixed)

# --- Example 10: Show type of each element ---
data = (10, "Python", 3.14, False)
for item in data:
    print(f"  {item} → {type(item)}")

# =============================
# 5. NESTED TUPLES
# =============================

# --- Example 11: Tuple of tuples ---
nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("\nNested:", nested)
print("First inner tuple:", nested[0])    # (1, 2, 3)
print("Second inner tuple:", nested[1])   # (4, 5, 6)

# --- Example 12: Mixed nesting ---
student = ("Trush", (95, 87, 92), True)
print("\nStudent:", student)
print("Name:", student[0])
print("Scores:", student[1])

# =============================
# 6. CREATING TUPLES FROM OTHER TYPES
# =============================

# --- Example 13: From a list ---
from_list = tuple([10, 20, 30])
print("\nFrom list:", from_list)   # (10, 20, 30)

# --- Example 14: From a string ---
from_string = tuple("Hello")
print("From string:", from_string)   # ('H', 'e', 'l', 'l', 'o')

# --- Example 15: From a range ---
from_range = tuple(range(5))
print("From range:", from_range)   # (0, 1, 2, 3, 4)

# --- Example 16: From range with step ---
from_range2 = tuple(range(1, 10, 2))
print("From range(1,10,2):", from_range2)   # (1, 3, 5, 7, 9)

# =============================
# 7. COMPARING TUPLE vs NOT TUPLE
# =============================

# --- Example 17: Understanding the comma rule ---
a = (5,)       # tuple
b = (5)        # int
c = 5,         # tuple (no parentheses needed!)

print(f"\n(5,) → type: {type(a)}, value: {a}")
print(f"(5)  → type: {type(b)}, value: {b}")
print(f"5,   → type: {type(c)}, value: {c}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a tuple with your name, age, and city
# 2. Create a single-element tuple with your favorite number
# 3. Create a tuple from the string "Python" using tuple()
# ============================================
