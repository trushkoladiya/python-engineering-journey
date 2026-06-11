# ============================================
# MODULE 7 - SUBTOPIC 4: Tuple Operations
# ============================================

# =============================
# 1. CONCATENATION (+)
# =============================

# --- Example 1: Joining two tuples ---
a = (1, 2, 3)
b = (4, 5, 6)
result = a + b
print("a + b:", result)   # (1, 2, 3, 4, 5, 6)

# --- Example 2: Joining different types ---
names = ("Trush", "Rahul")
ages = (21, 30)
combined = names + ages
print("Combined:", combined)   # ('Trush', 'Rahul', 21, 30)

# --- Example 3: Adding a single element ---
original = (1, 2, 3)
extended = original + (4,)   # Note: (4,) is a single-element tuple
print("Extended:", extended)   # (1, 2, 3, 4)

# =============================
# 2. REPETITION (*)
# =============================

# --- Example 4: Repeating a tuple ---
t = (1, 2, 3)
repeated = t * 3
print("\nt * 3:", repeated)   # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# --- Example 5: Creating initialized tuples ---
zeros = (0,) * 5
print("5 zeros:", zeros)   # (0, 0, 0, 0, 0)

dashes = ("-",) * 10
print("10 dashes:", dashes)

# =============================
# 3. MEMBERSHIP (in, not in)
# =============================

# --- Example 6: Checking if element exists ---
fruits = ("apple", "banana", "cherry", "date")
print("\n'apple' in fruits:", "apple" in fruits)       # True
print("'mango' in fruits:", "mango" in fruits)         # False
print("'mango' not in fruits:", "mango" not in fruits) # True

# --- Example 7: Membership with numbers ---
numbers = (10, 20, 30, 40, 50)
search = 30
if search in numbers:
    print(f"\n{search} is in the tuple!")
else:
    print(f"\n{search} is NOT in the tuple!")

# --- Example 8: Membership with user-like input ---
valid_colors = ("red", "green", "blue", "yellow")
chosen = "green"
if chosen in valid_colors:
    print(f"'{chosen}' is a valid color ✓")
else:
    print(f"'{chosen}' is NOT a valid color ✗")

# =============================
# 4. LENGTH (len())
# =============================

# --- Example 9: Getting tuple length ---
animals = ("cat", "dog", "bird", "fish")
print("\nLength:", len(animals))   # 4

empty = ()
print("Empty tuple length:", len(empty))   # 0

# =============================
# 5. MIN, MAX, SUM
# =============================

# --- Example 10: Min and max ---
scores = (85, 92, 78, 95, 88)
print("\nScores:", scores)
print("Highest:", max(scores))   # 95
print("Lowest:", min(scores))    # 78

# --- Example 11: Sum ---
prices = (9.99, 14.50, 3.75, 22.00)
total = sum(prices)
print(f"\nPrices: {prices}")
print(f"Total: {total}")

# --- Example 12: Min and max with strings ---
names = ("Charlie", "Trush", "Amit")
print(f"\nFirst alphabetically: {min(names)}")   # Amit
print(f"Last alphabetically: {max(names)}")      # Trush

# =============================
# 6. COMBINING OPERATIONS
# =============================

# --- Example 13: Practical example ---
week1_sales = (100, 150, 200, 180, 220)
week2_sales = (130, 170, 190, 210, 250)

all_sales = week1_sales + week2_sales
print(f"\nAll sales: {all_sales}")
print(f"Total days: {len(all_sales)}")
print(f"Total revenue: {sum(all_sales)}")
print(f"Best day: {max(all_sales)}")
print(f"Worst day: {min(all_sales)}")

# ============================================
# TRY IT YOURSELF:
# 1. Concatenate two tuples of your favorite foods
# 2. Check if "python" is in a tuple of languages
# 3. Find the total of a tuple of 5 prices
# ============================================
