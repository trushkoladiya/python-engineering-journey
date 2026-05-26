# ============================================
# MODULE 2 - SUBTOPIC 5: Type Checking
# ============================================

# --- Example 1: type() with different values ---
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>

# --- Example 2: Comparing types ---
name = "Trush"
age = 21
print(type(name) == str)    # True
print(type(age) == int)     # True

# --- Example 3: isinstance() basics ---
x = 42
print(isinstance(x, int))     # True
print(isinstance(x, float))   # False

# --- Example 4: isinstance() vs type() ---
value = True
print(isinstance(value, bool))   # True
print(isinstance(value, int))    # True  ← bool IS an int
print(type(value) == int)        # False ← strict match only

# --- Example 5: Checking multiple types ---
x = 3.14
print(isinstance(x, (int, float)))  # True — int OR float?

# --- Example 6: type() with expressions ---
print(type(10 + 5))      # <class 'int'>
print(type(10 + 5.0))    # <class 'float'>
print(type(10 == 5))     # <class 'bool'>

# --- Example 7: Checking None ---
x = None
print(x is None)                  # True ← simplest way
print(isinstance(x, type(None)))  # True

# ============================================
# TRY IT YOURSELF:
# 1. Check type of different values
# 2. Try isinstance(True, int) — why True?
# 3. Check if a value is int or float
# ============================================
