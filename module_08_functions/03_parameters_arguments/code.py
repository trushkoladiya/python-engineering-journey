# ============================================
# MODULE 8 - SUBTOPIC 3: Parameters & Arguments
# ============================================

# =============================
# 1. POSITIONAL PARAMETERS
# =============================

# --- Example 1: Single parameter ---
def greet(name):
    print(f"Hello, {name}!")

greet("Trush")
greet("Rahul")
greet("Charlie")

# --- Example 2: Two parameters ---
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

print()
add(3, 5)
add(10, 20)
add(100, 200)

# --- Example 3: Three parameters ---
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

print()
describe_person("Trush", 21, "Mumbai")
describe_person("Rahul", 30, "Delhi")

# =============================
# 2. DEFAULT PARAMETERS
# =============================

# --- Example 4: One default parameter ---
def greet_with_default(name="World"):
    print(f"Hello, {name}!")

print()
greet_with_default("Trush")   # Uses provided value
greet_with_default()           # Uses default "World"

# --- Example 5: Multiple defaults ---
def create_profile(name, age=0, city="Unknown"):
    print(f"  Name: {name}, Age: {age}, City: {city}")

print("\nProfiles:")
create_profile("Trush", 21, "Mumbai")
create_profile("Rahul", 30)
create_profile("Charlie")

# --- Example 6: Power function with default exponent ---
def power(base, exponent=2):
    result = base ** exponent
    print(f"{base}^{exponent} = {result}")

print()
power(5)        # 5^2 = 25
power(3, 3)     # 3^3 = 27
power(2, 10)    # 2^10 = 1024

# =============================
# 3. KEYWORD ARGUMENTS
# =============================

# --- Example 7: Using keyword arguments ---
def show_order(item, quantity, price):
    total = quantity * price
    print(f"  {item}: {quantity} x ${price:.2f} = ${total:.2f}")

print("\nOrders:")
show_order(item="Burger", quantity=2, price=8.99)
show_order(price=4.50, item="Coffee", quantity=3)   # Order doesn't matter

# --- Example 8: Keyword arguments for clarity ---
def send_message(to, subject, body):
    print(f"\n  To: {to}")
    print(f"  Subject: {subject}")
    print(f"  Body: {body}")

send_message(
    to="trushkoladiya.work@gmail.com",
    subject="Hello!",
    body="How are you?"
)

# =============================
# 4. MIXING ARGUMENT TYPES
# =============================

# --- Example 9: Positional + default ---
def format_name(first, last, title="Mr."):
    print(f"  {title} {first} {last}")

print("\nFormatted names:")
format_name("John", "Doe")
format_name("Jane", "Smith", "Dr.")
format_name("Trush", "Koladiya", "Mr.")

# --- Example 10: Positional + keyword ---
def calculate_price(price, tax_rate=0.10, discount=0):
    final = price * (1 + tax_rate) - discount
    print(f"  Price: ${price:.2f}, Tax: {tax_rate*100:.0f}%, "
          f"Discount: ${discount:.2f}, Final: ${final:.2f}")

print("\nPrice calculations:")
calculate_price(100)
calculate_price(100, tax_rate=0.18)
calculate_price(100, discount=10)
calculate_price(100, tax_rate=0.18, discount=15)

# =============================
# 5. PARAMETER vs ARGUMENT
# =============================

# --- Example 11: Understanding the difference ---
# Parameters: defined in the function header
# Arguments: values passed when calling

def multiply(x, y):      # x, y are PARAMETERS
    print(f"  {x} × {y} = {x * y}")

print("\nMultiplication:")
multiply(3, 4)            # 3, 4 are ARGUMENTS
multiply(7, 8)            # 7, 8 are ARGUMENTS

# --- Example 12: Using variables as arguments ---
width = 10
height = 5

def area(w, h):
    print(f"  Area: {w} × {h} = {w * h}")

print("\nArea calculation:")
area(width, height)

# =============================
# 6. PRACTICAL EXAMPLES
# =============================

# --- Example 13: Repeating text ---
def repeat_text(text, times=1):
    for i in range(times):
        print(f"  {text}")

print("\nRepeated text:")
repeat_text("Hello!")
repeat_text("Python!", 3)

# --- Example 14: Building a greeting card ---
def greeting_card(name, message="Happy Birthday!", border="*"):
    line = border * 30
    print(f"\n{line}")
    print(f"  Dear {name},")
    print(f"  {message}")
    print(f"{line}")

greeting_card("Trush")
greeting_card("Rahul", "Congratulations!", "=")

# ============================================
# TRY IT YOURSELF:
# 1. Create a function with 2 parameters that calculates area
# 2. Create a function with a default parameter
# 3. Call a function using keyword arguments
# ============================================
