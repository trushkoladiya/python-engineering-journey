# ============================================
# MODULE 14 - SUBTOPIC 9: __init__.py
# ============================================

# __init__.py makes a directory a Python package.
# It runs automatically when the package is imported.

import os
import sys
import tempfile
import shutil

# =============================
# 1. EMPTY __init__.py
# =============================

print("=== Empty __init__.py ===")
print()

base_dir = tempfile.mkdtemp()

# Create package with empty __init__.py
pkg_dir = os.path.join(base_dir, "basic_pkg")
os.makedirs(pkg_dir)

with open(os.path.join(pkg_dir, "__init__.py"), "w") as f:
    f.write("")   # empty — just marks it as a package

with open(os.path.join(pkg_dir, "tools.py"), "w") as f:
    f.write('def hello():\n    return "Hello from tools!"\n')

sys.path.insert(0, base_dir)

import basic_pkg
print(f"  type(basic_pkg) = {type(basic_pkg)}")
print(f"  It's a package! (empty __init__.py is fine)")
print()

# =============================
# 2. __init__.py WITH CODE
# =============================

print("=== __init__.py with Initialization Code ===")
print()

# Create a new package with active __init__.py
pkg2_dir = os.path.join(base_dir, "active_pkg")
os.makedirs(pkg2_dir)

with open(os.path.join(pkg2_dir, "__init__.py"), "w") as f:
    f.write('''
# This code runs when the package is imported
PACKAGE_VERSION = "2.0"
PACKAGE_NAME = "active_pkg"

print(f"  [__init__.py] Package '{PACKAGE_NAME}' v{PACKAGE_VERSION} loaded!")
''')

print("  Importing 'active_pkg':")
import active_pkg

print(f"  active_pkg.PACKAGE_VERSION = '{active_pkg.PACKAGE_VERSION}'")
print(f"  active_pkg.PACKAGE_NAME = '{active_pkg.PACKAGE_NAME}'")
print()

# =============================
# 3. __init__.py FOR CONVENIENT IMPORTS
# =============================

print("=== __init__.py for Convenient Imports ===")
print()

# Create a shapes package
shapes_dir = os.path.join(base_dir, "shapes")
os.makedirs(shapes_dir)

# Create modules
with open(os.path.join(shapes_dir, "circle.py"), "w") as f:
    f.write('''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(r={self.radius})"
''')

with open(os.path.join(shapes_dir, "rectangle.py"), "w") as f:
    f.write('''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"
''')

with open(os.path.join(shapes_dir, "triangle.py"), "w") as f:
    f.write('''
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Triangle(b={self.base}, h={self.height})"
''')

# __init__.py imports key classes for convenience
with open(os.path.join(shapes_dir, "__init__.py"), "w") as f:
    f.write('''
# Import classes so users can do: from shapes import Circle
from .circle import Circle
from .rectangle import Rectangle
from .triangle import Triangle
''')

# Now users get a CLEAN import experience
from shapes import Circle, Rectangle, Triangle

c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)

print("  Without __init__.py imports:")
print("    from shapes.circle import Circle       ← verbose")
print("    from shapes.rectangle import Rectangle  ← verbose")
print()
print("  With __init__.py imports:")
print("    from shapes import Circle, Rectangle    ← clean!")
print()
print(f"  {c} → area = {c.area():.2f}")
print(f"  {r} → area = {r.area()}")
print(f"  {t} → area = {t.area():.1f}")
print()

# =============================
# 4. __all__ — CONTROLLING WILDCARD IMPORTS
# =============================

print("=== __all__ — Controlling 'from pkg import *' ===")
print()

# Create a module with __all__
tools_dir = os.path.join(base_dir, "mytools")
os.makedirs(tools_dir)

with open(os.path.join(tools_dir, "__init__.py"), "w") as f:
    f.write('''
# Only these names are exported with 'from mytools import *'
__all__ = ["public_func", "PUBLIC_CONST"]

def public_func():
    return "I am public!"

def _private_func():
    return "I am private!"

PUBLIC_CONST = "AVAILABLE"
_PRIVATE_CONST = "HIDDEN"
''')

from mytools import public_func, PUBLIC_CONST

print(f"  public_func() = '{public_func()}'")
print(f"  PUBLIC_CONST = '{PUBLIC_CONST}'")
print()

print("  __all__ = ['public_func', 'PUBLIC_CONST']")
print("  'from mytools import *' would only get these two")
print("  _private_func and _PRIVATE_CONST are excluded")
print()

# =============================
# 5. __init__.py PACKAGE METADATA
# =============================

print("=== Package Metadata in __init__.py ===")
print()

# Common pattern: define metadata in __init__.py
metadata_dir = os.path.join(base_dir, "mylib")
os.makedirs(metadata_dir)

with open(os.path.join(metadata_dir, "__init__.py"), "w") as f:
    f.write('''
"""MyLib — A demonstration library."""

__version__ = "1.0.0"
__author__ = "Python Learner"
__license__ = "MIT"
__all__ = ["__version__", "__author__"]
''')

import mylib

print(f"  mylib.__version__ = '{mylib.__version__}'")
print(f"  mylib.__author__ = '{mylib.__author__}'")
print(f"  mylib.__license__ = '{mylib.__license__}'")
print(f"  mylib.__doc__ = '{mylib.__doc__.strip()}'")
print()

# =============================
# 6. SUMMARY
# =============================

print("=== __init__.py Summary ===")
print()
print("  1. Empty __init__.py → just marks folder as package")
print("  2. With imports → provides convenient top-level access")
print("  3. With __all__ → controls 'from pkg import *'")
print("  4. With metadata → version, author, etc.")
print("  5. With code → runs on first import")
print()

# Cleanup
sys.path.remove(base_dir)
shutil.rmtree(base_dir)

# ============================================
# TRY IT YOURSELF:
# 1. Create a package with __init__.py that imports key classes
# 2. Add __all__ to control wildcard imports
# 3. Add version metadata to your __init__.py
# ============================================
