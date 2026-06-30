# ============================================
# MODULE 8 - SUBTOPIC 13: Performance & Best Practices
# ============================================

# =============================
# 1. AVOID UNNECESSARY CALLS
# =============================

# --- Example 1: Store result instead of recalculating ---
def expensive_calculation(n):
    """Simulates a slow calculation."""
    total = 0
    for i in range(n):
        total = total + i * i
    return total

# ❌ Bad — calling twice for the same value
print("Bad approach:")
print(f"  Result: {expensive_calculation(1000)}")
print(f"  Double: {expensive_calculation(1000) * 2}")  # Calculated again!

# ✅ Good — store and reuse
print("\nGood approach:")
result = expensive_calculation(1000)
print(f"  Result: {result}")
print(f"  Double: {result * 2}")

# --- Example 2: Avoid len() in loop condition ---
names = ["Trush", "Rahul", "Charlie", "Diana"]

# ❌ Less Pythonic
print("\nUsing index:")
for i in range(len(names)):
    print(f"  {names[i]}")

# ✅ More Pythonic — direct iteration
print("\nDirect iteration:")
for name in names:
    print(f"  {name}")

# =============================
# 2. KEEP FUNCTIONS SMALL
# =============================

# --- Example 3: Breaking up a large function ---
# Instead of one big function, use several small ones

def validate_score(score):
    """Check if score is valid."""
    return 0 <= score <= 100

def calculate_grade(score):
    """Convert score to letter grade."""
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

def format_result(name, score, grade):
    """Format a student result string."""
    return f"  {name}: {score} ({grade})"

# Clean, composed usage
def process_student(name, score):
    """Process a single student's score."""
    if not validate_score(score):
        return f"  {name}: Invalid score ({score})"
    grade = calculate_grade(score)
    return format_result(name, score, grade)

students = [("Trush", 95), ("Rahul", 82), ("Charlie", -5), ("Diana", 67)]
print("\nStudent Results:")
for name, score in students:
    print(process_student(name, score))

# =============================
# 3. WRITE REUSABLE FUNCTIONS
# =============================

# --- Example 4: General vs specific ---
# ❌ Too specific
def greet_trush():
    print("Hello, Trush!")

# ✅ General and reusable
def greet(name, greeting="Hello"):
    """Greet anyone with any greeting."""
    print(f"  {greeting}, {name}!")

print("\nGreetings:")
greet("Trush")
greet("Rahul", "Hi")
greet("Charlie", "Welcome")

# --- Example 5: Reusable tax calculator ---
def calculate_total(price, tax_rate=0.18, discount=0):
    """Calculate final price with tax and discount."""
    taxed = price * (1 + tax_rate)
    final = taxed - discount
    return round(final, 2)

print(f"\nBasic: ${calculate_total(100)}")
print(f"With 5% tax: ${calculate_total(100, 0.05)}")
print(f"With discount: ${calculate_total(100, discount=10)}")

# =============================
# 4. MINIMIZE SIDE EFFECTS
# =============================

# --- Example 6: Pure function (no side effects) ---
def get_passing_students(students, threshold=60):
    """Return a new list of passing students."""
    passing = []
    for name, score in students:
        if score >= threshold:
            passing.append((name, score))
    return passing   # Returns new list, doesn't modify input

all_students = [("Trush", 95), ("Rahul", 45), ("Charlie", 72), ("Diana", 38)]
passed = get_passing_students(all_students)
print(f"\nAll: {all_students}")
print(f"Passed: {passed}")
print(f"Original unchanged: {all_students}")

# =============================
# 5. USE DEFAULT VALUES WISELY
# =============================

# --- Example 7: Smart defaults ---
def search(items, query, case_sensitive=False, max_results=10):
    """Search items with sensible defaults."""
    results = []
    for item in items:
        if case_sensitive:
            match = query in item
        else:
            match = query.lower() in item.lower()
        if match:
            results.append(item)
        if len(results) >= max_results:
            break
    return results

fruits = ["Apple", "Apricot", "Banana", "Avocado", "Blueberry"]
print(f"\nSearch 'a': {search(fruits, 'a')}")
print(f"Search 'A' (case): {search(fruits, 'A', case_sensitive=True)}")
print(f"Search 'a' (max 2): {search(fruits, 'a', max_results=2)}")

# =============================
# 6. MEANINGFUL FUNCTION NAMES
# =============================

# --- Example 8: Name tells what it does ---
def is_valid_email(email):
    """Check if email has basic valid format."""
    return "@" in email and "." in email

def count_words(text):
    """Count the number of words in a text."""
    return len(text.split())

def get_initials(full_name):
    """Get initials from a full name."""
    parts = full_name.split()
    return "".join(part[0].upper() for part in parts)

print(f"\nValid email: {is_valid_email('test@example.com')}")
print(f"Word count: {count_words('Hello World Python')}")
print(f"Initials: {get_initials('John Michael Doe')}")

# ============================================
# TRY IT YOURSELF:
# 1. Refactor a long function into 3 smaller ones
# 2. Make a specific function more general by adding parameters
# 3. Convert a function with side effects to a pure function
# ============================================
