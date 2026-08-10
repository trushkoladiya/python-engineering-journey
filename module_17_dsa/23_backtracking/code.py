# ============================================
# MODULE 17 - SUBTOPIC 23: Backtracking
# ============================================

# Backtracking: explore all solutions by building candidates
# incrementally, and abandoning paths that can't work.

# =============================
# 1. GENERATE ALL SUBSETS
# =============================

print("=== Generate All Subsets ===")
print()

def subsets(nums):
    """Generate all subsets using backtracking."""
    result = []

    def backtrack(start, current):
        result.append(current[:])    # record current subset

        for i in range(start, len(nums)):
            current.append(nums[i])         # choose
            backtrack(i + 1, current)        # explore
            current.pop()                    # undo (backtrack)

    backtrack(0, [])
    return result

data = [1, 2, 3]
all_subsets = subsets(data)
print(f"  Items: {data}")
print(f"  Subsets ({len(all_subsets)}):")
for s in all_subsets:
    print(f"    {s}")
print()

# =============================
# 2. GENERATE ALL PERMUTATIONS
# =============================

print("=== Generate All Permutations ===")
print()

def permutations(nums):
    """Generate all permutations using backtracking."""
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i + 1:])
            current.pop()    # backtrack

    backtrack([], nums)
    return result

data = [1, 2, 3]
all_perms = permutations(data)
print(f"  Items: {data}")
print(f"  Permutations ({len(all_perms)}):")
for p in all_perms:
    print(f"    {p}")
print()

# =============================
# 3. COMBINATIONS
# =============================

print("=== Generate Combinations ===")
print()

def combinations(nums, k):
    """Generate all combinations of size k."""
    result = []

    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return

        for i in range(start, len(nums)):
            # Pruning: not enough elements left
            if len(nums) - i < k - len(current):
                break

            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result

data = [1, 2, 3, 4, 5]
k = 3
combos = combinations(data, k)
print(f"  Choose {k} from {data}:")
print(f"  Combinations ({len(combos)}):")
for c in combos:
    print(f"    {c}")
print()

# =============================
# 4. N-QUEENS PROBLEM
# =============================

print("=== N-Queens Problem ===")
print()

def solve_n_queens(n):
    """Find all solutions to the N-Queens problem."""
    solutions = []

    def is_safe(board, row, col):
        """Check if placing a queen at (row, col) is safe."""
        # Check column
        for r in range(row):
            if board[r] == col:
                return False
            # Check diagonals
            if abs(board[r] - col) == abs(r - row):
                return False
        return True

    def backtrack(board, row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1    # backtrack

    board = [-1] * n
    backtrack(board, 0)
    return solutions

# Solve for n=4
solutions = solve_n_queens(4)
print(f"  4-Queens solutions: {len(solutions)}")
for sol in solutions:
    print(f"\n  Solution:")
    for row in range(4):
        line = ["♛" if col == sol[row] else "." for col in range(4)]
        print(f"    {' '.join(line)}")
print()

# Count solutions for different board sizes
print("  Solutions count for different N:")
for n in range(1, 9):
    count = len(solve_n_queens(n))
    print(f"    {n}-Queens: {count} solutions")
print()

# =============================
# 5. SUDOKU SOLVER (SIMPLIFIED 4×4)
# =============================

print("=== Sudoku Solver (4×4) ===")
print()

def solve_sudoku_4x4(board):
    """Solve a 4×4 Sudoku using backtracking."""

    def is_valid(board, row, col, num):
        # Check row
        if num in board[row]:
            return False
        # Check column
        for r in range(4):
            if board[r][col] == num:
                return False
        # Check 2×2 box
        box_r, box_c = (row // 2) * 2, (col // 2) * 2
        for r in range(box_r, box_r + 2):
            for c in range(box_c, box_c + 2):
                if board[r][c] == num:
                    return False
        return True

    def solve(board):
        for row in range(4):
            for col in range(4):
                if board[row][col] == 0:
                    for num in range(1, 5):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0    # backtrack
                    return False
        return True

    solve(board)
    return board

puzzle = [
    [1, 0, 0, 4],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [4, 0, 0, 2],
]

print("  Puzzle:")
for row in puzzle:
    print(f"    {row}")

solution = solve_sudoku_4x4([r[:] for r in puzzle])
print("\n  Solution:")
for row in solution:
    print(f"    {row}")
print()

# =============================
# 6. SUM COMBINATIONS
# =============================

print("=== Combination Sum ===")
print()

def combination_sum(candidates, target):
    """Find all combinations that sum to target (reuse allowed)."""
    result = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()

    candidates.sort()
    backtrack(0, [], target)
    return result

candidates = [2, 3, 6, 7]
target = 7
combos = combination_sum(candidates, target)
print(f"  Candidates: {candidates}, Target: {target}")
print(f"  Combinations:")
for c in combos:
    print(f"    {c} (sum={sum(c)})")
print()

# =============================
# 7. WORD SEARCH
# =============================

print("=== Word Search in Grid ===")
print()

def word_search(board, word):
    """Check if word exists in grid (horizontal/vertical adjacent)."""
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False

        # Mark as visited
        temp = board[r][c]
        board[r][c] = "#"

        # Explore 4 directions
        found = (backtrack(r + 1, c, idx + 1) or
                 backtrack(r - 1, c, idx + 1) or
                 backtrack(r, c + 1, idx + 1) or
                 backtrack(r, c - 1, idx + 1))

        board[r][c] = temp    # backtrack
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False

grid = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]

print("  Grid:")
for row in grid:
    print(f"    {' '.join(row)}")
print()

for word in ["ABCCED", "SEE", "ABCB", "FCC"]:
    # Make a copy for each search
    grid_copy = [row[:] for row in grid]
    found = word_search(grid_copy, word)
    result = "✓ found" if found else "✗ not found"
    print(f"  '{word}': {result}")
print()

# ============================================
# TRY IT YOURSELF:
# 1. Generate all valid parentheses combinations
#    for n pairs (e.g., n=3 → "()()()", "(()())", etc.)
# 2. Solve the "Letter Combinations of a Phone Number"
# 3. Find all paths from top-left to bottom-right
#    in a grid (only moving right or down)
# ============================================
