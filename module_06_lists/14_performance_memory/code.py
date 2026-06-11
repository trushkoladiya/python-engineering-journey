# ============================================
# MODULE 6 - SUBTOPIC 14: Performance & Memory Concepts
# ============================================
import time

# =============================
# 1. FAST OPERATIONS
# =============================

# --- Example 1: Index access is fast ---
big_list = list(range(100000))
# Accessing any index is equally fast:
print("First:", big_list[0])
print("Middle:", big_list[50000])
print("Last:", big_list[-1])
print("Index access: always fast regardless of position!\n")

# --- Example 2: append() is fast ---
nums = []
for i in range(10):
    nums.append(i)
print(f"Built with append: {nums}")
print("append() is fast — adds to the end\n")

# --- Example 3: pop() from end is fast ---
nums = [1, 2, 3, 4, 5]
last = nums.pop()
print(f"Popped {last} from end: {nums}")
print("pop() from end is fast\n")

# =============================
# 2. SLOW OPERATIONS
# =============================

# --- Example 4: insert(0) is slow — shifts all elements ---
# Demonstration with small list:
nums = [2, 3, 4, 5]
print("Before insert(0, 1):", nums)
nums.insert(0, 1)   # must shift 2,3,4,5 to make room
print("After insert(0, 1):", nums)
print("insert(0) must shift ALL elements → slow for large lists\n")

# --- Example 5: pop(0) is slow ---
nums = [1, 2, 3, 4, 5]
first = nums.pop(0)   # must shift 2,3,4,5 left
print(f"Popped {first} from start: {nums}")
print("pop(0) must shift ALL elements → slow for large lists\n")

# --- Example 6: 'in' checks every element ---
small = [1, 2, 3, 4, 5]
print(f"3 in {small}: {3 in small}")
print(f"99 in {small}: {99 in small}")
print("'in' must check each element one by one\n")

# =============================
# 3. TIMING COMPARISON
# =============================

# --- Example 7: append vs insert(0) timing ---
size = 50000

# Time append
start = time.time()
append_list = []
for i in range(size):
    append_list.append(i)
append_time = time.time() - start

# Time insert at beginning
start = time.time()
insert_list = []
for i in range(size):
    insert_list.insert(0, i)
insert_time = time.time() - start

print("--- Timing: append vs insert(0) ---")
print(f"  append() x{size}: {append_time:.4f}s")
print(f"  insert(0) x{size}: {insert_time:.4f}s")
print(f"  insert(0) is {insert_time/append_time:.0f}x slower!\n")

# =============================
# 4. BETTER APPROACHES
# =============================

# --- Example 8: Build at end + reverse (instead of insert at 0) ---
# ❌ Slow way
result_slow = []
for i in range(10):
    result_slow.insert(0, i)

# ✅ Fast way
result_fast = []
for i in range(10):
    result_fast.append(i)
result_fast.reverse()

print(f"Slow (insert at 0): {result_slow}")
print(f"Fast (append + reverse): {result_fast}")
print(f"Same result? {result_slow == result_fast}\n")

# --- Example 9: Use 'in' wisely ---
# For frequent lookups, consider using a set (covered later)
# For now, sort the list or limit the search
nums = list(range(1000))
target = 500

# Simple approach:
found = target in nums
print(f"Found {target}? {found}")

# If you know it's sorted, you can stop early:
nums_sorted = list(range(1000))
found = False
for num in nums_sorted:
    if num == target:
        found = True
        break
    if num > target:   # no need to check further
        break
print(f"Found with early exit? {found}\n")

# =============================
# 5. MEMORY AWARENESS
# =============================

# --- Example 10: Lists store references ---
# Each element in a list takes memory
small = [1, 2, 3]
big = list(range(1000000))
print(f"Small list: {len(small)} items")
print(f"Big list: {len(big)} items")
print("Tip: Don't create huge lists if you only need to iterate once\n")

# --- Example 11: range() is memory-efficient ---
# range() doesn't create a list — it generates numbers on demand
# list(range(n)) creates the full list in memory
print("range(1000000) → uses almost no memory (generator)")
print("list(range(1000000)) → stores 1 million items in memory")
print("Use range() in loops, convert to list only when needed\n")

# =============================
# 6. OPERATION SPEED SUMMARY
# =============================

# --- Example 12: Reference card ---
print("=" * 45)
print("LIST OPERATION SPEED REFERENCE")
print("=" * 45)
print(f"{'Operation':<25} {'Speed':<10}")
print("-" * 45)
operations = [
    ("list[i]", "Fast"),
    ("list[i] = x", "Fast"),
    ("append(x)", "Fast"),
    ("pop()", "Fast"),
    ("len(list)", "Fast"),
    ("insert(0, x)", "Slow"),
    ("pop(0)", "Slow"),
    ("remove(x)", "Slow"),
    ("x in list", "Slow*"),
    ("sort()", "Medium"),
    ("reverse()", "Fast"),
    ("list[a:b]", "Medium"),
]
for op, speed in operations:
    print(f"  {op:<25} {speed:<10}")
print("-" * 45)
print("* 'in' is fast for small lists, slow for large")
print("=" * 45)

# ============================================
# TRY IT YOURSELF:
# 1. Time how long it takes to append 100,000 items vs insert at 0
# 2. Compare building a reversed list with insert(0) vs append+reverse
# 3. Observe that range(1000000) in a for loop uses no extra memory
# ============================================
