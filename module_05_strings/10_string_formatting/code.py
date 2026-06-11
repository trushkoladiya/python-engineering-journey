# ============================================
# MODULE 5 - SUBTOPIC 10: String Formatting
# ============================================

# =============================
# 1. F-STRINGS (MODERN WAY)
# =============================

# --- Example 1: Basic f-string ---
name = "Trush"
age = 21
print(f"My name is {name} and I am {age} years old.")

# --- Example 2: Expressions inside f-strings ---
x = 10
y = 3
print(f"{x} + {y} = {x + y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

# --- Example 3: String methods in f-strings ---
name = "trush"
print()
print(f"Name: {name.upper()}")        # TRUSH
print(f"Name: {name.capitalize()}")   # Trush

# --- Example 4: Multiple values ---
city = "Ahmedabad"
temp = 38
print(f"It is {temp}°C in {city} today.")

# =============================
# 2. FORMAT() METHOD
# =============================

# --- Example 5: Basic format() ---
name = "Rahul"
age = 22
print()
print("My name is {} and I am {} years old.".format(name, age))

# --- Example 6: Numbered placeholders ---
print("{0} likes {1}. {0} also likes {2}.".format("Trush", "Python", "Java"))

# --- Example 7: Named placeholders ---
print("{name} is {age} years old.".format(name="Priya", age=23))

# =============================
# 3. NUMBER FORMATTING
# =============================

# --- Example 8: Decimal places ---
pi = 3.14159265
print()
print(f"Default: {pi}")
print(f"2 decimals: {pi:.2f}")    # 3.14
print(f"4 decimals: {pi:.4f}")    # 3.1416
print(f"0 decimals: {pi:.0f}")    # 3

# --- Example 9: Thousands separator ---
population = 8500000
price = 1234567.89
print()
print(f"Population: {population:,}")        # 8,500,000
print(f"Price: ${price:,.2f}")              # $1,234,567.89

# --- Example 10: Percentage ---
correct = 45
total = 60
percent = correct / total
print()
print(f"Score: {correct}/{total}")
print(f"Percentage: {percent:.1%}")   # 75.0%
print(f"Percentage: {percent:.0%}")   # 75%

# =============================
# 4. ALIGNMENT AND PADDING
# =============================

# --- Example 11: Right-align ---
print()
print(f"{'Item':<15} {'Price':>10}")
print(f"{'-' * 25}")
print(f"{'Apple':<15} {'$1.50':>10}")
print(f"{'Banana':<15} {'$0.75':>10}")
print(f"{'Cherry':<15} {'$3.00':>10}")

# --- Example 12: Center alignment ---
title = "Python Strings"
print()
print(f"{'=' * 30}")
print(f"{title:^30}")
print(f"{'=' * 30}")

# --- Example 13: Padding with characters ---
print()
print(f"{'Hello':*^20}")    # *******Hello********
print(f"{'Hello':->20}")    # ---------------Hello
print(f"{'Hello':-<20}")    # Hello---------------

# --- Example 14: Number alignment ---
print()
print("--- Sales Report ---")
for i in range(1, 6):
    amount = i * 1234
    print(f"  Day {i}: ${amount:>10,}")

# =============================
# 5. PRACTICAL FORMATTING
# =============================

# --- Example 15: Formatted table ---
print()
print(f"{'Name':<12} {'Age':>5} {'City':<15}")
print("-" * 35)
data = [
    ("Trush", 21, "Ahmedabad"),
    ("Rahul", 22, "Mumbai"),
    ("Priya", 23, "Delhi"),
]
for name, age, city in data:
    print(f"{name:<12} {age:>5} {city:<15}")

# --- Example 16: Receipt format ---
print()
print("=" * 30)
print(f"{'RECEIPT':^30}")
print("=" * 30)
items = [("Coffee", 4.50), ("Sandwich", 8.99), ("Cookie", 2.50)]
total = 0
for item, price in items:
    print(f"  {item:<15} ${price:>6.2f}")
    total += price
print("-" * 30)
print(f"  {'TOTAL':<15} ${total:>6.2f}")
print("=" * 30)

# --- Example 17: Multiplication table with formatting ---
print()
print("--- Multiplication Table ---")
# Header
header = "    "
for i in range(1, 6):
    header = header + f"{i:>4}"
print(header)
print("   " + "-" * 20)
# Rows
for i in range(1, 6):
    row = f"{i:>2} |"
    for j in range(1, 6):
        row = row + f"{i * j:>4}"
    print(row)

# ============================================
# TRY IT YOURSELF:
# 1. Print your name and age using an f-string
# 2. Format 3.14159 to show exactly 3 decimal places
# 3. Create a formatted table with 3 products and their prices
# ============================================
