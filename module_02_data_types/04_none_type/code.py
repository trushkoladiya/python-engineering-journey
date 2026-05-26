# ============================================
# MODULE 2 - SUBTOPIC 4: None Type
# ============================================

# --- Example 1: Creating a None variable ---
result = None
print(result)        # None
print(type(result))  # <class 'NoneType'>

# --- Example 2: None means "no value" ---
username = None  # Trush hasn't entered his name yet
print(f"Username: {username}")  # Username: None

# --- Example 3: print() returns None ---
value = print("hello")
print(value)  # None — because print() returns nothing

# --- Example 4: Checking for None with 'is' ---
x = None
print(x is None)       # True  ✅ correct way
print(x is not None)   # False

# --- Example 5: Why 'is' and not '==' ---
# 'is' checks identity (same object)
# '==' checks equality (same value)
# For None, always use 'is'
x = None
print(x is None)    # True ✅
print(x == None)    # True (works but not recommended)

# --- Example 6: None is falsy ---
print(bool(None))   # False
print(bool(0))      # False — 0 is also falsy
print(bool(""))     # False — empty string is also falsy
# None, 0, and "" are all falsy, but they are different!

# --- Example 7: None vs other falsy values ---
a = None
b = 0
c = ""
print(a is None)  # True
print(b is None)  # False — 0 is not None
print(c is None)  # False — "" is not None

# --- Example 8: Reassigning from None ---
score = None
print(f"Score: {score}")  # Score: None

score = 95
print(f"Score: {score}")  # Score: 95

# --- Example 9: None is a singleton ---
# There is only ONE None object in all of Python
a = None
b = None
print(a is b)    # True — they are the exact same object
print(id(a))
print(id(b))     # Same id!

# ============================================
# TRY IT YOURSELF:
# 1. Create a variable set to None and check its type
# 2. Try: is None the same as 0? the same as ""?
# 3. Assign None, then reassign a value — print both
# ============================================
