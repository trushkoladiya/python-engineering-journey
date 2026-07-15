# ============================================
# MODULE 12 - SUBTOPIC 15: Real-World Patterns
# ============================================

# This brings it all together — real-world systems modeled with OOP.
# We use everything from Module 12: classes, methods, inheritance,
# encapsulation, composition, dunder methods, and design principles.

# ========================================================
# PATTERN 1: INVENTORY MANAGEMENT SYSTEM
# ========================================================

print("=" * 55)
print("  PATTERN 1: Inventory Management System")
print("=" * 55)
print()

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self._stock = stock

    def is_available(self):
        return self._stock > 0

    def sell(self, quantity):
        if quantity <= 0:
            return False
        if quantity > self._stock:
            return False
        self._stock -= quantity
        return True

    def restock(self, quantity):
        if quantity > 0:
            self._stock += quantity

    def get_stock(self):
        return self._stock

    def __str__(self):
        status = "In Stock" if self.is_available() else "Out of Stock"
        return f"{self.name}: ${self.price:.2f} ({self._stock} left) [{status}]"

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self._stock})"


class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        self._products[product.name] = product

    def find(self, name):
        return self._products.get(name)

    def get_available(self):
        result = []
        for product in self._products.values():
            if product.is_available():
                result.append(product)
        return result

    def total_value(self):
        total = 0
        for product in self._products.values():
            total += product.price * product.get_stock()
        return total

    def show(self):
        print("  Inventory:")
        for product in self._products.values():
            print(f"    {product}")
        print(f"    Total value: ${self.total_value():.2f}")


# Use the system
inventory = Inventory()
inventory.add_product(Product("Laptop", 999.99, 10))
inventory.add_product(Product("Mouse", 29.99, 50))
inventory.add_product(Product("Keyboard", 79.99, 30))
inventory.add_product(Product("Monitor", 449.99, 15))

inventory.show()
print()

# Sell some items
laptop = inventory.find("Laptop")
if laptop and laptop.sell(3):
    print(f"  Sold 3 laptops. Remaining: {laptop.get_stock()}")

mouse = inventory.find("Mouse")
if mouse and mouse.sell(10):
    print(f"  Sold 10 mice. Remaining: {mouse.get_stock()}")

print()
inventory.show()
print()

# ========================================================
# PATTERN 2: STUDENT GRADE TRACKER
# ========================================================

print("=" * 55)
print("  PATTERN 2: Student Grade Tracker")
print("=" * 55)
print()


class Grade:
    """Represents a single grade for a subject."""
    def __init__(self, subject, score):
        self.subject = subject
        self.score = max(0, min(100, score))   # clamp 0-100

    def letter(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"{self.subject}: {self.score} ({self.letter()})"

    def __repr__(self):
        return f"Grade('{self.subject}', {self.score})"


class StudentRecord:
    """Tracks grades for a single student."""
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self._grades = []

    def add_grade(self, subject, score):
        self._grades.append(Grade(subject, score))

    def average(self):
        if not self._grades:
            return 0
        total = 0
        for g in self._grades:
            total += g.score
        return total / len(self._grades)

    def highest(self):
        if not self._grades:
            return None
        best = self._grades[0]
        for g in self._grades[1:]:
            if g.score > best.score:
                best = g
        return best

    def is_passing(self):
        return self.average() >= 60

    def __str__(self):
        status = "PASS" if self.is_passing() else "FAIL"
        return f"{self.name} (ID: {self.student_id}) — Avg: {self.average():.1f} [{status}]"

    def show_grades(self):
        print(f"  {self}")
        for g in self._grades:
            print(f"    {g}")


# Use the system
students = [
    StudentRecord("Trush", "S001"),
    StudentRecord("Rahul", "S002"),
    StudentRecord("Charlie", "S003"),
]

# Add grades
students[0].add_grade("Math", 95)
students[0].add_grade("English", 88)
students[0].add_grade("Science", 92)

students[1].add_grade("Math", 72)
students[1].add_grade("English", 65)
students[1].add_grade("Science", 55)

students[2].add_grade("Math", 45)
students[2].add_grade("English", 50)
students[2].add_grade("Science", 40)

for student in students:
    student.show_grades()
    best = student.highest()
    if best:
        print(f"    Best: {best}")
    print()

# ========================================================
# PATTERN 3: SIMPLE BANKING SYSTEM
# ========================================================

print("=" * 55)
print("  PATTERN 3: Simple Banking System")
print("=" * 55)
print()


class Transaction:
    """Represents a single transaction."""
    def __init__(self, trans_type, amount, description=""):
        self.trans_type = trans_type   # "deposit" or "withdrawal"
        self.amount = amount
        self.description = description

    def __str__(self):
        sign = "+" if self.trans_type == "deposit" else "-"
        desc = f" ({self.description})" if self.description else ""
        return f"  {sign}${self.amount:.2f}{desc}"


class Account:
    """A bank account with transaction history."""
    _next_id = 1000

    def __init__(self, owner):
        Account._next_id += 1
        self.account_id = f"ACC-{Account._next_id}"
        self.owner = owner
        self._balance = 0.0
        self._transactions = []
        self._active = True

    def deposit(self, amount, description=""):
        if not self._active:
            return "Account is closed"
        if amount <= 0:
            return "Amount must be positive"
        self._balance += amount
        self._transactions.append(Transaction("deposit", amount, description))
        return f"Deposited ${amount:.2f}. Balance: ${self._balance:.2f}"

    def withdraw(self, amount, description=""):
        if not self._active:
            return "Account is closed"
        if amount <= 0:
            return "Amount must be positive"
        if amount > self._balance:
            return f"Insufficient funds (balance: ${self._balance:.2f})"
        self._balance -= amount
        self._transactions.append(Transaction("withdrawal", amount, description))
        return f"Withdrew ${amount:.2f}. Balance: ${self._balance:.2f}"

    def get_balance(self):
        return self._balance

    def close(self):
        self._active = False
        return f"Account {self.account_id} closed"

    def show_history(self):
        print(f"  Account {self.account_id} ({self.owner})")
        print(f"  Balance: ${self._balance:.2f}")
        if self._transactions:
            print(f"  Transactions:")
            for t in self._transactions:
                print(f"    {t}")

    def __str__(self):
        status = "Active" if self._active else "Closed"
        return f"{self.account_id}: {self.owner} — ${self._balance:.2f} [{status}]"


class Bank:
    """Manages multiple accounts."""
    def __init__(self, name):
        self.name = name
        self._accounts = {}

    def open_account(self, owner):
        account = Account(owner)
        self._accounts[account.account_id] = account
        return account

    def find_account(self, account_id):
        return self._accounts.get(account_id)

    def total_deposits(self):
        total = 0
        for acc in self._accounts.values():
            total += acc.get_balance()
        return total

    def show_all(self):
        print(f"  {self.name} — {len(self._accounts)} accounts")
        for acc in self._accounts.values():
            print(f"    {acc}")
        print(f"  Total deposits: ${self.total_deposits():.2f}")


# Use the system
bank = Bank("Python National Bank")

acc1 = bank.open_account("Trush")
acc2 = bank.open_account("Rahul")

print(f"  {acc1.deposit(5000, 'Initial deposit')}")
print(f"  {acc1.deposit(1500, 'Salary')}")
print(f"  {acc1.withdraw(800, 'Rent')}")
print()

print(f"  {acc2.deposit(3000, 'Initial deposit')}")
print(f"  {acc2.withdraw(500, 'Groceries')}")
print(f"  {acc2.withdraw(10000, 'Car')}")
print()

acc1.show_history()
print()
acc2.show_history()
print()

bank.show_all()

# ============================================
# KEY TAKEAWAYS:
#
# 1. Identify NOUNS → classes (Product, Student, Account)
# 2. Identify VERBS → methods (sell, deposit, withdraw)
# 3. Identify RELATIONSHIPS → composition (Bank has Accounts)
# 4. Each class has ONE responsibility
# 5. Objects interact through methods
# 6. Start simple — add complexity only when needed
#
# You now have the foundation to build real software!
# ============================================
