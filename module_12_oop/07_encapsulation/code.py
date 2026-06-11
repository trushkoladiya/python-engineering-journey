# ============================================
# MODULE 12 - SUBTOPIC 7: Encapsulation
# ============================================

# Encapsulation = controlling access to object data.
# Protect attributes from being changed incorrectly.

# =============================
# 1. THE PROBLEM WITHOUT ENCAPSULATION
# =============================

# --- Example 1: No protection ---
print("=== Without Encapsulation ===")
print()

class BankAccountBad:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance    # public — anyone can change it!

acc = BankAccountBad("Trush", 1000)
print(f"  {acc.owner}: ${acc.balance}")

# Anyone can set an invalid balance!
acc.balance = -999999
print(f"  After bad change: ${acc.balance}")
print("  Problem: no validation!")
print()

# =============================
# 2. PUBLIC ATTRIBUTES
# =============================

# --- Example 2: Public = accessible everywhere ---
print("=== Public Attributes ===")
print()

class Person:
    def __init__(self, name, age):
        self.name = name   # public
        self.age = age     # public

p = Person("Trush", 21)
print(f"  name: {p.name}")    # direct access — OK
print(f"  age: {p.age}")      # direct access — OK
p.name = "Rahul"                # direct modification — OK
print(f"  Changed name: {p.name}")
print()

# =============================
# 3. PROTECTED ATTRIBUTES (_)
# =============================

# --- Example 3: Single underscore = "please don't touch" ---
print("=== Protected Attributes (_) ===")
print()

class Employee:
    def __init__(self, name, salary):
        self.name = name         # public
        self._salary = salary    # protected (convention)

    def get_salary(self):
        return self._salary

    def set_salary(self, amount):
        if amount >= 0:
            self._salary = amount
        else:
            print(f"    Invalid salary: {amount}")

emp = Employee("Trush", 50000)
print(f"  Name: {emp.name}")
print(f"  Salary (via getter): {emp.get_salary()}")

# You CAN still access _salary directly (it's just a convention!)
print(f"  Direct access: {emp._salary}")
print("  Note: _ is a hint, Python doesn't block it")
print()

# =============================
# 4. PRIVATE ATTRIBUTES (__)
# =============================

# --- Example 4: Double underscore = name mangling ---
print("=== Private Attributes (__) ===")
print()

class SecretAgent:
    def __init__(self, name, code):
        self.name = name
        self.__code = code    # private — name-mangled

    def get_code(self):
        return self.__code    # accessible inside the class

agent = SecretAgent("Bond", "007")
print(f"  Name: {agent.name}")
print(f"  Code (via method): {agent.get_code()}")

# Direct access fails!
try:
    print(agent.__code)
except AttributeError as e:
    print(f"  Direct __code access: AttributeError — {e}")

# Name mangling: Python renames __code to _SecretAgent__code
print(f"  Mangled name access: {agent._SecretAgent__code}")
print("  Note: __ makes it harder, not impossible")
print()

# =============================
# 5. GETTERS AND SETTERS
# =============================

# --- Example 5: Controlled access ---
print("=== Getters and Setters ===")
print()

class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    # Getter
    def get_name(self):
        return self._name

    def get_grade(self):
        return self._grade

    # Setter with validation
    def set_grade(self, grade):
        valid_grades = ["A", "B", "C", "D", "F"]
        if grade in valid_grades:
            self._grade = grade
            print(f"    Grade updated to {grade}")
        else:
            print(f"    Invalid grade: '{grade}'. Must be one of {valid_grades}")

s = Student("Trush", "B")
print(f"  Name: {s.get_name()}")
print(f"  Grade: {s.get_grade()}")

s.set_grade("A")       # valid
s.set_grade("Z")       # invalid — rejected
s.set_grade("F")       # valid

print(f"  Final grade: {s.get_grade()}")
print()

# =============================
# 6. ENCAPSULATED BANK ACCOUNT
# =============================

# --- Example 6: Full protection ---
print("=== Encapsulated Bank Account ===")
print()

class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self.__balance = balance    # private

    def get_owner(self):
        return self._owner

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. Balance: ${self.__balance}"
        return "Invalid amount!"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount!"
        if amount > self.__balance:
            return f"Insufficient funds! Balance: ${self.__balance}"
        self.__balance -= amount
        return f"Withdrew ${amount}. Balance: ${self.__balance}"

acc = BankAccount("Trush", 1000)
print(f"  Owner: {acc.get_owner()}")
print(f"  Balance: ${acc.get_balance()}")
print(f"  {acc.deposit(500)}")
print(f"  {acc.withdraw(200)}")
print(f"  {acc.withdraw(5000)}")
print(f"  {acc.deposit(-100)}")
print(f"  Final balance: ${acc.get_balance()}")
print()

# =============================
# 7. ALL ACCESS LEVELS TOGETHER
# =============================

# --- Example 7: Comparison ---
print("=== Access Levels Summary ===")
print()

class Demo:
    def __init__(self):
        self.public_var = "I'm public"          # anyone can use
        self._protected_var = "I'm protected"   # convention: internal
        self.__private_var = "I'm private"       # name-mangled

    def show_all(self):
        print(f"    public:    {self.public_var}")
        print(f"    protected: {self._protected_var}")
        print(f"    private:   {self.__private_var}")

d = Demo()
print("  From inside the class:")
d.show_all()
print()

print("  From outside the class:")
print(f"    d.public_var:    '{d.public_var}'")
print(f"    d._protected_var: '{d._protected_var}'")
try:
    print(f"    d.__private_var: '{d.__private_var}'")
except AttributeError:
    print(f"    d.__private_var: AttributeError (blocked!)")

# ============================================
# TRY IT YOURSELF:
# 1. Create a 'Password' class with a private __password attribute
# 2. Add get_password() that returns masked version ("****")
# 3. Add set_password(new_pass) with length validation (min 6 chars)
# 4. Add verify(attempt) that checks if attempt matches
# ============================================
