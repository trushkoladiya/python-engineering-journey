# ============================================
# MODULE 2 - SUBTOPIC 6: Memory & Identity Basics
# ============================================

# --- Example 1: id() shows the identity ---
x = 42
print(id(x))  # unique number for this object

y = "hello"
print(id(y))  # different number

# --- Example 2: Same object, same id ---
a = "Python"
b = a  # b points to the same object as a
print(id(a))
print(id(b))
print(id(a) == id(b))  # True — same object

# --- Example 3: 'is' vs '==' ---
a = 256
b = 256
print(a == b)   # True — same value
print(a is b)   # True — Python caches small integers

# --- Example 4: Different objects, same value ---
a = 1000
b = 1000
print(a == b)   # True — same value
print(a is b)   # May be False — different objects

# --- Example 5: Immutability demo ---
x = 10
print(f"x = {x}, id = {id(x)}")
x = 20  # this creates a NEW object, doesn't change the old one
print(f"x = {x}, id = {id(x)}")  # different id!

# --- Example 6: Strings are immutable ---
name = "Trush"
first_id = id(name)
name = "Koladiya"  # new object
second_id = id(name)
print(first_id == second_id)  # False — different objects

# --- Example 7: Reference behavior ---
a = "hello"
b = a           # b references the same object
print(a is b)   # True

b = "world"     # b now points to a new object
print(a is b)   # False
print(a)        # "hello" — a is unchanged

# --- Example 8: None identity ---
x = None
y = None
print(x is y)    # True — there's only ONE None
print(id(x) == id(y))  # True

# ============================================
# TRY IT YOURSELF:
# 1. Compare id() of two variables with the same value
# 2. Reassign a variable and check if id() changes
# 3. Try 'is' vs '==' with different values
# ============================================
