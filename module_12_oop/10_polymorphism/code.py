# ============================================
# MODULE 12 - SUBTOPIC 10: Polymorphism
# ============================================

# Polymorphism = same method name, different behavior.
# Each object decides how it responds to the same call.

# =============================
# 1. BASIC POLYMORPHISM
# =============================

# --- Example 1: Same method, different behavior ---
print("=== Basic Polymorphism ===")
print()

class Dog:
    def speak(self):
        return "Woof!"

    def move(self):
        return "Runs on 4 legs"

class Cat:
    def speak(self):
        return "Meow!"

    def move(self):
        return "Sneaks silently"

class Duck:
    def speak(self):
        return "Quack!"

    def move(self):
        return "Waddles and flies"

# Same method name, different results
animals = [Dog(), Cat(), Duck()]

for animal in animals:
    class_name = type(animal).__name__
    print(f"  {class_name}: {animal.speak()}, {animal.move()}")
print()

# =============================
# 2. POLYMORPHISM WITH INHERITANCE
# =============================

# --- Example 2: Through a common parent ---
print("=== Polymorphism via Inheritance ===")
print()

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Same function works with any shape!
def print_area(shape):
    print(f"  {shape.name}: area = {shape.area():.2f}")

shapes = [Rectangle(5, 3), Circle(4), Triangle(6, 8)]
for shape in shapes:
    print_area(shape)
print()

# =============================
# 3. POLYMORPHISM WITH FUNCTIONS
# =============================

# --- Example 3: A function that works with any compatible object ---
print("=== Polymorphic Function ===")
print()

class EmailNotifier:
    def send(self, message):
        return f"Email sent: {message}"

class SMSNotifier:
    def send(self, message):
        return f"SMS sent: {message}"

class PushNotifier:
    def send(self, message):
        return f"Push notification: {message}"

# This function works with ANY object that has send()
def notify(notifier, message):
    print(f"  {notifier.send(message)}")

notifiers = [EmailNotifier(), SMSNotifier(), PushNotifier()]
for n in notifiers:
    notify(n, "Hello!")
print()

# =============================
# 4. OPERATOR OVERLOADING: __add__
# =============================

# --- Example 4: Making + work with your objects ---
print("=== Operator Overloading: + ===")
print()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2      # calls p1.__add__(p2)

print(f"  {p1} + {p2} = {p3}")
print()

# =============================
# 5. OPERATOR OVERLOADING: __eq__ and __lt__
# =============================

# --- Example 5: Comparison operators ---
print("=== Operator Overloading: == and < ===")
print()

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __str__(self):
        return f"{self.celsius}°C"

t1 = Temperature(20)
t2 = Temperature(30)
t3 = Temperature(20)

print(f"  {t1} == {t2}? {t1 == t2}")   # False
print(f"  {t1} == {t3}? {t1 == t3}")   # True
print(f"  {t1} < {t2}? {t1 < t2}")     # True
print(f"  {t2} < {t1}? {t2 < t1}")     # False
print()

# =============================
# 6. OPERATOR OVERLOADING: __len__
# =============================

# --- Example 6: Making len() work ---
print("=== Operator Overloading: len() ===")
print()

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"

playlist = Playlist("My Favorites")
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

print(f"  {playlist}")
print(f"  Length: {len(playlist)}")   # calls __len__
print()

# =============================
# 7. OPERATOR OVERLOADING: __sub__
# =============================

# --- Example 7: Making - work ---
print("=== Operator Overloading: - ===")
print()

class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            return NotImplemented
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            return NotImplemented
        return Money(self.amount - other.amount, self.currency)

    def __str__(self):
        return f"${self.amount:.2f} {self.currency}"

m1 = Money(100)
m2 = Money(30)
m3 = m1 + m2
m4 = m1 - m2

print(f"  {m1} + {m2} = {m3}")
print(f"  {m1} - {m2} = {m4}")
print()

# =============================
# 8. PRACTICAL: POLYMORPHIC PAYMENT SYSTEM
# =============================

# --- Example 8: Real-world polymorphism ---
print("=== Payment System ===")
print()

class CreditCard:
    def __init__(self, number):
        self.number = number

    def process(self, amount):
        masked = "****" + self.number[-4:]
        return f"Charged ${amount:.2f} to credit card {masked}"

class PayPal:
    def __init__(self, email):
        self.email = email

    def process(self, amount):
        return f"Charged ${amount:.2f} to PayPal ({self.email})"

class BankTransfer:
    def __init__(self, account):
        self.account = account

    def process(self, amount):
        return f"Transferred ${amount:.2f} to bank account {self.account}"

# One function handles all payment methods!
def checkout(payment_method, amount):
    result = payment_method.process(amount)
    print(f"  {result}")

methods = [
    CreditCard("1234567890123456"),
    PayPal("trush@example.com"),
    BankTransfer("ACC-789012"),
]

for method in methods:
    checkout(method, 49.99)

# ============================================
# TRY IT YOURSELF:
# 1. Create a Vector class with __add__ and __sub__
# 2. Create different Logger classes (FileLogger, ConsoleLogger)
#    that all have a log(message) method
# 3. Write one function that works with any logger
# ============================================
