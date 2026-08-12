# ============================================
# MODULE 18 - SUBTOPIC 2: Object Memory Model
# ============================================

# Every value in Python is an OBJECT in memory.
# Variables are NAMES (references) pointing to objects.

import sys
import gc

# =============================
# 1. VARIABLES ARE REFERENCES
# =============================

print("=== Variables Are References ===")
print()

x = 42
y = x  # y points to the SAME object

print(f"  x = {x}, id(x) = {id(x)}")
print(f"  y = {y}, id(y) = {id(y)}")
print(f"  Same object? {x is y}")
print()

# Assigning y = x does NOT copy the value
# Both x and y reference the same integer object

# =============================
# 2. id() — OBJECT IDENTITY
# =============================

print("=== id() Shows Memory Address ===")
print()

a = "hello"
b = "hello"
c = "world"

print(f"  a = '{a}', id = {id(a)}")
print(f"  b = '{b}', id = {id(b)}")
print(f"  c = '{c}', id = {id(c)}")
print(f"  a is b: {a is b}")  # Often True (string interning)
print(f"  a is c: {a is c}")  # False
print()

# Python may reuse objects for small integers and short strings
# This is called "interning" — an optimization

# =============================
# 3. INTEGER CACHING
# =============================

print("=== Integer Caching (-5 to 256) ===")
print()

# Python pre-creates integers from -5 to 256
# They are reused, not recreated

small1 = 100
small2 = 100
print(f"  small1 = 100, id = {id(small1)}")
print(f"  small2 = 100, id = {id(small2)}")
print(f"  Same object: {small1 is small2}")  # True
print()

big1 = 1000
big2 = 1000
print(f"  big1 = 1000, id = {id(big1)}")
print(f"  big2 = 1000, id = {id(big2)}")
print(f"  Same object: {big1 is big2}")  # May be False
print()

# =============================
# 4. REFERENCE COUNTING
# =============================

print("=== Reference Counting ===")
print()

# sys.getrefcount() shows how many references point to an object
# Note: calling getrefcount itself adds 1 temporary reference

data = [10, 20, 30]
print(f"  data = [10, 20, 30]")
print(f"  Reference count: {sys.getrefcount(data)}")

alias = data  # Another reference
print(f"  After alias = data: {sys.getrefcount(data)}")

another = data  # Yet another reference
print(f"  After another = data: {sys.getrefcount(data)}")

del alias  # Remove one reference
print(f"  After del alias: {sys.getrefcount(data)}")

del another  # Remove another reference
print(f"  After del another: {sys.getrefcount(data)}")
print()

# When reference count reaches 0, Python frees the memory

# =============================
# 5. MUTABLE vs IMMUTABLE REFERENCES
# =============================

print("=== Mutable vs Immutable References ===")
print()

# Immutable (int): reassignment creates a NEW object
x = 10
print(f"  x = 10, id = {id(x)}")

x = 20  # x now points to a DIFFERENT object
print(f"  x = 20, id = {id(x)}")
print()

# Mutable (list): modification changes the SAME object
my_list = [1, 2, 3]
original_id = id(my_list)
print(f"  my_list = [1, 2, 3], id = {id(my_list)}")

my_list.append(4)
print(f"  After append(4): {my_list}, id = {id(my_list)}")
print(f"  Same object: {id(my_list) == original_id}")
print()

# =============================
# 6. SHARED REFERENCES WITH MUTABLE OBJECTS
# =============================

print("=== Shared References (Mutable Danger) ===")
print()

list_a = [1, 2, 3]
list_b = list_a  # Both point to SAME list

list_b.append(4)

print(f"  list_a: {list_a}")  # [1, 2, 3, 4] — changed!
print(f"  list_b: {list_b}")  # [1, 2, 3, 4]
print(f"  Same object: {list_a is list_b}")
print()

# To avoid this, make a COPY
list_c = [10, 20, 30]
list_d = list_c.copy()  # Independent copy

list_d.append(40)
print(f"  list_c: {list_c}")  # [10, 20, 30] — unchanged
print(f"  list_d: {list_d}")  # [10, 20, 30, 40]
print(f"  Same object: {list_c is list_d}")
print()

# =============================
# 7. is vs ==
# =============================

print("=== is vs == ===")
print()

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"  a == b: {a == b}")  # True — same value
print(f"  a is b: {a is b}")  # False — different objects
print(f"  a is c: {a is c}")  # True — same object
print()

# Use == for value comparison (almost always)
# Use is for identity check (mainly with None)
print(f"  x = None")
x = None
print(f"  x is None: {x is None}")  # Correct way
print(f"  x == None: {x == None}")  # Works but not recommended
print()

# =============================
# 8. GARBAGE COLLECTION
# =============================

print("=== Garbage Collection ===")
print()

# Python's garbage collector handles circular references

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def __repr__(self):
        return f"Node({self.value})"

# Create circular reference
node_a = Node("A")
node_b = Node("B")
node_a.next_node = node_b  # A → B
node_b.next_node = node_a  # B → A (circular!)

print(f"  node_a: {node_a}, next: {node_a.next_node}")
print(f"  node_b: {node_b}, next: {node_b.next_node}")
print(f"  Circular: node_a.next_node.next_node is node_a: "
      f"{node_a.next_node.next_node is node_a}")
print()

# Delete references
del node_a
del node_b

# The garbage collector will find and clean the cycle
collected = gc.collect()
print(f"  Garbage collector freed {collected} objects")
print()

# =============================
# 9. gc MODULE BASICS
# =============================

print("=== gc Module ===")
print()

print(f"  GC enabled: {gc.isenabled()}")
print(f"  GC thresholds: {gc.get_threshold()}")
print(f"  GC counts: {gc.get_count()}")
print()

# Thresholds control when automatic collection runs
# (threshold0, threshold1, threshold2) — generations of objects
# Young objects are checked more frequently

# =============================
# 10. DEEP COPY vs SHALLOW COPY
# =============================

print("=== Deep Copy vs Shallow Copy ===")
print()

import copy

original = [[1, 2], [3, 4], [5, 6]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

# Modify a nested list
original[0].append(99)

print(f"  Original: {original}")
print(f"  Shallow copy: {shallow}")  # Also changed!
print(f"  Deep copy: {deep}")        # Not changed
print()

# Shallow copy: new outer list, but inner lists are shared
# Deep copy: everything is fully independent

# ============================================
# TRY IT YOURSELF:
# 1. Check id() of the same integer assigned to 
#    two different variables (try with 5, then 500)
# 2. Create a circular reference and use gc.collect()
# 3. Compare shallow vs deep copy with nested dicts
# ============================================
