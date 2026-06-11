# ============================================
# MODULE 4 - SUBTOPIC 9: Nested Loops
# ============================================

# --- Example 1: Basic nested for loop ---
for i in range(3):
    for j in range(3):
        print("i =", i, "j =", j)
    print("---")
# Outer runs 3 times, inner runs 3 times each = 9 total prints

# --- Example 2: Multiplication table (1-5) ---
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")    # tab-separated
    print()                        # new line after each row
# Output:
# 1    2    3    4    5
# 2    4    6    8    10
# ...

# --- Example 3: Right triangle pattern ---
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

# --- Example 4: Inverted triangle ---
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

# --- Example 5: Number triangle ---
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# --- Example 6: Rectangle pattern ---
rows = 4
cols = 6
for i in range(rows):
    for j in range(cols):
        print("#", end=" ")
    print()
# Output:
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #

# --- Example 7: Nested while loop ---
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print(i, end=" ")
        j += 1
    print()
    i += 1
# Output:
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

# --- Example 8: Mixed for and while ---
for row in range(1, 4):
    col = 1
    while col <= row:
        print(row, end=" ")
        col += 1
    print()
# Output:
# 1
# 2 2
# 3 3 3

# --- Example 9: Finding pairs that sum to a target ---
target = 10
print("Pairs that sum to", target, ":")
for a in range(1, target):
    for b in range(a, target):
        if a + b == target:
            print(a, "+", b, "=", target)
# Output:
# 1 + 9 = 10
# 2 + 8 = 10
# 3 + 7 = 10
# 4 + 6 = 10
# 5 + 5 = 10

# --- Example 10: Counting total iterations ---
outer_count = 0
inner_count = 0
for i in range(5):
    outer_count += 1
    for j in range(3):
        inner_count += 1
print("Outer iterations:", outer_count)    # 5
print("Inner iterations:", inner_count)    # 15 (5 × 3)

# --- Example 11: break in nested loop (only breaks inner) ---
for i in range(3):
    print("Outer:", i)
    for j in range(5):
        if j == 2:
            break           # only breaks the inner loop
        print("  Inner:", j)
# Each outer iteration: inner runs for j = 0, 1 then breaks

# --- Example 12: Pyramid pattern ---
n = 5
for i in range(1, n + 1):
    # Print spaces
    for s in range(n - i):
        print(" ", end="")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Output:
#     *
#    ***
#   *****
#  *******
# *********

# ============================================
# TRY IT YOURSELF:
# 1. Print a 5x5 grid of coordinates: (0,0) (0,1) ... (4,4)
# 2. Create an inverted number triangle
# 3. Print a diamond pattern using nested loops
# ============================================
