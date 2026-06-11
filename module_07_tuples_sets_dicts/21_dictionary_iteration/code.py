# ============================================
# MODULE 7 - SUBTOPIC 21: Dictionary Iteration
# ============================================

# =============================
# 1. LOOPING OVER KEYS (DEFAULT)
# =============================

# --- Example 1: Basic key loop ---
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print("Keys:")
for key in person:
    print(f"  {key}")

# --- Example 2: Using keys to access values ---
scores = {"Trush": 95, "Rahul": 87, "Charlie": 92}
print("\nScores:")
for name in scores:
    print(f"  {name}: {scores[name]}")

# =============================
# 2. LOOPING OVER VALUES
# =============================

# --- Example 3: Basic values loop ---
prices = {"apple": 2.50, "banana": 1.75, "cherry": 4.00}
print("\nPrices:")
for price in prices.values():
    print(f"  ${price:.2f}")

# --- Example 4: Sum of values ---
total = 0
for price in prices.values():
    total = total + price
print(f"Total: ${total:.2f}")

# =============================
# 3. LOOPING OVER KEY-VALUE PAIRS
# =============================

# --- Example 5: Basic items loop ---
person = {"name": "Trush", "age": 21, "city": "Mumbai"}
print("\nPerson details:")
for key, value in person.items():
    print(f"  {key}: {value}")

# --- Example 6: Formatted output ---
inventory = {"apples": 50, "bananas": 30, "oranges": 45, "grapes": 20}
print("\n--- Inventory Report ---")
for item, count in inventory.items():
    status = "LOW" if count < 35 else "OK"
    print(f"  {item:10s} {count:3d} [{status}]")

# =============================
# 4. ENUMERATE WITH DICTIONARIES
# =============================

# --- Example 7: Numbered iteration ---
fruits = {"apple": "red", "banana": "yellow", "grape": "purple"}
print("\nNumbered list:")
for i, (fruit, color) in enumerate(fruits.items(), 1):
    print(f"  {i}. {fruit} is {color}")

# =============================
# 5. FILTERING DURING ITERATION
# =============================

# --- Example 8: Collect passing students ---
scores = {"Trush": 95, "Rahul": 42, "Charlie": 78, "Diana": 35, "Eve": 88}
passing = {}
failing = {}

for name, score in scores.items():
    if score >= 50:
        passing[name] = score
    else:
        failing[name] = score

print(f"\nPassing: {passing}")
print(f"Failing: {failing}")

# --- Example 9: Finding entries ---
ages = {"Trush": 21, "Rahul": 35, "Charlie": 18, "Diana": 42, "Eve": 28}
print("\nPeople over 25:")
for name, age in ages.items():
    if age > 25:
        print(f"  {name}: {age}")

# =============================
# 6. BUILDING NEW DICTS FROM ITERATION
# =============================

# --- Example 10: Transforming values ---
prices = {"apple": 2.50, "banana": 1.75, "cherry": 4.00}
discounted = {}
for item, price in prices.items():
    discounted[item] = round(price * 0.8, 2)   # 20% off

print(f"\nOriginal: {prices}")
print(f"Discounted: {discounted}")

# --- Example 11: Counting characters ---
text = "hello world"
char_count = {}
for char in text:
    if char != " ":
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1

print(f"\nCharacter counts in '{text}':")
for char, count in sorted(char_count.items()):
    print(f"  '{char}': {count}")

# ============================================
# TRY IT YOURSELF:
# 1. Loop through a dictionary and print only keys
# 2. Loop through values and find the maximum
# 3. Use items() to filter and build a new dictionary
# ============================================
