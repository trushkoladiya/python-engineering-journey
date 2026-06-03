# ============================================
# MODULE 4 - SUBTOPIC 8: Loop Control Statements
# ============================================

# --- Example 1: break — stop the loop ---
for i in range(10):
    if i == 5:
        break           # exit the loop when i is 5
    print(i)
# Output: 0, 1, 2, 3, 4

# --- Example 2: break — search for a value ---
target = 7
for num in range(1, 20):
    if num == target:
        print("Found:", target)   # Found: 7
        break

# --- Example 3: break with while ---
count = 0
while True:              # infinite loop
    if count >= 5:
        break            # exit when count reaches 5
    print("Count:", count)
    count += 1
# Output: Count: 0, Count: 1, Count: 2, Count: 3, Count: 4

# --- Example 4: continue — skip specific values ---
for i in range(8):
    if i == 3 or i == 5:
        continue         # skip 3 and 5
    print(i)
# Output: 0, 1, 2, 4, 6, 7

# --- Example 5: continue — print only even numbers ---
for i in range(1, 11):
    if i % 2 != 0:
        continue         # skip odd numbers
    print(i)
# Output: 2, 4, 6, 8, 10

# --- Example 6: continue with while ---
num = 0
while num < 10:
    num += 1
    if num % 3 == 0:
        continue         # skip multiples of 3
    print(num, end=" ")
print()
# Output: 1 2 4 5 7 8 10

# --- Example 7: pass — placeholder ---
for i in range(5):
    pass                 # does nothing — no error
# Loop runs 5 times but does nothing

# Using pass to plan code structure:
x = 10
if x > 5:
    pass                 # TODO: add logic later
else:
    pass                 # TODO: handle else case

# --- Example 8: break — find first even number ---
for n in range(1, 20):
    if n % 2 == 0:
        print("First even:", n)   # First even: 2
        break

# --- Example 9: break only exits the innermost loop ---
for i in range(3):
    for j in range(3):
        if j == 1:
            break        # only breaks the inner loop
        print("i =", i, "j =", j)
# Output:
# i = 0 j = 0
# i = 1 j = 0
# i = 2 j = 0
# (j never gets past 1 because break stops inner loop)

# --- Example 10: Combining break and continue ---
# Print numbers 1-20, skip multiples of 3, stop at 15
for i in range(1, 21):
    if i == 15:
        print("Reached 15 — stopping!")
        break
    if i % 3 == 0:
        continue         # skip multiples of 3
    print(i, end=" ")
print()
# Output: 1 2 4 5 7 8 10 11 13 14 Reached 15 — stopping!

# --- Example 11: Finding first digit in a string ---
text = "trush21dev"
for char in text:
    if char >= "0" and char <= "9":
        print("First digit found:", char)   # First digit found: 2
        break

# --- Example 12: Sum until negative number ---
# Simulating adding numbers until a "stop" value
numbers_as_strings = "10 20 30 -1 40 50"
total = 0
for part in numbers_as_strings.split():   # split string into parts
    value = int(part)
    if value < 0:
        break            # stop at negative number
    total += value
print("Total:", total)   # Total: 60  (10 + 20 + 30)

# ============================================
# TRY IT YOURSELF:
# 1. Use break to find the first number divisible by 7 in range(1, 100)
# 2. Use continue to print only numbers NOT divisible by 4 from 1-20
# 3. Use pass as a placeholder inside an if-else structure
# ============================================
