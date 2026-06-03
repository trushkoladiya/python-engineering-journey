# ============================================
# MODULE 4 - SUBTOPIC 6: While Loop
# ============================================

# --- Example 1: Basic while loop — counting up ---
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
# Output: Count: 1, Count: 2, Count: 3, Count: 4, Count: 5

# --- Example 2: Counting down ---
num = 5
while num >= 1:
    print(num)
    num -= 1
print("Go!")
# Output: 5, 4, 3, 2, 1, Go!

# --- Example 3: Sum of numbers 1 to 10 ---
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("Sum of 1 to 10:", total)    # Sum of 1 to 10: 55

# --- Example 4: Multiplication table ---
number = 7
multiplier = 1
while multiplier <= 10:
    result = number * multiplier
    print(number, "x", multiplier, "=", result)
    multiplier += 1

# --- Example 5: Condition checked before each iteration ---
x = 100
while x > 0:
    print(x)
    x -= 30
# Output: 100, 70, 40, 10
# When x becomes -20, condition fails → loop stops

# --- Example 6: Loop that never runs ---
y = 0
while y > 10:
    print("This never prints")   # condition is False from the start

# --- Example 7: Using while with strings ---
text = "Trush"
index = 0
while index < 5:
    print("Character:", text[index])
    index += 1
# Prints each character: T, r, u, s, h

# --- Example 8: Power calculation ---
base = 2
exponent = 8
result = 1
counter = 0
while counter < exponent:
    result *= base    # result = result * base
    counter += 1
print(base, "to the power of", exponent, "=", result)  # 256

# --- Example 9: Finding digits of a number ---
num = 12345
digit_count = 0
temp = num
while temp > 0:
    temp = temp // 10    # remove last digit
    digit_count += 1
print("Number of digits in", num, ":", digit_count)   # 5

# --- Example 10: Factorial calculation ---
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("Factorial of", n, "is", factorial)   # 120

# --- Example 11: Intentional infinite loop (commented out) ---
# while True:
#     print("This runs forever!")
#     # Press Ctrl+C to stop

# --- Example 12: Doubling until a limit ---
value = 1
while value < 1000:
    print(value)
    value *= 2
# Output: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512

# ============================================
# TRY IT YOURSELF:
# 1. Print all even numbers from 2 to 20 using a while loop
# 2. Calculate the sum of digits of a number (e.g., 1234 → 10)
# 3. Count how many times you can divide a number by 2 before it reaches 1
# ============================================
