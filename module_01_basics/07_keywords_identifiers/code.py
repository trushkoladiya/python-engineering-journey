# ============================================
# MODULE 1 - SUBTOPIC 7: Keywords & Identifiers
# ============================================

# --- Example 1: Viewing all Python keywords ---
# Python has a built-in way to see all keywords
import keyword
print(keyword.kwlist)

# --- Example 2: How many keywords exist? ---
print("Total keywords:", len(keyword.kwlist))

# --- Example 3: Checking if a word is a keyword ---
print(keyword.iskeyword("if"))      # True — it's a keyword
print(keyword.iskeyword("hello"))   # False — not a keyword
print(keyword.iskeyword("class"))   # True
print(keyword.iskeyword("name"))    # False

# --- Example 4: Valid identifiers (variable names) ---
name = "Trush"          # ✅ starts with letter
_count = 10             # ✅ starts with underscore
age2 = 21               # ✅ has digits (but doesn't start with one)
my_variable = "hello"   # ✅ uses underscores
print(name, _count, age2, my_variable)

# --- Example 5: Invalid identifiers (would cause errors) ---
# 2name = "Koladiya" # ❌ starts with a digit
# my-var = 10        # ❌ has a hyphen
# my var = 10        # ❌ has a space
# class = "hello"    # ❌ class is a keyword

# --- Example 6: Case sensitivity ---
color = "red"
Color = "blue"
COLOR = "green"
print(color)   # red
print(Color)   # blue
print(COLOR)   # green
# All three are different variables!

# --- Example 7: Naming conventions (snake_case) ---
# ✅ Good Python style (snake_case)
user_name = "Trush"
total_score = 100
is_active = True

# ⚠️ Works but not recommended in Python
userName = "Koladiya"
totalScore = 200

print(user_name, total_score, is_active)

# --- Example 8: Underscore prefixed names ---
_private = "hidden"     # convention: "internal use"
__special = "very private"
print(_private)
print(__special)

# ============================================
# TRY IT YOURSELF:
# 1. Check if "for" is a keyword
# 2. Try creating a variable starting with a number (see error)
# 3. Create 3 variables using good snake_case naming
# ============================================
