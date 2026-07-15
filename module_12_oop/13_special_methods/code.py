# ============================================
# MODULE 12 - SUBTOPIC 13: Special (Dunder) Methods
# ============================================

# Dunder methods = double underscore methods (__method__)
# They define how objects behave with Python's built-in features.

# =============================
# 1. WITHOUT __str__
# =============================

# --- Example 1: The ugly default ---
print("=== Without __str__ ===")
print()

class DogBad:
    def __init__(self, name, age):
        self.name = name
        self.age = age

buddy_bad = DogBad("Buddy", 3)
print(f"  print(buddy_bad): {buddy_bad}")
print("  → Ugly memory address! Not useful.")
print()

# =============================
# 2. __str__ — HUMAN-READABLE
# =============================

# --- Example 2: Clean printing ---
print("=== __str__ ===")
print()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (age {self.age})"

buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

print(f"  print(buddy): {buddy}")
print(f"  print(max_dog): {max_dog}")
print(f"  str(buddy): {str(buddy)}")
print()

# =============================
# 3. __repr__ — DEVELOPER-READABLE
# =============================

# --- Example 3: Unambiguous representation ---
print("=== __repr__ ===")
print()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

laptop = Product("Laptop", 999.99)

print(f"  str(laptop):  {str(laptop)}")     # user-friendly
print(f"  repr(laptop): {repr(laptop)}")     # developer-friendly
print()

# =============================
# 4. __str__ vs __repr__
# =============================

# --- Example 4: In different contexts ---
print("=== str vs repr in Context ===")
print()

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student {self.name} (grade {self.grade})"

    def __repr__(self):
        return f"Student('{self.name}', '{self.grade}')"

s = Student("Trush", "A")

# str is used by print()
print(f"  print: {s}")

# repr is used in lists and debugging
students = [Student("Trush", "A"), Student("Rahul", "B")]
print(f"  In a list: {students}")   # uses __repr__ for list items
print()

# =============================
# 5. __len__
# =============================

# --- Example 5: Making len() work ---
print("=== __len__ ===")
print()

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"

p = Playlist("Road Trip")
p.add("Song A")
p.add("Song B")
p.add("Song C")

print(f"  {p}")
print(f"  len(p) = {len(p)}")
print()

# =============================
# 6. __contains__
# =============================

# --- Example 6: Making 'in' work ---
print("=== __contains__ ===")
print()

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, member):
        self.members.append(member)

    def __contains__(self, member):
        return member in self.members

    def __len__(self):
        return len(self.members)

    def __str__(self):
        return f"Team '{self.name}': {self.members}"

team = Team("Alpha")
team.add("Trush")
team.add("Rahul")
team.add("Charlie")

print(f"  {team}")
print(f"  'Trush' in team? {'Trush' in team}")     # True
print(f"  'Dave' in team? {'Dave' in team}")        # False
print()

# =============================
# 7. __eq__ AND __lt__
# =============================

# --- Example 7: Comparison operators ---
print("=== __eq__ and __lt__ ===")
print()

class Score:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __eq__(self, other):
        return self.points == other.points

    def __lt__(self, other):
        return self.points < other.points

    def __repr__(self):
        return f"Score('{self.name}', {self.points})"

    def __str__(self):
        return f"{self.name}: {self.points} pts"

s1 = Score("Trush", 95)
s2 = Score("Rahul", 87)
s3 = Score("Charlie", 95)

print(f"  {s1} == {s2}? {s1 == s2}")    # False
print(f"  {s1} == {s3}? {s1 == s3}")    # True (same points)
print(f"  {s2} < {s1}? {s2 < s1}")      # True
print()

# Sorting works with __lt__!
scores = [s1, s2, s3]
scores.sort()
print("  Sorted scores:")
for s in scores:
    print(f"    {s}")
print()

# =============================
# 8. PRACTICAL: COMPLETE CLASS
# =============================

# --- Example 8: A well-designed class with dunders ---
print("=== Complete Class with Dunders ===")
print()

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages

books = [
    Book("Python Basics", "John", 250),
    Book("Data Science", "Jane", 400),
    Book("Web Dev", "Rahul", 300),
    Book("Python Basics", "John", 250),   # same as first
]

print("  Books:")
for book in books:
    print(f"    {book} ({len(book)} pages)")

print()
print(f"  books[0] == books[3]? {books[0] == books[3]}")
print(f"  books[0] == books[1]? {books[0] == books[1]}")

books.sort()
print()
print("  Sorted by pages:")
for book in books:
    print(f"    {book} ({len(book)} pages)")

# ============================================
# TRY IT YOURSELF:
# 1. Create a 'Money' class with __str__, __repr__, __add__, __eq__
# 2. Create a 'TodoList' class with __len__, __contains__, __str__
# 3. Make your classes feel natural to use with print(), len(), in, etc.
# ============================================
