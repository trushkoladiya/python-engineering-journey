# ============================================
# MODULE 3 - SUBTOPIC 6: Identity Operators
# ============================================

# --- Example 1: is — checks if same object ---
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)       # True  — same values
print(a is b)       # False — different objects in memory

# --- Example 2: Same object reference ---
a = [1, 2, 3]
b = a               # b now points to the SAME object as a
print(a is b)       # True  — same object
print(a == b)       # True  — same values too

# --- Example 3: Verifying with id() ---
a = [10, 20]
b = a
print(id(a))        # some number (e.g., 140234567890)
print(id(b))        # same number!
print(id(a) == id(b))  # True

c = [10, 20]
print(id(a) == id(c))  # False — different objects

# --- Example 4: is not ---
x = [1, 2]
y = [1, 2]
print(x is not y)   # True — different objects
print(x != y)       # False — same values!

# --- Example 5: Checking None with is ---
result = None
print(result is None)       # True ✅ (correct way)
print(result is not None)   # False

name = "Trush"
print(name is None)         # False
print(name is not None)     # True

# --- Example 6: Why is matters with None ---
# Always use "is" for None, not "=="
value = None
print(value is None)    # True ✅ — the right way
print(value == None)    # True — works but not recommended

# --- Example 7: Small integers are cached ---
# Python caches integers from -5 to 256
a = 100
b = 100
print(a is b)       # True — Python reuses the same object

a = 1000
b = 1000
print(a is b)       # Could be False — large numbers may not be cached

# --- Example 8: Strings behave similarly ---
s1 = "hello"
s2 = "hello"
print(s1 is s2)     # True — Python interns short strings
print(s1 == s2)     # True

# --- Example 9: Boolean identity ---
x = True
print(x is True)     # True
print(x is not False) # True

y = False
print(y is False)    # True

# --- Example 10: is with different types ---
a = 1
b = 1.0
print(a == b)        # True  — same value
print(a is b)        # False — different types, different objects

# ============================================
# TRY IT YOURSELF:
# 1. Create two lists with same values — are they "is"?
# 2. Assign one list to another — are they "is" now?
# 3. Check if a variable set to None "is None"
# ============================================
