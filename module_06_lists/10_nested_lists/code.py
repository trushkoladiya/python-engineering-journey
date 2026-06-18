# ============================================
# MODULE 6 - SUBTOPIC 10: Nested Lists (Deep)
# ============================================

# =============================
# 1. ACCESSING NESTED ELEMENTS
# =============================

# --- Example 1: Basic nested access ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Full matrix:", matrix)
print("Row 0:", matrix[0])         # [1, 2, 3]
print("Row 1:", matrix[1])         # [4, 5, 6]
print("matrix[0][1]:", matrix[0][1])  # 2
print("matrix[2][2]:", matrix[2][2])  # 9

# --- Example 2: Negative indexing in nested lists ---
print("\nLast row:", matrix[-1])          # [7, 8, 9]
print("Last element:", matrix[-1][-1])   # 9

# --- Example 3: Mixed nested structure ---
student = ["Trush", [90, 85, 95], "A"]
print(f"\nName: {student[0]}")
print(f"Scores: {student[1]}")
print(f"Best score: {student[1][2]}")
print(f"Grade: {student[2]}")

# =============================
# 2. MODIFYING NESTED STRUCTURES
# =============================

# --- Example 4: Change a nested element ---
grid = [[1, 2], [3, 4], [5, 6]]
print("\nBefore:", grid)
grid[1][0] = 99
print("After grid[1][0]=99:", grid)   # [[1, 2], [99, 4], [5, 6]]

# --- Example 5: Replace an entire row ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1] = [40, 50, 60]
print("\nReplaced row 1:", matrix)

# --- Example 6: Append to a nested list ---
data = [["Trush"], ["Rahul"], ["Priya"]]
data[0].append(21)
data[1].append(22)
data[2].append(23)
print("\nWith ages:", data)

# =============================
# 3. CREATING MATRICES
# =============================

# --- Example 7: Create a 3x3 grid of zeros ---
rows = 3
cols = 3
grid = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    grid.append(row)
print("\n3x3 zero grid:")
for row in grid:
    print(f"  {row}")

# --- Example 8: Create identity-like pattern ---
size = 4
grid = []
for i in range(size):
    row = []
    for j in range(size):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    grid.append(row)
print("\nDiagonal pattern:")
for row in grid:
    print(f"  {row}")

# =============================
# 4. ITERATING NESTED LISTS
# =============================

# --- Example 9: Print matrix row by row ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nMatrix:")
for row in matrix:
    for item in row:
        print(f"{item:>3}", end="")
    print()

# --- Example 10: Iterate with indices ---
matrix = [[10, 20], [30, 40], [50, 60]]
print("\nWith indices:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"  [{i}][{j}] = {matrix[i][j]}")

# --- Example 11: Sum all elements ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
for row in matrix:
    for item in row:
        total += item
print(f"\nSum of all elements: {total}")   # 45

# =============================
# 5. MATRIX OPERATIONS
# =============================

# --- Example 12: Sum each row ---
grades = [[85, 90, 78], [92, 88, 95], [70, 75, 80]]
students = ["Trush", "Rahul", "Priya"]
print("\n--- Grade Summary ---")
for i in range(len(grades)):
    row_sum = 0
    for grade in grades[i]:
        row_sum += grade
    avg = row_sum / len(grades[i])
    print(f"  {students[i]}: sum={row_sum}, avg={avg:.1f}")

# --- Example 13: Sum each column ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
num_cols = len(matrix[0])
print("\nColumn sums:")
for col in range(num_cols):
    col_sum = 0
    for row in matrix:
        col_sum += row[col]
    print(f"  Column {col}: {col_sum}")

# --- Example 14: Transpose a matrix ---
matrix = [[1, 2, 3], [4, 5, 6]]
rows = len(matrix)
cols = len(matrix[0])

transposed = []
for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transposed.append(new_row)

print("\nOriginal:")
for row in matrix:
    print(f"  {row}")
print("Transposed:")
for row in transposed:
    print(f"  {row}")

# =============================
# 6. PRACTICAL PATTERNS
# =============================

# --- Example 15: Tic-tac-toe board ---
board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]
print("\n--- Tic-Tac-Toe ---")
for row in board:
    print(" | ".join(row))
    print("-" * 9)

# --- Example 16: Find an element in a 2D list ---
matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
target = 50
print(f"\nSearching for {target}:")
found = False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(f"  Found at [{i}][{j}]")
            found = True
            break
    if found:
        break

# ============================================
# TRY IT YOURSELF:
# 1. Create a 4x4 matrix filled with increasing numbers (1-16)
# 2. Find the maximum element in a 2D list
# 3. Print a tic-tac-toe board with empty spaces
# ============================================
