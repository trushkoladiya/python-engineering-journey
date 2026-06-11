# ============================================
# MODULE 5 - SUBTOPIC 13: Performance & Best Practices
# ============================================

# =============================
# 1. CONCATENATION WITH + (SIMPLE CASES)
# =============================

# --- Example 1: Simple concatenation is fine ---
first = "Hello"
second = "World"
result = first + " " + second
print("Simple concat:", result)   # Hello World

# --- Example 2: Small number of pieces — + is OK ---
greeting = "Hi" + " " + "there" + "!"
print("Small concat:", greeting)  # Hi there!

# =============================
# 2. JOIN() FOR MANY STRINGS
# =============================

# --- Example 3: Building with + in a loop (less efficient) ---
result_plus = ""
for i in range(10):
    result_plus = result_plus + str(i)
print()
print("Using +:", result_plus)   # 0123456789

# --- Example 4: Building with join() (more efficient) ---
parts = []
for i in range(10):
    parts = parts + [str(i)]
result_join = "".join(parts)
print("Using join:", result_join)   # 0123456789

# --- Example 5: Join is cleaner for building sentences ---
words = ["Python", "is", "a", "great", "language"]
sentence_plus = ""
for i in range(len(words)):
    sentence_plus = sentence_plus + words[i]
    if i < len(words) - 1:
        sentence_plus = sentence_plus + " "

sentence_join = " ".join(words)

print()
print("With +:", sentence_plus)
print("With join:", sentence_join)
print("Same?", sentence_plus == sentence_join)   # True

# --- Example 6: Join for comma-separated values ---
items = ["apple", "banana", "cherry", "date"]
csv_line = ", ".join(items)
print()
print("CSV:", csv_line)   # apple, banana, cherry, date

# =============================
# 3. F-STRINGS VS CONCATENATION
# =============================

# --- Example 7: Concatenation with type conversion ---
name = "Trush"
age = 21
score = 95.5

# ❌ With + (need str() conversions, harder to read)
message1 = "Name: " + name + ", Age: " + str(age) + ", Score: " + str(score)

# ✅ With f-string (clean and readable)
message2 = f"Name: {name}, Age: {age}, Score: {score}"

print()
print("With +:", message1)
print("With f:", message2)
print("Same?", message1 == message2)   # True

# --- Example 8: F-strings with formatting ---
price = 19.99
quantity = 3
total = price * quantity

# ❌ Messy with concatenation
print()
print("Total: $" + str(round(total, 2)))

# ✅ Clean with f-string
print(f"Total: ${total:.2f}")

# =============================
# 4. AVOIDING UNNECESSARY COPIES
# =============================

# --- Example 9: Multiple concatenations create many strings ---
# Each += creates a brand new string
text = ""
text = text + "Hello"    # new string "Hello"
text = text + " "         # new string "Hello "
text = text + "World"     # new string "Hello World"
text = text + "!"         # new string "Hello World!"
print()
print("Built step by step:", text)

# Better: do it in one step
text = "Hello" + " " + "World" + "!"
print("Built at once:", text)

# --- Example 10: Best — use f-strings or join ---
# For fixed parts:
text = f"Hello World!"
print("With f-string:", text)

# =============================
# 5. PRACTICAL COMPARISON
# =============================

# --- Example 11: Building a numbered list ---
items = ["Learn Python", "Practice daily", "Build projects", "Never give up"]

# Method 1: Using + (works but verbose)
print()
print("--- Method 1: Using + ---")
result1 = ""
for i in range(len(items)):
    result1 = result1 + str(i + 1) + ". " + items[i] + "\n"
print(result1)

# Method 2: Using f-string + join (cleaner)
print("--- Method 2: Using f-string + join ---")
lines = []
for i in range(len(items)):
    lines = lines + [f"{i + 1}. {items[i]}"]
result2 = "\n".join(lines)
print(result2)

# --- Example 12: Building a CSV from data ---
print()
print("--- Building CSV ---")
names = ["Trush", "Rahul", "Priya"]
ages = ["21", "22", "23"]
cities = ["Ahmedabad", "Mumbai", "Delhi"]

# Build each row with join
print("name,age,city")   # header
for i in range(len(names)):
    row = ",".join([names[i], ages[i], cities[i]])
    print(row)

# =============================
# 6. SUMMARY OF BEST PRACTICES
# =============================

# --- Example 13: Quick reference ---
print()
print("=" * 40)
print("STRING BEST PRACTICES SUMMARY")
print("=" * 40)
print()
print("1. Simple concat (2-3 pieces) → use +")
print("   Example: 'Hello' + ' ' + 'World'")
print()
print("2. Many strings in a loop → use join()")
print("   Example: ' '.join(word_list)")
print()
print("3. Mix text + variables → use f-strings")
print("   Example: f'Name: {name}, Age: {age}'")
print()
print("4. Formatted numbers → use f-string specs")
print("   Example: f'Price: ${price:.2f}'")
print("=" * 40)

# ============================================
# TRY IT YOURSELF:
# 1. Build the string "1-2-3-4-5-6-7-8-9-10" using join()
# 2. Rewrite this using an f-string: "Name: " + name + " Age: " + str(age)
# 3. Build a comma-separated list of even numbers from 2 to 20
# ============================================
