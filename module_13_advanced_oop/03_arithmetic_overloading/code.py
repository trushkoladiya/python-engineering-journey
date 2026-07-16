# ============================================
# MODULE 13 - SUBTOPIC 3: Arithmetic Operator Overloading
# ============================================

# Full set: __add__, __sub__, __mul__, __truediv__,
#           __floordiv__, __mod__, __pow__, __neg__, __abs__
# Plus reflected (__radd__, etc.) and in-place (__iadd__, etc.)

# =============================
# 1. COMPLETE ARITHMETIC CLASS
# =============================

# --- Example 1: A Vector class with full arithmetic ---
print("=== Vector Arithmetic ===")
print()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # --- Arithmetic operators ---
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):   # scalar multiplication
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __neg__(self):           # unary minus: -v
        return Vector(-self.x, -self.y)

    def __abs__(self):           # abs(v) → magnitude
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"  v1 = {v1}")
print(f"  v2 = {v2}")
print(f"  v1 + v2 = {v1 + v2}")
print(f"  v1 - v2 = {v1 - v2}")
print(f"  v1 * 3  = {v1 * 3}")
print(f"  -v1     = {-v1}")
print(f"  abs(v1) = {abs(v1):.2f}")
print()

# =============================
# 2. REFLECTED OPERATORS
# =============================

# --- Example 2: __radd__, __rmul__ for right-side operations ---
print("=== Reflected Operators ===")
print()

class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                return NotImplemented
            return Money(self.amount + other.amount, self.currency)
        if isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented

    def __radd__(self, other):
        # Called when: other + self (and other doesn't know how)
        # e.g., 50 + Money(100) → int.__add__ fails → Money.__radd__ called
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented

    def __rmul__(self, other):
        # Called when: 3 * Money(100) → int.__mul__ fails
        return self.__mul__(other)

    def __str__(self):
        return f"${self.amount:.2f} {self.currency}"

m = Money(100)

# Normal order
print(f"  Money(100) + Money(50) = {m + Money(50)}")
print(f"  Money(100) + 25 = {m + 25}")
print(f"  Money(100) * 3  = {m * 3}")

# Reflected order — other side is not Money
print(f"  25 + Money(100) = {25 + m}")       # calls __radd__
print(f"  3 * Money(100)  = {3 * m}")        # calls __rmul__
print()

# =============================
# 3. IN-PLACE OPERATORS
# =============================

# --- Example 3: __iadd__, __isub__ for +=, -= ---
print("=== In-Place Operators (+=, -=) ===")
print()

class Counter:
    def __init__(self, value=0):
        self.value = value

    def __iadd__(self, other):     # +=
        if isinstance(other, int):
            self.value += other
            return self
        if isinstance(other, Counter):
            self.value += other.value
            return self
        return NotImplemented

    def __isub__(self, other):     # -=
        if isinstance(other, int):
            self.value -= other
            return self
        return NotImplemented

    def __str__(self):
        return f"Counter({self.value})"

c = Counter(10)
print(f"  Start: {c}")

c += 5
print(f"  After += 5: {c}")

c += 3
print(f"  After += 3: {c}")

c -= 2
print(f"  After -= 2: {c}")

c2 = Counter(100)
c += c2
print(f"  After += Counter(100): {c}")
print()

# =============================
# 4. DIVISION AND MODULO
# =============================

# --- Example 4: __truediv__, __floordiv__, __mod__ ---
print("=== Division and Modulo ===")
print()

class Fraction:
    def __init__(self, numerator, denominator=1):
        self.num = numerator
        self.den = denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.den + other.num * self.den
            new_den = self.den * other.den
            return Fraction(new_num, new_den)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.den - other.num * self.den
            new_den = self.den * other.den
            return Fraction(new_num, new_den)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.den * other.den)
        return NotImplemented

    def __truediv__(self, other):       # /
        if isinstance(other, Fraction):
            return Fraction(self.num * other.den, self.den * other.num)
        return NotImplemented

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f"  {f1} + {f2} = {f1 + f2}")
print(f"  {f1} - {f2} = {f1 - f2}")
print(f"  {f1} * {f2} = {f1 * f2}")
print(f"  {f1} / {f2} = {f1 / f2}")
print()

# =============================
# 5. POWER OPERATOR
# =============================

# --- Example 5: __pow__ ---
print("=== Power Operator ===")
print()

class Number:
    def __init__(self, value):
        self.value = value

    def __pow__(self, other):       # **
        if isinstance(other, Number):
            return Number(self.value ** other.value)
        if isinstance(other, (int, float)):
            return Number(self.value ** other)
        return NotImplemented

    def __str__(self):
        return str(self.value)

n = Number(2)
print(f"  Number(2) ** 3     = {n ** 3}")
print(f"  Number(2) ** 10    = {n ** 10}")
print(f"  Number(3) ** Number(4) = {Number(3) ** Number(4)}")
print()

# =============================
# 6. PRACTICAL: COMPLETE MONEY CLASS
# =============================

# --- Example 6: Real-world numeric class ---
print("=== Complete Money Class ===")
print()

class Dollar:
    def __init__(self, amount):
        self.amount = round(amount, 2)

    def __add__(self, other):
        if isinstance(other, Dollar):
            return Dollar(self.amount + other.amount)
        if isinstance(other, (int, float)):
            return Dollar(self.amount + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Dollar):
            return Dollar(self.amount - other.amount)
        if isinstance(other, (int, float)):
            return Dollar(self.amount - other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Dollar(self.amount * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        return Dollar(-self.amount)

    def __abs__(self):
        return Dollar(abs(self.amount))

    def __str__(self):
        return f"${self.amount:.2f}"

    def __repr__(self):
        return f"Dollar({self.amount})"

# Demonstrate all operations
price = Dollar(29.99)
tax = Dollar(2.40)
discount = Dollar(5.00)

print(f"  Price:    {price}")
print(f"  Tax:      {tax}")
print(f"  Discount: {discount}")
print(f"  Subtotal: {price + tax}")
print(f"  After discount: {price + tax - discount}")
print(f"  Double:   {price * 2}")
print(f"  3 * tax:  {3 * tax}")            # reflected
print(f"  Negate:   {-price}")
print(f"  Abs(-$5): {abs(Dollar(-5))}")

# Sum a list of Dollar amounts
items = [Dollar(10.50), Dollar(25.00), Dollar(3.99), Dollar(15.75)]
total = Dollar(0)
for item in items:
    total += item
print(f"\n  Cart total: {total}")

# ============================================
# TRY IT YOURSELF:
# 1. Add __floordiv__ and __mod__ to the Fraction class
# 2. Create a 'Matrix2x2' class with __add__ and __mul__
# 3. Create a 'Duration' class (hours, minutes) with full arithmetic
# ============================================
