# ============================================
# MODULE 6 - SUBTOPIC 9: List Iteration
# ============================================

# =============================
# 1. BASIC FOR LOOP
# =============================

# --- Example 1: Iterate over elements ---
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"  {fruit}")

# --- Example 2: Process each element ---
nums = [1, 2, 3, 4, 5]
print("\nDoubled:")
for num in nums:
    print(f"  {num} → {num * 2}")

# --- Example 3: Sum all elements ---
prices = [9.99, 14.50, 3.75, 7.25]
total = 0
for price in prices:
    total += price
print(f"\nTotal: ${total:.2f}")

# =============================
# 2. INDEX-BASED ITERATION
# =============================

# --- Example 4: Using range(len()) ---
colors = ["red", "green", "blue"]
print("\nWith indices:")
for i in range(len(colors)):
    print(f"  Index {i}: {colors[i]}")

# --- Example 5: Modify elements using index ---
nums = [1, 2, 3, 4, 5]
print("\nBefore:", nums)
for i in range(len(nums)):
    nums[i] = nums[i] ** 2
print("Squared:", nums)

# --- Example 6: Compare adjacent elements ---
temps = [72, 68, 75, 80, 65, 70]
print("\nTemperature changes:")
for i in range(1, len(temps)):
    diff = temps[i] - temps[i - 1]
    direction = "up" if diff > 0 else "down"
    print(f"  Day {i}: {temps[i]}° ({direction} {abs(diff)}°)")

# =============================
# 3. ENUMERATE()
# =============================

# --- Example 7: Basic enumerate ---
fruits = ["apple", "banana", "cherry"]
print("\nEnumerate:")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# --- Example 8: Start from 1 ---
students = ["Trush", "Rahul", "Priya"]
print("\nStudent roster:")
for num, name in enumerate(students, start=1):
    print(f"  {num}. {name}")

# --- Example 9: Find index of element ---
scores = [85, 92, 78, 96, 88]
print("\nScores above 90:")
for i, score in enumerate(scores):
    if score > 90:
        print(f"  Index {i}: {score}")

# --- Example 10: Enumerate with formatting ---
items = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [999.99, 29.99, 79.99, 349.99]
print("\n--- Inventory ---")
for i, item in enumerate(items):
    print(f"  #{i + 1}: {item:<12} ${prices[i]:>8.2f}")

# =============================
# 4. WHILE LOOP ITERATION
# =============================

# --- Example 11: While loop with list ---
fruits = ["apple", "banana", "cherry"]
i = 0
print("\nUsing while:")
while i < len(fruits):
    print(f"  {fruits[i]}")
    i += 1

# --- Example 12: While with condition ---
nums = [2, 4, 6, 7, 8, 10]
i = 0
print("\nIterating until odd number:")
while i < len(nums) and nums[i] % 2 == 0:
    print(f"  {nums[i]} (even)")
    i += 1
if i < len(nums):
    print(f"  Stopped at {nums[i]} (odd)")

# =============================
# 5. ITERATING MULTIPLE LISTS
# =============================

# --- Example 13: Parallel iteration with index ---
names = ["Trush", "Rahul", "Priya"]
ages = [21, 22, 23]
print("\nParallel iteration:")
for i in range(len(names)):
    print(f"  {names[i]} is {ages[i]} years old")

# --- Example 14: Using zip() for parallel iteration ---
names = ["Trush", "Rahul", "Priya"]
scores = [95, 87, 92]
print("\nUsing zip:")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# =============================
# 6. PRACTICAL PATTERNS
# =============================

# --- Example 15: Build result from iteration ---
words = ["hello", "world", "python"]
upper_words = []
for word in words:
    upper_words.append(word.upper())
print(f"\nOriginal: {words}")
print(f"Upper: {upper_words}")

# --- Example 16: Filter during iteration ---
nums = [1, -2, 3, -4, 5, -6, 7]
positives = []
negatives = []
for num in nums:
    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)
print(f"\nAll: {nums}")
print(f"Positives: {positives}")
print(f"Negatives: {negatives}")

# --- Example 17: Running total ---
sales = [100, 250, 75, 300, 150]
print("\n--- Running Total ---")
running = 0
for i, sale in enumerate(sales, start=1):
    running += sale
    print(f"  Day {i}: ${sale} (Total: ${running})")

# ============================================
# TRY IT YOURSELF:
# 1. Iterate over [10, 20, 30, 40] and print each element tripled
# 2. Use enumerate to print a numbered shopping list
# 3. Iterate two lists (names and grades) in parallel
# ============================================
