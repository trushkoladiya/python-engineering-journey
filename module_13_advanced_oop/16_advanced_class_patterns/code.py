# ============================================
# MODULE 13 - SUBTOPIC 16: Advanced Class Patterns
# ============================================

# Fluent interfaces (method chaining) and immutable object design.

from collections import namedtuple

# =============================
# 1. FLUENT INTERFACE (METHOD CHAINING)
# =============================

# --- Example 1: Basic chaining ---
print("=== Method Chaining ===")
print()

class QueryBuilder:
    def __init__(self, table):
        self.table = table
        self._columns = "*"
        self._conditions = []
        self._order = None
        self._limit = None

    def select(self, columns):
        self._columns = columns
        return self    # return self for chaining

    def where(self, condition):
        self._conditions.append(condition)
        return self

    def order_by(self, column):
        self._order = column
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        query = f"SELECT {self._columns} FROM {self.table}"
        if self._conditions:
            query += " WHERE " + " AND ".join(self._conditions)
        if self._order:
            query += f" ORDER BY {self._order}"
        if self._limit:
            query += f" LIMIT {self._limit}"
        return query

# Chain it all together!
query = (QueryBuilder("users")
         .select("name, email")
         .where("age > 18")
         .where("active = true")
         .order_by("name")
         .limit(10)
         .build())

print(f"  {query}")
print()

# =============================
# 2. FLUENT HTML BUILDER
# =============================

# --- Example 2: Building HTML with chaining ---
print("=== Fluent HTML Builder ===")
print()

class HtmlElement:
    def __init__(self, tag):
        self.tag = tag
        self._classes = []
        self._attrs = {}
        self._content = ""

    def add_class(self, cls):
        self._classes.append(cls)
        return self

    def attr(self, key, value):
        self._attrs[key] = value
        return self

    def content(self, text):
        self._content = text
        return self

    def build(self):
        attrs = ""
        if self._classes:
            attrs += f' class="{" ".join(self._classes)}"'
        for k, v in self._attrs.items():
            attrs += f' {k}="{v}"'
        return f"<{self.tag}{attrs}>{self._content}</{self.tag}>"

html = (HtmlElement("div")
        .add_class("container")
        .add_class("dark")
        .attr("id", "main")
        .content("Hello World")
        .build())

print(f"  {html}")
print()

# =============================
# 3. IMMUTABLE OBJECTS
# =============================

# --- Example 3: Blocking modification after init ---
print("=== Immutable Object ===")
print()

class ImmutablePoint:
    def __init__(self, x, y):
        super().__setattr__("x", x)
        super().__setattr__("y", y)
        super().__setattr__("_frozen", True)

    def __setattr__(self, name, value):
        if getattr(self, "_frozen", False):
            raise AttributeError(
                f"Cannot modify '{name}': ImmutablePoint is frozen"
            )
        super().__setattr__(name, value)

    def __delattr__(self, name):
        raise AttributeError("Cannot delete from ImmutablePoint")

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"ImmutablePoint({self.x}, {self.y})"

p = ImmutablePoint(3, 4)
print(f"  {p}")
print(f"  p.x = {p.x}, p.y = {p.y}")

try:
    p.x = 10
except AttributeError as e:
    print(f"  Modify: {e}")

try:
    del p.x
except AttributeError as e:
    print(f"  Delete: {e}")
print()

# =============================
# 4. IMMUTABLE WITH NEW INSTANCES
# =============================

# --- Example 4: "Modify" by creating a new object ---
print("=== Immutable with New Instances ===")
print()

class FrozenVector:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)

    def __setattr__(self, name, value):
        raise AttributeError("FrozenVector is immutable")

    # "Modify" by returning a NEW object
    def move(self, dx, dy):
        return FrozenVector(self.x + dx, self.y + dy)

    def scale(self, factor):
        return FrozenVector(self.x * factor, self.y * factor)

    def __add__(self, other):
        return FrozenVector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"FrozenVector({self.x}, {self.y})"

v1 = FrozenVector(1, 2)
v2 = v1.move(3, 4)         # new object!
v3 = v1.scale(2)            # new object!

print(f"  v1 = {v1}")
print(f"  v1.move(3, 4) = {v2}")
print(f"  v1.scale(2) = {v3}")
print(f"  v1 unchanged = {v1}")
print()

# =============================
# 5. NAMED TUPLES
# =============================

# --- Example 5: Quick immutable data objects ---
print("=== Named Tuples ===")
print()

Point = namedtuple("Point", ["x", "y"])
Color = namedtuple("Color", ["r", "g", "b"])

p1 = Point(3, 4)
p2 = Point(1, 2)
c = Color(255, 128, 0)

print(f"  Point: {p1}")
print(f"  p1.x = {p1.x}, p1.y = {p1.y}")
print(f"  Color: {c}")
print(f"  c.r = {c.r}")

# Immutable!
try:
    p1.x = 10
except AttributeError as e:
    print(f"  Modify: {e}")

# Can unpack
x, y = p1
print(f"  Unpacked: x={x}, y={y}")
print()

# =============================
# 6. FLUENT CONFIGURATION
# =============================

# --- Example 6: Builder pattern for config ---
print("=== Fluent Configuration ===")
print()

class ServerConfig:
    def __init__(self):
        self._host = "localhost"
        self._port = 8080
        self._debug = False
        self._workers = 1

    def host(self, h):
        self._host = h
        return self

    def port(self, p):
        self._port = p
        return self

    def debug(self, d=True):
        self._debug = d
        return self

    def workers(self, w):
        self._workers = w
        return self

    def build(self):
        return {
            "host": self._host,
            "port": self._port,
            "debug": self._debug,
            "workers": self._workers,
        }

    def __str__(self):
        return str(self.build())

# Configure with chaining
config = (ServerConfig()
          .host("0.0.0.0")
          .port(3000)
          .debug()
          .workers(4)
          .build())

print(f"  Config: {config}")
print()

# =============================
# 7. PRACTICAL: PIPELINE
# =============================

# --- Example 7: Data processing pipeline ---
print("=== Data Pipeline ===")
print()

class Pipeline:
    def __init__(self, data):
        self.data = data

    def filter(self, func):
        self.data = [x for x in self.data if func(x)]
        return self

    def transform(self, func):
        self.data = [func(x) for x in self.data]
        return self

    def sort(self, reverse=False):
        self.data.sort(reverse=reverse)
        return self

    def limit(self, n):
        self.data = self.data[:n]
        return self

    def result(self):
        return self.data

numbers = list(range(1, 21))

result = (Pipeline(numbers)
          .filter(lambda x: x % 2 == 0)     # keep even
          .transform(lambda x: x ** 2)        # square them
          .sort(reverse=True)                  # descending
          .limit(5)                            # top 5
          .result())

print(f"  Input: {numbers}")
print(f"  Pipeline result: {result}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a fluent EmailBuilder with .to(), .subject(), .body()
# 2. Create an immutable Money class (amount, currency)
# 3. Create a Pipeline for string processing
# ============================================
