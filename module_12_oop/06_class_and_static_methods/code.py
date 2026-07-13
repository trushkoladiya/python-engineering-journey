# ============================================
# MODULE 12 - SUBTOPIC 6: Class Methods & Static Methods
# ============================================

# Instance method → uses self (works with one object)
# Class method    → uses cls  (works with the class)
# Static method   → uses neither (utility function in a class)

# =============================
# 1. REVIEW: INSTANCE METHOD
# =============================

# --- Example 1: Instance method (what you already know) ---
print("=== Instance Method (Review) ===")
print()

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):    # instance method — uses 'self'
        return f"{self.name} says: Woof!"

buddy = Dog("Buddy")
print(f"  {buddy.bark()}")
print()

# =============================
# 2. CLASS METHODS
# =============================

# --- Example 2: Basic class method ---
print("=== Class Methods ===")
print()

class Student:
    count = 0    # class attribute

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def get_info(self):          # instance method — uses self
        return f"Student: {self.name}"

    @classmethod
    def get_count(cls):          # class method — uses cls
        return f"Total students: {cls.count}"

s1 = Student("Trush")
s2 = Student("Rahul")
s3 = Student("Charlie")

print(f"  {s1.get_info()}")
print(f"  {s2.get_info()}")
print(f"  {Student.get_count()}")       # called on the class
print(f"  {s1.get_count()}")            # also works on an object
print()

# =============================
# 3. CLASS METHOD AS FACTORY
# =============================

# --- Example 3: Alternative constructors ---
print("=== Class Method as Factory ===")
print()

# A "factory" method creates objects in a different way

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Create a Person from birth year instead of age."""
        age = 2026 - birth_year
        return cls(name, age)     # cls(...) creates a new Person

    @classmethod
    def from_string(cls, data_string):
        """Create a Person from a string like 'Trush-21'."""
        name, age = data_string.split("-")
        return cls(name, int(age))

# Normal creation
p1 = Person("Trush", 21)

# Factory: from birth year
p2 = Person.from_birth_year("Rahul", 2000)

# Factory: from string
p3 = Person.from_string("Charlie-30")

print(f"  p1: {p1.name}, age {p1.age}")
print(f"  p2: {p2.name}, age {p2.age}")
print(f"  p3: {p3.name}, age {p3.age}")
print()

# =============================
# 4. STATIC METHODS
# =============================

# --- Example 4: Basic static method ---
print("=== Static Methods ===")
print()

class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Static methods are called on the class
print(f"  MathHelper.add(3, 5) = {MathHelper.add(3, 5)}")
print(f"  MathHelper.is_even(4) = {MathHelper.is_even(4)}")
print(f"  MathHelper.is_even(7) = {MathHelper.is_even(7)}")
print(f"  MathHelper.celsius_to_fahrenheit(100) = {MathHelper.celsius_to_fahrenheit(100)}")
print()

# =============================
# 5. STATIC METHOD IN A CLASS
# =============================

# --- Example 5: Static methods as helpers ---
print("=== Static Method as Helper ===")
print()

class Validator:
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    @staticmethod
    def is_valid_age(age):
        return isinstance(age, int) and 0 <= age <= 150

    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name.strip()) > 0

# Test validators
test_data = [
    ("trush@example.com", 21, "Trush"),
    ("invalid-email", -5, ""),
    ("rahul@test.org", 200, "Rahul"),
]

for email, age, name in test_data:
    print(f"  Email '{email}': valid={Validator.is_valid_email(email)}")
    print(f"  Age {age}: valid={Validator.is_valid_age(age)}")
    print(f"  Name '{name}': valid={Validator.is_valid_name(name)}")
    print()

# =============================
# 6. ALL THREE TOGETHER
# =============================

# --- Example 6: One class with all method types ---
print("=== All Three Method Types ===")
print()

class BankAccount:
    total_accounts = 0
    interest_rate = 0.05

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    # Instance method — works with THIS account
    def deposit(self, amount):
        self.balance += amount
        return f"{self.owner} deposited ${amount}. Balance: ${self.balance}"

    # Class method — works with the class
    @classmethod
    def get_total_accounts(cls):
        return f"Total accounts: {cls.total_accounts}"

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate
        return f"Interest rate set to {rate * 100}%"

    # Static method — utility helper
    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

acc1 = BankAccount("Trush", 1000)
acc2 = BankAccount("Rahul", 2000)

# Instance method
print(f"  {acc1.deposit(500)}")

# Class methods
print(f"  {BankAccount.get_total_accounts()}")
print(f"  {BankAccount.set_interest_rate(0.07)}")

# Static method
print(f"  Is $100 valid? {BankAccount.validate_amount(100)}")
print(f"  Is -50 valid? {BankAccount.validate_amount(-50)}")
print(f"  Is 'abc' valid? {BankAccount.validate_amount('abc')}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a 'Circle' class with:
#    - __init__(radius) as instance method
#    - area() as instance method
#    - from_diameter(d) as class method (creates from diameter)
#    - is_valid_radius(r) as static method
# ============================================
