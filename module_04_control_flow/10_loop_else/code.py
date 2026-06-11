# ============================================
# MODULE 4 - SUBTOPIC 10: Loop with Else
# ============================================

# --- Example 1: Basic for-else ---
for i in range(5):
    print(i, end=" ")
else:
    print()   # new line
    print("Loop completed normally")
# Output: 0 1 2 3 4
#         Loop completed normally

# --- Example 2: for-else with break — else is SKIPPED ---
for i in range(5):
    if i == 3:
        print("Breaking at", i)
        break
    print(i, end=" ")
else:
    print("This won't print")    # skipped because break was hit
# Output: 0 1 2 Breaking at 3

# --- Example 3: Basic while-else ---
count = 0
while count < 3:
    print("count:", count)
    count += 1
else:
    print("While loop finished normally")
# Output: count: 0, count: 1, count: 2
#         While loop finished normally

# --- Example 4: while-else with break ---
num = 0
while num < 10:
    if num == 5:
        print("Stopped at 5")
        break
    num += 1
else:
    print("Loop completed")     # skipped — break was hit
# Output: Stopped at 5

# --- Example 5: Search pattern — found ---
target = 7
for n in range(1, 11):
    if n == target:
        print("Found", target, "!")
        break
else:
    print(target, "not found in range")
# Output: Found 7 !

# --- Example 6: Search pattern — NOT found ---
target = 15
for n in range(1, 11):
    if n == target:
        print("Found", target, "!")
        break
else:
    print(target, "not found in range")   # 15 not found in range

# --- Example 7: Checking for a prime number ---
num = 17
if num < 2:
    print(num, "is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not prime (divisible by", str(i) + ")")
            break
    else:
        print(num, "is prime!")    # 17 is prime!

# --- Example 8: Another prime check — not prime ---
num = 12
for i in range(2, num):
    if num % i == 0:
        print(num, "is not prime (divisible by", str(i) + ")")
        break
else:
    print(num, "is prime!")
# Output: 12 is not prime (divisible by 2)

# --- Example 9: Loop that never runs — else still runs ---
for i in range(0):            # range(0) is empty — loop body never runs
    print("Inside loop")
else:
    print("Else runs even when loop body never executed!")
# Output: Else runs even when loop body never executed!

# --- Example 10: Search for a character in a string ---
text = "trush koladiya"
search = "z"
for char in text:
    if char == search:
        print("Character '" + search + "' found!")
        break
else:
    print("Character '" + search + "' not found in text")
# Output: Character 'z' not found in text

# --- Example 11: Finding first divisible number ---
divisor = 7
for num in range(50, 100):
    if num % divisor == 0:
        print("First number divisible by", divisor, "in range 50-99:", num)
        break
else:
    print("No number divisible by", divisor, "found")
# Output: First number divisible by 7 in range 50-99: 56

# ============================================
# TRY IT YOURSELF:
# 1. Search for a letter in your name — print "found" or "not found"
# 2. Check if a given number (e.g., 29) is prime using for-else
# 3. Find the first number in range(100, 200) divisible by 13
# ============================================
