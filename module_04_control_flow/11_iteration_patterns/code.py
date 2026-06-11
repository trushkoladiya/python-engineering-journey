# ============================================
# MODULE 4 - SUBTOPIC 11: Iteration Patterns
# ============================================

# ---- PATTERN 1: Counter-Based Loops ----
# Fixed number of iterations — you know how many times to loop

# --- Example 1: Simple counter with for ---
for i in range(5):
    print("Iteration", i + 1)
# Iteration 1, 2, 3, 4, 5

# --- Example 2: Counter with while ---
attempt = 1
while attempt <= 3:
    print("Attempt", attempt, "of 3")
    attempt += 1

# --- Example 3: Repeat an action N times ---
n = 4
for _ in range(n):    # _ means we don't use the variable
    print("Hello!")
# Prints "Hello!" 4 times


# ---- PATTERN 2: Condition-Based Loops ----
# Loop until a condition changes — unknown number of iterations

# --- Example 4: Halving until below 1 ---
value = 128.0
steps = 0
while value >= 1:
    print("Value:", value)
    value /= 2
    steps += 1
print("Took", steps, "steps to go below 1")

# --- Example 5: Collatz sequence (3n+1 problem) ---
n = 10
steps = 0
print("Collatz sequence starting from", n, ":")
while n != 1:
    print(n, end=" → ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1
print(n)   # prints the final 1
print("Steps:", steps)


# ---- PATTERN 3: Accumulator Pattern ----
# Build up a result across iterations

# --- Example 6: Sum accumulator ---
total = 0
for i in range(1, 11):
    total += i
print("Sum of 1-10:", total)       # 55

# --- Example 7: Product accumulator ---
product = 1
for i in range(1, 8):
    product *= i
print("7! =", product)            # 5040

# --- Example 8: String accumulator ---
result = ""
for i in range(1, 6):
    result += str(i) + " "
print("Numbers:", result)          # Numbers: 1 2 3 4 5

# --- Example 9: Counting accumulator ---
text = "Trush Koladiya loves Python!"
vowel_count = 0
for char in text:
    if char in "aeiouAEIOU":
        vowel_count += 1
print("Vowels in text:", vowel_count)   # 9

# --- Example 10: Max finder (accumulator pattern) ---
# Find the largest digit in a number
number = 59372
max_digit = 0
temp = number
while temp > 0:
    digit = temp % 10        # get last digit
    if digit > max_digit:
        max_digit = digit
    temp = temp // 10        # remove last digit
print("Largest digit in", number, ":", max_digit)   # 9


# ---- PATTERN 4: Iterating with Index ----
# Access both position and value

# --- Example 11: Index-based string iteration ---
word = "Trush"
for i in range(len(word)):
    print("Index", i, "→", word[i])
# Index 0 → T, Index 1 → r, etc.

# --- Example 12: Comparing adjacent characters ---
text = "aabbccdd"
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        print("Repeat at index", i, ":", text[i])
# Finds adjacent duplicate characters

# --- Example 13: Reverse iteration with index ---
word = "Trush"
for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")
print()   # hsurT

# --- Example 14: Building a reversed string ---
original = "Python"
reversed_str = ""
for i in range(len(original) - 1, -1, -1):
    reversed_str += original[i]
print("Original:", original)
print("Reversed:", reversed_str)    # nohtyP

# --- Example 15: Sum of even-indexed characters' ASCII values ---
text = "abcdef"
total = 0
for i in range(0, len(text), 2):    # step 2 — even indices only
    total += ord(text[i])
print("Sum of ASCII at even indices:", total)

# ============================================
# TRY IT YOURSELF:
# 1. Use the accumulator pattern to calculate the sum of squares (1² + 2² + ... + 10²)
# 2. Count how many uppercase letters are in a string using a counter
# 3. Reverse a number (e.g., 12345 → 54321) using while loop and accumulator
# ============================================
