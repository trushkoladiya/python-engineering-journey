# ============================================
# MODULE 7 - SUBTOPIC 10: Set Operations (Core)
# ============================================

# =============================
# 1. add() — ADD A SINGLE ELEMENT
# =============================

# --- Example 1: Basic add ---
fruits = {"apple", "banana"}
print("Before:", fruits)
fruits.add("cherry")
print("After add:", fruits)

# --- Example 2: Adding duplicate has no effect ---
numbers = {1, 2, 3}
numbers.add(2)   # Already exists
print("\nAfter adding duplicate 2:", numbers)   # {1, 2, 3}

# --- Example 3: Building a set one element at a time ---
colors = set()
colors.add("red")
colors.add("green")
colors.add("blue")
print("\nBuilt set:", colors)

# =============================
# 2. update() — ADD MULTIPLE ELEMENTS
# =============================

# --- Example 4: Update with a list ---
fruits = {"apple", "banana"}
fruits.update(["cherry", "date", "elderberry"])
print("\nAfter update with list:", fruits)

# --- Example 5: Update with a tuple ---
numbers = {1, 2, 3}
numbers.update((4, 5, 6))
print("After update with tuple:", numbers)

# --- Example 6: Update with another set ---
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_a.update(set_b)
print("After update with set:", set_a)   # {1, 2, 3, 4, 5}

# --- Example 7: Update with a string ---
chars = {"a", "b"}
chars.update("cde")
print("After update with string:", chars)   # {'a', 'b', 'c', 'd', 'e'}

# =============================
# 3. remove() — ERROR IF NOT FOUND
# =============================

# --- Example 8: Basic remove ---
fruits = {"apple", "banana", "cherry", "date"}
print("\nBefore remove:", fruits)
fruits.remove("banana")
print("After remove 'banana':", fruits)

# --- Example 9: Remove raises error if missing ---
# Uncomment to see the error:
# fruits.remove("mango")   # KeyError: 'mango'
print("Removing missing element would cause KeyError")

# =============================
# 4. discard() — NO ERROR IF NOT FOUND
# =============================

# --- Example 10: Basic discard ---
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print("\nAfter discard 'banana':", fruits)

# --- Example 11: Discard missing element — no error ---
fruits.discard("mango")   # No error!
print("After discard 'mango' (not found):", fruits)

# --- Example 12: Comparing remove vs discard ---
test_set = {1, 2, 3}
print("\nUsing discard for missing element:")
test_set.discard(99)   # No error
print("  No error with discard!")

# Using remove for missing element would crash:
# test_set.remove(99)   # KeyError: 99

# =============================
# 5. pop() — REMOVE RANDOM ELEMENT
# =============================

# --- Example 13: Pop removes and returns an element ---
colors = {"red", "green", "blue", "yellow"}
print("\nBefore pop:", colors)
removed = colors.pop()
print(f"Removed: {removed}")
print(f"After pop: {colors}")

# --- Example 14: Pop from set until empty ---
nums = {10, 20, 30}
print("\nPopping all elements:")
while len(nums) > 0:
    item = nums.pop()
    print(f"  Popped: {item}, Remaining: {nums}")

# =============================
# 6. clear() — REMOVE ALL ELEMENTS
# =============================

# --- Example 15: Clear the entire set ---
animals = {"cat", "dog", "bird", "fish"}
print("\nBefore clear:", animals)
animals.clear()
print("After clear:", animals)   # set()
print("Length:", len(animals))    # 0

# =============================
# 7. PRACTICAL EXAMPLES
# =============================

# --- Example 16: Building a unique collection ---
seen_numbers = set()
data = [5, 3, 8, 3, 5, 1, 8, 3, 5, 9]
print("\nProcessing data:", data)

for num in data:
    if num not in seen_numbers:
        print(f"  New number: {num}")
        seen_numbers.add(num)
    else:
        print(f"  Duplicate: {num} (skipped)")

print("Unique numbers:", seen_numbers)

# --- Example 17: Safe removal pattern ---
items = {"pen", "pencil", "eraser", "ruler"}
to_remove = ["pencil", "marker", "eraser", "tape"]

print("\nRemoving items safely:")
for item in to_remove:
    if item in items:
        items.remove(item)
        print(f"  Removed: {item}")
    else:
        print(f"  Not found: {item}")

print("Remaining:", items)

# ============================================
# TRY IT YOURSELF:
# 1. Create a set and add 5 elements one by one
# 2. Try remove() and discard() on a missing element
# 3. Pop all elements from a set using a while loop
# ============================================
