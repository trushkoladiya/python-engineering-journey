# ============================================
# MODULE 2 - SUBTOPIC 2: Boolean Type
# ============================================

# --- Example 1: Boolean values ---
is_student = True
is_raining = False
print(is_student)        # True
print(is_raining)        # False
print(type(is_student))  # <class 'bool'>

# --- Example 2: Falsy values (become False) ---
print("--- Falsy values ---")
print(bool(False))   # False
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(""))      # False (empty string)
print(bool(None))    # False

# --- Example 3: Truthy values (become True) ---
print("--- Truthy values ---")
print(bool(True))     # True
print(bool(1))        # True
print(bool(42))       # True
print(bool(-1))       # True (negative is still non-zero)
print(bool(3.14))     # True
print(bool("hello"))  # True (non-empty string)
print(bool(" "))      # True (space is a character!)

# --- Example 4: Boolean with and ---
print("--- and ---")
print(True and True)    # True  — both must be True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# --- Example 5: Boolean with or ---
print("--- or ---")
print(True or True)     # True  — at least one must be True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# --- Example 6: Boolean with not ---
print("--- not ---")
print(not True)   # False
print(not False)  # True

# --- Example 7: Combining operations ---
a = True
b = False
print(a and not b)        # True and True → True
print(not a or b)         # False or False → False

# --- Example 8: Booleans are numbers ---
print("--- Booleans as numbers ---")
print(True + True)    # 2
print(True + 5)       # 6
print(False + 10)     # 10
print(True * 100)     # 100
print(False * 100)    # 0

# --- Example 9: Comparing bool type ---
print(type(True))     # <class 'bool'>
print(type(1))        # <class 'int'>
print(True == 1)      # True — same value
print(True is 1)      # False — different objects

# --- Example 10: Practical example ---
has_ticket = True
has_id = True
can_enter = has_ticket and has_id
print(f"Can Trush enter: {can_enter}")  # Can Trush enter: True

# ============================================
# TRY IT YOURSELF:
# 1. Test bool() on different values
# 2. Try: bool([]) and bool([1,2,3]) — what happens?
# 3. Combine True/False with and, or, not
# ============================================
