# ============================================
# MODULE 12 - SUBTOPIC 5: Instance Methods
# ============================================

# Instance methods = functions that belong to a class.
# They use 'self' to access the object's data.

# =============================
# 1. BASIC INSTANCE METHODS
# =============================

# --- Example 1: Simple methods ---
print("=== Basic Instance Methods ===")
print()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def get_info(self):
        return f"{self.name}, age {self.age}"

buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

print(f"  {buddy.bark()}")
print(f"  {max_dog.bark()}")
print(f"  {buddy.get_info()}")
print(f"  {max_dog.get_info()}")
print()

# =============================
# 2. METHODS THAT MODIFY DATA
# =============================

# --- Example 2: Changing object state ---
print("=== Methods That Modify Data ===")
print()

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        if self.count > 0:
            self.count -= 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count

c = Counter()
print(f"  Start: {c.get_count()}")

c.increment()
c.increment()
c.increment()
print(f"  After 3 increments: {c.get_count()}")

c.decrement()
print(f"  After 1 decrement: {c.get_count()}")

c.reset()
print(f"  After reset: {c.get_count()}")
print()

# =============================
# 3. METHODS THAT RETURN VALUES
# =============================

# --- Example 3: Computing and returning results ---
print("=== Methods That Return Values ===")
print()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)

print(f"  Rectangle 1 ({r1.width}x{r1.height}):")
print(f"    Area: {r1.area()}")
print(f"    Perimeter: {r1.perimeter()}")
print(f"    Is square? {r1.is_square()}")
print()

print(f"  Rectangle 2 ({r2.width}x{r2.height}):")
print(f"    Area: {r2.area()}")
print(f"    Perimeter: {r2.perimeter()}")
print(f"    Is square? {r2.is_square()}")
print()

# =============================
# 4. METHODS WITH PARAMETERS
# =============================

# --- Example 4: Methods that take arguments ---
print("=== Methods with Parameters ===")
print()

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Amount must be positive!"

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive!"
        if amount > self.balance:
            return f"Insufficient funds! Balance: ${self.balance}"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

    def get_balance(self):
        return f"{self.owner}'s balance: ${self.balance}"

acc = BankAccount("Trush", 1000)
print(f"  {acc.get_balance()}")
print(f"  {acc.deposit(500)}")
print(f"  {acc.withdraw(200)}")
print(f"  {acc.withdraw(5000)}")
print(f"  {acc.get_balance()}")
print()

# =============================
# 5. METHODS CALLING OTHER METHODS
# =============================

# --- Example 5: Using self to call other methods ---
print("=== Methods Calling Other Methods ===")
print()

class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def summary(self):
        # This method calls the other two methods
        f = self.to_fahrenheit()
        k = self.to_kelvin()
        return f"{self.celsius}°C = {f}°F = {k}K"

temps = [0, 100, 37, -40]
for t in temps:
    converter = TemperatureConverter(t)
    print(f"  {converter.summary()}")
print()

# =============================
# 6. METHODS THAT RETURN BOOLEANS
# =============================

# --- Example 6: Checking conditions ---
print("=== Boolean Methods ===")
print()

class Password:
    def __init__(self, value):
        self.value = value

    def is_long_enough(self):
        return len(self.value) >= 8

    def has_digit(self):
        for char in self.value:
            if char.isdigit():
                return True
        return False

    def has_upper(self):
        for char in self.value:
            if char.isupper():
                return True
        return False

    def is_strong(self):
        return self.is_long_enough() and self.has_digit() and self.has_upper()

passwords = ["abc", "password", "Pass1234", "hello123", "STRONG1pass"]
for pwd in passwords:
    p = Password(pwd)
    print(f"  '{pwd}':")
    print(f"    Long enough: {p.is_long_enough()}, Has digit: {p.has_digit()}, "
          f"Has upper: {p.has_upper()}, Strong: {p.is_strong()}")
print()

# =============================
# 7. PRACTICAL: SHOPPING CART
# =============================

# --- Example 7: A complete class with multiple methods ---
print("=== Shopping Cart ===")
print()

class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return f"Removed '{name}'"
        return f"'{name}' not found"

    def get_total(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

    def item_count(self):
        return len(self.items)

    def show_cart(self):
        if not self.items:
            return f"  {self.owner}'s cart is empty"
        result = f"  {self.owner}'s cart ({self.item_count()} items):\n"
        for item in self.items:
            result += f"    - {item['name']}: ${item['price']:.2f}\n"
        result += f"    Total: ${self.get_total():.2f}"
        return result

cart = ShoppingCart("Trush")
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 29.99)
cart.add_item("Keyboard", 79.99)

print(cart.show_cart())
print()

cart.remove_item("Mouse")
print("  After removing Mouse:")
print(cart.show_cart())

# ============================================
# TRY IT YOURSELF:
# 1. Create a 'TodoList' class with methods:
#    add_task(task), complete_task(task), show_tasks()
# 2. Create a 'Calculator' class with methods:
#    add(n), subtract(n), multiply(n), reset(), get_result()
# ============================================
