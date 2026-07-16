# ============================================
# MODULE 13 - SUBTOPIC 2: Comparison Dunder Methods
# ============================================

# All six comparison operators can be customized:
#   __eq__ (==), __ne__ (!=), __lt__ (<), __gt__ (>), __le__ (<=), __ge__ (>=)

from functools import total_ordering

# =============================
# 1. ALL SIX COMPARISONS (MANUAL)
# =============================

# --- Example 1: Implementing all six ---
print("=== All Six Comparison Methods ===")
print()

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius == other.celsius

    def __ne__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius != other.celsius

    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius < other.celsius

    def __gt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius > other.celsius

    def __le__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius <= other.celsius

    def __ge__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius >= other.celsius

    def __repr__(self):
        return f"Temperature({self.celsius})"

    def __str__(self):
        return f"{self.celsius}°C"

t1 = Temperature(20)
t2 = Temperature(30)
t3 = Temperature(20)

print(f"  {t1} == {t2}? {t1 == t2}")
print(f"  {t1} == {t3}? {t1 == t3}")
print(f"  {t1} != {t2}? {t1 != t2}")
print(f"  {t1} <  {t2}? {t1 < t2}")
print(f"  {t1} >  {t2}? {t1 > t2}")
print(f"  {t1} <= {t3}? {t1 <= t3}")
print(f"  {t2} >= {t1}? {t2 >= t1}")
print()

# =============================
# 2. @total_ordering SHORTCUT
# =============================

# --- Example 2: Define only __eq__ and __lt__, get the rest free ---
print("=== @total_ordering Shortcut ===")
print()

@total_ordering
class Score:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __eq__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.points == other.points

    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.points < other.points

    def __str__(self):
        return f"{self.name}: {self.points}pts"

    def __repr__(self):
        return f"Score('{self.name}', {self.points})"

s1 = Score("Trush", 95)
s2 = Score("Rahul", 80)
s3 = Score("Charlie", 95)

# We only defined __eq__ and __lt__, but ALL comparisons work:
print(f"  {s1} == {s3}? {s1 == s3}")    # __eq__
print(f"  {s1} != {s2}? {s1 != s2}")    # auto from __eq__
print(f"  {s2} <  {s1}? {s2 < s1}")     # __lt__
print(f"  {s1} >  {s2}? {s1 > s2}")     # auto from __lt__ + __eq__
print(f"  {s2} <= {s1}? {s2 <= s1}")    # auto
print(f"  {s1} >= {s3}? {s1 >= s3}")    # auto
print()

# =============================
# 3. SORTING WITH COMPARISONS
# =============================

# --- Example 3: sorted(), min(), max() work with comparisons ---
print("=== Sorting and min/max ===")
print()

scores = [Score("Trush", 95), Score("Rahul", 80), Score("Charlie", 90),
          Score("Dave", 75), Score("Eve", 88)]

print("  Unsorted:")
for s in scores:
    print(f"    {s}")

scores.sort()
print("\n  Sorted (ascending):")
for s in scores:
    print(f"    {s}")

scores.sort(reverse=True)
print("\n  Sorted (descending):")
for s in scores:
    print(f"    {s}")

print(f"\n  Best:  {max(scores)}")
print(f"  Worst: {min(scores)}")
print()

# =============================
# 4. TYPE CHECKING WITH NotImplemented
# =============================

# --- Example 4: Graceful handling of wrong types ---
print("=== Type Checking ===")
print()

@total_ordering
class Weight:
    def __init__(self, kg):
        self.kg = kg

    def __eq__(self, other):
        if not isinstance(other, Weight):
            return NotImplemented
        return self.kg == other.kg

    def __lt__(self, other):
        if not isinstance(other, Weight):
            return NotImplemented
        return self.kg < other.kg

    def __str__(self):
        return f"{self.kg}kg"

w = Weight(70)

# Comparing with same type — works
print(f"  Weight(70) == Weight(70)? {w == Weight(70)}")
print(f"  Weight(70) == Weight(80)? {w == Weight(80)}")

# Comparing with different type — returns NotImplemented → False
print(f"  Weight(70) == 70? {w == 70}")
print(f"  Weight(70) == 'hello'? {w == 'hello'}")
print()

# =============================
# 5. MULTI-FIELD COMPARISON
# =============================

# --- Example 5: Comparing on multiple attributes ---
print("=== Multi-Field Comparison ===")
print()

@total_ordering
class Version:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def _as_tuple(self):
        return (self.major, self.minor, self.patch)

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._as_tuple() == other._as_tuple()

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._as_tuple() < other._as_tuple()

    def __str__(self):
        return f"v{self.major}.{self.minor}.{self.patch}"

    def __repr__(self):
        return f"Version({self.major}, {self.minor}, {self.patch})"

versions = [
    Version(2, 1, 0),
    Version(1, 9, 5),
    Version(2, 0, 1),
    Version(1, 9, 5),
    Version(3, 0, 0),
]

print("  Versions unsorted:")
for v in versions:
    print(f"    {v}")

versions.sort()
print("\n  Versions sorted:")
for v in versions:
    print(f"    {v}")

print(f"\n  v1.9.5 == v1.9.5? {Version(1,9,5) == Version(1,9,5)}")
print(f"  v2.0.1 >  v1.9.5? {Version(2,0,1) > Version(1,9,5)}")
print()

# =============================
# 6. PRACTICAL: PRIORITY QUEUE ITEM
# =============================

# --- Example 6: Items sorted by priority ---
print("=== Priority Items ===")
print()

@total_ordering
class Task:
    PRIORITY_MAP = {"high": 3, "medium": 2, "low": 1}

    def __init__(self, name, priority="medium"):
        self.name = name
        self.priority = priority

    def _priority_value(self):
        return self.PRIORITY_MAP.get(self.priority, 0)

    def __eq__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return self._priority_value() == other._priority_value()

    def __lt__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return self._priority_value() < other._priority_value()

    def __str__(self):
        return f"[{self.priority.upper()}] {self.name}"

tasks = [
    Task("Fix bug", "high"),
    Task("Write docs", "low"),
    Task("Code review", "medium"),
    Task("Deploy", "high"),
    Task("Clean up", "low"),
]

tasks.sort(reverse=True)    # highest priority first
print("  Tasks by priority:")
for task in tasks:
    print(f"    {task}")

# ============================================
# TRY IT YOURSELF:
# 1. Create a 'Date' class with year, month, day comparisons
# 2. Use @total_ordering with just __eq__ and __lt__
# 3. Sort a list of dates and find the earliest/latest
# ============================================
