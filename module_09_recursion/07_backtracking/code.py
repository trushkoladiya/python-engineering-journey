# ============================================
# MODULE 9 - SUBTOPIC 7: Backtracking (Introduction)
# ============================================

# =============================
# 1. GENERATING ALL SUBSETS
# =============================

# --- Example 1: Subsets using include/exclude ---
def subsets(items, current=None, index=0, results=None):
    if current is None:
        current = []
    if results is None:
        results = []
    
    if index == len(items):
        results.append(current[:])   # Save a copy
        return results
    
    # Choice 1: INCLUDE items[index]
    current.append(items[index])
    subsets(items, current, index + 1, results)
    
    # Choice 2: EXCLUDE items[index] (BACKTRACK)
    current.pop()   # Undo the choice!
    subsets(items, current, index + 1, results)
    
    return results

print("Subsets of [1, 2, 3]:")
result = subsets([1, 2, 3])
for s in result:
    print(f"  {s}")
print(f"Total: {len(result)} subsets")

# --- Example 2: Subsets of strings ---
print(f"\nSubsets of ['a', 'b', 'c']:")
for s in subsets(["a", "b", "c"]):
    print(f"  {s}")

# =============================
# 2. GENERATING PERMUTATIONS
# =============================

# --- Example 3: All permutations ---
def permutations(items, current=None, results=None):
    if current is None:
        current = []
    if results is None:
        results = []
    
    if len(current) == len(items):
        results.append(current[:])
        return results
    
    for item in items:
        if item not in current:   # Only use unused items
            current.append(item)       # Choose
            permutations(items, current, results)   # Explore
            current.pop()              # Backtrack (undo!)
    
    return results

print(f"\nPermutations of [1, 2, 3]:")
for p in permutations([1, 2, 3]):
    print(f"  {p}")

# --- Example 4: Permutations of a word ---
print(f"\nPermutations of 'ABC':")
for p in permutations(list("ABC")):
    print(f"  {''.join(p)}")

# =============================
# 3. COMBINATIONS
# =============================

# --- Example 5: Choose k items from n ---
def combinations(items, k, start=0, current=None, results=None):
    if current is None:
        current = []
    if results is None:
        results = []
    
    if len(current) == k:
        results.append(current[:])
        return results
    
    for i in range(start, len(items)):
        current.append(items[i])           # Choose
        combinations(items, k, i + 1, current, results)  # Explore
        current.pop()                       # Backtrack
    
    return results

print(f"\nCombinations of [1,2,3,4] choose 2:")
for c in combinations([1, 2, 3, 4], 2):
    print(f"  {c}")

# =============================
# 4. BACKTRACKING WITH CONSTRAINTS
# =============================

# --- Example 6: Generate numbers with digits summing to target ---
def digit_sum_numbers(target, max_digits, current="", results=None):
    if results is None:
        results = []
    
    current_sum = sum(int(d) for d in current) if current else 0
    
    if current_sum == target and len(current) <= max_digits and current:
        results.append(current)
        return results
    
    if current_sum >= target or len(current) >= max_digits:
        return results   # Prune — no point going further
    
    for digit in range(1, 10):
        if current_sum + digit <= target:
            digit_sum_numbers(target, max_digits, current + str(digit), results)
    
    return results

print(f"\n2-digit numbers with digit sum = 5:")
nums = digit_sum_numbers(5, 2)
print(f"  {nums}")

# --- Example 7: Simple path finding ---
def find_paths(grid_rows, grid_cols, row=0, col=0, path=None):
    """Find all paths from top-left to bottom-right (only right/down)."""
    if path is None:
        path = []
    
    path.append((row, col))
    
    if row == grid_rows - 1 and col == grid_cols - 1:
        print(f"  {path}")
        path.pop()   # Backtrack
        return
    
    # Move right
    if col + 1 < grid_cols:
        find_paths(grid_rows, grid_cols, row, col + 1, path)
    
    # Move down
    if row + 1 < grid_rows:
        find_paths(grid_rows, grid_cols, row + 1, col, path)
    
    path.pop()   # Backtrack

print(f"\nAll paths in 2x3 grid (right/down only):")
find_paths(2, 3)

# ============================================
# TRY IT YOURSELF:
# 1. Generate all subsets of [1, 2, 3, 4] that sum to 5
# 2. Generate all 3-letter combinations from "ABCDE"
# 3. Count all paths in a 3x3 grid
# ============================================
