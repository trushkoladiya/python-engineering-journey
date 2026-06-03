# ============================================
# MODULE 4 - SUBTOPIC 7: For Loop
# ============================================

# --- Example 1: Basic for loop with range ---
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# --- Example 2: range(start, stop) ---
for i in range(1, 6):
    print("Number:", i)
# Output: 1, 2, 3, 4, 5

# --- Example 3: range(start, stop, step) ---
# Even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)
# Output: 2, 4, 6, 8, 10

# --- Example 4: Counting down with negative step ---
for i in range(5, 0, -1):
    print(i)
print("Go!")
# Output: 5, 4, 3, 2, 1, Go!

# --- Example 5: Iterating over a string ---
word = "Trush"
for char in word:
    print(char)
# Output: T, r, u, s, h

# --- Example 6: Sum of numbers using for loop ---
total = 0
for num in range(1, 101):   # 1 to 100
    total += num
print("Sum of 1 to 100:", total)   # Sum of 1 to 100: 5050

# --- Example 7: Multiplication table with for ---
number = 9
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# --- Example 8: Counting characters in a string ---
text = "trush koladiya"
count = 0
for char in text:
    if char == "a":       # using if inside for loop
        count += 1
print("Number of 'a':", count)   # Number of 'a': 2

# --- Example 9: Step of 3 ---
for i in range(0, 30, 3):
    print(i, end=" ")
print()   # new line
# Output: 0 3 6 9 12 15 18 21 24 27

# --- Example 10: Using range with large step ---
for i in range(0, 101, 10):
    print(i, end=" ")
print()
# Output: 0 10 20 30 40 50 60 70 80 90 100

# --- Example 11: Factorial with for loop ---
n = 6
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial of", n, "is", factorial)   # 720

# --- Example 12: Power calculation ---
base = 3
exp = 4
result = 1
for _ in range(exp):    # _ means we don't need the variable
    result *= base
print(base, "**", exp, "=", result)   # 3 ** 4 = 81

# --- Example 13: Loop variable retains last value ---
for x in range(5):
    pass   # do nothing — just loop
print("After loop, x =", x)   # After loop, x = 4

# --- Example 14: Printing a simple pattern ---
for i in range(1, 6):
    print("*" * i)
# Output:
# *
# **
# ***
# ****
# *****

# ============================================
# TRY IT YOURSELF:
# 1. Print all odd numbers from 1 to 25 using range with step
# 2. Count how many vowels are in a string using a for loop
# 3. Calculate 2^10 using a for loop (without using **)
# ============================================
