# ============================================
# MODULE 6 - SUBTOPIC 12: Copying Lists
# ============================================
import copy   # needed for deepcopy

# =============================
# 1. REFERENCE (NOT A COPY)
# =============================

# --- Example 1: Assignment creates a reference ---
a = [1, 2, 3]
b = a           # b and a point to the SAME list
b[0] = 999
print("a:", a)   # [999, 2, 3] — a also changed!
print("b:", b)   # [999, 2, 3]
print("Same object?", a is b)   # True

# --- Example 2: Visualize the reference ---
x = [10, 20, 30]
y = x
print(f"\nBefore: x={x}, y={y}")
y.append(40)
print(f"After y.append(40): x={x}, y={y}")
# Both show [10, 20, 30, 40]!

# =============================
# 2. SHALLOW COPY METHODS
# =============================

# --- Example 3: Copy with slice [:] ---
original = [1, 2, 3, 4, 5]
copy1 = original[:]
copy1[0] = 999
print(f"\nSlice copy:")
print(f"  Original: {original}")   # [1, 2, 3, 4, 5] — unchanged!
print(f"  Copy: {copy1}")          # [999, 2, 3, 4, 5]

# --- Example 4: Copy with .copy() ---
original = [1, 2, 3, 4, 5]
copy2 = original.copy()
copy2[0] = 888
print(f"\n.copy() method:")
print(f"  Original: {original}")   # unchanged
print(f"  Copy: {copy2}")

# --- Example 5: Copy with list() ---
original = [1, 2, 3, 4, 5]
copy3 = list(original)
copy3[0] = 777
print(f"\nlist() constructor:")
print(f"  Original: {original}")   # unchanged
print(f"  Copy: {copy3}")

# --- Example 6: All three methods produce the same result ---
original = [10, 20, 30]
c1 = original[:]
c2 = original.copy()
c3 = list(original)
print(f"\nAll equal? {c1 == c2 == c3}")   # True
print(f"Same as original? {c1 == original}")   # True
print(f"Same object? {c1 is original}")   # False

# =============================
# 3. SHALLOW COPY LIMITATION
# =============================

# --- Example 7: Shallow copy with nested lists ---
original = [[1, 2], [3, 4], [5, 6]]
shallow = original[:]

# Modifying an inner list affects both!
shallow[0][0] = 999
print(f"\nShallow copy problem:")
print(f"  Original: {original}")   # [[999, 2], [3, 4], [5, 6]] — changed!
print(f"  Shallow: {shallow}")     # [[999, 2], [3, 4], [5, 6]]

# --- Example 8: But replacing a whole row is safe ---
original = [[1, 2], [3, 4]]
shallow = original[:]
shallow[0] = [99, 99]   # replaces the reference, not the inner list
print(f"\nReplace whole row:")
print(f"  Original: {original}")   # [[1, 2], [3, 4]] — unchanged
print(f"  Shallow: {shallow}")     # [[99, 99], [3, 4]]

# =============================
# 4. DEEP COPY
# =============================

# --- Example 9: Deep copy for full independence ---
original = [[1, 2], [3, 4], [5, 6]]
deep = copy.deepcopy(original)

deep[0][0] = 999
print(f"\nDeep copy:")
print(f"  Original: {original}")   # [[1, 2], [3, 4], [5, 6]] — unchanged!
print(f"  Deep: {deep}")           # [[999, 2], [3, 4], [5, 6]]

# --- Example 10: Deep copy with complex nesting ---
data = [[1, [2, 3]], [4, [5, 6]]]
data_copy = copy.deepcopy(data)
data_copy[0][1][0] = 999
print(f"\nComplex nesting:")
print(f"  Original: {data}")      # unchanged
print(f"  Deep copy: {data_copy}")

# =============================
# 5. WHEN TO USE WHICH
# =============================

# --- Example 11: Simple list — shallow copy is fine ---
nums = [1, 2, 3, 4, 5]
backup = nums.copy()
nums.append(6)
print(f"\nSimple list backup:")
print(f"  Modified: {nums}")
print(f"  Backup: {backup}")   # still [1, 2, 3, 4, 5]

# --- Example 12: Nested list — need deep copy ---
matrix = [[1, 0], [0, 1]]
matrix_backup = copy.deepcopy(matrix)
matrix[0][0] = 99
print(f"\nNested list backup:")
print(f"  Modified: {matrix}")
print(f"  Backup: {matrix_backup}")   # still [[1, 0], [0, 1]]

# =============================
# 6. PRACTICAL PATTERNS
# =============================

# --- Example 13: Undo feature using copies ---
data = [10, 20, 30]
history = [data.copy()]   # save initial state

data.append(40)
history.append(data.copy())

data[0] = 999
history.append(data.copy())

print("\n--- History ---")
for i, state in enumerate(history):
    print(f"  Step {i}: {state}")

# Undo to step 1:
data = history[1].copy()
print(f"After undo: {data}")

# --- Example 14: Function-like pattern (safe modification) ---
original = [5, 3, 8, 1, 9]
working = original.copy()
working.sort()
print(f"\nOriginal preserved: {original}")
print(f"Sorted copy: {working}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a list, assign it to another variable, modify one — see what happens
# 2. Make a proper copy using .copy() and verify independence
# 3. Try shallow vs deep copy with a nested list [[1,2],[3,4]]
# ============================================
